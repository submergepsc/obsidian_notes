---
id: 20260515-delete-kugou-music
name: Delete Kugou Music
slug: delete-kugou-music
cwd: /home/loviya
summary: 删除本机酷狗音乐 Wine/Spark 包、运行进程和残留安装包。
tags:
  - kugou
  - music
  - uninstall
priority: normal
---

# Delete Kugou Music

## Current Snapshot

- status: 已完成
- goal: 恢复刚才被删除的酷狗 Spark 安装；记录微信目录压缩包误删无法从本机副本恢复。
- blocker: 微信文件目录中三个“酷狗概念版”压缩包是用 `rm -f` 删除，未进入回收站，当前未找到其它本机副本。
- next: 无；如需微信压缩包，只能从原微信聊天/发送方/备份重新取得，或另做底层文件恢复尝试。
- updated: 2026-05-15 15:44:00 +0800

## Key Results

- 已从 `/home/loviya/.cache/.fr-SK1TO3` 解包缓存重建 `/tmp/com.kugou.spark_20.0.52.27315spark8_all.deb`。
- 已重新安装 `com.kugou.spark` 20.0.52.27315spark8。
- 已把重建的 `.deb` 副本放回 `/home/loviya/下载/` 和 `/home/loviya/apps/music/`。
- 已验证 `/usr/share/applications/com.kugou.spark.desktop` 恢复。
- 未找到微信目录中三个“酷狗概念版”压缩包的本机副本。

## Decisions

- 将用户指令“删掉酷狗音乐”按卸载酷狗音乐本体和清理安装包处理。

## Delete Kugou Music

- updated: 2026-05-15 15:19:00 +0800
- cwd: `/home/loviya`
- source instruction: `删掉酷狗音乐`
- problem:
  - 本机已安装 `com.kugou.spark` 20.0.52.27315spark8，且存在运行中的 KuGou Wine 进程。
  - 用户目录中还有酷狗 `.deb` 安装包副本。
- improvement:
  - 停止运行进程，卸载系统包，并清理用户目录中的安装包。
- result:
  - 待执行。
- next:
  - 请求 sudo 权限卸载 `com.kugou.spark`。

## Restore Kugou Spark

- updated: 2026-05-15 15:44:00 +0800
- cwd: `/home/loviya`
- source instruction: `等一下,把上面的酷狗恢复`
- problem:
  - 用户要求恢复刚才删除的酷狗内容。
  - `com.kugou.spark` 的原 `.deb` 已被删除，但系统缓存里还保留了解包目录。
  - 微信文件目录中三个“酷狗概念版”压缩包是用 `rm -f` 删除，未进入回收站。
- improvement:
  - 用 `dpkg-deb --build /home/loviya/.cache/.fr-SK1TO3 /tmp/com.kugou.spark_20.0.52.27315spark8_all.deb` 重建安装包。
  - 用 `sudo apt-get install -y /tmp/com.kugou.spark_20.0.52.27315spark8_all.deb` 重新安装 Spark 酷狗。
  - 将 `.deb` 复制回 `/home/loviya/下载/com.kugou.spark_20.0.52.27315spark8_all.deb` 和 `/home/loviya/apps/music/com.kugou.spark_20.0.52.27315spark8_all.deb`。
- result:
  - `dpkg -l` 显示 `com.kugou.spark` 20.0.52.27315spark8 已安装。
  - `/usr/share/applications/com.kugou.spark.desktop` 已恢复。
  - 两个 `.deb` 副本均已恢复为 273M。
  - 全用户目录搜索未找到“酷狗概念版”压缩包副本。
- next:
  - 无；如需微信压缩包，只能从原微信聊天/发送方/备份重新取得，或另做底层文件恢复尝试。
