# Bash内建命令速查

这份文件专门列 Bash 常见内建命令。它们不是外部程序，而是 Bash 自己实现的。

## 常见内建命令

### `cd`

切换目录。

### `pwd`

显示当前目录。在很多系统里也有外部版本，但日常可理解为基础命令。

### `echo`

输出文本。

### `printf`

格式化输出。

### `read`

读取用户输入。

### `export`

导出环境变量。

### `unset`

删除变量或函数。

### `readonly`

设置只读变量或函数。

### `alias`

定义别名。

### `unalias`

取消别名。

### `history`

查看历史命令。

### `help`

查看 Bash 内建帮助。

### `type`

判断命令类型。

### `source`

在当前 shell 中执行脚本。

```bash
source ~/.bashrc
```

也可以写成：

```bash
. ~/.bashrc
```

### `exec`

用新程序替换当前 shell 进程。

```bash
exec bash
```

### `eval`

把参数重新当作命令执行。

```bash
cmd="ls -la"
eval "$cmd"
```

使用时要小心，避免执行不可信输入。

### `shift`

脚本参数左移。

```bash
shift
```

### `getopts`

解析脚本选项。

```bash
while getopts ":f:n:" opt; do
  case $opt in
    f) file="$OPTARG" ;;
    n) num="$OPTARG" ;;
  esac
done
```

### `trap`

捕获信号并执行动作。

```bash
trap 'echo 中断了' INT
```

### `times`

显示 shell 和子进程时间统计。

### `wait`

等待后台任务完成。

```bash
wait
wait $pid
```

### `jobs`

查看当前 shell 任务。

### `bg` / `fg`

后台、前台任务切换。

### `test` / `[ ]` / `[[ ]]`

条件测试。

## 查看完整内建命令列表

```bash
compgen -b
help
enable -a
```

说明：

- `compgen -b`：列出 bash builtins
- `help`：列出大量内建命令帮助入口
- `enable -a`：查看内建命令启用状态
