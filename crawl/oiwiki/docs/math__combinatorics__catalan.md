# å¡ç¹å°æ° - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/catalan/

# å¡ç¹å °æ°

## å¼å ¥

Catalan æ°ç»å¸¸åºç°å¨åç±»è®¡æ°é®é¢ä¸­ï¼æ¯å©æ¶æ°å­¦å®¶ EugÃ¨ne Charles Catalan å¨ 1958 å¹´ç ç©¶æ¬å·åºåè®¡æ°é®é¢æ¶åç°äºè¿ä¸æ°åï¼å®ä¹å æ­¤å¾åï¼æ¸ ææ°å­¦å®¶æå®å¾æ©å¨ 18 ä¸çºª 30 å¹´ä»£å°±å·²ç»åç°è¿ä¸æ°åï¼

Catalan æ°æ»¡è¶³å¦ä¸éæ¨å ³ç³»ï¼

ð¶ð={1,ð=0,âðâ1ð=0ð¶ðð¶ðâ1âð,ð>0.(1)(1)Cn={1,n=0,âi=0nâ1CiCnâ1âi,n>0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ°åçåå é¡¹ä¸ºï¼ï¼[OEIS: A000108](https://oeis.org/A000108)ï¼ä¸æ ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼

1,1,2,5,14,42,132,429,1430,â¦1,1,2,5,14,42,132,429,1430,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## åºç¨

Catalan æ° ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨å ³ç³»æçå¤©ç¶çéå½ç»æï¼è§æ¨¡ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡æ°é®é¢ ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥éè¿æä¸¾åçç¹ï¼åæä¸ºä¸¤ä¸ªè§æ¨¡åå«ä¸º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð â1 âð)(nâ1âi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­é®é¢ï¼è¿ä¸éæ¨å ³ç³»ä½¿å¾ Catalan æ°å¹¿æ³åºç°äºåç±»å ·æç±»ä¼¼éå½ç»æçé®é¢ä¸­ï¼

  * **è·¯å¾è®¡æ°é®é¢** ï¼æä¸ä¸ªå¤§å°ä¸º ð ÃðnÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹æ ¼å¾ï¼å·¦ä¸è§ä¸º (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ä¸è§ä¸º (ð,ð)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»å·¦ä¸è§å¼å§ï¼æ¯æ¬¡é½åªè½åå³æè åä¸èµ°ä¸åä½ï¼ä¸èµ°å°å¯¹è§çº¿ ð¦ =ð¥y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¹ï¼ä½å¯ä»¥è§¦ç¢°ï¼çæ åµä¸ï¼å°è¾¾å³ä¸è§çè·¯å¾æ»æ°ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®¾æ¹æ¡æ°ä¸º ððTn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èè ð â¥2nâ¥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼è®¾è·¯å¾ **ç¬¬ä¸æ¬¡** èµ°å°å¯¹è§çº¿ ð¦ =ð¥y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¹æ¯ (ð,ð)Â (ð â[1,ð])(k,k)Â (kâ[1,n])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¤èµ·ç¹åç»ç¹å¤ï¼ä¸­é´çç¹ **ä¸ç»è¿å¯¹è§çº¿ï¼ä¸è½ç¢°å°ï¼** çè·¯å¾ï¼

![catalan2](./images/catalan-2.svg)

å¦å¾æç¤ºï¼è¿äºè·¯å¾çç¬¬ä¸æ­¥ä¸å®åå³ï¼ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (1,0)(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æåä¸æ­¥ä¸å®åä¸ï¼ä» (ð,ð â1)(k,kâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼è¿äºè·¯å¾å°±æ¯ä» (1,0)(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð â1)(k,kâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸è¶è¿ç´çº¿ ð¦ =ð¥ â1y=xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾ï¼è¿æ ·è·¯å¾çæ°ç®å°±æ¯ ððâ1Tkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ï¼ä» (ð,ð)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ³è·¯å¾æ°å°±æ¯ ððâðTnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®ä¹æ³åçï¼ç¬¬ä¸æ¬¡å¨ (ð,ð)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤è§¦ç¢°å¯¹è§çº¿çè·¯å¾æ°ç®ä¸º ððâ1ððâðTkâ1Tnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¸¾ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå¯è½æ§ï¼ææåæ³è·¯å¾çæ°ç®ä¸º

ðð=ðâð=1ððâ1ððâð.Tn=âk=1nTkâ1Tnâk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä»£æ¢ ð =ð +1k=i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥åç°ï¼è¿å°±æ¯ Catalan æ°çéæ¨å ³ç³»ï¼ç± ð0 =1T0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ ðð =ð¶ðTn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **åå ä¸ç¸äº¤å¼¦è®¡æ°é®é¢** ï¼åä¸æ 2ð2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ï¼å°è¿äºç¹æå¯¹è¿æ¥èµ·æ¥ä¸ä½¿å¾æå¾å°ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡çº¿æ®µä¸¤ä¸¤ä¸äº¤çæ¹æ¡æ°æ¯ ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®° 2ð2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹çæ¹æ¡æ°ä¸º ððTn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° 2ð2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹æé¡ºæ¶éæ å·ï¼åå«ä¸º 1,2,â¦,2ð1,2,â¦,2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºå¼¦ä¸¤ä¸¤ä¸äº¤ï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·ç¹åªè½è¿æ¥å¶æ°å·ç¹ï¼å¦åï¼ä¸¤ç¹ä¹é´çå¥æ°ä¸ªç¹æ æ³å¨ä¸ç©¿è¿ä¸¤ç¹è¿çº¿çæ åµä¸ä¸¤ä¸¤é å¯¹ï¼å¦æè¿æ¥äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 2ðÂ (ð â[1,ð])2kÂ (kâ[1,n])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å·¦è¾¹æ 2ð â22kâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ï¼å³è¾¹æ 2ð â2ð2nâ2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ï¼ç±ä¹æ³åçï¼è¿æ ·çæ¹æ¡æ°ä¸º ððâ1ððâðTkâ1Tnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æä¸¾ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ðð =âðð=1ððâ1ððâðTn=âk=1nTkâ1Tnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ð =ð +1k=i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å° Catalan æ°çéæ¨å ³ç³»ï¼ç± ð0 =1T0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ ðð =ð¶ðTn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **ä¸è§ååè®¡æ°é®é¢** ï¼å¯¹è§çº¿ä¸ç¸äº¤çæ åµä¸ï¼å°ä¸ä¸ªå¸ (ð +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢åºååæä¸è§å½¢åºåçæ¹æ³æ°ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®¾ (ð +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢ä¸è§ååçæ¹æ¡æ°ä¸º ððTn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å éå®ä¸æ¡è¾¹ (1,ð +2)(1,n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºåºè¾¹ï¼å®ä¸å®å±äºä¸ä¸ªä¸è§å½¢ï¼è®°è¯¥ä¸è§å½¢çç¬¬ä¸ä¸ªç¹ä¸º ðÂ (ð â[2,ð +1])kÂ (kâ[2,n+1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·ï¼åå¸å¤è¾¹å½¢åæäºä¸ä¸ªé¨åï¼

    * ä¸è§å½¢ (1,ð,ð +2)(1,k,n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
    * ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢ï¼é¡¶ç¹ 1 â¼ð1â¼k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
    * (ð +3 âð)(n+3âk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢ï¼é¡¶ç¹ ð â¼(ð +2)kâ¼(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åé¢ä¸¤ä¸ªé¨åé½æ¯å­é®é¢ï¼æä»¥ï¼æéæ¨å ³ç³»

ðð=ð+1âð=2ððâ2ðð+1âð.Tn=âk=2n+1Tkâ2Tn+1âk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤ ð =ð +2k=i+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å° Catalan æ°éå½å ³ç³»ï¼ç± ð0 =ð1 =1T0=T1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ ðð =ð¶ðTn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **äºåæ è®¡æ°é®é¢** ï¼å«æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹çå½¢æä¸åçäºåæ æ°ç®ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç­ä»·å°ï¼å«æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéå¶ç»ç¹çå½¢æä¸åçæ»¡äºåæ æ°ç®ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹çäºåæ æ°ç®ä¸º ððTn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»»åä¸ä¸ªæ ¹ç»ç¹ï¼æä¸¾å·¦å³å­æ å¤§å°ï¼è®¾å·¦å­æ å¤§å°ä¸º ð â[0,ð â1]iâ[0,nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå³å­æ å¤§å°ä¸º (ð â1 âð)(nâ1âi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å·¦å³å­æ åä¸ºå­é®é¢ï¼æä»¥ï¼æéæ¨å ³ç³»

ðð=ðâ1âð=0ððððâ1âð.Tn=âi=0nâ1TiTnâ1âi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯ Catalan æ°éæ¨å ³ç³»ï¼ç± ð0 =ð1 =1T0=T1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ ðð =ð¶ðTn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **æ¬å·åºåè®¡æ°é®é¢** ï¼ç± ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹æ¬å·ææçåæ³æ¬å·åºåæ°ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

èç³»è·¯å¾è®¡æ°é®é¢ï¼å°å·¦æ¬å·è§ä¸ºåä¸èµ°ï¼å³æ¬å·è§ä¸ºåå³èµ°ï¼åæ³æ¬å·åºåå³ä¸ºï¼å¨ä»»æä½ç½®ï¼å·¦æ¬å·çæ°éä¸å°äºå³æ¬å·çæ°éï¼ç¸å½äºè·¯å¾è®¡æ°é®é¢ä¸­ï¼å¨ä»»ææ¶å»ï¼åä¸èµ°çæ¬¡æ°ä¸å°äºåå³èµ°çæ¬¡æ°ï¼å æ­¤ï¼åæ³æ¬å·åºåä¸åæ³è·¯å¾ä¹é´å­å¨åå°ï¼åæ³æ¬å·åºåçæ°ç®åæ ·ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **åºæ åºåè®¡æ°é®é¢** ï¼ä¸ä¸ªæ ï¼æ ç©·å¤§ï¼çè¿æ åºåä¸º 1,2,3,â¦,ð1,2,3,â¦,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ³åºæ åºåçæ°ç®ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

èç³»æ¬å·åºåè®¡æ°é®é¢ï¼å°å ¥æ è§ä¸ºå·¦æ¬å·ï¼åºæ è§ä¸ºå³æ¬å·ï¼ä»»ææ¶å»ï¼å ¥æ çæ¬¡æ°ä¸å°äºåºæ çæ¬¡æ°ï¼å æ­¤ï¼åæ³åºæ åºåä¸åæ³æ¬å·åºåä¹é´å­å¨åå°ï¼åæ³åºæ åºåçæ°ç®åæ ·ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **æ°åè®¡æ°é®é¢** ï¼ç± ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æçæ°å ð1,ð2,â¦,ð2ða1,a2,â¦,a2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼é¨ååæ»¡è¶³ ð1 +ð2 +â¦ +ðð â¥0Â (ð =1,2,3,â¦,2ð)a1+a2+â¦+akâ¥0Â (k=1,2,3,â¦,2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°åæ°ç®ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

èç³»æ¬å·åºåè®¡æ°é®é¢ï¼å° +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è§ä¸ºå·¦æ¬å·ï¼â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è§ä¸ºå³æ¬å·ï¼ä»»ææ¶å»ï¼+1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éä¸å°äº â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éï¼å æ­¤ï¼åæ³æ°åä¸åæ³æ¬å·åºåä¹é´å­å¨åå°ï¼åæ³æ°åçæ°ç®åæ ·ä¸º ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å°½ç®¡è¿ä¸éæ¨å ³ç³»åºç¨å¹¿æ³ï¼ä½æ¯ç´æ¥è®¡ç®å¤æåº¦è¾é«ï¼éè¦å¯»æ¾æ´ä¸ºç®åçå ¬å¼ï¼

## å¸¸è§å½¢å¼

Catalan æ°æå¦ä¸å¸¸è§çè¡¨è¾¾å¼ï¼

ð¶ð=1ð+1(2ðð)=(2ð)!ð!(ð+1)!,Â ðâ¥0.(2)(2)Cn=1n+1(2nn)=(2n)!n!(n+1)!,Â nâ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¶ð=(2ðð)â(2ðð+1),Â ðâ¥0.(3)(3)Cn=(2nn)â(2nn+1),Â nâ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¶ð=(4ðâ2)ð+1ð¶ðâ1,Â ð>0,Â ð¶0=1.(4)(4)Cn=(4nâ2)n+1Cnâ1,Â n>0,Â C0=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Catalan æ°çè¿äºå½¢å¼é½å¯ä»¥é«æè®¡ç®ï¼åä¸¤ä¸ªå½¢å¼å°å®è½¬æ¢ä¸ºé¶ä¹åç»åæ°çè®¡ç®é®é¢ï¼ç¬¬ä¸ä¸ªå½¢å¼åæä¾äºé¡ºæ¬¡è®¡ç®çéæ¨å ¬å¼ï¼

å¯¹äºè¿ä¸ç§å¸¸è§å½¢å¼ï¼æ¬ææä¾ä¸¤ç§è¯ææ¹å¼ï¼

### ä»£æ°æ¨æ¼

éè¿ä»£æ°æ¹æ³å¾åº Catalan æ°çä¸è¿°è¡¨è¾¾å¼å ±ä¸¤æ­¥ï¼é¦å ï¼éªè¯ä¸ä¸ªå½¢å¼ç¸äºç­ä»·ï¼

è¯æè¡¨è¾¾å¼ (2) â¼(4)(2)â¼(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·

åªéè¦è¯æè¡¨è¾¾å¼ (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è½¬åä¸ºè¡¨è¾¾å¼ (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­é¶ä¹å½¢å¼ï¼

ð¶ð=(2ðð)â(2ðð+1)=(2ð)!ð!ð!â(2ð)!(ðâ1)!(ð+1)!=(2ð)!ð!ð!(1âð!(ðâ1)!(ð+1))=(2ð)!ð!ð!(1âðð+1)=(2ð)!ð!(ð+1)!.Cn=(2nn)â(2nn+1)=(2n)!n!n!â(2n)!(nâ1)!(n+1)!=(2n)!n!n!(1ân!(nâ1)!(n+1))=(2n)!n!n!(1ânn+1)=(2n)!n!(n+1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¥åï¼è¡¨è¾¾å¼ (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¯ä»¥è½¬åä¸ºè¡¨è¾¾å¼ (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­é¶ä¹å½¢å¼ï¼

ð¶ð=ðâð=1(4ðâ2)ð+1=ðâð=12ð(2ðâ1)ð(ð+1)=(2ð)!ð!(ð+1)!.Cn=âi=1n(4iâ2)i+1=âi=1n2i(2iâ1)i(i+1)=(2n)!n!(n+1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ä¸ä¸ªè¡¨è¾¾å¼äºç¸ç­ä»·ï¼

ç´§æ¥çï¼éªè¯è¿äºå½¢å¼ç¡®å®æ¯ Catalan æ°éæ¨å ¬å¼çè§£ï¼ä¸ºæ­¤ï¼èèä½¿ç¨çæå½æ°æ¹æ³ç´æ¥æ±åºéæ¨å ¬å¼ (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ï¼

å©ç¨çæå½æ°æ¹æ³æ±è§£éæ¨å ¬å¼ (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èè Catalan æ°çæ®éçæå½æ° ð¶(ð¥) =ââð=0ð¶ðð¥ðC(x)=ân=0âCnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº Catalan æ°çéæ¨å ³ç³»åå·ç§¯å½¢å¼å¾ç¸ä¼¼ï¼æä»¥èèç¨å·ç§¯æé ð¶(ð¥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹ç¨ï¼

ð¶(ð¥)=ââð=0ð¶ðð¥ð=1+ââð=1(ðâ1âð=0ð¶ðð¶ðâðâ1)ð¥ð=1+ð¥ââð=1ðâ1âð=0ð¶ðð¥ðð¶ðâðâ1ð¥ðâðâ1=1+ð¥ââð=0ð¶ðð¥ðââð=0ð¶ðð¥ð=1+ð¥ð¶2(ð¥).C(x)=ân=0âCnxn=1+ân=1â(âi=0nâ1CiCnâiâ1)xn=1+xân=1ââi=0nâ1CixiCnâiâ1xnâiâ1=1+xâi=0âCixiâj=0âCjxj=1+xC2(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼åæ°ç¬¬äºä¸ªç­å·äº¤æ¢äºæ±åæ¬¡åºï¼å¹¶ä»¤ ð =ð â1 âðj=nâ1âi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼è§£å¾ï¼

ð¶(ð¥)=1Â±â1â4ð¥2ð¥=21ââ1â4ð¥.C(x)=1Â±1â4x2x=21â1â4x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±åå¼æ¡ä»¶ ð¶0 =1C0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ï¼ð¶(0) =1C(0)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»£å ¥æ£éªå¯ä»¥åç°å¯ä¸å¯è¡çè§£å°±æ¯

ð¶(ð¥)=1ââ1â4ð¥2ð¥.C(x)=1â1â4x2x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¥ä¸æ¥ï¼éè¦å°å®å±å¼ä¸ºå¹çº§æ°çå½¢å¼ï¼å©ç¨ (1 +ð¥)ð(1+x)a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [å¹çº§æ°å±å¼å¼](../../poly/intro/#å¸¸è§çå¹çº§æ°å±å¼å¼) å¯ç¥ï¼

â1â4ð¥=ââð=0(12)âðð!(â4ð¥)ð,1â4x=ân=0â(12)ânn!(â4x)n,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼(12)âð(12)ân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸éé¶ä¹å¹ï¼

(12)âð=ðâ1âð=0(12âð)=12ððâ1âð=1(1â2ð)=(â1)ðâ12ððâ1âð=1(2ðâ1)=(â1)ðâ122ðâ1ðâ1âð=1(2ðâ1)2ðð=(â1)ðâ122ðâ1(2ðâ2)!(ðâ1)!.(12)ân=âk=0nâ1(12âk)=12nâk=1nâ1(1â2k)=(â1)nâ12nâk=1nâ1(2kâ1)=(â1)nâ122nâ1âk=1nâ1(2kâ1)2kk=(â1)nâ122nâ1(2nâ2)!(nâ1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥ ð¶(ð¥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼å°±æ

ð¶(ð¥)=12ð¥(1âââð=0(12)âðð!(â4ð¥)ð)=â12ð¥ââð=1(â4ð¥)ðð!(12)âð=â12ð¥ââð=1(â4ð¥)ðð!(â1)ðâ122ðâ1(2ðâ2)!(ðâ1)!=ââð=1(2ðâ2)!(ðâ1)!ð!ð¥ðâ1=ââð=0(2ð)!ð!(ð+1)!ð¥ð.C(x)=12x(1âân=0â(12)ânn!(â4x)n)=â12xân=1â(â4x)nn!(12)ân=â12xân=1â(â4x)nn!(â1)nâ122nâ1(2nâ2)!(nâ1)!=ân=1â(2nâ2)!(nâ1)!n!xnâ1=ân=0â(2n)!n!(n+1)!xn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ­¤ï¼å°±å¾å° ð¶ðCn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### ç»åæä¹

ç±äº Catalan æ°å ·æææ¾çç»åæä¹ï¼æä»¥åªä½¿ç¨ç»åè®¡æ°æ¹æ³åæ ·å¯ä»¥è¯æè¿äºå½¢å¼ï¼æ¬èä¸ºä¸ä¸ªè¡¨è¾¾å¼åå«æä¾ä¸ä¸ªç»åæä¹çè¯æï¼

è¡¨è¾¾å¼ (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¯æ

èè æ°åè®¡æ°é®é¢ï¼å¯¹äºä»»æç± Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æçåºå {ðð}2ðð=1{ai}i=12n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹å®çé¨ååä¸º ðð =âðð=1ððSi=âj=1iai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶å®ä¹å®ç **è¶ é¢é** ï¼exceedanceï¼ä¸º ðð <0Si<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð = â1ai=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ æ°éï¼è¶ é¢éä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç­ä»·äºæ°ååæ³ï¼è¶ é¢éçåå¼èå´æ¯ [0,ð][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ± (ð +1)(n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§å¯è½çåå¼ï¼éè¦è¯æçæ¯ï¼ä¸åè¶ é¢éçæ°åæ°éå ¶å®æ¯ä¸æ ·çï¼

ä¸ºæ­¤ï¼å¯ä»¥æé ä¸ä¸ªä»è¶ é¢éä¸º ð >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°åå°è¶ é¢éä¸º (ð â1)(eâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°åçæ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºè¶ é¢éä¸º ð >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºå {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸æ  ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä½¿å¾ ðð =0Si=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð = +1ai=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«çä¸æ æå°å¼ï¼å° ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·¦å³ä¸¤ä¾§çåºåäº¤æ¢ï¼å°±å¾å°å¦ä¸åºå {ðâ²ð}{aiâ²}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ðð+1,ðð+2,â¯,ð2ð,ðð,ð1,ð2,â¯,ððâ1.ak+1,ak+2,â¯,a2n,ak,a1,a2,â¯,akâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºååºåä¸­ ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¾§é¨åå¨äº¤æ¢ååå¯¹åºçé¨åååºåä¸åï¼æä»¥å®ä»¬è´¡ç®çè¶ é¢éä¹ä¸åï¼å¯¹äºååºåä¸­ ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·¦ä¾§é¨åï¼å®ä»¬å¯¹åºçé¨ååå¨äº¤æ¢åå ¨é¨å¢å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å®ä»¬è´¡ç®çè¶ é¢éä¼åå°ï¼èä¸åå°çæ°éæ°å¥½ç­äºååºå ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·¦ä¾§é¨åä¸­æ»¡è¶³ ðð = â1Si=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð = â1ai=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ æ°éï¼å ä¸º ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¿è¯äºè¿æ ·çä¸æ æä¸ä» æä¸ä¸ªï¼æä»¥ï¼åºå {ðâ²ð}{aiâ²}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¶ é¢éå°±ç­äº (ð â1)(eâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼æ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥å°åºåçè¶ é¢éæ°å¥½åå° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯éçï¼æ³¨æå°åºå {ðâ²ð}{aiâ²}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçä½ç½®æ°å¥½ä¸ºæ»¡è¶³ ðâ²ð = +1Skâ²=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðâ²ð = +1aiâ²=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ æå¤§å¼ï¼è¿æ¯å ä¸ºäº¤æ¢åï¼è¿äºé¨ååé½æ¯äº¤æ¢åå¯¹åºçé¨ååæ°å¥½å¤§ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ç°å¨çé¨ååä¸º +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºäº¤æ¢åé¨ååç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼æ ¹æ® ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåï¼äº¤æ¢åè¿ä¸é¨åï¼å³ååºå ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·¦ä¾§é¨åï¼æ¯æ²¡ææ»¡è¶³ ðð =0Si=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð = +1ai=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«çä¸æ çï¼

ç±æ­¤ï¼æ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææäºè¶ é¢éä¸º ð >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºååè¶ é¢éä¸º (ð â1)(eâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºåä¹é´çåå°ï¼è¿å°±è¯´æï¼ä¸åè¶ é¢éçæ°åæ°éå ¶å®æ¯ä¸æ ·çï¼ç±äºæ°åæ»æ°æ¯ (2ðð)(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ³æ°åï¼å³è¶ é¢éä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°åï¼æ°éå°±ç­äº

ð¶ð=1ð+1(2ðð).Cn=1n+1(2nn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±è¯æäº Catalan æ°çè¡¨è¾¾å¼ (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¡¨è¾¾å¼ (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¯æ

èè è·¯å¾è®¡æ°é®é¢ï¼è¿æ¯å ¸åçæ ¼è·¯è®¡æ°é®é¢ï¼å¯ä»¥éè¿åå°åçæ±è§£ï¼å ·ä½å°æ¬é®é¢ï¼èèç¨æ»è·¯å¾æ°ç®åå»ä¸åæ³çè·¯å¾æ°ç®ï¼æ»è·¯å¾æ°ä¸å ±è¦èµ° 2ð2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­¥ï¼å ¶ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­¥åå³ï¼æä»¥æ¹æ¡æ°ä¸º (2ðð)(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æ¡è·¯å¾ä¸åæ³ï¼å½ä¸ä» å½å®ç¢°å°äºç´çº¿ ð¦ =ð¥ +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºä»»æä¸æ¡éæ³è·¯å¾ï¼å¯ä»¥æ¾å°ç¬¬ä¸æ¬¡ç¢°å°ç´çº¿ ð¦ =ð¥ +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½ç½®ï¼å¹¶å°è¯¥ä½ç½®ä¹åçè·¯å¾å ³äºç´çº¿ ð¦ =ð¥ +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¯¹ç§°ï¼æ­¤æ¶ï¼å¯ä»¥åç°ï¼ä¸æ¡ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ³è·¯å¾ï¼åæäºä¸æ¡ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð â1,ð +1)(nâ1,n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾ï¼

![catalan1](./images/catalan-1.svg)

ç±äºä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð â1,ð +1)(nâ1,n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾å¿ å®è¦ç©¿è¿ç´çº¿ ð¦ =ð¥ +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æ¯æ¡è¿æ ·çè·¯å¾é½å¯¹åºä¸æ¡ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° (ð,ð)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ³è·¯å¾ï¼ç±»ä¼¼æ»è·¯å¾æ°çè®¡ç®ï¼éæ³è·¯å¾æ°ç®çæ»æ°å°±æ¯ (2ðð+1)(2nn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼åæ³è·¯å¾çæ»æ°ä¸º

ð¶ð=(2ðð)â(2ðð+1).Cn=(2nn)â(2nn+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯ Catalan æ°çè¡¨è¾¾å¼ (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¡¨è¾¾å¼ (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¯æ

èè ä¸è§ååè®¡æ°é®é¢ï¼è®¾ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸ (ð +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢ï¼åºå®å®çä¸ä¸ªè¾¹ä¸ºåºè¾¹ï¼å¯¹äºå¤è¾¹å½¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ä¸ªä¸è§ååï¼é½å¯ä»¥éæ©å®çä¸ä¸ªéåºè¾¹ï¼å æ¬ä¸è§ååæ¶æ°å çè¾¹ï¼æ è®°ï¼å¹¶å®åï¼è¿å ±æ (4ð +2)ð¶ð(4n+2)Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§ååå æ è®°çæ¹æ¡ï¼åè®¾ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸ (ð +3)(n+3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹å½¢ï¼ä»åºå®å®çä¸ä¸ªè¾¹ä¸ºåºè¾¹ï¼å¯¹äºå¤è¾¹å½¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥éæ©å®çä¸æ¡éåºè¾¹æ è®°ï¼ç¶åååä¸è§ååï¼è¿å ±æ (ð +2)ð¶ð+1(n+2)Cn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§æ è®°å ååçæ¹æ¡ï¼

![](./images/catalan-triangulation.svg)

å¦å¾æç¤ºï¼è¿ä¸¤ç»æä½å¾å°çç»æä¹é´å­å¨ææ¾çåå°ï¼å¯¹äº ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååå¹¶æ è®°çä¸ä¸ªç»æï¼å¯ä»¥å°å®çæ è®°è¾¹æ©å±ä¸ºä¸è§å½¢ï¼å®åææåçç»ç¹æ©å±ä¸ºä¸æ¡æ°è¾¹ï¼å¹¶å°è¿æ¡æ°è¾¹æä¸æ è®°ï¼è¿å°±å¾å°å¯¹ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ è®°å¹¶ååçä¸ä¸ªç»æï¼å¯¹äº ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ è®°å¹¶ååçä¸ä¸ªç»æï¼å¯ä»¥å°å®çæ è®°è¾¹åç¼©ä¸ºä¸ä¸ªç¹ï¼å¹¶å°åç¼©å¾å°çå¯¹è§çº¿æä¸æ è®°ï¼ä¸æååç¼©å¾å°çé¡¶ç¹ï¼è¿å°±å¾å°å¯¹ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååå¹¶æ è®°çä¸ä¸ªç»æï¼å æ­¤ï¼

(4ð+2)ð¶ð=(ð+2)ð¶ð+1.(4n+2)Cn=(n+2)Cn+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¨ä½æ´çï¼å¹¶ç»å ð¶0 =1C0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å° Catalan æ°çè¡¨è¾¾å¼ (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## ä¾é¢

[æ´è°· P1044 æ ](https://www.luogu.com.cn/problem/P1044)

å ¥æ é¡ºåºä¸º 1,2,â¦,ð1,2,â¦,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±ææå¯è½çåºæ é¡ºåºçæ»æ°ï¼

åèä»£ç 

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text #include <iostream> using namespace std ; int n ; long long f [ 25 ]; int main () { f [ 0 ] = 1 ; cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) f [ i ] = f [ i \- 1 ] * ( 4 * i \- 2 ) / ( i \+ 1 ); // è¿éç¨çæ¯å¸¸è§å½¢å¼ 4 cout << f [ n ] << endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text f = [ 0 ] * 25 f [ 0 ] = 1 n = int ( input ()) for i in range ( 1 , n \+ 1 ): f [ i ] = f [ i \- 1 ] * ( 4 * i \- 2 ) // ( i \+ 1 ) # è¿éç¨çæ¯å¸¸è§å½¢å¼ 4 print ( f [ n ]) ```   
---|---  
  
## ä¹ é¢

  * [Luogu P2532 [AHOI2012] æ å±é¶æ¢¯](https://www.luogu.com.cn/problem/P2532)
  * [Luogu P1641 [SCOI2010] çæå­ç¬¦ä¸²](https://www.luogu.com.cn/problem/P1641)
  * [Luogu P3200 [HNOI2009] æè¶£çæ°å](https://www.luogu.com.cn/problem/P3200)
  * [AtCoder Beginner Contest 205 E - White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)
  * [AtCoder Regular Contest 145 C - Split and Maximize](https://www.luogu.com.cn/problem/AT_arc145_c)
  * [Luogu P5014 æ°´ã®ä¸è§ï¼ä¿®æ¹çï¼](https://www.luogu.com.cn/problem/P5014)
  * [Luogu P3978 [TJOI2015] æ¦çè®º](https://www.luogu.com.cn/problem/P3978)

## åèèµæä¸æ³¨é

  * [Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/catalan.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/catalan.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Chrogeek](https://github.com/Chrogeek), [Fidelxyz](https://github.com/Fidelxyz), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [kfy666](https://github.com/kfy666), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [Peanut-Tang](https://github.com/Peanut-Tang), [purple-vine](https://github.com/purple-vine), [refinedcoding](https://github.com/refinedcoding), [shawlleyw](https://github.com/shawlleyw), [ShizuhaAki](https://github.com/ShizuhaAki), [Skyminers](https://github.com/Skyminers), [SukkaW](https://github.com/SukkaW), [ucSec](https://github.com/ucSec), [WFHFAQFXY](https://github.com/WFHFAQFXY), [xglight](https://github.com/xglight), [zryi2003](https://github.com/zryi2003)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
