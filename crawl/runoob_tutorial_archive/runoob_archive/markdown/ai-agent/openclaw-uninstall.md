# OpenClaw 卸载指南

- Source: https://www.runoob.com/ai-agent/openclaw-uninstall.html

本文介绍如何 彻底卸载 OpenClaw，包括 CLI、Gateway 服务、配置文件以及工作区数据。


OpenClaw 卸载有两种情况：


- CLI 仍然存在（推荐方式）
- CLI 已删除但后台服务仍在运行（手动清理）


---


## 一、推荐方式（CLI 仍然存在）


如果系统中仍然可以运行 openclaw 命令，建议使用内置卸载命令。


### 1. 标准卸载


```
openclaw uninstall
```


该命令会删除：


- Gateway 服务
- 本地状态数据
- 配置文件
- Agent 工作目录等数据


### 2. 非交互式卸载（自动化脚本）

适用于 CI 或自动化脚本环境：


```
# 直接执行
openclaw uninstall --all --yes --non-interactive

# 无本地 CLI 时，通过 npx 执行
npx -y openclaw uninstall --all --yes --non-interactive
```



- **uninstall**：卸载程序
- **--all**：把服务和本地数据一起清掉（包括网关服务、配置文件、数据库等）
- **--yes**：自动确认，不再让你中途一遍遍手动输入 Y


---


## 二、手动卸载（完整清理）


如果你希望 完全控制卸载过程，可以按以下步骤手动清理。


### 1. 停止 Gateway 服务


```
openclaw gateway stop
```


### 2. 卸载 Gateway 服务


```
openclaw gateway uninstall
```


该步骤会删除系统中的后台服务：


- macOS：launchd
- Linux：systemd
- Windows：Scheduled Tasks


### 3. 删除配置与状态目录


```
rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
```


默认目录：


```
~/.openclaw
```


其中包含：


- 配置文件
- Token
- Session
- 日志
- Agent 状态数据


如果设置过自定义环境变量：


```
OPENCLAW_CONFIG_PATH
```


也需要手动删除对应文件。


### 4. 删除 Agent 工作区（可选）


```
rm -rf ~/.openclaw/workspace
```


该目录通常存放：


- Agent 生成代码
- 任务执行文件
- 中间数据


### 5 删除 CLI

根据安装方式选择对应命令：


```
# npm 安装
npm rm -g openclaw

# pnpm 安装
pnpm remove -g openclaw

# bun 安装
bun remove -g openclaw
```


### 6. 删除 macOS 应用（如果安装）


```
rm -rf /Applications/OpenClaw.app
```


---

## 三、CLI 丢失但服务仍在运行


如果已经删除 CLI，但 OpenClaw Gateway 仍在后台运行，可以手动删除系统服务。


### 1. macOS（launchd 服务）


默认服务标签：`bot.molt.gateway`（多配置为 `bot.molt.`，旧版为 `com.openclaw.*`）


```
# 停止并卸载服务
launchctl bootout gui/$UID/bot.molt.gateway

# 删除服务配置文件
rm -f ~/Library/LaunchAgents/bot.molt.gateway.plist

# 多配置场景：替换为对应 profile 标签
# launchctl bootout gui/$UID/bot.molt.<profile>
# rm -f ~/Library/LaunchAgents/bot.molt.<profile>.plist

# 清理旧版残留（如有）
rm -f ~/Library/LaunchAgents/com.openclaw.*.plist
```


### 2. Linux（systemd 用户服务）


默认服务名：`openclaw-gateway.service`（多配置为 `openclaw-gateway-.service`）


```
# 停止并禁用服务
systemctl --user disable --now openclaw-gateway.service

# 删除服务配置文件
rm -f ~/.config/systemd/user/openclaw-gateway.service

# 刷新 systemd 配置
systemctl --user daemon-reload

# 多配置场景：替换为对应 profile 服务名
# systemctl --user disable --now openclaw-gateway-<profile>.service
# rm -f ~/.config/systemd/user/openclaw-gateway-<profile>.service
# systemctl --user daemon-reload
```


### 3. Windows（计划任务）


默认任务名：`OpenClaw Gateway`（多配置为 `OpenClaw Gateway ()`）


```
# 删除计划任务
schtasks /Delete /F /TN "OpenClaw Gateway"

# 删除任务脚本
Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"

# 多配置场景：替换为对应 profile 任务名
# schtasks /Delete /F /TN "OpenClaw Gateway (<profile>)"
# Remove-Item -Force "$env:USERPROFILE\.openclaw-<profile>\gateway.cmd"
```


---

## 四、Docker 安装的卸载方式


如果 OpenClaw 运行在 Docker 中：


```
docker stop openclaw
docker rm openclaw
docker volume rm openclaw-data
```


或


```
docker-compose down -v
```


---


## 五、源码安装（git clone）卸载


若通过 `git clone` 源码方式安装，需先清理服务，再删除源码与配置：


- 先执行「推荐卸载方式」或「手动清理服务残留」，停止并卸载网关服务
- 删除源码仓库目录
```
# 替换为你的源码路径
rm -rf /path/to/openclaw-repo
```

- 按前文步骤删除状态、配置与工作区目录


---


## 六、卸载前建议备份


如果需要保留数据，可以先创建备份：


```
openclaw backup create
```


然后再执行卸载。


### 卸载验证


卸载完成后，可通过以下方式验证是否彻底清理：


- 执行 `openclaw --version`，提示「命令未找到」则 CLI 卸载成功
- 检查系统服务： macOS：`launchctl list | grep molt` 无输出
- Linux：`systemctl --user list-units | grep openclaw` 无输出
- Windows：任务计划程序中无「OpenClaw Gateway」相关任务


    检查目录：`~/.openclaw`（及多配置 `~/.openclaw-<profile>`）已删除


---

## 七、常见残留目录


彻底卸载时建议检查以下目录：


```
~/.openclaw
~/.openclaw/workspace
~/Library/LaunchAgents/ai.openclaw.gateway.plist
~/.config/systemd/user/openclaw-gateway.service
```









	  AI 思考中...





			** [OpenClaw Skills — ClawHub](https://www.runoob.com/openclaw-skills.html)
			[OpenClaw 快速上手](https://www.runoob.com/openclaw-quickstart.html) **













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