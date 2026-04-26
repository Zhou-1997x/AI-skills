# AI-skills

> 🌐 **[English](#english) | [中文](#chinese)**

---

<a name="chinese"></a>

## 🇨🇳 中文介绍

### 项目简介

**AI-skills** 是一个纯前端（HTML + JavaScript）AI 工具集合，无需安装、无需后端，打开浏览器即可使用。

本项目收录了多种 AI 常用技能工具，帮助你更高效地与 AI 协作，涵盖提示词优化、写作助手、代码助手、视频翻译等场景。

---

### 🛠️ 工具列表

| 工具 | 文件 | 功能描述 |
|------|------|----------|
| 🧠 AI 提示词库 | [`ai-prompt-library.html`](./ai-prompt-library.html) | 33 个分类提示词模板，覆盖写作、代码、分析、创意、翻译、角色扮演、学习、数据 8 大类，支持搜索、筛选、一键复制和在线编辑 |
| ✍️ AI 写作助手 | [`ai-writing-assistant.html`](./ai-writing-assistant.html) | 支持润色、摘要、扩写、改写、正式化、口语化、翻译、校对 8 种写作模式，生成可直接用于任意 AI 工具的优化提示词 |
| 💻 AI 代码助手 | [`ai-code-helper.html`](./ai-code-helper.html) | 支持代码解释、代码审查、重构、调试、生成、语言转换、测试生成、文档生成 8 大功能，覆盖 15 种编程语言 |
| 🎬 视频自动翻译器 | [`video-translator.html`](./video-translator.html) | 通过 Whisper API 对视频进行自动转录和多语言字幕翻译，支持实时字幕叠加播放 |

---

### 🚀 快速开始

1. 克隆或下载本仓库
2. 在浏览器中直接打开任意 `.html` 文件（无需服务器）
3. 根据界面提示使用对应工具
4. 将生成的提示词复制到 ChatGPT、Claude、文心一言、Kimi 等 AI 工具中

> 💡 **提示：** 视频翻译器需要配置 Whisper API 密钥，其他工具均可离线使用。

---

### 📚 AI 常用技能说明

#### 提示词工程（Prompt Engineering）

高质量的提示词是发挥 AI 能力的关键。本项目内置的提示词库覆盖以下场景：

- **写作场景**：文章润色、内容摘要、扩写、营销文案、邮件撰写
- **代码场景**：代码解释、Bug 调试、代码审查、单元测试生成
- **分析场景**：竞品分析、数据分析、SWOT 分析、用户反馈分析
- **创意场景**：故事创作、头脑风暴、AI 绘图提示词、品牌命名
- **学习场景**：概念解释、费曼学习法、学习计划、知识问答
- **角色扮演**：专家顾问、苏格拉底辩证法、面试模拟

#### 关键 AI 技能

| 技能 | 说明 |
|------|------|
| 角色设定 | 为 AI 赋予具体身份，提升输出质量 |
| 思维链（CoT） | 引导 AI 逐步推理，减少错误 |
| 少样本示例 | 提供 1-3 个示例，帮助 AI 理解格式 |
| 结构化输出 | 要求 AI 按指定格式（表格/列表/JSON）输出 |
| 角色扮演 | 模拟专家、助手等角色进行深度交互 |
| 迭代优化 | 对 AI 输出进行多轮改进 |

---

### 📁 项目结构

```
AI-skills/
├── ai-prompt-library.html      # AI 提示词库
├── ai-writing-assistant.html   # AI 写作助手
├── ai-code-helper.html         # AI 代码助手
├── video-translator.html       # 视频自动翻译器
└── README.md                   # 项目说明
```

---

<a name="english"></a>

## 🇺🇸 English Introduction

### About

**AI-skills** is a collection of pure front-end (HTML + JavaScript) AI tools — no installation, no backend required. Just open any `.html` file in a browser and start using it.

This project includes various commonly-used AI skill tools to help you collaborate with AI more efficiently, covering prompt optimization, writing assistance, code assistance, video translation, and more.

---

### 🛠️ Tool List

| Tool | File | Description |
|------|------|-------------|
| 🧠 AI Prompt Library | [`ai-prompt-library.html`](./ai-prompt-library.html) | 33 categorized prompt templates across 8 categories: Writing, Code, Analysis, Creative, Translation, Roleplay, Learning, Data. Supports search, filter, one-click copy and inline editing. |
| ✍️ AI Writing Assistant | [`ai-writing-assistant.html`](./ai-writing-assistant.html) | 8 writing modes: Polish, Summarize, Expand, Rewrite, Formalize, Casualize, Translate, Proofread. Generates optimized prompts ready for any AI tool. |
| 💻 AI Code Helper | [`ai-code-helper.html`](./ai-code-helper.html) | 8 code tasks: Explain, Review, Refactor, Debug, Generate, Language Convert, Test Generation, Documentation. Supports 15 programming languages. |
| 🎬 Video Auto-Translator | [`video-translator.html`](./video-translator.html) | Automatically transcribes video using Whisper API and translates subtitles into multiple languages with real-time overlay playback. |

---

### 🚀 Quick Start

1. Clone or download this repository
2. Open any `.html` file directly in your browser (no server needed)
3. Follow the on-screen instructions
4. Copy the generated prompts into ChatGPT, Claude, Gemini, or any other AI tool

> 💡 **Note:** The Video Translator requires a Whisper API key. All other tools work offline.

---

### 📚 Key AI Skills Explained

#### Prompt Engineering

High-quality prompts are the key to unlocking AI's full potential. The built-in prompt library covers:

- **Writing**: Article polishing, summarization, expansion, marketing copy, email drafting
- **Coding**: Code explanation, bug debugging, code review, unit test generation
- **Analysis**: Competitor analysis, data analysis, SWOT analysis, user feedback analysis
- **Creative**: Story writing, brainstorming, AI image prompts, brand naming
- **Learning**: Concept explanation, Feynman technique, learning plans, Q&A practice
- **Roleplay**: Expert consultant, Socratic method, mock interviews

#### Essential AI Skills

| Skill | Description |
|-------|-------------|
| Role Assignment | Give AI a specific persona to improve output quality |
| Chain of Thought | Guide AI to reason step-by-step, reducing errors |
| Few-shot Examples | Provide 1-3 examples to help AI understand the format |
| Structured Output | Ask AI to respond in specific formats (table/list/JSON) |
| Roleplay | Simulate expert or assistant roles for deep interaction |
| Iterative Refinement | Improve AI outputs through multiple rounds of feedback |

---

### 📁 Project Structure

```
AI-skills/
├── ai-prompt-library.html      # AI Prompt Library
├── ai-writing-assistant.html   # AI Writing Assistant
├── ai-code-helper.html         # AI Code Helper
├── video-translator.html       # Video Auto-Translator
└── README.md                   # Project documentation
```

---

### 🤝 Contributing

Feel free to open issues or pull requests to add new prompt templates, improve existing tools, or suggest new AI skill tools.

---

*Built with ❤️ for AI enthusiasts · 为 AI 爱好者打造*

