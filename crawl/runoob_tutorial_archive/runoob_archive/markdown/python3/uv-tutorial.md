# uv 入门教程 -- Python 包与环境管理工具

- Source: https://www.runoob.com/python3/uv-tutorial.html

在 Python 开发中，包管理和环境隔离是每个开发者都会遇到的问题。无论是 pip 的缓慢、virtualenv 的繁琐，还是 conda 的臃肿，**uv** 都让开发者们期待一个更高效的解决方案。


### 什么是 uv？


uv 是由 Astral 公司开发的一款用 Rust 编写的 Python 包管理器和环境管理器，主要目标是提供比现有工具快 10-100 倍的性能，同时保持简单直观的用户体验。


uv 可以替代 pip、virtualenv、pip-tools、pyenv 等工具，提供依赖管理、虚拟环境创建、Python 版本管理等一站式服务。


### uv 的优势


- **速度极快**：由于使用 Rust 编写，uv 的性能远超 pip 和其他包管理工具，安装依赖的速度可以提升 10-100 倍。
- **功能集成**：集依赖解析、包安装、环境管理和 Python 版本管理于一体，无需再安装和学习多个工具。
- **确定性构建**：uv 会生成 `uv.lock` 文件，确保在任何环境中都能安装完全相同的依赖版本，避免"在我机器上能运行"的问题。
- **与现有工具兼容**：uv 可以处理 `requirements.txt` 和 `pyproject.toml`，可以无缝替代现有工作流中的 pip。


---


## 安装 uv


### 在 macOS 上安装


推荐使用 Homebrew 安装：


```
brew install uv
```


或者使用官方安装脚本：


```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### 在 Linux 上安装


```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### 在 Windows 上安装


使用 Winget：


```
winget install uv
```


或者使用官方安装脚本（PowerShell）：


```
irm https://astral.sh/uv/install.ps1 | iex
```


安装完成后，验证是否成功：


```
uv --version
```


输出内容类似如下，表明安装成功：


```
uv 0.8.14 (Homebrew 2025-08-28)
```


---


## 1、管理 Python 版本


uv 内置 Python 版本管理功能，无需额外安装 pyenv 等工具。


查看可用的 Python 版本：


```
uv python list
```


输出结果类似如下：


```
cpython-3.14.0rc2-macos-aarch64-none                 <download available>
cpython-3.13.7-macos-aarch64-none                    <download available>
cpython-3.12.11-macos-aarch64-none                   <download available>
cpython-3.11.13-macos-aarch64-none                   <download available>
cpython-3.10.18-macos-aarch64-none                   <download available>
cpython-3.9.6-macos-aarch64-none                     /usr/bin/python3
pypy-3.11.13-macos-aarch64-none                      <download available>
```


安装特定版本的 Python：


```
# 安装最新的 Python 3.12
uv python install 3.12

# 安装特定版本
uv python install 3.11.6

# 安装 PyPy 版本
uv python install pypy3.10
```


设置全局默认 Python 版本：


```
uv python default 3.12
```


为当前项目固定 Python 版本（会创建 `.python-version` 文件）：


```
uv python pin 3.12
```


执行这个命令后，当前项目下就会生成一个 .python-version，打开后，显示版本号内容：


```
3.12
```


---


## 2、管理虚拟环境


创建虚拟环境：


```
# 在当前目录创建名为 .venv 的虚拟环境（使用系统默认 Python）
uv venv

# 使用指定 Python 版本创建虚拟环境
uv venv --python 3.12
```


激活虚拟环境：


```
# macOS / Linux
source .venv/bin/activate

# Windows（PowerShell）
.venv\Scripts\activate
```


退出虚拟环境：


```
deactivate
```


**
日常开发中可以使用 `uv run` 直接运行脚本，无需手动激活虚拟环境。


---


## 3、包管理（pip 兼容模式）


uv 提供了与 pip 完全兼容的命令接口，可以直接替换已有工作流中的 pip 命令：


安装包：


```
# 安装最新版本
uv pip install requests

# 安装特定版本
uv pip install requests==2.31.0

# 从 requirements.txt 批量安装
uv pip install -r requirements.txt
```


升级包：


```
uv pip install --upgrade requests
```


卸载包：


```
uv pip uninstall requests
```


查看已安装的包：


```
uv pip list
```


导出当前环境的依赖到 requirements.txt：


```
uv pip freeze > requirements.txt
```


---


## 4、项目管理（推荐方式）


uv 支持以 `pyproject.toml` 为中心的现代项目管理方式，这是比 pip 模式更推荐的使用方法，尤其适合团队协作和多环境部署。


### 初始化项目


```
uv init my_project
cd my_project
```


这会创建以下基本项目结构：


```
my_project/
├── pyproject.toml    # 项目配置和依赖声明
├── .python-version   # 固定 Python 版本
├── README.md
└── main.py
```


### 添加和移除依赖


在项目模式下，推荐使用 `uv add` 和 `uv remove` 管理依赖，它们会自动更新 `pyproject.toml` 和 `uv.lock`：


```
# 添加生产依赖
uv add requests

# 添加指定版本的依赖
uv add "requests>=2.31.0"

# 添加开发依赖（只在开发环境使用，如测试框架）
uv add --dev pytest ruff

# 移除依赖
uv remove requests
```


### 安装项目全部依赖（uv sync）


克隆项目或更新 `pyproject.toml` 后，运行以下命令一键安装所有依赖：


```
uv sync
```


> uv sync 说明：**类似于 `pip install -r requirements.txt`，它会根据 `pyproject.toml` 和 `uv.lock` 安装所有依赖，确保环境与其他开发者完全一致。如果安装速度慢，可以在 `pyproject.toml` 中设置国内镜像源：
>
>
```
[tool.uv]
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```


### 生成/更新锁文件


```
uv lock
```


该命令会解析 `pyproject.toml` 中的依赖并生成（或更新）`uv.lock` 文件。`uv.lock` 应该提交到版本库，确保团队所有成员使用完全相同的依赖版本。


---


## 5、运行脚本（uv run）


`uv run` 是 uv 中非常实用的命令，可以**无需手动激活虚拟环境**直接运行脚本或命令，uv 会自动找到并使用正确的环境：


```
# 直接运行 Python 脚本
uv run main.py

# 运行项目中的测试
uv run pytest

# 运行任意命令（在虚拟环境的上下文中执行）
uv run python -c "import requests; print(requests.__version__)"
```


使用 `uv run` 相比手动激活环境的优势：不会误用错误的 Python 版本，也不会忘记激活环境导致包找不到，特别适合在 CI/CD 和脚本自动化中使用。


---


## 迁移到 uv


如果你正在使用其他工具，可以按以下方式迁移到 uv：


**从 pip + virtualenv 迁移：**


```
# 创建并激活虚拟环境
uv venv
source .venv/bin/activate

# 安装原有依赖
uv pip install -r requirements.txt
```


**从 pip-tools 迁移：**


```
# 编译依赖（替代 pip-compile）
uv pip compile requirements.in -o requirements.txt

# 同步环境（替代 pip-sync）
uv pip sync requirements.txt
```


**从 poetry 或 pdm 迁移：**


```
# 直接使用现有的 pyproject.toml
uv sync
```









	  AI 思考中...





			** [Python 类型注解（Type Hints）](https://www.runoob.com/python-type-hints.html)
			[Python OpenAI](https://www.runoob.com/python-openai.html) **













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