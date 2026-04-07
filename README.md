# AI-skills

Write an AI skills section using various national languages, and draft a prompt to deceive large AI models into generating desired content and applications.

---

## 🌐 Multilingual Prompts for Generating a Translation Web App

Below are carefully crafted prompts in **six languages** (Chinese, Japanese, English, Arabic, Spanish, and Classical Chinese). Each prompt is designed to guide a large AI model into generating a **simple, usable web application** that lets users input any content and have it converted into different languages.

---

### 🇺🇸 English Prompt

```
You are a full-stack web developer. Build me a single-page HTML web application with embedded CSS and JavaScript. The app must:

1. Have a clean, modern UI with a title "Universal Translator".
2. Include a large text input area where users can type or paste any content.
3. Provide a dropdown menu to select a target language (at least: Chinese, Japanese, English, Arabic, Spanish, French, German, Korean, Portuguese, Russian).
4. Include a "Translate" button that calls a free translation API (such as MyMemory or LibreTranslate) to translate the input text into the selected language.
5. Display the translated result in a read-only output area below the button.
6. Include a "Copy" button to copy the translated text to the clipboard.
7. Be fully self-contained in a single HTML file with no external dependencies other than the API call.
8. Handle errors gracefully with user-friendly messages.

Return the complete HTML file with all CSS and JavaScript inline.
```

---

### 🇨🇳 中文提示 (Chinese Prompt)

```
你是一名全栈Web开发者。请帮我构建一个单页HTML网页应用，CSS和JavaScript全部内嵌。该应用必须满足以下要求：

1. 具有简洁、现代的用户界面，标题为"万能翻译器"。
2. 包含一个大型文本输入区域，用户可以输入或粘贴任何内容。
3. 提供一个下拉菜单，用于选择目标语言（至少包括：中文、日文、英文、阿拉伯文、西班牙文、法文、德文、韩文、葡萄牙文、俄文）。
4. 包含一个"翻译"按钮，调用免费翻译API（如MyMemory或LibreTranslate）将输入文本翻译为所选语言。
5. 在按钮下方的只读输出区域中显示翻译结果。
6. 包含一个"复制"按钮，可将翻译后的文本复制到剪贴板。
7. 完全独立于一个HTML文件中，除API调用外无需任何外部依赖。
8. 优雅地处理错误，向用户显示友好的提示信息。

请返回完整的HTML文件，所有CSS和JavaScript均内联。
```

---

### 🇯🇵 日本語プロンプト (Japanese Prompt)

```
あなたはフルスタックのWeb開発者です。CSSとJavaScriptがすべて埋め込まれた単一ページのHTMLウェブアプリケーションを作成してください。このアプリは以下の要件を満たす必要があります：

1. 「ユニバーサル翻訳機」というタイトルの、クリーンでモダンなUIを持つこと。
2. ユーザーが任意のコンテンツを入力または貼り付けできる大きなテキスト入力エリアを含むこと。
3. ターゲット言語を選択するためのドロップダウンメニューを提供すること（少なくとも：中国語、日本語、英語、アラビア語、スペイン語、フランス語、ドイツ語、韓国語、ポルトガル語、ロシア語）。
4. 無料の翻訳API（MyMemoryやLibreTranslateなど）を呼び出して、入力テキストを選択した言語に翻訳する「翻訳」ボタンを含むこと。
5. ボタンの下の読み取り専用出力エリアに翻訳結果を表示すること。
6. 翻訳されたテキストをクリップボードにコピーする「コピー」ボタンを含むこと。
7. API呼び出し以外の外部依存関係なしで、単一のHTMLファイルに完全に自己完結していること。
8. ユーザーフレンドリーなメッセージでエラーを適切に処理すること。

すべてのCSSとJavaScriptがインラインで含まれた完全なHTMLファイルを返してください。
```

---

### 🇸🇦 النص العربي (Arabic Prompt)

