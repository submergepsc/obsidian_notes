好，这一块我给你整理成一份**可以直接丢进 Obsidian 的完整笔记**，结构清晰、可复用👇
# 添加的一些快捷操作
# 🐧 Ubuntu 快速打开 Obsidian 仓库（完整指南）
## 🎯 目标
实现以下能力：
* ✔ 一条命令打开指定 Obsidian 仓库
* ✔ 可选：双击打开
* ✔ 可扩展多个仓库
* ✔ 类似 Windows `$PROFILE` / `.bat` 的体验
# 🧠 基础原理
在 Linux 中，本质就是：
```bash
obsidian "/你的仓库路径"
```
例如：
```bash
obsidian "/media/loviya/新的D盘/obsidian_notes"
```
# 🧩 方案一：alias（最简单 ⭐⭐⭐⭐）
## 📌 写入 `~/.bashrc`
```bash
nano ~/.bashrc
```
添加：
```bash
alias ob='obsidian "/media/loviya/新的D盘/obsidian_notes"'
```
## 🔄 生效
```bash
source ~/.bashrc
```
## 🚀 使用
```bash
ob
```
## ✔ 优点
* 简单
* 快速
* 类似 Windows `$PROFILE`
## ❗注意
* `=` 两边不能有空格 ❌
* 路径建议加引号（防止空格/中文问题）
# 🧩 方案二：脚本（更灵活 ⭐⭐⭐⭐⭐）
## 📌 创建脚本
```bash
mkdir -p ~/bin
nano ~/bin/ob_file
```
写入：
```bash
#!/bin/bash
obsidian "/media/loviya/新的D盘/obsidian_notes"
```
 **再给一个例子**:
```bash
#!/bin/bash
export GTK_IM_MODULE=xim
export QT_IM_MODULE=xim
export XMODIFIERS=@im=fcitx
# 不管 GTK 还是 Qt 程序，都走 XIM 接口，而 XIM 背后用的是 fcitx 输入法”
export WINEPREFIX="$HOME/wechat"
# 如果你全屏/最大化会闪，可以保留这行
export LIBGL_ALWAYS_SOFTWARE=1
exec wine "$HOME/wechat/drive_c/Program Files/Tencent/Weixin/Weixin.exe"
```
## 🔑 赋执行权限
```bash
chmod +x ~/bin/ob_file
```
## 📌 确保 PATH 包含 ~/bin
```bash
echo $PATH
```
如果没有：
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
## 🚀 使用
```bash
ob_file
```
## ✔ 优点
* 可扩展逻辑
* 可传参数
* 更接近脚本工具
## 🔥 推荐优化
直接改名：
```bash
mv ~/bin/ob_file ~/bin/ob
```
👉 使用：
```bash
ob
```
	👉 比 alias 更干净
# 🧩 方案三：函数（最灵活 ⭐⭐⭐⭐⭐）
在 `~/.bashrc` 中：
```bash
ob() {
    obsidian "/media/loviya/新的D盘/obsidian_notes"
}
```
## 🚀 使用
```bash
ob
```
## ✔ 优点
* 支持参数
* 可扩展逻辑
* 比 alias 强
# 🧩 方案四：桌面快捷方式（GUI）
 #### **这是添加的**.
```bash
nano ~/.local/share/application/wechat.desktop  # 可以在应用搜索搜到，super建然后搜索
chmod +x  ~/.local/share/application/wechat.desktop 
cp ~/.local/share/application/wechat.desktop  ~/桌面/
chmod +x ~/桌面/wechat.desktop # 添加权限然后右键允许启动
```
```
## 📌 创建 `.desktop`
k
```bash
nano ~/Desktop/obsidian-myvault.desktop
```
写入：
```ini
[Desktop Entry]
Name=My Obsidian Vault
Exec=obsidian "/media/loviya/新的D盘/obsidian_notes"
Icon=obsidian
Type=Application
Terminal=false
```
  **再给一个例子**:
  ```bash
  [Desktop Entry]
Name=wechat
Name[zh_CN]=微信
Exec=/home/loviya/run-wechat.sh
Icon=/usr/share/icons/hicolor/256x256/apps/wechat.png
Type=Application
Categories=Utility;
StartupNotify=true
Terminal=false
  ```

## 🔑 赋权限
```bash
chmod +x ~/Desktop/obsidian-myvault.desktop
```
## 🚀 使用
* 双击打开
* 可固定到 dock
# 🧠 alias vs 脚本 vs 函数
| 方式       | 推荐    | 特点     |
| -------- | ----- | ------ |
| alias    | ⭐⭐⭐⭐  | 简单快捷   |
| 脚本       | ⭐⭐⭐⭐⭐ | 最通用    |
| 函数       | ⭐⭐⭐⭐⭐ | 最灵活    |
| .desktop | ⭐⭐⭐   | GUI 使用 |
# 🧠 Bash 引号规则（关键知识）
## 单引号 `'...'`
* 完全原样输出
* 不解析变量
* 不执行命令
```bash
echo '$HOME'
# 输出: $HOME
```
## 双引号 `"..."`
* 解析变量
* 执行命令替换
```bash
echo "$HOME"
# 输出: /home/loviya
```
## 推荐写法（避免嵌套地狱）
```bash
alias ob='obsidian /media/loviya/新的D盘/obsidian_notes'
```
# ⚠️ 常见坑总结
## ❌ alias 写错
```bash
alias ob = xxx   # 错
```
✔ 正确：
```bash
alias ob='xxx'
```
## ❌ 路径没加引号
```bash
obsidian /path with space   # 错
```
✔ 正确：
```bash
obsidian "/path with space"
```
## ❌ ~/bin 不存在
```bash
nano ~/bin/ob   # 报错
```
✔ 解决：
```bash
mkdir -p ~/bin
```
## ❌ 修改 bashrc 不生效
✔ 解决：
```bash
source ~/.bashrc
```
# 🚀 进阶：多仓库管理（强烈推荐）
## alias 方式
```bash
alias ob_main='obsidian ~/vaults/main'
alias ob_linux='obsidian ~/vaults/linux'
alias ob_tmp='obsidian ~/vaults/tmp'
```
## 函数方式（更高级）
```bash
ob() {
    case "$1" in
        main) obsidian ~/vaults/main ;;
        linux) obsidian ~/vaults/linux ;;
        tmp) obsidian ~/vaults/tmp ;;
        *) echo "Usage: ob [main|linux|tmp]" ;;
    esac
}
```
## 🚀 使用
```bash
ob main
ob linux
```
# 🧠 一句话总结
👉 Ubuntu 里没有 `.bat` 和 `$PROFILE`
👉 对应替代是：
* `.bashrc` → alias / function
* shell 脚本 → `~/bin/xxx`
* `.desktop` → 双击启动
如果你下一步想升级，我可以帮你做一套：
👉 **“Obsidian + Linux + 知识库结构（结合你现在折腾 Wine / Linux）”完整体系**
