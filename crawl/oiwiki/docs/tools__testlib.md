# Testlib 简介 - OI Wiki

- Source: https://oi-wiki.org/tools/testlib/

# Testlib 简介

如果你正在使用 C++ 出一道算法竞赛题目，Testlib 是编写相关程序（generator, validator, checker, interactor）时的优秀辅助工具．它是俄罗斯和其他一些国家的出题人的必备工具，许多比赛也都在用它：ROI、ICPC 区域赛、所有 Codeforces round……

Testlib 库仅有 `testlib.h` 一个文件，使用时仅需在所编写的程序开头添加 `#include "testlib.h"` 即可．

Testlib 的具体用途：

  * 编写 [Generator](generator/)，即数据生成器．
  * 编写 [Validator](validator/)，即数据校验器，判断生成数据是否符合题目要求，如数据范围、格式等．
  * 编写 [Interactor](interactor/)，即交互器，用于交互题．
  * 编写 [Checker](checker/)，即 [Special Judge](../special-judge/)．

Testlib 与 Codeforces 开发的 [Polygon](https://polygon.codeforces.com/) 出题平台完全兼容．

`testlib.h` 在 2005 年移植自 `testlib.pas`，并一直在更新．Testlib 与绝大多数编译器兼容，如 VC++ 和 GCC g++，并兼容 C++11．

**本文主要翻译自[Testlib - Codeforces](https://codeforces.com/testlib)．`testlib.h` 的 GitHub 存储库为 [MikeMirzayanov/testlib](https://github.com/MikeMirzayanov/testlib)．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/tools/testlib/index.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/tools/testlib/index.md "edit.link.title")  
>  __本页面贡献者：[sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [NachtgeistW](https://github.com/NachtgeistW), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
