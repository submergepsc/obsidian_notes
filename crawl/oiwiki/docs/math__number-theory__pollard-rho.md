# åè§£è´¨å æ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/pollard-rho/

# åè§£è´¨å æ°

## å¼å ¥

ç»å®ä¸ä¸ªæ­£æ´æ° ð âð+NâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯å¿«éæ¾å°å®çä¸ä¸ª [éå¹³å¡å æ°](../basic/)ï¼

èèæ´ç´ ç®æ³ï¼å æ°æ¯æå¯¹åå¸çï¼ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå æ°å¯ä»¥è¢«åæä¸¤åï¼å³ [2,âð][2,N]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å [âð +1,ð)[N+1,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªéè¦æ [2,âð][2,N]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éçæ°éåä¸éï¼åæ ¹æ®é¤æ³å°±å¯ä»¥æ¾åºè³å°ä¸¤ä¸ªå æ°äºï¼è¿ä¸ªæ¹æ³çæ¶é´å¤æåº¦ä¸º ð(âð)O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å½ ð â¥1018Nâ¥1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è¿ä¸ªç®æ³çè¿è¡æ¶é´æä»¬æ¯æ æ³æ¥åçï¼å¸æææ´ä¼ç§çç®æ³ï¼ä¸ç§æ³æ³æ¯éè¿éæºçæ¹æ³ï¼çæµä¸ä¸ªæ°æ¯ä¸æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå æ°ï¼å¦æè¿æ°å¥½å¯ä»¥å¨ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦ä¸æ±è§£ç­æ¡ï¼ä½æ¯å¯¹äº ð â¥1018Nâ¥1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°æ®ï¼æåçæµçæ¦çæ¯ 1101811018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), ææçæµçæ¬¡æ°æ¯ 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ææ¯å¨ [2,âð][2,N]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿è¡çæµï¼æåçä¼å¤§ä¸äºï¼æä»¬å¸æææ¹æ³æ¥ä¼åçæµï¼

## æ´ç´ ç®æ³

