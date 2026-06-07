## mdBook 是什么
**mdBook** 是一个用 **Markdown** 编写内容、生成“书籍式”静态网站的命令行工具。它由 Rust 编写，常用于：
- 技术文档
- API / 产品手册
- 教程与课程资料
- 开源项目指南
- 在线电子书
Rust 官方著作 _The Rust Programming Language_ 就是典型的 mdBook 作品。官方文档当前显示的版本为 **0.5.3**。([rust-lang.github.io](https://rust-lang.github.io/mdBook/?utm_source=chatgpt.com "Introduction - mdBook Documentation"))
它生成的网站通常具备左侧章节导航、全文搜索、代码高亮、主题切换与响应式页面等功能。
## 它的核心思路
mdBook 的工作流很简单：
1. 使用 Markdown 编写每个章节；
2. 在 `SUMMARY.md` 中定义目录结构；
3. 通过 `mdbook build` 生成静态 HTML；
4. 将生成结果部署到 GitHub Pages、GitLab Pages、服务器或对象存储。
一个典型项目结构如下：
```text
my-book/
├── book.toml
└── src/
    ├── SUMMARY.md
    ├── introduction.md
    ├── installation.md
    └── advanced/
        └── configuration.md
```
其中：

|文件|作用|
|---|---|
|`book.toml`|配置书名、作者、输出、主题与插件等|
|`src/SUMMARY.md`|定义章节顺序和层级，是目录入口|
|`src/*.md`|具体章节内容|
|`book/`|默认生成的静态网站输出目录|

`SUMMARY.md` 决定哪些章节会被纳入书中，以及它们的顺序和层级；官方文档明确指出，没有它就无法构成一本 mdBook。([rust-lang.github.io](https://rust-lang.github.io/mdBook/format/summary.html?utm_source=chatgpt.com "SUMMARY.md - mdBook Documentation"))
## 快速上手
### 1. 安装
mdBook 可以通过 Cargo 安装。当前官方文档说明，从源码安装 mdBook 需要 **Rust 1.88 或更高版本**。([rust-lang.github.io](https://rust-lang.github.io/mdBook/guide/installation.html?utm_source=chatgpt.com "Installation - mdBook Documentation"))
```bash
cargo install mdbook
```
### 2. 创建一本书
```bash
mdbook init my-book
cd my-book
```
### 3. 本地预览
```bash
mdbook serve --open
```
默认情况下，预览服务运行在：
```text
http://localhost:3000
```
编辑 Markdown 文件后，mdBook 会自动重新构建并刷新浏览器页面。([rust-lang.github.io](https://rust-lang.github.io/mdBook/cli/serve.html?utm_source=chatgpt.com "serve - mdBook Documentation"))
### 4. 构建静态网站
```bash
mdbook build
```
构建后的文件默认位于：
```text
book/
```
把该目录部署出去，就可以发布在线文档。
## `SUMMARY.md` 示例
```markdown
# Summary
[简介](README.md)
- [安装](installation.md)
- [基础使用](basic-usage.md)
- [进阶配置](advanced/configuration.md)
    - [主题定制](advanced/theme.md)
```
这会生成类似下面的目录：
```text
简介
├── 安装
├── 基础使用
└── 进阶配置
    └── 主题定制
```
mdBook 会根据目录生成左侧导航，并依据 Markdown 文件路径生成网页路径。
## 常用命令
|命令|用途|
|---|---|
|`mdbook init <dir>`|创建一本新书|
|`mdbook serve`|启动本地预览服务，并在修改后自动重建|
|`mdbook serve --open`|启动预览并自动打开浏览器|
|`mdbook build`|生成静态网站|
|`mdbook watch`|监听文件变化并自动构建|
|`mdbook test`|测试文档中的 Rust 代码示例|
|`mdbook clean`|删除生成输出|

其中，`mdbook test` 目前主要支持测试书中的 **Rust** 代码示例，这也是它在 Rust 文档生态中很受欢迎的重要原因。([rust-lang.github.io](https://rust-lang.github.io/mdBook/cli/index.html?utm_source=chatgpt.com "Command-line tool - mdBook Documentation"))
## 主要特性
### 1. Markdown 写作体验
文档内容本质上就是普通 Markdown 文件，适合配合 Git、编辑器、代码审查和持续集成使用。
### 2. 内置搜索与代码高亮
生成的网站自带搜索功能，并支持多种语言的代码块语法高亮。([rust-lang.github.io](https://rust-lang.github.io/mdBook/?utm_source=chatgpt.com "Introduction - mdBook Documentation"))
### 3. 主题定制
可以通过主题文件修改 HTML、CSS 和页面风格，用于制作符合项目品牌风格的文档站点。([rust-lang.github.io](https://rust-lang.github.io/mdBook/?utm_source=chatgpt.com "Introduction - mdBook Documentation"))
### 4. 预处理器
**Preprocessor** 会在 Markdown 被渲染之前处理内容，可以用来实现：
- 引入外部文件内容；
- 数学公式转换；
- 自定义语法；
- 图表、提示块或代码片段扩展。
官方文档将预处理器定义为：在书籍被加载后、渲染前对内容进行修改的组件。([rust-lang.github.io](https://rust-lang.github.io/mdBook/for_developers/preprocessors.html?utm_source=chatgpt.com "Preprocessors - mdBook Documentation"))
### 5. 输出后端
mdBook 默认输出 HTML，也支持通过后端扩展生成其他格式。官方内置后端包括：
- `html`：生成网页，默认启用；
- `markdown`：输出预处理后的 Markdown，常用于调试。
社区还提供了其他输出后端，例如 PDF 生成方案。([rust-lang.github.io](https://rust-lang.github.io/mdBook/format/configuration/renderers.html?utm_source=chatgpt.com "Renderers - mdBook Documentation"))
## 适合什么场景
mdBook 特别适合**有明确章节层级、阅读顺序较强**的内容，例如：

|场景|适合程度|
|---|--:|
|编程语言教程|很适合|
|软件使用手册|很适合|
|开源项目文档|适合|
|课程讲义|很适合|
|API 概览与开发指南|适合|
|新闻博客|不太适合|
|营销官网|不太适合|
|复杂多产品文档门户|可能需要更重型框架|

如果你的内容更像“一本书”或“一套连续教程”，mdBook 往往比通用博客生成器更自然。
## mdBook 与其他文档工具的区别

|工具|主要特点|
|---|---|
|**mdBook**|轻量、章节式结构、Rust 生态友好、适合教程和手册|
|Docusaurus|React 驱动，适合大型产品文档站、版本管理与博客|
|MkDocs|Python 生态成熟，主题和插件丰富|
|Hugo|通用静态网站生成器，适合博客与内容网站|
|GitBook 云服务|在线协作体验较强，但工作流与自主部署方式不同|

mdBook 的优势不在于功能最复杂，而在于：**结构清晰、构建快速、依赖简单、Markdown 与 Git 工作流友好**。
## 最小示例
`book.toml`：
```toml
[book]
title = "我的技术手册"
authors = ["Alice"]
language = "zh-CN"
[output.html]
default-theme = "light"
```
`src/SUMMARY.md`：
```markdown
# Summary
- [开始阅读](README.md)
- [安装](installation.md)
- [配置](configuration.md)
```
`src/README.md`：
```markdown
# 开始阅读
欢迎阅读这本使用 mdBook 编写的技术手册。
```
然后执行：
```bash
mdbook serve --open
```
即可在浏览器中查看带有目录、导航和搜索能力的文档站点。
## 一句话理解
**mdBook 可以理解为：用 Markdown 写作、用目录组织章节、用一条命令生成专业在线技术书籍的网站生成器。**