# OpenCode CLI 使用

- Source: https://www.runoob.com/opencode/opencode-cli.html

OpenCode 提供了强大的命令行接口（CLI），不仅可以启动交互式 TUI，还可以通过命令实现自动化、脚本化操作。


**默认情况下，OpenCode CLI 会启动 TUI，但它的真正能力在于"可编程调用"。**


**OpenCode CLI 不只是一个命令工具，而是一个可编程的 AI 开发接口。**


---


## 一、基础用法


### 1、启动 TUI（默认行为）


```
opencode
```


等同于进入交互式终端界面


### 2、指定项目目录


```
opencode /path/to/project
```


在指定目录中启动 TUI


### 3、非交互模式（脚本调用）


```
opencode run 解释一下 JavaScript 中闭包的原理
```


直接返回结果，不进入界面


---


## 二、CLI 核心能力


OpenCode CLI 的核心能力可以总结为三类：


- **交互模式：**TUI（默认）
- **命令执行：**run / serve
- **系统管理：**agent / auth / session 等


---


## 三、常用参数（Flags）


| 参数 | 简写 | 说明 |
| --- | --- | --- |
| --continue | -c | 继续上一个会话 |
| --session | -s | 指定会话 ID |
| --fork |  | 从当前会话分叉 |
| --model | -m | 指定模型（provider/model） |
| --agent |  | 指定代理 |
| --port |  | 服务端口 |
| --hostname |  | 监听地址 |


---


## 四、核心命令详解


### 1、run（最常用）


用于非交互执行：


```
opencode run 分析这个 Go 项目的上下文使用方式
```


**适用场景：**


- 脚本自动化
- CI/CD
- 快速问答


### 连接后台服务（避免冷启动）


```
# 启动后台服务
opencode serve

# 使用 run 连接
opencode run --attach http://localhost:4096 解释 async/await
```


### 常用参数


| 参数 | 说明 |
| --- | --- |
| --model | 指定模型 |
| --file | 附加文件 |
| --format | 输出格式（json / 默认） |
| --share | 分享会话 |


## 五、auth（认证管理）


### 登录


```
opencode auth login
```


配置 API Key（存储在本地）


---


### 查看已登录提供商


```
opencode auth list
```


### 退出登录


```
opencode auth logout
```


---


## 六、models（模型管理）


### 查看所有模型


```
opencode models
```


### 按提供商筛选


```
opencode models anthropic
```


### 刷新模型列表


```
opencode models --refresh
```


---


## 七、agent（代理系统）


### 创建代理


```
opencode agent create
```


可自定义提示词 + 工具


### 查看代理


```
opencode agent list
```


---


## 八、session（会话管理）


### 查看会话


```
opencode session list
```


### 限制数量


```
opencode session list -n 10
```


---


## 九、serve（服务模式）


启动 API 服务：


```
opencode serve
```


提供 HTTP 接口（无界面）


**可选参数：**


- --port：端口
- --hostname：监听地址


---


## 十、web（Web UI）


```
opencode web
```


启动带网页界面的版本


---


## 十一、mcp（扩展能力）


### 添加 MCP 服务


```
opencode mcp add
```


### 查看列表


```
opencode mcp list
```


MCP 用于扩展 AI 能力（如工具调用）


---


## 十二、stats（使用统计）


```
opencode stats
```


查看 Token 使用量与费用


---


## 十三、export / import


### 导出会话


```
opencode export
```


### 导入会话


```
opencode import session.json
```


---


## 十四、升级与卸载


### 升级


```
opencode upgrade
```


### 卸载


```
opencode uninstall
```


---


## 十五、全局参数


| 参数 | 说明 |
| --- | --- |
| --help | 查看帮助 |
| --version | 查看版本 |
| --log-level | 日志级别 |


---


## 十六、环境变量（高级配置）


OpenCode 支持通过环境变量控制行为，例如：


```
OPENCODE_DISABLE_AUTOUPDATE=true
OPENCODE_SERVER_PASSWORD=123456
```


**常见用途：**


- 关闭自动更新
- 配置服务认证
- 自定义配置路径


---


## 十七、使用建议（重点）


- 日常开发使用 TUI
- 自动化使用 run
- 复杂任务结合 agent
- 高频调用使用 serve + attach










	  AI 思考中...





			** [OpenCode 终端界面](https://www.runoob.com/opencode-tui.html)
			[OpenCode Web 使用](https://www.runoob.com/opencode-web.html) **













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