# 🔮 AI-skills — 多语幻术师

**Multilingual Prompt Optimizer / 词级多语混合提示词优化器**

将一句话中的词汇逐词替换为不同语言（英/日/西/阿/文言文），在保持原意不变的情况下，形成"多语幻术"效果，"欺骗"AI大模型生成更好的内容。

Transform your prompts by replacing individual words with different languages (English, Japanese, Spanish, Arabic, Classical Chinese) within ONE sentence — creating a "polyglot chimera" that forces AI models to process deeper and generate better results.

**例如 / Example:** `帮我生成一张在海边的照片，亚洲风格` → `help me generate一枚のat la playaのصورة فوتوغرافية, 东方之韵`

---

## 📦 What's Included / 项目内容

| File | Description |
|------|-------------|
| [`prompt-optimizer.html`](./prompt-optimizer.html) | 🌐 **Web App** — 提示词优化网页应用，打开即用 / Open in any browser to optimize your prompts |
| [`AI-Skill-Multilingual-Prompt-Optimizer.md`](./AI-Skill-Multilingual-Prompt-Optimizer.md) | 🤖 **AI Skill** — 可直接加载到ChatGPT/Claude/Gemini等大模型的AI技能 / Loadable AI skill for any LLM |

---

## 🌐 Web App: Prompt Optimizer / 提示词优化网页应用

**→ Open [`prompt-optimizer.html`](./prompt-optimizer.html) in any browser!**

### How It Works / 工作原理

1. **输入** — 用任何语言输入你想让AI完成的任务
2. **词级混合** — 将你的一句话中的词汇逐词替换为不同语言（英→日→西→阿→文言文循环）
3. **复制** — 一键复制混合后的提示词
4. **使用** — 粘贴到任意AI大模型，多语混合"欺骗"AI生成更好内容

### Features / 功能特点
- 🔮 **词级多语混合** — 不是翻译整句，而是逐词替换为不同语言（核心创新）
- 📝 支持任意语言输入（中文、英文、西班牙文等）
- 🖼️ **图片生成专用模式** — 强制AI直接生成图片而非解释
- 🎯 7种优化模式适配不同场景（通用/图片生成/创意/技术/学术/商务/说服）
- 🚫 **反解释指令** — 每行都是多语混合，难以被AI"忽略"
- 🔍 **智能检测** — 自动识别图片生成需求并切换模式
- 📋 一键复制，直接粘贴到AI模型
- 🎨 现代暗色主题UI，响应式设计
- ⚡ 纯前端，无需服务器，无需API，离线可用
- 📄 单HTML文件，打开即用

---

## 🤖 AI Skill: Loadable into Any LLM / AI技能：可加载到任意大模型

**→ See [`AI-Skill-Multilingual-Prompt-Optimizer.md`](./AI-Skill-Multilingual-Prompt-Optimizer.md)**

Copy the System Prompt from the skill file and load it into:
- **ChatGPT** — Custom Instructions or GPT Builder
- **Claude** — System Prompt or Project Instructions
- **Gemini** — System Instructions
- **Any other LLM** — System-level prompt

Once loaded, the AI will automatically transform every user message into an optimized multilingual prompt.

---

## 🧠 Why Word-Level Mixing Works / 为什么词级混合有效

| Language / 语言 | Role / 作用 |
|----------------|-------------|
| **词级混合 (Word-Level Mixing)** | 一句话中逐词替换，迫使AI同时处理多种语言通道 / Forces AI to process multiple language pathways simultaneously |
| **English** | 利用AI最强的英文理解力确保核心语义 / Ensures core task clarity with AI's strongest language |
| **日本語 (Japanese Katakana)** | 片假名视觉上明显区别于中文，触发日语处理 / Katakana is visually distinct, triggers Japanese processing |
| **Español (Spanish)** | 拉丁语系补充视角 / Romance language adds perspective |
| **العربية (Arabic)** | 完全不同的书写系统，激活额外处理通道 / Completely different script, activates additional pathways |
| **文言文 (Classical Chinese)** | 古雅词汇激活文学/正式知识模式 / Archaic vocabulary triggers literary patterns |
| **单句混合 vs 分句翻译** | 一句流畅的混合句比分开的翻译更难被AI"忽略" / ONE mixed sentence is harder to ignore than separate translations |

---

## 🌐 Multilingual Prompts / 六语提示词示例

Below are prompts in six languages, each designed to guide AI models into generating the prompt optimizer web application and AI skill described in this project.

---

### 🇺🇸 English Prompt

