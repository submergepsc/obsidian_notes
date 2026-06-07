`mdBook` 是一个用 Rust 开发的工具，用于将 Markdown 文件构建成漂亮的电子书或文档网站。它类似于 GitBook，但更轻量，适合开发文档、教程、技术手册等。下面我给你整理一份完整的使用指南。
## 1. 安装 mdBook
### 通过 cargo（推荐，如果你有 Rust 环境）
```bash
cargo install mdbook
```
安装完成后可以验证：
```bash
mdbook --version
```
### 通过预编译二进制（无需 Rust）
去 [mdBook Releases](https://github.com/rust-lang/mdBook/releases) 下载对应平台的压缩包，解压后把 `mdbook` 可执行文件放到 PATH 中即可。
## 2. 创建新书籍项目
```bash
mdbook init mybook
```
- `mybook` 是你的项目目录名。
- 这条命令会创建一个目录结构：
```
mybook/
├── book.toml       # 配置文件
├── src/
│   ├── SUMMARY.md  # 目录结构文件
│   └── chapter_1.md
└── ...
```
- `SUMMARY.md` 是整个书的目录，通过它来控制章节顺序和层级。
- `chapter_1.md` 是第一个章节示例。
## 3. 配置书籍
编辑 `book.toml`，可以设置书名、作者、语言等，例如：
```toml
[book]
title = "我的第一本书"
author = "张三"
description = "这是一本示例电子书"
[build]
create-missing = true
```
## 4. 编辑章节和目录
### SUMMARY.md 示例：
```markdown
# Summary
- [简介](./chapter_1.md)
- [安装](./chapter_2.md)
- [使用教程](./chapter_3.md)
```
- `- [标题](文件路径)` 表示章节。
- 支持多级嵌套：
```markdown
- [使用教程](./chapter_3.md)
  - [命令行](./chapter_3_1.md)
  - [配置文件](./chapter_3_2.md)
```
## 5. 构建书籍
```bash
mdbook build
```
- 默认会在 `book/` 文件夹生成静态 HTML 文件。
- 打开 `book/index.html` 就可以预览。
## 6. 本地预览
```bash
mdbook serve
```
- 默认地址是 [http://localhost:3000](http://localhost:3000/)。
- 支持热更新：修改 Markdown 文件后浏览器自动刷新。
## 7. 进阶功能
1. **自定义主题**
    ```bash
    mdbook build --theme <theme-folder>
    ```
    或在 `book.toml` 中配置：
    ```toml
    [output.html]
    theme = "my-theme"
    ```
2. **增加插件**  
    mdBook 支持 preprocessors 和 renderer，例如数学公式、搜索插件等。
    ```toml
    [preprocessor.mathjax]
    command = "mdbook-mathjax"
    ```
3. **导出 PDF**
    - 可以使用 `mdbook-pdf` 插件：
        ```bash
        cargo install mdbook-pdf
        mdbook-pdf build
        ```
## 8. 常用命令汇总
|命令|功能|
|---|---|
|`mdbook init <dir>`|初始化书籍项目|
|`mdbook build`|构建静态 HTML|
|`mdbook serve`|启动本地预览服务器|
|`mdbook watch`|监听文件变化并自动构建|
|`mdbook clean`|清理构建目录|
|`mdbook build --dest <dir>`|指定构建输出目录|

如果你愿意，我可以帮你直接写一个**最简 mdBook 模板项目**，你只需要下载就能直接修改章节。
你希望我帮你做吗？