# OpenCode 第一次使用

- Source: https://www.runoob.com/opencode/opencode-first-usage.html

安装了 Claude Code 及配置好 API 后，我们就可以开始使用了。


可以先进入项目目录：


```
cd /path/to/project
```


然后运行 OpenCode：


```
opencode
```


运行以下命令为项目初始化 OpenCode：


```
/init
```


OpenCode 会分析你的项目并在项目根目录创建一个 AGENTS.md 文件。


退出 OpenCode，使用以下命令：


```
/exit
```


接下来，我们用一个最简单的示例项目来完成第一次使用。


创建一个示例项目：


```
mkdir opencode-runoob-test
cd opencode-runoob-test
```


然后运行 OpenCode：


```
opencode
```


运行以下命令为初始化：


```
/init
```


![](https://www.runoob.com/wp-content/uploads/2026/04/c0c597ec-ff5a-40a9-9d46-de9eb41d5d20.png)


创建一个简单文件：


```
touch main.py
```


写入以下内容：


```
def add(a, b):
    return a + b
```


### 让 OpenCode 解释代码


输入：


```
解释 main.py 这个文件在做什么，用新手能理解的方式说明
```


OpenCode 会读取当前目录下的代码，并给出解释。


![](https://www.runoob.com/wp-content/uploads/2026/04/10ce95d7-d9c7-4172-a191-cd1fc77a8f4b.png)


### 让 OpenCode 帮你改代码


继续在 OpenCode 会话中输入：


```
给这个函数增加类型注解，并补充基本的错误处理
```


OpenCode 会给出修改建议，通常包含：



- 修改后的代码
- 修改原因说明


![](https://www.runoob.com/wp-content/uploads/2026/04/e2ea67f5-1ea9-4e2f-81b8-732072231464.png)


### @ 符号

使用 `@` 可以快速搜索并引用项目中的文件不需要手动复制代码，适合理解陌生项目。 比如 @main.py 就可以关联到这个文件：


![](https://www.runoob.com/wp-content/uploads/2026/04/2d999b3f-df4e-44a7-96e9-dde33187a1e7.png)


---


## OpenCode 的基本交互方式


### 常见指令类型


你可以把对 Claude Code 的指令分为三类：


**1、解释型**


```
解释这段代码

这个函数为什么这么写
```


** 2、修改型**


```
帮我重构这个函数

拆分成多个小函数
```


**3、生成型**


```
补一个测试用例

增加日志输出
```


一个简单但好用的指令模板：


```
在不改变现有行为的前提下，
帮我优化 XXX 文件的可读性，
并说明你做了哪些修改。
```


---


## 添加新功能（推荐流程）


对于复杂需求，建议采用三步法：


- 先制定计划
- 再优化方案
- 最后执行实现


---


### 1、制定计划（Plan 模式）


按下 `Tab` 键切换到计划模式：


![](https://www.runoob.com/wp-content/uploads/2026/04/11ad82e2-ba2e-4eb5-9aa5-b464bbcd63cf.png)


此时 OpenCode **不会修改代码**，只会给出实现方案。


#### 示例需求


```
当用户删除一条笔记时，我们希望在数据库中将其标记为已删除。
然后新增一个页面，用于展示最近删除的笔记。
在该页面中，用户可以恢复笔记或彻底删除笔记。
```


**说明：**


- 描述越详细，结果越准确
- 可以像和同事沟通一样描述需求


### 2、优化与迭代计划


OpenCode 给出方案后，你可以继续补充：


```
我们希望这个新页面采用之前用过的一套设计。
请参考这张图片，并按该风格实现。
```


**技巧：**


- 可以拖拽图片到终端作为参考
- 可以补充业务规则、UI 要求等


本质就是和 AI 一起做设计评审。


### 3、执行实现（Build 模式）


再次按 **Tab** 切换回执行模式：


然后输入：


```
很好，按照这个方案开始实现吧。
```


OpenCode 会：


- 创建/修改代码
- 更新相关文件
- 执行必要命令


---


## 直接修改（适合简单需求）


对于简单任务，可以跳过计划，直接执行：


```
给 /settings 路由添加认证逻辑。
参考 @packages/functions/src/notes.ts 中的实现方式，
并在 @packages/functions/src/settings.ts 中实现相同逻辑。
```


**建议：**


- 提供参考代码路径
- 说明目标效果


---


## 撤销与重做


如果修改结果不符合预期，可以使用：


### 撤销修改


```
/undo
```


作用：


- 回滚代码改动
- 恢复之前的对话状态


### 重做修改


```
/redo
```


**提示：**


- /undo 可以多次使用
- 适合反复尝试不同方案


---


## 分享对话


你可以将当前会话分享给团队：


```
/share
```


执行后：


- 生成分享链接
- 自动复制到剪贴板


**注意：**


- 对话默认不会自动分享


---


## 使用技巧


### 1、把它当初级工程师


- 说清楚需求
- 提供上下文
- 不要模糊表达


### 2、优先使用计划模式


- 避免错误修改
- 先评审方案再执行


### 3、多用文件引用


- @路径 能大幅提高准确率


### 4、小步迭代


- 不要一次做太复杂的需求
- 拆分任务逐步完成


**OpenCode 的使用本质是：用对话驱动开发流程，而不是手写代码。**








	  AI 思考中...





			** [OpenCode 配置](https://www.runoob.com/opencode-setup.html)
			[VS Code 安装 OpenCode](https://www.runoob.com/opencode-vscode.html) **













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