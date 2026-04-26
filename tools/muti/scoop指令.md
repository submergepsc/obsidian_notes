这也是非常适合作为**速查手册 (Cheatsheet)** 保存的内容。鉴于你的开发者背景，我将这些命令按照**生命周期**和**功能模块**进行了分类，并补充了针对国内网络环境的特殊配置。
# 目录结构
```
H:\Applications\Scoop
├── apps/       <-- 核心：所有软件的具体安装位置
├── buckets/    <-- 仓库：软件的安装脚本（“菜单”）
├── cache/      <-- 缓存：下载下来的安装包（zip, exe 等）
├── persist/    <-- 数据：软件的配置文件（防止更新时丢失）
└── shims/      <-- 垫片：命令行的入口（最为关键的设计）
```
### 第一部分：Scoop 安装命令（重置版）
如果需要在一台新电脑或者重置后的环境安装 Scoop，请按顺序执行以下步骤。
#### 1. 前置策略（允许脚本运行）
PowerShell 默认禁止运行脚本，必须先开启： 
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
#### 2. 正式安装（二选一）
**方案 A：标准安装（如果你挂了代理/梯子）**
PowerShell
```
# 这里的 get.scoop.sh 需要能访问 GitHub
iwr -useb get.scoop.sh | iex
```
方案 B：指定代理安装（推荐）
如果你有代理（例如端口 7890），可以直接在安装时指定，防止下载失败：
PowerShell
```
iwr -useb get.scoop.sh | iex -Proxy 'http://127.0.0.1:7890'
```
方案 C：自定义安装目录（高级）
如果你不想装在默认的 C:\Users\用户名\scoop，可以用这一句：
PowerShell
```
# 示例：装到 D:\Applications\Scoop
$env:SCOOP='D:\Applications\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')
iwr -useb get.scoop.sh | iex
```
------
### 第二部分：Scoop 常用命令速查
#### 1. 软件管理（核心）
| **命令**        | **说明**                 | **示例**                                   |
| --------------- | ------------------------ | ------------------------------------------ |
| **`search`**    | 搜索软件（支持模糊搜索） | `scoop search python`                      |
| **`install`**   | 安装软件                 | `scoop install git` `scoop install curl`   |
| **`uninstall`** | 卸载软件                 | `scoop uninstall git`                      |
| **`update`**    | 更新 Scoop 本身或某软件  | `scoop update` (自身) / `scoop update git` |
| **`update `** | **一键更新所有软件**     | `scoop update *`                           |
| **`status`**    | 检查哪些软件有新版本     | `scoop status`                             |
| **`hold`**      | **锁定版本**（禁止更新） | `scoop hold python` (防止自动升级挂掉项目) |
| **`unhold`**    | 解除版本锁定             | `scoop unhold python`                      |
| **`info`**      | 查看软件详细信息         | `scoop info python`                        |
#### 2. 仓库管理 (Buckets)
Scoop 默认只有 main 仓库（无 GUI 工具）。你需要添加其他仓库来扩展软件库。
| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| bucket known | 列出官方认可的知名仓库 | scoop bucket known |
| bucket add | 添加仓库 | scoop bucket add extras (必装) / versions |
| bucket list | 查看已添加的仓库 | scoop bucket list |
| bucket rm | 移除仓库 | scoop bucket rm extras |
**👨‍💻 开发者推荐组合：**
PowerShell
```
scoop bucket add extras    # 包含大量 GUI 软件 (如 Chrome, VSCode)
scoop bucket add versions  # 包含旧版本软件 (如 python3.7, python2.7)
scoop bucket add java      # 专门管理各种 JDK (OpenJDK, OracleJDK)
scoop bucket add nerd-fonts # 各种编程专用字体
```
#### 3. 清理与维护 (Cleanup)
Scoop 下载旧版本不会自动删除（方便回滚），定期清理可以释放空间。
| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| cleanup | 删除旧版本，保留最新版 | scoop cleanup python |
| cleanup * | 一键清理所有旧版本 | scoop cleanup * |
| cache show | 查看下载缓存占用 | scoop cache show |
| cache rm * | 清空下载缓存（安装失败时常用） | scoop cache rm * |
#### 4. 环境配置 (Config)
针对网络和下载器的优化，这是你刚才遇到问题的关键部分。
| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| config proxy | 设置代理（解决 GitHub 连接） | scoop config proxy 127.0.0.1:7890 |
| config rm proxy | 移除代理 | scoop config rm proxy |
| config aria2-enabled | 开启多线程下载（推荐） | scoop config aria2-enabled true |
| checkup | 体检（诊断环境问题） | scoop checkup |
------
### 第三部分：开发者专属技巧 (Pro Tips)
作为软件工程学生，以下两个功能是你必须掌握的“杀手锏”：
#### 1. 版本瞬间切换 (`reset`)
当你同时安装了 `python@3.12` 和 `python@3.8`，想把系统默认 Python 切换到 3.8：
PowerShell
```
scoop reset python@3.8
```
*这会自动调整环境变量（Shims），让 `python` 命令指向 3.8 版本。无需重启，立即生效。*
#### 2. 导出/导入软件列表
重装系统时，不需要一个个重新敲命令安装，可以导出清单：
PowerShell
```
# 导出当前安装的所有软件名到文本文件
scoop export > my_apps.txt
# 在新电脑上批量安装
scoop import my_apps.txt
```
#### 3. 安装超级权限软件 (`sudo`)
有些软件必须写入系统目录或注册表（Scoop 默认不提倡，但有时没办法），需要安装 `sudo`：
PowerShell
```
scoop install sudo
sudo scoop install <软件名> -g  # -g 代表全局安装
```
------
建议下一步：
你可以把这篇回复复制到你的笔记软件（Obsidian/Notion）里，或者在终端里输入 scoop help 也能看到简易版的官方说明。你现在的环境（Scoop + Extras + Aria2 + Proxy）已经是一个非常完美的 Windows 开发环境了。
