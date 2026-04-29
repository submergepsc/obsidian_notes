# Linux chattr 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux chattr 命令用于改变文件或目录的属性，这些属性可以控制文件系统的行为，提供更高级的文件管理功能。

常用属性 

### 语法

```bash
chattr [选项] [+/-/=属性] 文件或目录
```


### 常用选项

  * `-R`: 递归处理目录及其子目录
  * `-V`: 显示详细信息
  * `-v`: 显示版本信息



### 属性模式

  * `+` : 添加属性
  * `-` : 移除属性
  * `=` : 设置为指定属性



### 常用属性

属性 | 说明  
---|---  
`a` | **仅追加** ：文件只能追加内容，不能删除或修改已有内容（需 root 权限）。  
`i` | **不可变** ：文件不能被删除、修改、重命名或创建硬链接（需 root 权限）。  
`A` | 不更新文件的最后访问时间（`atime`）。  
`c` | 文件在磁盘上自动压缩（部分文件系统支持）。  
`s` | 安全删除：文件被删除时，其数据会被清零（不可恢复）。  
`u` | 文件被删除后，其内容仍可恢复（与 `s` 相反）。  
`d` | 文件在 `dump` 备份时会被跳过。  
  
### 实例

**添加属性（+）：**

```bash
sudo chattr +i file.txt # 设置文件为不可变（防删除/修改） sudo chattr +a /var/log/syslog # 日志文件只能追加
```


**移除属性（-）：**

```bash
sudo chattr -i file.txt # 取消不可变属性
```


**重置属性（=）：**

```bash
sudo chattr =a file.txt # 移除所有属性，仅保留 `a`
```


**保护重要配置文件：**

```bash
chattr +i /etc/passwd chattr +i /etc/shadow
```


**设置日志文件只能追加：**

```bash
chattr +a /var/log/messages
```


**递归设置目录属性：**

```bash
chattr -R +i /etc/important/
```


**查看文件属性（使用 lsattr 命令）：**

```bash
lsattr filename
```


输出示例：

```bash
\----i--------- file.txt # `i` 表示不可变
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
