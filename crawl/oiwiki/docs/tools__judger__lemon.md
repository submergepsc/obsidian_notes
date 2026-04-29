# Lemon - OI Wiki

- Source: https://oi-wiki.org/tools/judger/lemon/

# Lemon

## Lemon

Warning

macOS 下 Lemon 可能会出现内存测试不准确的情况，因为 macOS 缺少部分 Linux 的监测工具，且 Lemon-Linux 也没有针对 macOS 进行优化．

**Lemon** 是 zhipeng-jia 编写的开源评测工具，源代码托管于 [zhipeng-jia/project-lemon](https://github.com/zhipeng-jia/project-lemon)．

### 可直接运行的版本

  * Ir1d 提供了一份 Linux 下编译好的版本，源代码托管于 [FreestyleOJ/Project_lemon](https://github.com/FreestyleOJ/Project_lemon/tree/Built)．
  * （已停止维护）Menci 提供了一份更新的版本，源代码托管于 [Menci/Lemon](https://github.com/Menci/Lemon/)．
  * （已停止维护）Dust1404 维护了一份支持子文件夹和单题测试等功能的版本，源代码托管于 [Dust1404/Project_LemonPlus](https://github.com/Dust1404/Project_LemonPlus)．
  * iotang 和 Coelacanthus 维护了一份支持子文件夹和单题测试等功能的版本，源代码托管于 [Project-LemonLime/Project_LemonLime](https://github.com/Project-LemonLime/Project_LemonLime)．

### 自行编译

Ubuntu：

```text 1 2 3 4 5 6 7 ``` |  ```text sudo apt update sudo apt install qt5-default build-essential git -y git clone \--depth = 1 https://github.com/Menci/Lemon.git cd lemon # 可以修改 -j 后面的数字来调整 make job 的线程数 ./make -j2 sudo install -Dm755 -t /usr/bin/ Lemon ```   
---|---  
  
如要编译 LemonLime，请参阅 LemonLime 的 [编译手册](https://github.com/Project-LemonLime/Project_LemonLime/blob/master/BUILD.md)．

### 数据格式

首先打开 lemon 选择「新建试题」，然后打开新建试题的文件夹．

题目和数据应该如以下格式所示：

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text ├── data │ ├── gendata.py │ ├── product │ │ ├── product100.in │ │ ├── product100.out │ │ ├── product10.in │ │ ├── product10.out │ │ ├── product11.in ... ```   
---|---  
  
当所有试题添加完成后，回到 lemon 选择「自动添加试题」．此时题目和数据点将显示在 lemon 当中．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/tools/judger/lemon.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/tools/judger/lemon.md "edit.link.title")  
>  __本页面贡献者：[AP54](https://github.com/AP54), [bear-good](https://github.com/bear-good), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [HeRaNO](https://github.com/HeRaNO), [i-Yirannn](https://github.com/i-Yirannn), [Ir1d](https://github.com/Ir1d), [NachtgeistW](https://github.com/NachtgeistW), [ranwen](https://github.com/ranwen), [Tiger3018](https://github.com/Tiger3018), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
