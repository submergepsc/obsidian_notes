# 启动项 BIOS / UEFI / EFI 分区相关命令

这篇笔记主要处理 UEFI 启动项、EFI 系统分区挂载、Windows / Ubuntu 启动文件修复、以及卸载分区时出现 `busy` 的情况。

先记住几个概念：

- BIOS / UEFI：主板固件。新电脑一般是 UEFI。
- EFI 系统分区：一般是 FAT32 格式的小分区，里面放启动文件，常见挂载点是 `/boot/efi`。
- NVRAM 启动项：主板保存的启动菜单项，例如 Ubuntu、Windows Boot Manager。
- `efibootmgr`：Linux 下查看、创建、删除、调整 UEFI 启动项的工具。
- `/dev/nvme0n1p1`：一个磁盘分区示例，不一定是你的 EFI 分区。
- `/dev/nvme0n1`：整块 NVMe 磁盘。
- `p1`、`p9`：第 1 个分区、第 9 个分区。

不要直接照抄分区编号。先用 `lsblk -f` 确认哪个分区是 EFI 分区。

## 1. EFI / 启动项

```bash
sudo efibootmgr
```

查看当前 UEFI 启动项。

常见输出里会看到：

- `BootCurrent`：这次开机实际用的是哪个启动项。
- `BootOrder`：主板尝试启动的顺序。
- `Boot0000`、`Boot0007`：具体启动项编号。
- `ubuntu`、`Windows Boot Manager`：启动项名字。

这个命令只查看，不修改。

```bash
sudo efibootmgr -v
```

查看更详细的启动项信息。

`-v` 是 verbose，意思是详细输出。它会显示启动项指向哪个磁盘、哪个分区、哪个 `.efi` 文件。

这个命令很适合确认：

- Windows 启动项是不是指向 `\EFI\Microsoft\Boot\bootmgfw.efi`
- Ubuntu 启动项是不是指向 `\EFI\ubuntu\shimx64.efi` 或 `grubx64.efi`
- 启动项是否指向了已经不存在的分区

这个命令只查看，不修改。

```bash
sudo efibootmgr -b 0007 -B
```

删除编号为 `0007` 的 UEFI 启动项。

参数含义：

- `-b 0007`：选择 `Boot0007` 这个启动项。
- `-B`：删除这个启动项。

注意：这里删除的是主板 NVRAM 里的启动菜单记录，不是删除 EFI 分区里的文件。

风险：

- 如果删错，启动菜单里可能不再显示某个系统。
- 文件通常还在，之后可以用 `efibootmgr -c` 或系统修复工具重新创建。

使用前建议先执行：

```bash
sudo efibootmgr -v
```

确认 `0007` 到底是哪一个启动项。

```bash
sudo efibootmgr -c -d /dev/nvme0n1 -p 9 -L "Windows Boot Manager" -l '\EFI\Microsoft\Boot\bootmgfw.efi'
```

创建一个新的 UEFI 启动项，名字叫 `Windows Boot Manager`，指向 Windows 的 EFI 启动文件。

参数含义：

- `-c`：create，创建新启动项。
- `-d /dev/nvme0n1`：启动文件所在的整块磁盘。
- `-p 9`：启动文件所在磁盘的第 9 个分区。
- `-L "Windows Boot Manager"`：启动项显示名称。
- `-l '\EFI\Microsoft\Boot\bootmgfw.efi'`：EFI 分区内部的启动文件路径。

重点：

