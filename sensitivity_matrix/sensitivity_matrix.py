#!/usr/bin/env python3
"""
Optical Alignment Sensitivity Matrix Tool
==========================================
Computes the sensitivity matrix A (8x5) that maps pose adjustments
(X, Y, Z, RX, RY) to Zernike coefficient changes (Z1..Z8), then
inverts it to produce guided adjustment movements.

Workflow
--------
1. Load a CSV of measurement data (see zernike_sampling_template.csv).
2. Build or refine the sensitivity matrix using central differences
   (recommended) or least-squares regression over all provided rows.
3. Given a current Zernike measurement, compute the recommended
   pose adjustment and print step-by-step movement guidance.

Usage
-----
    # Build matrix and adjust toward zero from a current measurement
    python sensitivity_matrix.py --data my_data.csv \
        --current 200,55,-23,-10,8,-13,-55,33 \
        --target  0,0,0,0,0,0,0,0 \
        --step-factor 0.3

    # Use least-squares mode (when > 11 rows are provided)
    python sensitivity_matrix.py --data my_data.csv \
        --current 200,55,-23,-10,8,-13,-55,33 \
        --method lstsq

    # Interactive mode: prompts for current Zernike values
    python sensitivity_matrix.py --data my_data.csv --interactive
"""

import argparse
import sys
import csv
import json
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

POSE_COLS = ["X (mm)", "Y (mm)", "Z (mm)", "RX", "RY"]
ZERNIKE_COLS = [f"Z{i} (nm)" for i in range(1, 9)]
RMS_COL = "Surface RMS (nm)"

# Central-difference group pairs: (positive group label, negative group label)
CD_PAIRS = [
    ("X+", "X-"),
    ("Y+", "Y-"),
    ("Z+", "Z-"),
    ("RX+", "RX-"),
    ("RY+", "RY-"),
]

