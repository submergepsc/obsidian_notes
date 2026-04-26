这份笔记完全按照 Markdown 格式排版，你可以直接一键复制，粘贴到你的 Obsidian 或 Typora 知识库中。

---

# ⚡ aria2c 极简速通与实战笔记

**官方网站 / 发行版下载**：[https://aria2.github.io/](https://aria2.github.io/)

**GitHub 仓库**：[https://github.com/aria2/aria2](https://github.com/aria2/aria2)

## 0. 核心定位

`aria2` 是一款极其轻量、极度消耗底层网络 I/O 而非系统资源的**命令行下载神器**。它原生支持 HTTP/HTTPS、FTP、SFTP、BitTorrent (BT) 和 Metalink 协议。无 UI 界面的特性使其非常适合部署在服务器、WSL 环境或作为后台 RPC 服务运行。

## 1. 极速安装

根据不同的开发环境，可以直接通过包管理器秒装：

- **Windows (使用 Scoop 包管理器)**：
    
    PowerShell
    
    ```
    scoop install aria2
    ```
    
- **Linux / WSL (基于 Debian/Ubuntu)**：
    
    Bash
    
    ```
    sudo apt update
    sudo apt install aria2
    ```
    

## 2. 基础实战命令

日常在终端中调用 `aria2c`，掌握以下几条命令即可覆盖 90% 的场景：

**① 基础单文件下载**

Bash

```
aria2c "https://example.com/file.zip"
```

**② 榨干带宽：多线程并发下载 (最常用)**

Bash

```
# -x 指定最大连接数(最高16)，-s 指定文件分块数
aria2c -x 16 -s 16 "https://example.com/large-system-image.iso"
```

**③ 指定下载路径与重命名**

Bash

```
# -d 指定目录，-o 指定文件名
aria2c -d /home/user/Downloads -o my_custom_name.zip "https://example.com/file.zip"
```

**④ 下载 BT 种子或磁力链接**

Bash

```
# 直接跟上磁力链接即可，Aria2 会自动解析元数据
aria2c "magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C"
```

**⑤ 批量下载 (从文本读取)**

将所有链接保存在 `urls.txt` 中，每行一个链接：

Bash

```
# 批量读取并自动并行下载
aria2c -i urls.txt
```

## 3. 核心参数字典速查 (Cheat Sheet)

|**简写**|**完整参数名**|**极客说明**|
|---|---|---|
|`-x`|`--max-connection-per-server`|到同一服务器的最大连接数，默认 `1`，极限值 `16`。|
|`-s`|`--split`|下载文件时的分块数量。配合 `-x` 使用，榨干单文件的直链带宽。|
|`-c`|`--continue`|**断点续传**。网络中断或手残 `Ctrl+C` 关掉后，加上它重新运行即可接着下。|
|`-d`|`--dir`|下载目标路径。配合数据盘路径使用，避免撑爆系统盘。|
|`-o`|`--out`|强制重命名下载的文件。|
|`-i`|`--input-file`|从指定的本地文本文件中读取 URL 列表。|
|无|`--file-allocation`|磁盘预分配策略。强烈建议配为 `falloc`（现代文件系统），瞬间占位，消除后期合并时的固态硬盘 I/O 卡顿。|

## 4. 进阶玩法预警：RPC 模式

`aria2c` 不仅仅是一个敲一下动一下的命令。它的终极形态是**常驻后台的下载微服务**。

通过命令 `aria2c --enable-rpc`（配合编写 `aria2.conf` 配置文件），它可以静默运行在系统后台。你可以通过网页前端面板（如 Ariang）或者其他自动化脚本（甚至配合各种浏览器插件），通过 WebSocket / HTTP API 向它随时推送下载任务。