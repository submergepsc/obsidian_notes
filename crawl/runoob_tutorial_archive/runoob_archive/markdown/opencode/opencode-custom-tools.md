# OpenCode 自定义工具

- Source: https://www.runoob.com/opencode/opencode-custom-tools.html

自定义工具（Custom Tools）允许你为 OpenCode 扩展能力，让 LLM 在对话过程中调用你定义的函数，从而实现数据库查询、脚本执行、API 调用等复杂操作。


这些工具会与内置工具（如 `read`、`write`、`bash`）协同工作，构建完整的自动化开发能力体系。


---


自定义工具是 OpenCode 的核心扩展能力，它让 LLM 从只会生成代码，升级为可以执行任务。


通过合理设计工具，你可以构建：


- 自动化开发流水线
- 智能代码助手
- AI 运维系统
- 企业内部 AI 工具平台


---


## 一、什么是自定义工具


自定义工具本质上是一个函数接口，LLM 可以在运行过程中主动调用它，并获取执行结果。


典型应用场景：


- 查询数据库（SQL / NoSQL）
- 调用内部 API
- 执行脚本（Python / Shell）
- 读取系统状态或环境信息
- 封装复杂业务逻辑


你可以理解为：**让 AI 拥有执行能力的插件机制**。


---


## 二、工具存放位置


OpenCode 会自动加载以下目录中的工具：


- **项目级：**`.opencode/tools/`
- **全局级：**`~/.config/opencode/tools/`


文件名即工具名称（非常关键）。


---


## 三、基础工具定义（推荐方式）


使用 `tool()` 辅助函数可以获得类型安全和参数校验能力。


```
import { tool } from "@opencode-ai/plugin"

export default tool({
  description: "Query the project database",
  args: {
    query: tool.schema.string().describe("SQL query to execute"),
  },
  async execute(args) {
    return `Executed query: ${args.query}`
  },
})
```


**说明：**


- `description`：工具描述，LLM 用于判断是否调用
- `args`：参数定义（基于 Zod）
- `execute`：实际执行逻辑


---


## 四、单文件多工具


一个文件可以导出多个工具，每个工具会自动命名为：


`_`


```
import { tool } from "@opencode-ai/plugin"

export const add = tool({
  description: "Add two numbers",
  args: {
    a: tool.schema.number(),
    b: tool.schema.number(),
  },
  async execute(args) {
    return args.a + args.b
  },
})

export const multiply = tool({
  description: "Multiply two numbers",
  args: {
    a: tool.schema.number(),
    b: tool.schema.number(),
  },
  async execute(args) {
    return args.a * args.b
  },
})
```


最终生成工具：


- `math_add`
- `math_multiply`


---


## 五、与内置工具冲突


如果你的工具名称与内置工具相同，会**覆盖内置工具**。


```
// 覆盖内置 bash 工具
export default tool({
  description: "Restricted bash wrapper",
  args: {
    command: tool.schema.string(),
  },
  async execute(args) {
    return `blocked: ${args.command}`
  },
})
```


**建议：**


- 避免命名冲突
- 如果只是限制能力，优先使用 `permission` 配置


---


## 六、参数定义（Zod）


参数使用 Zod Schema 定义，支持类型校验与描述：


```
args: {
  query: tool.schema.string().describe("SQL query"),
  limit: tool.schema.number().optional(),
}
```


也可以直接使用 Zod：


```
import { z } from "zod"

export default {
  description: "Example tool",
  args: {
    name: z.string(),
  },
  async execute(args) {
    return `Hello ${args.name}`
  },
}
```


---


## 七、上下文（Context）


工具执行时会自动注入上下文信息：


```
export default tool({
  description: "Get project info",
  args: {},
  async execute(args, context) {
    const { agent, sessionID, directory, worktree } = context
    return `Agent: ${agent}, Dir: ${directory}`
  },
})<
```


可用字段：


- `agent`：当前代理
- `sessionID`：会话 ID
- `messageID`：消息 ID
- `directory`：当前工作目录
- `worktree`：Git 根目录


---


## 八、调用外部语言（Python 示例）


你可以用任何语言实现工具逻辑，例如 Python。


### 1、Python 脚本


```
# .opencode/tools/add.py
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + b)
```


### 2、工具封装


```
import { tool } from "@opencode-ai/plugin"
import path from "path"

export default tool({
  description: "Add two numbers using Python",
  args: {
    a: tool.schema.number(),
    b: tool.schema.number(),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, ".opencode/tools/add.py")
    const result = await Bun.$`python3 ${script} ${args.a} ${args.b}`.text()
    return result.trim()
  },
})
```


这种方式适合：


- 已有 Python 工具链
- 调用数据分析 / AI 模型
- 执行复杂计算任务


---


## 九、最佳实践


- 工具描述要清晰，帮助 LLM 正确选择
- 参数设计尽量简单明确
- 避免副作用（除非明确需要）
- 优先通过 permission 控制风险操作
- 工具应聚焦单一职责










	  AI 思考中...





			** [OpenCode Skills](https://www.runoob.com/opencode-skills.html)














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