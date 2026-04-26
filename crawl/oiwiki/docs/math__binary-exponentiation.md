# å¿«éå¹ - OI Wiki

- Source: https://oi-wiki.org/math/binary-exponentiation/

# å¿«éå¹

## å¼å ¥

**å¿«éå¹** ï¼fast exponentiationï¼ï¼ä¹ç§° **äºè¿å¶åå¹** ï¼binary exponentiationï¼æ **å¹³æ¹åå¹æ³** ï¼exponentiation by squaringï¼ï¼æ¯ä¸ä¸ªå¨ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å è®¡ç® ððan![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå°æå·§ï¼èæ´åçè®¡ç®éè¦ Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´ï¼

è¿ä¸ªæå·§å¯ä»¥åºç¨äºä»»ä½ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹æ³æ»¡è¶³ç»åå¾çåºæ¯ä¸­ï¼ä¾å¦æ¨¡æä¹ä¸åå¹ãç©éµå¹ç­ï¼è¯¦è§åæ åºç¨ ä¸èï¼

## è¿ç¨

è®¡ç® ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡æ¹è¡¨ç¤ºå° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¨ä¸èµ·ï¼ðð =ðÃðâ¯ÃðâðÂ ä¸ª aan=aÃaâ¯ÃaânÂ ä¸ª a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶èå½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤ªå¤§æåæ¬¡ä¹æ³å¼éå¤ªå¤§çæ¶ä¾¯ï¼è¿ç§æ¹æ³å°±ä¸å¤ªéç¨äºï¼äºè¿å¶åå¹çæ³æ³æ¯ï¼å°åå¹çä»»å¡æç §ææ°ç **äºè¿å¶è¡¨ç¤º** æ¥åå²ææ´å°çä»»å¡ï¼

ä¾å­

åè®¾è¦è®¡ç® 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå°å®å±å¼ä¸ºè¿ä¹å¼ï¼éè¦ 13 â1 =1213â1=12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³ï¼ä½æ¯ï¼å ä¸º

313=3(1101)2=38Ã34Ã31,313=3(1101)2=38Ã34Ã31,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼åªè¦è½å¿«éè®¡ç®åº 31,32,34,3831,32,34,38![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±è½éè¿ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³è®¡ç®åº 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼äºæ¯ï¼åªéè¦ç¥éä¸ä¸ªå¿«éçæ¹æ³æ¥è®¡ç®ä¸è¿° 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç 2ð2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹çåºåï¼è¿æ¯å®¹æçï¼å ä¸ºå ä¸ºåºåä¸­ï¼é¤ç¬¬ä¸ä¸ªï¼ä»»æä¸ä¸ªå ç´ é½æ¯å ¶åä¸ä¸ªå ç´ çå¹³æ¹ï¼

æ ¹æ®è¿äºåæï¼å¯ä»¥å¾å° 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡ç®è¿ç¨å¦ä¸ï¼

31=3,32=(31)2=32=9,34=(32)2=92=81,38=(34)2=812=6561,313=6561Ã81Ã3=1594323.31=3,32=(31)2=32=9,34=(32)2=92=81,38=(34)2=812=6561,313=6561Ã81Ã3=1594323.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ç¨ä¸­ï¼åªè¿è¡äº 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³è¿ç®ï¼

è¿å°±æ¯å¿«éå¹çåºæ¬æ³æ³ï¼è³äºå ·ä½å®ç°ï¼æä¸¤ç§å¸¸è§ççæ¬ï¼

### è¿­ä»£çæ¬

è®¾ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºä¸º (ðð¡ðð¡â1â¯ð1ð0)2(ntntâ1â¯n1n0)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼æ

ð=ðð¡2ð¡+ðð¡â12ð¡â1+â¯+ð121+ð020,n=nt2t+ntâ12tâ1+â¯+n121+n020,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð â{0,1}niâ{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å°±æ

ðð=ððð¡2ð¡+ðð¡â12ð¡â1+â¯+ð121+ð020=ðð020Ãðð121Ãâ¯Ãððð¡â12ð¡â1Ãððð¡2ð¡.an=ant2t+ntâ12tâ1+â¯+n121+n020=an020Ãan121Ãâ¯Ãantâ12tâ1Ãant2t.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ³¨æï¼åªæ ðð =1ni=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¡¹æä¼çæ­£åºç°å¨ä¹ç§¯çè®¡ç®ä¸­ï¼

æ ¹æ®è¿ä¸è¡¨è¾¾å¼ï¼å¯ä»¥é¦å å¨ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®åº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª 2ð2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹çåå¼ï¼ç¶åè±è´¹ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´éæ©ç­äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶ä½å¯¹åºçå¹æ¬¡ä¹å°æç»ç»æä¸­ï¼è¿å°±æ¯å¿«éå¹çè¿­ä»£çæ¬å®ç°ï¼

ä¼ªä»£ç å¦ä¸ï¼

ðð¥ð ð¨ð«ð¢ð­ð¡ð¦Â FastPow(ð,ð):ðð§ð©ð®ð­.Â BaseÂ ðÂ and exponentÂ ð.ðð®ð­ð©ð®ð­.Â PowerÂ ðð.ððð­ð¡ð¨ð.1ððð ð¢ðð¡âId2ð°ð¡ð¢ð¥ðÂ ð>0Â ðð¨3ð¢ðÂ ðmod2=1Â ð­ð¡ðð§4ððð ð¢ðð¡âððð ð¢ðð¡â ð5ðð§ð ð¢ð6ðâðâ ð7ðâð/28ðð§ð ð°ð¡ð¢ð¥ð9ð«ðð­ð®ð«ð§Â ððð ð¢ðð¡AlgorithmÂ FastPow(a,n):Input.Â BaseÂ aÂ and exponentÂ n.Output.Â PowerÂ an.Method.1resultâId2whileÂ n>0Â do3ifÂ nmod2=1Â then4resultâresultâ a5end if6aâaâ a7nân/28end while9returnÂ result![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿ä¸æ¹æ³è®¡ç®å¿«éå¹ï¼éè¦è¿è¡ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³è¿ç®ï¼

### éå½çæ¬

è¿ä¸è¿ç¨åæ ·å¯ä»¥éè¿éå½å½¢å¼å®ç°ï¼æ³¨æå°ï¼ææ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶å±å¼å¯ä»¥éå½å°åä½

(ðð¡ðð¡â1â¯ð1ð0)2=2Ã(ðð¡ðð¡â1â¯ð1)2+ð0.(ntntâ1â¯n1n0)2=2Ã(ntntâ1â¯n1)2+n0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼å¹æ¬¡ ððan![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥éå½å°è®¡ç®ä¸º

ðð=â§{ {â¨{ {â©1,ð=0,(ðâð/2â)2,ð>0Â andÂ ðÂ is even,(ðâð/2â)2â ð,ð>0Â andÂ ðÂ is odd.an={1,n=0,(aân/2â)2,n>0Â andÂ nÂ is even,(aân/2â)2â a,n>0Â andÂ nÂ is odd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯å¿«éå¹çéå½çæ¬å®ç°ï¼

ä¼ªä»£ç å¦ä¸ï¼

ðð¥ð ð¨ð«ð¢ð­ð¡ð¦Â FastPow(ð,ð):ðð§ð©ð®ð­.Â BaseÂ ðÂ and exponentÂ ð.ðð®ð­ð©ð®ð­.Â PowerÂ ðð.ððð­ð¡ð¨ð.1ð¢ðÂ ð=0Â ð­ð¡ðð§2ð«ðð­ð®ð«ð§Â Id3ðð§ð ð¢ð4ððð ð¢ðð¡âFastPow(ð,ð/2)5ð¢ðÂ ðmod2=0Â ð­ð¡ðð§6ð«ðð­ð®ð«ð§Â ððð ð¢ðð¡â ððð ð¢ðð¡7ðð¥ð¬ð8ð«ðð­ð®ð«ð§Â ððð ð¢ðð¡â ððð ð¢ðð¡â ð9ðð§ð ð¢ðAlgorithmÂ FastPow(a,n):Input.Â BaseÂ aÂ and exponentÂ n.Output.Â PowerÂ an.Method.1ifÂ n=0Â then2returnÂ Id3end if4resultâFastPow(a,n/2)5ifÂ nmod2=0Â then6returnÂ resultâ result7else8returnÂ resultâ resultâ a9end if![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿ä¸æ¹æ³è®¡ç®å¿«éå¹ï¼éè¦éå½ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼åæ ·éè¦ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¹æ³è¿ç®ï¼å°½ç®¡å¤æåº¦ç¸åï¼ç±äºéå½æ¬èº«æä¸å®å¼éï¼æä»¥å®è·µä¸­è¿­ä»£çæ¬çéåº¦æ´å¿«ï¼

## åºç¨

### æ¨¡æä¹ä¸åå¹

[æ´è°· P1226ãæ¨¡æ¿ãå¿«éå¹](https://www.luogu.com.cn/problem/P1226)

ç»å®ä¸ä¸ªæ´æ° ð,ð,ða,b,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ððmodðabmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð â¥2pâ¥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿æ¯ä¸ä¸ªéå¸¸å¸¸è§çåºç¨ï¼ä¾å¦å®å¯ä»¥ç¨äºè®¡ç®æ¨¡æä¹ä¸çä¹æ³éå ï¼æ¢ç¶æä»¬ç¥éåæ¨¡çè¿ç®ä¸ä¼å¹²æ¶ä¹æ³è¿ç®ï¼å æ­¤æä»¬åªéè¦å¨è®¡ç®çè¿ç¨ä¸­åæ¨¡å³å¯ï¼

é¦å æä»¬å¯ä»¥ç´æ¥æç §ä¸è¿°éå½æ¹æ³å®ç°ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text long long binpow ( long long a , long long b , long long p ) { if ( b == 0 ) return 1 ; long long res = binpow ( a , b / 2 , p ); if ( b % 2 ) return res * res % p * a % p ; else return res * res % p ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def binpow ( a , b , p ): if b == 0 : return 1 res = binpow ( a , b // 2 , p ) if ( b % 2 ) == 1 : return res * res * a % p else : return res * res % p ```   
---|---  
  
ç¬¬äºç§å®ç°æ¹æ³æ¯ééå½å¼çï¼å®å¨å¾ªç¯çè¿ç¨ä¸­å°äºè¿å¶ä½ä¸º 1 æ¶å¯¹åºçå¹ç´¯ä¹å°ç­æ¡ä¸­ï¼å°½ç®¡ä¸¤è ççè®ºå¤æåº¦æ¯ç¸åçï¼ä½ç¬¬äºç§å¨å®è·µè¿ç¨ä¸­çéåº¦æ¯æ¯ç¬¬ä¸ç§æ´å¿«çï¼å ä¸ºéå½ä¼è±è´¹ä¸å®çå¼éï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text long long binpow ( long long a , long long b , long long p ) { long long res = 1 ; while ( b > 0 ) { if ( b & 1 ) res = res * a % p ; a = a * a % p ; b >>= 1 ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def binpow ( a , b , p ): res = 1 while b > 0 : if b & 1 : res = res * a % p a = a * a % p b >>= 1 return res ```   
---|---  
  
æ³¨æ

  * æ¨¡æ°éå¸¸æ åµä¸å¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ååç¹æ®çæ åµä¸ï¼æ¨¡æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½ç­äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶éè¦ç¹æ®èè ð =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼
  * å½ææ°å¾å¤§æ¶ï¼éå©ç¨ [æ©å±æ¬§æå®ç](../number-theory/fermat/#æ©å±æ¬§æå®ç) éå¹åè®¡ç®ï¼

### è®¡ç®ææ³¢é£å¥æ°

æ ¹æ®ææ³¢é£å¥æ°åçéæ¨å¼ ð¹ð =ð¹ðâ1 +ð¹ðâ2Fn=Fnâ1+Fnâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å¯ä»¥æå»ºä¸ä¸ª 2 Ã22Ã2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµæ¥è¡¨ç¤ºä» ð¹ð,ð¹ð+1Fi,Fi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð¹ð+1,ð¹ð+2Fi+1,Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¢ï¼äºæ¯å¨è®¡ç®è¿ä¸ªç©éµç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹çæ¶ä¾¯ï¼æä»¬ä½¿ç¨å¿«éå¹çææ³ï¼å¯ä»¥å¨ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å è®¡ç®åºç»æï¼å¯¹äºæ´å¤çç»èåè§ [ææ³¢é£å¥æ°å](../combinatorics/fibonacci/)ï¼ç©éµå¿«éå¹çå®ç°åè§ [ç©éµå ééæ¨](../linear-algebra/matrix/#ç©éµå) ä¸­çå®ç°ï¼

### å¤æ¬¡ç½®æ¢

é®é¢æè¿°

ç»ä½ ä¸ä¸ªé¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºååä¸ä¸ªç½®æ¢ï¼æè¿ä¸ªåºåç½®æ¢ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼

ç®åå°æè¿ä¸ªç½®æ¢å ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹ï¼ç¶åæå®åºç¨å°åºåä¸å³å¯ï¼æ¶é´å¤æåº¦ä¸º ð(ðlogâ¡ð)O(nlogâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºæ´å¤çç»èåè§ [ç½®æ¢çå¤å](../permutation/#å¤å)ï¼

æ³¨æ

å¯¹è¿ä¸ªç½®æ¢å»ºå¾ï¼ç¶åå¨æ¯ä¸ä¸ªç¯ä¸åå«å ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹ï¼äºå®ä¸ç­ä»·äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ç¯é¿åæ¨¡ï¼ï¼å¯ä»¥å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦ä¸è§£å³æ­¤é®é¢ï¼

### å éå ä½ä¸­å¯¹ç¹éçæä½

[HDU 4087 A Letter to Programmers](https://acm.hdu.edu.cn/showproblem.php?pid=4087)

ç»å®ä¸ç»´ç©ºé´ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦æ±å° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæä½é½åºç¨äºè¿äºç¹ï¼å å« 3 ç§æä½ï¼

  1. æ²¿æä¸ªåéç§»å¨ç¹çä½ç½®ï¼Shiftï¼ï¼
  2. ææ¯ä¾ç¼©æ¾è¿ä¸ªç¹çåæ ï¼Scaleï¼ï¼
  3. ç»ææ¡ç´çº¿æè½¬ï¼Rotateï¼ï¼

è¿æä¸ä¸ªç¹æ®çæä½ï¼å°±æ¯å°æä¸ªæä½åºåéå¤ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼Repeatï¼ï¼Repeat æä½å¯ä»¥åµå¥ï¼è¾åºæä½ç»æåæ¯ä¸ªç¹çåæ ï¼

åè [åéä¸ç©éµ](../linear-algebra/vector/#åéä¸ç©éµ) ä¸­çå å®¹ï¼æ¯ä¸ç§æä½é½å¯ä»¥ç¨ä¸ä¸ªåæ¢ç©éµè¡¨ç¤ºï¼ä¸ç³»åè¿ç»­çåæ¢å¯ä»¥ç¨ç©éµçä¹ç§¯æ¥è¡¨ç¤ºï¼ä¸ä¸ª Repeat æä½å°±ç¸å½äºåä¸ä¸ªç©éµç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹ï¼è¿æ ·å¯ä»¥ç¨ ð(ðlogâ¡ð)O(mlogâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´è®¡ç®åºæ´ä¸ªåæ¢åºåæç»å½¢æçç©éµï¼æåå°å®åºç¨å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ä¸ï¼æ»å¤æåº¦ ð(ð +ðlogâ¡ð)O(n+mlogâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å®é¿è·¯å¾è®¡æ°

é®é¢æè¿°

ç»ä¸ä¸ªæåå¾ï¼è¾¹æä¸º 1ï¼ï¼æ±ä»»æä¸¤ç¹ ð¢,ð£u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é´ä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¿åº¦ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ¡æ°ï¼

æä»¬æè¯¥å¾çé»æ¥ç©éµ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹ï¼é£ä¹ ðð,ðMi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±è¡¨ç¤ºä» ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¿åº¦ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ°ç®ï¼è¯¥ç®æ³çå¤æåº¦æ¯ ð(ð3logâ¡ð)O(n3logâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æå ³è¯¥ç®æ³çç»èè¯·åè§ [ç©éµ](../linear-algebra/matrix/#å®é¿è·¯å¾ç»è®¡) é¡µé¢ï¼

### æ¨¡æä¹ä¸çæ´æ°ä¹æ³

é®é¢æè¿°

ç»å®éè´æ´æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ­£æ´æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¡ç® ð ÃðmodðaÃbmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð,ð â¤ð â¤1018a,bâ¤mâ¤1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸äºè¿å¶åå¹çææ³ä¸æ ·ï¼è¿æ¬¡æä»¬å°å ¶ä¸­çä¸ä¸ªä¹æ°è¡¨ç¤ºä¸ºè¥å¹²ä¸ª 2 çæ´æ°æ¬¡å¹çåçå½¢å¼ï¼å ä¸ºå¨å¯¹ä¸ä¸ªæ°åä¹ 2 å¹¶åæ¨¡çè¿ç®çæ¶ä¾¯ï¼æä»¬å¯ä»¥è½¬åä¸ºå åæä½é²æ­¢æ´åæº¢åºï¼è¿æ ·å¯ä»¥å¨ ð(logâ¡ð)O(logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦ä¸è§£å³é®é¢ï¼éå½æ¹æ³å¦ä¸ï¼

ðâ ð=â§{ {â¨{ {â©0ifÂ ð=02â ð2â ðifÂ ð>0Â andÂ ðÂ even2â ðâ12â ð+ðifÂ ð>0Â andÂ ðÂ oddaâ b={0ifÂ a=02â a2â bifÂ a>0Â andÂ aÂ even2â aâ12â b+bifÂ a>0Â andÂ aÂ odd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½å¨å®é ä½¿ç¨ä¸­ï¼æ­¤æ¹æ³ç±äºå¼å ¥äºæ´å¤§çè®¡ç®å¤æåº¦å¯¼è´æ¶é´æçä¸ä¼ï¼å®é ç¼ç¨ä¸­éå¸¸å©ç¨ [å¿«éä¹](../number-theory/mod-arithmetic/#å¿«éä¹) æ¥è¿è¡æ¨¡æ°èå´å¨ `long long` æ¶çä¹æ³æä½ï¼

### é«ç²¾åº¦å¿«éå¹

åç½®æè½ï¼[å¤§æ´æ°ä¹æ³](../bignum/#ä¹æ³)

[æ´è°· P1045 [NOIP 2003 æ®åç»] éº¦æ£®æ°](https://www.luogu.com.cn/problem/P1045)

ç»å®æ´æ° ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼1000 <ð <31000001000<P<3100000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼è®¡ç® 2ð â12Pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ°ä¸æå 500500![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ°å­ï¼ç¨åè¿å¶æ°è¡¨ç¤ºï¼ï¼ä¸è¶³ 500500![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¶é«ä½è¡¥ 0ï¼

ä»£ç å®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <cmath> #include <cstring> #include <iostream> using namespace std ; const int M = 500 ; int a [ 505 ], b [ 505 ], t [ 505 ]; // å¤§æ´æ°ä¹æ³ void mult ( int x [], int y []) { memset ( t , 0 , sizeof ( t )); for ( int i = 1 ; i <= x [ 0 ]; i ++ ) { for ( int j = 1 ; j <= y [ 0 ]; j ++ ) { if ( i \+ j \- 1 > M ) continue ; t [ i \+ j \- 1 ] += x [ i ] * y [ j ]; t [ i \+ j ] += t [ i \+ j \- 1 ] / 10 ; t [ i \+ j \- 1 ] %= 10 ; t [ 0 ] = i \+ j ; } } memcpy ( b , t , sizeof ( b )); } // å¿«éå¹ void binpow ( int p ) { if ( p == 1 ) { memcpy ( b , a , sizeof ( b )); return ; } binpow ( p / 2 ); // (2^(p/2))^2=2^p mult ( b , b ); // å¯¹ b å¹³æ¹ if ( p % 2 == 1 ) mult ( b , a ); } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int p ; cin >> p ; a [ 0 ] = 1 ; // è®°å½ a æ°ç»çä½æ° a [ 1 ] = 2 ; // å¯¹ 2 è¿è¡å¹³æ¹ b [ 0 ] = 1 ; // è®°å½ b æ°ç»çä½æ° b [ 1 ] = 1 ; // ç­æ¡æ°ç» binpow ( p ); cout << ( int )( log10 ( 2 ) * p ) \+ 1 << '\n' ; b [ 1 ] -= 1 ; // æåä¸ä½å 1 for ( int i = M ; i >= 1 ; i \-- ) { cout << b [ i ]; if (( i \- 1 ) % 50 == 0 ) { cout << '\n' ; } } } ```   
---|---  
  
## åºæ°åºå®çé¢å¤çå¿«éå¹

å½åºæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºå®æ¶ï¼å¯ä»¥å©ç¨ [ååææ³](../../ds/decompose/)ï¼ç¨ä¸å®çæ¶é´é¢å¤çåç¨ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´åç­ä¸æ¬¡å¹è¯¢é®ï¼è¿ä¸ç®æ³ä¹å¸¸ç§°ä¸ºå éå¹ï¼è¿ç¨å¦ä¸ï¼

  1. éå®ä¸ä¸ªæ° ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¢å¤çåº ð0,ð1,â¯,ðð â1a0,a1,â¯,asâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð0,ðð ,â¯,ðâð/ð âð a0,as,â¯,aâp/sâs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼å¹¶å­å¨ä¸¤ä¸ªæ°ç»éï¼
  2. å¯¹äºæ¯ä¸æ¬¡è¯¢é® ððab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æåæ âð/ð âð  +(ðmodð )âb/sâs+(bmods)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ðð =ðâð/ð âð  â ððmodð ab=aâb/sâsâ abmods![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±åºç­æ¡ï¼

åè®¾ææ° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çèå´æ¯ [0,ð][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹åé¿ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»å¸¸éæ©ä¸º âðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè ä¸ä¹ç¸è¿ç 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡ï¼éæ© âðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è·å¾æä¼çé¢å¤çå¤æåº¦ ð(âð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èéæ© 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡å¯ä»¥ä½¿ç¨ä½æä½ç®åè®¡ç®ï¼

ç¹å«å°ï¼å¯¹äºæ¨¡æä¹ä¸å¹çè®¡ç®ï¼åºæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸åéå«çæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹è¦ç¸åè¿ä¸è¦æ±ï¼ç±äº [æ©å±æ¬§æå®ç](../number-theory/fermat/#æ©å±æ¬§æå®ç)ï¼å¯¹äºä»»ææ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¢å¤ççææ°èå´ä¸çä¸º ð =2ð(ð)n=2Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºç´ æ¨¡æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¢å¤ççèå´ä¸çä¸º ð =ð â1n=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸¤ç§æ å½¢é¢å¤ççå¤æåº¦é½æ¯ ð(âð)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int a , mod , pow1 [ 65536 ], pow2 [ 65536 ]; void preproc () { pow1 [ 0 ] = pow2 [ 0 ] = 1 ; for ( int i = 1 ; i < 65536 ; i ++ ) pow1 [ i ] = 1L L * pow1 [ i \- 1 ] * a % mod ; int pow65536 = 1L L * pow1 [ 65535 ] * a % mod ; for ( int i = 1 ; i < 65536 ; i ++ ) pow2 [ i ] = 1L L * pow2 [ i \- 1 ] * pow65536 % mod ; } int query ( int pows ) { return 1L L * pow1 [ pows & 65535 ] * pow2 [ pows >> 16 ] % mod ; } ```   
---|---  
  
## ä¹ é¢

  * [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
  * [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
  * [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
  * [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
  * [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
  * [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
  * [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)

**æ¬é¡µé¢é¨åå å®¹è¯èªåæ[ÐÐ¸Ð½Ð°ÑÐ½Ð¾Ðµ Ð²Ð¾Ð·Ð²ÐµÐ´ÐµÐ½Ð¸Ðµ Ð² ÑÑÐµÐ¿ÐµÐ½Ñ](http://e-maxx.ru/algo/binary_pow) ä¸å ¶è±æç¿»è¯ç [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/27 12:26:08ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/binary-exponentiation.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/binary-exponentiation.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [cbw2007](https://github.com/cbw2007), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [c-forrest](https://github.com/c-forrest), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [luoguyuntianming](https://github.com/luoguyuntianming), [Marcythm](https://github.com/Marcythm), [Peanut-Tang](https://github.com/Peanut-Tang), [Aquistcev](https://github.com/Aquistcev), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [chinggg](https://github.com/chinggg), [eyedeng](https://github.com/eyedeng), [FFjet](https://github.com/FFjet), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [hhc0001](https://github.com/hhc0001), [hsfzLZH1](https://github.com/hsfzLZH1), [Hszzzx](https://github.com/Hszzzx), [JEB-Bem](https://github.com/JEB-Bem), [Jude Gao](mailto:jude.gao@faire.com), [kenlig](https://github.com/kenlig), [kfy666](https://github.com/kfy666), [Konano](https://github.com/Konano), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [qwqAutomaton](https://github.com/qwqAutomaton), [shawlleyw](https://github.com/shawlleyw), [shenshuaijie](https://github.com/shenshuaijie), [StudyingFather](https://github.com/StudyingFather), [TOMWT-qwq](https://github.com/TOMWT-qwq), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TRSWNCA](https://github.com/TRSWNCA), [uqzjc](https://github.com/uqzjc), [Zhoier](https://github.com/Zhoier)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
