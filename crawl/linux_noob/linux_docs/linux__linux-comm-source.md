# Linux source 命令 

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、什么是 source 命令

source 是 Linux/Unix 系统中的一个内置 shell 命令，用于在当前 shell 环境中执行指定文件中的命令。与直接运行脚本不同，source 命令不会创建新的子 shell，而是在当前 shell 中直接执行文件内容。

### 类比理解

可以把 source 命令想象成"复制粘贴"操作：

  * 普通执行脚本：像是把文件发给别人执行（新开终端）
  * source 命令：像是把文件内容直接粘贴到你当前的终端中执行



* * *

## 二、source 命令的基本语法

## 实例

```bash
source 文件名 [ 参数 ]
```


或者使用等效的点号(.)表示法：

## 实例

```bash
. 文件名 [ 参数 ]
```


### 参数说明

  * **文件名** ：要执行的脚本文件路径（可以是相对路径或绝对路径）
  * **参数** ：可选，传递给脚本的参数



* * *

## 三、source 命令与直接执行脚本的区别

对比项 | source 命令 | 直接执行脚本  
---|---|---  
执行环境 | 当前 shell 环境 | 新建子 shell 环境  
变量影响 | 会改变当前 shell 的环境变量 | 不影响当前 shell 的环境  
进程关系 | 不创建新进程 | 创建新进程  
退出影响 | 如果脚本中有 exit，会退出当前 shell | 只退出子 shell  
  
* * *

## 四、source 命令的典型应用场景

### 1\. 加载环境变量配置

最常见的用途是加载 `~/.bashrc` 或 `/etc/profile` 等配置文件：

## 实例

```bash
source ~ / .bashrc
```


### 2\. 激活虚拟环境

在 Python 开发中激活虚拟环境：

## 实例

```bash
source venv / bin / activate
```


### 3\. 更新当前 shell 环境

当修改了配置文件但不想重新登录时：

## 实例

```bash
source / etc / profile
```


### 4\. 模块化脚本开发

将大型脚本拆分为多个小文件，用 source 引入：

## 实例

```bash
# 在主脚本中 source utils.sh # 引入工具函数 source config.sh # 引入配置
```


* * *

## 五、实际使用示例

### 示例1：加载自定义环境变量

创建测试文件 `myenv.sh`：

## 实例

```bash
#!/bin/bash export MY_VAR = "Hello World" alias ll = 'ls -alF'
```


使用 source 加载：

## 实例

```bash
source myenv.sh echo $MY_VAR # 输出: Hello World ll # 等效于 ls -alF
```


### 示例2：调试脚本

当调试脚本时，可以使用 source 来保留脚本中设置的变量：

## 实例

```bash
source debug_script.sh # 脚本中设置的变量现在可以在当前 shell 中检查
```


* * *

## 六、注意事项与常见问题

  1. **安全性** ：source 会直接在当前环境执行文件内容，只 source 可信的文件
  2. **文件查找** ：source 使用当前 shell 的 PATH 查找文件，建议使用完整路径
  3. **错误处理** ：如果 sourced 文件中有错误，会影响当前 shell
  4. **递归问题** ：避免在 sourced 文件中再 source 自身，会导致无限循环



### 常见错误

## 实例

```bash
# 错误：忘记文件需要有可执行权限 source . / script.sh # 如果 script.sh 不可读 # 错误：文件不存在 source non_exist_file.sh
```


* * *

## 七、替代方案比较

### 1\. source vs export

  * `export` 只设置变量
  * `source` 可以执行任意命令



### 2\. source vs eval

  * `eval` 执行字符串而非文件
  * `source` 更安全，有明确的文件来源



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
