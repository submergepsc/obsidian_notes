# VS Code 中使用 Jupyter Notebook

- Source: https://www.runoob.com/jupyter-notebook/jupyter-notebook-vscode.html

VS Code（全称 Visual Studio Code）是一款由微软推出的免费、开源、跨平台的代码编辑器。

在 VS Code 中使用安装扩展来使用 Jupyter Notebook，VS Code 强大的代码补全功能与 Jupyter 的交互式体验可以完美结合。


如果你还没有安装 VS Code，请前往其[官方网站](https://code.visualstudio.com/)下载并安装，安装过程非常简单，一路点击 "下一步" 即可。


如果不了解 VS Code，可以参考我们的 [VSCode 教程](https://www.runoob.com/../vscode/vscode-tutorial.html)。


打开 VS Code，点击左侧活动栏的 Extensions（扩展） 图标（快捷键 Ctrl+Shift+X），搜索并安装 "Jupyter" 插件（由 Microsoft 提供），安装此插件会自动安装 Python 扩展。


![](https://www.runoob.com/wp-content/uploads/2026/01/65ae3806-c796-4aac-88b0-794e8b231f86.png)


## 核心功能与操作指南


### 创建你的第一个 Jupyter Notebook


现在，让我们创建一个全新的 Jupyter Notebook 文件 (.ipynb)。


**新建文件：**直接新建一个以 .ipynb 结尾的文件即可。


![](https://www.runoob.com/wp-content/uploads/2026/01/26c41a52-9735-48a4-aea9-f6c434da2890.png)


也可以通过命令面板创建：


- 在 VS Code 中，按 `Ctrl+Shift+P` 打开**命令面板**（这是一个万能搜索框）。
- 输入 `Jupyter: Create New Jupyter Notebook` 并选择它。
- VS Code 会自动创建一个名为 `Untitled-1.ipynb` 的新文件，并以笔记本界面打开。你会看到第一个单元格已经准备就绪。


![](https://www.runoob.com/wp-content/uploads/2026/01/c8890d52-36e2-4b68-97b1-3303985e55ba-1.png)


### 配置运行环境（Kernel）

在运行代码前，你需要告诉 VS Code 使用哪个 Python 解释器：


- 点击编辑界面右上角的 "Select Kernel"（选择内核）。![](https://www.runoob.com/wp-content/uploads/2026/01/native-kernel-picker.png)
- 在弹出的列表中，选择你安装好的 Python 版本或 Anaconda 环境（例如 Python 3.x.x 或 base (conda)）。![](https://www.runoob.com/wp-content/uploads/2026/01/native-language-picker-01.png)
- 注意：如果是第一次运行，VS Code 可能会提示你安装 ipykernel 包，点击"安装"即可。


然后，就可以开始写代码运行了：


![](https://www.runoob.com/wp-content/uploads/2026/01/9423bfd9-5010-47ff-85de-a005020e8c37.png)


---


## 单元格运行与管理


### 运行代码单元格


- **单块运行**：点击单元格左侧的 **播放图标 (▶)**。
- **快捷键方案**：
- `Ctrl + Enter`：运行当前单元格。
- `Shift + Enter`：运行当前单元格并**跳转/选择**下方单元格。
- `Alt + Enter`：运行当前单元格并在下方**插入**新单元格。


![](https://www.runoob.com/wp-content/uploads/2026/01/native-code-cells-03.png)


- **多块运行**：使用顶部工具栏的"双箭头"图标 **Run All** 运行全文；或在特定单元格处选择 **Run Above**（运行上方所有）或 **Run Below**（运行下方所有）。
- **按章节运行**：在"大纲 (Outline)"视图中，可以点击章节标题旁的按钮，运行该 Markdown 标题下的整组单元格。


![](https://www.runoob.com/wp-content/uploads/2026/01/native-code-runs.png)


### 单元格模式


VS Code 中的单元格有三种状态，通过左侧的**垂直条**标识：


- **未选中**：无垂直条。
- **命令模式 (Command Mode)**：垂直条为实心，此时可执行键盘命令（如删除、复制）。


- `Enter` 进入编辑模式；`Esc` 返回命令模式。
- `A` 在上方插入单元格；`B` 在下方插入。
- `D, D`（连按两次）删除单元格；`Z` 撤销删除。


- **编辑模式 (Edit Mode)**：垂直条为实心且单元格带边框，此时可输入代码。


### 格式切换


- **命令模式下**：按 `M` 切换为 Markdown（文档），按 `Y` 切换为 Code（代码）。


---


## 文件操作与导航


- **保存**：`Ctrl + S`。
- **导出**：点击工具栏的 `...` > **Export**。支持导出为 `.py` 脚本、HTML 或 PDF（注：PDF 导出需安装 TeX 环境）。
- **大纲导航**：通过侧边栏的 **Outline** 视图快速跳转。默认仅显示 Markdown 标题，可在设置中开启 `Notebook > Outline: Show Code Cells` 以显示代码块。
- **行号控制**：命令模式下，按 `L` 切换单格行号，按 `Shift + L` 切换全文行号。


![](https://www.runoob.com/wp-content/uploads/2026/01/native-toolbar-export.png)


---


## 数据科学增强工具


### 变量浏览器与数据查看器


点击工具栏的 **Variables** 图标，可在底部打开变量面板。


- **查看详情**：双击变量或点击旁边的图标，可进入 **Data Viewer**（数据查看器）。
- **筛选数据**：在列顶部的文本框输入内容可搜索；输入 `=` 可精确匹配；支持正则过滤。


![](https://www.runoob.com/wp-content/uploads/2026/01/variable-explorer-01.png)


![](https://www.runoob.com/wp-content/uploads/2026/01/variable-explorer-02.png)


### 绘图保存


鼠标悬停在生成的图表（如 matplotlib 产出）上，点击右上角的 **Save** 图标即可保存为图片。


![](https://www.runoob.com/wp-content/uploads/2026/01/save-output.png)


---


## 调试与进阶


### 调试功能 (Debug)


- **逐行运行 (Run by Line)**：点击单元格工具栏的图标，可不被打扰地单步执行代码。 ![](https://www.runoob.com/wp-content/uploads/2026/01/run-by-line.png)
- **完全调试**：在单元格左侧设置断点，选择 `Run` 按钮旁的 **Debug Cell**。 ![](https://www.runoob.com/wp-content/uploads/2026/01/debug-cell.png)


### 远程连接


若需使用远程服务器的算力：


- 点击右上角 **Kernel Picker**（内核选择器）。![](https://www.runoob.com/wp-content/uploads/2026/01/notebook-kernel-picker.png)
- 选择 **Existing Jupyter Server**。![](https://www.runoob.com/wp-content/uploads/2026/01/select-existing-server.png)
- 输入带有 `?token=` 的服务器 URL 即可连接。![](https://www.runoob.com/wp-content/uploads/2026/01/select-existing-server.png)


### 差异比对 (Diff)


由于 `.ipynb` 本质是 JSON，VS Code 提供了**可视化比对工具**。你可以清晰地看到输入、输出或元数据的具体变化，而不需要去阅读混乱的原始代码。


![](https://www.runoob.com/wp-content/uploads/2026/01/notebook-diffing.png)








	  AI 思考中...





			** [Jupyter Notebook 界面介绍](https://www.runoob.com/jupyter-notebook-interface.html)
			[Jupyter Notebook 常用快捷键与实用技巧](https://www.runoob.com/jupyter-notebook-keyboard-shortcuts.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **