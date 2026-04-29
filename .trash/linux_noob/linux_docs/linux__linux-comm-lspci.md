# Linux lspci 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 lspci 命令

`lspci` 是 Linux 系统中一个用于列出所有 PCI 设备信息的实用工具命令。PCI (Peripheral Component Interconnect) 是一种计算机总线标准，用于连接主板和各种硬件设备。

通过 `lspci` 命令，系统管理员和开发人员可以：

  * 查看系统中安装的所有 PCI 设备
  * 获取设备的详细信息，包括厂商 ID、设备 ID 等
  * 诊断硬件兼容性问题
  * 检查驱动程序是否正确加载



* * *

## 基本语法

`lspci` 命令的基本语法格式如下：

```bash
lspci [选项]
```


如果不带任何选项，`lspci` 会显示系统中所有 PCI 设备的简要信息列表。

* * *

## 常用选项参数

### 显示详细信息

## 实例

```bash
lspci -v # 显示详细信息(verbose) lspci -vv # 显示更详细的信息(very verbose) lspci -vvv # 显示最详细的信息(very very verbose)
```


### 特定设备查询

## 实例

```bash
lspci -s < 总线 > : < 设备 > . < 功能 > # 查看特定设备信息
```


例如：

## 实例

```bash
lspci -s 00: 02.0 # 查看总线00、设备02、功能0的设备
```


### 其他常用选项

## 实例

```bash
lspci -n # 以数字形式显示厂商和设备ID lspci -nn # 同时显示数字ID和设备名称 lspci -k # 显示内核驱动模块信息 lspci -t # 以树状图显示设备层次结构 lspci -mm # 机器可读格式输出 lspci -D # 显示完整域名(包括域号)
```


* * *

## 输出解读

一个典型的 `lspci` 输出如下：

```bash
00:00.0 Host bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX Host bridge (rev 01) 00:01.0 PCI bridge: Intel Corporation 440BX/ZX/DX - 82443BX/ZX/DX AGP bridge (rev 01) 00:07.0 ISA bridge: Intel Corporation 82371AB/EB/MB PIIX4 ISA (rev 08) 00:07.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01) 00:07.2 USB controller: Intel Corporation 82371AB/EB/MB PIIX4 USB (rev 01) 00:07.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08) 00:0f.0 VGA compatible controller: VMware SVGA II Adapter 00:10.0 SCSI storage controller: LSI Logic / Symbios Logic 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (rev 01) 00:11.0 Ethernet controller: Intel Corporation 82545EM Gigabit Ethernet Controller (Copper) (rev 01) 00:12.0 Multimedia audio controller: Ensoniq ES1371/ES1373 / Creative Labs CT2518 (rev 02)
```


输出格式说明：

  * **第一部分** ：`00:00.0` 是设备地址，格式为 `总线:设备.功能`
  * **第二部分** ：设备类型，如 "Host bridge"、"VGA compatible controller"等
  * **第三部分** ：设备厂商和具体型号



* * *

## 实际应用示例

### 示例1：查看所有PCI设备的基本信息

## 实例

```bash
lspci
```


### 示例2：查看显卡详细信息

## 实例

```bash
lspci -v | grep -i vga -A 12
```


### 示例3：查看USB控制器及其驱动信息

## 实例

```bash
lspci -v -k | grep -i usb -A 3
```


### 示例4：以树状结构显示PCI设备

## 实例

```bash
lspci -t
```


输出示例：

```bash
-[0000:00]-+-00.0 +-01.0 +-07.0 +-07.1 +-07.2 +-07.3 +-0f.0 +-10.0 +-11.0 \\-12.0
```


* * *

## 常见问题解决

### 1\. 命令未找到

如果系统提示 `lspci: command not found`，说明需要安装 `pciutils` 包：

## 实例

```bash
# Debian/Ubuntu sudo apt-get install pciutils # CentOS/RHEL sudo yum install pciutils
```


### 2\. 权限不足

普通用户执行 `lspci` 可能无法获取完整信息，可以使用 `sudo`：

## 实例

```bash
sudo lspci -v
```


### 3\. 设备识别问题

如果某些设备无法识别，可以尝试更新 PCI ID 数据库：

## 实例

```bash
sudo update-pciids
```


* * *

## 进阶技巧

### 1\. 结合 grep 过滤特定设备

## 实例

```bash
lspci | grep -i ethernet # 查找网卡 lspci | grep -i audio # 查找声卡
```


### 2\. 导出设备信息到文件

## 实例

```bash
lspci -vvv > pci_info.txt
```


### 3\. 查看设备的完整配置空间

## 实例

```bash
lspci -xxxx # 以十六进制显示配置空间
```


* * *

## 总结

`lspci` 是 Linux 系统下诊断和查看 PCI 设备信息的重要工具。通过本文的学习，你应该能够：

  1. 理解 `lspci` 命令的基本用法和常用选项
  2. 解读 `lspci` 的输出信息
  3. 使用 `lspci` 解决常见的硬件识别问题
  4. 掌握一些高级使用技巧



对于系统管理员和开发人员来说，熟练使用 `lspci` 命令可以帮助快速定位硬件相关问题，是 Linux 系统维护的重要技能之一。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
