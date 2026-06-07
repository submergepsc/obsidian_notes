# OpenCode 安装

- Source: https://www.runoob.com/opencode/opencode-install.html

OpenCode 是一个开源的 AI 编程 Agent，支持在终端中直接完成代码理解、修改、执行等开发任务。


相比传统 AI 工具，OpenCode 可以直接参与开发流程，而不仅仅是生成代码。


在安装之前，需要确保你的环境满足以下条件：


### 1、操作系统要求


- macOS
- Linux
- Windows（推荐使用 WSL）


### 2、终端工具


需要一个现代终端，例如：

- WezTerm（跨平台）：[https://wezterm.org/](https://wezterm.org/)
- Alacritty（跨平台）：[https://alacritty.org/](https://alacritty.org/)
- Ghostty（Linux/macOS）：[https://ghostty.org/](https://ghostty.org/)
- Kitty（Linux/macOS）：[https://github.com/kovidgoyal/kitty](https://github.com/kovidgoyal/kitty)


### 3、API Key


OpenCode 本身不提供模型，需要你配置 AI 服务商（后文会详细介绍）：


- OpenAI（GPT）
- Anthropic（Claude）
- Google（Gemini）
- DeepSeek
- 阿里百炼
- GLM
- MiniMax


---


## 安装方式


OpenCode 提供多种安装方式，推荐优先使用官方脚本。


## 1、一键安装（推荐）


```
curl -fsSL https://opencode.ai/install | bash
```


说明：


- 自动下载最新版本
- 自动配置环境
- 适用于 macOS / Linux / WSL

安装完成后，还会提示你怎么用，OpenCode 包含免费模式，使用方式：


```
cd <project>  # 进入项目目录
opencode      # 启动 OpenCode
```


![](https://www.runoob.com/wp-content/uploads/2026/04/af06eb8e-3cdf-4a7e-aa59-cd6fd4c4bf34.png)


### 2、使用 Node.js 安装


如果你熟悉 Node.js，可以使用：


```
npm install -g opencode-ai
```


或者：


```
pnpm install -g opencode-ai
```


或者：


```
yarn global add opencode-ai
```


### 3、macOS（Homebrew）


```
brew install anomalyco/tap/opencode
```


说明：


- 推荐使用官方 tap（更新更快）
- `brew install opencode` 更新较慢


### 3、Windows 安装


### 推荐方式：WSL


原因：


- 更稳定
- 完整支持所有功能

使用 Chocolatey：


```
choco install opencode
```


使用 Scoop：


```
scoop install opencode
```


使用 NPM：


```
npm install -g opencode-ai
```


使用 Mise：


```
mise use -g github:anomalyco/opencode
```


使用 Docker：


```
docker run -it --rm ghcr.io/anomalyco/opencode
```


你也可以从 Releases 页面 [https://github.com/anomalyco/opencode/releases](https://github.com/anomalyco/opencode/releases)直接下载二进制文件。


### 4、Linux 安装


通用方式（推荐）：


```
curl -fsSL https://opencode.ai/install | bash
```


Arch Linux：


```
sudo pacman -S opencode
```


或：


```
paru -S opencode-bin
```


Docker（进阶）：


```
docker run -it --rm ghcr.io/anomalyco/opencode
```


---


## 验证安装


安装完成后，执行：


```
opencode --version
```


如果输出类似：


```
1.1.50
```


说明安装成功。


---


## 启动 OpenCode


直接运行：


```
opencode
```

**

如果出现 EACCES: permission denied, open ''** 是权限问题，我们可以修复目录权限：


```
sudo chown -R $(whoami) ~/.local
```


然后执行：


```
chmod -R 755 ~/.local
```


你会看到终端界面（TUI）:


![](https://www.runoob.com/wp-content/uploads/2026/04/f0d7fd3e-9f67-4c55-ab21-bd08ebc9a09e.png)


打开后，你就可以在这个界面提问了。









	  AI 思考中...





			** [OpenCode 简介](https://www.runoob.com/opencode-intro.html)
			[OpenCode 配置](https://www.runoob.com/opencode-setup.html) **













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