# å½åç©ºé´ - OI Wiki

- Source: https://oi-wiki.org/lang/namespace/

# å½åç©ºé´

## æ¦è¿°

C++ ç **å½åç©ºé´** æºå¶å¯ä»¥ç¨æ¥è§£å³å¤æé¡¹ç®ä¸­åå­å²çªçé®é¢ï¼

ä¸¾ä¸ªä¾å­ï¼C++ æ ååºçææå å®¹åå®ä¹å¨ `std` å½åç©ºé´ä¸­ï¼å¦æä½ å®ä¹äºä¸ä¸ªå« `cin` çåéï¼åå¯ä»¥éè¿ `cin` æ¥è®¿é®ä½ å®ä¹ç `cin` åéï¼éè¿ `std::cin` è®¿é®æ ååºç `cin` å¯¹è±¡ï¼èä¸ç¨æ å¿äº§çå²çªï¼

## å£°æ

ä¸é¢çä»£ç å£°æäºä¸ä¸ªåå­å« `A` çå½åç©ºé´ï¼

```text 1 2 3 4 5 ``` |  ```text namespace A { int cnt ; void f ( int x ) { cnt = x ; } } // namespace A ```   
---|---  
  
å£°æä¹åï¼å¨è¿ä¸ªå½åç©ºé´å¤é¨ï¼ä½ å¯ä»¥éè¿ `A::f(x)` æ¥è®¿é®å½åç©ºé´ `A` å é¨ç `f` å½æ°ï¼ä¹å¯ä»¥éè¿ `A::cnt` æ¥è®¿é®å½åç©ºé´ `A` å é¨ç `cnt` åéï¼

