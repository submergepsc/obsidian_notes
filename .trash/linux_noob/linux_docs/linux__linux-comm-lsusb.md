# Linux lsusb 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 lsusb 命令

`lsusb` 是 Linux 系统中一个用于列出所有连接到计算机的 USB 设备的实用命令。它相当于"list USB"的缩写，能够显示 USB 总线及其连接的设备详细信息。

### 命令作用

  1. 查看当前系统连接的 USB 设备列表
  2. 获取 USB 设备的详细信息（厂商ID、产品ID等）
  3. 诊断 USB 连接问题
  4. 验证 USB 设备是否被系统正确识别



* * *

## 基本语法

```bash
lsusb [选项]
```


### 常用选项参数说明

选项 | 说明  
---|---  
`-v` | 显示详细输出（verbose），包括设备描述符信息  
`-t` | 以树状结构显示 USB 设备层次关系  
`-s [[bus]:][devnum]` | 仅显示指定总线和设备号的设备  
`-d [vendor]:[product]` | 仅显示指定厂商ID和产品ID的设备  
`-D 设备文件` | 显示指定设备文件的详细信息  
`--help` | 显示帮助信息  
`--version` | 显示版本信息  
  
* * *

## 基础使用示例

### 1\. 列出所有 USB 设备（基本用法）

## 实例

```bash
lsusb
```


典型输出示例：

```bash
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub Bus 001 Device 004: ID 8087:0a2b Intel Corp. Bus 001 Device 003: ID 046d:c52b Logitech, Inc. Unifying Receiver Bus 001 Device 002: ID 05e3:0608 Genesys Logic, Inc. Hub Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```


输出解析：

  * `Bus XXX`: USB 总线编号
  * `Device XXX`: 设备在该总线上的编号
  * `ID XXXX:XXXX`: 厂商ID:产品ID
  * 设备描述信息



### 2\. 显示详细信息（-v 选项）

## 实例

```bash
lsusb -v
```


这个命令会输出非常详细的 USB 设备信息，包括：

  * 设备描述符
  * 配置描述符
  * 接口描述符
  * 端点描述符
  * 设备支持的 USB 协议版本
  * 设备类别、子类别和协议



* * *

## 高级用法

### 1\. 树状显示 USB 设备连接关系

## 实例

```bash
lsusb -t
```


示例输出：

```bash
/: Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M /: Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/10p, 480M |__ Port 3: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 12M |__ Port 4: Dev 4, If 0, Class=Wireless, Driver=btusb, 12M
```


### 2\. 筛选特定设备

## 实例

```bash
# 仅显示总线1上的设备 lsusb -s 1 : # 仅显示总线1设备3 lsusb -s 1 : 3 # 仅显示Logitech设备（通过厂商ID:产品ID） lsusb -d 046d:
```


### 3\. 查看特定设备文件信息

## 实例

```bash
lsusb -D / dev / bus / usb / 001 / 003
```


* * *

## 实际应用场景

### 1\. 检查USB设备是否被识别

当插入USB设备但无法使用时，首先使用 `lsusb` 检查系统是否识别了该设备。

### 2\. 获取设备ID用于驱动安装

许多Linux驱动需要知道设备的厂商ID和产品ID，这些信息可以通过 `lsusb` 获取。

### 3\. 调试USB连接问题

通过比较插入设备前后的 `lsusb` 输出，可以判断设备是否被正确识别。

### 4\. 查看USB设备详细信息

使用 `-v` 选项可以获取设备的详细技术规格，有助于开发USB相关应用。

* * *

## 常见问题解答

### Q1: 为什么我的USB设备没有出现在 lsusb 输出中？

可能原因：

  1. 设备物理连接有问题
  2. USB端口或集线器故障
  3. 设备电源不足
  4. 内核驱动问题



### Q2: 如何通过 lsusb 输出判断设备速度？

在详细输出 (`lsusb -v`) 中查找 `bcdUSB` 字段：

  * `2.00`: USB 2.0
  * `3.00`: USB 3.0
  * `3.10`: USB 3.1



### Q3: 如何永久保存 lsusb 输出？

## 实例

```bash
lsusb > usb_devices.txt
```


* * *

## 实践练习

  1. 插入一个USB设备，观察 `lsusb` 输出的变化
  2. 使用 `-d` 选项查找特定厂商的设备
  3. 比较 `lsusb` 和 `lsusb -v` 的输出差异
  4. 尝试使用 `-t` 选项理解USB设备的连接拓扑



* * *

## 总结

`lsusb` 是一个简单但功能强大的工具，能够帮助用户和系统管理员：

  * 快速查看连接的USB设备
  * 获取设备详细信息
  * 诊断USB相关问题
  * 为驱动安装提供必要信息



掌握 `lsusb` 命令的使用，能够让你在Linux环境下更高效地管理和调试USB设备。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