- `-d` 后面写整块磁盘，不写分区。这里是 `/dev/nvme0n1`，不是 `/dev/nvme0n1p9`。
- `-p` 后面写分区编号。`-p 9` 表示 `/dev/nvme0n1p9`。
- `-l` 后面的路径是 EFI 分区内部路径，使用反斜杠 `\`，不是 Linux 常见的 `/`。

这个命令常用于：

- Windows 启动项丢失。
- BIOS/UEFI 菜单里没有 Windows Boot Manager。
- EFI 文件还在，但主板启动项记录没了。

执行前必须确认第 9 个分区真的是 EFI 分区：

```bash
lsblk -f
```

EFI 分区通常特征：

- 文件系统是 `vfat` 或 `FAT32`
- 分区大小常见为 100MB 到 1GB
- 挂载点可能是 `/boot/efi`

```bash
sudo efibootmgr -o 0007,0000
```

设置 UEFI 启动顺序。

参数含义：

- `-o`：order，设置启动顺序。
- `0007,0000`：先尝试 `Boot0007`，再尝试 `Boot0000`。

这个命令会改变主板启动优先级。

常见用途：

- 让 Windows 优先启动。
- 让 Ubuntu / GRUB 优先启动。
- 临时修复开机总是进错系统的问题。

执行前建议先看当前启动项编号：

```bash
sudo efibootmgr
```

## 2. 挂载 / 卸载 EFI 分区

```bash
sudo mount /dev/nvme0n1p1 /mnt
```

把 `/dev/nvme0n1p1` 这个分区挂载到 `/mnt`。

挂载以后，访问 `/mnt` 就是在访问这个分区里的文件。

如果 `/dev/nvme0n1p1` 是 EFI 分区，那么挂载后可能看到：

```text
/mnt/EFI
```

里面可能有：

```text
Microsoft
ubuntu
Boot
```

注意：

- `/dev/nvme0n1p1` 只是示例。
- `/mnt` 是临时挂载点。
- 如果 `/mnt` 里面本来有内容，挂载后会暂时被遮住，卸载后才恢复显示。

更清晰的做法是先创建专用挂载点：

```bash
sudo mkdir -p /mnt/efi
sudo mount /dev/nvme0n1p1 /mnt/efi
```

```bash
sudo umount /dev/nvme0n1p1
```

正常卸载这个分区。

卸载后，系统不再通过挂载点访问这个分区。

注意命令是 `umount`，不是 `unmount`。

如果提示：

```text
target is busy
```

说明还有程序、终端、文件管理器、shell 当前目录正在使用这个分区。

```bash
sudo umount -l /dev/nvme0n1p1
```

懒卸载，`-l` 是 lazy。

含义：

- 先把挂载点从当前目录树里摘掉。
- 等没有程序继续使用它时，系统再真正释放。

适合情况：

- 普通 `umount` 提示 busy。
- 你已经确认没有重要写入操作。
- 只是想结束挂载状态。

风险：

- 如果分区还在写入，可能不如正常卸载稳妥。

```bash
sudo umount -lf /dev/nvme0n1p1
```

强制懒卸载。

参数含义：

- `-l`：lazy，懒卸载。
- `-f`：force，强制。

这是更激进的卸载方式。

风险：

- 如果有程序正在写文件，可能造成数据没有完全写入。
- 一般不要作为首选。

建议顺序：

1. 先用普通 `umount`
2. busy 时查占用
3. 确认没问题再用 `umount -l`
4. `umount -lf` 只作为最后手段

## 3. 磁盘查看

```bash
lsblk -f
```

查看磁盘、分区、文件系统、UUID、挂载点。

常用于确认：

- 哪个分区是 EFI 分区。
- 哪个分区是 Linux 根分区 `/`。
- 哪个分区已经挂载。
- 文件系统类型是 `vfat`、`ext4`、`ntfs` 还是其他。

示例重点：

- `FSTYPE` 是 `vfat` 的小分区，可能是 EFI。
- `MOUNTPOINTS` 是 `/boot/efi` 的分区，就是当前系统使用的 EFI 分区。

```bash
findmnt /boot/efi
```

查看 `/boot/efi` 这个挂载点对应哪个设备。

如果输出里显示 `/dev/nvme0n1p1`，说明当前系统的 EFI 分区就是 `/dev/nvme0n1p1`。

这个命令适合回答：

- 当前 Ubuntu 正在用哪个 EFI 分区？
- `/boot/efi` 有没有挂载？
- EFI 分区是不是挂错了？

```bash
mount | grep nvme0n1p1
```

从所有挂载记录里筛选包含 `nvme0n1p1` 的行。

参数和管道含义：

- `mount`：列出当前所有挂载。
- `|`：把左边命令输出交给右边。
- `grep nvme0n1p1`：只显示包含 `nvme0n1p1` 的行。

用途：

- 检查 `/dev/nvme0n1p1` 是否已经挂载。
- 查看它挂载到了哪里。

## 4. 占用检测 / 处理

```bash
sudo fuser -m /dev/nvme0n1p1
```

查看哪些进程正在使用这个分区。

参数含义：

- `fuser`：找出正在使用某个文件、目录或文件系统的进程。
- `-m`：按整个文件系统检查，而不是只检查单个文件。

常用于解决：

```text
umount: target is busy
```

输出通常是进程号 PID。可以再用下面命令查看进程是什么：

```bash
ps -fp 进程号
```

```bash
sudo fuser -km /dev/nvme0n1p1
```

杀掉正在使用这个分区的进程。

参数含义：

- `-k`：kill，杀掉占用进程。
- `-m`：按整个文件系统检查。

风险很高：

- 如果你的终端当前目录就在这个分区里，可能把相关 shell 或文件管理器杀掉。
- 如果有程序正在写文件，可能造成数据丢失。
- 不要在没看清 PID 的情况下随便执行。

更稳妥顺序：

```bash
sudo fuser -m /dev/nvme0n1p1
ps -fp 进程号
cd ~
sudo umount /dev/nvme0n1p1
```

只有确认可以杀时，再考虑：

```bash
sudo fuser -km /dev/nvme0n1p1
```

```bash
sudo lsof | grep nvme0n1p1
```

查看哪些打开的文件和 `nvme0n1p1` 有关。

参数含义：

- `lsof`：list open files，列出进程打开的文件。
- `grep nvme0n1p1`：筛选相关设备名。

用途：

- 找出是谁占用了挂载分区。
- 比 `fuser` 输出更详细，但内容也更多。

如果输出太多，可以针对挂载目录查：

```bash
sudo lsof +D /mnt/efi
```

## 5. 文件操作：EFI 修复

```bash
sudo cp -r /mnt/win/Windows/Boot/EFI/* /mnt/efi/EFI/Microsoft/
```

把 Windows 里的 EFI 启动文件复制到 EFI 分区的 Microsoft 目录。

参数含义：

- `cp`：复制。
- `-r`：递归复制目录。
- `/mnt/win/Windows/Boot/EFI/*`：源文件，Windows 分区里的 EFI 启动文件。
- `/mnt/efi/EFI/Microsoft/`：目标位置，EFI 分区里的 Microsoft 启动目录。

常见用途：

- Windows 的 EFI 文件缺失。
- EFI 分区里没有 `EFI/Microsoft`。
- 手动恢复 Windows Boot Manager 文件。

前提：

- Windows 系统分区已经挂载到 `/mnt/win`。
- EFI 分区已经挂载到 `/mnt/efi`。
- 目标目录存在或你先创建了它。

风险：

- 可能覆盖已有文件。
- 如果源路径或目标路径写错，可能复制到错误位置。

执行前建议先看：

```bash
ls /mnt/win/Windows/Boot/EFI
ls /mnt/efi/EFI
```

```bash
sudo rm -rf /mnt/old_efi/EFI/ubuntu
```

删除某个 EFI 分区里的 Ubuntu 启动文件目录。

参数含义：

- `rm`：删除。
- `-r`：递归删除目录。
- `-f`：强制删除，不逐个确认。
- `/mnt/old_efi/EFI/ubuntu`：要删除的目录。

风险非常高：

- 路径写错会直接删除错误目录。
- 删除后，Ubuntu 对应的启动文件可能没了。
- 如果这个 EFI 分区还在被当前系统使用，可能导致下次无法正常进 Ubuntu。

执行前必须确认：

```bash
ls /mnt/old_efi/EFI
findmnt /boot/efi
sudo efibootmgr -v
```

不要在不确定时执行 `rm -rf`。

```bash
ls /mnt/efi/EFI
```

查看 EFI 分区里的启动目录。

常见目录：

- `Microsoft`：Windows 启动文件。
- `ubuntu`：Ubuntu / GRUB 启动文件。
- `Boot`：默认 fallback 启动文件，常见 `BOOTX64.EFI`。

这个命令只查看，不修改。

## 6. 目录操作

```bash
sudo mkdir -p /mnt/efi
```

创建 `/mnt/efi` 目录，作为 EFI 分区的挂载点。

参数含义：

- `mkdir`：创建目录。
- `-p`：父目录不存在就一起创建；目录已经存在也不报错。

常见后续命令：

```bash
sudo mount /dev/nvme0n1p1 /mnt/efi
```

```bash
cd ~
```

回到当前用户的 home 目录。

这个命令经常用于卸载分区前。

原因：

如果你的 shell 当前目录在 `/mnt/efi` 或 `/mnt` 里面，系统会认为这个分区正在被使用，`umount` 可能提示 busy。先 `cd ~` 可以解除当前 shell 对挂载点的占用。

## 7. 分区工具

```bash
sudo apt install gparted
```

安装 GParted 图形化分区工具。

用途：

- 查看磁盘分区结构。
- 修改分区大小。
- 新建、删除、格式化分区。
- 给分区设置 EFI System Partition 标志。

需要联网和软件源可用。

```bash
sudo gparted
```

以管理员权限打开 GParted。

风险：

- GParted 可以删除、格式化、调整分区。
- 操作错磁盘会造成系统或数据损坏。

使用前建议：

- 确认当前选择的是哪块磁盘。
- 不要随手点 Apply。
- 分区调整前备份重要数据。

## 8. 系统操作

```bash
reboot
```

重启系统。

修改 UEFI 启动项、复制 EFI 文件、调整启动顺序后，通常需要重启来验证 BIOS/UEFI 是否能正常识别。

## 9. 综合流程：EFI 修复

原笔记里的流程：

```bash
lsblk -f
findmnt /boot/efi
sudo mount xxx /mnt
ls /mnt/EFI
sudo rm -rf ...
sudo umount -l xxx
sudo efibootmgr
sudo efibootmgr -b xxxx -B
```

逐步解释：

```bash
lsblk -f
```

先看所有磁盘分区，找出 EFI 分区、Windows 分区、Ubuntu 分区。

```bash
findmnt /boot/efi
```

确认当前 Ubuntu 正在使用哪个 EFI 分区。

```bash
sudo mount xxx /mnt
```

把某个分区挂载到 `/mnt`。

这里的 `xxx` 应替换成真实分区，例如：

```bash
sudo mount /dev/nvme0n1p1 /mnt
```

```bash
ls /mnt/EFI
```

查看挂载分区里的 EFI 目录。

如果报错没有这个目录，说明：

- 这个分区可能不是 EFI 分区。
- 或者 EFI 目录位置不对。

```bash
sudo rm -rf ...
```

删除某个目录或文件。

这里不能照抄省略号。必须替换成明确路径。

危险示例：

```bash
sudo rm -rf /mnt/EFI/ubuntu
```

含义是删除这个 EFI 分区里的 Ubuntu 启动文件。

执行前必须确认你真的要删除。

```bash
sudo umount -l xxx
```

懒卸载刚才挂载的分区。

`xxx` 可以是设备名，也可以是挂载点，例如：

```bash
sudo umount -l /dev/nvme0n1p1
sudo umount -l /mnt
```

更推荐写挂载点，因为直观：

```bash
sudo umount -l /mnt
```

```bash
sudo efibootmgr
```

查看当前 UEFI 启动项。

```bash
sudo efibootmgr -b xxxx -B
```

删除指定编号的启动项。

`xxxx` 要替换为真实编号，例如：

```bash
sudo efibootmgr -b 0007 -B
```

不要把 `xxxx` 原样执行。

## 10. 解决 busy

原笔记里的流程：

```bash
cd ~
sudo fuser -m /dev/xxx
sudo fuser -km /dev/xxx
sudo umount -l /dev/xxx
```

逐步解释：

```bash
cd ~
```

先离开挂载目录，避免当前终端占用分区。

```bash
sudo fuser -m /dev/xxx
```

查看哪个进程占用了这个分区。

`/dev/xxx` 要替换成真实设备，例如：

```bash
sudo fuser -m /dev/nvme0n1p1
```

```bash
sudo fuser -km /dev/xxx
```

杀掉占用这个分区的进程。

这是危险命令，建议先确认进程是什么：

```bash
ps -fp 进程号
```

```bash
sudo umount -l /dev/xxx
```

懒卸载分区。

更稳妥的 busy 处理顺序：

```bash
cd ~
sudo fuser -m /dev/nvme0n1p1
ps -fp 进程号
sudo umount /dev/nvme0n1p1
```

如果普通卸载仍然失败，再考虑：

```bash
sudo umount -l /dev/nvme0n1p1
```

只有确认可以结束占用进程时，才使用：

```bash
sudo fuser -km /dev/nvme0n1p1
```

## 11. 分区整理

```bash
sudo gparted
```

打开图形分区工具进行整理。

常见整理动作：

- 删除不用的旧 EFI 分区。
- 调整分区大小。
- 给正确的 EFI 分区设置 `esp`、`boot` 标志。
- 查看哪个分区是 FAT32 EFI 分区。

注意：

- 不要删除当前系统正在使用的 EFI 分区。
- 不要删除 Windows 或 Ubuntu 的系统分区。
- 分区操作前先备份重要数据。

## 12. 推荐排查顺序

如果只是想看启动项：

```bash
sudo efibootmgr
sudo efibootmgr -v
```

如果想确认 EFI 分区：

```bash
lsblk -f
findmnt /boot/efi
```

如果想临时查看 EFI 分区内容：

```bash
sudo mkdir -p /mnt/efi
sudo mount /dev/nvme0n1p1 /mnt/efi
ls /mnt/efi/EFI
sudo umount /mnt/efi
```

如果卸载时 busy：

```bash
cd ~
sudo fuser -m /dev/nvme0n1p1
sudo umount /dev/nvme0n1p1
```

如果要删除启动项：

```bash
sudo efibootmgr -v
sudo efibootmgr -b 0007 -B
```

如果要改启动顺序：

```bash
sudo efibootmgr
sudo efibootmgr -o 0007,0000
```

## 13. 最危险的命令

这些命令执行前一定要确认对象：

```bash
sudo efibootmgr -b 0007 -B
```

删除主板里的某个启动项。

```bash
sudo efibootmgr -c -d /dev/nvme0n1 -p 9 -L "Windows Boot Manager" -l '\EFI\Microsoft\Boot\bootmgfw.efi'
```

创建启动项。如果磁盘或分区编号写错，会创建一个错误启动项。

```bash
sudo efibootmgr -o 0007,0000
```

改变启动顺序。写错可能导致开机进入别的系统或启动失败。

```bash
sudo rm -rf /mnt/old_efi/EFI/ubuntu
```

删除 EFI 启动文件。路径写错风险很大。

```bash
sudo fuser -km /dev/nvme0n1p1
```

杀掉占用分区的进程。可能中断正在运行的程序。

```bash
sudo umount -lf /dev/nvme0n1p1
```

强制懒卸载。可能影响未写完的数据。
