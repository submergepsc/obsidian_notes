# Java éæ - OI Wiki

- Source: https://oi-wiki.org/lang/java/

# Java éæ

## å ³äº Java

Java æ¯ä¸ç§å¹¿æ³ä½¿ç¨çè®¡ç®æºç¼ç¨è¯­è¨ï¼æ¥æ **è·¨å¹³å°** ã**é¢åå¯¹è±¡** ã**æ³åç¼ç¨** çç¹æ§ï¼å¹¿æ³åºç¨äºä¼ä¸çº§ Web åºç¨å¼ååç§»å¨åºç¨å¼åï¼

## ç¯å¢å®è£ 

åè§ [JDK](../../tools/compiler/#jdk)ï¼

## åºæ¬è¯­æ³

### ä¸»å½æ°

Java ç±»ä¼¼ C/C++ è¯­è¨ï¼éè¦ä¸ä¸ªå½æ°ï¼å¨é¢åå¯¹è±¡ä¸­ï¼è¿è¢«ç§°ä¸ºæ¹æ³ï¼ä½ä¸ºç¨åºæ§è¡çå ¥å£ç¹ï¼

Java çä¸»å½æ°çæ ¼å¼æ¯åºå®çï¼å½¢å¦ï¼

```text 1 2 3 4 5 ``` |  ```text class Test { public static void main ( String [] args ) { // ç¨åºçä»£ç  } } ```   
---|---  
  
ä¸ä¸ªæå ç Java ç¨åºï¼åç§°ä¸è¬æ¯ `*.jar`ï¼ä¸­å¯ä»¥æå¾å¤ä¸ªç±»ä¼¼çå½æ°ï¼ä½æ¯å½è¿è¡è¿ä¸ªç¨åºçæ¶åï¼åªæå ¶ä¸­ä¸ä¸ªå½æ°ä¼è¢«è¿è¡ï¼è¿æ¯å®ä¹å¨ `Jar` ç `Manifest` æä»¶ä¸­çï¼å¨ OI æ¯èµä¸­ä¸è¬ç¨ä¸å°å ³äºå®çç¥è¯ï¼

### æ³¨é

å C/C++ ä¸æ ·ï¼Java ä½¿ç¨ `//` å `/* */` åå«æ³¨éåè¡åå¤è¡ï¼

### åºæ¬æ°æ®ç±»å

ç±»åå| æä¹  
---|---  
boolean| å¸å°ç±»å  
byte| å­èç±»å  
char| å­ç¬¦å  
double| åç²¾åº¦æµ®ç¹  
float| åç²¾åº¦æµ®ç¹  
int| æ´å  
long| é¿æ´å  
short| ç­æ´å  
null| ç©º  
  
### å£°æåé

```text 1 2 3 4 ``` |  ```text int a = 12 ; // è®¾ç½® a ä¸ºæ´æ°ç±»å,å¹¶ç» a èµå¼ä¸º 12 String str = "Hello, OI-wiki" ; // å£°æå­ç¬¦ä¸²åé str char ch = 'W' ; double PI = 3.1415926 ; ```   
---|---  
  
### final å ³é®å­

`final` å«ä¹æ¯è¿æ¯æç»çãä¸å¯æ´æ¹çç»æï¼è¢« `final` ä¿®é¥°çåéåªè½è¢«èµå¼ä¸æ¬¡ï¼èµå¼åä¸åæ¹åï¼

```text 1 ``` |  ```text final double PI = 3.1415926 ; ```   
---|---  
  
### æ°ç»

```text 1 2 3 ``` |  ```text // æåä¸ªå ç´ çæ´æ°ç±»åæ°ç» // å ¶è¯­æ³æ ¼å¼ä¸º æ°æ®ç±»å[] åéå = new æ°æ®ç±»å[æ°ç»å¤§å°] int [] ary = new int [ 10 ] ; ```   
---|---  
  
### å­ç¬¦ä¸²

  * å­ç¬¦ä¸²æ¯ Java ä¸ä¸ªå ç½®çç±»ï¼

```text 1 2 3 4 5 6 ``` |  ```text // æä¸ºç®åçæé ä¸ä¸ªå­ç¬¦ä¸²åéçæ¹æ³å¦ä¸ String a = "Hello" ; // è¿å¯ä»¥ä½¿ç¨å­ç¬¦æ°ç»æé ä¸ä¸ªå­ç¬¦ä¸²åé char [] stringArray = { 'H' , 'e' , 'l' , 'l' , 'o' }; String s = new String ( stringArray ); ```   
---|---  
  
### å åå¯¼å ¥å 

Java ä¸­çç±»ï¼`Class`ï¼é½è¢«æ¾å¨ä¸ä¸ªä¸ªå ï¼`package`ï¼éé¢ï¼å¨ä¸ä¸ªå éé¢ä¸å è®¸æååçç±»ï¼å¨ç±»çç¬¬ä¸è¡éå¸¸è¦è¯´æè¿ä¸ªç±»æ¯å±äºåªä¸ªå çï¼ä¾å¦ï¼

```text 1 ``` |  ```text package org.oi \- wiki . tutorial ; ```   
---|---  
  
å çå½åè§èä¸è¬æ¯ï¼`é¡¹ç®ææè çé¡¶çº§å.é¡¹ç®ææè çäºçº§å.é¡¹ç®åç§°`ï¼

éè¿ `import` å ³é®å­æ¥å¯¼å ¥ä¸å¨æ¬ç±»æå±çå ä¸é¢çç±»ï¼ä¾å¦ä¸é¢è¦ç¨å°ç `Scanner`ï¼

```text 1 ``` |  ```text import java.util.Scanner ; ```   
---|---  
  
å¦ææ³è¦å¯¼å ¥æå ä¸é¢ææçç±»ï¼åªéè¦æè¿ä¸ªè¯­å¥æåçåå·åçç±»åæ¢æ `*`ï¼

### è¾å ¥

å¯ä»¥éè¿ `Scanner` ç±»æ¥å¤çå½ä»¤è¡è¾å ¥ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text package org.oiwiki.tutorial ; import java.util.Scanner ; class Test { public static void main ( String [] args ) { Scanner scan = new Scanner ( System . in ); // System.in æ¯è¾å ¥æµ int a = scan . nextInt (); double b = scan . nextDouble (); String c = scan . nextLine (); } } ```   
---|---  
  
### è¾åº

å¯ä»¥å¯¹åéè¿è¡æ ¼å¼åè¾åºï¼

ç¬¦å·| æä¹  
---|---  
`%f`| æµ®ç¹ç±»å  
`%s`| å­ç¬¦ä¸²ç±»å  
`%d`| æ´æ°ç±»å  
`%c`| å­ç¬¦ç±»å  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text class Test { public static void main ( String [] args ) { int a = 12 ; char b = 'A' ; double s = 3.14 ; String str = "Hello world" ; System . out . printf ( "%f\n" , s ); System . out . printf ( "%d\n" , a ); System . out . printf ( "%c\n" , b ); System . out . printf ( "%s\n" , str ); } } ```   
---|---  
  
### æ§å¶è¯­å¥

Java çæµç¨æ§å¶è¯­å¥ä¸ C++ æ¯åºæ¬ç¸åçï¼

#### éæ©

  * if

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* å¤æ­æ¡ä»¶ */ ){ // æ¡ä»¶æç«æ¶æ§è¡è¿éé¢çä»£ç  } } } ```   
---|---  
  
  * if...else

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* å¤æ­æ¡ä»¶ */ ) { // æ¡ä»¶æç«æ¶æ§è¡è¿éé¢çä»£ç  } else { // æ¡ä»¶ä¸æç«æ¶æ§è¡è¿éé¢çä»£ç  } } } ```   
---|---  
  
  * if...else if...else

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* å¤æ­æ¡ä»¶ */ ) { //å¤æ­æ¡ä»¶æç«æ§è¡è¿éé¢çä»£ç  } else if ( /* å¤æ­æ¡ä»¶2 */ ) { // å¤æ­æ¡ä»¶2æç«æ§è¡è¿éé¢çä»£ç  } else { // ä¸è¿°æ¡ä»¶é½ä¸æç«æ§è¡è¿éé¢çä»£ç  } } } ```   
---|---  
  
  * switch...case

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text class Test { public static void main ( String [] args ) { switch ( /* è¡¨è¾¾å¼ */ ){ case /* å¼ 1 */ : // å½è¡¨è¾¾å¼åå¾çå¼ç¬¦åå¼ 1 æ§è¡æ­¤æ®µä»£ç  break ; // å¦æä¸å ä¸ break è¯­å¥,ä¼è®©ç¨åºæé¡ºåºå¾ä¸æ§è¡ç´å° break case /* å¼ 2 */ : // å½è¡¨è¾¾å¼åå¾çå¼ç¬¦åå¼ 2 æ§è¡æ­¤æ®µä»£ç  break ; default : // å½è¡¨è¾¾å¼ä¸ç¬¦åä¸é¢åä¸¾çå¼çæ¶åæ§è¡è¿éé¢çä»£ç  } } } ```   
---|---  
  
#### å¾ªç¯

  * for

`for` å ³é®å­æä¸¤ç§ä½¿ç¨æ¹æ³ï¼å ¶ä¸­ç¬¬ä¸ç§æ¯æ®éç `for` å¾ªç¯ï¼å½¢å¼å¦ä¸ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { for ( /* åå§å */ ; /* å¾ªç¯çå¤æ­æ¡ä»¶ */ ; /* æ¯æ¬¡å¾ªç¯åæ§è¡çæ­¥éª¤ */ ) { // å½å¾ªç¯çæ¡ä»¶æç«æ§è¡å¾ªç¯ä½å ä»£ç  } } } ```   
---|---  
  
ç¬¬äºç§æ¯ç±»ä¼¼ C++ ç `foreach` ä½¿ç¨æ¹æ³ï¼ç¨äºå¾ªç¯æ°ç»æè éåä¸­çæ°æ®ï¼ç¸å½äºæä¸ä¸ç§æ¹å¼ä¸­çå¾ªç¯åééèèµ·æ¥äºï¼å½¢å¼å¦ä¸ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { for ( /* å ç´ ç±»åX */ /* å ç´ åY */ : /* éåZ */ ) { // è¿ä¸ªè¯­å¥åçæ¯ä¸æ¬¡å¾ªç¯æ¶ï¼å ç´ Yåå«æ¯éåZä¸­çä¸ä¸ªå ç´ ï¼ } } } ```   
---|---  
  
  * while

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { while ( /* å¤å®æ¡ä»¶ */ ) { // æ¡ä»¶æç«æ¶æ§è¡å¾ªç¯ä½å ä»£ç  } } } ```   
---|---  
  
  * do...while

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { do { // éè¦æ§è¡çä»£ç  } while ( /* å¾ªç¯å¤æ­æ¡ä»¶ */ ); } } ```   
---|---  
  
## æ³¨æäºé¡¹

### ç±»åä¸æä»¶åä¸è´

åå»º Java æºç¨åºéè¦ç±»ååæä»¶åä¸è´æè½ç¼è¯éè¿ï¼å¦åç¼è¯å¨ä¼æç¤ºæ¾ä¸å°ç±»ï¼éå¸¸è¯¥æä»¶åä¼å¨å ·ä½ OJ ä¸­æå®ï¼

ä¾ï¼

`Add.java`

```text 1 2 3 4 5 ``` |  ```text class Add { public static void main ( String [] args ) { // ... } } ```   
---|---  
  
å¨è¯¥æä»¶ä¸­éä½¿ç¨ `Add` ä¸ºç±»åæ¹å¯ç¼è¯éè¿ï¼

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/java.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/java.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[jingyuexing](mailto:1941755817@qq.com), [ksyx](https://github.com/ksyx), [qyl27](https://github.com/qyl27), [Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [mgt](mailto:i@margatroid.xyz), [NachtgeistW](https://github.com/NachtgeistW), [billchenchina](https://github.com/billchenchina), [diauweb](https://github.com/diauweb), [Konano](https://github.com/Konano), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [Qubik65536](https://github.com/Qubik65536), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [weiyong1024](https://github.com/weiyong1024), [1804040636](https://github.com/1804040636), [clansty](https://github.com/clansty), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [gtn1024](https://github.com/gtn1024), [Henry-ZHR](https://github.com/Henry-ZHR), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [orzAtalod](https://github.com/orzAtalod), [Peanut-Tang](https://github.com/Peanut-Tang), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [Xeonacid](https://github.com/Xeonacid), [yusancky](https://github.com/yusancky), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
