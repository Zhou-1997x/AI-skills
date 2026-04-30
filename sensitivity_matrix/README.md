# Optical Alignment Sensitivity Matrix Tool

> **计算机辅助装调 / Computer-Aided Optical Alignment**

This folder provides templates and a Python tool for collecting Zernike-based optical
measurement data, fitting a **sensitivity matrix A** (8 Zernike items × 5 pose DOFs),
and computing **recommended pose adjustments** to minimize wavefront error.

---

## Background 背景

In precision optical alignment you move five degrees of freedom (X, Y, Z, RX, RY) and
observe how eight Zernike aberration coefficients (Z1 – Z8) respond.  Near the operating
point the relationship is approximately **linear**:

```
Δz = A · Δp
```

| Symbol | Meaning |
|--------|---------|
| `Δp` | Pose change vector `[ΔX, ΔY, ΔZ, ΔRX, ΔRY]ᵀ` |
| `Δz` | Zernike change vector `[ΔZ1, …, ΔZ8]ᵀ` (nm) |
| **A** | 8 × 5 sensitivity matrix (nm / mm, nm / deg, etc.) |

Once **A** is known, the correction for any measured Zernike error is:

```
Δp_cmd = λ · A⁺ · (z_target − z_measured)
```

where `A⁺` is the Moore–Penrose pseudoinverse and `λ ∈ (0, 1]` is a damping step factor.

---

## Files 文件说明

| File | Description |
|------|-------------|
| `zernike_sampling_template.csv` | Blank 11-row sampling template (1 base + 10 perturbations) |
| `zernike_sampling_template_with_repeats.csv` | Same template with 3 repeats per point for noise reduction |
| `example_data.csv` | Example file pre-filled with the two positions from the design discussion |
| `sensitivity_matrix.py` | Python tool — builds matrix and prints adjustment guidance |

---

## Quick Start 快速上手

### 1. Install dependencies

```bash
pip install numpy
```

### 2. Collect calibration data

You need **at minimum** 11 measurement rows:

| Row | Group | What to do |
|-----|-------|------------|
| S00 | Base  | Record baseline pose (all zeros) and measure Z1–Z8, RMS |
| S01 | X+    | Move X by `+dX`, keep others at baseline, measure |
| S02 | X−    | Move X by `−dX`, keep others at baseline, measure |
| S03 | Y+    | Move Y by `+dY`, … |
| S04 | Y−    | Move Y by `−dY`, … |
| S05 | Z+    | Move Z by `+dZ`, … |
| S06 | Z−    | Move Z by `−dZ`, … |
| S07 | RX+   | Move RX by `+dRX`, … |
| S08 | RX−   | Move RX by `−dRX`, … |
| S09 | RY+   | Move RY by `+dRY`, … |
| S10 | RY−   | Move RY by `−dRY`, … |

Recommended perturbation step sizes (adjust for your system):

| DOF | Default step |
|-----|-------------|
| X   | 0.02 mm |
| Y   | 0.02 mm |
| Z   | 0.05 mm |
| RX  | 0.02 (deg or rad, be consistent) |
| RY  | 0.02 |

Copy `zernike_sampling_template.csv`, fill in the `Z1..Z8` and `Surface RMS` columns for
each row, and save it (e.g. as `my_measurements.csv`).

### 3. Build the matrix and get adjustment guidance

```bash
python sensitivity_matrix.py \
    --data my_measurements.csv \
    --current 200,55,-23,-10,8,-13,-55,33 \
    --target  0,0,0,0,0,0,0,0 \
    --step-factor 0.3
```

The tool prints:

1. The 8 × 5 sensitivity matrix **A**
2. The full pseudoinverse solution `Δp`
3. Damped movement commands `Δp_cmd`
4. Human-readable step-by-step instructions

### 4. Apply, measure, iterate

```
Measure Zernike → compute Δp_cmd → move stage → measure again → repeat
```

Stop when RMS reaches your tolerance.

---

## Command-Line Reference CLI参数