å½åç©ºé´çå£°ææ¯å¯ä»¥åµå¥çï¼å æ­¤ä¸é¢è¿æ®µä»£ç ä¹æ¯å è®¸çï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text namespace A { namespace B { void f () { ... } } // namespace B void f () { B :: f (); // å®é è®¿é®çæ¯ A::B::f()ï¼ç±äºå½åä½äºå½åç©ºé´ A // å ï¼æä»¥å¯ä»¥çç¥åé¢ç A:: } } // namespace A void f () // è¿éå®ä¹çæ¯å ¨å±å½åç©ºé´ç f å½æ°ï¼ä¸ A::f å A::B::f // é½ä¸ä¼äº§çå²çª { A :: f (); A :: B :: f (); } ```   
---|---  
  
## `using` æä»¤

å£°æäºå½åç©ºé´ä¹åï¼å¦æå¨å½åç©ºé´å¤é¨è®¿é®å½åç©ºé´å é¨çæåï¼éè¦å¨æåååé¢å ä¸ `å½åç©ºé´::`ï¼

ææ²¡æä»ä¹æ¯è¾æ¹ä¾¿çæ¹æ³è½è®©æä»¬ç´æ¥éè¿æååè®¿é®å½åç©ºé´å çæåå¢ï¼ç­æ¡æ¯è¯å®çï¼æä»¬å¯ä»¥ä½¿ç¨ `using` æä»¤ï¼

`using` æä»¤æå¦ä¸ä¸¤ç§å½¢å¼ï¼

  1. `using å½åç©ºé´::æåå;`ï¼è¿æ¡æä»¤å¯ä»¥è®©æä»¬çç¥æä¸ªæåååçå½åç©ºé´ï¼ç´æ¥éè¿æååè®¿é®æåï¼ç¸å½äºå°è¿ä¸ªæåå¯¼å ¥äºå½åçä½ç¨åï¼
  2. `using namespace å½åç©ºé´;`ï¼è¿æ¡æä»¤å¯ä»¥ç´æ¥éè¿æååè®¿é®å½åç©ºé´ä¸­ç **ä»»ä½** æåï¼ç¸å½äºå°è¿ä¸ªå½åç©ºé´çæææåå¯¼å ¥äºå½åçä½ç¨åï¼

å æ­¤ï¼å¦ææ§è¡äº `using namespace std;`ï¼å°±ä¼å¨å½åä½ç¨åå° `std` ä¸­çææåå­å¼å ¥å°å ¨å±å½åç©ºé´å½ä¸­ï¼è¿æ ·ï¼æä»¬å°±å¯ä»¥ç¨ `cin` ä»£æ¿ `std::cin`ï¼ç¨ `cout` ä»£æ¿ `std::cout`ï¼

`using` æä»¤å¯è½ä¼å¯¼è´å½åå²çªï¼

ç±äº `using namespace std;` ä¼å° `std` ä¸­ç **ææåå­** å¼å ¥ï¼å æ­¤å¦æå£°æäºä¸ `std` éåçåéæå½æ°ï¼å°±å¯è½ä¼å ä¸ºå½åå²çªèå¯¼è´ç¼è¯éè¯¯ï¼

å æ­¤å¨å·¥ç¨ä¸­ï¼å¹¶ä¸æ¨èä½¿ç¨ `using namespace å½åç©ºé´;` çæä»¤ï¼

æäº `using` æä»¤ï¼[C++ è¯­æ³åºç¡](../basic/#cin-ä¸-cout) ä¸­çä»£ç å¯ä»¥æè¿ä¸¤ç§ç­ä»·åæ³ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text #include <iostream> using std :: cin ; using std :: cout ; using std :: endl ; int main () { int x , y ; cin >> x >> y ; cout << y << endl << x ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text #include <iostream> using namespace std ; int main () { int x , y ; cin >> x >> y ; cout << y << endl << x ; return 0 ; } ```   
---|---  
  
## æ åå½åç©ºé´

å½æä»¬å¨ä¸ä¸ªä½ç¨åéåªå®ä¹äºä¸ä¸ªç¨äºé²æ­¢åå­å²çªçå½åç©ºé´æ¶ï¼å ¶å®ä¹åä½¿ç¨å°å¯ä»¥åå¾éå¸¸ç®æ´ï¼æä»¬å¯ä»¥ä½¿ç¨æ åå½åç©ºé´ï¼

å½¢å¦ `namespace { /* something ... */ }`ï¼çç¥å½åç©ºé´çåå­ï¼å®ä¹çå½åç©ºé´è¢«ç§°ä¸ºæ åå½åç©ºé´ï¼ä¸ä¸ªæä»¶éçæ åå½åç©ºé´ä¼è¢«è§ä¸ºæ¥æç¬æçåå­ï¼åå ¶ä»å½åç©ºé´é½ä¸åï¼ä½åä¸ä¸ªä½ç¨åå å¤ä¸ªæ åå½åç©ºé´è¢«è§ä¸ºç¸åçå½åç©ºé´ï¼å¨æ åå½åç©ºé´å®ä¹åï¼å ¶ä¸­çåå­å¨å ¶å¤çä½ç¨åå å¯ä»¥å¨ä½¿ç¨æ¶è¢«æ¥æ¾å°ï¼å¦åå¨æ åå½åç©ºé´å®ä¹åå å ¥äºä¸æ¡ `using namespace` æä»¤ï¼

## åºç¨

### é²æ­¢å­ä»»å¡é´åå­å²çª

å¨ä¸äºå ·æå¤ä¸ªå­ä»»å¡çé®é¢ä¸­ï¼æä»¬å¯ä»¥å¯¹æ¯ä¸ªå­ä»»å¡åå®ä¹ä¸ä¸ªå½åç©ºé´ï¼å¨å ¶ä¸­å®ä¹æä»¬è§£å³è¯¥å­ä»»å¡æéè¦çåéä¸å½æ°ï¼è¿æ ·å³ä½¿ä¸¤ä¸ªå­ä»»å¡çå®ç°ä¸­å³ä½¿å£°æäºç¸ååå­ä¹ä¸ä¼å²çªï¼ä»èä½¿åä¸ªå­ä»»å¡é´äºä¸å¹²æ°ï¼ä¼å¨ä¸å®ç¨åº¦ä¸æ¹ä¾¿è°è¯ï¼ä¹ä¼æ¹åç¨åºçå¯è¯»æ§ï¼

### é²æ­¢ä¸æ ååºä»¥åç¯å¢å¼å ¥çåå­å²çª

åæ¶ï¼ä½¿ç¨å½åç©ºé´ä¹å¯ä»¥é²æ­¢ä¸äºç®æ³ç«èµä¸­å¸¸ç¨çåå­ä¸æ åå²çªï¼å¦ä¸ä¾ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text #include <math.h> #include <vector> using namespace std ; namespace Sol { int end ; // std::end è¢« using namespace std; å¼å ¥ int y1 ; // y1 æ¯ POSIX å®ä¹çç¬¬äºç±» Bessel å½æ° // å æ­¤éå¸¸æ åµä¸ï¼å¨ Linux ä¸ä¼æå²çªèå¨ Windows ä¸æ²¡æ void solve () { // å¨ Sol::solve() éæ éå®ï¼ä¸ç¨ ::ï¼å°ä½¿ç¨æä»¬å£°æç end ä»¥å y1 // å¹¶ä¸ä¼å¯¼è´åå­å²çªï¼ èè¥ä»¥ä¸ä»£ç å¨å ¨å±å½åç©ºé´ä¸­ï¼å°ä¼å¯¼è´å²çªï¼ å ¶ä¸­ end // åªä¼å¨åå­æ¥æ¾ï¼å³ç¼è¯ä½¿ç¨å®çä»£ç ï¼æ¶ä¸ std::end å²çªï¼è y1 // å¨å£°ææ¶å°±ä¼å²çªï¼ å¹¶ä¸ y1 çå²çªå ä¸ºä¸ç¯å¢æå ³çè³å¨ Windows // ä¸ä¸ä¼è¢«åç°ï¼å´ä¼å¨ Linux çè¯æµç¯å¢ä¸é æç¼è¯éè¯¯ï¼ } } // namespace Sol int main () { Sol :: solve (); } ```   
---|---  
  
## åè

  * [Namespaces - cppreference.com](https://en.cppreference.com/w/cpp/language/namespace)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/namespace.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/namespace.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [NachtgeistW](https://github.com/NachtgeistW), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [amlhdsan](https://github.com/amlhdsan), [billchenchina](https://github.com/billchenchina), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [ntt998244353](https://github.com/ntt998244353), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
