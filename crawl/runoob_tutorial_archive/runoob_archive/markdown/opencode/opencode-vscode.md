# VS Code 安装 Claude Code

- Source: https://www.runoob.com/opencode/opencode-vscode.html

如果不喜欢使用 OpenCode 的命令行模型，我们可以在 VS Code 编辑器中安装 Claude Code。


打开 VS Code，进入扩展市场，搜索 **OpenCode** 安装：


![](https://www.runoob.com/wp-content/uploads/2026/04/daec2273-e6f5-4ccf-92e7-d597838d8fcf.png)


安装完成后，点击右上角 OpenCode 图标，即可进入 OpenCode 页面：


![](https://www.runoob.com/wp-content/uploads/2026/04/8d93f96c-894b-4b91-85a8-2fd96dc26f31.png)


整个界面如下所示：


![](https://www.runoob.com/wp-content/uploads/2026/04/0da3d682-9db8-4d3c-8136-ce1af124cb07.png)


---

## 其他说明


OpenCode 不仅可以在终端中独立运行，还可以与常见开发工具集成使用，例如 VS Code、Cursor、Windsurf、VSCodium 等。


**只要你的 IDE 支持终端，就可以使用 OpenCode。**


最简单的方式就是：在 IDE 内置终端中运行 `opencode`。


### 一、快速开始


#### 1、启动 OpenCode


在 VS Code 中打开项目后：


- 打开终端（快捷键：**Ctrl + `**）
- 输入以下命令：


```
opencode
```


即可进入 OpenCode 界面。


![](https://www.runoob.com/wp-content/uploads/2026/04/ea24d3dd-786a-434c-bc52-08dad43d1cd3.png) #### 2、快捷启动方式（推荐） | 功能 | Mac | Windows / Linux | | --- | --- | --- | | 快速打开 OpenCode | Cmd + Esc | Ctrl + Esc | | 新建 OpenCode 会话 | Cmd + Shift + Esc | Ctrl + Shift + Esc | **说明：**


- 如果已有会话，快捷键会自动聚焦
- 也可以点击 IDE 中的 OpenCode 按钮


### 二、核心功能


#### 1、上下文感知（非常重要）


OpenCode 会自动获取你当前的开发上下文，例如：


- 当前打开的文件
- 选中的代码
- 当前标签页


这意味着：


- 无需手动复制代码
- AI 可以直接理解你正在编辑的内容


#### 2、文件引用快捷键


你可以通过快捷键快速插入文件引用：


| 系统 | 快捷键 |
| --- | --- |
| Mac | Cmd + Option + K |
| Windows / Linux | Ctrl + Alt + K |


插入效果类似：


```
@File#L37-42
```


表示引用某个文件的指定行范围。


### 三、配置默认编辑器


如果你希望在 OpenCode 中执行 `/editor` 或 `/export` 时使用 VS Code，需要设置环境变量：


```
export EDITOR="code --wait"
```


**说明：**


- `--wait` 表示等待编辑完成后再返回
- 适用于 macOS / Linux









	  AI 思考中...





			** [OpenCode 第一次使用](https://www.runoob.com/opencode-first-usage.html)
			[OpenCode 终端界面](https://www.runoob.com/opencode-tui.html) **













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