```
python sensitivity_matrix.py --help

Options:
  --data CSV          Path to the measurement data CSV file  [required]
  --method            'central_diff' (default) or 'lstsq'
  --current Z1,...,Z8 Current Zernike measurements (nm, comma-separated)
  --target  Z1,...,Z8 Target Zernike values (default: 0,0,0,0,0,0,0,0)
  --step-factor λ     Damping factor 0 < λ ≤ 1  (default: 0.3)
  --max-steps JSON    JSON dict of max absolute step per DOF, e.g.
                      '{"X (mm)": 0.05, "RX": 0.03}'
  --interactive       Enter interactive loop: prompt for measurements
                      and print guidance repeatedly
  --save-matrix FILE  Save computed matrix to a CSV file
```

### Matrix-building methods

| Method | When to use |
|--------|-------------|
| `central_diff` | You have paired +/− rows for every DOF (recommended, most accurate) |
| `lstsq` | You have many arbitrary-pose rows; fits by least-squares regression |

---

## CSV Format CSV格式

The data CSV must have these column headers (order does not matter):

```
Sample ID, Group, Status, X (mm), Y (mm), Z (mm), RX, RY,
Z1 (nm), Z2 (nm), Z3 (nm), Z4 (nm), Z5 (nm), Z6 (nm), Z7 (nm), Z8 (nm),
Surface RMS (nm), Note
```

- **Group** values used by `central_diff`: `Base`, `X+`, `X-`, `Y+`, `Y-`,
  `Z+`, `Z-`, `RX+`, `RX-`, `RY+`, `RY-`
- Rows with empty `Group` are ignored
- Missing Zernike cells in a row cause that row to be skipped

---

## Example Output 示例输出

```
Loaded 11 rows from 'my_measurements.csv'.

Building sensitivity matrix via central differences...

Sensitivity matrix A  [rows = Zernike Z1..Z8, cols = X,Y,Z,RX,RY]
(units: nm per mm for X/Y/Z,  nm per degree/unit for RX/RY)

              X (mm)        Y (mm)          Z (mm)            RX            RY
--------------------------------------------------------------------
Z1          -250.0000      80.0000       -40.0000      300.0000     -120.0000
Z2           ...
...

============================================================
  ADJUSTMENT GUIDANCE
============================================================

Current Zernike measurement vs. target:
  Item      Measured (nm)   Target (nm)   Error (nm)
  --------------------------------------------------
  Z1               200.00            0.00      -200.00
  Z2                55.00            0.00       -55.00
  ...

Recommended movement (step_factor = 0.3):
------------------------------------------------------------
  X (mm)  : +0.045000 mm   [positive (+)]
  Y (mm)  : -0.030000 mm   [negative (−)]
  Z (mm)  : +0.096000 mm   [positive (+)]
  RX      : -0.036000      [negative (−)]
  RY      : +0.120000      [positive (+)]

Step-by-step instructions:
------------------------------------------------------------
  Move X (mm) by +0.045000 mm  (positive (+))
  Move Y (mm) by -0.030000 mm  (negative (−))
  Move Z (mm) by +0.096000 mm  (positive (+))
  Move RX by -0.036000 rad/unit  (negative (−))
  Move RY by +0.120000 rad/unit  (positive (+))
```

---

## Tips and Best Practices 使用建议

1. **Repeat each point 2–3 times** and average to reduce noise.
2. **Lock all other DOFs** when perturbing a single one.
3. **Keep step sizes within the linear region**: too small → noise dominates;
   too large → nonlinearity.
4. **Use `step_factor = 0.2–0.5`** in practice; never apply the full correction
   in one shot.
5. **Rebuild the matrix** if the optical state has drifted substantially.
6. **Use RMS** only as a convergence check, not as the primary inversion signal.
7. When the system is near the optimum, reduce the step factor to avoid over-shooting.

---

## Mathematical Summary 数学原理

### Sensitivity matrix (central differences)

```
A[:, i] = (z(p₀ + δeᵢ) − z(p₀ − δeᵢ)) / (2δ)
```

where `eᵢ` is the unit vector for DOF `i`.

### Adjustment computation

```
error = z_target − z_measured
Δp    = A⁺ · error          # Moore–Penrose pseudoinverse
Δp_cmd = λ · Δp              # damped command  (λ = step_factor)
```

If A is well-conditioned (all DOFs sampled independently), `A⁺ = (AᵀA)⁻¹Aᵀ`.

### Iterative alignment loop

```
while RMS > tolerance:
    z_meas  = measure()
    Δp_cmd  = λ · A⁺ · (z_target − z_meas)
    apply(Δp_cmd)
    if RMS_new > RMS_old:
        reduce λ or re-calibrate A
```
