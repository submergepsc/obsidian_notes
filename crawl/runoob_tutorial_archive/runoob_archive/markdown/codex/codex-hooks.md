# Codex 规则与钩子

- Source: https://www.runoob.com/codex/codex-hooks.html

通过规则（Rules）和钩子（Hooks），你可以自定义 Codex 的行为，使其更好地适应你的工作流程。本节详细介绍这两个功能。


---


## 规则（Rules）


规则允许你为 Codex 定义自定义的行为指南，应用于所有对话。


### 规则文件位置


Codex 从以下位置加载规则：


- `~/.codex/rules/` - 用户级别规则
- `{项目}/.codex/rules/` - 项目级别规则


### 规则文件格式


## 创建规则文件


```
# 我的编码规则

## 代码风格
- 使用 4 空格缩进
- 每行最多 100 个字符
- 始终使用 const/let，不使用 var

## 注释规范
- 公共函数必须包含 JSDoc 注释
- 复杂逻辑添加行内注释说明
- 删除所有调试用的 console.log

## 测试要求
- 所有新功能必须包含测试用例
- 测试文件命名：*.test.js 或 *.spec.js

## Git 提交
- 提交信息使用Conventional Commits格式
- 提交前运行 lint 和测试
```


### 启用规则


## 在配置中启用规则


```
[features]
codex_hooks = true
```


**规则会被注入到每个对话的系统提示中，确保 Codex 始终遵循你的编码规范。


---


## 钩子（Hooks）


钩子允许你在特定事件发生时执行自定义操作。


### 钩子文件位置


钩子在 `~/.codex/hooks.json` 中配置：


## 创建钩子配置


```
{
  "hooks": [
    {
      "event": "on_tool_call",
      "match": "shell",
      "action": "allow"
    },
    {
      "event": "on_task_complete",
      "action": "notify",
      "command": "echo 'Task completed'"
    }
  ]
}
```


### 可用事件


| 事件 | 说明 |
| --- | --- |
| on_tool_call | 工具调用前触发 |
| on_task_start | 任务开始时触发 |
| on_task_complete | 任务完成时触发 |
| on_error | 发生错误时触发 |
| on_message | 收到消息时触发 |


### 钩子操作


| 操作 | 说明 |
| --- | --- |
| allow | 允许操作继续 |
| deny | 阻止操作 |
| notify | 发送通知 |
| log | 记录日志 |
| custom | 执行自定义脚本 |


> 启用钩子功能需要设置 `[features].codex_hooks = true`


---


## 实战示例


### 示例 1：自动运行测试


每次 Codex 修改文件后自动运行测试：


## 自动测试钩子


```
{
  "hooks": [
    {
      "event": "on_tool_call",
      "match": "edit_file",
      "action": "custom",
      "command": "npm test",
      "timeout": 60
    }
  ]
}
```


### 示例 2：强制代码审查


在提交前强制进行代码审查：


## 代码审查钩子


```
{
  "hooks": [
    {
      "event": "on_tool_call",
      "match": "git_commit",
      "action": "custom",
      "command": "/review",
      "require_approval": true
    }
  ]
}
```


### 示例 3：记录日志


记录所有命令执行：


## 日志钩子


```
{
  "hooks": [
    {
      "event": "on_tool_call",
      "match": "shell",
      "action": "log",
      "log_file": "/tmp/codex-commands.log"
    }
  ]
}
```


---


## 规则与钩子的区别


| 特性 | 规则 | 钩子 |
| --- | --- | --- |
| 作用时机 | 对话开始时 | 事件触发时 |
| 主要用途 | 定义编码规范 | 自动化操作 |
| 配置位置 | rules/ 目录 | hooks.json |


> 规则和钩子可以结合使用：规则定义"怎么做"，钩子定义"什么时候做"。


---


## 最佳实践


### 规则最佳实践


- 保持规则简洁明了
- 避免过于严格的限制
- 根据项目需求调整规则


### 钩子最佳实践


- 避免长时间运行的钩子
- 设置合理的超时时间
- 测试钩子行为


> 过度使用钩子可能会影响 Codex 的性能，只添加真正需要的钩子。


---


## 常见问题


### Q: 规则不生效？


确保规则文件在正确的位置，并启用了 `codex_hooks` 特性。


### Q: 钩子执行失败会阻止操作吗？


这取决于钩子配置，某些钩子失败会阻止后续操作。


### Q: 可以动态启用/禁用规则吗？


是的，可以通过配置文件或环境变量控制。








	  AI 思考中...





			** [Codex MCP 服务器配置](https://www.runoob.com/codex-mcp.html)
			[Codex 非交互模式](https://www.runoob.com/codex-noninteractive.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#caabaea7a3a48ab8bfa4a5a5a8e4a9a5a7)

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