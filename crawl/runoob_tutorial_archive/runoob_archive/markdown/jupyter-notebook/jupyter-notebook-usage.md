# Jupyter Notebook 使用

- Source: https://www.runoob.com/jupyter-notebook/jupyter-notebook-usage.html

上一章节我们已经完成了 Jupyter Notebook 的安装。


安装完成后，让我们立即启动它，看看这个智能笔记本长什么样。


### 1. 启动 Jupyter Notebook


首先，在命令行中，切换到你希望存放未来笔记本项目文件的目录。例如，你想在桌面的 `my_jupyter` 文件夹里工作：


```
# Windows 示例
cd C:\Users\你的用户名\Desktop\my_jupyter

# macOS/Linux 示例
cd ~/Desktop/my_jupyter
```


然后，输入启动命令：


```
jupyter notebook
```


按下回车后，会发生两件事：


命令行窗口会开始运行一个服务器（不要关闭这个窗口）。


![](https://www.runoob.com/wp-content/uploads/2026/01/f79223e4-9cb5-43da-b132-6376e5c2d67f.png)


默认网页浏览器（如 Chrome， Firefox）会自动打开一个新页面，地址通常是 `http://localhost:8888`，这个就是 **Jupyter Notebook 的仪表盘**

![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-1.png)


这时候就可以点 File（文件） -> New（新建） -> Notebook（笔记本） 来创建 notebook 来创建：


![](https://www.runoob.com/wp-content/uploads/2026/01/f8594e58-089c-44ac-9a9d-40c3145a80e1.png")


也可以用过以下方式。


### 2. 创建你的第一个笔记本


在打开的浏览器页面（仪表盘）中：


- 点击页面右上角的 **New** 按钮。
- 在下拉菜单中选择 **Python 3 (ipykernel)**。 ![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-2.png)
- 这时，一个新的浏览器标签页会打开，这就是一个全新的、空白的 **Notebook 文档**。![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-3.png)


### 3. 编写并运行第一段代码


你现在看到的是一个单元格，这是 Notebook 的核心。


- 在第一个单元格里输入：
```
print("Hello, Jupyter! I am from Runoob!")
```

- 按 `Shift + Enter` 键来运行这个单元格。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-4.png)


你会立刻在单元格下方看到输出结果 `Hello, Jupyter! I am from Runoob!`，同时界面会自动为你创建第二个空白单元格。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-5.png)


完成后，会重新生成一个单元格，在下面贴入以下代码：


## 实例


```
# 这是一个代码单元格
print("Hello, Jupyter!")
print("1 + 2 =", 1 + 2)

# 尝试运行这个单元格（Shift+Enter），看看结果吧！
```


**预期运行结果**：


```
Hello, Jupyter!
1 + 2 = 3
```


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-6.png)


### 4. 了解单元格类型


单元格有两种主要模式（通过工具栏下拉菜单切换）：


- **Code**：用于编写和执行代码（默认）。
- **Markdown**：用于编写带格式的文本说明。例如，你可以输入 `# 这是标题`，然后运行（Shift+Enter），它就会显示为大标题。

![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-7.png)


尝试将一个新单元格的类型改为 **Markdown**，然后输入 `## 这是我的数据分析项目`，运行它看看效果。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-8.png)


### 5. 保存与关闭


- **保存**：Notebook 会自动定时保存，你也可以点击工具栏的 **保存图标**（软盘形状）手动保存。你的笔记本会被保存为后缀名为 `.ipynb` 的文件。
- **关闭**：直接关闭浏览器标签页即可关闭笔记本。要**停止整个 Jupyter 服务**，回到最初那个命令行窗口，按两次 `Ctrl + C`，然后根据提示确认关闭。


![](https://www.runoob.com/wp-content/uploads/2026/01/jupyter-install-runoob-9.png)








	  AI 思考中...





			** [Jupyter Notebook 安装](https://www.runoob.com/jupyter-notebook-install.html)
			[Jupyter Notebook 中文设置](https://www.runoob.com/jupyter-notebook-chinese.html) **













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