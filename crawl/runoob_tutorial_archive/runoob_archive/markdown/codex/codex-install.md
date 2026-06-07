# Codex 安装与使用

- Source: https://www.runoob.com/codex/codex-install.html

Codex 可以通过多种方式使用，根据开发者的习惯，大致可以分为五种方式：


| 安装方式 | 使用场景 | 推荐程度 |
| --- | --- | --- |
| Codex 应用 | 直接下载 Codex 应用 | ⭐⭐⭐⭐ |
| Codex CLI | 在终端使用 | ⭐⭐⭐⭐⭐ |
| IDE 插件 | 在 VS Code / Cursor 使用 | ⭐⭐⭐⭐ |
| Homebrew 安装 | Mac 用户 | ⭐⭐⭐⭐ |
| GitHub Release 二进制 | 手动安装 | ⭐⭐⭐ |


![](https://www.runoob.com/wp-content/uploads/2026/03/codex-four-ways.svg)


接下来分别介绍。


---


## 1、Codex 应用


最简单的方式就是 **直接使用 Codex 应用**，需要好的网络连接。


访问：[https://chatgpt.com/codex](https://chatgpt.com/codex)


下载应用：


![](https://www.runoob.com/wp-content/uploads/2026/03/831e8eed-fe85-4706-b00d-585cae8e0bdb.png)


登录 ChatGPT 账号即可使用。


界面说明：


![](https://www.runoob.com/wp-content/uploads/2026/03/65a8928c-4085-426b-b009-1323232dc6ec.png)


然后可以输入框输入我们的需求：


![](https://www.runoob.com/wp-content/uploads/2026/03/1a6e68e2-0471-473c-b92a-2f0b87781ef5.png)


支持计划：


- ChatGPT Plus
- ChatGPT Pro
- ChatGPT Business
- ChatGPT Edu
- ChatGPT Enterprise


Web 版的特点：


- 不需要本地环境
- 直接连接 GitHub
- 任务在云端运行
- 可以自动创建 PR


适合：


- 快速体验 Codex
- 代码审查
- 代码库分析


---


## 2、Codex CLI（最常用） 开发者最常用的方式是 Codex CLI。 CLI 是一个运行在终端中的 AI 编程代理，可以： 阅读代码 修改代码 执行 shell 命令 自动修复 bug Codex CLI 在本地运行，因此代码不会被上传到云端，只有 prompt 和必要的上下文会发送给模型。 ### 安装 Codex CLI 使用 npm 安装：
```
sudo npm install -g @openai/codex

# 使用国内镜像安装更快
sudo npm install -g @openai/codex --registry=https://registry.npmmirror.com
```
 安装完成后运行：
```
codex
```
 即可启动 Codex。 ### 登录 Codex 首次运行需要登录。 有两种方式： #### 方法一：ChatGPT 登录（推荐）
```
codex
```
 选择：
```
Sign in with ChatGPT
```
 然后浏览器会打开登录页面。 登录完成即可使用。 #### 方法二：API Key 登录 如果是开发者模式，可以使用 API Key：
```
# macOS / Linux - 临时设置（仅当前终端会话有效）
export OPENAI_API_KEY="sk-你的API密钥"

# 永久配置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export OPENAI_API_KEY="sk-你的API密钥"' >> ~/.zshrc
source ~/.zshrc

# Windows PowerShell
$env:OPENAI_API_KEY="sk-你的API密钥"

# 配置后启动（指定模型）
codex --model gpt-5-codex
```
 然后运行：
```
codex
```
 #### 方式三：auth.json 文件配置 手动编辑认证文件, 创建目录:
```
mkdir -p ~/.codex
```
 写入 API key:
```
cat > ~/.codex/auth.json << 'EOF'
{
  "OPENAI_API_KEY": "sk-你的API密钥"
}
EOF
```
 ### 第一次运行 Codex 进入项目目录：
```
cd my-project
```
 启动 Codex：
```
codex
```
 然后输入：
```
分析下当前的项目结构
```
 Codex 会自动： 扫描代码库 分析项目结构 输出系统架构说明 例如，我们创建一个目录：
```
mkdir codex-runoob-test
```
 进入目录：
```
cd codex-runoob-test
```
 新建 test.py 文件，代码如下：
```
print("Hello Runoob!")
```
 启动 Codex：
```
codex
```
 选第一个 Yes, continue 回车，这样就可以开始使用 Codex Cli 开始写代码了: ### Codex 的三种运行模式 Codex CLI 提供三种安全模式。 模式 功能 Suggest 只建议修改 Auto Edit 自动修改文件 Full Auto 自动执行所有操作 默认模式：
```
Suggest
```
 切换模式：
```
codex --auto-edit
```
 或者：
```
codex --full-auto
```
 Full Auto 模式可以自动执行代码修复和任务。 ### 更新与卸载
```
# 更新到最新版本
npm update -g @openai/codex

# 或强制重装最新版
npm install -g @openai/codex@latest

# 卸载
npm uninstall -g @openai/codex

# Homebrew 卸载
brew uninstall --cask codex
```
 3、Homebrew 安装（Mac 推荐） Mac 用户可以使用 Homebrew 安装。
```
brew install --cask codex
```
 安装完成后运行：
```
codex
```
 即可启动。 这种方式适合： Mac 开发者 不想安装 Node.js 的用户。 GitHub Release 安装（二进制）


如果不想使用 npm，也可以直接下载二进制版本。


下载地址：[https://github.com/openai/codex/releases](https://github.com/openai/codex/releases)


常见版本：

Mac Apple Silicon：


```
codex-aarch64-apple-darwin.tar.gz
```


Mac Intel：


```
codex-x86_64-apple-darwin.tar.gz
```


Linux：


```
codex-x86_64-unknown-linux-musl.tar.gz
```


下载后解压：


```
tar -xzf codex-xxx.tar.gz
```


重命名：


```
mv codex-x86_64-unknown-linux-musl codex
```


加入 PATH：


```
sudo mv codex /usr/local/bin
```


然后运行：


```
codex
```


即可使用。


---


## 5、IDE 插件安装


Codex 还可以在 IDE 中使用，例如：


- VS Code
- Cursor
- Windsurf
- VS Code forks


安装方式：

- 1. 打开 IDE 插件市场
- 2. 搜索 **Codex**
- 3. 安装插件
- 4. 登录 ChatGPT 账号


![](https://www.runoob.com/wp-content/uploads/2026/03/d57e8d8d-80d5-4c8d-94e7-6cdf3597a6ae.png)


这样可以在 IDE 内直接使用 Codex。


例如：


- 自动修复代码
- 自动生成函数
- 自动重构代码


---


## 6、更新 Codex


Codex CLI 更新非常简单：


```
codex --upgrade
```


或者：


```
npm update -g @openai/codex
```


```
codex --version
```


Codex CLI 目前支持：


| 系统 | 支持情况 |
| --- | --- |
| macOS | 完整支持 |
| Linux | 完整支持 |
| Windows | 实验支持（建议 WSL） |









	  AI 思考中...





			** [CodeX 简介](https://www.runoob.com/codex-intro.html)
			[Codex 基础入门](https://www.runoob.com/codex-usage.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#83e2e7eeeaedc3f1f6edecece1ade0ecee)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **