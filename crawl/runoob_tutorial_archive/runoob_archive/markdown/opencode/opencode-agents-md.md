# OpenCode 规则（AGENTS.md）

- Source: https://www.runoob.com/opencode/opencode-agents-md.html

在 OpenCode 中，**规则（Rules）是控制 AI 行为的核心机制**。


我们可以通过 `AGENTS.md` 文件，为 OpenCode 提供自定义指令，让它按照你的项目规范进行开发。


工具决定 AI 能做什么，AGENTS.md 决定 AI 应该怎么做。


**AGENTS.md = 给 AI 制定团队开发规范。**


---


## 一、什么是 AGENTS.md


`AGENTS.md` 是一个规则文件，用于：


- 定义项目结构
- 约束代码风格
- 规范开发流程
- 指导 AI 如何执行任务


这些内容会被加入到 LLM 的上下文中。


**效果：**


- AI 更懂你的项目
- 生成的代码更符合规范
- 减少反复修改


---


## 二、快速初始化


在 OpenCode 中运行：


```
/init
```


该命令会：


- 扫描你的项目结构
- 分析代码组织方式
- 自动生成 AGENTS.md


**建议：**


- 将 AGENTS.md 提交到 Git
- 作为团队统一规范


---


## 三、示例结构


```
# 项目说明

这是一个基于 TypeScript 的 monorepo 项目。

## 项目结构

- packages/ 核心模块
- infra/ 基础设施
- web/ 前端应用

## 代码规范

- 使用 TypeScript 严格模式
- 公共代码放在 packages/core
- 所有函数必须添加注释

## 开发约定

- 使用 workspace 方式引用模块
- API 必须统一错误处理
```


本质：把团队规范"写给 AI 看"


---


## 四、规则的作用范围


### 1、项目级规则


路径：


```
./AGENTS.md
```


作用：


- 仅当前项目生效
- 团队共享


### 2、全局规则


路径：


```
~/.config/opencode/AGENTS.md
```


作用：


- 对所有项目生效
- 个人使用


**建议用途：**


- 个人编码习惯
- 输出风格控制


---


## 五、Claude Code 兼容性


OpenCode 兼容 Claude Code 的规则体系：


- 项目规则：CLAUDE.md
- 全局规则：~/.claude/CLAUDE.md
- 技能目录：~/.claude/skills/


如果不想使用，可以关闭：


```
export OPENCODE_DISABLE_CLAUDE_CODE=1
```


---


## 六、规则加载优先级（重要）


OpenCode 启动时按以下顺序加载：


- 当前目录向上查找 AGENTS.md
- 如果没有 → 查找 CLAUDE.md
- 全局规则 ~/.config/opencode/AGENTS.md
- Claude 全局规则 ~/.claude/CLAUDE.md


**关键点：**


- AGENTS.md 优先级最高
- 同级只会使用第一个匹配文件


---


## 七、扩展规则（instructions）


可以在 `opencode.json` 中加载额外规则文件：


```
{
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines.md",
    ".cursor/rules/*.md"
  ]
}
```


优点：


- 复用已有文档
- 避免重复维护


### 支持远程规则


```
{
  "instructions": [
    "https://raw.githubusercontent.com/xxx/rules/main/style.md"
  ]
}
```


**说明：**


- 支持 URL 加载
- 超时：5 秒


---


## 八、模块化规则（高级）


### 推荐方式（使用 instructions）


```
{
  "instructions": [
    "docs/dev.md",
    "test/rules.md",
    "packages/*/AGENTS.md"
  ]
}
```


适合：


- monorepo
- 大型项目


### 方式二：在 AGENTS.md 中手动引用


```
# 规则加载说明

当遇到 @xxx 文件时，请使用 read 工具加载。

- 不要一次性加载全部文件
- 按需加载
- 加载后必须遵守
```


示例：


```
TypeScript 规范：@docs/typescript.md
React 规范：@docs/react.md
API 规范：@docs/api.md
```


实现"按需加载规则"


---


## 九、最佳实践（重点）


### 1、规则要具体


❌ 不要写：


```
代码要规范
```


✅ 应该写：


```
所有函数必须添加 JSDoc 注释
```


### 2、规则要可执行


AI 只能执行明确规则，而不是抽象描述。


### 3、不要写太长


建议：


- 核心规则写在 AGENTS.md
- 详细规则拆到 instructions 文件


### 4、团队统一维护


- 纳入 Git 管理
- 作为开发规范的一部分









	  AI 思考中...





			** [OpenCode 工具](https://www.runoob.com/opencode-tools.html)
			[OpenCode 代理（Agent）](https://www.runoob.com/opencode-agent.html) **













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