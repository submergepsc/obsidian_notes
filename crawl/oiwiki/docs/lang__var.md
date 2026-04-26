# åé - OI Wiki

- Source: https://oi-wiki.org/lang/var/

# åé

## æ°æ®ç±»å

C++ çç±»åç³»ç»ç±å¦ä¸å é¨åç»æï¼

  1. åºç¡ç±»åï¼æ¬å·å ä¸ºä»£è¡¨å ³é®è¯/ä»£è¡¨ç±»åï¼
     1. æ ç±»å/`void` å (`void`)
     2. ï¼C++11 èµ·ï¼ç©ºæéç±»å (`std::nullptr_t`)
     3. ç®æ¯ç±»å
        1. æ´æ°ç±»å (`int`)
        2. å¸å°ç±»å/`bool` å (`bool`)
        3. å­ç¬¦ç±»å (`char`)
        4. æµ®ç¹ç±»å (`float`,`double`)
  2. å¤åç±»å4

### å¸å°ç±»å

ä¸ä¸ª `bool` ç±»åçåéåå¼åªå¯è½ä¸ºä¸¤ç§ï¼`true` å `false`ï¼

ä¸è¬æ åµä¸ï¼ä¸ä¸ª `bool` ç±»ååéå æ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­èï¼ä¸è¬æ åµä¸ï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­è =88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼çç©ºé´ï¼

Tip

å¯éè¿å¤´æä»¶ `<climits>`(C++)/`<limits.h>`(C) ä¸­çå®å¸¸é `CHAR_BIT` è·åå­èçä½æ°ï¼

C è¯­è¨çå¸å°ç±»å