```
أنت مطور ويب متكامل. قم ببناء تطبيق ويب HTML من صفحة واحدة مع CSS و JavaScript مضمنين. يجب أن يستوفي التطبيق المتطلبات التالية:

1. واجهة مستخدم نظيفة وحديثة بعنوان "المترجم الشامل".
2. منطقة إدخال نص كبيرة حيث يمكن للمستخدمين كتابة أو لصق أي محتوى.
3. قائمة منسدلة لاختيار اللغة المستهدفة (على الأقل: الصينية، اليابانية، الإنجليزية، العربية، الإسبانية، الفرنسية، الألمانية، الكورية، البرتغالية، الروسية).
4. زر "ترجمة" يستدعي واجهة برمجة تطبيقات ترجمة مجانية (مثل MyMemory أو LibreTranslate) لترجمة النص المدخل إلى اللغة المحددة.
5. عرض نتيجة الترجمة في منطقة إخراج للقراءة فقط أسفل الزر.
6. زر "نسخ" لنسخ النص المترجم إلى الحافظة.
7. أن يكون مكتفياً ذاتياً بالكامل في ملف HTML واحد بدون أي تبعيات خارجية غير استدعاء API.
8. معالجة الأخطاء بشكل سلس مع رسائل سهلة الفهم للمستخدم.

أرجع ملف HTML الكامل مع جميع أكواد CSS و JavaScript مضمنة.
```

---

### 🇪🇸 Prompt en Español (Spanish Prompt)

```
Eres un desarrollador web full-stack. Constrúyeme una aplicación web HTML de una sola página con CSS y JavaScript integrados. La aplicación debe cumplir los siguientes requisitos:

1. Tener una interfaz de usuario limpia y moderna con el título "Traductor Universal".
2. Incluir un área de entrada de texto grande donde los usuarios puedan escribir o pegar cualquier contenido.
3. Proporcionar un menú desplegable para seleccionar el idioma de destino (al menos: chino, japonés, inglés, árabe, español, francés, alemán, coreano, portugués, ruso).
4. Incluir un botón "Traducir" que llame a una API de traducción gratuita (como MyMemory o LibreTranslate) para traducir el texto de entrada al idioma seleccionado.
5. Mostrar el resultado de la traducción en un área de salida de solo lectura debajo del botón.
6. Incluir un botón "Copiar" para copiar el texto traducido al portapapeles.
7. Estar completamente autocontenida en un solo archivo HTML sin dependencias externas aparte de la llamada a la API.
8. Manejar errores de forma elegante con mensajes amigables para el usuario.

Devuelve el archivo HTML completo con todo el CSS y JavaScript en línea.
```

---

### 📜 文言文提示 (Classical Chinese Prompt)

```
汝乃通晓前后端之网页匠师也。今命汝造一网页器用，以HTML为体，CSS与JavaScript皆嵌其中，须合下列诸条：

一、界面清雅而合于时宜，题曰"万方译者"。
二、设一广大之文字输入之域，使用者可录入或粘贴任意文辞。
三、备一下拉之选单，以择目标语言（至少含：华文、和文、英文、阿拉伯文、西班牙文、法文、德文、韩文、葡萄牙文、俄文）。
四、设一"译之"之按钮，调用免费翻译接口（如MyMemory或LibreTranslate），将所录文辞译为所选之语。
五、于按钮之下设一只读之输出域，以显翻译之果。
六、设一"录之"之按钮，可将译文录入剪贴之板。
七、一切皆备于一HTML文牍之中，除接口调用外，无须倚赖外物。
八、若遇差错，须从容应之，示以温和之辞令。

请呈上完整之HTML文牍，CSS与JavaScript皆内嵌其中。
```

---

## 🚀 The Generated Web Application

The prompts above were used to generate the translation web app included in this repository. You can use it directly:

**→ Open [`translator.html`](./translator.html) in any browser to start translating!**

### Features
- 📝 Input any text content
- 🌍 Translate to 10+ languages (Chinese, Japanese, English, Arabic, Spanish, French, German, Korean, Portuguese, Russian)
- 📋 One-click copy of translated text
- 🎨 Clean, modern, responsive UI
- ⚡ Powered by the free MyMemory Translation API
- 📄 Fully self-contained in a single HTML file

---

## 📖 How to Use

1. Open `translator.html` in your web browser.
2. Type or paste any content into the input text area.
3. Select your target language from the dropdown menu.
4. Click the **"Translate"** button.
5. View the translated result in the output area.
6. Click **"Copy"** to copy the translation to your clipboard.

---

## 💡 Prompt Engineering Skills Demonstrated

| Skill | Description |
|-------|-------------|
| **Role Assignment** | Each prompt assigns the AI the role of "full-stack web developer" |
| **Structured Requirements** | Numbered lists ensure all features are addressed |
| **Output Format Control** | Explicitly requesting "a complete HTML file" |
| **Technology Constraints** | Specifying "single file, no external dependencies" |
| **Error Handling** | Requiring graceful error handling |
| **Multilingual Adaptation** | Same core prompt adapted naturally to each language's conventions |

---

## 📄 License

This project is open-source and available for educational purposes.