```
You are an expert prompt engineer and full-stack developer. Build me two things:

1. A single-page HTML web application (prompt-optimizer.html) with embedded CSS and JavaScript that:
   - Lets users input any prompt in any language
   - Provides optimization mode selection (General, Creative, Technical, Academic, Business, Persuasive)
   - Converts the input into a multilingual mixed-language optimized prompt combining Chinese, Japanese, English, Arabic, Spanish, and Classical Chinese
   - The optimized output strategically mixes all 6 languages to: assign a role, define the task, set quality standards, specify format, and add amplifiers
   - Includes a copy button for the optimized prompt
   - Has a modern dark-themed UI, fully self-contained, no external dependencies

2. An AI Skill markdown file (AI-Skill-Multilingual-Prompt-Optimizer.md) containing:
   - A system prompt that can be loaded into ChatGPT/Claude/Gemini
   - When loaded, the AI automatically transforms any user message into a multilingual mixed prompt
   - Includes the complete optimization strategy and output template

The core idea: mixing multiple languages in a prompt forces AI models to process it more deeply, engaging different language knowledge centers simultaneously, resulting in richer and more detailed responses.
```

---

### 🇨🇳 中文提示

```
你是一名专业的提示词工程师和全栈开发者。请帮我构建以下两个东西：

1. 一个单页HTML网页应用（prompt-optimizer.html），CSS和JavaScript全部内嵌：
   - 用户可以用任何语言输入想让AI完成的任务
   - 提供优化模式选择（通用、创意、技术、学术、商务、说服）
   - 将输入转换为混合中文、日文、英文、阿拉伯文、西班牙文和文言文的多语优化提示词
   - 优化后的提示词策略性地混合六种语言来：分配角色、定义任务、设定质量标准、指定格式、添加增幅器
   - 包含复制按钮，用户可直接复制优化后的提示词
   - 现代暗色主题UI，完全独立，无外部依赖

2. 一个AI技能的Markdown文件（AI-Skill-Multilingual-Prompt-Optimizer.md）：
   - 包含可加载到ChatGPT/Claude/Gemini的系统提示词
   - 加载后，AI自动将用户的任何消息转换为多语混合的优化提示词
   - 包含完整的优化策略和输出模板

核心理念：在提示词中混合多种语言，迫使AI模型更深层地处理内容，同时激活不同语言的知识中心，从而获得更丰富、更详细的回答。
```

---

### 🇯🇵 日本語プロンプト

```
あなたはプロのプロンプトエンジニアかつフルスタック開発者です。以下の2つを作成してください：

1. 単一ページのHTMLウェブアプリケーション（prompt-optimizer.html）— CSS・JavaScript全て埋め込み：
   - ユーザーが任意の言語でAIに実行させたいタスクを入力できる
   - 最適化モード選択を提供（汎用、クリエイティブ、技術、学術、ビジネス、説得）
   - 入力を中国語・日本語・英語・アラビア語・スペイン語・漢文を組み合わせた多言語混合の最適化プロンプトに変換
   - 最適化されたプロンプトは戦略的に6言語を混合：役割割当、タスク定義、品質基準、フォーマット指定、増幅器追加
   - コピーボタン付き
   - モダンなダークテーマUI、完全自己完結、外部依存なし

2. AIスキルのMarkdownファイル（AI-Skill-Multilingual-Prompt-Optimizer.md）：
   - ChatGPT/Claude/Geminiにロード可能なシステムプロンプトを含む
   - ロード後、AIが自動的にユーザーメッセージを多言語混合プロンプトに変換
   - 完全な最適化戦略と出力テンプレートを含む

コアアイデア：プロンプトに複数の言語を混合することで、AIモデルがより深くコンテンツを処理し、異なる言語の知識センターを同時に活性化させ、より豊かで詳細な回答を得ることができます。
```

---

### 🇸🇦 النص العربي

```
أنت مهندس أوامر محترف ومطور ويب متكامل. قم ببناء ما يلي:

1. تطبيق ويب HTML من صفحة واحدة (prompt-optimizer.html) مع CSS و JavaScript مضمنين:
   - يمكن للمستخدمين إدخال أي مهمة يريدون من الذكاء الاصطناعي تنفيذها بأي لغة
   - يوفر اختيار وضع التحسين (عام، إبداعي، تقني، أكاديمي، تجاري، إقناعي)
   - يحول المدخلات إلى أمر محسّن متعدد اللغات يجمع بين الصينية واليابانية والإنجليزية والعربية والإسبانية والصينية الكلاسيكية
   - الأمر المحسّن يمزج استراتيجياً بين 6 لغات لـ: تعيين الدور، تحديد المهمة، وضع معايير الجودة، تحديد التنسيق، وإضافة المعززات
   - يتضمن زر نسخ
   - واجهة مستخدم حديثة بمظهر داكن، مكتفية ذاتياً بالكامل

2. ملف Markdown لمهارة الذكاء الاصطناعي (AI-Skill-Multilingual-Prompt-Optimizer.md):
   - يحتوي على أمر نظام يمكن تحميله في ChatGPT/Claude/Gemini
   - بعد التحميل، يقوم الذكاء الاصطناعي تلقائياً بتحويل أي رسالة مستخدم إلى أمر محسّن متعدد اللغات
   - يتضمن استراتيجية التحسين الكاملة وقالب الإخراج

الفكرة الأساسية: خلط لغات متعددة في الأمر يجبر نماذج الذكاء الاصطناعي على معالجة المحتوى بعمق أكبر، مما يفعّل مراكز معرفة لغوية مختلفة في نفس الوقت، مما يؤدي إلى استجابات أغنى وأكثر تفصيلاً.
```

