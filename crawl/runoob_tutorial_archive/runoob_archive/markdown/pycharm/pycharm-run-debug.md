# PyCharm 运行与调试

- Source: https://www.runoob.com/pycharm/pycharm-run-debug.html

PyCharm 提供了强大的运行和调试工具，帮助开发者高效执行和排查 Python 代码问题。本部分将详细介绍环境配置、脚本运行和调试技巧。

---


## 配置运行环境


### 设置 Python 解释器


**打开解释器设置：**设置 → 项目 → Python 解释器（Windows/Linux：Ctrl+Alt+S，Mac：⌘,）。


**选择解释器：**


- **虚拟环境**（推荐）：`Virtualenv` / `Conda` / `Pipenv`
- **系统解释器**：直接使用已安装的 Python
- **远程解释器**：连接服务器或 Docker 环境


![](https://www.runoob.com/wp-content/uploads/2025/04/988af3ed-26ac-4c66-98d5-a50d7d7884cf.png)


**安装依赖包：**


- 在解释器界面点击 `+` 搜索并安装包（如 `requests`）
- 或通过终端运行 `pip install package_name`


![](https://www.runoob.com/wp-content/uploads/2025/04/6850c65f-51c7-481f-95b7-bc9351bf482b.png)


---


## 配置运行参数


**打开运行配置：**


- 顶部工具栏 → `运行 → 编辑配置`（Run → Edit Configurations）
- 或点击运行按钮旁边的配置下拉菜单


![](https://www.runoob.com/wp-content/uploads/2025/04/ffcad3f3-8c5d-4641-9733-54c1b8445fc5.png)


**添加 Python 配置：**点击 + → 选择 Python


![](https://www.runoob.com/wp-content/uploads/2025/04/944807fc-45db-4cc3-ab01-93001ae617d0.png)


**关键参数：**


- **脚本路径**：选择要执行的 `.py` 文件
- **参数（Parameters）**：输入命令行参数（如 `--port 8000`）
- **工作目录**：设置脚本运行时的当前目录
- **环境变量**：添加自定义环境变量（如 `PYTHONPATH`）


![](https://www.runoob.com/wp-content/uploads/2025/04/71a8cb9d-1033-4227-b8c5-e70a7960c4ca.png)


**保存配置：**点击 应用 → 确定。

---


## 运行 Python 脚本


### 单文件运行



**方法一：右键运行**：


- 在编辑器中右键 → `运行 '文件名'`（Run 'filename'）


**方法二：工具栏运行**：


- 点击顶部工具栏的绿色运行按钮 ▶️


**方法三：快捷键运行**：


- `Shift + F10`（运行当前文件）
- `Ctrl + Shift + F10`（运行当前编辑的文件）




![](https://www.runoob.com/wp-content/uploads/2025/04/053dc3e5-17a9-4e1f-aff2-590d8d7e729e.png)


### 模块运行（如 Flask/Django）

**配置模块运行：**在运行配置中选择模块名称而非脚本路径。


例如：


- **模块名**：`flask`
- **参数**：`run --port=5000`


运行带参数的模块：


```
# 例如运行 Django 开发服务器
python manage.py runserver 0.0.0.0:8000
```


在运行配置的 "参数" 栏输入：runserver 0.0.0.0:8000


![](https://www.runoob.com/wp-content/uploads/2025/04/ed31435f-0e8f-47ac-852d-116ac630b151.png)

---


## 调试代码


### 设置断点



**添加断点**：


- 在行号左侧单击（出现红色圆点）
- 右键断点可设置条件（如 `x > 10`）



**断点类型**：


- **行断点**：暂停在指定行
- **异常断点**：在抛出异常时暂停（`运行 → 查看断点 → 添加 Python 异常断点`）



**启动调试**：


- 点击工具栏的 `🐞 调试` 按钮
- 或快捷键 `Shift + F9`


![](https://www.runoob.com/wp-content/uploads/2025/04/py_debug_tool_window.png)


### 变量监视（Watches）



**查看变量**：


- 调试启动后，在 `变量（Variables）` 面板查看当前作用域的变量值
- 双击变量可编辑值（用于临时测试）



**添加监视**：


- 在 `监视（Watches）` 面板点击 `+`
- 输入变量名或表达式（如 `len(items)`）


### 调试控制操作

| 操作 | 快捷键（Win/Linux） | 快捷键（Mac） | 说明 |
| --- | --- | --- | --- |
| 步过（Step Over） | F8 | F8 | 执行当前行，不进入函数内部 |
| 步入（Step Into） | F7 | F7 | 进入函数内部调试 |
| 步出（Step Out） | Shift + F8 | ⇧ + F8 | 执行完当前函数，返回到调用处 |
| 继续（Resume） | F9 | ⌘ + F8 | 继续运行直到下一个断点 |
| 停止（Stop） | Ctrl + F2 | ⌘ + F2 | 终止调试会话 |


### 调试控制台（Debug Console）



**交互式调试**：


- 在调试过程中，可在 `调试控制台` 直接执行 Python 代码
- 例如：临时调用函数或修改变量




**评估表达式**：


- 选中代码 → 右键 → `评估表达式（Evaluate Expression）`
- 或快捷键 `Alt + F8`

---


## 高级调试技巧

### 远程调试



**配置远程解释器**：


- `文件 → 设置 → Python 解释器 → 添加远程解释器`
- 支持 SSH、Docker 和 Vagrant



**调试远程代码**：


- 断点和调试操作与本地调试一致

### 多进程调试



**子进程调试**：


- 在运行配置中勾选 `在子进程中调试（Debug child processes）`
- 适用于 `multiprocessing` 或 `subprocess` 场景



**附加到进程**：


- `运行 → 附加到本地进程（Attach to Local Process）`
- 选择正在运行的 Python 进程


---


## 常见问题解决


### Q1：断点不生效？


- 检查解释器是否匹配项目环境
- 确保代码已保存（`Ctrl + S`）
- 检查断点是否被禁用（断点图标为灰色）


### Q2：如何调试单元测试？


- 在测试文件中右键 → `调试 '测试名'`
- 或使用 `pytest` / `unittest` 专用运行配置


### Q3：调试时变量显示 "Unknown"？


- 优化代码结构，避免过于复杂的表达式
- 使用 `Watches` 手动添加监视变量


---


## 调试快捷键



| 场景 | 操作 |
| --- | --- |
| 快速运行当前文件 | Shift + F10 |
| 启动调试 | Shift + F9 |
| 条件断点 | 右键断点 → 设置条件 |
| 查看变量值 | 调试时在 Variables 面板查看 |
| 临时执行代码 | 调试控制台输入命令 |
| 多进程调试 | 运行配置中勾选 Debug child processes |








	  AI 思考中...





			** [PyCharm 代码编辑](https://www.runoob.com/pycharm-code-editor.html)
			[PyCharm 版本控制集成](https://www.runoob.com/pycharm-git.html) **













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