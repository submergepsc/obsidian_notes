# ç´ æ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/prime/

# ç´ æ°

ç´ æ°ä¸åæ°çå®ä¹ï¼è§ [æ°è®ºåºç¡](../basic/)ï¼

ç´ æ°è®¡æ°å½æ°ï¼å°äºæç­äº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ°çä¸ªæ°ï¼ç¨ ð(ð¥)Ï(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºï¼éç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¢å¤§ï¼æè¿æ ·çè¿ä¼¼ç»æï¼ð(ð¥) â¼ð¥lnâ¡(ð¥)Ï(x)â¼xlnâ¡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## ç´ æ§æµè¯

**ç´ æ§æµè¯** ï¼Primality testï¼å¯ä»¥ç¨äºå¤å®æç»èªç¶æ°æ¯å¦ä¸ºç´ æ°ï¼

ç´ æ§æµè¯æä¸¤ç§ï¼

  1. ç¡®å®æ§æµè¯ï¼ç»å¯¹ç¡®å®ä¸ä¸ªæ°æ¯å¦ä¸ºç´ æ°ï¼å¸¸è§ä¾å­å æ¬è¯é¤æ³ãLucasâLehmer æµè¯åæ¤­åæ²çº¿ç´ æ§è¯æï¼
  2. æ¦çæ§æµè¯ï¼éå¸¸æ¯ç¡®å®æ§æµè¯å¿«å¾å¤ï¼ä½æå¯è½ï¼å°½ç®¡æ¦çå¾å°ï¼éè¯¯å°å° [åæ°](../basic/#ç´) è¯å«ä¸ºè´¨æ°ï¼å°½ç®¡åä¹åä¸ä¼ï¼ï¼å æ­¤ï¼éè¿æ¦çç´ æ§æµè¯çæ°å­è¢«ç§°ä¸º **å¯è½ç´ æ°** ï¼ç´å°å®ä»¬çç´ æ°å¯ä»¥è¢«ç¡®å®æ§å°è¯æï¼èéè¿æµè¯ä½å®é ä¸æ¯åæ°çæ°å­åè¢«ç§°ä¸º **ä¼ªç´ æ°** ï¼æè®¸å¤ç¹å®ç±»åçä¼ªç´ æ°ï¼æå¸¸è§çæ¯è´¹é©¬ä¼ªç´ æ°ï¼å®ä»¬æ¯æ»¡è¶³è´¹é©¬å°å®ççåæ°ï¼æ¦çæ§æµè¯çå¸¸è§ä¾å­å æ¬ MillerâRabin æµè¯ï¼

### è¯é¤æ³

æ´ååæ³èªç¶å¯ä»¥æä¸¾ä»å°å°å¤§çæ¯ä¸ªæ°çæ¯å¦è½æ´é¤ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 ``` |  ```text bool isPrime ( int a ) { if ( a < 2 ) return false ; for ( int i = 2 ; i < a ; ++ i ) if ( a % i == 0 ) return false ; return true ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def isPrime ( a ): if a < 2 : return False for i in range ( 2 , a ): if a % i == 0 : return False return True ```   
---|---  
  
è¿æ ·åæ¯ååç¨³å¦¥äºï¼ä½æ¯ççæå¿ è¦æ¯ä¸ªæ°é½å»å¤æ­åï¼

å¾å®¹æåç°è¿æ ·ä¸ä¸ªäºå®ï¼å¦æ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ï¼é£ä¹ ðð¥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ï¼

è¿ä¸ªç»è®ºåè¯æä»¬ï¼å¯¹äºæ¯ä¸å¯¹ (ð¥,ðð¥)(x,ax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªæ£éªå ¶ä¸­çä¸ä¸ªå°±è¶³å¤äºï¼ä¸ºäºæ¹ä¾¿èµ·è§ï¼æä»¬åªèå¯æ¯ä¸å¯¹çè¾å°æ°ï¼ä¸é¾åç°ï¼ææè¿äºè¾å°æ°é½å¨ [1,âð][1,a]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸ªåºé´éï¼

ç±äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¯å®æ¯çº¦æ°ï¼æä»¥ä¸æ£éªå®ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 ``` |  ```text bool isPrime ( int a ) { if ( a < 2 ) return 0 ; for ( int i = 2 ; ( long long ) i * i <= a ; ++ i ) // é²æº¢åº if ( a % i == 0 ) return 0 ; return 1 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def isPrime ( a ): if a < 2 : return False for i in range ( 2 , int ( sqrt ( a )) \+ 1 ): if a % i == 0 : return False return True ```   
---|---  
  
### Fermat ç´ æ§æµè¯

**Fermat ç´ æ§æ£éª** æ¯æç®åçæ¦çæ§ç´ æ§æ£éªï¼

æä»¬å¯ä»¥æ ¹æ® [è´¹é©¬å°å®ç](../fermat/#è´¹é©¬å°å®ç) å¾åºä¸ç§æ£éªç´ æ°çæè·¯ï¼

åºæ¬ææ³æ¯ä¸æ­å°éåå¨ [2,ð â1][2,nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çåºåº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶æ£éªæ¯å¦æ¯æ¬¡é½æ ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text bool fermat ( int n ) { if ( n < 3 ) return n == 2 ; // test_time ä¸ºæµè¯æ¬¡æ°,å»ºè®®è®¾ä¸ºä¸å°äº 8 // çæ´æ°ä»¥ä¿è¯æ­£ç¡®ç,ä½ä¹ä¸å®è¿å¤§,å¦åä¼å½±åæç for ( int i = 1 ; i <= test_time ; ++ i ) { int a = rand () % ( n \- 2 ) \+ 2 ; if ( quickPow ( a , n \- 1 , n ) != 1 ) return false ; } return true ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text def fermat ( n ): if n < 3 : return n == 2 # test_time ä¸ºæµè¯æ¬¡æ°,å»ºè®®è®¾ä¸ºä¸å°äº 8 # çæ´æ°ä»¥ä¿è¯æ­£ç¡®ç,ä½ä¹ä¸å®è¿å¤§,å¦åä¼å½±åæç for i in range ( 1 , test_time \+ 1 ): a = random . randint ( 0 , 32767 ) % ( n \- 2 ) \+ 2 if quickPow ( a , n \- 1 , n ) != 1 : return False return True ```   
---|---  
  
å¦æ ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ç´ æ°ï¼åç§° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä»¥ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåºç **Fermat ä¼ªç´ æ°** ï¼æä»¬å¨å®è·µä¸­è§å¯å°ï¼å¦æ ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éå¸¸æ¯ç´ æ°ï¼ä½å ¶å®å­å¨åä¾ï¼å¯¹äº ð =341n=341![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð =2a=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è½ç¶æ 2340 â¡1(mod341)2340â¡1(mod341)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ 341 =11 â 31341=11â 31![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åæ°ï¼äºå®ä¸ï¼å¯¹äºä»»ä½åºå®çåºåº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·çåä¾é½ææ ç©·å¤ä¸ª1ï¼

æ¢ç¶å¯¹äºåä¸ªåºåºï¼Fermat ç´ æ§æµè¯æ æ³ä¿è¯æ­£ç¡®æ§ï¼ä¸ä¸ªèªç¶çæ³æ³å°±æ¯å¤æ£æ¥å ç»åºåºï¼ä½æ¯ï¼å³ä½¿æ£æ¥äºææå¯è½çä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çåºåº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾ç¶æ æ³ä¿è¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç´ æ°ï¼ä¹å°±æ¯è¯´ï¼è´¹é©¬å°å®ççéå½é¢å¹¶ä¸æç«ï¼å³ä½¿å¯¹äºææ ð âðaân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ä¸å®æ¯ç´ æ°ï¼è¿æ ·çæ°ç§°ä¸º [Carmichael æ°](../primitive-root/#carmichael-æ°)ï¼å®ä¹ææ ç©·å¤ä¸ªï¼è¿è¿«ä½¿æä»¬å¯»æ¾æ´ä¸ºä¸¥æ ¼çç´ æ§æµè¯ï¼

### MillerâRabin ç´ æ§æµè¯

**MillerâRabin ç´ æ§æµè¯** ï¼MillerâRabin primality testï¼æ¯æ´å¥½çç´ æ°å¤å®æ¹æ³ï¼å®æ¯ç± Miller å Rabin äºäººæ ¹æ® Fermat ç´ æ§æµè¯ä¼åå¾å°çï¼åå ¶å®æ¦çæ§ç´ æ°æµè¯ä¸æ ·ï¼å®ä¹åªè½æ£æµåºä¼ªç´ æ°ï¼è¦ç¡®ä¿æ¯ç´ æ°ï¼éè¦ç¨æ ¢å¾å¤çç¡®å®æ§ç®æ³ï¼ç¶èï¼å®é ä¸æ²¡æå·²ç¥çæ°å­éè¿äº MillerâRabin æµè¯ç­é«çº§æ¦çæ§æµè¯ä½å®é ä¸å´æ¯åæ°ï¼å æ­¤æä»¬å¯ä»¥æ¾å¿ä½¿ç¨ï¼

å¨ä¸èèä¹æ³çå¤æåº¦æ¶ï¼å¯¹æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½®æµè¯çæ¶é´å¤æåº¦æ¯ ð(ðlogâ¡ð)O(klogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼MillerâRabin ç´ æ§æµè¯å¸¸ç¨äºå¯¹é«ç²¾åº¦æ°è¿è¡æµè¯ï¼æ­¤æ¶æ¶é´å¤æåº¦æ¯ ð(ðlog3â¡ð)O(klog3â¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨ FFT ç­ææ¯å¯ä»¥ä¼åå° [ð(ðlog2â¡ðlogâ¡logâ¡ðlogâ¡logâ¡logâ¡ð)O(klog2â¡nlogâ¡logâ¡nlogâ¡logâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity)ï¼

ä¸ºäºè§£å³ Carmichael æ°å¸¦æ¥çææï¼MillerâRabin ç´ æ§æµè¯è¿ä¸æ­¥èèäºç´ æ°çå¦ä¸æ§è´¨ï¼

äºæ¬¡æ¢æµå®ç

å¦æ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ï¼å ð¥2 â¡1(modð)x2â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ä¸º ð¥ â¡1(modð)xâ¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè ð¥ â¡ð â1(modð)xâ¡pâ1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å®¹æéªè¯ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥ç´ æ°æ¶ï¼ð¥ â¡1(modð)xâ¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ â¡ð â1(modð)xâ¡pâ1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥ä½¿å¾ä¸å¼æç«ï¼ç± [Lagrange å®ç](../congruence-equation/#å®ç-3lagrange-å®ç) å¯ç¥ï¼è¿å°±æ¯è¯¥æ¹ç¨çææè§£ï¼

å°è´¹é©¬å°å®çåäºæ¬¡æ¢æµå®çç»åèµ·æ¥ä½¿ç¨ï¼å°±å¾å° MillerâRabin ç´ æ§æµè¯ï¼

  1. å° ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çææ° ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸º ð â1 =ð¢ Ã2ð¡nâ1=uÃ2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å¨æ¯è½®æµè¯ä¸­å¯¹éæºåºæ¥ç ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ±åº ð£ =ðð¢modðv=aumodn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹åå¯¹è¿ä¸ªå¼æ§è¡æå¤ ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹³æ¹æä½ï¼
  3. å¨æ´ä¸ªè¿ç¨ä¸­ï¼å¦æåç° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå¹³å¡å¹³æ¹æ ¹ï¼å³é¤äº Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¤çå ¶ä»æ ¹ï¼ï¼å°±å¯ä»¥å¤æ­è¯¥æ°ä¸æ¯ç´ æ°ï¼
  4. å¦åï¼åä½¿ç¨ Fermat ç´ æ§æµè¯å¤æ­ï¼

è¿æä¸äºå®ç°ä¸çå°ç»èï¼

  * å¯¹äºä¸è½®æµè¯ï¼å¦ææä¸æ¶å» ðð¢Ã2ð  â¡ð â1(modð)auÃ2sâ¡nâ1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¹åçå¹³æ¹æä½å ¨é½ä¼å¾å° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯ä»¥ç´æ¥éè¿æ¬è½®æµè¯ï¼
  * å¦ææ¾åºäºä¸ä¸ªéå¹³å¡å¹³æ¹æ ¹ ðð¢Ã2ð  â¢ð â1(modð)auÃ2sâ¢nâ1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¹åçå¹³æ¹æä½å ¨é½ä¼å¾å° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥éæ©ç´æ¥è¿å `false`ï¼ä¹å¯ä»¥æ¾å° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹³æ¹æä½ååè¿å `false`ï¼

è¿æ ·å¾å°äºè¾æ­£ç¡®ç Miller Rabinï¼ï¼æ¥èª fjzzq2002ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text bool millerRabin ( int n ) { if ( n < 3 || n % 2 == 0 ) return n == 2 ; if ( n % 3 == 0 ) return n == 3 ; int u = n \- 1 , t = 0 ; while ( u % 2 == 0 ) u /= 2 , ++ t ; // test_time ä¸ºæµè¯æ¬¡æ°ï¼å»ºè®®è®¾ä¸ºä¸å°äº 8 // çæ´æ°ä»¥ä¿è¯æ­£ç¡®çï¼ä½ä¹ä¸å®è¿å¤§ï¼å¦åä¼å½±åæç for ( int i = 0 ; i < test_time ; ++ i ) { // 0, 1, n-1 å¯ä»¥ç´æ¥éè¿æµè¯, a åå¼èå´ [2, n-2] int a = rand () % ( n \- 3 ) \+ 2 , v = quickPow ( a , u , n ); if ( v == 1 ) continue ; int s ; for ( s = 0 ; s < t ; ++ s ) { if ( v == n \- 1 ) break ; // å¾å°å¹³å¡å¹³æ¹æ ¹ n-1ï¼éè¿æ­¤è½®æµè¯ v = ( long long ) v * v % n ; } // å¦ææ¾å°äºéå¹³å¡å¹³æ¹æ ¹ï¼åä¼ç±äºæ æ³æå break; èè¿è¡å° s == t // å¦æ Fermat ç´ æ§æµè¯æ æ³éè¿ï¼åä¸ç´è¿è¡å° s == t å v é½ä¸ä¼ç­äº -1 if ( s == t ) return 0 ; } return 1 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text def millerRabin ( n ): if n < 3 or n % 2 == 0 : return n == 2 if n % 3 == 0 : return n == 3 u , t = n \- 1 , 0 while u % 2 == 0 : u = u // 2 t = t \+ 1 # test_time ä¸ºæµè¯æ¬¡æ°,å»ºè®®è®¾ä¸ºä¸å°äº 8 # çæ´æ°ä»¥ä¿è¯æ­£ç¡®ç,ä½ä¹ä¸å®è¿å¤§,å¦åä¼å½±åæç for i in range ( test_time ): # 0, 1, n-1 å¯ä»¥ç´æ¥éè¿æµè¯, a åå¼èå´ [2, n-2] a = random . randint ( 2 , n \- 2 ) v = pow ( a , u , n ) if v == 1 : continue s = 0 while s < t : if v == n \- 1 : break v = v * v % n s = s \+ 1 # å¦ææ¾å°äºéå¹³å¡å¹³æ¹æ ¹ï¼åä¼ç±äºæ æ³æå break; èè¿è¡å° s == t # å¦æ Fermat ç´ æ§æµè¯æ æ³éè¿ï¼åä¸ç´è¿è¡å° s == t å v é½ä¸ä¼ç­äº -1 if s == t : return False return True ```   
---|---  
  
å¯ä»¥è¯æ2ï¼å¥åæ° ð >9n>9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿éæºéåçä¸ä¸ªåºåº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç MillerâRabin ç´ æ§æµè¯çæ¦çè³å¤ä¸ºååä¹ä¸ï¼å æ­¤ï¼éæºéå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªåºåºåï¼ä»å°åæ°è¯¯å¤ä¸ºç´ æ°çæ¦çä¸è¶ è¿ 1/4ð1/4k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®¾ ð â1 =ð¢2ð¡nâ1=u2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°ä¸ ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ­£æ´æ°ï¼é£ä¹ï¼æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥éè¿åºåºä¸º ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç MillerâRabin ç´ æ§æµè¯è¯´æ

ðð¢â¡1(modð),Â orÂ ðð¢2ðâ¡â1(modð)Â for someÂ 0â¤ð<ð¡.auâ¡1(modn),Â orÂ au2iâ¡â1(modn)Â for someÂ 0â¤i<t.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®°è¿æ ·ç ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çåä½ç±»ï¼éåä¸º ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦è¯´æçæ¯

|ð|â¤14ð(ð).|S|â¤14Ï(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ [æ¬§æå½æ°](../euler-totient/)ï¼è¯æåä¸ºä¸æ­¥ï¼

**ç¬¬ä¸æ­¥** ï¼è®¾ ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä½¿å¾ 2â â£ð â12ââ£pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«çæå¤§æ­£æ´æ°ï¼é£ä¹ï¼å¯ä»¥è¯æ

ðâðâ²={ðmodð:ðð¢2ââ1â¡Â±1(modð)}.SâSâ²={amodn:au2ââ1â¡Â±1(modn)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªæä¸¤ç§å¯è½ï¼å¦æ ðð¢ â¡1(modð)auâ¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ¾ç¶ ðð¢2ââ1 â¡1(modð)au2ââ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç«ï¼äº¦å³ ð âðâ²aâSâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå¯¹äº 0 â¤ð <ð¡0â¤i<t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç« ðð¢2ð â¡ â1(modð)au2iâ¡â1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯¹äºä»»æç´ å å­ ð â£ðpâ£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðð¢2ð â¡ â1(modð)au2iâ¡â1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ ð¿ð(ð)Î´p(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [é¶](../primitive-root/#é¶)ï¼é£ä¹ï¼æ¾ç¶æ ð¿ð(ð) â£ð¢2ð+1Î´p(a)â£u2i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¯ ð¿ð(ð) â¤ð¢2ðÎ´p(a)â¤u2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æï¼ð¿ð(ð)Î´p(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å æ°åè§£ä¸­ï¼22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææ°æ°ä¸º ð +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å è 2ð+1 â£ð¿ð(ð)2i+1â£Î´p(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±è´¹é©¬å°å®çå¯ç¥ï¼ð¿ð(ð) â£ð â1Î´p(a)â£pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼2ð+1 â£ð â12i+1â£pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸ç¹å¯¹äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææç´ å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å æ­¤ï¼ð +1 â¤âi+1â¤â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æ ðð¢2ââ1 =(ðð¢2ð)2ââ1âð â¡ Â±1(modð)au2ââ1=(au2i)2ââ1âiâ¡Â±1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ·æ ð âðâ²aâSâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç»¼åä¸¤ç§å¯è½ï¼å°±å¾å° ð âðâ²SâSâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**ç¬¬äºæ­¥** ï¼è®¡ç® |ðâ²||Sâ²|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°ï¼

åè®¾ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç´ å æ°åè§£ ð =ðð11ðð22â¯ððððn=p1e1p2e2â¯pkek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ç± [ä¸­å½å©ä½å®ç](../crt/) å¯ç¥ï¼æ¡ä»¶ ðð¢2ââ1 â¡1(modð)au2ââ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·äº ðð¢2ââ1 â¡1(modðððð)au2ââ1â¡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ððððpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼ç±äºæ¨¡å¥ç´ æ°å¹ ððððpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [åæ ¹](../primitive-root/#åæ) æ»æ¯å­å¨çï¼æä»¥ï¼åä½æ¹ç¨ ðð¢2ââ1 â¡1(modðððð)au2ââ1â¡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [è§£çæ°é](../residue/#æ§è´¨) ä¸º

gcd(ð¢2ââ1,ðððâ1ð(ððâ1))=gcd(ð¢2ââ1,ððâ1)=2ââ1gcd(ð¢,ððâ1).gcd(u2ââ1,pieiâ1(piâ1))=gcd(u2ââ1,piâ1)=2ââ1gcd(u,piâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¬¬ä¸ä¸ªç­å·æç«ï¼æ¯å ä¸º ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå å­ï¼ä¸å¯è½æ¯ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼ç¬¬äºä¸ªç­å·æç«ï¼æ¯å ä¸º ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåæ¹å¼ï¼æä»¥ï¼ç±ä¸­å½å©ä½å®çå¯ç¥ï¼åä½æ¹ç¨ ðð¢2ââ1 â¡1(modð)au2ââ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£çæ°éä¸º

âðâ£ð2ââ1gcd(ð¢,ðâ1).âpâ£n2ââ1gcd(u,pâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åçï¼æ¡ä»¶ ðð¢2ââ1 â¡ â1(modð)au2ââ1â¡â1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·äº ðð¢2ââ1 â¡ â1(modðððð)au2ââ1â¡â1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ððððpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å¯¹äºä»»æå å­ ððððpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¡ä»¶ ðð¢2ââ1 â¡ â1(modðððð)au2ââ1â¡â1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ç­ä»·äº ðð¢2ââ1 â¢1(modðððð)au2ââ1â¢1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð¢2â â¡1(modðððð)au2ââ¡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼ç±»ä¼¼ä¸æï¼å¯ä»¥è®¡ç®åºåä½æ¹ç¨ ðð¢2â â¡1(modðððð)au2ââ¡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£çæ°éä¸º 2âgcd(ð¢,ðð â1)2âgcd(u,piâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼åä½æ¹ç¨ ðð¢2ââ1 â¡ â1(modðððð)au2ââ1â¡â1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£çæ°éä¹ç­äº

2âgcd(ð¢,ððâ1)â2ââ1gcd(ð¢,ððâ1)=2ââ1gcd(ð¢,ððâ1).2âgcd(u,piâ1)â2ââ1gcd(u,piâ1)=2ââ1gcd(u,piâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ¬¡åºç¨ä¸­å½å©ä½å®çï¼å°±å¾å°åä½æ¹ç¨ ðð¢2ââ1 â¡ â1(modð)au2ââ1â¡â1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£çæ°éç­äº

âðâ£ð2ââ1gcd(ð¢,ðâ1).âpâ£n2ââ1gcd(u,pâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ç»¼åä¸¤ç§æ å½¢ï¼æ

|ðâ²|=2âðâ£ð2ââ1gcd(ð¢,ðâ1).|Sâ²|=2âpâ£n2ââ1gcd(u,pâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**ç¬¬ä¸æ­¥** ï¼è¯æ |ðâ²| â¤ð(ð)/4|Sâ²|â¤Ï(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç»åæ¬§æå½æ°çè¡¨è¾¾å¼ ð(ð) =âððððâ1ð(ðð â1)Ï(n)=âipieiâ1(piâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥

ð(ð)|ðâ²|=12âððððâ1ðððâ12ââ1gcd(ð¢,ððâ1).Ï(n)|Sâ²|=12âipieiâ1piâ12ââ1gcd(u,piâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºæ¯ä¸ä¸ª ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¸åºçå å­ ðððâ1ðððâ12ââ1gcd(ð¢,ððâ1)pieiâ1piâ12ââ1gcd(u,piâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ä¸ä¸ªå¶æ°ï¼æä»¥ï¼ð(ð)/|ðâ²|Ï(n)/|Sâ²|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªæ´æ°ï¼åè®¾ |ðâ²| â¤ð(ð)/4|Sâ²|â¤Ï(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æç«ï¼å¿ ç¶æ ð(ð)/|ðâ²| =1,2,3Ï(n)/|Sâ²|=1,2,3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³

âððððâ1ðððâ12ââ1gcd(ð¢,ððâ1)=2,4,6.âipieiâ1piâ12ââ1gcd(u,piâ1)=2,4,6.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºè¿ä¹å¼ä¸­çæ¯ä¸ªå å­é½æ¯å¶æ°ï¼æä»¥ï¼è¿ä¸ªè¿ä¹å¼è¦ä¹åªæä¸ä¸ªå å­ä¸è¿ä¸ªå å­å°±ç­äº 2,4,62,4,6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦ä¹å°±åªæä¸¤ä¸ªå å­ä¸é½ç­äº 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

é¦å èèæä¸¤ä¸ªå å­çæ å½¢ï¼æ­¤æ¶ï¼ä¸¤ä¸ªå å­é½æ²¡æå¥ç´ å å­ï¼æä»¥ï¼ðððâ1ð =1pieiâ1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ²¡æå¹³æ¹å å­ï¼ä¸å¦¨è®¾ ð =ð1ð2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð1 <ð2p1<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ç´ æ°ï¼ä¸¤ä¸ªå å­é½ç­äº 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼æ»æ ðð â1 =2âgcd(ð¢,ðð â1)piâ1=2âgcd(u,piâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ðð =1 +2âððpi=1+2âmi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ððmi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°ï¼èä¸ ðð â£ð¢miâ£u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ð1ð2 =ð =1 +ð¢2ð¡p1p2=n=1+u2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ ð1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡å°±å¾å° ð1ð2 â¡1(modð1)p1p2â¡1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ è ð2 â¡1(modð1)p2â¡1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æï¼ð1 â£ð2m1â£m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¿æ¥ä¹æç«ï¼è¿å°±è¯´æ ð1 =ð2m1=m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯ ð1 =ð2p1=p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸ ð1 <ð2p1<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¾ï¼è¿ä¸æ å½¢ä¸æç«ï¼

æåï¼èèåªæä¸ä¸ªå å­çæ å½¢ï¼äº¦å³åæ° ð =ððn=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼å¿ ç¶æ ððâ1 â£2,4,6peâ1â£2,4,6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¯ä¸çæ å½¢æ¯ ð =3,ð =2p=3,e=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ð =9n=9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å½é¢æè®¾ç¸çç¾ï¼è¿ä¸æ å½¢ä¹ä¸æç«ï¼

ç»¼åæææ å½¢å¯ç¥ï¼|ðâ²| â¤ð(ð)/4|Sâ²|â¤Ï(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

ç»åä¸è¿°ä¸ä¸ªæ­¥éª¤å¯ç¥ï¼|ð| â¤|ðâ²| â¤ð(ð)/4|S|â¤|Sâ²|â¤Ï(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææå¥åæ° ð >9n>9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼

å¦å¤ï¼åè®¾ [å¹¿ä¹ Riemann çæ³](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)ï¼generalized Riemann hypothesis, GRHï¼æç«ï¼åå¯¹æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¤åªéè¦æµè¯ [2,min{ð â2,â2ln2â¡ðâ}][2,min{nâ2,â2ln2â¡nâ}]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ¨é¨æ´æ°å³å¯ **ç¡®å®** æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ§ï¼3

èå¨ OI èå´å ï¼éå¸¸é½æ¯å¯¹ [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èå´å çæ°è¿è¡ç´ æ§æ£éªï¼å¯¹äº [1,232)[1,232)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èå´å çæ°ï¼éå {2,7,61}{2,7,61}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ªæ°ä½ä¸ºåºåºè¿è¡ MillerâRabin ç´ æ§æ£éªå°±å¯ä»¥ç¡®å®ç´ æ§ï¼å¯¹äº [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èå´å çæ°ï¼éå {2,325,9375,28178,450775,9780504,1795265022}{2,325,9375,28178,450775,9780504,1795265022}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ªæ°ä½ä¸ºåºåºè¿è¡ MillerâRabin ç´ æ§æ£éªå°±å¯ä»¥ç¡®å®ç´ æ§ï¼4

ä¹å¯ä»¥éå {2,3,5,7,11,13,17,19,23,29,31,37}{2,3,5,7,11,13,17,19,23,29,31,37}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç´ æ°ï¼æ£éª [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èå´å çç´ æ°ï¼

æ³¨æå¦æè¦ä½¿ç¨ä¸é¢çæ°åä¸­çæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºåºåºå¤æ­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ§ï¼

  * ææçæ°é½è¦åä¸éï¼ä¸è½åªéå°äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼
  * æ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢æ ðmodðamodn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å¦æ ð â¡0(modð)aâ¡0(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð â¡ Â±1(modð)aâ¡Â±1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç´æ¥éè¿è¯¥è½®æµè¯ï¼

## åç´ æ°

é¡¾åæä¹ï¼ç´ æ°å°±æ¯å å­åªæä¸¤ä¸ªçæ°ï¼é£ä¹åç´ æ°ï¼å°±æ¯å å­æå¤çæ°ï¼å¹¶ä¸å å­ä¸ªæ°ç¸åçæ¶åå¼æå°ï¼ï¼æä»¥åç´ æ°æ¯ç¸å¯¹äºä¸ä¸ªéåæ¥è¯´çï¼

ä¸ç§ç¬¦åç´è§çåç´ æ°å®ä¹æ¯ï¼å¨ä¸ä¸ªæ­£æ´æ°éåä¸­ï¼å å­æå¤å¹¶ä¸å¼æå°çæ°ï¼å°±æ¯åç´ æ°ï¼

åç´ æ°

å¯¹äºæä¸ªæ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æä»»ä½å°äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ°ççº¦æ°ä¸ªæ°é½å°äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ä¸ªæ°ï¼åç§°ä¸ºæ¯ **åç´ æ°** ï¼anti-prime, a.k.a., highly compositive numbersï¼ï¼

æ³¨æ

æ³¨æåºå [emirp](https://en.wikipedia.org/wiki/Emirp)ï¼å®è¡¨ç¤ºçæ¯éä½åè½¬åæ¯ä¸åç´ æ°çç´ æ°ï¼å¦ 149 å 941 åä¸º emirpï¼101 ä¸æ¯ emirpï¼ï¼

### è¿ç¨

é£ä¹ï¼å¦ä½æ¥æ±è§£åç´ æ°å¢ï¼

é¦å ï¼æ¢ç¶è¦æ±å å­æ°ï¼é¦å è¦åçå°±æ¯ç´ å å­åè§£ï¼æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£æ ð =ðð11ðð22â¯ððððn=p1k1p2k2â¯pnkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼å ¶ä¸­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç´ æ°ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä»çææ°ï¼è¿æ ·çè¯æ»å å­ä¸ªæ°å°±æ¯ (ð1 +1) Ã(ð2 +1) Ã(ð3 +1)â¯ Ã(ðð +1)(k1+1)Ã(k2+1)Ã(k3+1)â¯Ã(kn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä½æ¯æ¾ç¶è´¨å å­åè§£çå¤æåº¦æ¯å¾é«çï¼å¹¶ä¸åä¸ä¸ªæ°çç»æä¸è½è¢«åé¢å©ç¨ï¼æä»¥è¦æ¢ä¸ªæ¹æ³ï¼

æä»¬æ¥è§å¯ä¸ä¸åç´ æ°çç¹ç¹ï¼

  1. åç´ æ°è¯å®æ¯ä» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§çè¿ç»­ç´ æ°çå¹æ¬¡å½¢å¼çä¹ç§¯ï¼

  2. æ°å¼å°çç´ æ°çå¹æ¬¡å¤§äºç­äºæ°å¼å¤§çç´ æ°ï¼å³ ð =ðð11ðð22â¯ððððn=p1k1p2k2â¯pnkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼æ ð1 â¥ð2 â¥ð3 â¥â¯ â¥ððk1â¥k2â¥k3â¥â¯â¥kn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£éï¼

  1. å¦æä¸æ¯ä» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§çè¿ç»­ç´ æ°ï¼é£ä¹å¦æå¹æ¬¡ä¸åï¼æç´ æ°åææ°å¼æ´å°çç´ æ°ï¼é£ä¹æ­¤æ¶å å­ä¸ªæ°ä¸åï¼ä½æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°å¼åå°äºï¼äº¤æ¢å°ä» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§çè¿ç»­ç´ æ°çæ¶å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼æå°ï¼

  2. å¦ææ°å¼å°çç´ æ°çå¹æ¬¡å°äºæ°å¼å¤§çç´ æ°çå¹ï¼é£ä¹å¦ææè¿ä¸¤ä¸ªç´ æ°äº¤æ¢ä½ç½®ï¼å¹æ¬¡ä¸åï¼ï¼é£ä¹æå¾ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­æ°éä¸åï¼ä½æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼åå°ï¼

å¦å¤è¿æä¸¤ä¸ªé®é¢ï¼

  1. å¯¹äºç»å®ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦æä¸¾å°åªä¸ä¸ªç´ æ°å¢ï¼

ææç«¯çæ åµå¤§ä¸äºå°±æ¯ ð =ð1ð2â¯ððn=p1p2â¯pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥åªè¦è¿ç»­ç´ æ°è¿ä¹å°åå¥½å°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼å¦ææä¸¾å°æ´å¤§çç´ æ°ï¼åæå³è¿å¿ å®æä¸ªä¹åç´ æ°çå¹æ¬¡ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å°±ä¸å¯è½æä¸ºåç´ æ°ï¼

  2. æä»¬è¦æä¸¾å°å¤å°æ¬¡å¹å¢ï¼

æä»¬èèä¸ä¸ªæç«¯æ åµï¼å½æä»¬æå°çç´ æ°çæä¸ªå¹æ¬¡å·²ç»æ¯æç»ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çæå¤§å¼ï¼å¤§çè¯ï¼é£ä¹å±å¼æå ¶ä»çå½¢å¼ï¼æå¤§å¹æ¬¡ä¸å®å°äºè¿ä¸ªå¹æ¬¡ï¼æç«¯æ åµä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸º 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬¡å¹ï¼é£ä¹æä¸¾å° âlog2â¡ðââlog2â¡nâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

ç»èæäºï¼é£ä¹æä»¬å ·ä½å¦ä½å ·ä½å®ç°å¢ï¼

æä»¬å¯ä»¥æå½åèµ°å°æ¯ä¸ä¸ªç´ æ°åé¢çæ¶ååä¸¾æä¸æ£µæ çæ ¹èç¹ï¼ç¶åä¸å±å±çå»æ¾ï¼æ¾å°ä»ä¹æ¶ååæ­¢å¢ï¼

  1. å½åèµ°å°çæ°å­å·²ç»å¤§äºæä»¬æ³è¦çæ°å­äºï¼

  2. å½åæä¸¾çå å­å·²ç»ç¨ä¸å°äºï¼

  3. å½åå å­å¤§äºæä»¬æ³è¦çå å­äºï¼

  4. å½åå å­æ­£å¥½æ¯æä»¬æ³è¦çå å­ï¼æ­¤æ¶å¤æ­æ¯å¦éè¦æ´æ°æå° ansans![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

ç¶å dfs éé¢ä¸æ­ä¸å±ä¸å±æä¸¾æ¬¡æ°ç»§ç»­å¾ä¸è¿­ä»£å¯ä»¥ï¼

### ä¾é¢

[Codeforces 27E. A number with a given number of divisors](https://codeforces.com/problemset/problem/27/E)

æ±å ·æç»å®é¤æ°ä¸ªæ°çæå°èªç¶æ°ï¼ç­æ¡ä¿è¯ä¸è¶ è¿ 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£é¢æè·¯

å¯¹äºè¿ç§é¢ï¼æä»¬åªè¦ä»¥å å­æ°ä¸º dfs çè¿åæ¡ä»¶åºåï¼ä¸æ­æ´æ°æ¾å°çæå°å¼å°±å¯ä»¥äºï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text #include <iostream> constexpr int p [ 15 ] = { 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43 , 47 }; // p ä¸­çç´ æ°ä¹ç§¯è¶ è¿äº 1e18 int n ; long long ans = 2e18 ; // u: å½åèèçè´¨æ°å¨ p ä¸­çä¸æ  // num: å½åææçæ°å¼ // cnt: å½åæ°å¼çå æ°ä¸ªæ° // pre: ä¸ä¸ä¸ªå å­çå¹æ¬¡ï¼éå®æ¬æ¬¡éæ©çå¹æ¬¡ void dfs ( int u , long long num , long long cnt , int pre ) { if ( cnt > n || u >= 15 ) return ; if ( cnt == n ) return ans = std :: min ( ans , num ), void (); for ( int i = 1 ; i <= pre ; ++ i ) { if ( num * p [ u ] > ans ) break ; // åªæ dfs ( u \+ 1 , num *= p [ u ], cnt * ( i \+ 1 ), i ); } } int main () { std :: cin >> n ; dfs ( 0 , 1 , 1 , 59 ); // floor(log2(1e18))=19 std :: cout << ans << std :: endl ; return 0 ; } ```   
---|---  
  
[ZOJ 2562 More Divisors](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827366061)

æ±ä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°ä¸­ï¼é¤æ°æå¤çæ°ï¼

è§£é¢æè·¯

æè·¯åä¸ï¼åªä¸è¿è¦æ¹æ¹ dfs çè¿åæ¡ä»¶ï¼æ³¨æè¿æ ·çé¢ç®çæ°æ®èå´ï¼32 ä½æ´æ°å¯è½æº¢åºï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <iostream> int p [ 16 ] = { 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43 , 47 , 53 }; unsigned long long n ; unsigned long long ans , ans_num ; // ans ä¸º n ä»¥å çæå¤§åç´ æ°ï¼ä¼æç»­æ´æ°ï¼ï¼ans_sum ä¸º // ansçå å­æ°ã // depth: å½åå¨æä¸¾ç¬¬å ä¸ªç´ æ° // temp: å½åå å­æ°éä¸º num çæ¶åçæ°å¼ // num: å½åå å­æ° // upï¼ä¸ä¸ä¸ªç´ æ°çå¹ï¼éå¶å½åå å­å¹æ¬¡ä¸ç void dfs ( int depth , unsigned long long temp , unsigned long long num , int up ) { if ( depth >= 16 || temp > n ) return ; if ( num > ans_num ) { // æ´æ°ç­æ¡ ans = temp ; ans_num = num ; } if ( num == ans_num && ans > temp ) ans = temp ; // æ´æ°ç­æ¡ for ( int i = 1 ; i <= up ; i ++ ) { if ( temp * p [ depth ] > n ) break ; // åªæï¼å¦æå ä¸ä¸ªè¿ä¸ªä¹æ°çç»ææ¯ansè¦å¤§ï¼åå¿ ä¸æ¯æä½³æ¹æ¡ dfs ( depth \+ 1 , temp *= p [ depth ], num * ( i \+ 1 ), i ); // åä¸ä¸ªè¯¥ä¹æ°ï¼è¿è¡å¯¹ä¸ä¸ä¸ªä¹æ°çæç´¢ } return ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> n ) { ans_num = 0 ; dfs ( 0 , 1 , 1 , 60 ); cout << ans << '\n' ; } return 0 ; } ```   
---|---  
  
## åèèµæä¸æ³¨é

  1. Rui-Juan Jing, Marc Moreno-Maza, Delaram Talaashrafi, "[Complexity Estimates for Fourier-Motzkin Elimination](https://arxiv.org/abs/1811.01510)", Journal of Functional Programming 16:2 (2006) pp 197-217.
  2. [æ°è®ºé¨åç¬¬ä¸èï¼ç´ æ°ä¸ç´ æ§æµè¯](http://www.matrix67.com/blog/archives/234)
  3. [MillerâRabin ä¸ PollardâRho å­¦ä¹ ç¬è®° - Bill Yang's Blog](https://blog.bill.moe/miller-rabin-notes/)
  4. [Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)
  5. [Fermat pseudoprime - Wikipedia](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
  6. [æ¡å­çç®æ³ç¬è®°ââåç´ æ°è¯¦è§£ï¼acm/OIï¼](https://zhuanlan.zhihu.com/p/41759808)
  7. [The Rabin-Miller Primality Test](http://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf)
  8. [Highly composite number - Wikipedia](https://en.wikipedia.org/wiki/Highly_composite_number)

* * *

  1. Pomerance, Carl, John L. Selfridge, and Samuel S. Wagstaff. "The pseudoprimes to 25â 10â¹." Mathematics of Computation 35, no. 151 (1980): 1003-1026. çå®ç 1 è¯´æäºï¼å¯¹äºåºå®çåºåº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è½å¤éè¿æ´å¼ºç MillerâRabin ç´ æ§æµè¯çåæ°ä¹æ¯æ ç©·å¤çï¼Â â©

  2. æ¬ç»è®ºåå ¶è¯æåèäº Crandall, Richard, and Carl Pomerance. Prime numbers: a computational perspective. New York, NY: Springer New York, 2005. çç¬¬ 3.5 èï¼Â â©

  3. Bach, Eric , "[Explicit bounds for primality testing and related problems](https://doi.org/10.2307%2F2008811)", Mathematics of Computation, 55:191 (1990) pp 355â380.Â â©

  4. æ´å¤ç±»ä¼¼çç»æè¯·åè [Deterministic variant of the MillerâRabin primality test](https://miller-rabin.appspot.com/#)ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/prime.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/prime.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [StudyingFather](https://github.com/StudyingFather), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [383494](https://github.com/383494), [Alpacabla](https://github.com/Alpacabla), [HeRaNO](https://github.com/HeRaNO), [abc1763613206](https://github.com/abc1763613206), [alphagocc](https://github.com/alphagocc), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [drkelo](https://github.com/drkelo), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [GuanghaoYe](https://github.com/GuanghaoYe), [H-J-Granger](https://github.com/H-J-Granger), [HHH2309](https://github.com/HHH2309), [isdanni](https://github.com/isdanni), [kenlig](https://github.com/kenlig), [lazyasn](https://github.com/lazyasn), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [r-value](https://github.com/r-value), [shawlleyw](https://github.com/shawlleyw), [shopee-jin](https://github.com/shopee-jin), [shuzhouliu](https://github.com/shuzhouliu), [sun2snow](https://github.com/sun2snow), [untitledunrevised](https://github.com/untitledunrevised), [void-mian](https://github.com/void-mian), [Voileexperiments](https://github.com/Voileexperiments), [weilycoder](https://github.com/weilycoder), [xtlsoft](https://github.com/xtlsoft), [yusancky](https://github.com/yusancky), [YuzhenQin1](https://github.com/YuzhenQin1), [Siger Young](mailto:siger-young@users.noreply.github.com), [Siger Young](https://github.com/Siger Young), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TrisolarisHD](https://github.com/TrisolarisHD)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
