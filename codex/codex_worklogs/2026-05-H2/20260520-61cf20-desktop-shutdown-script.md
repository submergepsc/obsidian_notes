---
id: 20260520-61cf20-desktop-shutdown-script
name: 桌面立即关机脚本
slug: desktop-shutdown-script
cwd: /home/loviya
summary: 在桌面创建一个双击即可使用的立即关机脚本，带二次确认并调用 systemctl poweroff。
---

Current Snapshot:
- workflow id: 20260520-61cf20-desktop-shutdown-script
- current status: 已完成
- current goal: 在桌面新增一个立即关机脚本。
- current blocker: 无
- next step: 无
- tags: [桌面, 关机, 脚本, poweroff]
- summary: 已在桌面创建 ，脚本会先用 zenity 询问确认，再执行 。

Key Results:
- 新建脚本：
- 脚本已设置可执行权限。

Decisions:
- 优先使用 ，因为它在当前系统可用。
- 加入 zenity 二次确认，避免误触立即关机。

Artifacts:
- 

Commands:
- 

Open Questions:
- 若用户希望去掉确认窗口，可改为直接执行 poweroff。
