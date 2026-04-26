# Hello, World! - OI Wiki

- Source: https://oi-wiki.org/lang/helloworld/

# Hello, World!

## ç¯å¢é ç½®

å·¥æ¬²åå ¶äºï¼å¿ å å©å ¶å¨ï¼

### éæå¼åç¯å¢

IDE æä½è¾ä¸ºç®åï¼ä¸è¬å ¥é¨ç©å®¶ä¼éç¨ IDE æ¥ç¼åä»£ç ï¼å¨ç«èµä¸­æå¸¸è§çæ¯ [Dev-C++](../../tools/editor/devcpp/)ï¼å¦æèè¯ç¯å¢æ¯ Windows ç³»ç»ï¼ä¸è¬ä¹ä¼æä¾è¿ä¸ IDEï¼ï¼

### ç¼è¯å¨

#### Windows

æ¨èä½¿ç¨ GNU ç¼è¯å¨ï¼éè¦å» [MinGW Distro](https://nuwen.net/mingw.html) ä¸è½½ MinGW å¹¶å®è£ ï¼æ­¤å¤ Windows ä¸ä¹å¯ä»¥éæ© [Microsoft Visual C++ ç¼è¯å¨](https://docs.microsoft.com/en-us/cpp/build/projects-and-build-systems-cpp)ï¼éè¦å» [Visual Studio é¡µé¢](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019) ä¸è½½å®è£ ï¼

#### macOS

å¨ç»ç«¯ä¸­æ§è¡ï¼

```text 1 ``` |  ```text xcode-select \--install ```   
---|---  
  
#### Linux

ä½¿ç¨ `g++ -v` æ¥æ£æ¥æ¯å¦å®è£ è¿ `g++`ï¼

ä½¿ç¨å¦ä¸å½ä»¤å¯ä»¥å®è£ ï¼

```text 1 ``` |  ```text sudo apt update && sudo apt install g++ ```   
---|---  
  
#### å¨å½ä»¤è¡ä¸­ç¼è¯ä»£ç 

çç»ä¹åä¹æç©å®¶ä¼ä½¿ç¨æ´çµæ´»çå½ä»¤è¡æ¥ç¼è¯ä»£ç ï¼è¿æ ·å°±ä¸ä¾èµ IDE äºï¼èæ¯ä½¿ç¨èªå·±çæçææ¬ç¼è¾å¨ç¼åä»£ç ï¼

```text 1 ``` |  ```text g++ test.cpp -o test -lm ```   
---|---  
  
`g++` æ¯ C++ è¯­è¨çç¼è¯å¨ï¼C è¯­è¨çç¼è¯å¨ä¸º `gcc`ï¼ï¼`-o` ç¨äºæå®å¯æ§è¡æä»¶çæä»¶åï¼ç¼è¯éé¡¹ `-lm` ç¨äºé¾æ¥æ°å­¦åº `libm`ï¼ä»èä½¿å¾ä½¿ç¨ `math.h` çä»£ç å¯ä»¥æ­£å¸¸ç¼è¯è¿è¡ï¼

æ³¨ï¼C++ ç¨åºä¸éè¦ `-lm` å³å¯æ­£å¸¸ç¼è¯è¿è¡ï¼åå¹´ NOI/NOIP è¯é¢ç C++ ç¼è¯éé¡¹ä¸­é½å¸¦ç `-lm`ï¼æ è¿éä¹ä¸å¹¶å ä¸ï¼

## ç¬¬ä¸ä»½ä»£ç 

éè¿è¿æ ·ä¸ä¸ªç¤ºä¾ç¨åºæ¥å±å¼ C++ å ¥é¨ä¹æ å§ï½

æ³¨ï¼è¯·å¨ç¼ååæ³¨æå¼å¯è±æè¾å ¥æ³ï¼

C++ è¯­è¨

```text 1 2 3 4 5 6 ``` |  ```text #include <iostream> // å¼ç¨å¤´æä»¶ int main () { // å®ä¹ main å½æ° std :: cout << "Hello, world!" ; // ä½¿ç¨æ åå½åç©ºé´ä¸­ç cout å½æ° return 0 ; // è¿å 0ï¼ç»æ main å½æ°ï¼ç¼è¯å¨ä¸è¬ä¼èªå¨å ä¸è¿ä¸è¡ï¼ä¸è¬å¯ä»¥çç¥ } ```   
---|---  
  
C è¯­è¨

```text 1 2 3 4 5 6 ``` |  ```text #include <stdio.h> // å¼ç¨å¤´æä»¶ int main () { // å®ä¹ main å½æ° printf ( "Hello, world!" ); // è¾åº Hello, world! return 0 ; // è¿å 0ï¼ç»æ main å½æ° } ```   
---|---  
  
æ³¨æï¼C è¯­è¨å¨è¿éä» ååèï¼C++ åºæ¬å ¼å®¹ C è¯­è¨ï¼å¹¶ä¸æ¥æè®¸å¤æ°çåè½ï¼å¯ä»¥è®©éæå¨èµåºä¸äºåååï¼å ·ä½è¯·è§ [C++ ä¸å ¶ä»å¸¸ç¨è¯­è¨åºå«](../cpp-other-langs/)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/helloworld.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/helloworld.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [mgt](mailto:i@margatroid.xyz), [ucSec](https://github.com/ucSec), [lihaoyu1234](https://github.com/lihaoyu1234), [cbw2007](https://github.com/cbw2007), [cmpute](https://github.com/cmpute), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](mailto:1609483441@qq.com), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [gavinliu266](https://github.com/gavinliu266), [H-J-Granger](https://github.com/H-J-Granger), [ksyx](https://github.com/ksyx), [NachtgeistW](https://github.com/NachtgeistW), [orzAtalod](https://github.com/orzAtalod), [Persdre](https://github.com/Persdre), [SodaCris](mailto:18463922396@163.com), [Tiphereth-A](https://github.com/Tiphereth-A), [yanboishere](https://github.com/yanboishere)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
