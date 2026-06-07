# Codex 基础入门

- Source: https://www.runoob.com/codex/codex-usage.html

### 启动 Codex CLI


安装并配置好账号后，在项目目录下打开终端，输入 `codex` 即可启动交互式界面：


```
# 进入你的项目目录
cd ~/my-project

# 启动 Codex 交互界面
codex

# 带初始提示词直接启动
codex "帮我分析这个项目的结构"

# 启动时指定模型
codex --model gpt-5
```


**

💡 建议在项目根目录下启动 Codex，这样它能完整读取项目文件结构。Codex 界面很简洁，光标所在处就是输入框，直接输入你的需求即可。


### 三种审批模式（Approval Mode）


Codex CLI 提供三种不同级别的操作权限模式，你可以根据任务需求选择合适的模式：


| 模式 | 说明 | 适用场景 |
| --- | --- | --- |
| ask（默认） | 只读模式：可以读取文件、制定方案，但执行任何操作前都需要你确认 | 陌生代码库探索、风险评估 |
| auto-edit | 自动编辑：可以读取和修改当前目录文件，但网络操作仍需确认 | 日常代码开发、重构任务 |
| full-auto | 完全自动：在禁用网络的沙箱中全自动运行，无需确认 | 批量任务、CI/CD 自动化 |


```
# 指定审批模式启动
codex --approval-mode ask        # 默认只读模式
codex --approval-mode auto-edit  # 自动编辑模式（缩写 -a auto-edit）
codex --approval-mode full-auto  # 完全自动模式

# 在交互界面中切换
/approvals  # 输入此命令切换审批模式
```


### 你的第一次对话


#### 示例 1：分析项目结构


```
codex "分析这个项目的目录结构，告诉我主要文件的作用"

# Codex 会自动读取文件，输出类似：
# ✓ 读取 package.json
# ✓ 扫描 src/ 目录（23 个文件）
# &#x1f4c2; 项目结构分析：
# - src/index.ts：应用入口，初始化 Express 服务器
# - src/routes/：API 路由定义（共 5 个端点）
# ...
```


#### 示例 2：修复 Bug


```
codex "我的 login 函数有 bug，用户登录后 token 没有正确保存，帮我找出问题并修复"

# Codex 会：
# 1. 读取相关文件
# 2. 分析代码逻辑
# 3. 提出修改方案
# 4. 等待你确认后执行修改
```


#### 示例 3：生成新功能


```
codex "给我的 Express 应用添加一个用户注册接口，需要验证邮箱格式，密码至少8位，并把用户信息存入数据库"

# 传入图片上下文
codex -i design.png "按照这个设计图，实现对应的 React 组件"
```


### 图片输入


Codex CLI 支持将图片作为上下文输入，这在以下场景特别有用：


- 分析报错截图
- 根据 UI 设计图生成前端代码
- 解读架构图并据此实现功能


```
# 方法一：命令行传入图片路径
codex -i screenshot.png "解释这个报错信息，并告诉我如何修复"

# 方法二：传入多张图片
codex --image img1.png,img2.jpg "对比这两个界面的区别，实现图一的设计"

# 方法三：在交互界面中粘贴图片（macOS）
# 复制图片后，在 Codex 输入框中直接按 Cmd+V 粘贴

# 方法四：Shift + 拖拽图片到终端窗口
```









	  AI 思考中...





			** [Codex 安装与使用](https://www.runoob.com/codex-install.html)
			[Codex 配置文件](https://www.runoob.com/codex-config-file.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#4d2c292024230d3f382322222f632e2220)

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