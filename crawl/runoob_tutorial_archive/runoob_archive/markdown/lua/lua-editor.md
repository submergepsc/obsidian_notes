# Lua 编辑器

- Source: https://www.runoob.com/lua/lua-editor.html

可以使用专业的编辑器来编辑 Lua，为大家推荐几款常用的编辑器：


- VS Code：[https://code.visualstudio.com/](https://code.visualstudio.com/)
- **阿里 Qoder：**[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- **字节 Trae：**[https://www.trae.com.cn/](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


你可以从以上软件的官网中下载对应的软件，按步骤安装即可。


接下来我们将为大家演示如何使用 Qoder 工具来编写 Lua 代码。


Qoder 是基于 VSCode 开源框架打造的 AI 编程平台，本章节我们将介绍使用 Qoder 开发 Lua。


Qoder（/ˈkoʊdər/）是一款面向真实软件开发的 Agentic 编码平台,通过增强上下文工程与智能体无缝结合，全面理解你的代码库，并以系统化方式推进开发任务。


Qoder 提供代码智能生成、智能问答、多文件修改、编程智能体等能力，思考更深入、编码更高效、构建更出色，为开发者带来高效、流畅的编码体验。


**Qoder 个人版目前向所有用户提供免费试用。**


---


## 1、注册并安装 Qoder


**首先访问 [**https://qoder.com/**](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz) 注册 Qoder 账号，注册完成后点击右上角的**下载**按钮，根据你的电脑系统，下载安装程序。**


![](https://www.runoob.com/wp-content/uploads/2026/01/1d73bf5c-6bb9-417c-abbf-75987b0b4459.png)


下载后，双击文件开始安装，然后，双击 Qoder IDE 图标启动 Qoder。


相关链接：


- Qoder 官网：[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- Qoder 文档：[https://docs.qoder.com/zh/quick-start](https://docs.qoder.com/zh/quick-start)
- Qoder 命令行工具：[https://docs.qoder.com/zh/cli/quick-start](https://docs.qoder.com/zh/cli/quick-start)


---


## 2、登录 Qoder


在 Qoder IDE 右上角，点击用户图标，或使用键盘快捷键（⌘ ⇧ ,（macOS）或 Ctrl Shift ,（Windows）），然后选择 登录。


![](https://www.runoob.com/wp-content/uploads/2026/01/6936bbe1-f329-47c3-b45c-f6dab7dadcdb.png)


如果还没账号，可以在打开的网页中点击底部的**立即注册**链接注册个账号，或使用 Google 或 GitHub 账号直接注册。


![](https://www.runoob.com/wp-content/uploads/2026/01/3afcda57-995c-4540-b22e-7c8527b3ccde.png)


登录成功后，就会返回 Qoder IDE 后，然后我们可以自由使用所有功能。


![](https://www.runoob.com/wp-content/uploads/2026/01/6d00865f-8911-4277-b635-26b50fc8e14b.png)


整个界面上看，Qoder 操作上跟 VS Code 基本也没区别，本身 Qoder 是基于 VSCode 打造的，所以熟悉 VS Code 的用起来也轻车熟路。


点击右侧扩展按钮，安装 Lua 扩展：


![](https://www.runoob.com/wp-content/uploads/2026/03/6864a438-8773-4681-b7b5-d0245fd3fc3b.png)


### 创建 Lua 项目


创建项目目录：


mkdir lua-runoob-test

进行项目目录：


```
cd lua-runoob-test
```


使用 qoder 命令启动该 lua 项目：


```
qoder .
```


Qoder 就会打开该项目，我们创建文件 main.lua，输入以下代码：


```
print("Hello Lua")

local function add(a,b)
    return a+b
end

print(add(3,5))
```


![](https://www.runoob.com/wp-content/uploads/2026/03/fa755873-548d-4545-aa16-e73910c44f54.png)


运行程序：


```
lua main.lua
```


输出：


```
Hello Lua
```









	  AI 思考中...





			** [Lua goto 语句](https://www.runoob.com/lua-goto.html)














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