# Default perturbation step sizes (used only when computing step from the CSV
# pose columns, not when computing from CD_PAIRS directly)
DEFAULT_STEPS = {
    "X (mm)": 0.02,
    "Y (mm)": 0.02,
    "Z (mm)": 0.05,
    "RX": 0.02,
    "RY": 0.02,
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_csv(filepath: str) -> list[dict]:
    """Return list of row dicts from a CSV file, skipping rows with no Group."""
    rows = []
    with open(filepath, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            group = row.get("Group", "").strip()
            if not group:
                continue
            rows.append(row)
    return rows


def _parse_float(val: str) -> float | None:
    """Parse a cell value to float; return None for blank/invalid."""
    v = val.strip() if val else ""
    if not v:
        return None
    try:
        return float(v)
    except ValueError:
        return None


def extract_zernike(row: dict) -> np.ndarray | None:
    """Return (8,) Zernike array for a row, or None if any value is missing."""
    vals = [_parse_float(row.get(col, "")) for col in ZERNIKE_COLS]
    if any(v is None for v in vals):
        return None
    return np.array(vals, dtype=float)


def extract_pose(row: dict) -> np.ndarray | None:
    """Return (5,) pose array for a row, or None if any value is missing."""
    vals = [_parse_float(row.get(col, "")) for col in POSE_COLS]
    if any(v is None for v in vals):
        return None
    return np.array(vals, dtype=float)


# ---------------------------------------------------------------------------
# Sensitivity matrix computation
# ---------------------------------------------------------------------------

def build_matrix_central_diff(rows: list[dict]) -> tuple[np.ndarray, list[str]]:
    """
    Build the 8×5 sensitivity matrix A using central differences.

    For each DOF pair (e.g. X+ / X-) found in the 'Group' column, compute:
        A[:, i] = (z_plus - z_minus) / (2 * delta)

    where delta is inferred from the pose column difference in the CSV.

    Returns
    -------
    A : ndarray of shape (8, 5)
    warnings : list of warning strings
    """
    # Index rows by Group label (take average if multiple rows per group)
    group_z: dict[str, list[np.ndarray]] = {}
    group_p: dict[str, list[np.ndarray]] = {}

    for row in rows:
        group = row.get("Group", "").strip()
        z = extract_zernike(row)
        p = extract_pose(row)
        if z is not None:
            group_z.setdefault(group, []).append(z)
        if p is not None:
            group_p.setdefault(group, []).append(p)

    # Average repeated measurements for the same group
    avg_z: dict[str, np.ndarray] = {g: np.mean(v, axis=0) for g, v in group_z.items()}
    avg_p: dict[str, np.ndarray] = {g: np.mean(v, axis=0) for g, v in group_p.items()}

    A = np.zeros((8, 5))
    warnings: list[str] = []

    for col_idx, (pos_group, neg_group) in enumerate(CD_PAIRS):
        z_plus = avg_z.get(pos_group)
        z_minus = avg_z.get(neg_group)
        p_plus = avg_p.get(pos_group)
        p_minus = avg_p.get(neg_group)

        if z_plus is None or z_minus is None:
            warnings.append(
                f"  [WARN] Missing Zernike data for group pair ({pos_group}, {neg_group}). "
                f"Column {POSE_COLS[col_idx]} will be zero in matrix."
            )
            continue

        if p_plus is not None and p_minus is not None:
            delta = (p_plus[col_idx] - p_minus[col_idx]) / 2.0
        else:
            delta = DEFAULT_STEPS[POSE_COLS[col_idx]]
            warnings.append(
                f"  [INFO] Pose data missing for ({pos_group}/{neg_group}); "
                f"using default step {delta} for {POSE_COLS[col_idx]}."
            )

        if abs(delta) < 1e-12:
            warnings.append(
                f"  [WARN] Step size is essentially zero for {POSE_COLS[col_idx]}; skipping."
            )
            continue

        A[:, col_idx] = (z_plus - z_minus) / (2.0 * delta)

    return A, warnings


def build_matrix_lstsq(rows: list[dict]) -> tuple[np.ndarray, list[str]]:
    """
    Build the 8×5 sensitivity matrix A by least-squares regression over all
    rows that have complete pose + Zernike data.

    Solves: Z_mat = P_mat @ A.T  =>  A.T = lstsq(P_mat, Z_mat)

    Requires a baseline (Base) row to be present; changes are computed
    relative to the mean of all Base rows.

    Returns
    -------
    A : ndarray of shape (8, 5)
    warnings : list of warning strings
    """
    warnings: list[str] = []

    # Collect baseline
    base_z_list = []
    base_p_list = []
    for row in rows:
        if row.get("Group", "").strip().lower() == "base":
            z = extract_zernike(row)
            p = extract_pose(row)
            if z is not None:
                base_z_list.append(z)
            if p is not None:
                base_p_list.append(p)

    if not base_z_list:
        warnings.append("  [WARN] No Base group rows found; using zeros as baseline.")
        z0 = np.zeros(8)
        p0 = np.zeros(5)
    else:
        z0 = np.mean(base_z_list, axis=0)
        p0 = np.mean(base_p_list, axis=0) if base_p_list else np.zeros(5)

    # Collect all non-base rows with complete data
    dP_list = []
    dZ_list = []
    for row in rows:
        if row.get("Group", "").strip().lower() == "base":
            continue
        z = extract_zernike(row)
        p = extract_pose(row)
        if z is None or p is None:
            continue
        dP_list.append(p - p0)
        dZ_list.append(z - z0)

    if len(dP_list) < 5:
        warnings.append(
            f"  [WARN] Only {len(dP_list)} non-base rows with complete data; "
            "least-squares may be poorly conditioned. Consider collecting more data."
        )

    if not dP_list:
        warnings.append("  [ERROR] No usable non-base rows; returning zero matrix.")
        return np.zeros((8, 5)), warnings

    P_mat = np.array(dP_list)   # shape (N, 5)
    Z_mat = np.array(dZ_list)   # shape (N, 8)

    # Solve P @ A.T ≈ Z  =>  A.T ≈ pinv(P) @ Z
    AT, residuals, rank, sv = np.linalg.lstsq(P_mat, Z_mat, rcond=None)
    A = AT.T  # shape (8, 5)

    cond = sv[0] / sv[-1] if sv[-1] > 1e-12 else float("inf")
    if cond > 1e4:
        warnings.append(
            f"  [WARN] Pose matrix condition number is large ({cond:.1e}). "
            "Results may be inaccurate; consider adding more independent measurements."
        )

    return A, warnings


# ---------------------------------------------------------------------------
# Adjustment computation
# ---------------------------------------------------------------------------

def compute_adjustment(
    A: np.ndarray,
    z_measured: np.ndarray,
    z_target: np.ndarray | None = None,
    step_factor: float = 0.3,
    max_steps: dict | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute recommended pose adjustment.

    Parameters
    ----------
    A          : (8, 5) sensitivity matrix
    z_measured : (8,) current Zernike measurements
    z_target   : (8,) target Zernike values (default: zeros)
    step_factor: damping factor λ ∈ (0, 1]
    max_steps  : dict mapping POSE_COLS index to max allowed absolute change

    Returns
    -------
    delta_p    : (5,) recommended pose change (before step_factor)
    delta_p_cmd: (5,) commanded pose change (after step_factor and clamping)
    """
    if z_target is None:
        z_target = np.zeros(8)

    error = z_target - z_measured  # shape (8,)

    # Pseudoinverse solution
    A_pinv = np.linalg.pinv(A)    # shape (5, 8)
    delta_p = A_pinv @ error       # shape (5,)

    # Apply step factor
    delta_p_cmd = step_factor * delta_p

    # Clamp to max steps if provided
    if max_steps is not None:
        for i, col in enumerate(POSE_COLS):
            limit = max_steps.get(col)
            if limit is not None:
                delta_p_cmd[i] = np.clip(delta_p_cmd[i], -abs(limit), abs(limit))

    return delta_p, delta_p_cmd


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_matrix(A: np.ndarray) -> None:
    """Pretty-print the 8×5 sensitivity matrix."""
    header = f"{'':10s}" + "".join(f"{c:>14s}" for c in POSE_COLS)
    print(header)
    print("-" * (10 + 14 * 5))
    for i, row in enumerate(A):
        label = f"Z{i+1:<9d}"
        vals = "".join(f"{v:14.4f}" for v in row)
        print(label + vals)
    print()


def print_guidance(
    z_measured: np.ndarray,
    z_target: np.ndarray,
    delta_p: np.ndarray,
    delta_p_cmd: np.ndarray,
    step_factor: float,
) -> None:
    """Print the adjustment guidance in a human-readable format."""
    print("=" * 60)
    print("  ADJUSTMENT GUIDANCE")
    print("=" * 60)

    print("\nCurrent Zernike measurement vs. target:")
    print(f"  {'Item':<8s} {'Measured (nm)':>15s} {'Target (nm)':>13s} {'Error (nm)':>12s}")
    print("  " + "-" * 50)
    for i in range(8):
        error = z_target[i] - z_measured[i]
        print(
            f"  Z{i+1:<7d} {z_measured[i]:>15.2f} {z_target[i]:>13.2f} {error:>12.2f}"
        )

    print(f"\nFull pseudoinverse solution Δp (step_factor not yet applied):")
    for i, col in enumerate(POSE_COLS):
        print(f"  {col:<10s}: {delta_p[i]:+.6f}")

    print(f"\nRecommended movement (step_factor = {step_factor}):")
    print("-" * 60)
    directions = []
    for i, col in enumerate(POSE_COLS):
        val = delta_p_cmd[i]
        if abs(val) < 1e-9:
            direction = "no change"
        else:
            direction = "positive (+)" if val > 0 else "negative (−)"
        unit = "mm" if "mm" in col else "rad/unit"
        directions.append((col, val, direction, unit))
        print(f"  {col:<10s}: {val:+.6f} {unit}   [{direction}]")

    print("\nStep-by-step instructions:")
    print("-" * 60)
    for col, val, direction, unit in directions:
        if abs(val) < 1e-9:
            print(f"  {col}: no adjustment needed")
        else:
            print(f"  Move {col} by {val:+.6f} {unit}  ({direction})")
    print("=" * 60)
    print()
    print("NOTES:")
    print("  1. Measure again after applying these adjustments.")
    print("  2. If RMS decreases, continue iterating.")
    print("  3. If RMS increases, reduce step_factor (try 0.1–0.2).")
    print("  4. Rebuild the sensitivity matrix when the optical state")
    print("     has changed significantly.")
    print()


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------

def interactive_session(A: np.ndarray, step_factor: float, max_steps: dict) -> None:
    """Repeatedly prompt for current Zernike values and print guidance."""
    print("\nEntering interactive adjustment mode.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        raw = input("Enter Z1..Z8 (comma-separated, nm): ").strip()
        if raw.lower() in ("quit", "exit", "q"):
            print("Exiting.")
            break
        try:
            vals = [float(v.strip()) for v in raw.split(",")]
        except ValueError:
            print("  Invalid input. Please enter 8 comma-separated numbers.\n")
            continue
        if len(vals) != 8:
            print(f"  Expected 8 values, got {len(vals)}.\n")
            continue

        z_meas = np.array(vals)
        target_raw = input(
            "Enter target Z1..Z8 (comma-separated, nm) [default: all zeros]: "
        ).strip()
        if target_raw == "":
            z_target = np.zeros(8)
        else:
            try:
                z_target = np.array([float(v.strip()) for v in target_raw.split(",")])
            except ValueError:
                print("  Invalid target. Using zeros.\n")
                z_target = np.zeros(8)

        delta_p, delta_p_cmd = compute_adjustment(
            A, z_meas, z_target, step_factor, max_steps
        )
        print_guidance(z_meas, z_target, delta_p, delta_p_cmd, step_factor)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute sensitivity matrix and produce optical alignment guidance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--data",
        required=True,
        metavar="CSV",
        help="Path to the measurement data CSV file.",
    )
    parser.add_argument(
        "--method",
        choices=["central_diff", "lstsq"],
        default="central_diff",
        help=(
            "Method to build the sensitivity matrix: "
            "'central_diff' (default) uses paired +/- perturbation rows; "
            "'lstsq' uses least-squares regression over all rows."
        ),
    )
    parser.add_argument(
        "--current",
        metavar="Z1,...,Z8",
        help="Comma-separated current Zernike measurements Z1..Z8 (nm).",
    )
    parser.add_argument(
        "--target",
        metavar="Z1,...,Z8",
        default="0,0,0,0,0,0,0,0",
        help="Comma-separated target Zernike values Z1..Z8 (nm). Default: all zeros.",
    )
    parser.add_argument(
        "--step-factor",
        type=float,
        default=0.3,
        metavar="LAMBDA",
        help="Damping factor λ ∈ (0, 1] applied to the pseudoinverse solution. Default: 0.3.",
    )
    parser.add_argument(
        "--max-steps",
        metavar="JSON",
        default=None,
        help=(
            'JSON string mapping DOF names to max absolute step, e.g. '
            '\'{"X (mm)": 0.05, "RX": 0.03}\''
        ),
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="After building the matrix, enter interactive adjustment mode.",
    )
    parser.add_argument(
        "--save-matrix",
        metavar="FILE",
        default=None,
        help="Save the computed sensitivity matrix to a CSV file.",
    )
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)

    # Load data
    data_path = Path(args.data)
    if not data_path.exists():
        print(f"ERROR: File not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    rows = load_csv(str(data_path))
    if not rows:
        print("ERROR: No valid rows found in CSV.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(rows)} rows from '{data_path}'.\n")

    # Build sensitivity matrix
    if args.method == "central_diff":
        print("Building sensitivity matrix via central differences...")
        A, warns = build_matrix_central_diff(rows)
    else:
        print("Building sensitivity matrix via least-squares regression...")
        A, warns = build_matrix_lstsq(rows)

    for w in warns:
        print(w)

    print("\nSensitivity matrix A  [rows = Zernike Z1..Z8, cols = X,Y,Z,RX,RY]")
    print("(units: nm per mm for X/Y/Z,  nm per degree/unit for RX/RY)\n")
    print_matrix(A)

    # Save matrix if requested
    if args.save_matrix:
        save_path = Path(args.save_matrix)
        with open(save_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["Zernike Item"] + POSE_COLS)
            for i, row in enumerate(A):
                writer.writerow([f"Z{i+1}"] + list(row))
        print(f"Sensitivity matrix saved to '{save_path}'.\n")

    # Parse max steps
    max_steps: dict | None = None
    if args.max_steps:
        try:
            max_steps = json.loads(args.max_steps)
        except json.JSONDecodeError as exc:
            print(f"WARNING: Could not parse --max-steps JSON: {exc}", file=sys.stderr)

    # Single-shot adjustment
    if args.current:
        try:
            z_meas = np.array([float(v.strip()) for v in args.current.split(",")])
        except ValueError:
            print("ERROR: --current values must be comma-separated numbers.", file=sys.stderr)
            sys.exit(1)
        if len(z_meas) != 8:
            print(
                f"ERROR: --current expects 8 values, got {len(z_meas)}.", file=sys.stderr
            )
            sys.exit(1)

        z_target = np.array([float(v.strip()) for v in args.target.split(",")])
        if len(z_target) != 8:
            print(
                f"ERROR: --target expects 8 values, got {len(z_target)}.", file=sys.stderr
            )
            sys.exit(1)

        delta_p, delta_p_cmd = compute_adjustment(
            A, z_meas, z_target, args.step_factor, max_steps
        )
        print_guidance(z_meas, z_target, delta_p, delta_p_cmd, args.step_factor)

    # Interactive mode
    if args.interactive:
        interactive_session(A, args.step_factor, max_steps or {})


if __name__ == "__main__":
    main()
