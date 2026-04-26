# é«ç²¾åº¦è®¡ç® - OI Wiki

- Source: https://oi-wiki.org/math/bignum/

# é«ç²¾åº¦è®¡ç®

> å¤ªé¿ä¸ççï¼ç»å°¾èªåæ¨¡æ¿â¦â¦

## å®ä¹

é«ç²¾åº¦è®¡ç®ï¼Arbitrary-Precision Arithmeticï¼ï¼ä¹è¢«ç§°ä½å¤§æ´æ°ï¼bignumï¼è®¡ç®ï¼è¿ç¨äºä¸äºç®æ³ç»ææ¥æ¯ææ´å¤§æ´æ°é´çè¿ç®ï¼æ°å­å¤§å°è¶ è¿è¯­è¨å å»ºæ´åï¼ï¼

## å¼å ¥

é«ç²¾åº¦é®é¢å å«å¾å¤å°çç»èï¼å®ç°ä¸ä¹æå¾å¤è®²ç©¶ï¼

æä»¥ä»å¤©å°±æ¥ä¸èµ·å®ç°ä¸ä¸ªç®åçè®¡ç®å¨å§ï¼

ä»»å¡

è¾å ¥ï¼ä¸ä¸ªå½¢å¦ `a <op> b` çè¡¨è¾¾å¼ï¼

  * `a`ã`b` åå«æ¯é¿åº¦ä¸è¶ è¿ 10001000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåè¿å¶éè´æ´æ°ï¼
  * `<op>` æ¯ä¸ä¸ªå­ç¬¦ï¼`+`ã`-`ã`*` æ `/`ï¼ï¼è¡¨ç¤ºè¿ç®ï¼
  * æ´æ°ä¸è¿ç®ç¬¦ä¹é´ç±ä¸ä¸ªç©ºæ ¼åéï¼

è¾åºï¼è¿ç®ç»æï¼

  * å¯¹äº `+`ã`-`ã`*` è¿ç®ï¼è¾åºä¸è¡è¡¨ç¤ºç»æï¼
  * å¯¹äº `/` è¿ç®ï¼è¾åºä¸¤è¡åå«è¡¨ç¤ºååä½æ°ï¼
  * ä¿è¯ç»æåä¸ºéè´æ´æ°ï¼

## å­å¨

å¨å¹³å¸¸çå®ç°ä¸­ï¼é«ç²¾åº¦æ°å­å©ç¨å­ç¬¦ä¸²è¡¨ç¤ºï¼æ¯ä¸ä¸ªå­ç¬¦è¡¨ç¤ºæ°å­çä¸ä¸ªåè¿å¶ä½ï¼å æ­¤å¯ä»¥è¯´ï¼é«ç²¾åº¦æ°å¼è®¡ç®å®é ä¸æ¯ä¸ç§ç¹å«çå­ç¬¦ä¸²å¤çï¼

è¯»å ¥å­ç¬¦ä¸²æ¶ï¼æ°å­æé«ä½å¨å­ç¬¦ä¸²é¦ï¼ä¸æ å°çä½ç½®ï¼ï¼ä½æ¯ä¹ æ¯ä¸ï¼ä¸æ æå°çä½ç½®å­æ¾çæ¯æ°å­ç **æä½ä½** ï¼å³å­å¨åè½¬çå­ç¬¦ä¸²ï¼è¿ä¹åçåå å¨äºï¼æ°å­çé¿åº¦å¯è½åçååï¼ä½æä»¬å¸æåæ ·æå¼ä½å§ç»ä¿æå¯¹é½ï¼ä¾å¦ï¼å¸æææçä¸ªä½é½å¨ä¸æ  `[0]`ï¼ææçåä½é½å¨ä¸æ  `[1]`â¦â¦ï¼ï¼åæ¶ï¼å ãåãä¹çè¿ç®ä¸è¬é½ä»ä¸ªä½å¼å§è¿è¡ï¼åæ³å°å­¦çç«å¼è¿ç®ï¼ï¼è¿é½ç»äºãåè½¬å­å¨ãä»¥å åççç±ï¼

æ­¤åæä»¬å°ä¸ç´æ²¿ç¨è¿ä¸çº¦å®ï¼å®ä¹ä¸ä¸ªå¸¸æ° `LEN = 1004` è¡¨ç¤ºç¨åºæå®¹çº³çæå¤§é¿åº¦ï¼

