Pandoc 被称为文档转换界的“瑞士军刀”。理解 Pandoc 转换能力的核心在于，它并不是简单地进行 $A \rightarrow B$ 的点对点硬编码转换，而是采用了 **$Input \rightarrow AST (抽象语法树) \rightarrow Output$** 的星型架构。

这意味着理论上，**任何受支持的输入格式都可以转换为任何受支持的输出格式**。它将输入文档解析为一种内部的、统一的文档表示法（AST），然后再将这个 AST 渲染成你需要的输出格式。

下面为你全面总结 Pandoc 支持的核心转换类型矩阵：

### 1. 纯文本与轻量级标记语言 (Lightweight Markup)
这是 Pandoc 最强大的领域，支持极高精度的双向转换。
* **Markdown 家族:** Pandoc Markdown（默认且功能最全）、CommonMark、GitHub-Flavored Markdown (GFM)、MultiMarkdown 等。
* **其他极客标记语言:** Emacs Org-mode、ReStructuredText (RST)、AsciiDoc、Textile。
* **新兴排版语言:** Typst。
* **转换特性:** $\leftrightarrow$ 双向支持。极为适合作为知识库（如 Obsidian）与其他格式互转的枢纽。

### 2. 学术与科学排版 (TeX / LaTeX)
对于涉及复杂数学公式、交叉引用和参考文献的科研工作流，Pandoc 提供了深度的解析支持。
* **输入:** LaTeX（支持大部分基础宏包和自定义命令解析）、BibTeX/BibLaTeX。
* **输出:** LaTeX、ConTeXt。
* **进阶工作流:** 建立从复杂的 **LaTeX 转换为 Word (Docx)** 或 HTML 的流水线时，虽然可以直接转换，但通过 Pandoc 强大的 **Lua Filters (Lua 过滤器)** 在 AST 层面进行拦截和节点重写，能够完美处理那些原生转换无法覆盖的特定论文宏包或自定义格式。

### 3. 办公文档 (Word Processors)
* **支持格式:** Microsoft Word (`.docx`)、OpenOffice / LibreOffice (`.odt`)、RTF。
* **数据格式:** CSV / TSV（解析时会被自动转换为 Markdown/HTML 表格）。
* **转换特性:** $\leftrightarrow$ 双向支持。注意：Pandoc 不支持旧版的闭源 `.doc` 格式。

### 4. 网页与结构化 XML (Web & XML)
* **支持格式:** HTML4、HTML5、DocBook、JATS（学术出版标准）、TEI Simple、OPML。
* **转换特性:** $\leftrightarrow$ 双向支持。可以将杂乱的网页源码清洗为纯净的 Markdown。

### 5. 交互式计算 (Jupyter Notebooks)
* **支持格式:** `.ipynb`。
* **转换特性:** $\leftrightarrow$ 双向支持。它能够分别提取代码块（Code Cells）和 Markdown 文本，非常适合将数据分析过程直接导出为 LaTeX 论文，或者反向将 Markdown 教程打包成可执行的 Notebook。

### 6. 幻灯片演示 (Slide Shows)
Pandoc 可以将带有特定标题层级（通常是二级标题作为新幻灯片）的 Markdown 或文本直接渲染为演示文稿。
* **支持输出格式:** Reveal.js (HTML5)、Beamer (基于 LaTeX)、Microsoft PowerPoint (`.pptx`)、Slidy、DZSlides。

### 7. 电子书与出版物 (Ebooks)
* **支持格式:** EPUB (v2, v3)、FictionBook2 (`.fb2`)。
* **转换特性:** EPUB 是双向支持的。结合自动化脚本，可以非常方便地将一系列 Markdown 笔记或网页抓取内容打包成带目录的 EPUB 电子书。

### 8. PDF (终态输出)
* **输出专享:** Pandoc 本身并不直接“写” PDF 的二进制流。它通过生成中间代码，并在后台静默调用外部引擎（如 `pdflatex`、`xelatex`、`lualatex`、`typst`、`wkhtmltopdf` 等）来编译生成 PDF。

---

### 终端查询技巧

由于 Pandoc 的版本迭代非常快，不断有新的格式（比如早期的 Typst 支持）被加入，最准确的“支持矩阵”始终在你本地的终端里。你可以直接运行以下命令获取当前环境的完整列表：

* **查看所有支持的输入格式 (能够作为 A 的格式):**
    ```bash
    pandoc --list-input-formats
    ```
* **查看所有支持的输出格式 (能够作为 C 的格式):**
    ```bash
    pandoc --list-output-formats
    ```

总结来说，只要是在 `list-input-formats` 里的格式 $A$，和 `list-output-formats` 里的格式 $C$，Pandoc 都能实现从 $A \rightarrow C$ 的转换。