æç®åçç®æ³å³ä¸ºä» [2,âð][2,N]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡éåï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text vector < int > breakdown ( int N ) { vector < int > result ; for ( int i = 2 ; i * i <= N ; i ++ ) { if ( N % i == 0 ) { // å¦æ i è½å¤æ´é¤ Nï¼è¯´æ i ä¸º N çä¸ä¸ªè´¨å å­ï¼ while ( N % i == 0 ) N /= i ; result . push_back ( i ); } } if ( N != 1 ) { // è¯´æåç»è¿æä½ä¹å N çä¸äºä¸ä¸ªç´ æ° result . push_back ( N ); } return result ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text def breakdown ( N ): result = [] for i in range ( 2 , int ( sqrt ( N )) \+ 1 ): if N % i == 0 : # å¦æ i è½å¤æ´é¤ Nï¼è¯´æ i ä¸º N çä¸ä¸ªè´¨å å­ï¼ while N % i == 0 : N //= i result . append ( i ) if N != 1 : # è¯´æåç»è¿æä½ä¹å N çä¸äºä¸ä¸ªç´ æ° result . append ( N ) return result ```   
---|---  
  
æä»¬è½å¤è¯æ `result` ä¸­çææå ç´ å³ä¸º `N` çå ¨ä½ç´ å æ°ï¼

è¯æ `result` ä¸­å³ä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½ç´ å æ°

é¦å èå¯ `N` çååï¼å½å¾ªç¯è¿è¡å° `i` ç»ææ¶ï¼ç±äºåæ§è¡ç»æ `while(N % i == 0) N /= i` é¨åï¼`i` ä¸åæ´é¤ `N`ï¼èä¸ï¼æ¯æ¬¡é¤å»ä¸ä¸ªå å­ï¼é½è½å¤ä¿è¯ `N` ä»æ´é¤ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸¤ç¹ä¿è¯äºï¼å½å¾ªç¯è¿è¡å° `i` å¼å§æ¶ï¼`N` æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå å­ï¼ä¸ä¸è¢«ä»»ä½å°äº `i` çæ´æ°æ´é¤ï¼

å ¶æ¬¡è¯æ `result` ä¸­çå ç´ åä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå å­ï¼å½å¾ªç¯è¿è¡å° `i` æ¶ï¼è½å¤å¨ `result` ä¸­å­å ¥ `i` çæ¡ä»¶æ¯ `N % i == 0`ï¼è¿è¯´æ `i` æ´é¤ `N`ï¼ä¸å·²ç»è¯´æ `N` æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå å­ï¼æ èæ `i` æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå å­ï¼å½å¯¹ `i` çå¾ªç¯ç»ææ¶ï¼è¥ `N` ä¸ä¸ºä¸ï¼ä¹ä¼å­å ¥ `result`ï¼æ­¤æ¶å®æ ¹æ®åæï¼ä¹å¿ ç¶æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå å­ï¼

å ¶æ¬¡è¯æ `result` ä¸­åä¸ºç´ æ°ï¼æä»¬åè®¾å­å¨ä¸ä¸ªå¨ `result` ä¸­çåæ° ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¿ ç¶å­å¨ `i` ä¸è¶ è¿ âð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»¡è¶³ `i` æ¯ `K` çä¸ä¸ªå å­ï¼è¿æ ·ç ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è½ä½ä¸ºå¾ªç¯ä¸­çæä¸ª `i` å­å ¥ `result`ï¼å ä¸ºç¬¬ä¸æ®µå·²ç»è¯´æï¼å½å¾ªç¯å° ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼`N` ä¸è¢«ä»»ä½å°äº ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `i` æ´é¤ï¼è¿æ ·ç ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸å¯è½å¨å¾ªç¯ç»æåå å ¥ï¼å ä¸ºå¾ªç¯éåºçæ¡ä»¶æ¯ `i * i > N`ï¼æ èå·²ç»éåå®äºææä¸è¶ è¿ âð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `i`ï¼èä¸æ®ä¸ææè¯´ï¼è¿äº `i` ç»ä¸è½æ´é¤ç®åç `N`ï¼äº¦å³ ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æåè¯æï¼ææ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å å­å¿ ç¶åºç°å¨ `result` ä¸­ï¼ä¸å¦¨åè®¾ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªç´ å å­ï¼ä½å¹¶æ²¡æåºç°å¨ `result` ä¸­ï¼æ ¹æ®ä¸æçè®¨è®ºï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è½æ¯å¾ªç¯ä¸­åºç°è¿ç `i`ï¼è®¾ `i` æ¯éåºå¾ªç¯åæåç `i`ï¼å `i` ä¸¥æ ¼å°äº ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èéåºå¾ªç¯åç `N` ä¸è¢«ä¹åç `i` æ´é¤ï¼æ è ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´é¤ `N`ï¼æä»¥æåç `N` å¤§äºä¸ï¼åæ ¹æ®åææè¿°ï¼å®å¿ ç¶æ¯ç´ æ°ï¼å `N` å°±ç­äº ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ ä¼å¨æåå å ¥ `result`ï¼ä¸åè®¾çç¾ï¼

å¼å¾æåºçæ¯ï¼å¦æå¼å§å·²ç»æäºä¸ä¸ªç´ æ°è¡¨çè¯ï¼æ¶é´å¤æåº¦å°ä» ð(âð)O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸éå° ð(âðlnâ¡ð)O(Nlnâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å» [ç­æ³](../sieve/) å¤æ¥é æ´å¤æè¡¨çä¿¡æ¯ï¼

ä¾é¢ï¼[CF 1445C](https://codeforces.com/problemset/problem/1445/C)

## Pollard Rho ç®æ³

### å¼å ¥

å©ç¨æ´åç®æ³è·å¾ä¸ä¸ªéå¹³å¡å å­çå¤æåº¦ä¸º ð(ð) =ð(âð)O(p)=O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°ç´ å å­ï¼èä¸é¢è¦ä»ç»ç Pollard-Rho ç®æ³æ¯ä¸ç§éæºåç®æ³ï¼å¯ä»¥å¨ ð(âð) =ð(ð1/4)O(p)=O(N1/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå¤æåº¦è·å¾ä¸ä¸ªéå¹³å¡å å­ï¼**æ³¨æ** ï¼éå¹³å¡å å­ä¸ä¸å®æ¯ç´ å å­ï¼ï¼

å®çæ ¸å¿æ³æ³æ¯ï¼å¯¹äºä¸ä¸ªéæºèªæ å° ð :â¤ð ââ¤ðf:ZpâZp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»ä»»ä½ä¸ç¹ ð¥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼è¿­ä»£è®¡ç® ð¥ð =ð(ð¥ðâ1)xn=f(xnâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°å¨ ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æææ¶é´å è¿å ¥å¾ªç¯ï¼å¦æè½å¤æ¾å° ð¥ð â¡ð¥ð(modð)xiâ¡xj(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´é¤ gcd(|ð¥ð âð¥ð|,ð)gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æå¤§å ¬çº¦æ°å°±æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªéå¹³å¡å å­ï¼

è¦çè§£è¿å ¥å¾ªç¯çæææ¶é´ä¸º ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥ä»çæ¥æè®ºä¸­è·å¾å¯åï¼

### çæ¥æè®º

ä¸èèåºçå¹´ä»½ï¼åè®¾æ¯å¹´é½æ¯ 365 å¤©ï¼ï¼é®ï¼ä¸ä¸ªæ¿é´ä¸­è³å°å¤å°äººï¼æè½ä½¿å ¶ä¸­ä¸¤ä¸ªäººçæ¥ç¸åçæ¦çè¾¾å° 50%50%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)?

è§£ï¼åè®¾ä¸å¹´æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤©ï¼æ¿é´ä¸­æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äººï¼ç¨æ´æ° 1,2,â¦,ð1,2,â¦,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹è¿äºäººè¿è¡ç¼å·ï¼åå®æ¯ä¸ªäººççæ¥åååå¸äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤©ä¹ä¸­ï¼ä¸ä¸¤ä¸ªäººççæ¥ç¸äºç¬ç«ï¼

è®¾ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäººçæ¥äºä¸ç¸åä¸ºäºä»¶ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), åäºä»¶ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¦çä¸º

ð(ð´)=ðâ1âð=0ðâððP(A)=âi=0kâ1nâin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è³å°æä¸¤ä¸ªäººçæ¥ç¸åçæ¦çä¸º ð(ââð´) =1 âð(ð´)P(Aâ)=1âP(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®é¢æå¯ç¥ ð(ââð´) â¥12P(Aâ)â¥12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), é£ä¹å°±æ

ð(ð´)=ðâ1âð=0ðâððâ¤12P(A)=âi=0kâ1nâinâ¤12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±ä¸ç­å¼ 1 +ð¥ â¤eð¥1+xâ¤ex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯å¾

ð(ð´)â¤ðâ1âð=1expâ¡(âðð)=expâ¡(âð(ðâ1)2ð)P(A)â¤âi=1kâ1expâ¡(âin)=expâ¡(âk(kâ1)2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤

expâ¡(âð(ðâ1)2ð)â¤12â¹ð(ð´)â¤12expâ¡(âk(kâ1)2n)â¤12â¹P(A)â¤12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å° ð =365n=365![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»£å ¥ï¼è§£å¾ ð â¥23kâ¥23![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ä¸ä¸ªæ¿é´ä¸­è³å° 2323![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äººï¼ä½¿å ¶ä¸­ä¸¤ä¸ªäººçæ¥ç¸åçæ¦çè¾¾å° 50%50%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), ä½è¿ä¸ªæ°å­¦äºå®åååç´è§ï¼æ ç§°ä¹ä¸ºä¸ä¸ªæè®ºï¼

å½ ð >56k>56![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð =365n=365![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åºç°ä¸¤ä¸ªäººåä¸å¤©çæ¥çæ¦çå°å¤§äº 99%99%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1ï¼é£ä¹å¨ä¸å¹´æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤©çæ åµä¸ï¼å½æ¿é´ä¸­æ 12(â8ðlnâ¡2+1 +1) ââ2ðlnâ¡212(8nlnâ¡2+1+1)â2nlnâ¡2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäººæ¶ï¼è³å°æä¸¤ä¸ªäººççæ¥ç¸åçæ¦ççº¦ä¸º 50%50%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±»ä¼¼å°å¯ä»¥è®¡ç®ï¼éæºååå°éåä¸åçæ¥ï¼é¦æ¬¡è·å¾éå¤çæ¥éè¦çäººæ°çææä¹æ¯ ð(âð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾è¿ä¸äººæ°ä¸º ðX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å

ð¸(ð)=ð+1âð¥=1ð(ðâ¥ð¥+1)=ðâð¥=0ð!(ðâð¥)!ðð¥=âðð2â13+ð(1).E(X)=âx=1n+1P(Xâ¥x+1)=âx=0nn!(nâx)!nx=Ïn2â13+o(1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å¯åæä»¬ï¼å¦æå¯ä»¥éæºéåä¸åæ°å­ï¼åºç°éå¤æ°å­éè¦çæ½æ ·è§æ¨¡çææä¹æ¯ ð(âð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

### å©ç¨æå¤§å ¬çº¦æ°æ±åºä¸ä¸ªçº¦æ°

å®é æå»ºä¸åæ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæºæ°åå¹¶ä¸ç°å®ï¼å ä¸º ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­£æ¯éè¦æ±çï¼æä»¥ï¼æä»¬éè¿ ð(ð¥) =(ð¥2 +ð)modðf(x)=(x2+c)modN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥çæä¸ä¸ªä¼ªéæºæ°åºå {ð¥ð}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éæºåä¸ä¸ª ð¥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ð¥2 =ð(ð¥1),Â ð¥3 =ð(ð¥2),Â â¦,Â ð¥ð =ð(ð¥ðâ1)x2=f(x1),Â x3=f(x2),Â â¦,Â xi=f(xiâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð â[1,ð)câ[1,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªéæºéåçå¸¸æ°ï¼

è¿ééåçå½æ°å®¹æè®¡ç®ï¼ä¸å¾å¾å¯ä»¥çæç¸å½éæºçåºåï¼ä½å®å¹¶ä¸æ¯å®å ¨éæºçï¼ä¸¾ä¸ªä¾å­ï¼è®¾ ð =50,Â ð =6,Â ð¥1 =1n=50,Â c=6,Â x1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(ð¥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæçæ°æ®ä¸º

1,7,5,31,17,45,31,17,45,31,â¦1,7,5,31,17,45,31,17,45,31,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥åç°æ°æ®å¨ ð¥4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥åé½å¨ 31,17,4531,17,45![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´å¾ªç¯ï¼å¦æå°è¿äºæ°å¦ä¸å¾ä¸æ ·æåèµ·æ¥ï¼ä¼åç°è¿ä¸ªå¾åé ·ä¼¼ä¸ä¸ª ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç®æ³ä¹å æ­¤å¾å rhoï¼

![pollard-rho](./images/pollard-rho.svg)

æ´éè¦çæ¯ï¼è¿æ ·çå½æ°ç¡®å®æä¾äº â¤ðZp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ä¸ªèªæ å°ï¼ä¹å°±æ¯è¯´ï¼å®æ»¡è¶³æ§è´¨ï¼å¦æ ð¥ â¡ð¦(modð)xâ¡y(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð(ð¥) â¡ð(ð¦)(modð)f(x)â¡f(y)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è¥ ð¥ â¡ð¦(modð)xâ¡y(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¥2 +ð â¡ð¦2 +ð(modð)x2+câ¡y2+c(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ³¨æå°ï¼ð(ð¥) =ð¥2 +ð âðð¥ðf(x)=x2+câkxN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿é ðð¥kx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªä¾èµäº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°ï¼ä¸ ð|ðp|N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æ ð(ð¥) =ð¥2 +ð(modð)f(x)=x2+c(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å è ð(ð¥) =ð(ð¦)(modð)f(x)=f(y)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä½ä¸º â¤ðZp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¼ªéæºèªæ å°åå¤è¿­ä»£å¾å°çåºåï¼{ð¥ðmodð}{xnmodp}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæææ¶é´å å°±ä¼åºç°éå¤ï¼åªè¦æä»¬è§å¯å°è¿æ ·çéå¤ ð¥ð â¡ð¥ð(modð)xiâ¡xj(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥æ ¹æ® gcd(|ð¥ð âð¥ð|,ð)gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±åºä¸ä¸ª ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå¹³å¡å å­ï¼æ³¨æå°ï¼ç±äº ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æªç¥ï¼æä»¬å¹¶æ²¡æåæ³ç´æ¥å¤æ­éå¤çåçï¼ä¸ä¸ªç®åçå¤æ­æ¹æ³æ­£æ¯ gcd(|ð¥ð âð¥ð|,ð)gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¥æ ¼å¤§äºä¸ï¼

è¿ä¸ç®æ³å¹¶ä¸æ¯æ»è½æåçï¼å ä¸º gcd(|ð¥ð âð¥ð|,ð)gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½ç­äº ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ð¥ð â¡ð¥ð(modð)xiâ¡xj(modN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼{ð¥ðmodð}{xnmodp}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¦æ¬¡åçéå¤æ¶ï¼æ°å¥½ {ð¥ð}{xn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åçéå¤äºï¼æä»¬æ²¡æå¾å°ä¸ä¸ªéå¹³å¡å å­ï¼èä¸ï¼{ð¥ð}{xn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§å¾ªç¯åï¼åç»§ç»­è¿­ä»£ä¹æ²¡ææä¹äºï¼å ä¸ºä¹ååªä¼éå¤è¿ä¸å¾ªç¯ï¼è¯¥ç®æ³åºè¾åºåè§£å¤±è´¥ï¼éè¦æ´æ¢ ð(ð¥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­éåç ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éæ°åè§£ï¼

æ ¹æ®ä¸æåæï¼çè®ºä¸ï¼ä»»ä½æ»¡è¶³ âð¥ â¡ð¦(modð),ð(ð¥) â¡ð(ð¦)(modð)âxâ¡y(modp),f(x)â¡f(y)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è½å¤ä¿è¯ä¸å®ä¼ªéæºæ§çå½æ° ð(ð¥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾å¦æäºå¤é¡¹å¼å½æ°ï¼é½å¯ä»¥ç¨å¨æ­¤å¤ï¼å®è·µä¸­ï¼ä¸»è¦ä½¿ç¨ ð(ð¥) =ð¥2 +ðÂ (ð â 0, â2)f(x)=x2+cÂ (câ 0,â2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼2

### å®ç°

æä»¬éè¦å®ç°çç®æ³ï¼è½å¤å¨è¿­ä»£è¿ç¨ä¸­å¿«éå¤æ­ {ð¥ðmodð}{xnmodp}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦å·²ç»åºç°éå¤ï¼å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä»¥ â¤ðZp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºé¡¶ç¹çæåå¾ä¸çè¾¹ï¼æä»¬å®é è¦å®ç°çæ¯ä¸ä¸ªå¤ç¯ç®æ³ï¼åªæ¯å°å¤ç­æ¹ä¸ºäºå¤æ­ gcd(|ð¥ð âð¥ð|,ð)gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦å¤§äºä¸ï¼

#### Floyd å¤ç¯

åè®¾ä¸¤ä¸ªäººå¨èµè·ï¼A çéåº¦å¿«ï¼B çéåº¦æ ¢ï¼ç»è¿ä¸å®æ¶é´åï¼A ä¸å®ä¼å B ç¸éï¼ä¸ç¸éæ¶ A è·è¿çæ»è·ç¦»åå» B è·è¿çæ»è·ç¦»ä¸å®æ¯åé¿çåæ°ï¼

è®¾ ð =ð(0),ð =ð(ð(0))a=f(0),b=f(f(0))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸æ¬¡æ´æ° ð =ð(ð),ð =ð(ð(ð))a=f(a),b=f(f(b))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦æ£æ¥å¨æ´æ°è¿ç¨ä¸­ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦ç¸ç­ï¼å¦æç¸ç­äºï¼é£ä¹å°±åºç°äºç¯ï¼

æä»¬æ¯æ¬¡ä»¤ ð =gcd(|ð¥ð âð¥ð|,ð)d=gcd(|xiâxj|,N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤æ­ d æ¯å¦æ»¡è¶³ 1 <ð <ð1<d<N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¥æ»¡è¶³åå¯ç´æ¥è¿å ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð =ðd=N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¯´æ {ð¥ð}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·²ç»å½¢æç¯ï¼å¨å½¢æç¯æ¶å°±ä¸è½åç»§ç»­æä½äºï¼ç´æ¥è¿å ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬èº«ï¼å¹¶ä¸å¨åç»­æä½éè°æ´éæºå¸¸æ° ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éæ°åè§£ï¼

åºäº Floyd å¤ç¯ç Pollard-Rho ç®æ³

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text ll Pollard_Rho ( ll N ) { if ( N == 4 ) return 2 ; // å ä¸ºä¸å¼å§è·³äºä¸¤æ­¥ï¼æä»¥éè¦ç¹å¤ä¸ä¸ 4 ll c = rand () % ( N \- 1 ) \+ 1 ; ll t = f ( 0 , c , N ); ll r = f ( f ( 0 , c , N ), c , N ); while ( t != r ) { ll d = gcd ( abs ( t \- r ), N ); if ( d > 1 ) return d ; t = f ( t , c , N ); r = f ( f ( r , c , N ), c , N ); } return N ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text import random def Pollard_Rho ( N ): if N == 4 : return 2 # å ä¸ºä¸å¼å§è·³äºä¸¤æ­¥ï¼æä»¥éè¦ç¹å¤ä¸ä¸ 4 c = random . randint ( 1 , N \- 1 ) t = f ( 0 , c , N ) r = f ( f ( 0 , c , N ), c , N ) while t != r : d = gcd ( abs ( t \- r ), N ) if d > 1 : return d t = f ( t , c , N ) r = f ( f ( r , c , N ), c , N ) return N ```   
---|---  
  
#### Brent å¤ç¯

å®é ä¸ï¼Floyd å¤ç¯ç®æ³å¯ä»¥æå¸¸æ°ä¸çæ¹è¿ï¼Brent å¤ç¯ä» ð =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§éå¢ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½®ï¼è®© A ç­å¨åå°ï¼B ååç§»å¨ 2ð2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­¥ï¼å¦æå¨è¿ç¨ä¸­ B éå°äº Aï¼åè¯´æå·²ç»å¾å°ç¯ï¼å¦åè®© A ç¬ç§»å° B çä½ç½®ï¼ç¶åç»§ç»­ä¸ä¸è½®ï¼

å¯ä»¥è¯æ3ï¼è¿æ ·å¾å°ç¯ä¹åéè¦è°ç¨ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬¡æ°æ°¸è¿ä¸å¤§äº Floyd å¤ç¯ç®æ³ï¼åè®ºæä¸­çæµè¯è¡¨æï¼Brent å¤ç¯éè¦çå¹³åæ¶é´ç¸è¾äº Floyd å¤ç¯åå°äº 24%24%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### åå¢ä¼å

æ è®ºæ¯ Floyd å¤ç¯è¿æ¯ Brent å¤ç¯ï¼è¿­ä»£æ¬¡æ°é½æ¯ ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼ä½æ¯æ¯æ¬¡è¿­ä»£é½ç¨ gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤æ­æ¯å¦æç¯ä¼ææ ¢ç®æ³è¿è¡éåº¦ï¼å¯ä»¥éè¿ä¹æ³ç´¯ç§¯æ¥åå°æ± gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬¡æ°ï¼

ç®åæ¥è¯´ï¼å¦æ gcd(ð,ð) >1gcd(a,N)>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ gcd(ððmodð,ð) =gcd(ðð,ð) >1gcd(abmodN,N)=gcd(ab,N)>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºä»»æ ð ââ+bâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼ä¹å°±æ¯è¯´ï¼å¦æè®¡ç®å¾å° gcd(â|ð¥ð âð¥ð|modð,ð) >1gcd(â|xiâxj|modN,N)>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å¿ ç¶æå ¶ä¸­ä¸å¯¹ (ð¥ð,ð¥ð)(xi,xj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ gcd(|ð¥ð âð¥ð|,ð) >1gcd(|xiâxj|,N)>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æè¯¥ä¹ç§¯å¨æä¸æ¶å»å¾å°é¶ï¼ååè§£å¤±è´¥ï¼éåºå¹¶è¿å ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬èº«ï¼

å¦ææ¯ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹è®¡ç®ä¸æ¬¡ gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç®æ³å¤æåº¦éä½å° ð(âð +ðâ1âðlogâ¡ð)O(p+kâ1plogâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éï¼logâ¡ðlogâ¡N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåæ¬¡è®¡ç® gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼éï¼æ³¨æå° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å logâ¡ðlogâ¡N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤§è´åé¶æ¶ï¼å¯ä»¥å¾å° ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå¤æåº¦ï¼å ·ä½å®ç°ä¸­ï¼å¤§å¤éå ð =128k=128![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿éæä¾ Brent å¤ç¯ä¸å ä¸åå¢ä¼åç Pollard-Rho ç®æ³å®ç°ï¼

å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text ll Pollard_Rho ( ll x ) { ll t = 0 ; ll c = rand () % ( x \- 1 ) \+ 1 ; ll s = t ; int step = 0 , goal = 1 ; ll val = 1 ; for ( goal = 1 ;; goal <<= 1 , s = t , val = 1 ) { for ( step = 1 ; step <= goal ; ++ step ) { t = f ( t , c , x ); val = val * abs ( t \- s ) % x ; // å¦æ val ä¸º 0ï¼éåºéæ°åè§£ if ( ! val ) return x ; if ( step % 127 == 0 ) { ll d = gcd ( val , x ); if ( d > 1 ) return d ; } } ll d = gcd ( val , x ); if ( d > 1 ) return d ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text from random import randint from math import gcd def Pollard_Rho ( x ): c = randint ( 1 , x \- 1 ) s = t = f ( 0 , c , x ) goal = val = 1 while True : for step in range ( 1 , goal \+ 1 ): t = f ( t , c , x ) val = val * abs ( t \- s ) % x if val == 0 : return x # å¦æ val ä¸º 0ï¼éåºéæ°åè§£ if step % 127 == 0 : d = gcd ( val , x ) if d > 1 : return d d = gcd ( val , x ) if d > 1 : return d s = t goal <<= 1 val = 1 ```   
---|---  
  
#### å¤æåº¦

Pollard-Rho ç®æ³ä¸­çææè¿­ä»£æ¬¡æ°ä¸º ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿é ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°ç´ å å­ï¼å ·ä½å®ç°æ è®ºæ¯éç¨ Floyd å¤ç¯è¿æ¯ Brent å¤ç¯ï¼å¦æä¸ä½¿ç¨åå¢ä¼åï¼ææå¤æåº¦é½æ¯ ð(âðlogâ¡ð)O(plogâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨å ä¸åå¢ä¼ååï¼å¯ä»¥è¿ä¼¼å¾å° ð(âð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå¤æåº¦ï¼

å¼å¾ä¸æçæ¯ï¼åæåæåºäºçæ¯å®å ¨éæºçèªæ å°å½æ°ï¼ä½ Pollard-Rho ç®æ³å®é ä½¿ç¨çæ¯ä¼ªéæºå½æ°ï¼æä»¥è¯¥ç®æ³å¹¶æ²¡æä¸¥æ ¼çå¤æåº¦åæï¼å®è·µä¸­éå¸¸è·å¾è¾å¿«ï¼

#### ä¾é¢ï¼æ±ä¸ä¸ªæ°çæå¤§ç´ å å­

ä¾é¢ï¼[P4718ãæ¨¡æ¿ãPollard-Rho ç®æ³](https://www.luogu.com.cn/problem/P4718)

å¯¹äºä¸ä¸ªæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨ [Miller Rabin ç®æ³](../prime/#millerrabin-ç´) å¤æ­æ¯å¦ä¸ºç´ æ°ï¼å¦ææ¯å°±å¯ä»¥ç´æ¥è¿åäºï¼å¦åç¨ Pollard-Rho ç®æ³æ¾ä¸ä¸ªå å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¤å»å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åéå½åè§£ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨ Miller Rabin å¤æ­æ¯å¦åºç°è´¨å å­ï¼å¹¶ç¨ max_factor æ´æ°å°±å¯ä»¥æ±åºæå¤§è´¨å å­äºï¼ç±äºè¿ä¸ªé¢ç®çæ°æ®è¿äºåºå¤§ï¼ç¨ Floyd å¤ç¯çæ¹æ³æ¯ä¸å¤çï¼è¿ééç¨åå¢ä¼åçæ¹æ³ï¼

å®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 ``` |  ```text #include <algorithm> #include <cstdlib> #include <ctime> #include <iostream> using namespace std ; using ll = long long ; using ull = unsigned long long ; int t ; ll max_factor , n ; ll gcd ( ll a , ll b ) { if ( b == 0 ) return a ; return gcd ( b , a % b ); } ll bmul ( ll a , ll b , ll m ) { // å¿«éä¹ ull c = ( ull ) a * ( ull ) b \- ( ull )(( long double ) a / m * b \+ 0.5L ) * ( ull ) m ; if ( c < ( ull ) m ) return c ; return c \+ m ; } ll qpow ( ll x , ll p , ll mod ) { // å¿«éå¹ ll ans = 1 ; while ( p ) { if ( p & 1 ) ans = bmul ( ans , x , mod ); x = bmul ( x , x , mod ); p >>= 1 ; } return ans ; } bool Miller_Rabin ( ll p ) { // å¤æ­ç´ æ° if ( p < 2 ) return false ; if ( p == 2 ) return true ; if ( p == 3 ) return true ; ll d = p \- 1 , r = 0 ; while ( ! ( d & 1 )) ++ r , d >>= 1 ; // å°då¤çä¸ºå¥æ° for ( ll k = 0 ; k < 10 ; ++ k ) { ll a = rand () % ( p \- 2 ) \+ 2 ; ll x = qpow ( a , d , p ); if ( x == 1 || x == p \- 1 ) continue ; for ( int i = 0 ; i < r \- 1 ; ++ i ) { x = bmul ( x , x , p ); if ( x == p \- 1 ) break ; } if ( x != p \- 1 ) return false ; } return true ; } ll Pollard_Rho ( ll x ) { ll s = 0 , t = 0 ; ll c = ( ll ) rand () % ( x \- 1 ) \+ 1 ; int step = 0 , goal = 1 ; ll val = 1 ; for ( goal = 1 ;; goal *= 2 , s = t , val = 1 ) { // åå¢ä¼å for ( step = 1 ; step <= goal ; ++ step ) { t = ( bmul ( t , t , x ) \+ c ) % x ; val = bmul ( val , abs ( t \- s ), x ); if (( step % 127 ) == 0 ) { ll d = gcd ( val , x ); if ( d > 1 ) return d ; } } ll d = gcd ( val , x ); if ( d > 1 ) return d ; } } void fac ( ll x ) { if ( x <= max_factor || x < 2 ) return ; if ( Miller_Rabin ( x )) { // å¦æxä¸ºè´¨æ° max_factor = max ( max_factor , x ); // æ´æ°ç­æ¡ return ; } ll p = x ; while ( p >= x ) p = Pollard_Rho ( x ); // ä½¿ç¨è¯¥ç®æ³ while (( x % p ) == 0 ) x /= p ; fac ( x ), fac ( p ); // ç»§ç»­åä¸åè§£xåp } int main () { cin >> t ; while ( t \-- ) { srand (( unsigned ) time ( NULL )); max_factor = 0 ; cin >> n ; fac ( n ); if ( max_factor == n ) // æå¤§çè´¨å æ°å³èªå·± cout << "Prime \n " ; else cout << max_factor << '\n' ; } return 0 ; } ```   
---|---  
  
## åèèµæä¸é¾æ¥

* * *

  1. <https://en.wikipedia.org/wiki/Birthday_problem#Reverse_problem>Â â©

  2. Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A. (2001). Handbook of Applied Cryptography. Section 3.11 and 3.12.Â â©

  3. Brent, R. P. (1980), An improved Monte Carlo factorization algorithm, BIT Numerical Mathematics, 20(2): 176â184, doi:10.1007/BF01933190Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/pollard-rho.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/pollard-rho.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [383494](https://github.com/383494), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [ShaoChenHeng](https://github.com/ShaoChenHeng), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [CCXXXI](https://github.com/CCXXXI), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [Menci](https://github.com/Menci), [PeterlitsZo](https://github.com/PeterlitsZo), [shuzhouliu](https://github.com/shuzhouliu), [usamoi](https://github.com/usamoi), [2740365712](https://github.com/2740365712), [Backl1ght](https://github.com/Backl1ght), [Bubbleioa](https://github.com/Bubbleioa), [GoodCoder666](https://github.com/GoodCoder666), [Great-designer](https://github.com/Great-designer), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [leoleoasd](https://github.com/leoleoasd), [megakite](https://github.com/megakite), [SaisycJiang](https://github.com/SaisycJiang), [shawlleyw](https://github.com/shawlleyw), [TianKong-y](https://github.com/TianKong-y), [Watersail2005](https://github.com/Watersail2005), [xyf007](https://github.com/xyf007)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