ç±æ­¤ä¸é¾ååºè¯»å ¥é«ç²¾åº¦æ°å­çä»£ç ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text void clear ( int a []) { for ( int i = 0 ; i < LEN ; ++ i ) a [ i ] = 0 ; } void read ( int a []) { static char s [ LEN \+ 1 ]; scanf ( "%s" , s ); clear ( a ); int len = strlen ( s ); // å¦ä¸æè¿°ï¼åè½¬ for ( int i = 0 ; i < len ; ++ i ) a [ len \- i \- 1 ] = s [ i ] \- '0' ; // s[i] - '0' å°±æ¯ s[i] æè¡¨ç¤ºçæ°ç  // æäºåå­¦å¯è½æ´ä¹ æ¯ç¨ ord(s[i]) - ord('0') çæ¹å¼çè§£ } ```   
---|---  
  
è¾åºä¹æç §å­å¨çéåºè¾åºï¼ç±äºä¸å¸æè¾åºåå¯¼é¶ï¼æ è¿éä»æé«ä½å¼å§åä¸å¯»æ¾ç¬¬ä¸ä¸ªéé¶ä½ï¼ä»æ­¤å¤å¼å§è¾åºï¼ç»æ­¢æ¡ä»¶ `i >= 1` èä¸æ¯ `i >= 0` æ¯å ä¸ºå½æ´ä¸ªæ°å­ç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ä»å¸æè¾åºä¸ä¸ªå­ç¬¦ `0`ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text void print ( int a []) { int i ; for ( i = LEN \- 1 ; i >= 1 ; \-- i ) if ( a [ i ] != 0 ) break ; for (; i >= 0 ; \-- i ) putchar ( a [ i ] \+ '0' ); putchar ( '\n' ); } ```   
---|---  
  
æ¼èµ·æ¥å°±æ¯ä¸ä¸ªå®æ´çå¤è¯»æºç¨åºå¯ï¼

`copycat.cpp`

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text #include <cstdio> #include <cstring> constexpr int LEN = 1004 ; int a [ LEN ]; void clear ( int a []) { for ( int i = 0 ; i < LEN ; ++ i ) a [ i ] = 0 ; } void read ( int a []) { static char s [ LEN \+ 1 ]; scanf ( "%s" , s ); clear ( a ); int len = strlen ( s ); for ( int i = 0 ; i < len ; ++ i ) a [ len \- i \- 1 ] = s [ i ] \- '0' ; } void print ( int a []) { int i ; for ( i = LEN \- 1 ; i >= 1 ; \-- i ) if ( a [ i ] != 0 ) break ; for (; i >= 0 ; \-- i ) putchar ( a [ i ] \+ '0' ); putchar ( '\n' ); } int main () { read ( a ); print ( a ); return 0 ; } ```   
---|---  
  
## ååè¿ç®

ååè¿ç®ä¸­é¾åº¦ä¹åä¸ç¸åï¼æç®åçæ¯é«ç²¾åº¦å åæ³ï¼å ¶æ¬¡æ¯é«ç²¾åº¦âåç²¾åº¦ï¼æ®éç `int`ï¼ä¹æ³åé«ç²¾åº¦âé«ç²¾åº¦ä¹æ³ï¼æåæ¯é«ç²¾åº¦âé«ç²¾åº¦é¤æ³ï¼

æä»¬å°æè¿ä¸ªé¡ºåºåå«å®ç°ææè¦æ±çåè½ï¼

### å æ³

é«ç²¾åº¦å æ³ï¼å ¶å®å°±æ¯ç«å¼å æ³å¦ï¼

![](./images/plus.svg)

ä¹å°±æ¯ä»æä½ä½å¼å§ï¼å°ä¸¤ä¸ªå æ°å¯¹åºä½ç½®ä¸çæ°ç ç¸å ï¼å¹¶å¤æ­æ¯å¦è¾¾å°æè¶ è¿ 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æè¾¾å°ï¼é£ä¹å¤çè¿ä½ï¼å°æ´é«ä¸ä½çç»æä¸å¢å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½åä½çç»æåå° 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text void add ( int a [], int b [], int c []) { clear ( c ); // é«ç²¾åº¦å®ç°ä¸­ï¼ä¸è¬ä»¤æ°ç»çæå¤§é¿åº¦ LEN æ¯å¯è½çè¾å ¥å¤§ä¸äº // ç¶åç¥å»æ«å°¾çå æ¬¡å¾ªç¯ï¼è¿æ ·ä¸æ¥å¯ä»¥çå»ä¸å°è¾¹çæ åµçå¤ç // å ä¸ºå®é è¾å ¥ä¸ä¼è¶ è¿ 1000 ä½ï¼æ å¨æ­¤å¾ªç¯å° LEN - 1 = 1003 å·²ç»è¶³å¤ for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { // å°ç¸åºä½ä¸çæ°ç ç¸å c [ i ] += a [ i ] \+ b [ i ]; if ( c [ i ] >= 10 ) { // è¿ä½ c [ i \+ 1 ] += 1 ; c [ i ] -= 10 ; } } } ```   
---|---  
  
è¯çåä¸ä¸é¨åç»åï¼å¯ä»¥å¾å°ä¸ä¸ªå æ³è®¡ç®å¨ï¼

`adder.cpp`

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text #include <cstdio> #include <cstring> constexpr int LEN = 1004 ; int a [ LEN ], b [ LEN ], c [ LEN ]; void clear ( int a []) { for ( int i = 0 ; i < LEN ; ++ i ) a [ i ] = 0 ; } void read ( int a []) { static char s [ LEN \+ 1 ]; scanf ( "%s" , s ); clear ( a ); int len = strlen ( s ); for ( int i = 0 ; i < len ; ++ i ) a [ len \- i \- 1 ] = s [ i ] \- '0' ; } void print ( int a []) { int i ; for ( i = LEN \- 1 ; i >= 1 ; \-- i ) if ( a [ i ] != 0 ) break ; for (; i >= 0 ; \-- i ) putchar ( a [ i ] \+ '0' ); putchar ( '\n' ); } void add ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { c [ i ] += a [ i ] \+ b [ i ]; if ( c [ i ] >= 10 ) { c [ i \+ 1 ] += 1 ; c [ i ] -= 10 ; } } } int main () { read ( a ); read ( b ); add ( a , b , c ); print ( c ); return 0 ; } ```   
---|---  
  
### åæ³

é«ç²¾åº¦åæ³ï¼ä¹å°±æ¯ç«å¼åæ³å¦ï¼

![](./images/subtraction.svg)

ä»ä¸ªä½èµ·éä½ç¸åï¼éå°è´çæ åµååä¸ä¸ä½å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´ä½æè·¯ä¸å æ³å®å ¨ä¸è´ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text void sub ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { // éä½ç¸å c [ i ] += a [ i ] \- b [ i ]; if ( c [ i ] < 0 ) { // åä½ c [ i \+ 1 ] -= 1 ; c [ i ] += 10 ; } } } ```   
---|---  
  
å°ä¸ä¸ä¸ªç¨åºä¸­ç `add()` æ¿æ¢æ `sub()`ï¼å°±æäºä¸ä¸ªåæ³è®¡ç®å¨ï¼

`subtractor.cpp`

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text #include <cstdio> #include <cstring> constexpr int LEN = 1004 ; int a [ LEN ], b [ LEN ], c [ LEN ]; void clear ( int a []) { for ( int i = 0 ; i < LEN ; ++ i ) a [ i ] = 0 ; } void read ( int a []) { static char s [ LEN \+ 1 ]; scanf ( "%s" , s ); clear ( a ); int len = strlen ( s ); for ( int i = 0 ; i < len ; ++ i ) a [ len \- i \- 1 ] = s [ i ] \- '0' ; } void print ( int a []) { int i ; for ( i = LEN \- 1 ; i >= 1 ; \-- i ) if ( a [ i ] != 0 ) break ; for (; i >= 0 ; \-- i ) putchar ( a [ i ] \+ '0' ); putchar ( '\n' ); } void sub ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { c [ i ] += a [ i ] \- b [ i ]; if ( c [ i ] < 0 ) { c [ i \+ 1 ] -= 1 ; c [ i ] += 10 ; } } } int main () { read ( a ); read ( b ); sub ( a , b , c ); print ( c ); return 0 ; } ```   
---|---  
  
è¯ä¸è¯ï¼è¾å ¥ `1 2`ââè¾åº `/9999999`ï¼è¯¶è¿ä¸ª **OI Wiki** æä¹ç»äºæä¸ä»½åçä»£ç åâ¦â¦

äºå®ä¸ï¼ä¸é¢çä»£ç åªè½å¤çåæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤§äºç­äºè¢«åæ° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼å¤çè¢«åæ°æ¯åæ°å°ï¼å³ ð <ða<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çæ åµå¾ç®åï¼

ð âð = â(ð âð)aâb=â(bâa)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦è®¡ç® ð âðbâa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å ä¸ºæ ð >ðb>a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è°ç¨ä»¥ä¸ä»£ç ä¸­ç `sub` å½æ°ï¼åæ³ä¸º `sub(b,a,c)`ï¼è¦å¾å° ð âðaâb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å¨å¾æ°åå ä¸è´å·å³å¯ï¼

### ä¹æ³

#### é«ç²¾åº¦âåç²¾åº¦

é«ç²¾åº¦ä¹æ³ï¼ä¹å°±æ¯ç«â¦â¦ç­ä¼å¿ç­ä¼å¿ï¼

å èèä¸ä¸ªç®åçæ åµï¼ä¹æ°ä¸­çä¸ä¸ªæ¯æ®éç `int` ç±»åï¼ææ²¡æç®åçå¤çæ¹æ³å¢ï¼

ä¸ä¸ªç´è§çæè·¯æ¯ç´æ¥å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä½ä¸çæ°å­ä¹ä»¥ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»æ°å¼ä¸æ¥è¯´ï¼è¿ä¸ªæ¹æ³æ¯æ­£ç¡®çï¼ä½å®å¹¶ä¸ç¬¦ååè¿å¶è¡¨ç¤ºæ³ï¼å æ­¤éè¦å°å®éæ°æ´çææ­£å¸¸çæ ·å­ï¼

éæ´çæ¹å¼ï¼ä¹æ¯ä»ä¸ªä½å¼å§éä½åä¸å¤çè¿ä½ï¼ä½æ¯è¿éçè¿ä½å¯è½éå¸¸å¤§ï¼çè³è¿å¤§äº 99![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºæ¯ä¸ä½è¢«ä¹ä¸ä¹åé½å¯è½è¾¾å° 9ð9b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éçº§ï¼æä»¥è¿éçè¿ä½ä¸è½åç®åå°è¿è¡ â10â10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ç®ï¼èæ¯è¦éè¿é¤ä»¥ 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåä»¥åä½æ°è®¡ç®ï¼è¯¦è§ä»£ç æ³¨éï¼ä¹å¯ä»¥åèä¸å¾å±ç¤ºçä¸ä¸ªè®¡ç®é«ç²¾åº¦æ° 13371337![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä»¥åç²¾åº¦æ° 4242![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿ç¨ï¼

![](./images/multiplication-short.png)

å½ç¶ï¼ä¹æ¯åºäºè¿ä¸ªåå ï¼è¿ä¸ªæ¹æ³éè¦ç¹å«å ³æ³¨ä¹æ° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çèå´ï¼è¥å®å 109109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç¸åºæ´åçåå¼ä¸çï¼å±äºåä¸æ°éçº§ï¼é£ä¹éè¦æ ç¨é«ç²¾åº¦âåç²¾åº¦ä¹æ³ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text void mul_short ( int a [], int b , int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { // ç´æ¥æ a çç¬¬ i ä½æ°ç ä¹ä»¥ä¹æ°ï¼å å ¥ç»æ c [ i ] += a [ i ] * b ; if ( c [ i ] >= 10 ) { // å¤çè¿ä½ // c[i] / 10 å³é¤æ³çåæ°æä¸ºè¿ä½çå¢éå¼ c [ i \+ 1 ] += c [ i ] / 10 ; // è c[i] % 10 å³é¤æ³çä½æ°æä¸ºå¨å½åä½çä¸çå¼ c [ i ] %= 10 ; } } } ```   
---|---  
  
#### é«ç²¾åº¦âé«ç²¾åº¦

å¦æä¸¤ä¸ªä¹æ°é½æ¯é«ç²¾åº¦ï¼é£ä¹ç«å¼ä¹æ³åå¯ä»¥å¤§æ¾èº«æäºï¼

åæ³ç«å¼ä¹æ³çæ¯ä¸æ­¥ï¼å®é ä¸æ¯è®¡ç®äºè¥å¹² ð Ãðð Ã10ðaÃbiÃ10i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåï¼ä¾å¦è®¡ç® 1337 Ã421337Ã42![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¡ç®çå°±æ¯ 1337 Ã2 Ã100 +1337 Ã4 Ã1011337Ã2Ã100+1337Ã4Ã101![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

äºæ¯å¯ä»¥å° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸ºå®çæææ°ç ï¼å ¶ä¸­æ¯ä¸ªæ°ç é½æ¯åç²¾åº¦æ°ï¼å°å®ä»¬åå«ä¸ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸ä¹ï¼ååå·¦ç§»å¨å°åèªçä½ç½®ä¸ç¸å å³å¾ç­æ¡ï¼å½ç¶ï¼æåä¹éè¦ç¨ä¸ä¸ä¾ç¸åçæ¹å¼å¤çè¿ä½ï¼

![](./images/multiplication-long.png)

æ³¨æè¿ä¸ªè¿ç¨ä¸ç«å¼ä¹æ³ä¸å°½ç¸åï¼æä»¬çç®æ³å¨æ¯ä¸æ­¥ä¹çè¿ç¨ä¸­å¹¶ä¸è¿ä½ï¼èæ¯å°ææçç»æä¿çå¨å¯¹åºçä½ç½®ä¸ï¼å°æååç»ä¸å¤çè¿ä½ï¼ä½è¿ä¸ä¼å½±åç»æï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text void mul ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { // è¿éç´æ¥è®¡ç®ç»æä¸­çä»ä½å°é«ç¬¬ i ä½ï¼ä¸ä¸å¹¶å¤çäºè¿ä½ // ç¬¬ i æ¬¡å¾ªç¯ä¸º c[i] å ä¸äºæææ»¡è¶³ p + q = i ç a[p] ä¸ b[q] çä¹ç§¯ä¹å // è¿æ ·åçææåç´æ¥è¿è¡ä¸å¾çè¿ç®æåæ±åæ¯ä¸æ ·çï¼åªæ¯æ´å ç®ç­çä¸ç§å®ç°æ¹å¼ for ( int j = 0 ; j <= i ; ++ j ) c [ i ] += a [ j ] * b [ i \- j ]; if ( c [ i ] >= 10 ) { c [ i \+ 1 ] += c [ i ] / 10 ; c [ i ] %= 10 ; } } } ```   
---|---  
  
### é¤æ³

é«ç²¾åº¦é¤æ³çä¸ç§å®ç°æ¹å¼å°±æ¯ç«å¼é¿é¤æ³ï¼

![](./images/division.svg)

ç«å¼é¿é¤æ³å®é ä¸å¯ä»¥çä½ä¸ä¸ªéæ¬¡åæ³çè¿ç¨ï¼ä¾å¦ä¸å¾ä¸­åæ°åä½çè®¡ç®å¯ä»¥è¿æ ·çè§£ï¼å° 4545![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå»ä¸æ¬¡ 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååå¾å°äº 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è½ååï¼æ æ­¤ä½ä¸º 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºäºåå°åä½è¿ç®ï¼æä»¬æåå¾å°è¢«é¤æ°çé¿åº¦ ððla![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸é¤æ°çé¿åº¦ ððlb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»ä¸æ  ðð âððlaâlb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼ä»é«ä½å°ä½ä½æ¥è®¡ç®åï¼è¿åæå·¥è®¡ç®æ¶å°ç¬¬ä¸æ¬¡ä¹æ³çæé«ä½ä¸è¢«é¤æ°æé«ä½å¯¹é½çåæ³æ¯ä¸æ ·çï¼

åèç¨åºå®ç°äºä¸ä¸ªå½æ° `greater_eq()` ç¨äºå¤æ­è¢«é¤æ°ä»¥ä¸æ  `last_dg` ä¸ºæä½ä½ï¼æ¯å¦å¯ä»¥ååå»é¤æ°èä¿æéè´ï¼æ­¤åå¯¹äºåçæ¯ä¸ä½ï¼ä¸æ­è°ç¨ `greater_eq()`ï¼å¹¶å¨æç«çæ¶åç¨é«ç²¾åº¦åæ³ä»ä½æ°ä¸­åå»é¤æ°ï¼ä¹å³æ¨¡æäºç«å¼é¤æ³çè¿ç¨ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` |  ```text // è¢«é¤æ° a ä»¥ä¸æ  last_dg ä¸ºæä½ä½ï¼æ¯å¦å¯ä»¥ååå»é¤æ° b èä¿æéè´ // len æ¯é¤æ° b çé¿åº¦ï¼é¿å åå¤è®¡ç® bool greater_eq ( int a [], int b [], int last_dg , int len ) { // æå¯è½è¢«é¤æ°å©ä½çé¨åæ¯é¤æ°é¿ï¼è¿ä¸ªæ åµä¸æå¤å¤åº 1 ä½ï¼æ å¦æ­¤å¤æ­å³å¯ if ( a [ last_dg \+ len ] != 0 ) return true ; // ä»é«ä½å°ä½ä½ï¼éä½æ¯è¾ for ( int i = len \- 1 ; i >= 0 ; \-- i ) { if ( a [ last_dg \+ i ] > b [ i ]) return true ; if ( a [ last_dg \+ i ] < b [ i ]) return false ; } // ç¸ç­çæ å½¢ä¸ä¹æ¯å¯è¡ç return true ; } void div ( int a [], int b [], int c [], int d []) { clear ( c ); clear ( d ); int la , lb ; for ( la = LEN \- 1 ; la > 0 ; \-- la ) if ( a [ la \- 1 ] != 0 ) break ; for ( lb = LEN \- 1 ; lb > 0 ; \-- lb ) if ( b [ lb \- 1 ] != 0 ) break ; if ( lb == 0 ) { // é¤æ°ä¸è½ä¸ºé¶ puts ( "> <" ); return ; } // c æ¯å // d æ¯è¢«é¤æ°çå©ä½é¨åï¼ç®æ³ç»æåèªç¶æä¸ºä½æ° for ( int i = 0 ; i < la ; ++ i ) d [ i ] = a [ i ]; for ( int i = la \- lb ; i >= 0 ; \-- i ) { // è®¡ç®åçç¬¬ i ä½ while ( greater_eq ( d , b , i , lb )) { // è¥å¯ä»¥åï¼åå // è¿ä¸æ®µæ¯ä¸ä¸ªé«ç²¾åº¦åæ³ for ( int j = 0 ; j < lb ; ++ j ) { d [ i \+ j ] -= b [ j ]; if ( d [ i \+ j ] < 0 ) { d [ i \+ j \+ 1 ] -= 1 ; d [ i \+ j ] += 10 ; } } // ä½¿åçè¿ä¸ä½å¢å 1 c [ i ] += 1 ; // è¿åå¾ªç¯å¼å¤´ï¼éæ°æ£æ¥ } } } ```   
---|---  
  
## å ¥é¨ç¯å®æï¼

å°ä¸é¢ä»ç»çååè¿ç®çå®ç°ç»åï¼å³å¯å®æå¼å¤´æå°çè®¡ç®å¨ç¨åºï¼

`calculator.cpp`

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 ``` |  ```text #include <cstdio> #include <cstring> constexpr int LEN = 1004 ; int a [ LEN ], b [ LEN ], c [ LEN ], d [ LEN ]; void clear ( int a []) { for ( int i = 0 ; i < LEN ; ++ i ) a [ i ] = 0 ; } void read ( int a []) { static char s [ LEN \+ 1 ]; scanf ( "%s" , s ); clear ( a ); int len = strlen ( s ); for ( int i = 0 ; i < len ; ++ i ) a [ len \- i \- 1 ] = s [ i ] \- '0' ; } void print ( int a []) { int i ; for ( i = LEN \- 1 ; i >= 1 ; \-- i ) if ( a [ i ] != 0 ) break ; for (; i >= 0 ; \-- i ) putchar ( a [ i ] \+ '0' ); putchar ( '\n' ); } void add ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { c [ i ] += a [ i ] \+ b [ i ]; if ( c [ i ] >= 10 ) { c [ i \+ 1 ] += 1 ; c [ i ] -= 10 ; } } } void sub ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { c [ i ] += a [ i ] \- b [ i ]; if ( c [ i ] < 0 ) { c [ i \+ 1 ] -= 1 ; c [ i ] += 10 ; } } } void mul ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { for ( int j = 0 ; j <= i ; ++ j ) c [ i ] += a [ j ] * b [ i \- j ]; if ( c [ i ] >= 10 ) { c [ i \+ 1 ] += c [ i ] / 10 ; c [ i ] %= 10 ; } } } bool greater_eq ( int a [], int b [], int last_dg , int len ) { if ( a [ last_dg \+ len ] != 0 ) return true ; for ( int i = len \- 1 ; i >= 0 ; \-- i ) { if ( a [ last_dg \+ i ] > b [ i ]) return true ; if ( a [ last_dg \+ i ] < b [ i ]) return false ; } return true ; } void div ( int a [], int b [], int c [], int d []) { clear ( c ); clear ( d ); int la , lb ; for ( la = LEN \- 1 ; la > 0 ; \-- la ) if ( a [ la \- 1 ] != 0 ) break ; for ( lb = LEN \- 1 ; lb > 0 ; \-- lb ) if ( b [ lb \- 1 ] != 0 ) break ; if ( lb == 0 ) { puts ( "> <" ); return ; } for ( int i = 0 ; i < la ; ++ i ) d [ i ] = a [ i ]; for ( int i = la \- lb ; i >= 0 ; \-- i ) { while ( greater_eq ( d , b , i , lb )) { for ( int j = 0 ; j < lb ; ++ j ) { d [ i \+ j ] -= b [ j ]; if ( d [ i \+ j ] < 0 ) { d [ i \+ j \+ 1 ] -= 1 ; d [ i \+ j ] += 10 ; } } c [ i ] += 1 ; } } } int main () { read ( a ); char op [ 4 ]; scanf ( "%s" , op ); read ( b ); switch ( op [ 0 ]) { case '+' : add ( a , b , c ); print ( c ); break ; case '-' : sub ( a , b , c ); print ( c ); break ; case '*' : mul ( a , b , c ); print ( c ); break ; case '/' : div ( a , b , c , d ); print ( c ); print ( d ); break ; default : puts ( "> <" ); } return 0 ; } ```   
---|---  
  
## åä½é«ç²¾åº¦

### å¼å ¥

å¨ä¸è¬çé«ç²¾åº¦å æ³ï¼åæ³ï¼ä¹æ³è¿ç®ä¸­ï¼æä»¬é½æ¯å°åä¸è¿ç®çæ°æåæä¸ä¸ªä¸ªåç¬çæ°ç è¿è¡è¿ç®ï¼

ä¾å¦è®¡ç® 8192 Ã428192Ã42![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¦ææç §é«ç²¾åº¦ä¹é«ç²¾åº¦çè®¡ç®æ¹å¼ï¼æä»¬å®é ä¸ç®çæ¯ (8000 +100 +90 +2) Ã(40 +2)(8000+100+90+2)Ã(40+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¨ä½æ°è¾å¤çæ¶åï¼æååºçæ°ä¹å¾å¤ï¼é«ç²¾åº¦è¿ç®çæçå°±ä¼ä¸éï¼

ææ²¡æåæ³ä½åºä¸äºä¼åå¢ï¼

æ³¨æå°æåæ°å­çæ¹å¼å¹¶ä¸å½±åæç»çç»æï¼å æ­¤æä»¬å¯ä»¥å°è¥å¹²ä¸ªæ°ç è¿è¡åå¹¶ï¼

### è¿ç¨

è¿æ¯ä»¥ä¸é¢è¿ä¸ªä¾å­ä¸ºä¾ï¼å¦ææä»¬æ¯ä¸¤ä½æåä¸ä¸ªæ°ï¼æä»¬å¯ä»¥æåæ (8100 +92) Ã42(8100+92)Ã42![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿æ ·çæåä¸å½±åæç»ç»æï¼ä½æ¯å ä¸ºæååºçæ°å­åå°äºï¼è®¡ç®æçä¹å°±æåäºï¼

ä» [è¿ä½å¶](../numeral-sys/base/) çè§åº¦çè§£è¿ä¸è¿ç¨ï¼æä»¬éè¿å¨è¾å¤§çè¿ä½å¶ï¼ä¸é¢æ¯ä¸¤ä½æåä¸ä¸ªæ°ï¼å¯ä»¥è®¤ä¸ºæ¯å¨ 100100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å¶ä¸è¿è¡è¿ç®ï¼ä¸è¿è¡è¿ç®ï¼ä»èè¾¾å°åå°åä¸è¿ç®çæ°å­çä½æ°ï¼æåè¿ç®æççç®çï¼

è¿å°±æ¯ **åä½é«ç²¾åº¦** çææ³ï¼

ä¸é¢æä»¬ç»åºåä½é«ç²¾åº¦çå æ³ä»£ç ï¼ç¨äºè¿ä¸æ­¥éè¿°å ¶å®ç°æ¹æ³ï¼

åä½é«ç²¾åº¦å æ³åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text // è¿éç a,b,c æ°ç»åä¸º p è¿å¶ä¸çæ° // æç»è¾åºç­æ¡æ¶éè¦å°æ°å­è½¬ä¸ºåè¿å¶ void add ( int a [], int b [], int c []) { clear ( c ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) { c [ i ] += a [ i ] \+ b [ i ]; if ( c [ i ] >= p ) { // å¨æ®éé«ç²¾åº¦è¿ç®ä¸ï¼p=10 c [ i \+ 1 ] += 1 ; c [ i ] -= p ; } } } ```   
---|---  
  
### åä½é«ç²¾ä¸çé«æç«å¼é¤æ³

å¨ä½¿ç¨åä½é«ç²¾æ¶ï¼å¦æè¯åæ¶ä»ç¶ä½¿ç¨ä¸æä»ç»çæ¹æ³ï¼ç±äºè¯åæ¬¡æ°ä¼å¾å¤ï¼è®¡ç®å¸¸æ°ä¼éå¸¸å¤§ï¼ä¾å¦å¨ä¸è¿å¶ä¸ï¼å¹³åæ¯ä¸ªä½éè¦è¯å 5000 æ¬¡ï¼è¿ä¸ªå·¨å¤§çå¸¸æ°æ¯ä¸å¯æ¥åçï¼å æ­¤æä»¬éè¦ä¸ä¸ªæ´é«æçè¯ååæ³ï¼

æä»¬å¯ä»¥æ double ä½ä¸ºåªä»ï¼åè®¾è¢«é¤æ°æ 4 ä½ï¼æ¯ ð4,ð3,ð2,ð1a4,a3,a2,a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¤æ°æ 3 ä½ï¼æ¯ ð3,ð2,ð1b3,b2,b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æä»¬åªè¦è¯ä¸ä½çåï¼ä½¿ç¨ ððð ðbase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å¶ï¼ç¨å¼å­ ð4ððð ð+ð3ð3+ð2ððð ðâ1+(ð1+1)ððð ðâ2a4base+a3b3+b2baseâ1+(b1+1)baseâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥ä¼°åï¼èå¯¹äºå¤ä¸ªä½çæ åµï¼å°±æ¯ä¸ä½çåæ³å ä¸ªå¾ªç¯ï¼ç±äºé¤æ°ä½¿ç¨ 3 ä½çç²¾åº¦æ¥åä¸ä¼°åï¼è½ä¿è¯ä¼°çå q' ä¸å®é å q çå ³ç³»æ»¡è¶³ ð â1 â¤ðâ² â¤ðqâ1â¤qâ²â¤q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·æ¯ä¸ªä½å¨æåçæ åµä¸ä¹åªéè¦ä¸¤æ¬¡è¯åï¼ä½ä¸æ­¤åæ¶è¦æ± ððð ð3base3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ double çææç²¾åº¦å ï¼å³ ððð ð3 <253base3<253![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥å¨è¿ç¨è¿ä¸ªæ¹æ³æ¶å»ºè®®ä¸è¦è¶ è¿ 32768 è¿å¶ï¼å¦åå¾å®¹æå ç²¾åº¦ä¸è¶³äº§çè¯¯å·®ä»èå¯¼è´éè¯¯ï¼

å¦å¤ï¼ç±äºä¼°çåæ»æ¯å°äºç­äºå®é åï¼æä»¥è¿æåè¿ä¸æ­¥ä¼åçç©ºé´ï¼ç»å¤§å¤æ°æ åµä¸æ¯ä¸ªä½åªä¼°åä¸æ¬¡ï¼è¿æ ·å¨ä¸ä¸ä¸ªä½ä¼°åæ¶ï¼è½ç¶å¾å°çåæå¯è½å ä¸ºåä¸ä½çè¯¯å·®é æè¯åç»æå¤§äºç­äº baseï¼ä½è¿æ²¡æå ³ç³»ï¼åªè¦å¨æååç»ä¸è¿ä½ä¾¿å¯ï¼ä¸¾ä¸ªä¾å­ï¼åè®¾ base æ¯ 10ï¼æ± 395081/9876395081/9876![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯åè®¡ç®æ­¥éª¤å¦ä¸ï¼

  1. é¦å è¯åè®¡ç®å¾å° 3950/988 =33950/988=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯ 395081 â(9876 Ã3 Ã101) =98801395081â(9876Ã3Ã101)=98801![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ­¥åºç°äºè¯¯å·®ï¼ä½ä¸ç¨ç®¡ï¼ç»§ç»­ä¸ä¸æ­¥è®¡ç®ï¼
  2. å¯¹ä½æ° 98801 ç»§ç»­è¯åè®¡ç®å¾å° 9880/988 =109880/988=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯ 98801 â(9876 Ã10 Ã100) =4198801â(9876Ã10Ã100)=41![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±æ¯æç»ä½æ°ï¼
  3. æè¯åè¿ç¨çç»æå èµ·æ¥å¹¶å¤çè¿ä½ï¼å³ 3 Ã101 +10 Ã100 =403Ã101+10Ã100=40![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¾¿æ¯åç¡®çåï¼

æ¹æ³è½ç¶ççç®åï¼ä½å ·ä½å®ç°ä¸å¾å®¹æè¿åï¼æä»¥ä»¥ä¸æä¾ä¸ä¸ªç»è¿å¤çªéªè¯ç¡®è®¤æ²¡æé®é¢çå®ç°ä¾å¤§å®¶åèï¼è¦æ³¨æçç»èä¹åå¨æ³¨éå½ä¸­ï¼

åä½é«ç²¾åº¦é«æç«å¼é¤æ³åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``` |  ```text // å®æ´æ¨¡æ¿åå®ç° https://baobaobear.github.io/post/20210228-bigint1/ // å¯¹bä¹ä»¥mulåå·¦ç§»offsetçç»æç¸åï¼ä¸ºé¤æ³æå¡ BigIntSimple & sub_mul ( const BigIntSimple & b , int mul , int offset ) { if ( mul == 0 ) return * this ; int borrow = 0 ; // ä¸åæ³ä¸åçæ¯ï¼borrowå¯è½å¾å¤§ï¼ä¸è½ä½¿ç¨åæ³çåæ³ for ( size_t i = 0 ; i < b . v . size (); ++ i ) { borrow += v [ i \+ offset ] \- b . v [ i ] * mul \- BIGINT_BASE \+ 1 ; v [ i \+ offset ] = borrow % BIGINT_BASE \+ BIGINT_BASE \- 1 ; borrow /= BIGINT_BASE ; } // å¦æè¿æåä½å°±ç»§ç»­å¤ç for ( size_t i = b . v . size (); borrow ; ++ i ) { borrow += v [ i \+ offset ] \- BIGINT_BASE \+ 1 ; v [ i \+ offset ] = borrow % BIGINT_BASE \+ BIGINT_BASE \- 1 ; borrow /= BIGINT_BASE ; } return * this ; } BigIntSimple div_mod ( const BigIntSimple & b , BigIntSimple & r ) const { BigIntSimple d ; r = * this ; if ( absless ( b )) return d ; d . v . resize ( v . size () \- b . v . size () \+ 1 ); // æåç®å¥½é¤æ°çæé«ä¸ä½+1çåæ°ï¼è¥æé«ä¸ä½æ¯a3,a2,a1 // é£ä¹dbæ¯a3+a2/base+(a1+1)/base^2çåæ°ï¼æåç¨ä¹æ³ä¼°åçæ¯ä¸ä½ // æ­¤æ³å¨BIGINT_BASE<=32768æ¶å¯å¨int32èå´å ç¨ // ä½å³ä½¿ä½¿ç¨int64ï¼é£ä¹ä¹åªæBIGINT_BASE<=131072æ¶å¯ç¨ï¼ådoubleçç²¾åº¦éå¶ï¼ // è½ä¿è¯ä¼°è®¡ç»æq'ä¸å®é ç»æqçå ³ç³»æ»¡è¶³q'<=q<=q'+1 // æä»¥æ¯ä¸ä½çè¯åå¹³ååªéè¦ä¸æ¬¡ï¼åªè¦åé¢åç»ä¸å¤çè¿ä½å³å¯ // å¦æè¦ä½¿ç¨æ´å¤§çbaseï¼é£ä¹éè¦æ´æ¢å ¶å®è¯åæ¹æ¡ double t = ( b . get (( unsigned ) b . v . size () \- 2 ) \+ ( b . get (( unsigned ) b . v . size () \- 3 ) \+ 1.0 ) / BIGINT_BASE ); double db = 1.0 / ( b . v . back () \+ t / BIGINT_BASE ); for ( size_t i = v . size () \- 1 , j = d . v . size () \- 1 ; j <= v . size ();) { int rm = r . get ( i \+ 1 ) * BIGINT_BASE \+ r . get ( i ); int m = std :: max (( int )( db * rm ), r . get ( i \+ 1 )); r . sub_mul ( b , m , j ); d . v [ j ] += m ; if ( ! r . get ( i \+ 1 )) // æ£æ¥æé«ä½æ¯å¦å·²ä¸º0ï¼é¿å æç«¯æ åµ \-- i , \-- j ; } r . trim (); // ä¿®æ­£ç»æçä¸ªä½ int carry = 0 ; while ( ! r . absless ( b )) { r . subtract ( b ); ++ carry ; } // ä¿®æ­£æ¯ä¸ä½çè¿ä½ for ( size_t i = 0 ; i < d . v . size (); ++ i ) { carry += d . v [ i ]; d . v [ i ] = carry % BIGINT_BASE ; carry /= BIGINT_BASE ; } d . trim (); d . sign = sign * b . sign ; return d ; } BigIntSimple operator / ( const BigIntSimple & b ) const { BigIntSimple r ; return div_mod ( b , r ); } BigIntSimple operator % ( const BigIntSimple & b ) const { BigIntSimple r ; div_mod ( b , r ); return r ; } ```   
---|---  
  
## Karatsuba ä¹æ³

è®°é«ç²¾åº¦æ°å­çä½æ°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹é«ç²¾åº¦âé«ç²¾åº¦ç«å¼ä¹æ³éè¦è±è´¹ ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´ï¼æ¬èä»ç»ä¸ä¸ªæ¶é´å¤æåº¦æ´ä¸ºä¼ç§çç®æ³ï¼ç±åèèï¼ä¿ç½æ¯ï¼æ°å­¦å®¶ Anatoly Karatsuba æåºï¼æ¯ä¸ç§åæ²»ç®æ³ï¼

èèä¸¤ä¸ªåè¿å¶å¤§æ´æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå å« ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°ç ï¼å¯ä»¥æåå¯¼é¶ï¼ï¼ä»»å 0 <ð <ð0<m<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®°

ð¥=ð¥1â 10ð+ð¥0,ð¦=ð¦1â 10ð+ð¦0,ð¥â ð¦=ð§2â 102ð+ð§1â 10ð+ð§0,x=x1â 10m+x0,y=y1â 10m+y0,xâ y=z2â 102m+z1â 10m+z0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ð¥0,ð¦0,ð§0,ð§1 <10ðx0,y0,z0,z1<10m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯å¾

ð§2=ð¥1â ð¦1,ð§1=ð¥1â ð¦0+ð¥0â ð¦1,ð§0=ð¥0â ð¦0.z2=x1â y1,z1=x1â y0+x0â y1,z0=x0â y0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§å¯ç¥

ð§1=(ð¥1+ð¥0)â (ð¦1+ð¦0)âð§2âð§0,z1=(x1+x0)â (y1+y0)âz2âz0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯è¦è®¡ç® ð§1z1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªéè®¡ç® (ð¥1 +ð¥0) â (ð¦1 +ð¦0)(x1+x0)â (y1+y0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸ ð§0z0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãð§2z2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸åå³å¯ï¼

ä¸å¼å®é ä¸æ¯ Karatsuba ç®æ³çæ ¸å¿ï¼å®å°é¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹æ³é®é¢è½¬åä¸ºäº 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¿åº¦æ´å°çå­é®é¢ï¼è¥ä»¤ ð =âð2âm=ân2â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®° Karatsuba ç®æ³è®¡ç®ä¸¤ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ä¹æ³çèæ¶ä¸º ð(ð)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ð(ð) =3 â ð(âð2â) +ð(ð)T(n)=3â T(ân2â)+O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±ä¸»å®çå¯å¾ ð(ð) =Î(ðlog2â¡3) âÎ(ð1.585)T(n)=Î(nlog2â¡3)âÎ(n1.585)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ´ä¸ªè¿ç¨å¯ä»¥éå½å®ç°ï¼ä¸ºæ¸ æ°èµ·è§ï¼ä¸é¢çä»£ç éè¿ Karatsuba ç®æ³å®ç°äºå¤é¡¹å¼ä¹æ³ï¼æååå¤çææçè¿ä½é®é¢ï¼

karatsuba_mulc.cpp

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` |  ```text int * karatsuba_polymul ( int n , int * a , int * b ) { if ( n <= 32 ) { // è§æ¨¡è¾å°æ¶ç´æ¥è®¡ç®ï¼é¿å ç»§ç»­éå½å¸¦æ¥çæçæå¤± int * r = new int [ n * 2 \+ 1 ](); for ( int i = 0 ; i <= n ; ++ i ) for ( int j = 0 ; j <= n ; ++ j ) r [ i \+ j ] += a [ i ] * b [ j ]; return r ; } int m = n / 2 \+ 1 ; int * r = new int [ m * 4 \+ 1 ](); int * z0 , * z1 , * z2 ; z0 = karatsuba_polymul ( m \- 1 , a , b ); z2 = karatsuba_polymul ( n \- m , a \+ m , b \+ m ); // è®¡ç® z1 // ä¸´æ¶æ´æ¹ï¼è®¡ç®å®æ¯åæ¢å¤ for ( int i = 0 ; i \+ m <= n ; ++ i ) a [ i ] += a [ i \+ m ]; for ( int i = 0 ; i \+ m <= n ; ++ i ) b [ i ] += b [ i \+ m ]; z1 = karatsuba_polymul ( m \- 1 , a , b ); for ( int i = 0 ; i \+ m <= n ; ++ i ) a [ i ] -= a [ i \+ m ]; for ( int i = 0 ; i \+ m <= n ; ++ i ) b [ i ] -= b [ i \+ m ]; for ( int i = 0 ; i <= ( m \- 1 ) * 2 ; ++ i ) z1 [ i ] -= z0 [ i ]; for ( int i = 0 ; i <= ( n \- m ) * 2 ; ++ i ) z1 [ i ] -= z2 [ i ]; // ç± z0ãz1ãz2 ç»åè·å¾ç»æ for ( int i = 0 ; i <= ( m \- 1 ) * 2 ; ++ i ) r [ i ] += z0 [ i ]; for ( int i = 0 ; i <= ( m \- 1 ) * 2 ; ++ i ) r [ i \+ m ] += z1 [ i ]; for ( int i = 0 ; i <= ( n \- m ) * 2 ; ++ i ) r [ i \+ m * 2 ] += z2 [ i ]; delete [] z0 ; delete [] z1 ; delete [] z2 ; return r ; } void karatsuba_mul ( int a [], int b [], int c []) { int * r = karatsuba_polymul ( LEN \- 1 , a , b ); memcpy ( c , r , sizeof ( int ) * LEN ); for ( int i = 0 ; i < LEN \- 1 ; ++ i ) if ( c [ i ] >= 10 ) { c [ i \+ 1 ] += c [ i ] / 10 ; c [ i ] %= 10 ; } delete [] r ; } ```   
---|---  
  
å ³äº `new` å `delete`

è§ [å å­æ± ](../../contest/common-tricks/#å)ï¼

ä½æ¯è¿æ ·çå®ç°å­å¨ä¸ä¸ªé®é¢ï¼å¨ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å¶ä¸ï¼å¤é¡¹å¼çæ¯ä¸ä¸ªç³»æ°é½æå¯è½è¾¾å° ð â ð2nâ b2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éçº§ï¼å¨åä½é«ç²¾åº¦å®ç°ä¸­å¯è½é ææ´æ°æº¢åºï¼èè¥å¨å¤é¡¹å¼ä¹æ³çè¿ç¨ä¸­å¤çè¿ä½é®é¢ï¼å ð¥1 +ð¥0x1+x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¦1 +ð¦0y1+y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»æå¯è½è¾¾å° 2 â ðð2â bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¢å ä¸ä¸ªä½ï¼å¦æéç¨ ð¥1 âð¥0x1âx0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡ç®æ¹å¼ï¼åä¸å¾ä¸ç¹æ®å¤çè´æ°çæ åµï¼ï¼å æ­¤ï¼éè¦ä¾ç §å®é çåºç¨åºæ¯æ¥å³å®éç¨ä½ç§å®ç°æ¹å¼ï¼

## åºäºå¤é¡¹å¼çé«æå¤§æ´æ°ä¹æ³

å¦ææ°æ®è§æ¨¡è¾¾å°äº 1010510105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ´å¤§ï¼æ®éçé«ç²¾åº¦ä¹æ³å¯è½ä¼è¶ æ¶ï¼æ¬èå°ä»ç»ç¨å¤é¡¹å¼ä¼åæ­¤ç±»ä¹æ³çæ¹æ³ï¼

å¯¹äºä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çåè¿å¶æ´æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å°å®çä½ä¸ä¸ªæ¯ä½ç³»æ°åä¸ºæ´æ°ä¸ä¸è¶ è¿ 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤é¡¹å¼ ð´ =ð0100 +ð1101 +â¯ +ððâ110ðâ1A=a0100+a1101+â¯+anâ110nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·ï¼æä»¬å°±å°ä¸¤ä¸ªæ´æ°ä¹æ³è½¬åä¸ºäºä¸¤ä¸ªå¤é¡¹å¼ä¹æ³ï¼

æ®éçå¤é¡¹å¼ä¹æ³æ¶é´å¤æåº¦ä»æ¯ ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½å¯ä»¥ç¨å¤é¡¹å¼ä¸èä¸­ç [å¿«éå éå¶åæ¢](../poly/fft/)ã[å¿«éæ°è®ºåæ¢](../poly/ntt/) ç­ç®æ³ä¼åï¼ä¼ååçæ¶é´å¤æåº¦æ¯ ð(ðlogâ¡ð)O(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å°è£ ç±»

[è¿é](https://paste.ubuntu.com/p/7VKYzpC7dn/) æä¸ä¸ªå°è£ å¥½çé«ç²¾åº¦æ´æ°ç±»ï¼ä»¥å [è¿é](https://github.com/Baobaobear/MiniBigInteger/blob/main/bigint_tiny.h) æ¯æå¨æé¿åº¦åååè¿ç®çè¶ è¿·ä½ å®ç°ç±»ï¼

è¿éæ¯å¦ä¸ä¸ªæ¨¡æ¿

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 ``` |  ```text constexpr int MAXN = 9999 ; // MAXN æ¯ä¸ä½ä¸­æå¤§çæ°å­ constexpr int MAXSIZE = 10024 ; // MAXSIZE æ¯ä½æ° constexpr int DLEN = 4 ; // DLEN è®°å½åå ä½ struct Big { int a [ MAXSIZE ], len ; bool flag ; // æ è®°ç¬¦å·'-' Big () { len = 1 ; memset ( a , 0 , sizeof a ); flag = false ; } Big ( const int ); Big ( const char * ); Big ( const Big & ); Big & operator = ( const Big & ); Big operator \+ ( const Big & ) const ; Big operator \- ( const Big & ) const ; Big operator * ( const Big & ) const ; Big operator / ( const int & ) const ; // TODO: Big / Big; Big operator ^ ( const int & ) const ; // TODO: Big ^ Big; // TODO: Big ä½è¿ç®; int operator % ( const int & ) const ; // TODO: Big ^ Big; bool operator < ( const Big & ) const ; bool operator < ( const int & t ) const ; void print () const ; }; Big :: Big ( const int b ) { int c , d = b ; len = 0 ; // memset(a,0,sizeof a); CLR ( a ); while ( d > MAXN ) { c = d \- ( d / ( MAXN \+ 1 ) * ( MAXN \+ 1 )); d = d / ( MAXN \+ 1 ); a [ len ++ ] = c ; } a [ len ++ ] = d ; } Big :: Big ( const char * s ) { int t , k , index , l ; CLR ( a ); l = strlen ( s ); len = l / DLEN ; if ( l % DLEN ) ++ len ; index = 0 ; for ( int i = l \- 1 ; i >= 0 ; i -= DLEN ) { t = 0 ; k = i \- DLEN \+ 1 ; if ( k < 0 ) k = 0 ; g ( j , k , i ) t = t * 10 \+ s [ j ] \- '0' ; a [ index ++ ] = t ; } } Big :: Big ( const Big & T ) : len ( T . len ) { CLR ( a ); f ( i , 0 , len ) a [ i ] = T . a [ i ]; // TODO:éè½½æ­¤å¤ï¼ } Big & Big :: operator = ( const Big & T ) { CLR ( a ); len = T . len ; f ( i , 0 , len ) a [ i ] = T . a [ i ]; return * this ; } Big Big :: operator \+ ( const Big & T ) const { Big t ( * this ); int big = len ; if ( T . len > len ) big = T . len ; f ( i , 0 , big ) { t . a [ i ] += T . a [ i ]; if ( t . a [ i ] > MAXN ) { ++ t . a [ i \+ 1 ]; t . a [ i ] -= MAXN \+ 1 ; } } if ( t . a [ big ]) t . len = big \+ 1 ; else t . len = big ; return t ; } Big Big :: operator \- ( const Big & T ) const { int big ; bool ctf ; Big t1 , t2 ; if ( * this < T ) { t1 = T ; t2 = * this ; ctf = true ; } else { t1 = * this ; t2 = T ; ctf = false ; } big = t1 . len ; int j = 0 ; f ( i , 0 , big ) { if ( t1 . a [ i ] < t2 . a [ i ]) { j = i \+ 1 ; while ( t1 . a [ j ] == 0 ) ++ j ; \-- t1 . a [ j \-- ]; // WTF? while ( j > i ) t1 . a [ j \-- ] += MAXN ; t1 . a [ i ] += MAXN \+ 1 \- t2 . a [ i ]; } else t1 . a [ i ] -= t2 . a [ i ]; } t1 . len = big ; while ( t1 . len > 1 && t1 . a [ t1 . len \- 1 ] == 0 ) { \-- t1 . len ; \-- big ; } if ( ctf ) t1 . a [ big \- 1 ] = \- t1 . a [ big \- 1 ]; return t1 ; } Big Big :: operator * ( const Big & T ) const { Big res ; int up ; int te , tee ; f ( i , 0 , len ) { up = 0 ; f ( j , 0 , T . len ) { te = a [ i ] * T . a [ j ] \+ res . a [ i \+ j ] \+ up ; if ( te > MAXN ) { tee = te \- te / ( MAXN \+ 1 ) * ( MAXN \+ 1 ); up = te / ( MAXN \+ 1 ); res . a [ i \+ j ] = tee ; } else { up = 0 ; res . a [ i \+ j ] = te ; } } if ( up ) res . a [ i \+ T . len ] = up ; } res . len = len \+ T . len ; while ( res . len > 1 && res . a [ res . len \- 1 ] == 0 ) \-- res . len ; return res ; } Big Big :: operator / ( const int & b ) const { Big res ; int down = 0 ; gd ( i , len \- 1 , 0 ) { res . a [ i ] = ( a [ i ] \+ down * ( MAXN \+ 1 )) / b ; down = a [ i ] \+ down * ( MAXN \+ 1 ) \- res . a [ i ] * b ; } res . len = len ; while ( res . len > 1 && res . a [ res . len \- 1 ] == 0 ) \-- res . len ; return res ; } int Big :: operator % ( const int & b ) const { int d = 0 ; gd ( i , len \- 1 , 0 ) d = ( d * ( MAXN \+ 1 ) % b \+ a [ i ]) % b ; return d ; } Big Big :: operator ^ ( const int & n ) const { Big t ( n ), res ( 1 ); int y = n ; while ( y ) { if ( y & 1 ) res = res * t ; t = t * t ; y >>= 1 ; } return res ; } bool Big :: operator < ( const Big & T ) const { int ln ; if ( len < T . len ) return true ; if ( len == T . len ) { ln = len \- 1 ; while ( ln >= 0 && a [ ln ] == T . a [ ln ]) \-- ln ; if ( ln >= 0 && a [ ln ] < T . a [ ln ]) return true ; return false ; } return false ; } bool Big :: operator < ( const int & t ) const { Big tee ( t ); return * this < tee ; } void Big :: print () const { printf ( "%d" , a [ len \- 1 ]); gd ( i , len \- 2 , 0 ) { printf ( "%04d" , a [ i ]); } } void print ( const Big & s ) { int len = s . len ; printf ( "%d" , s . a [ len \- 1 ]); gd ( i , len \- 2 , 0 ) { printf ( "%04d" , s . a [ i ]); } } char s [ 100024 ]; ```   
---|---  
  
## ä¹ é¢

  * [NOIP 2012 å½çæ¸¸æ](https://loj.ac/problem/2603)
  * [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
  * [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
  * [UVa - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
  * [UVa - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
  * [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)

## åèèµæä¸é¾æ¥

  1. [Karatsuba algorithm - Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/30 14:50:40ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/bignum.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/bignum.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[StudyingFather](https://github.com/StudyingFather), [cbw2007](https://github.com/cbw2007), [H-J-Granger](https://github.com/H-J-Granger), [Ir1d](https://github.com/Ir1d), [Marcythm](https://github.com/Marcythm), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [countercurrent-time](https://github.com/countercurrent-time), [sshwy](https://github.com/sshwy), [ayuusweetfish](https://github.com/ayuusweetfish), [CCXXXI](https://github.com/CCXXXI), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ouuan](https://github.com/ouuan), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Xeonacid](https://github.com/Xeonacid), [383494](https://github.com/383494), [alphagocc](https://github.com/alphagocc), [AndrewWayne](https://github.com/AndrewWayne), [Baobaobear](https://github.com/Baobaobear), [c-forrest](https://github.com/c-forrest), [Chihaya-Yuka](https://github.com/Chihaya-Yuka), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [gi-b716](https://github.com/gi-b716), [Glenn-Su](https://github.com/Glenn-Su), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [justarandomstring](https://github.com/justarandomstring), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lss233](https://github.com/lss233), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [r-value](https://github.com/r-value), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [yusancky](https://github.com/yusancky)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