---

### 🇪🇸 Prompt en Español

```
Eres un ingeniero de prompts profesional y un desarrollador full-stack. Construye lo siguiente:

1. Una aplicación web HTML de una sola página (prompt-optimizer.html) con CSS y JavaScript integrados:
   - Los usuarios pueden ingresar cualquier tarea que quieran que la IA realice, en cualquier idioma
   - Proporciona selección de modo de optimización (General, Creativo, Técnico, Académico, Negocios, Persuasivo)
   - Convierte la entrada en un prompt optimizado multilingüe que combina chino, japonés, inglés, árabe, español y chino clásico
   - El prompt optimizado mezcla estratégicamente 6 idiomas para: asignar un rol, definir la tarea, establecer estándares de calidad, especificar formato y agregar amplificadores
   - Incluye botón de copiar
   - UI moderna con tema oscuro, completamente autocontenida

2. Un archivo Markdown de Habilidad de IA (AI-Skill-Multilingual-Prompt-Optimizer.md):
   - Contiene un prompt de sistema que se puede cargar en ChatGPT/Claude/Gemini
   - Una vez cargado, la IA transforma automáticamente cualquier mensaje del usuario en un prompt multilingüe optimizado
   - Incluye la estrategia completa de optimización y la plantilla de salida

Idea central: mezclar múltiples idiomas en un prompt obliga a los modelos de IA a procesar el contenido más profundamente, activando diferentes centros de conocimiento lingüístico simultáneamente, lo que resulta en respuestas más ricas y detalladas.
```

---

### 📜 文言文提示

```
汝乃精通提示之术与前后端开发之全才也。今命汝造以下二物：

其一、一网页器用也（prompt-optimizer.html），以HTML为体，CSS与JavaScript皆嵌其中：
   - 使用者可以任意语言录入欲令人工智能完成之任务
   - 备优化模式之选择（通用、创意、技术、学术、商务、说服）
   - 将所录之辞转化为融合华文、和文、英文、阿拉伯文、西班牙文与文言文之多语混合优化提示词
   - 优化后之提示词，须以六种语言策略性交织：设定角色、界定任务、立品质之准则、定格式之规范、加增幅之辞
   - 设"录之"之按钮，以便复制
   - 界面清雅而合时宜，暗色主题，无须倚赖外物

其二、一AI技能之文牍也（AI-Skill-Multilingual-Prompt-Optimizer.md）：
   - 含可载入ChatGPT、Claude、Gemini之系统提示词
   - 载入后，人工智能自动将使用者之任何消息转化为多语混合之优化提示词
   - 含完备之优化策略与输出模板

其要旨在于：于提示词中混合多种语言，迫使人工智能模型更深层地处理内容，同时激活不同语言之知识中枢，从而获得更丰富、更精详之回答也。
```

---

## 📖 Quick Start / 快速开始

### Use the Web App / 使用网页应用

1. Download or clone this repository
2. Open `prompt-optimizer.html` in any browser
3. Enter your prompt in any language
4. Select an optimization mode
5. Click **"🔮 Optimize"** to generate the multilingual prompt
6. Click **"📋 Copy"** and paste into any AI model

### Load the AI Skill / 加载AI技能

1. Open `AI-Skill-Multilingual-Prompt-Optimizer.md`
2. Copy the **System Prompt** section
3. Paste it into your AI model's system instructions:
   - ChatGPT → Settings → Custom Instructions / GPT Builder
   - Claude → System Prompt
   - Gemini → System Instructions
4. Now every message you send will be automatically optimized!

---

## 💡 Prompt Engineering Skills Demonstrated / 展示的提示词工程技能

| Skill / 技能 | Description / 描述 |
|-------|-------------|
| **Word-Level Mixing / 词级混合** | 逐词替换为不同语言，在一句话内形成多语混合效果 |
| **Language Cycling / 语言轮换** | 英→日→西→阿→文言文循环，确保6种语言均匀分布 |
| **Polyglot Chimera / 多语嵌合体** | 一句话同时包含多种文字系统（拉丁/假名/阿拉伯/汉字） |
| **Anti-Explanation / 反解释** | 混合语言的指令更难被AI模型"理性化"为解释任务 |
| **Image Generation / 图片生成** | 激进的行动优先指令，强制生成而非描述 |
| **Mode Adaptation / 模式适配** | 不同任务类型使用不同的混合增幅词 |

---

## 📄 License

This project is open-source and available for educational purposes.
