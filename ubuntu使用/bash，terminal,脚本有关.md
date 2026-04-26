

lsblk
[[bash，terminal,脚本有关/bash一些快捷操作]]


[[which和type的区别]] 

# bash脚本解读
[[bash，terminal,脚本有关/bash知识全景]]



[[nvm自动切换|command -v nvm >/dev/null 2>&1 && nvm use 22 >/dev/null]]
[[bash，terminal,脚本有关/nano里面取消tmux接管鼠标|set-hook -g pane-focus-in 'if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "tmux set -g mouse off" "tmux set -g mouse on"']]

# tmux有关
[[bash，terminal,脚本有关/bash,zsh_dash,sh,tmux介绍]]

[[bash，terminal,脚本有关/tmux介绍]]

[[终端窗口_tmux会话_分页与分屏]]




# 其他
[[bash，terminal,脚本有关/ctrl+26个字母快捷方式]]

[[bash，terminal,脚本有关/bash指令顺序和错误示例]]



--- 

`source $HOME/.cargo/env`当前环境立即生效。

`nautilus .`打开资源管理器
`xdg-open .`自动识别，如果是文件夹就调用资源管理器

**其外号：**：
```bash
	nano ~/.bashrc #打开文件
	# 在末尾添加：
	alias explorer='nautilus'
	#ctrl+o保存，ctrl+x退出
		source ～/。bashrc
	# 
```

ps -ef | grep Weixin.exe:chaxun weixin.exe juedui lujing :
`WINEPREFIX=~/wechat wine cmd`cmd
`WINEPREFIX=~/wechat wine taskmgr`renwuguanliqi
`WINEPREFIX=~/wechat wine explorer`
`ps -ef | grep fcitx` quebao fcitx
`fcitx5 -r`yunxing

`pkill -f pty`
`pkill -f terminal`///两个关闭终端的方法
`pkill -u "$USER"`关闭所有进程
`pkill -f Weixin.exe



`pstree -s $$`查看
`killall gnome-terminal-server`我目前的terminal名称


- 一条linux命令查询顺序
```bash
1️⃣ alias（别名）
2️⃣ 函数（function）
3️⃣ shell 内建命令（builtin）
4️⃣ PATH 里的可执行文件
```

查看别名： alias (wechat)
builtin: help
查看内置命令： type cd 
查看$PATH: echo $PATH
查看$ PATH里的程序：  which wechat
查看函数: declare -f (wechat 具体函数)   /type wechat
			declare -F(近查看函数名称)
			
| 类型       | 跳过（bypass）                                      | 强制使用（force）          | 删除 / 禁用                     |
| -------- | ----------------------------------------------- | -------------------- | --------------------------- |
| alias    | `\cmd`（只跳 alias）`command cmd`（跳 alias+function） | ❌ 无                  | `unalias name`(作用范围当前shell) |
| function | `command cmd`（跳 alias+function）                 | ❌ 无                  | `unset -f name`             |
| builtin  | `enable -n cmd`（禁用后走 PATH）                      | `builtin cmd`        | ❌ 不能删除`enable -n name` 可禁用  |
| PATH 程序  | 通过禁用 builtin（`enable -n`）绕开                     | `/usr/bin/cmd`（绝对路径） | 删除文件 / 修改 PATH              |


**nvm是函数**
`hash -r `刷新哈希表

sudo pkill -9 mihomo; ps -ef | grep -i clash ; resolvectl status  # 检查dns情况; env | grep -i proxy;


- bash执行一行命令的顺序
```txt
1️⃣ 词法解析（拆 token）
2️⃣ alias 展开
3️⃣ 变量展开
4️⃣ 命令执行
```









星火商店安装wine酷狗命令
![](assets/Pasted%20image%2020260425004100.png)

