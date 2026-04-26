# æ¨¡ç®æ¯ç®ä» - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/mod-arithmetic/

# æ¨¡ç®æ¯ç®ä»

ç®æ³ç«èµä¸­ï¼æ°è®ºé¨åçä¸ä¸ªéè¦ç»æé¨åå°±æ¯ **æ¨¡ç®æ¯** ï¼modular arithmeticï¼ï¼ä¹å°±æ¯å¨æä¸æ¨¡æ°ä¸è¿è¡åç§æ´æ°è¿ç®ï¼é¤äºåºç¡çååè¿ç®åæ±å¹å¤ï¼è¿å¯ä»¥æ¹ä¾¿å°è¿è¡åå¯¹æ°ãå¼åæ¬¡æ¹ãæ±é¶ä¹åç»åæ°ç­è¿ç®ï¼

æ¨¡ç®æ¯å¸¸è§äºåç±»é®é¢ä¸­ï¼èä¸ä» ä» å±éäºæ°è®ºé¨åï¼å¾å¤é®é¢çå®é ç­æ¡å¯è½éå¸¸å¤§ï¼è¶ è¿äºå¸¸è§çæ´ååéçå­å¨èå´ï¼æ­¤æ¶ï¼ä¸ºäºé¿å å¼å ¥å¤§æ´æ°è¿ç®åè¾åºé¿æ°å­ï¼é¢ç®å¸¸å¸¸è¦æ±å¯¹ç­æ¡åæ¨¡åè¾åºï¼è¿å°±è¦æ±çç»ææ¡åç±»æ¨¡ç®æ¯æå·§ï¼

## C/C++ çæ´æ°é¤æ³ååæ¨¡è¿ç®

å¨ C/C++ ä¸­ï¼æ´æ°é¤æ³ååæ¨¡è¿ç®ï¼ä¸æ°å­¦ä¸ä¹ æ¯çåæ¨¡åé¤æ³ä¸ä¸è´ï¼

å¯¹äºæææ åçæ¬ç C/C++ï¼è§å®å¨æ´æ°é¤æ³ä¸­ï¼

  1. å½é¤æ°ä¸º 0 æ¶ï¼è¡ä¸ºæªå®ä¹ï¼
  2. å¦å `(a / b) * b + a % b` çè¿ç®ç»æä¸ `a` ç¸ç­ï¼

ä¹å°±æ¯è¯´ï¼åæ¨¡è¿ç®çç¬¦å·åå³äºé¤æ³å¦ä½åæ´ï¼èé¤æ³å¦ä½åæ´ï¼è¿æ¯å®ç°å®ä¹çï¼ç±ç¼è¯å¨å³å®ï¼ï¼

