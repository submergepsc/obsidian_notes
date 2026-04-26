# æå¤§å¬çº¦æ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/gcd/

# æå¤§å ¬çº¦æ°

## å®ä¹

æå¤§å ¬çº¦æ°å³ä¸º Greatest Common Divisorï¼å¸¸ç¼©åä¸º gcdï¼

ä¸ç»æ´æ°çå ¬çº¦æ°ï¼æ¯æåæ¶æ¯è¿ç»æ°ä¸­æ¯ä¸ä¸ªæ°ççº¦æ°çæ°ï¼Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä»»æä¸ç»æ´æ°çå ¬çº¦æ°ï¼

ä¸ç»æ´æ°çæå¤§å ¬çº¦æ°ï¼æ¯æææå ¬çº¦æ°éé¢æå¤§çä¸ä¸ªï¼

å¯¹ä¸å ¨ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å ¶æå¤§å ¬çº¦æ°è®°ä¸º gcd(ð,ð)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¼èµ·æ­§ä¹æ¶å¯ç®åä¸º (ð,ð)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹ä¸å ¨ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ð1,â¦,ðða1,â¦,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å ¶æå¤§å ¬çº¦æ°è®°ä¸º gcd(ð1,â¦,ðð)gcd(a1,â¦,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¼èµ·æ­§ä¹æ¶å¯ç®åä¸º (ð1,â¦,ðð)(a1,â¦,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æå¤§å ¬çº¦æ°ä¸æå°å ¬åæ°çæ§è´¨è§ [æ°è®ºåºç¡](../basic/#æå¤§å)ï¼

é£ä¹å¦ä½æ±æå¤§å ¬çº¦æ°å¢ï¼æä»¬å èèä¸¤ä¸ªæ°çæ åµï¼

### æ¬§å éå¾ç®æ³

#### è¿ç¨

å¦ææä»¬å·²ç¥ä¸¤ä¸ªæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ä½æ±åºäºè çæå¤§å ¬çº¦æ°å¢ï¼

ä¸å¦¨è®¾ ð >ða>b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æä»¬åç°å¦æ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ï¼é£ä¹ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯äºè çæå¤§å ¬çº¦æ°ï¼ ä¸é¢è®¨è®ºä¸è½æ´é¤çæ åµï¼å³ ð =ð Ãð +ða=bÃq+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð <ðr<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æä»¬éè¿è¯æå¯ä»¥å¾å° gcd(ð,ð) =gcd(ð,ðmodð)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ç¨å¦ä¸ï¼

è¯æ

è®¾ ð =ðð +ða=bk+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶æ ð =ðmodðc=amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ ð â£ð,Â ð â£ðdâ£a,Â dâ£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð =ð âðð,ðð =ðð âðððc=aâbk,cd=adâbdk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±å³è¾¹çå¼å­å¯ç¥ ððcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ´æ°ï¼å³ ð â£ðdâ£c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥å¯¹äº ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬çº¦æ°ï¼å®ä¹ä¼æ¯ ð,ðmodðb,amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬çº¦æ°ï¼

åè¿æ¥ä¹éè¦è¯æï¼

è®¾ ð â£ð,Â ð â£(ðmodð)dâ£b,Â dâ£(amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬è¿æ¯å¯ä»¥åä¹åä¸æ ·å¾å°ä»¥ä¸å¼å­ ðmodðð =ðð âððð,Â ðmodðð +ððð =ððamodbd=adâbdk,Â amodbd+bdk=ad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å ä¸ºå·¦è¾¹å¼å­æ¾ç¶ä¸ºæ´æ°ï¼æä»¥ ððad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ºæ´æ°ï¼å³ ð â£ðdâ£a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ð,ðmodðb,amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬çº¦æ°ä¹æ¯ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬çº¦æ°ï¼

æ¢ç¶ä¸¤å¼å ¬çº¦æ°é½æ¯ç¸åçï¼é£ä¹æå¤§å ¬çº¦æ°ä¹ä¼ç¸åï¼

æä»¥å¾å°å¼å­ gcd(ð,ð) =gcd(ð,ðmodð)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¢ç¶å¾å°äº gcd(ð,ð) =gcd(ð,ð)gcd(a,b)=gcd(b,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éä¸¤ä¸ªæ°çå¤§å°æ¯ä¸ä¼å¢å¤§çï¼é£ä¹æä»¬ä¹å°±å¾å°äºå ³äºä¸¤ä¸ªæ°çæå¤§å ¬çº¦æ°çä¸ä¸ªéå½æ±æ³ï¼

#### å®ç°

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text // Version 1 int gcd ( int a , int b ) { if ( b == 0 ) return a ; return gcd ( b , a % b ); } // Version 2 int gcd ( int a , int b ) { return b == 0 ? a : gcd ( b , a % b ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text // Version 1 public int gcd ( int a , int b ) { if ( b == 0 ) return a ; return gcd ( b , a % b ); } // Version 2 public int gcd ( int a , int b ) { return b == 0 ? a : gcd ( b , a % b ); } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text def gcd ( a , b ): if b == 0 : return a return gcd ( b , a % b ) ```   
---|---  
  
éå½è³ `b == 0`ï¼å³ä¸ä¸æ­¥ç `a % b == 0`ï¼çæ åµåè¿åå¼å³å¯ï¼

æ ¹æ®ä¸è¿°éå½æ±æ³ï¼æä»¬ä¹å¯ä»¥ååºä¸ä¸ªè¿­ä»£æ±æ³ï¼

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text int gcd ( int a , int b ) { while ( b != 0 ) { int tmp = a ; a = b ; b = tmp % b ; } return a ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text public int gcd ( int a , int b ) { while ( b != 0 ) { int tmp = a ; a = b ; b = tmp % b ; } return a ; } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text def gcd ( a , b ): while b != 0 : a , b = b , a % b return a ```   
---|---  
  
ä¸è¿°ç®æ³é½å¯è¢«ç§°ä½æ¬§å éå¾ç®æ³ï¼Euclidean algorithmï¼ï¼

å¦å¤ï¼å¯¹äº C++17ï¼æä»¬å¯ä»¥ä½¿ç¨ [`<numeric>`](https://en.cppreference.com/w/cpp/header/numeric) å¤´ä¸­ç [`std::gcd`](https://en.cppreference.com/w/cpp/numeric/gcd) ä¸ [`std::lcm`](https://en.cppreference.com/w/cpp/numeric/lcm) æ¥æ±æå¤§å ¬çº¦æ°åæå°å ¬åæ°ï¼

æ³¨æ

å¨é¨åç¼è¯å¨ä¸­ï¼C++14 ä¸­å¯ä»¥ç¨ `std::__gcd(a,b)` å½æ°æ¥æ±æå¤§å ¬çº¦æ°ï¼ä½æ¯å ¶ä» ä½ä¸º `std::rotate` çç§æè¾ å©å½æ°ï¼1ä½¿ç¨è¯¥å½æ°å¯è½ä¼å¯¼è´é¢æä¹å¤çé®é¢ï¼æ ä¸è¬æ åµä¸ä¸æ¨èä½¿ç¨ï¼

å¦æä¸¤ä¸ªæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ gcd(ð,ð) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬ç§° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè´¨ï¼

#### æ§è´¨

æ¬§å éå¾ç®æ³çæ¶é´æçå¦ä½å¢ï¼ä¸é¢æä»¬è¯æï¼å¨è¾å ¥ä¸ºä¸¤ä¸ªé¿ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶æ´æ°æ¶ï¼æ¬§å éå¾ç®æ³çæ¶é´å¤æåº¦ä¸º ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼æ¢å¥è¯è¯´ï¼å¨é»è®¤ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¶çæ åµä¸ï¼æ¶é´å¤æåº¦ä¸º ð(logâ¡max(ð,ð))O(logâ¡max(a,b))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

è¯æ

å½æä»¬æ± gcd(ð,ð)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶åï¼ä¼éå°ä¸¤ç§æ åµï¼

  * ð <ða<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¶å gcd(ð,ð) =gcd(ð,ð)gcd(a,b)=gcd(b,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * ð â¥ðaâ¥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¶å gcd(ð,ð) =gcd(ð,ðmodð)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯¹ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ä¼è®© ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å°æåï¼è¿æå³çè¿ä¸è¿ç¨æå¤åç ð(logâ¡ð) =ð(ð)O(logâ¡a)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼

ç¬¬ä¸ç§æ åµåçåä¸å®ä¼åçç¬¬äºç§æ åµï¼å æ­¤ç¬¬ä¸ç§æ åµçåçæ¬¡æ°ä¸å® **ä¸å¤äº** ç¬¬äºç§æ åµçåçæ¬¡æ°ï¼

ä»èæä»¬æå¤éå½ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å°±å¯ä»¥å¾åºç»æï¼

äºå®ä¸ï¼åå¦æä»¬è¯çç¨æ¬§å éå¾ç®æ³å»æ± [ææ³¢é£å¥æ°å](../../combinatorics/fibonacci/) ç¸é»ä¸¤é¡¹çæå¤§å ¬çº¦æ°ï¼ä¼è®©è¯¥ç®æ³è¾¾å°æåå¤æåº¦ï¼

### æ´ç¸åææ¯

å¤§æ´æ°åæ¨¡çæ¶é´å¤æåº¦è¾é«ï¼èå åæ³æ¶é´å¤æåº¦è¾ä½ï¼éå¯¹å¤§æ´æ°ï¼æä»¬å¯ä»¥ç¨å åä»£æ¿ä¹é¤æ±åºæå¤§å ¬çº¦æ°ï¼

#### è¿ç¨

å·²ç¥ä¸¤æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± gcd(ð,ð)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸å¦¨è®¾ ð â¥ðaâ¥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¥ ð =ða=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å gcd(ð,ð) =ð =ðgcd(a,b)=a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ å¦åï¼âð â£ð,ð â£ðâdâ£a,dâ£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è¯æ ð â£ð âðdâ£aâb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å æ­¤ï¼ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ææ** å ¬å æ°é½æ¯ ð âðaâb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬å æ°ï¼gcd(ð,ð) =gcd(ð âð,ð)gcd(a,b)=gcd(aâb,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### Stein ç®æ³çä¼å

å¦æ ð â«ðaâ«b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´ç¸åææ¯ç ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤æåº¦å°ä¼è¾¾å°æåæ åµï¼

èèä¸ä¸ªä¼åï¼è¥ 2 â£ð,2 â£ð2â£a,2â£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼gcd(ð,ð) =2gcd(ð2,ð2)gcd(a,b)=2gcd(a2,b2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦åï¼è¥ 2 â£ð2â£a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼2 â£ð2â£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçï¼ï¼å ä¸º 2 â£ð2â£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµå·²ç»è®¨è®ºè¿äºï¼æä»¥ 2 â¤ð2â¤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ gcd(ð,ð) =gcd(ð2,ð)gcd(a,b)=gcd(a2,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¼ååçç®æ³ï¼å³ Stein ç®æ³ï¼æ¶é´å¤æåº¦æ¯ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è¥ 2 â£ð2â£a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ 2 â£ð2â£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯æ¬¡éå½è³å°ä¼å° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ååï¼

å¦åï¼2 â£ð âð2â£aâb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå°äºä¸ä¸ç§æ åµï¼

ç®æ³æå¤éå½ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼

#### å®ç°

é«ç²¾åº¦æ¨¡æ¿è§ [é«ç²¾åº¦è®¡ç®](../../bignum/)ï¼

é«ç²¾åº¦è¿ç®éå®ç°ï¼åæ³ãå¤§å°æ¯è¾ãå·¦ç§»ãå³ç§»ï¼å¯ç¨ä½ç²¾ä¹é¤ä»£æ¿ï¼ãäºè¿å¶æ«ä½ 0 çä¸ªæ°ï¼å¯ä»¥éè¿å¤æ­å¥å¶æ´åè®¡ç®ï¼ï¼

C++

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text Big gcd ( Big a , Big b ) { if ( a == 0 ) return b ; if ( b == 0 ) return a ; // è®°å½aåbçå ¬å æ°2åºç°æ¬¡æ°ï¼countr_zeroè¡¨ç¤ºäºè¿å¶æ«ä½0çä¸ªæ° int atimes = countr_zero ( a ); int btimes = countr_zero ( b ); int mintimes = min ( atimes , btimes ); a >>= atimes ; for (;;) { // aåbå ¬å æ°ä¸­ç2å·²ç»è®¡ç®è¿äºï¼åé¢ä¸å¯è½åºç°aä¸ºå¶æ°çæ åµ b >>= btimes ; // ç¡®ä¿ a<=b if ( a > b ) swap ( a , b ); b -= a ; if ( b == 0 ) break ; btimes = countr_zero ( b ); } return a << mintimes ; } ```   
---|---  
  
ä¸è¿°ä»£ç åèäº [libstdc++](https://github.com/gcc-mirror/gcc/blob/1667962ae755db27965778b8c8c684c6c0c4da21/libstdc%2B%2B-v3/include/std/numeric#L173) å [MSVC](https://github.com/microsoft/STL/blob/9aca22477df4eed3222b4974746ee79129eb44e7/stl/inc/numeric#L591) å¯¹ C++17 `std::gcd` çå®ç°ï¼å¨ `unsigned int` å `unsigned long long` çæ°æ®èå´ä¸ï¼å¦æå¯ä»¥ä»¥æå¿«çéåº¦è®¡ç® `countr_zero`ï¼å Stein ç®æ³æ¯æ¬§å éå¾ç®æ³æ¥å¾å¿«ï¼ä½åä¹åå¯è½æ¯æ¬§å éå¾ç®æ³æ ¢ï¼

å ³äº countr_zero

  1. gcc æ [å å»ºå½æ°](../../bit/#gcc-å) `__builtin_ctz`ï¼32 ä½ï¼æ `__builtin_ctzll`ï¼64 ä½ï¼å¯æ¿æ¢ä¸è¿°ä»£ç ç `countr_zero`ï¼
  2. ä» C++20 å¼å§ï¼å¤´æä»¶ `<bit>` å å«äº [`std::countr_zero`](https://en.cppreference.com/w/cpp/numeric/countr_zero)ï¼
  3. å¦æä¸ä½¿ç¨ä¸å¨æ ååºçå½æ°ï¼åæ æ³ä½¿ç¨ C++20 æ åï¼ä¸é¢çä»£ç æ¯ä¸ç§å¨ Word-RAM with multiplication æ¨¡åä¸ç»è¿é¢å¤çå ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå®ç°ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text constexpr int loghash [ 64 ] = { 0 , 32 , 48 , 56 , 60 , 62 , 63 , 31 , 47 , 55 , 59 , 61 , 30 , 15 , 39 , 51 , 57 , 28 , 46 , 23 , 43 , 53 , 58 , 29 , 14 , 7 , 35 , 49 , 24 , 44 , 54 , 27 , 45 , 22 , 11 , 37 , 50 , 25 , 12 , 38 , 19 , 41 , 52 , 26 , 13 , 6 , 3 , 33 , 16 , 40 , 20 , 42 , 21 , 10 , 5 , 34 , 17 , 8 , 36 , 18 , 9 , 4 , 2 , 1 }; int countr_zero ( unsigned long long x ) { return loghash [( x & \- x ) * 0x9150D32D8EB9EFC0U i64 >> 58 ]; } ```   
---|---  
  
èå¯¹äºé«ç²¾åº¦è¿ç®ï¼å¦æå®ç°æ¹æ³ç±»ä¼¼ `bitset`ï¼åæ­é ä¸è¿°å¯¹ `countr_zero` çå®ç°å¯ä»¥å¨ `O(n / w)` çæ¶é´å¤æåº¦ä¸å®æï¼ä½å¦æä¸ä¾¿æäºè¿å¶ä½æåï¼ååªè½æ´åå¤æ­æå¤§ç 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹å å­ï¼æ¶é´å¤æåº¦åå³äºå®ç°ï¼æ¯å¦ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text // ä»¥å°ç«¯åºå®ç°çäºè¿å¶ Bigï¼è¦æ±è½æä¸¾æ¯ä¸ä¸ªå ç´ int countr_zero ( Big a ) { int ans = 0 ; for ( auto x : a ) { if ( x != 0 ) { ans += 32 ; // æ¯ä¸ä½æ°æ®ç±»åçä½é¿ } else { return ans \+ countr_zero ( x ); } } return ans ; } // æ´åè®¡ç®ï¼å¦éä½¿ç¨å»ºè®®ç´æ¥åè¿ gcd å å¿«å¸¸æ° int countr_zero ( Big a ) { int ans = 0 ; while (( a & 1 ) == 0 ) { a >>= 1 ; ++ ans ; } return ans ; } ```   
---|---  
  
æ´å¤å ³äº `gcd` å®ç°ä¸å¿«æ ¢çè®¨è®ºå¯é è¯» [Fastest way to compute the greatest common divisor](https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/)ï¼

### å¤ä¸ªæ°çæå¤§å ¬çº¦æ°

é£æä¹æ±å¤ä¸ªæ°çæå¤§å ¬çº¦æ°å¢ï¼æ¾ç¶ç­æ¡ä¸å®æ¯æ¯ä¸ªæ°ççº¦æ°ï¼é£ä¹ä¹ä¸å®æ¯æ¯ç¸é»ä¸¤ä¸ªæ°ççº¦æ°ï¼æä»¬éç¨å½çº³æ³ï¼å¯ä»¥è¯æï¼æ¯æ¬¡ååºä¸¤ä¸ªæ°æ±åºç­æ¡ååæ¾åå»ï¼ä¸ä¼å¯¹æéè¦çç­æ¡é æå½±åï¼

## æå°å ¬åæ°

æ¥ä¸æ¥æä»¬ä»ç»å¦ä½æ±è§£æå°å ¬åæ°ï¼Least Common Multiple, LCMï¼ï¼

### å®ä¹

ä¸ç»æ´æ°çå ¬åæ°ï¼æ¯æåæ¶æ¯è¿ç»æ°ä¸­æ¯ä¸ä¸ªæ°çåæ°çæ°ï¼0 æ¯ä»»æä¸ç»æ´æ°çå ¬åæ°ï¼

ä¸ç»æ´æ°çæå°å ¬åæ°ï¼æ¯ææææ­£çå ¬åæ°éé¢ï¼æå°çä¸ä¸ªæ°ï¼

å¯¹æ´æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å ¶æå°å ¬åæ°è®°ä¸º lcmâ¡(ð,ð)lcmâ¡(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¼èµ·æ­§ä¹æ¶å¯ç®åä¸º [ð,ð][a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹æ´æ° ð1,â¦,ðða1,â¦,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å ¶æå°å ¬åæ°è®°ä¸º lcmâ¡(ð1,â¦,ðð)lcmâ¡(a1,â¦,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¼èµ·æ­§ä¹æ¶å¯ç®åä¸º [ð1,â¦,ðð][a1,â¦,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### ä¸¤ä¸ªæ°

è®¾ ð =ððð11ððð22â¯ðððð ð a=p1ka1p2ka2â¯pskas![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð =ððð11ððð22â¯ðððð ð b=p1kb1p2kb2â¯pskbs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬åç°ï¼å¯¹äº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼äºè çæå¤§å ¬çº¦æ°ç­äº

ðmin(ðð1,ðð1)1ðmin(ðð2,ðð2)2â¯ðmin(ððð ,ððð )ð p1min(ka1,kb1)p2min(ka2,kb2)â¯psmin(kas,kbs)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æå°å ¬åæ°ç­äº

ðmax(ðð1,ðð1)1ðmax(ðð2,ðð2)2â¯ðmax(ððð ,ððð )ð p1max(ka1,kb1)p2max(ka2,kb2)â¯psmax(kas,kbs)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äº ðð +ðð =max(ðð,ðð) +min(ðð,ðð)ka+kb=max(ka,kb)+min(ka,kb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥å¾å°ç»è®ºæ¯ gcd(ð,ð) Ãlcmâ¡(ð,ð) =ð Ãðgcd(a,b)Ãlcmâ¡(a,b)=aÃb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦æ±ä¸¤ä¸ªæ°çæå°å ¬åæ°ï¼å æ±åºæå¤§å ¬çº¦æ°å³å¯ï¼

### å¤ä¸ªæ°

å¯ä»¥åç°ï¼å½æä»¬æ±åºä¸¤ä¸ªæ°ç gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ±æå°å ¬åæ°æ¯ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤æåº¦ï¼é£ä¹å¯¹äºå¤ä¸ªæ°ï¼æä»¬å ¶å®æ²¡æå¿ è¦æ±ä¸ä¸ªå ±åçæå¤§å ¬çº¦æ°åå»å¤çï¼æç´æ¥çæ¹æ³å°±æ¯ï¼å½æä»¬ç®åºä¸¤ä¸ªæ°ç gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æè®¸å¨æ±å¤ä¸ªæ°ç gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶åï¼æä»¬å°å®æ¾å ¥åºåå¯¹åé¢çæ°ç»§ç»­æ±è§£ï¼é£ä¹ï¼æä»¬è½¬æ¢ä¸ä¸ï¼ç´æ¥å°æå°å ¬åæ°æ¾å ¥åºåå³å¯ï¼

## æ©å±æ¬§å éå¾ç®æ³

æ©å±æ¬§å éå¾ç®æ³ï¼Extended Euclidean algorithm, EXGCDï¼ï¼å¸¸ç¨äºæ± ðð¥ +ðð¦ =gcd(ð,ð)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç»å¯è¡è§£ï¼

### è¿ç¨

è®¾

ðð¥1 +ðð¦1 =gcd(ð,ð)ax1+by1=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ðð¥2 +(ðmodð)ð¦2 =gcd(ð,ðmodð)bx2+(amodb)y2=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ¬§å éå¾å®çå¯ç¥ï¼gcd(ð,ð) =gcd(ð,ðmodð)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ ðð¥1 +ðð¦1 =ðð¥2 +(ðmodð)ð¦2ax1+by1=bx2+(amodb)y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå ä¸º ðmodð =ð â(âððâ Ãð)amodb=aâ(âabâÃb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ ðð¥1 +ðð¦1 =ðð¥2 +(ð â(âððâ Ãð))ð¦2ax1+by1=bx2+(aâ(âabâÃb))y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ðð¥1 +ðð¦1 =ðð¦2 +ðð¥2 ââððâ Ãðð¦2 =ðð¦2 +ð(ð¥2 ââððâð¦2)ax1+by1=ay2+bx2ââabâÃby2=ay2+b(x2ââabây2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð =ð,ð =ða=a,b=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ð¥1 =ð¦2,ð¦1 =ð¥2 ââððâð¦2x1=y2,y1=x2ââabây2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å° ð¥2,ð¦2x2,y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ­ä»£å ¥éå½æ±è§£ç´è³ gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æå¤§å ¬çº¦æ°ï¼ä¸åï¼ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éå½ ð¥ =1,ð¦ =0x=1,y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå»æ±è§£ï¼

### å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int Exgcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; return a ; } int d = Exgcd ( b , a % b , x , y ); int t = x ; x = y ; y = t \- ( a / b ) * y ; return d ; } ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text def Exgcd ( a , b ): if b == 0 : return a , 1 , 0 d , x , y = Exgcd ( b , a % b ) return d , y , x \- ( a // b ) * y ```   
---|---  
  
å½æ°è¿åçå¼ä¸º gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨è¿ä¸ªè¿ç¨ä¸­è®¡ç® ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

### å¼ååæ

ðð¥ +ðð¦ =gcd(ð,ð)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ææ æ°ä¸ªï¼æ¾ç¶å ¶ä¸­æçè§£ä¼ç long longï¼  
ä¸å¹¸çæ¯ï¼è¥ ð â 0bâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ©å±æ¬§å éå¾ç®æ³æ±åºçå¯è¡è§£å¿ æ |ð¥| â¤ð,|ð¦| â¤ð|x|â¤b,|y|â¤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼  
ä¸é¢ç»åºè¿ä¸æ§è´¨çè¯æï¼

è¯æ

  * gcd(ð,ð) =ðgcd(a,b)=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ðmodð =0amodb=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ å¨ä¸ä¸å±ç»æ­¢éå½ï¼  
å¾å° ð¥1 =0,ð¦1 =1x1=0,y1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶ ð,ð â¥1 â¥|ð¥1|,|ð¦1|a,bâ¥1â¥|x1|,|y1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * gcd(ð,ð) â ðgcd(a,b)â b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è®¾ |ð¥2| â¤(ðmodð),|ð¦2| â¤ð|x2|â¤(amodb),|y2|â¤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼  
å ä¸º ð¥1 =ð¦2,ð¦1 =ð¥2 ââððâð¦2x1=y2,y1=x2ââabây2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
æä»¥ |ð¥1| =|ð¦2| â¤ð,|ð¦1| â¤|ð¥2| +|âððâð¦2| â¤(ðmodð) +âððâ|ð¦2||x1|=|y2|â¤b,|y1|â¤|x2|+|âabây2|â¤(amodb)+âabâ|y2|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
â¤ð ââððâð +âððâ|ð¦2| â¤ð ââððâ(ð â|ð¦2|)â¤aââabâb+âabâ|y2|â¤aââabâ(bâ|y2|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
ðmodð =ð ââððâð â¤ð ââððâ(ð â|ð¦2|) â¤ðamodb=aââabâbâ¤aââabâ(bâ|y2|)â¤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
å æ­¤ |ð¥1| â¤ð,|ð¦1| â¤ð|x1|â¤b,|y1|â¤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

### è¿­ä»£æ³ç¼åæ©å±æ¬§å éå¾ç®æ³

é¦å ï¼å½ ð¥ =1x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¦ =0y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¥1 =0x1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¦1 =1y1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ¾ç¶æï¼

{ðð¥+ðð¦=ððð¥1+ðð¦1=ð{ax+by=aax1+by1=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼

å·²ç¥ ðmodð =ð â(âððâ Ãð)amodb=aâ(âabâÃb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸é¢ä»¤ ð =âððâq=âabâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åèè¿­ä»£æ³æ± gcdï¼æ¯ä¸è½®çè¿­ä»£è¿ç¨å¯ä»¥è¡¨ç¤ºä¸ºï¼

(ð,ð)â(ð,ðâðð)(a,b)â(b,aâqb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°è¿­ä»£è¿ç¨ä¸­ç ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢ä¸º ðð¥ +ðð¦ =ðax+by=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢ä¸º ðð¥1 +ðð¦1 =ðax1+by1=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å¾å°ï¼

{ðð¥+ðð¦=ððð¥1+ðð¦1=ðâ{ðð¥1+ðð¦1=ðð(ð¥âðð¥1)+ð(ð¦âðð¦1)=ðâðð{ax+by=aax1+by1=bâ{ax1+by1=ba(xâqx1)+b(yâqy1)=aâqb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ®æ­¤å°±å¯ä»¥å¾å°è¿­ä»£æ³æ± exgcdï¼

å ä¸ºè¿­ä»£çæ¹æ³é¿å äºéå½ï¼æä»¥ä»£ç è¿è¡éåº¦å°æ¯éå½ä»£ç å¿«ä¸ç¹ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int gcd ( int a , int b , int & x , int & y ) { x = 1 , y = 0 ; int x1 = 0 , y1 = 1 , a1 = a , b1 = b ; while ( b1 ) { int q = a1 / b1 ; tie ( x , x1 ) = make_tuple ( x1 , x \- q * x1 ); tie ( y , y1 ) = make_tuple ( y1 , y \- q * y1 ); tie ( a1 , b1 ) = make_tuple ( b1 , a1 \- q * b1 ); } return a1 ; } ```   
---|---  
  
å¦æä½ ä»ç»è§å¯ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½ ä¼åç°ï¼ä»ä»¬å¨è¿­ä»£çæ¬çæ¬§å éå¾·ç®æ³ä¸­åå¼å®å ¨ç¸åï¼å¹¶ä¸ä»¥ä¸å ¬å¼æ è®ºä½æ¶ï¼å¨ while å¾ªç¯ä¹ååæ¯æ¬¡è¿­ä»£ç»ææ¶ï¼é½æ¯æç«çï¼ð¥ â ð +ð¦ â ð =ð1xâ a+yâ b=a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥1 â ð +ð¦1 â ð =ð1x1â a+y1â b=b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼è¯¥ç®æ³è¯å®è½æ­£ç¡®è®¡ç®åº gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æåæä»¬ç¥é ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¦æ±ç gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð¥ â ð +ð¦ â ð =ðxâ a+yâ b=g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### ç©éµçè§£é

å¯¹äºæ­£æ´æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ¬¡è¾è½¬ç¸é¤å³ gcd(ð,ð) =gcd(ð,ðmodð)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿ç¨ç©éµè¡¨ç¤ºå¦

[ððmodð]=[011ââð/ðâ][ðð][bamodb]=[011ââa/bâ][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­åä¸åæ´ç¬¦å· âðââcâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºä¸å¤§äº ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§æ´æ°ï¼æä»¬å®ä¹åæ¢ [ðð] â¦[011ââð/ðâ][ðð][ab]â¦[011ââa/bâ][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æåç°æ¬§å éå¾ç®æ³å³ä¸ååºç¨è¯¥åæ¢ï¼æ

[gcd(ð,ð)0]=(â¯[011ââð/ðâ][1001])[ðð][gcd(a,b)0]=(â¯[011ââa/bâ][1001])[ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤

[ð¥1ð¥2ð¥3ð¥4]=â¯[011ââð/ðâ][1001][x1x2x3x4]=â¯[011ââa/bâ][1001]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹

[gcd(ð,ð)0]=[ð¥1ð¥2ð¥3ð¥4][ðð][gcd(a,b)0]=[x1x2x3x4][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ»¡è¶³ ð â ð¥1 +ð â ð¥2 =gcd(ð,ð)aâ x1+bâ x2=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³æ©å±æ¬§å éå¾ç®æ³ï¼æ³¨æå¨æåä¹äºä¸ä¸ªåä½ç©éµä¸ä¼å½±åç»æï¼æç¤ºæä»¬å¯ä»¥å¨å¼å§æ¶ç»´æ¤ä¸ä¸ª 2 Ã22Ã2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåä½ç©éµç¼åæ´ç®æ´çè¿­ä»£æ¹æ³å¦

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int exgcd ( int a , int b , int & x , int & y ) { int x1 = 1 , x2 = 0 , x3 = 0 , x4 = 1 ; while ( b != 0 ) { int c = a / b ; std :: tie ( x1 , x2 , x3 , x4 , a , b ) = std :: make_tuple ( x3 , x4 , x1 \- x3 * c , x2 \- x4 * c , b , a \- b * c ); } x = x1 , y = x2 ; return a ; } ```   
---|---  
  
è¿ç§è¡¨è¿°ç¸è¾äºéå½æ´ç®åï¼

## åºç¨

  * [10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
  * [GYM - (J) once upon a time](http://codeforces.com/gym/100963)
  * [UVa - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)

## åèèµæä¸é¾æ¥

* * *

  1. [libstdc++: std Namespace Reference](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00978.html#a2686a128df5a576cb53a1ed5f674607)Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/27 12:26:08ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/gcd.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/gcd.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [hsfzLZH1](https://github.com/hsfzLZH1), [c-forrest](https://github.com/c-forrest), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [383494](https://github.com/383494), [i-yyi](https://github.com/i-yyi), [LuoshuiTianyi](https://github.com/LuoshuiTianyi), [mgt](mailto:i@margatroid.xyz), [untitledunrevised](https://github.com/untitledunrevised), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Backl1ght](https://github.com/Backl1ght), [buggg-hfc](https://github.com/buggg-hfc), [FinParker](https://github.com/FinParker), [gi-b716](https://github.com/gi-b716), [Great-designer](https://github.com/Great-designer), [hhc0001](https://github.com/hhc0001), [hly1204](https://github.com/hly1204), [hsiviter](https://github.com/hsiviter), [huaruoji](mailto:43847915+huaruoji@users.noreply.github.com), [Koishilll](https://github.com/Koishilll), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [PwzXxm](https://github.com/PwzXxm), [Qubik65536](https://github.com/Qubik65536), [shawlleyw](https://github.com/shawlleyw), [tder6](https://github.com/tder6), [TOMWT-qwq](https://github.com/TOMWT-qwq), [VaneHsiung](https://github.com/VaneHsiung), [warzone-oier](https://github.com/warzone-oier), [WillHouMoe](https://github.com/WillHouMoe)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
