# PyCharm 创建与管理项目

- Source: https://www.runoob.com/pycharm/pycharm-new-project.html

在 PyCharm 中，项目（Project） 是最基本的工作单元，它包含源代码、配置、依赖和环境设置。

本节详细介绍如何在 PyCharm 中创建和管理 Python 项目。


---


## 1. 创建新项目


### 1.1 从欢迎界面创建


PyCharm 启动的时候其实已经提供了很多快捷方式：


![](https://www.runoob.com/wp-content/uploads/2025/04/c31948a9-6d25-4e55-b950-62dada2ce023.png)


第一次启动的界面如下：


![](https://www.runoob.com/wp-content/uploads/2025/04/53106b40-5602-4e97-970a-8c7fd92f1f62.png)


点击 "新建项目"（New Project）。


也可以在菜单栏上的文件，点击 "新建项目(New Project)"。


![](https://www.runoob.com/wp-content/uploads/2025/04/02e17dd5-98a7-4f2b-a897-ceaeee48e026.png)


配置项目设置：


**位置（Location）：**选择并设置项目存储路径及名词。


**解释器（Interpreter）：**项目 venv（推荐）。


![](https://www.runoob.com/wp-content/uploads/2025/04/988af3ed-26ac-4c66-98d5-a50d7d7884cf.png)


‌venv‌ 是 Python 中的一个模块，用于创建和管理虚拟环境。虚拟环境是一个隔离的空间，允许你在其中安装和管理 Python 包，而不会影响到系统中的其他Python环境。

venv 是 Python 3.3 及以上版本的标准库，因此不需要额外安装其他工具即可使用‌。


- 项目 venv：虚拟环境默认存储在项目目录下的 venv 文件夹。
- 基础 Conda（如果已安装 Anaconda/Miniconda）
- 自定义环境


** 项目模板：**



- 选择项目类型，如"纯 Python"或"Flask"（适用于 Web 开发）。
- 默认创建 main.py 文件，包含简单的 Python 代码模板（如 print("Hello, World!")）。


### 1.2 从现有代码创建项目


如果已有 Python 代码，可以通过以下方式导入：


**欢迎界面 → "打开"（Open）**，选择项目目录或 **文件 → 打开（File → Open）**，选择项目文件夹。


PyCharm 会自动检测 Python 环境，如果没有，可以手动配置解释器。


![](https://www.runoob.com/wp-content/uploads/2025/04/8b70099e-eb93-42ca-ad13-b8a2745626c2.png)


---


## 2. 项目管理


### 2.1 项目结构（Project Structure）


PyCharm 默认的项目结构如下：


```
my_project/
├── .idea/          # PyCharm 配置文件（如运行配置、版本控制设置）
├── venv/           # 虚拟环境（如果使用 Virtualenv）
├── main.py         # 示例代码（如果勾选了 "创建 main.py"）
└── 其他文件/目录     # 用户创建的代码文件
```


⚠️ 注意：.idea/ 和 venv/ 通常不需要手动修改，PyCharm 会自动管理。


### 2.2 配置 Python 解释器

如果项目需要更换 Python 环境（如从 Python 3.8 切换到 3.10）：

文件 → 设置 → 项目 → Python 解释器（Windows/Linux：Ctrl+Alt+S，macOS：⌘,）。


点击 ⚙️ → 添加解释器（Add Interpreter），选择：


- **虚拟环境（Virtualenv）**（推荐）
- **系统 Python**（直接使用全局 Python）
- **Conda 环境**（如果使用 Anaconda）


选择 Python 版本，点击 "确定"。


### 2.3 运行/调试配置（Run/Debug Configurations）

PyCharm 允许为不同脚本设置不同的运行方式：


- **顶部工具栏 → 运行配置（Run Configurations）** → **"编辑配置"（Edit Configurations）**。
- 点击 **+**，选择 **Python**，配置： - **脚本路径（Script path）**：选择要运行的 `.py` 文件。 - **Python 解释器（Python interpreter）**：确保选择正确的环境。 - **参数（Parameters）**：可输入命令行参数（如 `--port 8000`）。
- 点击 **"应用"（Apply）**，然后可以点击 **▶️ 运行** 或 **🐞 调试**。


---

## 3. 项目常用操作


### 3.1 打开多个项目

PyCharm 默认单项目模式（一次只能打开一个项目），但可以通过以下方式管理多个项目：


- **文件 → 新建 → 项目（File → New → Project）**，创建新项目（PyCharm 会提示是否在新窗口打开）。
- 或 **文件 → 打开（File → Open）**，选择另一个项目目录。


### 3.2 关闭/重新打开项目


- **关闭当前项目**：`文件 → 关闭项目（File → Close Project）`，返回欢迎界面。
- **重新打开最近项目**：欢迎界面会显示 **"最近项目"（Recent Projects）**，点击即可重新打开。


### 3.3 项目依赖管理（requirements.txt / pyproject.toml）


PyCharm 可以自动识别 `requirements.txt` 或 `pyproject.toml` 并安装依赖：


右键 requirements.txt → "同步 Python 依赖"（Sync Python Requirements）。


或终端（Terminal） 运行：


```
pip install -r requirements.txt
```


如果要导出当前环境的依赖：


```
pip freeze > requirements.txt
```


---


## 4. 常见问题

**Q1：PyCharm 无法识别 Python 文件？**


- **检查文件扩展名**：确保是 `.py` 文件。
- **检查解释器配置**：`文件 → 设置 → Python 解释器`，确保已正确设置。


**Q2：如何删除项目？**

PyCharm 不会自动删除项目文件，需要手动：


- **关闭项目**（`文件 → 关闭项目`）。
- **在文件管理器（如 Windows 资源管理器）中删除项目文件夹**。


** Q3：如何备份/分享项目？**


- **推荐方式**：使用 Git（PyCharm 内置 Git 支持）。
- **手动方式**：复制项目文件夹（但建议排除 `.idea/` 和 `venv/`）。








	  AI 思考中...





			** [PyCharm 界面说明](https://www.runoob.com/pycharm-start-intro.html)
			[Pycharm 文件与文件夹操作](https://www.runoob.com/pycharm-file.html) **













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