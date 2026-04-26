```txt
Bash
├── ① 命令解析（Command Resolution）⭐核心
│   ├── alias
│   ├── function
│   ├── builtin
│   ├── PATH 查找
│   ├── command / builtin / type
│   └── hash 缓存（进阶）
│
├── ② 变量系统（Variables）⭐核心
│   ├── 普通变量
│   ├── 环境变量（export）
│   ├── 作用域（当前 shell / 子 shell）
│   ├── 特殊变量（$? $@ $1）
│   └── declare / readonly
│
├── ③ 执行模型（Execution Model）⭐⭐最重要
│   ├── 子 shell：()
│   ├── 当前 shell：{}
│   ├── 管道：|
│   ├── 后台：&
│   ├── 进程 vs shell
│   └── fork / exec（进阶理解）
│
├── ④ 重定向（Redirection）⭐⭐重点
│   ├── > >> < 
│   ├── 2>（stderr）
│   ├── 2>&1
│   ├── 文件描述符（0,1,2）
│   └── /dev/null
│
├── ⑤ 展开机制（Expansion）⭐容易混乱
│   ├── 变量展开：$var ${var}
│   ├── 命令替换：$(cmd)
│   ├── 通配符：*
│   ├── 引号规则（" vs '）
│   └── 顺序（很关键）
│
├── ⑥ 流控制（Control Flow）
│   ├── if / case
│   ├── for / while
│   ├── break / continue
│   └── test / [ ]
│
├── ⑦ 函数与脚本
│   ├── function 定义
│   ├── 参数传递（$1 $@）
│   ├── return / exit
│   └── source / 执行脚本
│
├── ⑧ 终端与系统（底层）
│   ├── stdin / stdout / stderr
│   ├── 信号（Ctrl+C）
│   ├── tty
│   └── job control（fg/bg）
│
└── ⑨ 高级（专家级）
    ├── set -e / -u / -o pipefail
    ├── trap（信号捕获）
    ├── exec（进程替换）
    ├── xargs / parallel
    └── shell 性能优化
```