å¦è¯·åé [C++ ä¸å ¶ä»å¸¸ç¨è¯­è¨çåºå« - bool](../cpp-other-langs/#bool)ï¼

C è¯­è¨æåæ¯æ²¡æå¸å°ç±»åçï¼ç´å° C99 æ¶æå¼å ¥ `_Bool` å ³é®è¯ä½ä¸ºå¸å°ç±»åï¼å ¶è¢«è§ä½æ ç¬¦å·æ´æ°ç±»åï¼

Note

C è¯­è¨ç `bool` ç±»åä» C23 èµ·ä¸åä½¿ç¨æ´åçé¶ä¸éé¶å¼å®ä¹ï¼èæ¯å®ä¹ä¸ºè¶³å¤å¨å­ `true` å `false` ä¸¤ä¸ªå¸¸éçç±»åï¼

ä¸ºæ¹ä¾¿ä½¿ç¨ï¼`stdbool.h` ä¸­æä¾äº `bool`,`true`,`false` ä¸ä¸ªå®ï¼å®ä¹å¦ä¸ï¼

```text 1 2 3 ``` |  ```text #define bool _Bool #define true 1 #define false 0 ```   
---|---  
  
è¿äºå®äº C23 ä¸­ç§»é¤ï¼å¹¶ä¸ C23 èµ·å¼å ¥ `true`,`false` å `bool` ä½ä¸ºå ³é®å­ï¼åæ¶ä¿ç `_Bool` ä½ä¸ºæ¿ä»£æ¼åå½¢å¼5ï¼

å¦å¤ï¼C23 èµ·è¿å¯ä»¥éè¿ `<limits.h>` ä¸­çå®å¸¸é `BOOL_WIDTH` è·åå¸å°ç±»åçä½å®½ï¼

### æ´æ°ç±»å

ç¨äºå­å¨æ´æ°ï¼æåºç¡çæ´æ°ç±»åæ¯ `int`.

æ³¨æ

ç±äºåå²åå ï¼C++ ä¸­å¸å°ç±»ååå­ç¬¦ç±»åä¼è¢«è§ä½ç¹æ®çæ´åï¼

å¨å ä¹ææçæ åµä¸é½ **ä¸åºè¯¥** å°é¤ `signed char` å `unsigned char` ä¹å¤çå­ç¬¦ç±»åä½ä¸ºæ´åä½¿ç¨ï¼

æ´æ°ç±»åä¸è¬æä½å®½æ 5 ä¸ªæ¢¯åº¦ï¼`char`,`short`,`int`,`long`,`long long`.

C++ æ åä¿è¯ `1 == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`

ç±äºåå²åå ï¼æ´æ°ç±»åçä½å®½æå¤ç§æµè¡æ¨¡åï¼ä¸ºè§£å³è¿ä¸é®é¢ï¼C99/C++11 å¼å ¥äº å®å®½æ´æ°ç±»åï¼

`int` ç±»åçå¤§å°

å¨ C++ æ åä¸­ï¼è§å® `int` çä½æ° **è³å°** ä¸º 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼

äºå®ä¸å¨ç°å¨çç»å¤§å¤æ°å¹³å°ï¼`int` çä½æ°åä¸º 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼

å¯¹äº `int` å ³é®å­ï¼å¯ä»¥ä½¿ç¨å¦ä¸ä¿®é¥°å ³é®å­è¿è¡ä¿®é¥°ï¼

ç¬¦å·æ§ï¼

  * `signed`ï¼è¡¨ç¤ºå¸¦ç¬¦å·æ´æ°ï¼é»è®¤ï¼ï¼
  * `unsigned`ï¼è¡¨ç¤ºæ ç¬¦å·æ´æ°ï¼

å¤§å°ï¼

  * `short`ï¼è¡¨ç¤º **è³å°** 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ï¼
  * `long`ï¼è¡¨ç¤º **è³å°** 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ï¼
  * ï¼C++11 èµ·ï¼`long long`ï¼è¡¨ç¤º **è³å°** 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ï¼

ä¸è¡¨ç»åºå¨ **ä¸è¬æ åµä¸** ï¼åæ´æ°ç±»åçä½å®½åè¡¨ç¤ºèå´å¤§å°ï¼å°æ°å¹³å°ä¸ä¸äºç±»åçè¡¨ç¤ºèå´å¯è½ä¸ä¸è¡¨ä¸åï¼ï¼

ç±»åå| ç­ä»·ç±»å| ä½å®½ï¼C++ æ åï¼| ä½å®½ï¼å¸¸è§ï¼| ä½å®½ï¼è¾ç½è§ï¼  
---|---|---|---|---  
`signed char`| `signed char`| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -| -  
`unsigned char`| `unsigned char`| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -| -  
`short`,`short int`,`signed short`,`signed short int`| `short int`| â¥16â¥16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -  
`unsigned short`,`unsigned short int`| `unsigned short int`| â¥16â¥16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -  
`int`,`signed`,`signed int`| `int`| â¥16â¥16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸¸è§äº Win16 APIï¼  
`unsigned`,`unsigned int`| `unsigned int`| â¥16â¥16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸¸è§äº Win16 APIï¼  
`long`,`long int`,`signed long`,`signed long int`| `long int`| â¥32â¥32![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸¸è§äº 64 ä½ LinuxãmacOSï¼  
`unsigned long`,`unsigned long int`| `unsigned long int`| â¥32â¥32![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸¸è§äº 64 ä½ LinuxãmacOSï¼  
`long long`,`long long int`,`signed long long`,`signed long long int`| `long long int`| â¥64â¥64![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -  
`unsigned long long`,`unsigned long long int`| `unsigned long long int`| â¥64â¥64![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| -  
  
å½ä½å®½ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æç¬¦å·ç±»åçè¡¨ç¤ºèå´ä¸º â2ð¥â1 â¼2ð¥â1 â1â2xâ1â¼2xâ1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1, æ ç¬¦å·ç±»åçè¡¨ç¤ºèå´ä¸º 0 â¼2ð¥ â10â¼2xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å ·ä½èè¨ï¼æä¸è¡¨ï¼

ä½å®½| è¡¨ç¤ºèå´  
---|---  
88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æç¬¦å·ï¼â27 â¼27 â1â27â¼27â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), æ ç¬¦å·ï¼0 â¼28 â10â¼28â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æç¬¦å·ï¼â215 â¼215 â1â215â¼215â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), æ ç¬¦å·ï¼0 â¼216 â10â¼216â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æç¬¦å·ï¼â231 â¼231 â1â231â¼231â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), æ ç¬¦å·ï¼0 â¼232 â10â¼232â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æç¬¦å·ï¼â263 â¼263 â1â263â¼263â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), æ ç¬¦å·ï¼0 â¼264 â10â¼264â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
ç­ä»·çç±»åè¡¨è¿°

å¨ä¸å¼åæ­§ä¹çæ åµä¸ï¼å è®¸çç¥é¨åä¿®é¥°å ³é®å­ï¼æè°æ´ä¿®é¥°å ³é®å­çé¡ºåºï¼è¿æå³çåä¸ç±»åä¼å­å¨å¤ç§ç­ä»·è¡¨è¿°ï¼

ä¾å¦ `int`ï¼`signed`ï¼`int signed`ï¼`signed int` è¡¨ç¤ºåä¸ç±»åï¼è `unsigned long` å `unsigned long int` è¡¨ç¤ºåä¸ç±»åï¼

å¦å¤ï¼ä¸äºç¼è¯å¨å®ç°äºæ©å±æ´æ°ç±»åï¼å¦ GCC å®ç°äº 128 ä½æ´æ°ï¼æç¬¦å·çç `__int128_t` åæ ç¬¦å·çç `__uint128_t`ï¼å¦ææ¨å¨æ¯èµæ¶æ³ä½¿ç¨è¿äºç±»åï¼**è¯·ä»ç»é è¯»æ¯èµè§å** ä»¥ç¡®å®æ¯å¦å è®¸ææ¯æä½¿ç¨æ©å±æ´æ°ç±»åï¼

æ³¨æ

STL ä¸ä¸å®å¯¹æ©å±æ´æ°ç±»åæè¶³å¤çæ¯æï¼æ ä½¿ç¨æ©å±æ´æ°ç±»åæ¶éæ ¼å¤å°å¿ï¼

ç¤ºä¾ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text #include <cmath> #include <iostream> int f1 ( int n ) { return abs ( n ); // Good } int f2 ( int n ) { return std :: abs ( n ); // Good } __int128_t f3 ( __int128_t n ) { return abs ( n ); // Bad } // Wrong // __int128_t f4(__int128_t n) { // return std::abs(n); // } int main () { std :: cout << "f1: " << f1 ( -42 ) << std :: endl ; std :: cout << "f2: " << f2 ( -42 ) << std :: endl ; // std::cout << "f3: " << f3(-42) << std::endl; // Wrong // std::cout << "f4: " << f4(-42) << std::endl; // Wrong return 0 ; } ```   
---|---  
  
ä»¥ä¸ç¤ºä¾ä»£ç å­å¨å¦ä¸é®é¢ï¼

  1. `__int128_t f3(__int128_t)` ä¸­ä½¿ç¨çæ¯ C é£æ ¼çç»å¯¹å¼å½æ°ï¼å ¶ç­¾åä¸º `int abs(int)`ï¼æ `n` é¦å ä¼å¼ºå¶è½¬æ¢ä¸º `int`ï¼ç¶åæä¼è°ç¨ `abs` å½æ°ï¼
  2. `__int128_t f4(__int128_t)` ä¸­ä½¿ç¨çæ¯ C++ é£æ ¼çç»å¯¹å¼å½æ°ï¼å ¶å¹¶æ²¡æç­¾åä¸º `__int128_t std::abs(__int128_t)` çå½æ°éè½½ï¼æä»¥æ æ³éè¿ç¼è¯ï¼
  3. C++ çæµå¼è¾åºä¸æ¯æ `__int128_t` ä¸ `__uint128_t`ï¼

ä»¥ä¸æ¯ä¸ç§è§£å³æ¹æ¡ï¼

ä¿®æ­£åçä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text #include <cmath> #include <iostream> __int128_t abs ( __int128_t n ) { return n < 0 ? \- n : n ; } std :: ostream & operator << ( std :: ostream & os , __uint128_t n ) { if ( n > 9 ) os << n / 10 ; os << ( int )( n % 10 ); return os ; } std :: ostream & operator << ( std :: ostream & os , __int128_t n ) { if ( n < 0 ) { os << '-' ; n = \- n ; } return os << ( __uint128_t ) n ; } int f1 ( int n ) { return abs ( n ); } int f2 ( int n ) { return std :: abs ( n ); } __int128_t f3 ( __int128_t n ) { return abs ( n ); } int main () { std :: cout << "f1: " << f1 ( -42 ) << std :: endl ; std :: cout << "f2: " << f2 ( -42 ) << std :: endl ; std :: cout << "f3: " << f3 ( -42 ) << std :: endl ; } ```   
---|---  
  
### å­ç¬¦ç±»å

åä¸ºãçªå­ç¬¦ç±»åãåãå®½å­ç¬¦ç±»åãï¼ç±äºç®æ³ç«èµå ä¹ä¸ä¼ç¨å°å®½å­ç¬¦ç±»åï¼æ æ­¤å¤ä» ä»ç»çªå­ç¬¦ç±»åï¼

çªå­ç¬¦åä½æ°ä¸è¬ä¸º 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼å®é ä¸åºå±å­å¨æ¹å¼ä»ç¶æ¯æ´æ°ï¼ä¸è¬éè¿ [ASCII ç¼ç ](http://www.asciitable.com/) å®ç°å­ç¬¦ä¸æ´æ°çä¸ä¸å¯¹åºï¼æå¦ä¸ä¸ç§ï¼

  * `signed char`ï¼æç¬¦å·å­ç¬¦è¡¨ç¤ºçç±»åï¼è¡¨ç¤ºèå´å¨ â128 â¼127â128â¼127![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼
  * `unsigned char`ï¼æ ç¬¦å·å­ç¬¦è¡¨ç¤ºçç±»åï¼è¡¨ç¤ºèå´å¨ 0 â¼2550â¼255![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼
  * `char` æ¥æä¸ `signed char` æ `unsigned char` ä¹ä¸ç¸åçè¡¨ç¤ºåå¯¹é½ï¼ä½å§ç»æ¯ç¬ç«çç±»åï¼

`char` çç¬¦å·æ§åå³äºç¼è¯å¨åç®æ å¹³å°ï¼ARM å PowerPC çé»è®¤è®¾ç½®éå¸¸æ²¡æç¬¦å·ï¼è x86 ä¸ x64 çé»è®¤è®¾ç½®éå¸¸æç¬¦å·ï¼

GCC å¯ä»¥å¨ç¼è¯åæ°ä¸­æ·»å `-fsigned-char` æ `-funsigned-char` æå®å° `char` è§ä½ `signed char` æ `unsigned char`ï¼å ¶ä»ç¼è¯å¨è¯·åç §ææ¡£ï¼éè¦æ³¨ææå®ä¸æ¶æé»è®¤å¼ä¸åçç¬¦å·æå¯è½ä¼ç ´å ABIï¼é æç¨åºæ æ³æ­£å¸¸å·¥ä½ï¼

æ³¨æ

ä¸å ¶ä»æ´åä¸åï¼`char`ã`signed char`ã`unsigned char` æ¯ **ä¸ç§ä¸åçç±»å** ï¼

ä¸è¬æ¥è¯´ `signed char`,`unsigned char` ä¸åºç¨æ¥å­å¨å­ç¬¦ï¼ç»å¤§å¤æ°æ åµä¸ï¼è¿ä¸¤ç§ç±»ååè¢«è§ä½æ´æ°ç±»åï¼

### æµ®ç¹ç±»å

ç¨äºå­å¨ãå®æ°ãï¼æ³¨æå¹¶ä¸æ¯ä¸¥æ ¼æä¹ä¸çå®æ°ï¼èæ¯å®æ°å¨ä¸å®è§åä¸çè¿ä¼¼ï¼ï¼å æ¬ä»¥ä¸ä¸ç§ï¼

  * `float`ï¼åç²¾åº¦æµ®ç¹ç±»åï¼å¦ææ¯æå°±ä¼å¹é  IEEE-754 binary32 æ ¼å¼ï¼
  * `double`ï¼åç²¾åº¦æµ®ç¹ç±»åï¼å¦ææ¯æå°±ä¼å¹é  IEEE-754 binary64 æ ¼å¼ï¼
  * `long double`ï¼æ©å±ç²¾åº¦æµ®ç¹ç±»åï¼å¦ææ¯æå°±ä¼å¹é  IEEE-754 binary128 æ ¼å¼ï¼å¦åå¦ææ¯æå°±ä¼å¹é  IEEE-754 binary64 æ©å±æ ¼å¼ï¼å¦åå¹é æç§ç²¾åº¦ä¼äº binary64 èå¼åè³å°å binary64 ä¸æ ·å¥½çé IEEE-754 æ©å±æµ®ç¹æ ¼å¼ï¼å¦åå¹é  IEEE-754 binary64 æ ¼å¼ï¼

æµ®ç¹æ ¼å¼| ä½å®½| æå¤§æ­£æ°| ç²¾åº¦ä½æ°  
---|---|---|---  
IEEE-754 binary32 æ ¼å¼| 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 3.4 Ã10383.4Ã1038![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 6 â¼96â¼9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
IEEE-754 binary64 æ ¼å¼| 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1.8 Ã103081.8Ã10308![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 15 â¼1715â¼17![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
IEEE-754 binary64 æ©å±æ ¼å¼| â¥80â¥80![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â¥1.2 Ã104932â¥1.2Ã104932![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â¥18 â¼21â¥18â¼21![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
IEEE-754 binary128 æ ¼å¼| 128128![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1.2 Ã1049321.2Ã104932![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33 â¼3633â¼36![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
> IEEE-754 æµ®ç¹æ ¼å¼çæå°è´æ°æ¯æå¤§æ­£æ°çç¸åæ°ï¼

å ä¸º `float` ç±»åè¡¨ç¤ºèå´è¾å°ï¼ä¸ç²¾åº¦ä¸é«ï¼å®é åºç¨ä¸­å¸¸ä½¿ç¨ `double` ç±»åè¡¨ç¤ºæµ®ç¹æ°ï¼

å¦å¤ï¼æµ®ç¹ç±»åå¯ä»¥æ¯æä¸äºç¹æ®å¼ï¼

  * æ ç©·ï¼æ­£æè´ï¼ï¼`INFINITY`.
  * è´é¶ï¼`-0.0`ï¼ä¾å¦ `1.0 / 0.0 == INFINITY`,`1.0 / -0.0 == -INFINITY`.
  * éæ°ï¼NaNï¼ï¼`std::nan`,`NAN`ï¼ä¸è¬å¯ä»¥ç± `0.0 / 0.0` ä¹ç±»çè¿ç®äº§çï¼å®ä¸ä»»ä½å¼ï¼å æ¬èªèº«ï¼æ¯è¾é½ä¸ç¸ç­ï¼C++11 åå¯ä»¥ ä½¿ç¨ `std::isnan` å¤æ­ä¸ä¸ªæµ®ç¹æ°æ¯ä¸æ¯ NaN.

### æ ç±»å

`void` ç±»åä¸ºæ ç±»åï¼ä¸ä¸é¢å ç§ç±»åä¸åçæ¯ï¼ä¸è½å°ä¸ä¸ªåéå£°æä¸º `void` ç±»åï¼ä½æ¯å½æ°çè¿åå¼å è®¸ä¸º `void` ç±»åï¼è¡¨ç¤ºè¯¥å½æ°æ è¿åå¼ï¼

### ç©ºæéç±»å

è¯·åé æéç [å¯¹åºç« è](../pointer/#ç©ºæé)

## å®å®½æ´æ°ç±»å

C++11 èµ·æä¾äºå®å®½æ´æ°çæ¯æï¼å ·ä½å¦ä¸ï¼

  * `<cstdint>`ï¼æä¾äºè¥å¹²å®å®½æ´æ°çç±»åååå®å®½æ´æ°ç±»åæå¤§å¼ãæå°å¼ç­çå®å¸¸éï¼
  * `<cinttypes>`ï¼ä¸ºå®å®½æ´æ°ç±»åæä¾äºç¨äº `std::fprintf` ç³»åå½æ°å `std::fscanf` ç³»åå½æ°çæ ¼å¼å®å¸¸éï¼

å®å®½æ´æ°æå¦ä¸å ç§ï¼

  * `intN_t`: å®½åº¦ **æ°ä¸º** ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çæç¬¦å·æ´æ°ç±»åï¼å¦ `int32_t`.
  * `int_fastN_t`: å®½åº¦ **è³å°** æ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç **æå¿«ç** æç¬¦å·æ´æ°ç±»åï¼å¦ `int_fast32_t`.
  * `int_leastN_t`: å®½åº¦ **è³å°** æ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç **æå°ç** æç¬¦å·æ´æ°ç±»åï¼å¦ `int_least32_t`.

æ ç¬¦å·çæ¬åªéå¨æç¬¦å·çæ¬åå ä¸ä¸ªå­æ¯ u å³å¯ï¼å¦ `uint32_t`,`uint_least8_t`.

æ åè§å®å¿ é¡»å®ç°å¦ä¸ 16 ç§ç±»åï¼

`int_fast8_t`,`int_fast16_t`,`int_fast32_t`,`int_fast64_t`,

`int_least8_t`,`int_least16_t`,`int_least32_t`,`int_least64_t`,

`uint_fast8_t`,`uint_fast16_t`,`uint_fast32_t`,`uint_fast64_t`,

`uint_least8_t`,`uint_least16_t`,`uint_least32_t`,`uint_least64_t`.

ç»å¤§å¤æ°ç¼è¯å¨å¨æ­¤åºç¡ä¸é½å®ç°äºå¦ä¸ 8 ç§ç±»åï¼

`int8_t`,`int16_t`,`int32_t`,`int64_t`,

`uint8_t`,`uint16_t`,`uint32_t`,`uint64_t`.

å¨å®ç°äºå¯¹åºç±»åçæ åµä¸ï¼C++ æ åè§å®å¿ é¡»å®ç°è¡¨ç¤ºå¯¹åºç±»åçæå¤§å¼ãæå°å¼ãä½å®½çå®å¸¸éï¼æ ¼å¼ä¸ºå°ç±»ååæ«å°¾ç `_t` å»æåè½¬å¤§åå¹¶æ·»å åç¼ï¼

  * `_MAX` è¡¨ç¤ºæå¤§å¼ï¼å¦ `INT32_MAX` å³ä¸º `int32_t` çæå¤§å¼ï¼
  * `_MIN` è¡¨ç¤ºæå°å¼ï¼å¦ `INT32_MIN` å³ä¸º `int32_t` çæå°å¼ï¼

æ³¨æ

å®å®½æ´æ°ç±»åæ¬è´¨ä¸æ¯æ®éæ´æ°ç±»åçç±»åå«åï¼æä»¥æ··ç¨å®å®½æ´æ°ç±»ååæ®éæ´æ°ç±»åå¯è½ä¼å½±åè·¨å¹³å°ç¼è¯ï¼ä¾å¦ï¼

ç¤ºä¾ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text #include <algorithm> #include <cstdint> #include <iostream> int main () { long long a ; int64_t b ; std :: cin >> a >> b ; std :: cout << std :: max ( a , b ) << std :: endl ; return 0 ; } ```   
---|---  
  
`int64_t` å¨ 64 ä½ Windows ä¸ä¸è¬ä¸º `long long int`, èå¨ 64 ä½ Linux ä¸ä¸è¬ä¸º `long int`, æä»¥è¿æ®µä»£ç å¨ä½¿ç¨ 64 ä½ Linux ä¸ç GCC æ¶ä¸è½éè¿ç¼è¯ï¼èä½¿ç¨ 64 ä½ Windows ä¸ç MSVC æ¶å¯ä»¥éè¿ç¼è¯ï¼å ä¸º `std::max` è¦æ±è¾å ¥çä¸¤ä¸ªåæ°ç±»åå¿ é¡»ç¸åï¼

æ­¤å¤ï¼C++17 èµ·å¨ `<limits>` ä¸­æä¾äº `std::numeric_limits` ç±»æ¨¡æ¿ï¼ç¨äºæ¥è¯¢åç§ç®æ°ç±»åçå±æ§ï¼å¦æå¤§å¼ãæå°å¼ãæ¯å¦æ¯æ´å½¢ãæ¯å¦æç¬¦å·ç­ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text #include <cstdint> #include <limits> std :: numeric_limits < int32_t >:: max (); // int32_t çæå¤§å¼, 2'147'483'647 std :: numeric_limits < int32_t >:: min (); // int32_t çæå°å¼, -2'147'483'648 std :: numeric_limits < double >:: min (); // double çæå°å¼, çº¦ä¸º 2.22507e-308 std :: numeric_limits < double >:: epsilon (); // 1.0 ä¸ double çä¸ä¸ªå¯è¡¨ç¤ºå¼çå·®, // çº¦ä¸º 2.22045e-16 ```   
---|---  
  
## ç±»åè½¬æ¢

å¨ä¸äºæ¶åï¼æ¯å¦æä¸ªå½æ°æ¥å `int` ç±»åçåæ°ï¼ä½ä¼ å ¥äº `double` ç±»åçåéï¼ï¼æä»¬éè¦å°æç§ç±»åï¼è½¬æ¢æå¦å¤ä¸ç§ç±»åï¼

C++ ä¸­ç±»åçè½¬æ¢æºå¶è¾ä¸ºå¤æï¼è¿éä¸»è¦ä»ç»å¯¹äºåºç¡æ°æ®ç±»åçä¸¤ç§è½¬æ¢ï¼æ°å¼æååæ°å¼è½¬æ¢ï¼

### æ°å¼æå

æ°å¼æåè¿ç¨ä¸­ï¼å¼æ¬èº«ä¿æä¸åï¼

Note

C é£æ ¼çå¯ååæ°åå¨ä¼ å¼è¿ç¨ä¸­ä¼è¿è¡é»è®¤åæ°æåï¼å¦ï¼

ç¤ºä¾ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <stdarg.h> #include <stdio.h> void test ( int tot , ...) { va_list valist ; int i ; // åå§åå¯ååæ°åè¡¨ va_start ( valist , tot ); for ( i = 0 ; i < tot ; ++ i ) { // è·åç¬¬ i ä¸ªåéçå¼ double xx = va_arg ( valist , double ); // Correct // float xx = va_arg(valist, float); // Wrong // è¾åºç¬¬ i ä¸ªåéçåºå±å­å¨å å®¹ printf ( "i = %d, value = 0x%016llx \n " , i , * ( long long * )( & xx )); } // æ¸ çå¯ååæ°åè¡¨çå å­ va_end ( valist ); } int main () { float f ; double fd , d ; f = 123\. ; // 0x42f60000 fd = 123\. ; // 0x405ec00000000000 d = 456\. ; // 0x407c800000000000 test ( 3 , f , fd , d ); } ```   
---|---  
  
å¨è°ç¨ `test` æ¶ï¼`f` æåä¸º `double`ï¼ä»èåºå±å­å¨å å®¹å `fd` ç¸åï¼è¾åºä¸º

```text 1 2 3 ``` |  ```text i = 0, value = 0x405ec00000000000 i = 1, value = 0x405ec00000000000 i = 2, value = 0x407c800000000000 ```   
---|---  
  
è¥å° `double xx = va_arg(valist, double);` æ¹ä¸º `float xx = va_arg(valist, float);`ï¼GCC åºè¯¥ç»åºä¸æ¡ç±»ä¼¼ä¸æçè­¦åï¼

```text 1 2 3 4 5 6 7 ``` |  ```text In file included from test.c:2: test.c: In function 'test': test.c:14:35: warning: 'float' is promoted to 'double' when passed through '...' 14 | float xx = va_arg(valist, float); | ^ test.c:14:35: note: (so you should pass 'double' not 'float' to 'va_arg') test.c:14:35: note: if this code is reached, the program will abort ```   
---|---  
  
æ­¤æ¶çç¨åºå°ä¼å¨è¾åºåç»æ­¢ï¼

è¿ä¸ç¹ä¹è½è§£éä¸ºä»ä¹ `printf` ç `%f` æ¢è½å¹é  `float` ä¹è½å¹é  `double`ï¼

#### æ´æ°æå

å°æ´æ°ç±»åï¼å¦ `char`ï¼ççº¯å³å¼å¯è½¬æ¢æè¾å¤§æ´æ°ç±»åï¼å¦ `int`ï¼ççº¯å³å¼ï¼

å ·ä½èè¨ï¼ç®æ¯è¿ç®ç¬¦ä¸æ¥åå°äº `int` çç±»åä½ä¸ºå®çå®åï¼èå¨å·¦å¼å°å³å¼è½¬æ¢åï¼å¦æéç¨å°±ä¼èªå¨å®æ½æ´æ°æåï¼

å ·ä½å°ï¼æå¦ä¸è§åï¼

  * æºç±»åä¸º `signed char`ã`signed short / short` æ¶ï¼å¯æåä¸º `int`ï¼
  * æºç±»åä¸º `unsigned char`ã`unsigned short` æ¶ï¼è¥ `int` è½ä¿ææºç±»åçå¼èå´ï¼åå¯æåä¸º `int`ï¼å¦åå¯æåä¸º `unsigned int`ï¼ï¼`C++20` èµ· `char8_t` ä¹éç¨æ¬è§åï¼
  * `char` çæåè§ååå³äºå ¶åºå±ç±»åæ¯ `signed char` è¿æ¯ `unsigned char`ï¼
  * `bool` ç±»åå¯è½¬æ¢å° `int`ï¼`false` åä¸º `0`ï¼`true` åä¸º `1`ï¼
  * è¥ç®æ ç±»åçå¼èå´å å«æºç±»åï¼ä¸æºç±»åçå¼èå´ä¸è½è¢« `int` å `unsigned int` å å«ï¼åæºç±»åå¯æåä¸ºç®æ ç±»åï¼6

æ³¨æ

`char`->`short` ä¸æ¯æ°å¼æåï¼å ä¸º `char` è¦ä¼å æåä¸º `int / unsigned int`ï¼ä¹åæ¯ `int / unsigned int`->`short`ï¼ä¸æ»¡è¶³æ°å¼æåçæ¡ä»¶ï¼

å¦ï¼ä»¥ä¸åå® `int` ä¸º 32 ä½ï¼`unsigned short` ä¸º 16 ä½ï¼`signed char` å `unsigned char` ä¸º 8 ä½ï¼`bool` ä¸º 1 ä½ï¼

  * `(signed char)'\0' - (signed char)'\xff'` ä¼å å° `(signed char)'\0'` æåä¸º `(int)0`ãå° `(signed char)'\xff'` æåä¸º `(int)-1`, åè¿è¡ `int` é´çè¿ç®ï¼æç»ç»æä¸º `(int)1`ï¼
  * `(unsigned char)'\0' - (unsigned char)'\xff'` ä¼å å° `(unsigned char)'\0'` æåä¸º `(int)0`ãå° `(unsigned char)'\xff'` æåä¸º `(int)255`, åè¿è¡ `int` é´çè¿ç®ï¼æç»ç»æä¸º `(int)-255`ï¼
  * `false - (unsigned short)12` ä¼å å° `false` æåä¸º `(int)0`ãå° `(unsigned short)12` æåä¸º `(int)12`, åè¿è¡ `int` é´çè¿ç®ï¼æç»ç»æä¸º `(int)-12`ï¼

#### æµ®ç¹æå

ä½å®½è¾å°çæµ®ç¹æ°å¯ä»¥æåä¸ºä½å®½è¾å¤§çæµ®ç¹æ°ï¼ä¾å¦ `float` ç±»åçåéå `double` ç±»åçåéè¿è¡ç®æ¯è¿ç®æ¶ï¼ä¼å° `float` ç±»ååéæåä¸º `double` ç±»ååéï¼ï¼å ¶å¼ä¸åï¼

### æ°å¼è½¬æ¢

æ°å¼è½¬æ¢è¿ç¨ä¸­ï¼å¼å¯è½ä¼åçæ¹åï¼

æ³¨æ

æ°å¼æåä¼å äºæ°å¼è½¬æ¢ï¼å¦ `bool`->`int` æ¶æ¯æ°å¼æåèéæ°å¼è½¬æ¢ï¼

#### æ´æ°è½¬æ¢

  * å¦æç®æ ç±»åä¸ºä½å®½ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ ç¬¦å·æ´æ°ç±»åï¼åè½¬æ¢ç»ææ¯åå¼ mod2ð¥mod2x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçç»æï¼

    * è¥ç®æ ç±»åä½å®½å¤§äºæºç±»åä½å®½ï¼

      * è¥æºç±»åä¸ºæç¬¦å·ç±»åï¼ä¸è¬æ åµä¸éå è¿è¡ç¬¦å·ä½æ©å±åè½¬æ¢ï¼

å¦

        * å° `(short)-1`ï¼`(short)0b1111'1111'1111'1111`ï¼è½¬æ¢ä¸º `unsigned int` ç±»åæ¶ï¼å è¿è¡ç¬¦å·ä½æ©å±ï¼å¾å° `0b1111'1111'1111'1111'1111'1111'1111'1111`ï¼åè¿è¡æ´æ°è½¬æ¢ï¼ç»æä¸º `(unsigned int)4'294'967'295`ï¼`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`ï¼ï¼
        * å° `(short)32'767`ï¼`(short)0b0111'1111'1111'1111`ï¼è½¬æ¢ä¸º `unsigned int` ç±»åæ¶ï¼å è¿è¡ç¬¦å·ä½æ©å±ï¼å¾å° `0b0000'0000'0000'0000'0111'1111'1111'1111`ï¼åè¿è¡æ´æ°è½¬æ¢ï¼ç»æä¸º `(unsigned int)32'767`ï¼`(unsigned int)0b0000'0000'0000'0000'0111'1111'1111'1111`ï¼ï¼
      * è¥æºç±»åä¸ºæ ç¬¦å·ç±»åï¼åéå è¿è¡é¶æ©å±åè½¬æ¢ï¼

å¦å° `(unsigned short)65'535`ï¼`(unsigned short)0b1111'1111'1111'1111`ï¼è½¬æ¢ä¸º `unsigned int` ç±»åæ¶ï¼å è¿è¡é¶æ©å±ï¼å¾å° `0b0000'0000'0000'0000'1111'1111'1111'1111`ï¼åè¿è¡æ´æ°è½¬æ¢ï¼ç»æä¸º `(unsigned int)65'535`ï¼`(unsigned int)0b0000'0000'0000'0000'1111'1111'1111'1111`ï¼ï¼

    * è¥ç®æ ç±»åä½å®½ä¸å¤§äºæºç±»åä½å®½ï¼åéå æªæ­åè½¬æ¢ï¼

å¦å° `(unsigned int)4'294'967'295`ï¼`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`ï¼è½¬æ¢ä¸º `unsigned short` ç±»åæ¶ï¼å è¿è¡æªæ­ï¼å¾å° `0b1111'1111'1111'1111`ï¼åè¿è¡æ´æ°è½¬æ¢ï¼ç»æä¸º `(unsigned short)65'535`ï¼`(unsigned short)0b1111'1111'1111'1111`ï¼ï¼

  * å¦æç®æ ç±»åä¸ºä½å®½ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¸¦ç¬¦å·æ´æ°ç±»åï¼å **ä¸è¬æ åµä¸** ï¼è½¬æ¢ç»æå¯ä»¥è®¤ä¸ºæ¯åå¼ mod2ð¥mod2x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçç»æï¼7

ä¾å¦å° `(unsigned int)4'294'967'295`ï¼`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`ï¼è½¬æ¢ä¸º `short` ç±»åæ¶ï¼ç»æä¸º `(short)-1`ï¼`(short)0b1111'1111'1111'1111`ï¼ï¼

  * å¦æç®æ ç±»åæ¯ `bool`ï¼åæ¯ å¸å°è½¬æ¢ï¼

  * å¦ææºç±»åæ¯ `bool`ï¼å `false` è½¬ä¸ºå¯¹åºç±»åç 0ï¼`true` è½¬ä¸ºå¯¹åºç±»åç 1ï¼

#### æµ®ç¹è½¬æ¢

ä½å®½è¾å¤§çæµ®ç¹æ°è½¬æ¢ä¸ºä½å®½è¾å°çæµ®ç¹æ°ï¼ä¼å°è¯¥æ°èå ¥å°ç®æ ç±»åä¸ææ¥è¿çå¼ï¼

#### æµ®ç¹æ´æ°è½¬æ¢

  * æµ®ç¹æ°è½¬æ¢ä¸ºæ´æ°æ¶ï¼ä¼èå¼æµ®ç¹æ°çå ¨é¨å°æ°é¨åï¼

å¦æç®æ ç±»åæ¯ `bool`ï¼åæ¯ å¸å°è½¬æ¢ï¼

  * æ´æ°è½¬æ¢ä¸ºæµ®ç¹æ°æ¶ï¼ä¼èå ¥å°ç®æ ç±»åä¸ææ¥è¿çå¼ï¼

å¦æè¯¥å¼ä¸è½éåºå°ç®æ ç±»åä¸­ï¼é£ä¹è¡ä¸ºæªå®ä¹ï¼

å¦ææºç±»åæ¯ `bool`ï¼é£ä¹ `false` è½¬æ¢ä¸ºé¶ï¼è `true` è½¬æ¢ä¸ºä¸ï¼

#### å¸å°è½¬æ¢

å°å ¶ä»ç±»åè½¬æ¢ä¸º `bool` ç±»åæ¶ï¼é¶å¼è½¬æ¢ä¸º `false`ï¼éé¶å¼è½¬æ¢ä¸º `true`ï¼

## å®ä¹åé

ç®åå°è¯´2ï¼å®ä¹ä¸ä¸ªåéï¼éè¦å å«ç±»åè¯´æç¬¦ï¼ææåéçç±»åï¼ï¼ä»¥åè¦å®ä¹çåéåï¼

ä¾å¦ï¼ä¸é¢è¿å æ¡è¯­å¥é½æ¯åéå®ä¹è¯­å¥ï¼

```text 1 2 3 ``` |  ```text int oi ; double wiki ; char org = 'c' ; ```   
---|---  
  
å¨ç®åæä»¬ææ¥è§¦å°çç¨åºæ®µä¸­ï¼å®ä¹å¨è±æ¬å·å è£¹çå°æ¹çåéæ¯å±é¨åéï¼èå®ä¹å¨æ²¡æè±æ¬å·å è£¹çå°æ¹çåéæ¯å ¨å±åéï¼å®é æä¾å¤ï¼ä½æ¯ç°å¨ä¸å¿ äºè§£ï¼

å®ä¹æ¶æ²¡æåå§åå¼çå ¨å±åéä¼è¢«åå§åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå±é¨åéæ²¡æè¿ç§ç¹æ§ï¼éè¦æå¨èµåå§å¼ï¼å¦åå¯è½å¼èµ·é¾ä»¥åç°ç bugï¼

## åéä½ç¨å

ä½ç¨åæ¯åéå¯ä»¥åæ¥ä½ç¨çä»£ç åï¼

å ¨å±åéçä½ç¨åï¼èªå ¶å®ä¹ä¹å¤å¼å§3ï¼è³æä»¶ç»æä½ç½®ä¸ºæ­¢ï¼

å±é¨åéçä½ç¨åï¼èªå ¶å®ä¹ä¹å¤å¼å§ï¼è³ä»£ç åç»æä½ç½®ä¸ºæ­¢ï¼

ç±ä¸å¯¹å¤§æ¬å·æ¬èµ·æ¥çè¥å¹²è¯­å¥ææä¸ä¸ªä»£ç åï¼

```text 1 2 3 4 5 6 7 ``` |  ```text int g = 20 ; // å®ä¹å ¨å±åé int main () { int g = 10 ; // å®ä¹å±é¨åé printf ( "%d \n " , g ); // è¾åº g return 0 ; } ```   
---|---  
  
å¦æä¸ä¸ªä»£ç åçå åµåä¸­å®ä¹äºç¸ååéåçåéï¼åå å±åä¸­å°æ æ³è®¿é®å¤å±åä¸­ç¸ååéåçåéï¼

ä¾å¦ä¸é¢çä»£ç ä¸­ï¼è¾åºç ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼å°æ¯ 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ä¸ºäºé²æ­¢åºç°ææä¹å¤çéè¯¯ï¼è¯·å°½éé¿å å±é¨åéä¸å ¨å±åééåçæ åµï¼

## å¸¸é

å¸¸éæ¯åºå®å¼ï¼å¨ç¨åºæ§è¡æé´ä¸ä¼æ¹åï¼

å¸¸éçå¼å¨å®ä¹åä¸è½è¢«ä¿®æ¹ï¼å®ä¹æ¶å ä¸ä¸ª `const` å ³é®å­å³å¯ï¼

```text 1 2 ``` |  ```text const int a = 2 ; a = 3 ; ```   
---|---  
  
å¦æä¿®æ¹äºå¸¸éçå¼ï¼å¨ç¼è¯ç¯èå°±ä¼æ¥éï¼`error: assignment of read-only variable 'a'`ï¼

## åèèµæä¸æ³¨é

  1. [Working Draft, Standard for Programming Language C++](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/n4917.pdf)
  2. [ç±»å - cppreference.com](https://zh.cppreference.com/w/cpp/language/type)
  3. C è¯­è¨ç [ç®æ¯ç±»å - cppreference.com](https://zh.cppreference.com/w/c/language/arithmetic_types)
  4. [åºç¡ç±»å - cppreference.com](https://zh.cppreference.com/w/cpp/language/types)
  5. [å®å®½æ´æ°ç±»åï¼C++11 èµ·ï¼- cppreference.com](https://zh.cppreference.com/w/cpp/types/integer)
  6. William Kahan (1 October 1997).["Lecture Notes on the Status of IEEE Standard 754 for Binary Floating-Point Arithmetic"](https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF).
  7. [éå¼è½¬æ¢ - cppreference.com](https://zh.cppreference.com/w/cpp/language/implicit_conversion)
  8. [å£°æ - cppreference](https://zh.cppreference.com/w/cpp/language/declarations)
  9. [ä½ç¨å - cppreference.com](https://zh.cppreference.com/w/cpp/language/scope)

* * *

  1. C++20 åè§å®æç¬¦å·æ´æ°è³å°è¦è¦ç [åç ](../../math/bit/#æ´æ°ä¸ä½åºå) çè¡¨ç¤ºèå´ï¼å³ â2ð¥â1 +1 â¼2ð¥â1 â1â2xâ1+1â¼2xâ1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼ä½å®é ä¸ç»å¤§å¤æ°å®ç°ä¸­åéç¨ [è¡¥ç ](../../math/bit/#æ´æ°ä¸ä½åºå) å®ç°ï¼C++20 èµ·è¿ä¸æ­¥è§å®æç¬¦å·æ´æ°å¿ é¡»ä½¿ç¨è¡¥ç å®ç°ï¼è¯¦è§ [Range of values - cppreference](https://en.cppreference.com/w/cpp/language/types.html#Range_of_values)ï¼Â â©

  2. å®ä¹ä¸ä¸ªåéæ¶ï¼é¤äºç±»åè¯´æç¬¦ä¹å¤ï¼è¿å¯ä»¥å å«å ¶ä»è¯´æç¬¦ï¼è¯¦è§ [å£°æ - cppreference](https://zh.cppreference.com/w/cpp/language/declarations)ï¼Â â©

  3. æ´åç¡®çè¯´æ³æ¯ [å£°æç¹](https://zh.cppreference.com/w/cpp/language/scope#.E5.A3.B0.E6.98.8E.E7.82.B9)ï¼Â â©

  4. å æ¬æ°ç»ç±»åãå¼ç¨ç±»åãæéç±»åãç±»ç±»åãå½æ°ç±»åç­ï¼ç±äºæ¬ç¯æç« æ¯é¢ååå­¦è çï¼æ ä¸å¨æ¬æåå ·ä½ä»ç»ï¼å ·ä½è¯·åé [ç±»å - cppreference.com](https://zh.cppreference.com/w/cpp/language/type)Â â©

  5. åè§ <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3054.pdf>Â â©

  6. ä¸å å«å®½å­ç¬¦ç±»åãä½ååæä¸¾ç±»åï¼è¯¦è§ [æ´åè½¬æ¢ - cppreference](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E6.95.B4.E5.9E.8B.E8.BD.AC.E6.8D.A2)ï¼Â â©

  7. èª C++20 èµ·çæï¼C++20 åç»ææ¯å®ç°å®ä¹çï¼è¯¦è§ [æ´åè½¬æ¢ - cppreference](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E6.95.B4.E5.9E.8B.E8.BD.AC.E6.8D.A2)ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/2/26 03:56:39ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/var.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/var.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [orzAtalod](https://github.com/orzAtalod), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [shuzhouliu](https://github.com/shuzhouliu), [abc1763613206](https://github.com/abc1763613206), [CamberLoid](https://github.com/CamberLoid), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Friendseeker](https://github.com/Friendseeker), [Great-designer](https://github.com/Great-designer), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [hhc0001](https://github.com/hhc0001), [ksyx](https://github.com/ksyx), [mgt](mailto:i@margatroid.xyz), [TOMWT-qwq](https://github.com/TOMWT-qwq), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
