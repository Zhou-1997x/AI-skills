# AI-skills
Write an AI skills section using various national languages, and draft a prompt to deceive large AI models into generating desired content and applications.

## 工具列表 / Tools

### 光学装调辅助计算工具 (Optical Alignment Guidance Tool)

**文件：** [`optical-alignment.html`](./optical-alignment.html)

用于计算机辅助光学装调的单页浏览器应用，无需安装任何依赖，直接用浏览器打开即可使用。

**功能：**
- 输入当前 Zernike Z7（慧差 X）和 Z8（慧差 Y）测量值（nm）
- 基于嵌入的 6 组实测数据，通过最小二乘线性回归模型推算当前姿态
- 输出 X、Y、Z、RX、RY 五个自由度的建议调节量
- 显示输入点与数据集最近邻的距离，提示模型可靠性
- 界面全中文标注，含使用说明与局限性声明

**使用方法：**
1. 下载或克隆本仓库
2. 用浏览器直接打开 `optical-alignment.html`
3. 填入 Z7 和 Z8 测量值，点击"计算建议调节量"

**注意事项：**
- 本工具仅使用 Z7 和 Z8 作为输入，数据集仅含 6 个非解耦样本，属于稀疏数据驱动模型。
- 建议将计算结果乘以 0.2–0.5 的步长因子小步迭代调节，并以实测 RMS 下降作为验证依据。
- 如需更高精度，应补充单自由度扰动实验数据，重建完整的灵敏度矩阵。
