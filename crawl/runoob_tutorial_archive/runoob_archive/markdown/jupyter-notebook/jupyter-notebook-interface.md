# Jupyter Notebook 界面介绍

- Source: https://www.runoob.com/jupyter-notebook/jupyter-notebook-interface.html

成功启动 Jupyter Notebook 后，会经历两个核心界面：


- 文件浏览器界面
- Notebook 编辑界面


### 1、文件浏览器界面


当你启动 Jupyter 时，看到的是这个管理界面，类似一个带后台控制功能的资源管理器：


![](https://www.runoob.com/wp-content/uploads/2026/01/ffdb7903-d899-4c36-a2c2-ea5e0f3d651c.png)


- **工作目录：** 这里显示的是你启动 Jupyter 时所在的文件夹。
- **注意图标颜色：** 笔记本图标若是**绿色**，代表该文档的内核（Kernel）正在后台运行，占用着 CPU 和内存；**灰色**则表示文件已保存但未激活。


点击正在运行的标签可以一键查看所有正在运行的 Notebook：


![](https://www.runoob.com/wp-content/uploads/2026/01/540f223e-ade8-496e-b893-70787c7a2b89.png)


新建 按钮用于创建新笔记，通常选择第一个选项 **Python 3**。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-2.png)


如果你下载了别人的 `.ipynb` 教程，使用 **Upload** 即可将其导入当前目录。


![](https://www.runoob.com/wp-content/uploads/2026/01/ff45f48e-1384-4fa3-aa86-dae0d0e81b82.png)


---


### Notebook 编辑界面


点击新建文件后进入的界面，这是 Notebook 编辑界面。


![](https://www.runoob.com/wp-content/uploads/2026/01/b535d34b-0600-496d-8fca-48754af961a9.png)


1、文件重命名： 点击左上角 `Jupyter` Logo 旁的标题（如 `Untitled`），即可弹出重命名框。


![](https://www.runoob.com/wp-content/uploads/2026/01/faf08862-49fd-4645-8f95-63f2da326cd0-1.png)


**2、保存与恢复：** `文件` 菜单下的 **恢复 Notebook 到检查点**，Jupyter 会建立检查点，如果你代码改乱了，可以随时回滚到之前的状态。


![](https://www.runoob.com/wp-content/uploads/2026/01/2017d91b-4f53-4c5f-a623-26f7c9e296f1-1.png)


#### 工具栏


工具栏最核心的三个动作：


- **插入 (`+`)：** 在当前单元格下方"加一行"。
- **控制 (剪刀、复制、粘贴)：** 用于调整代码块的顺序。
- **运行逻辑：** `Run **( ▶ )**` 执行当前块；`Interrupt` ( ■ ) 强制停止报错的代码；`Restart` ( ↻ ) 相当于给大脑断电重启，清空所有已运行的变量。


![](https://www.runoob.com/wp-content/uploads/2026/01/c6b9cc85-220e-49d8-a27a-9dfae7d11ace.png)


#### 单元格（Cell


单元格是 Jupyter 的灵魂，它有两种身份：


- **Code 模式：** * 左侧有 `In [数字]`。**数字非常重要**：它代表了代码执行的先后顺序*。
- 例如：你在第 1 个单元格定义了 `a = 10`，那么在第 4 个单元格写 `print(a)` 也是能跑通的，只要你运行的先后顺序对。


![](https://www.runoob.com/wp-content/uploads/2026/01/681938a0-b475-424c-8611-9b6ca858c2a9.png)


- **Markdown 模式：** 左侧没有 `In [ ]`。写完后运行，它会瞬间从原始文本变成带有标题、加粗、甚至数学公式的精美文档。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-8.png)


单元格右侧可以对单元格进行位置移动等操作：


![](https://www.runoob.com/wp-content/uploads/2026/01/b0fff265-0364-4fc6-8720-69e2678c0fd5.png)


#### 右上角：内核状态指示灯


- **空心圆 ( ○ )**：大脑正闲着，等候指令。
- **实心黑圆 ( ● )**：大脑正飞速运转（计算中）。
- **No Kernel / Python 3**：如果显示 No Kernel，点击它重新连接，否则代码无法运行。


![](https://www.runoob.com/wp-content/uploads/2026/01/10217eb0-197d-44c1-8bc3-a42c01c62aa8.png)








	  AI 思考中...





			** [Jupyter Notebook 中文设置](https://www.runoob.com/jupyter-notebook-chinese.html)
			[VS Code 中使用 Jupyter Notebook](https://www.runoob.com/jupyter-notebook-vscode.html) **













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