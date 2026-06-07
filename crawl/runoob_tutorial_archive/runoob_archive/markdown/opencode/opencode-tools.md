# OpenCode 工具

- Source: https://www.runoob.com/opencode/opencode-tools.html

OpenCode 的核心能力不仅来自大模型本身，更来自它可以调用的**工具（Tools）**。


工具的本质：让 LLM 从会说话变成会做事。


**Tools = OpenCode 的执行能力，而权限 = 安全边界。**


---


## 一、什么是工具（Tools）


工具是 LLM 在项目中执行操作的能力接口，例如：


- 读取代码
- 修改文件
- 执行命令
- 搜索代码
- 访问网络


没有工具：只能生成代码


有工具：可以**直接操作项目**


---


## 二、工具权限控制（最重要）


默认情况下：


- 所有工具都是启用的
- 且无需确认即可执行


**生产环境必须配置权限！**


### 1、基础权限配置


```
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny",
    "bash": "ask",
    "webfetch": "allow"
  }
}
```


| 权限值 | 说明 |
| --- | --- |
| allow | 允许直接执行 |
| deny | 完全禁止 |
| ask | 执行前需要人工确认 |


### 2、通配符控制


可以批量控制工具：


```
{
  "permission": {
    "mymcp_*": "ask"
  }
}
```


所有来自 MCP 的工具都需要审批


---


## 三、内置工具详解


OpenCode 内置了一整套工程级工具：


### 1、bash（命令执行）


```
{
  "permission": {
    "bash": "allow"
  }
}
```


作用：


- 执行 shell 命令
- 如 npm install、git status


**风险：**高（建议设为 ask）


### 2、edit（核心工具）


```
{
  "permission": {
    "edit": "allow"
  }
}
```


作用：


- 修改现有文件
- 基于精确文本替换


**说明：**这是 AI 修改代码的核心能力


### 3、write（文件创建）


作用：


- 创建新文件
- 覆盖已有文件


**注意：**


write 受 edit 权限控制


### 4、read（读取文件）


```
{
  "permission": {
    "read": "allow"
  }
}
```


作用：


- 读取代码文件
- 支持按行读取


**风险：**低（建议 always allow）


### 5、grep（内容搜索）


```
{
  "permission": {
    "grep": "allow"
  }
}
```


作用：


- 正则搜索代码


### 6、glob（文件匹配）


作用：


- 查找文件路径（如 src/**/*.ts）


### 7、list（目录浏览）


作用：


- 列出目录结构


### 8、patch（补丁应用）


作用：


- 应用 diff 补丁


**说明：**受 edit 权限控制


### 9、lsp（实验性）


作用：


- 代码智能分析（跳转定义、查引用）


启用方式：


```
OPENCODE_EXPERIMENTAL_LSP_TOOL=true
```


### 10、skill（技能加载）


作用：


- 加载 SKILL.md
- 增强 AI 行为


### 11、todowrite（任务管理）


作用：


- 维护任务列表
- 跟踪复杂流程


### 12、webfetch（网页读取）


作用：


- 获取指定 URL 内容


### 13、websearch（联网搜索）


启用方式：


```
OPENCODE_ENABLE_EXA=1 opencode
```


作用：


- 搜索互联网信息


**区别：**


- websearch：查找信息（发现）
- webfetch：读取内容（获取）


### 14、question（交互提问）


作用：


- 向用户提问
- 收集需求


适用于：


- 需求不明确
- 需要用户决策


---


## 四、自定义工具


你可以定义自己的工具，让 AI 执行自定义逻辑。


例如：


- 调用内部 API
- 操作数据库
- 执行业务逻辑


**本质：**让 LLM 调用函数


---


## 五、MCP 服务器（高级能力）


MCP（Model Context Protocol）允许你接入外部系统：


- 数据库
- 第三方 API
- 内部服务


相当于给 AI 接上"外部能力"


---


## 六、底层机制（重要）


OpenCode 使用 ripgrep 作为搜索引擎：


- 遵循 .gitignore
- 默认忽略 node_modules 等目录


### 如何覆盖忽略规则


创建文件：


```
.ignore
```


示例：


```
!node_modules/
!dist/
!build/
```


强制包含这些目录


---


## 七、最佳实践（强烈建议）


- read / grep / glob → allow
- edit → ask（开发阶段）
- bash → ask（生产环境）
- webfetch → allow


**核心原则：**


- 读取可以放开
- 修改必须控制
- 执行命令要谨慎









	  AI 思考中...





			** [OpenCode GitLab](https://www.runoob.com/opencode-gitlab.html)
			[OpenCode 规则（AGENTS.md）](https://www.runoob.com/opencode-agents-md.html) **













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