# Codex 云端版本

- Source: https://www.runoob.com/codex/codex-web.html

Codex Web 是云端版本，让你从任何设备访问 Codex，在隔离环境中运行任务。


---


## 访问 Codex Web


访问云端 Codex：


```
https://chatgpt.com/codex
```


### 使用前提


- ChatGPT Plus / Pro / Business / Enterprise 计划
- 或使用 OpenAI API Key


**
使用 API Key 时，部分云端功能可能不可用。


---


## 云端环境（Environments）


Environment 是 Codex Web 的核心概念，每个环境是一个隔离的工作空间。


### 创建环境


- 连接 GitHub 账号
- 选择一个仓库
- 配置设置脚本和环境变量
- 选择网络访问策略


### 任务执行流程


云端任务按以下流程执行：


- 创建容器，克隆仓库到选定分支
- 运行设置脚本安装依赖
- 应用网络访问设置
- Agent 执行任务（编辑代码、运行命令、验证结果）
- 显示结果和文件变更


---


## 默认镜像


云端使用名为 `universal` 的默认容器镜像：


- 预装常见语言：Python、Node.js、Go、Rust
- 包含常用工具：npm、pip、cargo、git
- 可固定运行时版本


### 版本固定


## 固定版本


```
# Environment 设置

# 固定 Python 版本
python_version = "3.11"

# 固定 Node.js 版本
node_version = "20"
```


---


## 设置脚本


设置脚本在容器创建时自动运行：


### 自动检测


Codex 自动识别项目类型并执行相应安装：


- Node.js：自动运行 npm install / yarn / pnpm
- Python：自动运行 pip install / poetry install


### 手动脚本


## 自定义设置脚本


```
# Setup Script
# 在环境设置中配置

npm install
npm run build
pip install -r requirements.txt
```


### 维护脚本


维护脚本在缓存容器启动时运行：


- 用于更新依赖或重新构建
- 比完整设置更快


> 设置脚本与 Agent 在不同的 Bash 会话中运行，export 命令不会持久化。


---


## 环境变量与 Secrets


### 环境变量


环境变量在整个任务期间可用：


## 设置环境变量


```
# Environment Variables
NODE_ENV=production
DEBUG=false
API_ENDPOINT=https://api.example.com
```


### Secrets


Secrets 用于存储敏感信息：


- 额外加密存储
- 仅在任务执行时解密
- 只在设置脚本中可用
- Agent 阶段自动移除


| 类型 | 可见范围 | 用途 |
| --- | --- | --- |
| Environment Variables | 设置脚本 + Agent | 常规配置 |
| Secrets | 仅设置脚本 | API Key、密码 |


---


## 网络访问控制


云端环境的网络访问默认受限：


### 默认设置


| 阶段 | 网络访问 |
| --- | --- |
| 设置脚本 | 允许（安装依赖需要） |
| Agent | 禁止（默认） |


### Agent 网络访问选项


| 设置 | 说明 |
| --- | --- |
| Off | 完全禁止网络访问 |
| On | 允许网络访问（可限制域名） |


### 域名白名单


## 域名配置


```
# 网络配置

# 白名单预设
domain_allowlist = "common-dependencies"
# 包含：github.com, npmjs.com, pypi.org 等

# 自定义域名
domain_allowlist = [
    "github.com",
    "api.mycompany.com"
]

# 限制 HTTP 方法
allowed_methods = ["GET", "HEAD", "OPTIONS"]
```


### 安全风险


启用 Agent 网络访问会增加风险：


- 提示注入（从恶意网页获取指令）
- 数据泄露（向外部发送代码或密钥）
- 下载恶意依赖


> 仅在必要时启用 Agent 网络访问，并使用域名白名单限制。


---


## 容器缓存


云端缓存容器状态以加速后续任务：


- 缓存最多 12 小时
- 设置脚本或环境变量变化时自动失效
- 新任务启动更快


---


## 云端任务管理


### 创建任务


- 选择环境
- 输入任务描述
- 选择模型和配置
- 启动任务


### 任务监控


- 实时查看进度
- 查看文件变更
- 检查命令输出


### 结果处理


- 查看变更 Diff
- 创建 Pull Request
- 下载变更文件


---


## 并行任务


云端支持并行运行多个任务：


- 同时处理不同功能
- 多个环境独立工作
- 提高整体效率


> 避免多个任务同时修改同一文件，否则会产生冲突。


---


## 常见问题


### Q: Cloud 和本地有什么区别？


Cloud 在远程服务器运行，适合并行任务和远程访问；本地直接操作你的文件。


### Q: 如何收费？


云端任务消耗额度，费用根据模型和使用量计算。


### Q: 可以访问本地文件吗？


云端无法访问本地文件，但可以通过 Git 同步。


### Q: 网络访问何时需要？


仅当 Agent 需要实时数据或外部 API 时才需要，设置脚本通常足够。








	  AI 思考中...





			** [Codex 命令行工具](https://www.runoob.com/codex-cli.html)
			[Codex 集成与连接](https://www.runoob.com/codex-integrations.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#4120252c282f0133342f2e2e236f222e2c)

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