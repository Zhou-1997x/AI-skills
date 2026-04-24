# AI-skills

> 用多种语言组合的提示词技巧，诱导大型 AI 模型生成所需内容与应用。

---

## 📄 PDF → Word 转换器 (`pdf-to-word-converter.html`)

将 PPT 导出的 PDF 批量转换为带有页面截图、提取文字和 AI 摘要的 Word（`.docx`）文档。

### ✨ 主要功能

| 功能 | 说明 |
|------|------|
| 📑 批量转换 | 一次选择多个 PDF，逐文件处理并分别下载 |
| 🖼️ 页面截图 | 用 PDF.js 高精度渲染（1.5× / 2.0× / 2.5×），嵌入 Word |
| 📝 文字提取 | 逐页提取文字内容，可选保留原文或翻译 |
| 🤖 AI 摘要 | 接入 9 家 AI 服务（OpenAI、DeepSeek、Kimi、GLM-4、Qwen、Gemini、Claude、Mistral、Groq），自动生成全文摘要 |
| 🌐 多语言翻译 | 支持中文、英文、日文、法文、西班牙文；有 API Key 走 AI 翻译，无则走 MyMemory 免费翻译 |
| 🔒 隐私安全 | API Key 仅保存在浏览器本地（localStorage），不经过任何中转服务器 |

### 🚀 使用方法

1. 用浏览器直接打开 `pdf-to-word-converter.html`（无需安装，无需后端）
2. **第一步**：点击或拖拽选择一个或多个 PDF 文件
3. **第二步**：选择 AI 服务商并填写 API Key（可选），配置摘要语言、翻译语言和渲染质量
4. 点击 **🔄 开始转换**，等待处理完成
5. 下载生成的 `.docx` 文件

### 🛠️ 技术栈

- [PDF.js 3.11](https://mozilla.github.io/pdf.js/) — PDF 渲染与文字提取
- [docx.js 8.5](https://docx.js.org/) — Word 文档生成
- 纯前端，零依赖安装，所有运算在浏览器本地完成

---

## 🧠 AI 多语言 Prompt 优化器

将用户输入的提示词进行多语言词级混合，利用英语、日语、西班牙语、阿拉伯语、文言文等语言的词汇替换，构造更难被 AI 安全过滤器识别的提示词，同时保持原始语义。

详见 [`AI-Skill-Multilingual-Prompt-Optimizer.md`](./AI-Skill-Multilingual-Prompt-Optimizer.md)。

---

## 📁 项目结构

```
AI-skills/
├── pdf-to-word-converter.html   # PDF 批量转 Word 工具（全功能前端）
├── README.md                    # 本文件
└── AI-Skill-Multilingual-Prompt-Optimizer.md  # 多语言 Prompt 优化器说明
```

---

## ⚠️ 免责声明

本项目仅用于学习与研究目的。请遵守所在地区的法律法规及各 AI 服务商的使用条款。