ä» [C99](https://en.cppreference.com/w/c/language/operator_arithmetic) å [C++11](https://en.cppreference.com/w/cpp/language/operator_arithmetic) æ åçæ¬èµ·ï¼è§å® **ååé¶åæ´** ï¼èå¼å°æ°é¨åï¼ï¼åæ¨¡çç¬¦å·å°±ä¸è¢«é¤æ°ç¸åï¼ä»æ­¤ï¼ä»¥ä¸æ­è¨ä¿è¯ä¸ºçï¼

```text 1 2 3 4 ``` |  ```text assert ( 5 % 3 == 2 ); assert ( 5 % -3 == 2 ); assert ( -5 % 3 == -2 ); assert ( -5 % -3 == -2 ); ```   
---|---  
  
## æ¨¡æ´æ°ç±»

æ¨¡ç®æ¯å¯ä»¥çåæ¯å¯¹ææ¨¡æ°ä¸ç [åä½ç±»](../basic/#åä½ç±»ä¸å©ä½ç³») è¿è¡åç§è¿ç®ï¼å¦æç¨ä¸ä¸ªç»æä½æ¥è¡¨ç¤ºä¸ä¸ªåä½ç±»ï¼å¹¶ä¸å°åä½ç±»ä¹é´çå ãåãä¹ç­è¿ç®å°è£ ä¸ºç»æä½çæ¹æ³æè¿ç®ç¬¦éè½½ï¼é£ä¹æ¨¡ç®æ¯å°±å¯ä»¥èªç¶å°å®ç°ä¸ºä¸ä¸ªæ¨¡æ´æ°ç±»ï¼ä¸é¢ç»åºä¸ä¸ªç®åçä¾å­ï¼å®æ¯ææ¨¡æ° ð <230M<230![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¸¦ç¬¦å·æ´æ°çå æ³ãåæ³ãä¹æ³ä»¥åå¿«éå¹è¿ç®ï¼

ä¸ä¸ªç®åçæ¨¡æ´æ°ç±»

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text // A simple ModInt implementation. template < int M > struct ModInt { struct skip_mod {}; ModInt ( int v , skip_mod ) : v ( v ) {} int v ; ModInt () : v ( 0 ) {} // Initialization: find remainder. // Equivalent to: v = int((x % M + M) % M) ModInt ( long long x ) { x %= M ; if ( x < 0 ) x += M ; v = int ( x ); } // Addition. // Equivalent to: ModInt((l.v + r.v) % M) friend ModInt operator \+ ( ModInt l , ModInt r ) { int res = l . v \+ r . v ; if ( res >= M ) res -= M ; return ModInt ( res , skip_mod {}); } // Subtraction. // Equivalent to: ModInt((l.v - r.v + M) % M) friend ModInt operator \- ( ModInt l , ModInt r ) { int res = l . v \- r . v ; if ( res < 0 ) res += M ; return ModInt ( res , skip_mod {}); } // Multiplication. friend ModInt operator * ( ModInt l , ModInt r ) { return ModInt ( 1L L * l . v * r . v % M , skip_mod {}); } // Exponentiation. ModInt pow ( long long b ) const { ModInt res { 1 }, po { * this }; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * po ; po = po * po ; } return res ; } }; ```   
---|---  
  
è¿ä¸ªå®ç°ææå°åå°äºåæ¨¡è¿ç®çæ¬¡æ°ï¼å ä¸ºåæ¨¡æä½éå¸¸æ¯æ®éçå ãåãä¹ææ¯è¾è¿ç®è¦èæ¶å¾å¤ï¼ä»£ç æ³¨éä¸­æä¾äºç­ä»·ä¸æ´ä¸ºç´æ¥çå®ç°æ¹å¼ï¼è¿äºç®åä¼åçä¸»è¦æè·¯æ¯ï¼ä¸¤ä¸ª [0,ð)[0,M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å çæ´æ°åå åè¿ç®æ¶ï¼ç»æä¸å®è½å¨åºé´ ( âð,2ð)(âM,2M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ï¼å æ­¤å¯ä»¥éè¿ä¸æ¬¡å åæ³è°æ´ååºé´ [0,ð)[0,M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥å®ç°ä¸­çåå¹è¿ç®ç¨å°äº [å¿«éå¹](../../binary-exponentiation/#æ¨¡æä¹ä¸åå¹) çæå·§ï¼

é¤äºè¿äºåºç¡è¿ç®å¤ï¼è¿å¯ä»¥å¨åç§æ¨¡æ°ä¸åå¦ä¸è¿ç®ï¼

  * [éå ](../inverse/)
  * [é¤æ³](../linear-equation/)
  * [é¶ä¹](../factorial/)
  * [ç»åæ°](../lucas/)
  * [å¼å¹³æ¹](../quad-residue/#æ¨¡æä¹ä¸å¼å¹³æ¹)
  * [åå¯¹æ°](../discrete-logarithm/)
  * [å¼æ¹](../residue/#æ¨¡æä¹ä¸å¼æ¹)

è¿äºè¿ç®éå¸¸å¨ç´ æ°æ¨¡æ°ä¸æ¯è¾å®¹æï¼å¯¹äºåæ°æ¨¡æ°ï¼å¾å¾éè¦ç¨å°å¯¹åºç®æ³çæ©å±çæ¬å [ä¸­å½å©ä½å®ç](../crt/)ï¼è¿äºæ¨¡æä¹ä¸çè¿ç®å¤§å¤å¯ä»¥çä½æ±è§£æç§åä½æ¹ç¨ï¼å¯¹äºæ±è§£åä½æ¹ç¨çä¸è¬æ¹æ³ï¼å¯ä»¥åè [åä½æ¹ç¨](../congruence-equation/) é¡µé¢ï¼

## ç¸å ³ç®æ³

æ¬èå°ä»ç»å ç§å¨æ¨¡æä¹ä¸ä¼ååæ¨¡ãä¹æ³åå¿«éå¹è¿ç®çæ¹æ³ï¼å¯¹äºç»å¤§å¤æ°é¢ç®æ¥è¯´ï¼åææä¾çç®åå®ç°å·²ç»è¶³å¤é«æï¼ç¶èï¼å½é¢ç®å¯¹ç®æ³å¸¸æ°æä¸¥æ ¼è¦æ±æ¶ï¼è¿äºä¼åæ¹æ³å°±å¯ä»¥åæ¥ä½ç¨ï¼éè¿åå°ä¸å¿ è¦çè®¡ç®ååæ¨¡æä½ï¼è¿ä¸æ­¥éä½ç®æ³çæ¶é´å¼éï¼

### å¿«éä¹

å¨ç´ æ§æµè¯ä¸è´¨å æ°åè§£ä¸­ï¼ç»å¸¸ä¼éå°æ¨¡æ°å¨ `long long` èå´å çä¹æ³åæ¨¡è¿ç®ï¼ä¸ºäºé¿å è¿ç®ä¸­çæ´åæº¢åºé®é¢ï¼æ¬èä»ç»ä¸ç§å¯ä»¥å¤çæ¨¡æ°å¨ `long long` èå´å ï¼ä¸éè¦ä½¿ç¨ `__int128` ä¸å¤æåº¦ä¸º ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çãå¿«éä¹ãï¼æ¬ç®æ³è¦æ±æµè¯ç³»ç»ä¸­ï¼`long double` è³å°è¡¨ç¤ºä¸º 8080![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ©å±ç²¾åº¦æµ®ç¹æ°1ï¼

åè®¾ 0 â¤ð,ð <ð0â¤a,b<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦è®¡ç® ððmodðabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ³¨æå°ï¼

ððmodð=ððââðððâð.abmodm=abââabmâm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨ `unsigned long long` çèªç¶æº¢åºï¼

ððmodð=ððââðððâð=(ððââðððâð)mod264.abmodm=abââabmâm=(abââabmâm)mod264.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åªè¦è½ç®åºå âðððââabmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æå³ä¾§è¡¨è¾¾å¼ä¸­çä¹æ³ååæ³è¿ç®é½å¯ä»¥ä½¿ç¨ `unsigned long long` ç´æ¥è®¡ç®ï¼

æ¥ä¸æ¥ï¼åªéè¦èèå¦ä½è®¡ç® âðððââabmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è§£å³æ¹æ¡æ¯å ä½¿ç¨ `long double` ç®åº ððam![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¹ä¸ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¢ç¶ä½¿ç¨äº `long double`ï¼å°±æ çä¼æç²¾åº¦è¯¯å·®ï¼åè®¾ `long double` è¡¨ç¤ºä¸º 8080![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ©å±ç²¾åº¦æµ®ç¹æ°ï¼å³ç¬¦å·ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ææ°ä¸º 1515![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼å°¾æ°ä¸º 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ï¼é£ä¹ `long double` æå¤è½ç²¾ç¡®è¡¨ç¤ºçææä½æ°ä¸º 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2ï¼æä»¥ ððam![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå·®ä»ç¬¬ 6565![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¼å§åºéï¼è¯¯å·®èå´3ä¸º (â2â64,2â64)(â2â64,2â64)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹ä¸ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸ª 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¸¦ç¬¦å·æ´æ°ï¼è¯¯å·®èå´ä¸º ( â0.5,0.5)(â0.5,0.5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ºäºç®ååç»­è®¨è®ºï¼å¯ä»¥å å ä¸ä¸ª 0.50.5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååæ´ï¼æåçè¯¯å·®èå´æ¯ {0,1}{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æåï¼ä»£å ¥ä¸å¼è®¡ç®æ¶ï¼éè¦ä¹ä»¥ âðâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æåçè¯¯å·®èå´æ¯ {0, âð}{0,âm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ `long long` èå´å ï¼æä»¥å½ç»æ ð â[0,ð)râ[0,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç´æ¥è¿å ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åè¿å ð +ðr+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»£ç å®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 ``` |  ```text long long mul ( long long a , long long b , long long m ) { long long c = ( unsigned long long ) a * b \- ( unsigned long long )(( long double ) a / m * b \+ 0.5L ) * m ; return c < 0 ? c \+ m : c ; } ```   
---|---  
  
å¦ä»ï¼ç»å¤§å¤æ°æµè¯ç³»ç»æé å¤ç C/C++ ç¼è¯å¨å·²æ¯æ `__int128` ç±»å4ï¼å æ­¤ä¹å¯ä»¥ç´æ¥å°ä¹æ°ç±»åæåè³ `__int128` ååæ¨¡è®¡ç®ï¼

åèå®ç°

```text 1 2 3 ``` |  ```text long long mul ( long long a , long long b , long long m ) { return ( __int128 ) a * b % m ; } ```   
---|---  
  
å½ç¶ï¼`__int128` çåæ¨¡è¿ç®èæ¶å¹¶ä¸å°ï¼å¦æéè¦è¿ä¸æ­¥å¡å¸¸ï¼å¯ä»¥èèæ¥ä¸æ¥ä¸¤èä»ç»çæ¹æ³ï¼

### Barrett çº¦å

åææå°ï¼é¤æ³ååæ¨¡è¿ç®éå¸¸æ¯å ¶ä»ååè¿ç®æ´ä¸ºèæ¶ï¼ä¸ºäºåå°åæ¨¡è¿ç®çå¼éï¼æä¸äºç®æ³å¯ä»¥å¨ä¸ç´æ¥ååæ¨¡çæ åµä¸å¾å°ç¸åçç»æï¼æ¬èè¦ä»ç»ç Barrett çº¦åç®æ³å°±æ¯å ¶ä¸­ä¹ä¸ï¼

è®¾ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåºå®æ¨¡æ°ï¼åè®¾è¦å¯¹ä¸åç ð >0a>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤æ¬¡è®¡ç® ðmodðamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±å¸¦ä½é¤æ³å¯ç¥

ð§=ðmodð=ðââððâð.z=amodm=aââamâm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ³é®å¨äºåæ° âððââamâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡ç®ï¼è®¾ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æä¸ªå¸¸æ°ï¼å°±æ5

âððâ=âðð ð/ð âââðâð ðâ/ð â.âamâ=âaRm/RâââaâRmâ/Râ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æéå ð  =2ðR=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å³å¼ä¸­ âð ðââRmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥é¢å¤çï¼é¤ä»¥ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½å¯ä»¥éè¿ç§»ä½è¿ç®è¿è¡ï¼æä»¥ï¼ç¨å³å¼è®¡ç®åæ°ï¼ä» éè¦ä¸æ¬¡ä¹æ³åä¸æ¬¡ç§»ä½æä½ï¼åä»£å ¥ ðmodðamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼å°±å¾å°ææ±ä½æ°çä¼°è®¡ ð§â²zâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç°å¨åæè¿æ ·åçè¯¯å·®ï¼[åæ´å½æ°](../basic/#åæ´å½æ°) å ·ææ§è´¨ï¼å¯¹äº ð¥ >ð¦ >0x>y>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ âð¥â ââð¦â â¤âð¥ âð¦ââxâââyââ¤âxâyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼è¯¯å·®

Î=|ð§â²âð§|=ðâ£âððâââðâð ðâ/ð ââ£â¤ðâð(ð ðââð ðâ)/ð ââ¤ðâðð â.Î=|zâ²âz|=m|âamâââaâRmâ/Râ|â¤mâa(RmââRmâ)/Rââ¤mâaRâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åªè¦ ð â¤ð aâ¤R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¯å·® ÎÎ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ä¸è¶ è¿ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ð§â² â¥ð§zâ²â¥z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ä¼°è®¡å¼ ð§â²zâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªè½æ¯ ð§z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð§ +ðz+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦å¨å¾å°ä¼°è®¡å¼åï¼å¨ ð§â² â¥ðzâ²â¥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ååå»å¤ä½ç ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥ä¿è¯ç­æ¡æ­£ç¡®ï¼

å¨ Barrett çº¦åçè®¡ç®è¿ç¨ä¸­ï¼ä» ä½¿ç¨äºä¸¤æ¬¡ä¹æ³ãä¸æ¬¡ç§»ä½æä½åè³å¤ä¸¤æ¬¡åæ³ï¼å°±å®æäºæ´æ°åæ¨¡ï¼ä½æççæåå¹¶éæ¯«æ ææ¬ï¼å®é ä¸ï¼Barrett çº¦åæ¶åçä¸­é´åéé¿åº¦å¾å¾é¿äºè¾å ¥åéé¿åº¦ï¼å®¹æåç°ï¼Barrett çº¦åä¸­æ¶åçæé¿ä¸­é´åéä¸º ðâð ðâaâRmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ â(ð¥)â(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ´æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºé¿åº¦ï¼é£ä¹ï¼æ

â(ðâð ðâ)ââ(ð)+â(ð )ââ(ð).â(aâRmâ)ââ(a)+â(R)ââ(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äº ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåéè¦æ»¡è¶³æ¡ä»¶ ð <ð a<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸é¿åº¦è³å°ä¸º 2â(ð) ââ(ð)2â(a)ââ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼éè¦åæ¨¡æ¶ï¼ä¸è¬é½æ â(ð) â¤â(ð)â(m)â¤â(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼è¿ä¸ä¸­é´åéçé¿åº¦å¯è½å¤§äºè¾å ¥é¿åº¦ â(ð)â(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾å¦ï¼å¦æéè¦å° 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°å¯¹ 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°åæ¨¡ï¼å®é ä¸ä¸­é´åééè¦ 64 Ã2 â32 =9664Ã2â32=96![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ï¼

Barrett çº¦åçä¸ä¸ªåºç¨åºæ¯å°±æ¯è®¡ç®ä¹ç§¯çä½æ° ððmodðabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå ¶ä¸­ä¸ä¸ªä¹æ°åºå®ï¼æ¯å¦ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºå®æ¶ï¼å¯ä»¥éè¿

ððmodð=ððââðâðð ðâ/ð âðabmodm=abââaâbRmâ/Râm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¡ä¸ä¸æç±»ä¼¼çä¼°è®¡ï¼åªè¦é¢å¤çåº âðð ðââbRmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼å³å¯ï¼è¿ç§ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºå®çæ å½¢ææ¶ä¹ç§°ä¸º Shoup æ¨¡ä¹6ï¼

æ´ä¸ºå¸¸è§çæ å½¢æ¯ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ä¸åºå®ï¼æ­¤æ¶ï¼éè¦é¦å è®¡ç® ððab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼åå©ç¨ Barrett çº¦åå¾å° ððmodðabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾å¦ï¼å®ç°æ¨¡æä¹ä¸ä¹æ³æ¶ï¼éè¦å¯¹ 0 â¤ð,ð <ð0â¤a,b<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç® ððmodðabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼éåç ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦æ»¡è¶³ ðð <ð ab<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®åæåæï¼è®¡ç®è¿ç¨æ¶åçæé¿ä¸­é´åéé¿åº¦ä¸º 2â(ðð) ââ(ð)2â(ab)ââ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ â(ð) ââ(ð) ââ(ð)â(a)ââ(b)ââ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è¯¥é¿åº¦ä¸º 3â(ð)3â(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼å¦æè¦ç¨ Barrett çº¦åå®ç° 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°çæ¨¡ä¹ï¼ä¸­é´åééè¦ 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°ï¼è¿ä¹æ¯ Barrett çº¦åå¨ç®æ³ç«èµä¸­å®é åºç¨æ¶çä¸ä¸ªéå¶ï¼

ä½ä¸ºç¤ºä¾ï¼å©ç¨ Barrett çº¦åå®ç° 32 ä½æç¬¦å·æ´æ°æ¨¡ä¹çåèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text // Modular multiplication of int32_t using Barrett reduction. class Barrett { int32_t m ; uint64_t r ; public : Barrett ( int32_t m ) : m ( m ), r (( uint64_t )( \- m ) / m \+ 1 ) {} // Barrett reduction: a % m. int32_t reduce ( int64_t a ) const { int64_t q = ( __int128 ) a * r >> 64 ; a -= q * m ; return a >= m ? a \- m : a ; } // Modular multiplication: (a * b) % m; // Assume that 0 <= a, b < m. int32_t mul ( int32_t a , int32_t b ) const { return reduce (( int64_t ) a * b ); } }; ```   
---|---  
  
å®ç°ä¸­éè¦ç¨å° 128 ä½æ´æ°4ï¼

### Montgomery æ¨¡ä¹

Montgomery æ¨¡ä¹ç®æ³çåè½å Barrett ç®æ³ååç±»ä¼¼ï¼å®åæ ·å¯ä»¥åå°æ¨¡æ´æ°è¿ç®è¿ç¨ä¸­åæ¨¡è¿ç®çå¼éï¼ä¸åä¸¤ä¸ªç®æ³é½æ¯å¨è¿ä¼¼è®¡ç®åæ°ä¸åï¼Montgomery æ¨¡ä¹å°æææ´æ°é½æ å°å° Montgomery ç©ºé´ä¸ï¼è Montgomery ç©ºé´ä¸­çè¿ç®ç¸å¯¹å®¹æï¼è¿èéä½äºæ´ä½è®¡ç®ææ¬ï¼

è®¾æ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥æ°ï¼å¹¶éå ð  =2ð >ðR=2k>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åä½ç±» ðmodðamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºç Montgomery å½¢å¼å°±æ¯

ðð modð.aRmodm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð  âðRâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥åä½ç±» ðmodðamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®ç Montgomery å½¢å¼ ðð modðaRmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´å­å¨åå°ï¼å æ­¤ï¼å¯ä»¥å°æ´æ°è½¬æ¢ä¸º Montgomery å½¢å¼åï¼è¿è¡è¥å¹²æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿ç®ï¼åå°å¾å°ç Montgomery å½¢å¼è½¬æ¢åæ´æ°ï¼ç»ææ»æ¯æ­£ç¡®çï¼

å©ç¨ Montgomery å½¢å¼å¯ä»¥æ¹ä¾¿å°è¿è¡å¾å¤æ¨¡æ´æ°çè¿ç®ï¼ååå·²ç»è¯´æï¼æ¯è¾ä¸¤ä¸ªåä½ç±»æ¯å¦ç¸åï¼åªè¦æ¯è¾å®ä»¬ç Montgomery å½¢å¼ï¼åå ä¸º

(ð+ð)ð modð=((ðð modð)Â±(ðð modð))modð,(a+b)Rmodm=((aRmodm)Â±(bRmodm))modm,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥åä½ç±»çå æ³ãåæ³å°±å¯¹åºå®ä»¬ç Montgomery å½¢å¼çå æ³ãåæ³ï¼ä½æ¯ï¼è¦è®¡ç®åä½ç±»çä¹æ³ï¼å¹¶ä¸è½ç´æ¥å°ä¸¤ä¸ª Montgomery å½¢å¼ç¸ä¹ï¼å ä¸º

(ðð)ð modð=((ðð modð)(ðð modð)ð â1)modð,(ab)Rmodm=((aRmodm)(bRmodm)Râ1)modm,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼è®¡ç®ä¸¤ä¸ª Montgomery å½¢å¼çä¹æ³æ¶ï¼éè¦å¯¹å®ä»¬çä¹ç§¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¦ä¸ **Montgomery çº¦å** ï¼Montgomery reductionï¼æä½ï¼

REDC:ð¥â¦ð¥ð â1modð.REDC:xâ¦xRâ1modm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿ä¸æä½ï¼ä¹ç§¯ ððab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Montgomery å½¢å¼å°±æ¯ REDCâ¡((ðð modð)(ðð modð))REDCâ¡((aRmodm)(bRmodm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Montgomery çº¦åæä½æ¯ Montgomery æ¨¡ä¹çæ ¸å¿æä½ï¼

  * å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½¬æ¢ä¸ºå®ç Montgomery å½¢å¼å°±æ¯ REDCâ¡((ðmodð)(ð 2modð))REDCâ¡((amodm)(R2modm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Montgomery å½¢å¼è½¬æ¢å ðmodðamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ REDCâ¡(ðð modð)REDCâ¡(aRmodm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * æ¨¡éå  ðâ1modðaâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºç Montgomery å½¢å¼å°±æ¯ REDCâ¡((ðð modð)â1(ð 3modð))REDCâ¡((aRmodm)â1(R3modm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç°å¨è®¨è®º Montgomery çº¦åæä½ REDCREDC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå®ç°æ¹æ³ï¼å¨è®¡ç® REDCâ¡(ð¥)REDCâ¡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ»æ¯åå® 0 â¤ð¥ <ð20â¤x<m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å¯¹äºä»¥ä¸æ å½¢é½æ¯æç«çï¼å ä¸º ð  âðRâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç± [è£´èå®ç](../bezouts/)ï¼å­å¨æ´æ° ð â1,ðâ²Râ1,mâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ð ð â1+ððâ²=1.RRâ1+mmâ²=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼è®¾ ð =âð¥ðâ²/ð âq=âxmâ²/Râ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

ð¥ð â1=ð¥1âððâ²ð â¡ð¥âð¥ððâ²+ððð ð =ð¥âð(ð¥ðâ²modð )ð (modð).xRâ1=x1âmmâ²Râ¡xâxmmâ²+qmRR=xâm(xmâ²modR)R(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º 0 â¤ð¥ <ð2 <ðð 0â¤x<m2<mR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 0 â¤ð¥ðâ²modð  <ð 0â¤xmâ²modR<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥

âð<ð¥âð(ð¥ðâ²modð )ð <ð.âm<xâm(xmâ²modR)R<m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼è¿ä¸ªåå ð¥ð â1modðxRâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´è³å¤å·®ä¸ä¸ª ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦å¨åå°äºé¶æ¶ï¼åå ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥å¾å° REDCâ¡(ð¥)REDCâ¡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¡ç®è¿ä¸ªåï¼åªéè¦ä¸¤æ¬¡æ´æ°ä¹æ³ãä¸æ¬¡æ´æ°åæ³åä¸¤æ¬¡ä½æä½ï¼åå«æ¯å¯¹ ð  =2ðR=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ååé¤æ³ï¼ï¼å æ­¤ï¼Montgomery çº¦åæä½å¯ä»¥é«æè¿è¡ï¼

ä¸ºäºè¿è¡ Montgomery æ¨¡ä¹æä½ï¼éè¦é¢å¤çåºä¸ç³»åå¸¸æ°ï¼é¦å ï¼Montgomery çº¦åä¸­ä¼ç¨å° ðâ² =ðâ1modð mâ²=mâ1modR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥éè¿ ä¸æ ä»ç»ç NewtonâHensel æ¹æ³è®¡ç®ï¼å ¶æ¬¡ï¼å°ä¸åæä½å½çº¦ä¸º Montgomery çº¦åæä½æ¶ï¼è¿æ¶åè¯¸å¦ ð 2modðR2modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ ·çå¸¸æ°ï¼ä¸ºäºå¾å°å®ï¼éè¦è®¡ç®ä¸æ¬¡ ð modðRmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å®ä¸èªèº«ç¸å å°±å¾å° 2ð modð2Rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éåï¼å°å®çä½ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Montgomery å½¢å¼ï¼ç´æ¥è®¡ç®å¿«éå¹ï¼å°±å¯ä»¥å¾å° 2ðð modð =ð 2modð2kRmodm=R2modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä½ä¸ºç¤ºä¾ï¼3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æç¬¦å·æ´æ°ç Montgomery æ¨¡ä¹å®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text // Montgomery modular multiplication. // The modulus m must be odd. The constant r is 2^32. class Montgomery { int32_t m ; uint32_t mm , r2 ; public : Montgomery ( int32_t m ) : m ( m ), mm ( 1 ), r2 ( \- m ) { // Compute mm as inv(m) mod r. for ( int i = 0 ; i < 5 ; ++ i ) { mm *= 2 \- mm * m ; } // Compute r2 as r * r mod m. // If allowed to use modular operation for uint64_t, simply use: // r2 = (uint64_t)(-m) % m; r2 %= m ; r2 <<= 1 ; if ( r2 >= ( uint32_t ) m ) r2 -= m ; for ( int i = 0 ; i < 5 ; ++ i ) { r2 = mul ( r2 , r2 ); } } // Montgomery reduction: x * inv(r) % m. // Also used to transform x from Montgomery space to the normal space. int32_t reduce ( int64_t x ) { uint32_t u = ( uint32_t ) x * mm ; int32_t ans = ( x \- ( int64_t ) m * u ) >> 32 ; return ans < 0 ? ans \+ m : ans ; } // Multiplication in Montgomery space: x * y * inv(r) % m. int32_t mul ( int32_t x , int32_t y ) { return reduce (( int64_t ) x * y ); } // Transform x from the normal space to Montgomery space. int32_t init ( int32_t x ) { return mul ( x , r2 ); } }; ```   
---|---  
  
ç¸å¯¹äº Barrett çº¦åå®ç°æ¨¡æä¹ä¸ä¹æ³ï¼Montgomery æ¨¡ä¹çè®¡ç®æ¶åè½¬æ¢ãMontgomery å½¢å¼çä¹æ³ãéè½¬æ¢ç­å¤ä¸ªæ­¥éª¤ï¼å æ­¤ï¼åªæå¨è½¬æ¢åéè½¬æ¢ä¹é´çæ¨¡è¿ç®æ¬¡æ°è¶³å¤å¤æ¶ï¼è½¬æ¢åéè½¬æ¢çææ¬æå¯ä»¥æå¹³ï¼è¿èè·å¾è¾é«çæ´ä½æçï¼ä½æ¯ï¼ç±äº Montgomery æ¨¡ä¹çå®ç°è¿ç¨ä¸­åªæ¶åé¿åº¦ä¸º 2â(ð)2â(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸­é´åéï¼æä»¥å®ç°èµ·æ¥æ´ä¸ºçµæ´»ï¼ä¾å¦ï¼3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°çæ¨¡ä¹ä» éè¦ 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°çä¸­é´åéï¼æä»¥ï¼å¦æéè¦å®ç°ä¸ä¸ªæ¨¡æ´æ°ç±»ç¨äºåç§æ°è®ºè®¡ç®ï¼Montgomery æ¨¡ä¹æ´ä¸ºåéï¼

### æ¨¡ 2 çå¹æ¬¡çæ´æ°ç±»

æ¬èè®¨è®ºæ¨¡æ°æ¯ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡æ¶ï¼æ¨¡æ´æ°ç±»çå®ç°ï¼å¨è¿ä¸ç¹æ®æ å½¢ä¸­ï¼é¤æ³ååæ¨¡è¿ç®å¯ä»¥éè¿ä½æä½å®ç°ï¼è®¡ç®æçå¾é«ï¼Barrett çº¦åå Montgomery æ¨¡ä¹é½æ¯å©ç¨äº 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºé¤æ°åæ¨¡æ°æ¶çè¿ä¸ç¹æ§æ¥å éè¿ç®ï¼ç¹å«å°ï¼å½æ¨¡æ°æ°ä¸º 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ç¹æ®æ°å­æ¶ï¼å¯ä»¥å©ç¨ç¸åºä½é¿çæ ç¬¦å·æ´æ°ç»åèªç¶æº¢åºå®ç°æ¨¡æ´æ°ç±»ï¼æ éä»»ä½æ¾å¼çåæ¨¡è¿ç®ï¼å³ä½¿æ¨¡æ°å¹¶éæ°å¥½å¦æ­¤ï¼ä¹å¯ä»¥è½¬åä¸ºè¿äºç¹æ®æ¨¡æ°çæ å½¢ï¼ä¾å¦æ¨¡æ°ä¸º 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¯ä»¥å¨æ¨¡æ° 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æä¸­é´è®¡ç®ï¼æååå°ç»æå¯¹ 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼é¤äºåæ¨¡æ¹ä¾¿å¤ï¼æ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°ç±»çå ¶ä»æä½ä¹æå¾å¤ç¹æ®å®ç°ï¼æ¬èéç¹ä»ç»éå ååå¹æä½çå®ç°æ¹å¼ï¼

é¦å æ¯åéæä½ï¼ç»å®å¥æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡æ° ð =2ðÂ (ð >2)m=2eÂ (e>2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éè¦æ±åº ðâ1modðaâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±éå çå¸¸è§æ¹æ³å æ¬æ©å±æ¬§å éå¾ç®æ³åå¿«éå¹æ³ï¼æ©å±æ¬§å éå¾ç®æ³çè¿ç¨æ¶åå¯¹ä¸è¬æ¨¡æ°åæ¨¡ï¼æ®éçå¿«éå¹æ³éè¦è®¡ç® ðð(ð)â1modðaÏ(m)â1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éè¦ Î(ð)Î(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡æ´æ°ä¹æ³ï¼æ´ä¸ºé«æçæ¹æ³æ¯ [NewtonâHensel æ¹æ³](../../poly/newton/)ï¼å ·ä½å°ï¼èèåºç¨å¦ä¸ç»è®ºï¼7

ðð¥â¡1(mod2ð)â¹ðð¥(2âðð¥)â¡1(mod22ð).mxâ¡1(mod2e)â¹mx(2âmx)â¡1(mod22e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®è¿ä¸è¡¨è¾¾å¼ï¼åªè¦ä» ð¥ =1x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼åå¤åºç¨ ð¥ âð¥(2 âðð¥)xâx(2âmx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å¨ âlog2â¡ðââlog2â¡eâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡è¿­ä»£åå¾å° ðâ1modð mâ1modR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä½ä¸ºç¤ºä¾ï¼æ¨¡ 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°åéæä½åèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 ``` |  ```text // Compute 1/v mod 2^32 for odd v. uint32_t inv_mod_2_32 ( uint32_t v ) { uint32_t x = 1 ; for ( int i = 0 ; i != 5 ; ++ i ) { x *= 2 \- v * x ; } return x ; } ```   
---|---  
  
æ¥ä¸æ¥ï¼è®¨è®ºåå¹æä½ï¼ç»å® ð¥,ð,ðx,a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡æ° ð =2ðÂ (ð >2)m=2eÂ (e>2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éè¦æ±åº ð¥ððmodðxabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°ï¼æ ¹æ®å¯¹æ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°ä¹æ³ç»æç [åæ](../primitive-root/#mod-pow-2) å¯ç¥ï¼ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯å¯ä»¥åæ Â±ðâÂ±gâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼8ï¼ä¸è´å·åºç°ä¸ä» åºç°å¨ ð â¡3(mod4)aâ¡3(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å¯¹äºè¿ç§æ åµï¼å¯ä»¥å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢æ âðâa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶å°æç»ç»æåä¹ä¸ ( â1)ð(â1)b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æ¥ä¸æ¥ä¸å¦¨åè®¾ ð â¡1(mod4)aâ¡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼æ­¤æ¶ï¼ç®æ³çæ ¸å¿æ³æ³æ¯ï¼å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ ðð¿(ð)modðgL(a)modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼ç¶åç¨ ð¥ððð¿(ð)modðxgbL(a)modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç®ææ±çå¹ï¼

è®¡ç® ð¿(ð)L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è®¡ç®ç¦»æ£å¯¹æ° indðâ¡ðindgâ¡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ³¨æå°ï¼åªè¦ ð â¡1(mod4)aâ¡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»è½åæå¦ä¸å½¢å¼ï¼

ðâ¡(2ð1+1)(2ð2+1)â¯(2ðð +1)(modð),aâ¡(2e1+1)(2e2+1)â¯(2es+1)(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼1 <ð1 <ð2 <â¯ <ðð  <ð1<e1<e2<â¯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¯å ä¸ºç´æ¥å°è¿ä¸ä¹ç§¯å±å¼å¯ä»¥åç°ï¼ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºä¸­ç­äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬¡ä½ä½å°±æ¯ç¬¬ ð1e1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ä¸æ ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼ï¼ç±æ­¤å°±å¯ä»¥éå½å°æ¾å°è¿ä¸è¡¨ç¤ºï¼æ ¹æ®ç¦»æ£å¯¹æ°ç [æ§è´¨](../discrete-logarithm/#æ§è´¨) å¯ç¥ï¼æ

4ð¿(ð)â¡4ð¿(2ð1+1)+4ð¿(2ð2+1)+â¯+4ð¿(2ðð +1)(modð).4L(a)â¡4L(2e1+1)+4L(2e2+1)+â¯+4L(2es+1)(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºç¦»æ£å¯¹æ°çæ¨¡æ°ç­äºé¶ ð¿ð(ð) =2ðâ2 =ð/4Î´m(g)=2eâ2=m/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æ­¤å¤ç´æ¥å°æ´ä¸ªåä½å¼é½ä¹ä»¥ 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥ä¿è¯è®¡ç®å¯ä»¥å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å©ä½ç±»ä¸­è¿è¡ï¼ç±æ­¤ï¼åªéè¦å¯¹ 1 <ð <ð1<d<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¢å¤çåºææç 4ð¿(2ð +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å¿«éè®¡ç® 4ð¿(ð)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

åè¿æ¥ï¼ä» ð¿(ð)L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¾å®¹æå¾å° ððmodðgamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼æ ¹æ® [äºé¡¹å¼å®ç](../../combinatorics/combination/#äºé¡¹å¼å®ç) å¯ç¥ï¼å¯¹äº 1 <ð <ð1<d<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

(2ð+1)2ðâðâ¡1(modð),(2ð+1)2ðâðâ1â¡1+2ðâ1(modð),(2d+1)2eâdâ¡1(modm),(2d+1)2eâdâ1â¡1+2eâ1(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼ð¿ð(2ð +1) =2ðâðÎ´m(2d+1)=2eâd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®é¶çæ§è´¨å¯ç¥

ð¿ð(2ð+1)=ð¿ð(ð)gcd(ð¿ð(ð),indðâ¡(2ð+1)).Î´m(2d+1)=Î´m(g)gcd(Î´m(g),indgâ¡(2d+1)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼gcd(ð¿ð(ð),indðâ¡(2ð +1)) =2ðâ2gcd(Î´m(g),indgâ¡(2d+1))=2dâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æ ð¿(2ð +1) =indðâ¡(2ð +1) =2ðâ2ðL(2d+1)=indgâ¡(2d+1)=2dâ2r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼2 â¤ð2â¤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼4ð¿(2ð +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºä¸­ç­äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½ä½æ°ä¸ºç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ä¸æ ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼ï¼å æ­¤ï¼åæ ·å¯ä»¥éè¿äºè¿å¶è¡¨ç¤ºéå½å°å° 4ð¿(ð)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸ºå½¢å¦ 4ð¿(2ð +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåï¼ç±æ­¤ï¼å°±å¯ä»¥å¾å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

å ·ä½å®ç°æ¶ï¼æä¸äºå¯ä»¥è¿ä¸æ­¥ä¼åçç¹ï¼é¦å ï¼å° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸ºä¹ç§¯å½¢å¼æ¶ï¼è¿æ¯éè¦ç¨å°é¤æ³ï¼æ´æ¹ä¾¿çæ¯è®¡ç® ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåè§£ï¼å³å¯»æ¾ 1 <ð1 <ð2 <â¯ <ðð  <ð1<e1<e2<â¯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ð(2ð1+1)(2ð2+1)â¯(2ðð +1)â¡1(modð)a(2e1+1)(2e2+1)â¯(2es+1)â¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼åæ ·æ¯éè¿å¯»æ¾ç­äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬¡ä½ä½æ¥ç¡®å® ð1e1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯è¦å¨ ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ¶å» 2ð1 +12e1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­ï¼åªéè¦å¨ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¹ä»¥ 2ð1 +12e1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼è¿å¯ä»¥éè¿ä½æä½è¿è¡ï¼åå ä¸º 4ð¿(ðâ1) = â4ð¿(ð)4L(aâ1)=â4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç»è®¡ 4ð¿(ð)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼éè¦ç¨åæ³ä»£æ¿å æ³ï¼å ¶æ¬¡ï¼å¯¹äºç¹æ®éæ©çåºåº ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿­ä»£æ éè¿è¡å° ð =ð â1d=eâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èåªè¦è¿è¡å° ð =âð/2â â1d=âe/2ââ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼ä¸ºæ­¤ï¼éè¦éæ© ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

4ð¿(2âð/2â+1)=2âð/2â.4L(2âe/2â+1)=2âe/2â.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äº ð â¥ð/2dâ¥e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

(2ð+1)2=22ð+2ð+1+1â¡2ð+1+1(modð).(2d+1)2=22d+2d+1+1â¡2d+1+1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼ä» ð =âð/2âd=âe/2â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§å½çº³å¯ç¥ï¼ð¿(2ð +1) =2ðL(2d+1)=2d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð â¥ð/2dâ¥e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼è¿èï¼åªè¦ ð/2 â¤ð1 <ð2 <â¯ <ðð  <ðe/2â¤e1<e2<â¯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

(2ð1+1)(2ð2+1)â¯(2ðð +1)â¡1+2ð1+2ð2+â¯+2ðð (modð)(2e1+1)(2e2+1)â¯(2es+1)â¡1+2e1+2e2+â¯+2es(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¥å

4ð¿((2ð1+1)(2ð2+1)â¯(2ðð +1))=2ð1+2ð2+â¯+2ðð .4L((2e1+1)(2e2+1)â¯(2es+1))=2e1+2e2+â¯+2es.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼å¤çå®ææ ð <ð/2d<e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶ä½åï¼å¯ä»¥ç´æ¥å¾å°å©ä½é¨åçç¦»æ£å¯¹æ°ï¼èæ ééä½è®¡ç®ï¼åºç¨ç¬¬ä¸ä¸ªä¼ååï¼æ´ä¸ªåå¹æä½åªéè¦ ð(ð)O(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å åæ³åä½æä½å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³æä½ï¼åºç¨ç¬¬äºä¸ªä¼ååï¼å¯ä»¥çå»çº¦ä¸åçå åæ³åä½æä½ï¼ä½éè¦é¢å¤ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³æä½ï¼

ä½ä¸ºç¤ºä¾ï¼æ¨¡ 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°åå¹æä½åèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` |  ```text // Store 4L(a) for a = 2^d + 1, where L(a) is disc. log. base 388251981. // The first two values are never used and thus set to zero. // The base is chosen such that 4L(2^16+1) = 2^16. constexpr uint32_t log_table [ 16 ] = { 0x00000000 , 0x00000000 , 0xbba0267c , 0x49b9d1e8 , 0xf0026f90 , 0xd6e17e20 , 0xe78bf840 , 0x039fe080 , 0xaf7f8100 , 0x60fe0200 , 0xd1f80400 , 0x23e00800 , 0x47801000 , 0x8e002000 , 0x18004000 , 0x20008000 , }; // Compute 4L(v). uint32_t log_mod_2_32 ( uint32_t x , uint32_t v ) { for ( int i = 2 ; i != 16 ; ++ i ) { if (( v >> i ) & 1 ) { v += v << i ; x -= log_table [ i ]; } } x += v ^ 1 ; return x ; } // Compute x*a for 4L(a) = v. uint32_t exp_mod_2_32 ( uint32_t x , uint32_t v ) { for ( int i = 2 ; i != 16 ; ++ i ) { if (( v >> i ) & 1 ) { x += x << i ; v -= log_table [ i ]; } } x *= v ^ 1 ; return x ; } // Compute x*a^b for odd a. uint32_t pow_odd_mod_2_32 ( uint32_t a , uint32_t b , uint32_t x ) { if ( a & 2 ) { a = \- a ; if ( b & 1 ) { x = \- x ; } } return exp_mod_2_32 ( x , log_mod_2_32 ( 0 , a ) * b ); } // Compute x*a^b mod 2^32. uint32_t pow_mod_2_32 ( uint32_t a , uint32_t b , uint32_t x = 1 ) { if ( ! a ) return b == 0 ? x : 0 ; auto d = __builtin_ctz ( a ); if (( uint64_t ) d * b >= 32 ) return 0 ; return pow_odd_mod_2_32 ( a >> d , b , x ) << ( d * b ); } ```   
---|---  
  
ç¦»æ£å¯¹æ°çé¢å¤çå¯ä»¥éè¿ PohligâHellman ç®æ³è¿è¡ï¼åºåº ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥éæ©ä¸º

5ind5â¡(2âð/2â)/2âð/2ââ2mod2ð.5ind5â¡(2âe/2â)/2âe/2ââ2mod2e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## åèèµæä¸æ³¨é

  * [Fast modular multiplication by orz - Codeforces](https://codeforces.com/blog/entry/96759)
  * [Barrett Reduction - Wikipedia](https://en.wikipedia.org/wiki/Barrett_reduction)
  * [Barrett Reduction - A41](https://encrypt.a41.io/primitives/modular-arithmetic/modular-reduction/barrett-reduction#cost-analysis-of-modular-multiplication)
  * [Barrett çº¦ååçåæ­£ç¡®æ§è¯æ by Chen - ç¥ä¹ä¸æ ](https://zhuanlan.zhihu.com/p/690876166)
  * [Montgomery Multiplication - CP Algorithms](https://cp-algorithms.com/algebra/montgomery_multiplication.html)
  * [Montgomery æ¨¡ä¹ by Chen - ç¥ä¹ä¸æ ](https://zhuanlan.zhihu.com/p/645428404)
  * [Binary Exponentiation by Factoring - CP Algorithms](https://cp-algorithms.com/algebra/factoring-exp.html)
  * Barrett, Paul. "Implementing the Rivest Shamir and Adleman public key encryption algorithm on a standard digital signal processor." In Conference on the Theory and Application of Cryptographic Techniques, pp. 311-323. Berlin, Heidelberg: Springer Berlin Heidelberg, 1986.
  * Becker, Hanno, Vincent Hwang, Matthias J. Kannwischer, Bo-Yin Yang, and Shang-Yi Yang. "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1." IACR Transactions on Cryptographic Hardware and Embedded Systems (2022): 221-244.
  * Montgomery, Peter L. "Modular multiplication without trial division." Mathematics of computation 44, no. 170 (1985): 519-521.

* * *

  1. è¿éç¨äºå¤§å¤æ° 64 ä½ç³»ç»ä¸ç GCC æ Clang ç¼è¯å¨ï¼Â â©

  2. åè§ [Double-precision floating-point format - Wikipedia](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)ï¼Â â©

  3. æ­¤å¤ç¨å°äºæ¡ä»¶ ð <ða<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð/ð â[0,1)a/mâ[0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Â â©

  4. å¨ç®åçä¸»æµç¼è¯ç¯å¢ä¸­ï¼åªæ Windows å¹³å°ä¸ç MSVC ä¸æ¯æ `__int128` ç±»åï¼è¥éè¦ç¼åå¯å¨å¤å¹³å°ä¸å ¼å®¹çä»£ç ï¼å¯ä»¥éè¿å® `_MSC_VER` æ£æµ MSVC ç¼è¯ç¯å¢ï¼å¹¶å¨è¯¥æ¡ä»¶ä¸å å« [`<intrin.h>`](https://learn.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list?view=msvc-170) å¤´æä»¶ï¼å©ç¨å ¶æä¾çå å»ºå½æ°ï¼å¦ `_umul128` ç­ï¼æ¥é´æ¥å®ç° 128 ä½æ´æ°è¿ç®ï¼ä» å¨ 64 ä½å¹³å°ä¸å¯ç¨ï¼ï¼Â â©â©

  5. æ­¤å¤ âððâârmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¯ä»¥æ¿æ¢æ ððrm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¶ä»æ´æ°ä¼°è®¡ï¼ä¾å¦ä¸åæ´å½æ° âððâârmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååèäºå ¥åæ´å½æ° âððâârmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ï¼åªè¦ç¸åºå°è°æ´å¯¹ä¼°è®¡å¼çè¯¯å·®ä¿®æ­£æ­¥éª¤ï¼Â â©

  6. Shoup å¨ä»çæ°è®ºè®¡ç®åº [NTL](https://libntl.org/) ä¸­å®ç°äº Barrett çº¦åçè¿ä¸æ©å±ï¼å æ­¤å¾åï¼Â â©

  7. ç´æ¥éªè¯ï¼ç± ðð¥ â¡1(mod2ð)mxâ¡1(mod2e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è®¾ ðð¥ =1 +ð2ðmx=1+Î»2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å°±æ ðð¥(2 âðð¥) =(1 +ð2ð)(1 âð2ð) =1 âð222ð â¡1(mod22ð)mx(2âmx)=(1+Î»2e)(1âÎ»2e)=1âÎ»222eâ¡1(mod22e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Â â©

  8. æä¸­æå¼é¡µé¢ä» è¯æäº ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥å 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®é ä¸ï¼å®å ¨éå¤è¯¥è¯æï¼å¯ä»¥è¯´æ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åä»»ä½æ¨¡ 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°ï¼åæä¼è®¨è®º ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåæ¹æ³ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/mod-arithmetic.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/mod-arithmetic.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[c-forrest](https://github.com/c-forrest), [HeRaNO](https://github.com/HeRaNO), [Tiphereth-A](https://github.com/Tiphereth-A), [383494](https://github.com/383494), [buuzzing](https://github.com/buuzzing), [cr4c1an](https://github.com/cr4c1an), [Emp7iness](https://github.com/Emp7iness), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [jifbt](https://github.com/jifbt), [Kaiser-Yang](https://github.com/Kaiser-Yang), [Koishilll](https://github.com/Koishilll), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [Qiu-Quanzhi](https://github.com/Qiu-Quanzhi), [Saisyc](https://github.com/Saisyc), [sshwy](https://github.com/sshwy), [StarryReverie](https://github.com/StarryReverie), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [xyf007](https://github.com/xyf007)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
