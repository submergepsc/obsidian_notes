# ELF Format Mini Lab
这个目录用于学习 Linux 下 ELF 可执行文件的基本结构。
## 文件
- `hello_elf.c`: 一个很小的 C 程序，包含全局变量、只读字符串、函数和 `main`。
- `Makefile`: 编译、运行、查看 ELF 的快捷命令。
- `inspect_elf.sh`: 用 `file`、`readelf`、`objdump` 查看 ELF 头、节表、符号表和反汇编。
## 快速开始
```sh
make
make run
make inspect
```
## 看什么
1. `readelf -h hello_elf`
   - `Class`: 32 位还是 64 位。
   - `Type`: 可执行文件、共享库还是目标文件。
   - `Entry point address`: 程序入口地址。
2. `readelf -S hello_elf`
   - `.text`: 机器指令。
   - `.rodata`: 只读字符串，比如 `message`。
   - `.data`: 已初始化的全局变量，比如 `global_counter`。
   - `.symtab` / `.strtab`: 调试构建里能看到的符号名和字符串表。
3. `readelf -s hello_elf`
   - 能找到 `main`、`add`、`message`、`global_counter` 等符号。
4. `objdump -d hello_elf`
   - 能看到 `main` 对应的汇编指令。
## 清理
```sh
make clean
```
