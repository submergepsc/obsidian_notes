# å¬å¹³ç»åæ¸¸æ - OI Wiki

- Source: https://oi-wiki.org/math/game-theory/impartial-game/

# å ¬å¹³ç»åæ¸¸æ

åç½®ç¥è¯ï¼[åå¼è®ºç®ä»](../intro/)

æ¬æè®¨è®º [å ¬å¹³ç»åæ¸¸æ](../intro/#å)ï¼

å ¬å¹³ç»åæ¸¸æä¸­ï¼æåºç¡ä¹æéè¦çæ¯æ­£å¸¸ Nim æ¸¸æï¼SpragueâGrundy å®çæåºï¼æææ­£å¸¸è§åçå ¬å¹³ç»åæ¸¸æé½ç­ä»·äºä¸ä¸ªåå  Nim æ¸¸æï¼ç±æ­¤ï¼å¯ä»¥åå±åº SpragueâGrundy å½æ°å Nim æ°çæ¦å¿µï¼å®ä»¬å®å ¨å°å»ç»äºä¸ä¸ªæ­£å¸¸è§åçå ¬å¹³ç»åæ¸¸æï¼å æ­¤ï¼æ¬æé¦å å»ºç«äºæ­£å¸¸ Nim æ¸¸æçç»è®ºå SpragueâGrundy çè®ºï¼éåï¼æ¬æè®¨è®ºäºç®æ³ç«èµä¸­å¸¸è§çä¸äºå ¬å¹³ç»åæ¸¸æï¼

æåï¼æ¬æç®åå°è®¨è®ºäºåå¸¸ Nim æ¸¸æï¼åå¸¸æ¸¸æç¸å¯¹äºæ­£å¸¸æ¸¸ææ¥è¯´è¦å¤æå¾å¤ï¼ä¹å¾å°å¨ç®æ³ç«èµä¸­åºç°ï¼æ¬ææå°çæ¸¸æï¼å¦ææ²¡æç¹å«è¯´æï¼åé»è®¤ä¸ºæ­£å¸¸çå ¬å¹³ç»åæ¸¸æï¼

ãç¶æãããå±é¢ãä¸ãæ¸¸æã

æ¬æä¼äº¤æ¿å°ä½¿ç¨è¿ä¸ä¸ªè¯è¯­ï¼å¨åå¼è®ºä¸­ï¼æ¸¸æçç¶æï¼stateï¼éå¸¸å æ¬å°æ¸¸æçæä¸æ¶å»ä¸ºæ­¢ï¼ææå¯è½ä¸æ¸¸ææå ³çä¿¡æ¯ï¼å¨ä¸è¬çæ å½¢ä¸ï¼æ¸¸æçç¶æéå¸¸å æ¬åæ¹ç©å®¶è¿å¾çè¡å¨ãå·²ç»å®ç°çéæºåéå¼ãåæ¹å·²ç¥ä¿¡æ¯çå å®¹ç­ï¼æ¸¸æçå±é¢ï¼positionï¼ç¸å¯¹æ¥è¯´å¹¶éåå¼è®ºçæ åæ¯è¯­ï¼éå¸¸æå¨æ¸¸æçæä¸æ¶å»ï¼åæ¹ç©å®¶é¢å¯¹çå±å¿ï¼ä¾å¦æ£ç±»æ¸¸æä¸­åæ£å­çä½ç½®ç­ï¼ä» å¯¹äºå ¬å¹³ç»åæ¸¸æï¼ææ´ä¸è¬çé¶åãç¡®å®ãå®ç¾ä¿¡æ¯æ¸¸æï¼èè¨ï¼ç±äºæ¸¸æä¸æ¶åéæºæ§ï¼ä¸ç©å®¶æªæ¥çè¡å¨éåä¸æ¶çå½æ°åä¸å°è¾¾å½åå±é¢çåå²è·¯å¾ï¼å³ä¹ååæ¹çè¡ä¸ºï¼æ å ³ï¼æä»¥ï¼æ¸¸æçç¶æï¼stateï¼åå±é¢ï¼positionï¼æ²¡æåºå«ï¼ä¸é½å¯ä»¥çä½åå¼å¾ä¸çä¸ä¸ªç»ç¹ï¼nodeï¼ï¼ç±äºä¸ä¸ªæ¸¸æï¼gameï¼æ»æ¯å¯ä»¥ç±å®çåå§å±é¢æè¿°ï¼æä»¥ææ¶ä¹ä¼ç´æ¥ä½¿ç¨ãå±é¢ãä¸è¯ä»£ææ¸¸ææ¬èº«ï¼

## Nim æ¸¸æ

Nim æ¸¸æçè§åå¾ç®åï¼

Nim æ¸¸æ

å ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼ä¸¤åç©å®¶è½®æµåèµ°ä»»æä¸å ä¸­çä»»æå¤æç³å­ï¼ä½ä¸è½ä¸åï¼åèµ°æåä¸æç³å­çç©å®¶è·èï¼

å®¹æéªè¯ï¼Nim æ¸¸ææ¯æ­£å¸¸è§åçå ¬å¹³ç»åæ¸¸æï¼

ä¾å­

ä¸¾ä¸ªä¾å­ï¼å½åï¼æ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç³å­çæ°éåå«ä¸º 2,5,42,5,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯ä»¥åèµ°ç¬¬ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸­ç 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç©åï¼å±é¢å°±åæäº 0,5,40,5,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å¯ä»¥åèµ°ç¬¬ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç©åï¼å±é¢å°±åæäº 2,1,42,1,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ææä¸æ¶å»çå±é¢åä¸ºäº 0,0,50,0,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç²åèµ°äºç¬¬ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç©åï¼ä¹å°±æ¯åèµ°äºæåä¸ä¸ªç©åï¼æ­¤æ¶ç²è·èï¼

### åå¼å¾åç¶æ

Nim æ¸¸æä¸­ï¼å±é¢å¯è½çååå¯ä»¥ç¨åå¼å¾æ¥æè¿°ï¼

å°æ¯ä¸ä¸ªå¯è½çç¶æé½çä½æ¯å¾ä¸­çä¸ä¸ªç»ç¹ï¼å¹¶å°ç¶æåå®çåç»§ç¶æï¼å³éè¿ä¸æ¬¡æä½å¯ä»¥è¾¾å°çç¶æï¼è¿è¾¹ï¼å°±å¾å°ä¸ä¸ªæåæ ç¯å¾ï¼è¿å°±æ¯åå¼å¾ï¼å¾æ¯æ ç¯çï¼å ä¸º Nim æ¸¸æä¸­ï¼æ¯æ¬¡æä½ï¼ç³å­çæ»æ°éé½æ¯ä¸¥æ ¼åå°çï¼

ä¾å­

ä¾å¦ï¼å¯¹äºåå§å±é¢æ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ä¸æ¯å ç³å­çæ°éåå«ä¸º 1,1,21,1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Nim æ¸¸æï¼å¯ä»¥ç»å¶å¦ä¸çåå¼å¾ï¼

![åå¼å¾çä¾å­](./images/nim.svg)

é©¬ä¸å°±ä¼æå°ï¼å¾ä¸­ççº¢è²ç»ç¹è¡¨ç¤ºå¿ èç¶æï¼é»è²ç»ç¹è¡¨ç¤ºå¿ è´¥ç¶æï¼

ç±äº Nim æ¸¸ææ¯å ¬å¹³ç»åæ¸¸æï¼æ¯ä¸ªç©å®¶æ¯å¦æå¿ èç­ç¥ï¼åªåå³å½åæ¸¸ææå¤çç¶æï¼èä¸ç©å®¶çèº«ä»½æ å ³ï¼å æ­¤ï¼ææç¶æå¯ä»¥åä¸ºï¼å æï¼**å¿ èç¶æ** åï¼å æï¼**å¿ è´¥ç¶æ** ï¼åå«è®°ä¸º NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ1ï¼è¿ä¸ªå®ä¹éç¨äºææå ¬å¹³ç»åæ¸¸æï¼

éè¿ä¸è¿°å¼çï¼å¯ä»¥å½çº³å°å°ææç¶ææ è®°ä¸ºå¿ èç¶æåå¿ è´¥ç¶æï¼

å¼ç

æ­£å¸¸è§åçå ¬å¹³ç»åæ¸¸æä¸­ï¼

  1. æ²¡æåç»§ç¶æçç¶ææ¯å¿ è´¥ç¶æ PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. ä¸ä¸ªç¶ææ¯å¿ èç¶æ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½ä¸ä» å½å­å¨è³å°ä¸ä¸ªå®çåç»§ç¶æä¸ºå¿ è´¥ç¶æ PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. ä¸ä¸ªç¶ææ¯å¿ è´¥ç¶æ PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½ä¸ä» å½å®çææåç»§ç¶æåä¸ºå¿ èç¶æ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¯¹äºç¬¬ä¸æ¡ï¼å¦æç©å®¶å½åå·²ç»æ²¡æå¯éçè¡å¨ï¼é£ä¹ç©å®¶å·²ç»è¾æäºæ¸¸æï¼

å¯¹äºç¬¬äºæ¡ï¼å¦æè¯¥ç¶æè³å°æä¸ä¸ªåç»§ç¶æä¸ºå¿ è´¥ç¶æï¼é£ä¹ç©å®¶å¯ä»¥æä½å°è¯¥å¿ è´¥ç¶æï¼æ­¤æ¶ï¼å¯¹æé¢ä¸´äºå æå¿ è´¥ç¶æï¼ç©å®¶èªå·±å°±è·å¾äºèå©ï¼

å¯¹äºç¬¬ä¸æ¡ï¼å¦æä¸å­å¨ä¸ä¸ªåç»§ç¶æä¸ºå¿ è´¥ç¶æï¼é£ä¹æ è®ºå¦ä½ï¼ç©å®¶åªè½æä½å°å¿ èç¶æï¼æ­¤æ¶ï¼å¯¹æé¢ä¸´äºå æå¿ èç¶æï¼ç©å®¶èªå·±å°±è¾æäºæ¸¸æï¼

ææå ¬å¹³ç»åæ¸¸æä¸­ï¼åå¼å¾é½æ¯æåæ ç¯å¾ï¼æä»¥ï¼éè¿è¿ä¸æ¡æ§è´¨ï¼å¯ä»¥å¨ç»å¶åºåå¼å¾åï¼å¨ ð(|ð| +|ð¸|)O(|V|+|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å ï¼è®¡ç®åºæ¯ä¸ªç¶ææ¯å¿ èç¶æè¿æ¯å¿ è´¥ç¶æï¼å ¶ä¸­ï¼|ð||V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåå¼å¾çç¶ææ°ç®ï¼|ð¸||E|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè¾¹æ°ï¼å³ææç¶æå¯ä»¥éåçè¡å¨çæ°éçæ»åï¼

è¿ä¸å¼çå¯ä»¥æ¨å¹¿å°åå¸¸æ¸¸æåæåå¾å¯è½æç¯çæ å½¢ï¼ç¸å ³è®¨è®ºè¯¦è§ æåå¾æ¸¸æ ä¸èï¼

### Nim å

ç»§ç»­èå¯ Nim æ¸¸æï¼

éè¿ç»å¶åå¼å¾ï¼å¯ä»¥å¨ Î©(âðð=1ðð)Î©(âi=1nai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å æ±åºæä¸å±é¢æ¯å¦æ¯å æå¿ èï¼ä½æ¯ï¼è¿æ ·åçå¤æåº¦è¿é«ï¼æ æ³å®é åºç¨ï¼å®é ä¸ï¼å¯ä»¥åç° Nim æ¸¸æçç¶ææ¯å¦å æå¿ èï¼åªä¸å½åå±é¢çç³å­æ°ç®ç Nim åæå ³ï¼

Nim å

èªç¶æ° ð1,ð2,â¯,ðða1,a2,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **Nim å** ï¼Nim sumï¼å®ä¹ä¸º ð1 âð2 ââ¯ âðða1âa2ââ¯âan![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æè° Nim åï¼å°±æ¯ [å¼æè¿ç®](../../bit/#ä½è¿ç®)ï¼

å®ç

Nim æ¸¸æä¸­ï¼ç¶æ (ð1,ð2,â¯,ðð)(a1,a2,â¯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥ç¶æ PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ä¸ä» å½ Nim å

ð1âð2ââ¯âðð=0.a1âa2ââ¯âan=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å¯¹ææå¯è½çç¶æåºç¨å½çº³æ³ï¼

  1. å¦æ ðð =0ai=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ð =1,â¯,ði=1,â¯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼è¯¥ç¶ææ²¡æåç»§ç¶æï¼ä¸ Nim åç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½é¢æç«ï¼
  2. å¦æ ð =ð1 âð2 ââ¯ âðð â 0k=a1âa2ââ¯âanâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼éè¦è¯æè¯¥ç¶ææ¯å¿ èç¶æï¼ä¹å°±æ¯è¯´ï¼éè¦æé ä¸ä¸ªåæ³ç§»å¨ï¼ä½¿å¾åç»§ç¶æä¸ºå¿ è´¥ç¶æï¼ç±å½çº³åè®¾ï¼åªéè¦è¯æåç»§ç¶ææ»¡è¶³ ðâ²1 âðâ²2 ââ¯ âðâ²ð =0a1â²âa2â²ââ¯âanâ²=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨ Nim åï¼å³å¼æï¼çæ§è´¨ï¼è¿ç­ä»·äºè¯´ï¼å­å¨ä¸å ç³å­ï¼å° ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿èµ°è¥å¹²é¢ç³å­ï¼å¯ä»¥å¾å° ðð âðaiâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ðð >ðð âðai>aiâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å®é ä¸ï¼è®¾ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºä¸­ï¼æé«ä½ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼é£ä¹ï¼ä¸å®å­å¨æä¸ª ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾å®çäºè¿å¶ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºç¸åºçç³å­å ï¼å°±ä¸å®æ ðð >ðð âðai>aiâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ðð âðaiâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´é«ä½å ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ ·ï¼

  3. å¦æ ð1 âð2 ââ¯ âðð =0a1âa2ââ¯âan=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼éè¦è¯æè¯¥ç¶ææ¯å¿ è´¥ç¶æï¼ç±å½çº³åè®¾å¯ç¥ï¼åªè¦è¯æå®çææåç»§ç¶æç Nim åé½ä¸æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¯å¿ ç¶çï¼ä»»ä½åæ³ç§»å¨å° ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º ðâ²ð â ððaiâ²â ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¿ ç¶ä¼ä½¿å¾ Nim ååä¸º ðâ²ð âðð â 0aiâ²âaiâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±æ­¤ï¼å¯ä»¥å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å å¤æ­ Nim æ¸¸æçä¸ä¸ªç¶ææ¯å¦ä¸ºå æå¿ èç¶æï¼

## SpragueâGrundy çè®º

SpragueâGrundy çè®ºæåºï¼ææå ¬å¹³ç»åæ¸¸æé½ç­ä»·äºåå  Nim æ¸¸æï¼è¿ä¸ç»è®ºä¸»è¦åºç¨çåºæ¯ï¼å°±æ¯æ¸¸æç±å¤ä¸ªç¸äºç¬ç«çå­æ¸¸æç»æçæ å½¢ï¼æ­¤æ¶ï¼æ¸¸æçç¶æå¤å®å¯ä»¥éè¿è®¡ç®å­æ¸¸æç SG å½æ°å¼ç Nim åæ¥å®æï¼å¦ææ¸¸ææ¬èº«æ²¡æè¿æ ·çç»æï¼é£ä¹ï¼å¤å®å¿ èç¶æåå¿ è´¥ç¶æåªéè¦åºç¨åæåå¼å¾ä¸èç å¼çï¼

### æ¸¸æçè®°æ³

åæå·²ç»è¯´æï¼ææå ¬å¹³ç»åæ¸¸æé½å¯ä»¥éè¿ç»å¶åå¼å¾æ¥æè¿°ï¼ç±äºåå¼å¾ä¸­ï¼æ¯ä¸ªç¶æçæ§è´¨åªç±å®çåç»§ç¶æå³å®ï¼æä»¥ï¼å¯ä»¥å°åå¼å¾ä¸­çä¸ä¸ªç¶æ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¨å®çåç»§ç¶æçéåæ¥è¡¨ç¤ºï¼

ä¾å­ï¼ç»­ï¼

ä»¥ä¸æçåå¼å¾ä¸ºä¾ï¼å¯ä»¥å¾å°å¦ä¸ç¶æè¡¨ç¤ºï¼

ð0,0,0={},ð0,1,0={ð0,0,0}={{}},ð0,0,1={ð0,0,0}={{}},ð0,0,2={ð0,0,0,ð0,0,1}={{},{{}}},ð0,1,1={ð0,0,0,ð0,1,0,ð0,0,1}={{},{{}}},ð0,1,2={ð0,0,2,ð0,1,0,ð0,1,1}={{{}},{{},{{}}}}.S0,0,0={},S0,1,0={S0,0,0}={{}},S0,0,1={S0,0,0}={{}},S0,0,2={S0,0,0,S0,0,1}={{},{{}}},S0,1,1={S0,0,0,S0,1,0,S0,0,1}={{},{{}}},S0,1,2={S0,0,2,S0,1,0,S0,1,1}={{{}},{{},{{}}}}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð0,1,0 =ð0,0,1S0,1,0=S0,0,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð0,0,2 =ð0,1,1S0,0,2=S0,1,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ä¸ªæ¸¸æå¯ä»¥ç¨å®çåå§ç¶æè¡¨ç¤ºï¼

å°½ç®¡å ¬å¹³æ¸¸æçè¡¨ç¤ºå¯è½ç¸å½å¤æï¼åå  Nim æ¸¸æç¸å¯¹æ¥è¯´ç®åå¾å¤ï¼åªæä¸å ç³å­ï¼ç³å­æ°éä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å®å¯ä»¥è¡¨ç¤ºä¸º

â0={},Â âð={âð:ð<ð,Â ðâð}={â0,â1,â¯,â(ðâ1)}.â0={},Â ân={âm:m<n,Â mâN}={â0,â1,â¯,â(nâ1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼è®°å· âðân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç³å­æ°éä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çåå  Nim æ¸¸æï¼çåå§ç¶æï¼ï¼

ä¾å­ï¼ç»­ï¼

å©ç¨è¿ä¸è®°å·ï¼ä¸é¢çä¾å­ä¸­çç¶æå¯ä»¥ç®åå°è¡¨ç¤ºä¸º

ð0,0,0=â0,Â ð0,1,0=ð0,0,1=â1,Â ð0,0,2=ð0,1,1=â2,Â ð0,1,2={â1,â2}.S0,0,0=â0,Â S0,1,0=S0,0,1=â1,Â S0,0,2=S0,1,1=â2,Â S0,1,2={â1,â2}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¨éåçè®¨è®ºä¸­ï¼è®°å· ð âðTâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºå½çè§£ä¸ºç¶æ ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¶æ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåç»§ç¶æï¼

### æ¸¸æçåä¸ç­ä»·

æ¸¸æçç­ä»·å ³ç³»ï¼ä¾èµäºæ¸¸æçå2çæ¦å¿µï¼

æ¸¸æçå

æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **å** ï¼sumï¼ï¼æç§° **æ¸¸æç»å** ï¼combined gameï¼ï¼è®°ä½ ðº +ð»G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ææ¸¸æ

ðº+ð»={ð+ð»:ðâðº}âª{ðº+â:ââð»}.G+H={g+H:gâG}âª{G+h:hâH}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¸¸æçåï¼å¯ä»¥çè§£ä¸ºç±ä¸¤ä¸ªåæ¶è¿è¡ä¸äºä¸å¹²æ°çå­æ¸¸æç»æçæ¸¸æï¼ç©å®¶å¨æ¯ä¸æ­¥è½ä¸åªè½éæ©å ¶ä¸­ä¸ä¸ªå­æ¸¸æç§»å¨ä¸æ­¥ï¼ä¸æ¸¸æå¨ä¸¤ä¸ªå­æ¸¸æé½æ æ³ç§»å¨æ¶ç»æï¼æ¸¸æçåçæ¦å¿µï¼å¯ä»¥æ¨å¹¿å°ä»»æå¤ä¸ªæ¸¸æçæ å½¢ï¼ä¸æ»¡è¶³ç»åå¾åäº¤æ¢å¾ââä¹å°±æ¯è¯´ï¼å¤ä¸ªæ¸¸æç»åçç»æï¼åç»åè¿è¡çæ¬¡åºä»¥åæ¸¸æçé¡ºåºé½æ å ³ï¼Nim æ¸¸æå°±æ¯å¤ä¸ªåå  Nim æ¸¸æçåï¼

ä¸ä¸ªè§å¯æ¯ï¼å°½ç®¡åå  Nim æ¸¸æä¸­ï¼é¤äºæ²¡æç³å­çæ å½¢ï¼é½æ¯å æå¿ èç¶æï¼ä½æ¯è¿äºä¸åçåå  Nim æ¸¸æå¨åå ¶ä»çåå  Nim æ¸¸æç»åèµ·æ¥æ¶ï¼å¾å°çæ¸¸æå¹¶ä¸ç¸åï¼æ¯å¦ï¼æ¸¸æ âðân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªæå¨åå¦ä¸ä¸ª âðân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»åæ¶ï¼æè½å¾å°ä¸ä¸ªå¿ è´¥æ¸¸æï¼åææå ¶ä»çæ¸¸æ âðâ² â  âðânâ²â ân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»åï¼å¾å°çæ¸¸æé½æ¯å¿ èæ¸¸æï¼

è¿ä¸ªè§å¯å¸¦æ¥çå¯ç¤ºæ¯ï¼å¯ä»¥éè¿èå¯ä¸å ¶ä»æ¸¸æçåæ¥ç ç©¶æä¸ªæ¸¸æçæ§è´¨ï¼è¿å°±å¼åºäºæ¸¸æçç­ä»·çæ¦å¿µï¼

æ¸¸æçç­ä»·å ³ç³»

å¦æå¯¹äºæææ¸¸æ ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¸¸æ ðº1 +ð»G1+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðº2 +ð»G2+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½åå¤äºå¿ è´¥ç¶ææå¿ èç¶æï¼é£ä¹ï¼ç§°æ¸¸æ ðº1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðº2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **ç­ä»·** ï¼equivalentï¼ï¼è®°ä½ ðº1 âðº2G1âG2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å®¹æéªè¯ï¼è¿æ ·å®ä¹ç ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¡®å®æ¯å ¨ä½å ¬å¹³æ¸¸æä¸ç [ç­ä»·å ³ç³»](../../order-theory/#äºå)ï¼

### SpragueâGrundy å½æ°

å¯¹ Nim æ¸¸æçåæè¯´æï¼ä¸åçåå  Nim æ¸¸æäºä¸ç­ä»·ï¼ä½æ¯ï¼ææçå ¬å¹³æ¸¸æé½ç­ä»·äºæä¸ªåå  Nim æ¸¸æï¼ç±æ­¤ï¼å¯ä»¥ç»æ¯ä¸ªå ¬å¹³æ¸¸æé½åé ä¸ä¸ªæ°å­ï¼è¿å°±æ¯ SpragueâGrundy å½æ°ï¼

ä¸ºäºè¯æè¿äºç»è®ºï¼é¦å éè¦å»ºç«å ³äºæ¸¸æç­ä»·å ³ç³»çä¸¤ä¸ªå¼çï¼ç¬¬ä¸ï¼å°å¿ è´¥æ¸¸æåä»»ä½æ¸¸æç»åå°ä¸èµ·ï¼é½ååæ¥çæ¸¸æç­ä»·ï¼

å¼ç 1

å¯¹äºæ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä»»ä½å¿ è´¥æ¸¸æ ð´ âPAâP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðº âðº +ð´GâG+A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

æç §å®ä¹ï¼åªéè¦è¯æå¯¹äºä»»ä½æ¸¸æ ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ ðº +ð» âðº +ð´ +ð»G+HâG+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

å¦ææ¸¸æ ðº +ð»G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¿ èç­ç¥ï¼é£ä¹ï¼æ¸¸æ ðº +ð´ +ð»G+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æå¿ èç­ç¥ï¼å¦æå¯¹æå¨å­æ¸¸æ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­è¿è¡äºç§»å¨ï¼å°±è¿è¡ç§»å¨ï¼å°å®æ¢å¤è³å¿ è´¥ç¶æï¼å¦åï¼æç §æ¸¸æ ðº +ð»G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå¿ èç­ç¥ç§»å¨ï¼è¿æ ·ä¸å®è½ä¿è¯æç»çèå©ï¼

å¦ææ¸¸æ ðº +ð»G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼é£ä¹ï¼æ¸¸æ ðº +ð´ +ð»G+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åæ ·æ¯å¿ è´¥æ¸¸æï¼å ä¸ºæ è®ºè¿ä¸ååè¿è¡çæ¯å­æ¸¸æ ðº +ð»G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå­æ¸¸æ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çç§»å¨ï¼å¯¹æé½å¯ä»¥å¨ä¸ä¸ååå°ç¸åºå­æ¸¸ææ¢å¤è³å¿ è´¥ç¶æï¼æç»ï¼å æç©å®¶ä¸å®æ æ³è·èï¼

ç¬¬äºï¼ä¸¤ä¸ªæ¸¸æç­ä»·ï¼å½ä¸ä» å½å®ä»¬çåæ¯å¿ è´¥æ¸¸æï¼è¿ä¸å¼çæä¾äºè¯æä¸¤ä¸ªæ¸¸æç­ä»·çæ¹æ³ï¼

å¼ç 2

æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·ï¼å½ä¸ä» å½ ðº +ðºâ² âPG+Gâ²âP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼

è¯æ

å¦ææ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·ï¼é£ä¹ï¼ðº +ðºâ²G+Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðº +ðºG+G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¶å¿ èæåæ¶å¿ è´¥ï¼èæ¸¸æ ðº +ðºG+G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼è¿æ¯å ä¸ºï¼å¯¹äºå æç©å®¶çä»»ä½æä½ï¼åæç©å®¶é½å¯ä»¥å¨å¦ä¸ä¸ªå­æ¸¸æä¸­éåç¸åçè¡å¨ï¼æåä¸å®æ¯å æç©å®¶æ æ³ç§»å¨ï¼

åè¿æ¥ï¼å¦æ ðº +ðºâ²G+Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼é£ä¹ï¼ç±å¼ç 1 å¯ç¥ï¼ðº âðº +(ðº +ðºâ²) =(ðº +ðº) +ðºâ² âðºâ²GâG+(G+Gâ²)=(G+G)+Gâ²âGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å©ç¨è¿äºå¼çï¼å¯ä»¥å¾å°å¦ä¸å®çï¼

å®çï¼SpragueâGrundyï¼

å¯¹äºä»»ä½ä¸ä¸ªï¼æéï¼å ¬å¹³æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½å­å¨ ð âðnâN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ðº â âðGâân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

è¯æ

è¦è¯æå®ççç»è®ºï¼å¯ä»¥åºç¨æ°å­¦å½çº³æ³ï¼è®¾æ¸¸æ ðº ={ðº1,ðº2,â¯,ðºð}G={G1,G2,â¯,Gk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å½çº³åè®¾å¯ç¥ï¼å­å¨ ð1,ð2,â¯,ððn1,n2,â¯,nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðºð â âððGiââni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯ä»¥èå¯æ¸¸æ

ðºâ²={âð1,âð2,â¯,âðð}.Gâ²={ân1,ân2,â¯,ânk}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°è¦è¯æçæ¯ï¼ðºâ² â âðGâ²ââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð =mexâ¡{ð1,ð2,â¯,ðð}m=mexâ¡{n1,n2,â¯,nk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ²¡æåºç°å¨éåä¸­çæå°èªç¶æ°ï¼

ç¬¬ä¸æ­¥ï¼éè¦è¯´æ ðº âðºâ²GâGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ® å¼ç 2ï¼åªéè¦è¯ææ¸¸æ ðº +ðºâ²G+Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼ä¸å¦¨åè®¾ ðº â  â0Gâ â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå æç©å®¶éæ© ðºðGi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹åæç©å®¶å°±å¯ä»¥éæ© âððâni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¿æ¥ï¼å¦æå æç©å®¶éæ©äº âððâni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæç©å®¶å°±å¯ä»¥éæ© ðºðGi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»ä¹ï¼å¨è¿ä¸¤æ­¥æä½åï¼æ¸¸æåä¸º ðºð + âððGi+âni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å¼ç 2 å ðºð â âððGiââni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¯å¿ è´¥æ¸¸æï¼è¿å°±è¯æäº ðº âðºâ²GâGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¬¬äºæ­¥ï¼éè¦è¯´æ ðºâ² â âðGâ²ââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ® å¼ç 2ï¼åªéè¦è¯æ ðºâ² + âðGâ²+âm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥æ¸¸æï¼ä¸å¦¨åè®¾ ðºâ² â  â0Gâ²â â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå æç©å®¶éæ©äº âðð â âðâniââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ ¹æ® ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå®ä¹ï¼åæç©å®¶å°±å¯ä»¥éæ© âðð âðºâ²âniâGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°æ¸¸æå±é¢åä¸º âðð + âðð âPâni+âniâP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æå¿ è´¥ï¼å¦æå æç©å®¶éæ©äº âðð âðºâ²âniâGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð <ðni<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åæç©å®¶å¯ä»¥éæ© âðð â âðâniââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¸¸æå±é¢åæ ·åä¸º âðð + âðð âPâni+âniâP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æå¿ è´¥ï¼æåï¼å¦æå æç©å®¶éæ©äº âðð âðºâ²âniâGâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð >ðni>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åæç©å®¶å¯ä»¥éæ© âð â âððâmââni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¸¸æå±é¢åä¸º âð + âð âPâm+âmâP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æå¿ è´¥ï¼è¿å°±è¯æäº ðºâ² â âðGâ²ââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±ç­ä»·å ³ç³»çä¼ éæ§å¯ç¥ï¼ðº â âðGââm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±å®æäºå½çº³ï¼è¯ææææ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ç­ä»·äºä¸ä¸ªåå  Nim æ¸¸æï¼

è¿ä¸ç»è®ºè¯´æï¼å¯ä»¥ä¸ºæ¯ä¸ä¸ªå ¬å¹³æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½åé ä¸ä¸ªèªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ðº â âðGâân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

Nim æ°

ä¸ä¸ªå ¬å¹³æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºç **Nim æ°** ï¼nimberï¼å°±æ¯ä½¿å¾ ðº â âðGâân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«çå¯ä¸èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿ä¸ªå°å ¬å¹³æ¸¸ææ å°å° Nim æ°çå½æ°ç§°ä¸º **SpragueâGrundy å½æ°** ï¼SpragueâGrundy functionï¼ï¼ç®ç§° **SG å½æ°** ï¼è®°ä½ SGâ¡( â )SGâ¡(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºæ¯ä¸ªå ¬å¹³æ¸¸æçç¶æé½æ¯å¦ä¸ä¸ªå ¬å¹³æ¸¸æï¼æä»¥ï¼å¯¹äºå ¬å¹³æ¸¸æçæ¯ä¸ä¸ªç¶æé½å¯ä»¥è®¡ç®ç¸åºç Nim æ°ï¼ä¹ç§°ä¸ºç¸åºç SG å½æ°å¼ï¼

æ ¹æ®æ¬èå®ççè¯æè¿ç¨å¯ç¥ï¼SpragueâGrundy å½æ°å¯ä»¥éå½å°è®¡ç®å¦ä¸ï¼

æ¨è®º

å ¬å¹³æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çä¸ä¸ªç¶æ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºç SpragueâGrundy å½æ°å¼ SGâ¡(ð¥)SGâ¡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³

SGâ¡(ð¥)=mexâ¡{SGâ¡(ð¥â²):ð¥â²âð¥}.SGâ¡(x)=mexâ¡{SGâ¡(xâ²):xâ²âx}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼mexâ¡(ð´) :=min{ð âð :ð âð´}mexâ¡(A):=min{nâN:nâA}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ²¡æåºç°å¨éå ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çæå°èªç¶æ°ï¼

ä¹å°±æ¯è¯´ï¼ä¸ä¸ªç¶æç SG å½æ°å¼ï¼ç­äºå®çææåç»§ç¶æç SG å½æ°å¼ç mexmex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼ï¼

å©ç¨ SG å½æ°å¼ï¼å³ Nim æ°ï¼ï¼å¯ä»¥å¤æ­ä¸ä¸ªç¶ææ¯å¦ä¸ºå æå¿ èç¶æï¼

æ¨è®º

å ¬å¹³æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çä¸ä¸ªç¶æ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å æå¿ èç¶æï¼å½ä¸ä» å½ SGâ¡(ð¥) â 0SGâ¡(x)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æåï¼æ¸¸æçåç SG å½æ°å¼ï¼å°±æ¯å­æ¸¸æç SG å½æ°å¼ç Nim åï¼å³å¼æï¼ï¼

å®çï¼SpragueâGrundyï¼

å¯¹äºå ¬å¹³æ¸¸æ ðº1,ðº2,â¯,ðºðG1,G2,â¯,Gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

SGâ¡(ðº1+ðº2+â¯+ðºð)=SGâ¡(ðº1)âSGâ¡(ðº2)ââ¯âSGâ¡(ðºð).SGâ¡(G1+G2+â¯+Gn)=SGâ¡(G1)âSGâ¡(G2)ââ¯âSGâ¡(Gn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å ä¸º âð1 + âð2 +â¯ + âððâa1+âa2+â¯+âan![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ç³å­æ°éä¸º (ð1,ð2,â¯,ðð)(a1,a2,â¯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Nim æ¸¸æï¼æä»¥ï¼æ ¹æ® Nim æ¸¸æçç»è®ºå¯ç¥ï¼æ¸¸æ

âð1+âð2+â¯+âðð+â(ð1âð2ââ¯âðð)âa1+âa2+â¯+âan+â(a1âa2ââ¯âan)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¯å æå¿ è´¥çï¼æ ¹æ® å¼ç 2ï¼æ

âð1+âð2+â¯+âððââ(ð1âð2ââ¯âðð).âa1+âa2+â¯+âanââ(a1âa2ââ¯âan).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼æ

SGâ¡(âð1+âð2+â¯+âðð)=ð1âð2ââ¯âðð.SGâ¡(âa1+âa2+â¯+âan)=a1âa2ââ¯âan.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ðð =SGâ¡(ðºð)ai=SGâ¡(Gi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ ðºð â âððGiââai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å©ç¨ ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä»£æ°æ§è´¨ï¼æ

(ðº1+ðº2+â¯+ðºð)+(âð1+âð2+â¯+âðð)=ðâð=1(ðºð+âðð)âP.(G1+G2+â¯+Gn)+(âa1+âa2+â¯+âan)=âi=1n(Gi+âai)âP.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å°±æ

SGâ¡(ðº1+ðº2+â¯+ðºð)=SGâ¡(âð1+âð2+â¯+âðð)=ð1âð2ââ¯âðð=SGâ¡(ðº1)âSGâ¡(ðº2)ââ¯âSGâ¡(ðºð).SGâ¡(G1+G2+â¯+Gn)=SGâ¡(âa1+âa2+â¯+âan)=a1âa2ââ¯âan=SGâ¡(G1)âSGâ¡(G2)ââ¯âSGâ¡(Gn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿ä¸å®çï¼å¨è®¡ç®æ¸¸æçåç SG å½æ°å¼æ¶ï¼å¯ä»¥å¤§å¹ ç®åè®¡ç®ï¼

ç±æ­¤ï¼å¯ä»¥æ»ç»åº SG å½æ°å¼çè®¡ç®æ¹æ³ï¼

  * å¯¹äºå¤ä¸ªç¬ç«çæ¸¸æï¼å¯ä»¥åå«è®¡ç®å®ä»¬ç SG å½æ°å¼ï¼åæ± Nim åï¼
  * å¯¹äºåä¸ªæ¸¸æï¼æ¯ä¸ªç¶æç SG å½æ°å¼é½æ¯å®çææåç»§ç¶æç SG å½æ°å¼ç mexmex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼ï¼
  * ç¹å«å°ï¼ç»æ­¢ç¶æï¼å³æ²¡æåç»§ç¶æçç¶æï¼ç SG å½æ°å¼ä¸º mexâ¡â  =0mexâ¡â =0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### Nim æ°

ææçå ¬å¹³æ¸¸æé½å¯ä¸å¯¹åºä¸ä¸ª Nim æ°ï¼ï¼æéï¼Nim æ°çéåå°±æ¯èªç¶æ°é ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼å®çä»£æ°æ§è´¨åèªç¶æ°éä¸åï¼å ·ä½æ¥è¯´ï¼Nim æ°ä¸å¯ä»¥å®ä¹ Nim å ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãNim ä¹ç§¯ ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ç§è¿ç®ï¼

Nim æ°çè¿ç®

å¯¹äº Nim æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å®ä¹ï¼

  * Nim å ð âð =mexâ¡({ðâ² âð :ðâ² <ð,Â ðâ² âð} âª{ð âðâ² :ðâ² <ð,Â ðâ² âð})aâb=mexâ¡({aâ²âb:aâ²<a,Â aâ²âN}âª{aâbâ²:bâ²<b,Â bâ²âN})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * Nim ç§¯ ð âð =mexâ¡({(ðâ² âð) â(ð âðâ²) â(ðâ² âðâ²) :ðâ² <ð,Â ðâ² <ð,Â ðâ²,ðâ² âð})aâb=mexâ¡({(aâ²âb)â(aâbâ²)â(aâ²âbâ²):aâ²<a,Â bâ²<b,Â aâ²,bâ²âN})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å ¨ä½ Nim æ°å¨è¿ç® ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ææä¸ä¸ªç¹å¾ä¸º 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [å](../../algebra/basic/#å)ï¼èä¸ï¼è¿äºè¿ç®ä»¥åå®ä»¬çéè¿ç®ï¼å¯¹äºå 22ð22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª Nim æ°æ¯å°é­çï¼è¿å°±å¾å°ä¸ç³»åå¤§å°ä¸º 22ð22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [æéå](../../algebra/field-theory/#æéå) ð 22ðF22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å¸¸è§çå ¬å¹³æ¸¸æ

å°½ç®¡ SpragueâGrundy çè®ºå®å ¨è§£å³äºå ¬å¹³æ¸¸æçé®é¢ï¼ä½æ¯ï¼å¤çå®é çå ¬å¹³æ¸¸ææ¶ï¼ç´æ¥åºç¨ SpragueâGrundy å®çè®¡ç®æçä»ç¶ä¸é«ï¼æ¯å¦ï¼Nim æ¸¸æä¸­ï¼æ´åè®¡ç® SpragueâGrundy å¼çå¤æåº¦æ¯ææ°çº§çï¼å æ­¤ï¼å¾å¾éè¦éè¿æè¡¨çæ¹å¼çæµå ·ä½çå ¬å¹³æ¸¸æçç»è®ºï¼

æ¬èåä¸¾äºä¸äºå¸¸è§çå ¬å¹³æ¸¸æåå ¶ç»è®ºï¼åè¿°ç»è®ºæ¶ï¼æ¬èåªç»åºäºå¿ èåå¿ è´¥ç¶æçå¤æ­æ³åï¼è³äºå¿ èç­ç¥ï¼å°±æ¯è¿è¡æ°å½çæä½ï¼ä½¿å¾çç»å¯¹æçå±é¢æ°å¥½ä¸ºå¿ è´¥ç¶æï¼ç±äºç®æ³ç«èµä¸­ç»å¸¸åºç°è¿äºæ¸¸æçåä½ï¼æä»¥ï¼ææ¡æ¯ä¸ªæ¸¸æçç»è®ºçè¯æè¿ç¨ä¹å¾éè¦ï¼

æ¬èç»è®ºçè¯ææ¹æ³

æ¬èç»è®ºçè¯æé½æ¯éªè¯æ§çï¼å¯¹äºä¸ä¸ªæ¸¸æï¼ç»è®ºä¸­ä¼æè¿°å®çå æå¿ è´¥ç¶æåå æå¿ èç¶æï¼è¯æä¸­ï¼åªéè¦éªè¯ä»ä¸ä¸ªå æå¿ è´¥ç¶æåºåï¼åªè½å¾å°å æå¿ èç¶æï¼èä»å æå¿ èç¶æåºåï¼æ»è½å¾å°è³å°ä¸ä¸ªå æå¿ è´¥ç¶æï¼è¦å°è¿äºè¯ææ¹åä¸ºä¸¥æ ¼çè¯æï¼éè¦å»ºç«åå¼å¾ï¼ç¶åå¯¹åå¼å¾ä¸çç¶æåºç¨æ°å­¦å½çº³æ³ï¼èè¿äºéªè¯çæ­¥éª¤å°±æ¯å ¶ä¸­çå½çº³é¨åï¼

### Bachet æ¸¸æ

ç¸è¾äºåå  Nim æ¸¸æï¼Bachet æ¸¸æéå¶äºæ¯æ¬¡å¯ä»¥åèµ°çç³å­çæ°éï¼

Bachet æ¸¸æ

æä¸å ç³å­ï¼å ±è®¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼ä¸¤åç©å®¶è½®æµåèµ°è³å° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æãè³å¤ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼åèµ°æåä¸æç³å­çç©å®¶è·èï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

æ¸¸æå æå¿ è´¥ï¼å½ä¸ä» å½ ð â¡0(modð +1)nâ¡0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æä¸

å½ ð â¢0(modð +1)nâ¢0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åªè¦åèµ° ðmod(ð+1) â[1,ð]nmod(k+1)â[1,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼å°±è½ä¿è¯å¯¹æå¤äºå¿ è´¥ç¶æï¼å æ­¤ï¼æ­¤æ¶æ¯å æå¿ èç¶æï¼

åè¿æ¥ï¼å½ ð â¡0(modð +1)nâ¡0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼é£ä¹ï¼è¦ä¹å·²ç»æ²¡æéæ©ï¼è¦ä¹èªå·±åèµ° ðâ²kâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­åï¼å¯¹æç´§æ¥çå¯ä»¥åèµ° ð +1 âðâ²k+1âkâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼è®©èªå·±åå°å¿ è´¥ç¶æï¼

è¯æäº

ä½ä¸º SpragueâGrundy å®ççåºç¨ï¼å¯ä»¥è®¡ç® ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåªå©ä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­æ¶ï¼å¯¹åºå±é¢ç SG å½æ°å¼ï¼

å¯¹äº ð â¤ðnâ¤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å½çº³å°è¯æ ð(ð) =ðf(n)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸åå  Nim æ¸¸æç¸åï¼å ä¸ºåèµ°ç³å­æ°ç®çéå¶æ²¡æåæ¥ä½ç¨ï¼å¯¹äº ð >ðn>k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¯ä»¥è¯æ ð(ð) =ðmod(ð+1)f(n)=nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼æ

ð(ð)=mexâ¡{ð(ðâð),ð(ðâð+1),â¯,ð(ðâ1)}.f(n)=mexâ¡{f(nâk),f(nâk+1),â¯,f(nâ1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éåäºæ¨¡ ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½ä½æ°ï¼é¤äº ðmod(ð+1)nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å°±æ ð(ð) =ðmod(ð+1)f(n)=nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### Moore's Nim-k æ¸¸æ

ç¸è¾äº Nim æ¸¸æï¼Moore's Nim-ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¸¸æå è®¸ä¸æ¬¡æ§ä» ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç³å­å ä¸­åç³å­ï¼

Moore's Nim-ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¸¸æ

å ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼ä¸¤åç©å®¶è½®æµåèµ°è³å° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ãè³å¤ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸­çä»»æå¤æç³å­ï¼ä½ä¸è½ä¸åï¼åèµ°æåä¸æç³å­çç©å®¶è·èï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

å°æ¯ä¸å ç³å­çæ°ç®é½è¡¨ç¤ºä¸ºäºè¿å¶æ°ï¼å¹¶å¯¹æ¯ä¸ªæ°ä½ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½ç»è®¡æå¤å°å ç³å­æ°ç®çç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®¡ç®è¿ä¸ªæ°ç®å¯¹äº (ð +1)(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ°ï¼å¦æå¯¹äºæ¯ä¸ªæ°ä½ï¼è¿ä¸ªä½æ°é½ç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å æå¿ è´¥ï¼å¦åï¼å æå¿ èï¼

è¯æ

ä»¿ç § Nim æ¸¸æçç»è®ºçè¯æï¼å¾å®¹æè¯ææ¬ç»è®ºï¼è®¾ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä½æ°ä¸ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæé«äºè¿å¶ä½ï¼ä¸å¯¹åºçä½æ°ä¸º ðâ² â¤ðkâ²â¤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¿ èç­ç¥ä¸ºï¼å¨ç³å­æ°ç®äºè¿å¶ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³å­å ä¸­ï¼éæ© ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ï¼å¹¶éæ©ç§»èµ°çç³å­æ°ç®æ°å¥½ä½¿å¾å¯¹æå±é¢ä¸­ï¼æ¯ä¸ªæ°ä½çä½æ°é½æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä¸éè¦è¯´æçæ¯ï¼æååèµ°ç³å­æ°éçéæ©æ»æ¯å¯è¡çï¼

å®é ä¸ï¼åªè¦éå® ðâ²kâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼æ¯å é½åèµ° 2ð2d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼å°±è½ä½¿å¾ç»æä¸­ï¼ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä½æ°åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºæ´ä½çæ°ä½çä½æ°ï¼å°è¿äºä½æ°éæææ´¾ç»æä¸ä¸ªå å³å¯ï¼

### é¶æ¢¯ Nim æ¸¸æ

é¶æ¢¯ Nim æ¸¸æç¨å¾®å¤æä¸äºï¼å®å è®¸ç³å­å¨ç¸é»çå ä¹é´ç§»å¨ï¼

é¶æ¢¯ Nim æ¸¸æ

å ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼ä¸¤åç©å®¶è½®æµæä½ï¼æ¯æ¬¡æä½ä¸­ï¼è¦ä¹åèµ°ç¬¬ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ä¸­çä»»æå¤æï¼è¦ä¹å°ç¬¬ ð >1i>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ä¸­çä»»æå¤æç§»å¨å°ç¬¬ ð â1iâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ï¼ä½ä¸è½ä¸åä»»ä½æä½ï¼åèµ°æåä¸æç³å­çç©å®¶åèï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

æ¸¸æå æå¿ è´¥ï¼å½ä¸ä» å½å¥æ°å ç³å­æ°éç Nim å ð1 âð3 ââ¯ âððâ1+(ðmod2) =0a1âa3ââ¯âanâ1+(nmod2)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

ä»»ä½ç©å®¶å°å¶æ°å çç³å­ç§»å¨å°å¥æ°å æ¶ï¼å¯¹æé½å¯ä»¥å°è¿äºç³å­ç»§ç»­ç§»å¨å°ä¸ä¸ä¸ªå¶æ°å ï¼æç§»èµ°ï¼ï¼å æ­¤ï¼è¿æ ·çç§»å¨ä¸ä¼å½±åå¥æ°å çå±é¢ï¼æ­¤æ¶ï¼æ¯ä¸ä¸ªå¥æ°å åä¸ç§»å¨å°ç¸é»çå¶æ°å ï¼æç§»èµ°ï¼é½å¯ä»¥çä½ç¬ç«çåå  Nim æ¸¸æï¼æ ¹æ® SpragueâGrundy å®çå ³äºæ¸¸æçåçç»è®ºï¼é¶æ¢¯ Nim æ¸¸æç SG å½æ°å¼ï¼æ¯è¿äºå­æ¸¸æç SG å½æ°å¼ç Nim åï¼è¿å°±å¾å°ä¸è¿°ç»è®ºï¼

### Fibonacci Nim æ¸¸æ

Fibonacci Nim æ¸¸æç±»ä¼¼ Bachet æ¸¸æï¼åªæä¸å ç³å­ï¼ä¸éå¶äºæ¯æ¬¡åèµ°çæ°éï¼ä¸ Bachet æ¸¸æä¸åï¼Fibonacci Nim æ¸¸æä¸­ï¼æ¯æ¬¡åèµ°çæ°éçéå¶æ¯å¨æçï¼

Fibonacci Nim æ¸¸æ

æä¸å ç³å­ï¼å ±è®¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼ä¸¤åç©å®¶è½®æµåç³å­ï¼ç¬¬ä¸ä¸ªè¡å¨çç©å®¶ä¸éå¶åèµ°çç³å­æ°ç®ï¼ä½æ¯ä¸è½åå®ç³å­ï¼éåï¼æ¯æ¬¡åèµ°çç³å­æ°ç®ä¸å¾è¶ è¿ä¸æ¬¡ï¼æå¯¹æååï¼åèµ°çç³å­æ°ç®çäºåï¼æ¯æ¬¡åèµ°çç³å­çæ°ç®ä¸å¾ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åèµ°æåä¸æç³å­çç©å®¶è·èï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

æ¸¸æå¼å§æ¶ï¼å æå¿ è´¥ï¼å½ä¸ä» å½ç³å­æ°ç® ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ [Fibonacci æ°](../../combinatorics/fibonacci/)ï¼

è¯æ

è®¾ ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå½åå±é¢å¯ç§»èµ°ç³å­æ°éçéé¢ï¼quotaï¼ï¼é£ä¹ï¼ç¬¬ä¸ååä¸­ï¼ð =ð â1q=nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¹åçååä¸­ï¼ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸æ¬¡ï¼å¯¹æï¼ç§»èµ°çç³å­æ°ç®çäºåï¼èå¯å©ä½ç³å­æ°ç® ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [Fibonacci ç¼ç ](../../combinatorics/fibonacci/#ææ³¢é£å¥ç¼ç)ï¼ä¹å°±æ¯å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä¸å°åè§£ä¸ºä¸ç³»åä¸ç¸é»çãæ­£ç Fibonacci æ°çåï¼éè¦è¯æçæ¯ï¼å½åç¶ææ¯å¿ èç¶æï¼å½ä¸ä» å½ ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤§äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåè§£ä¸­çæå° Fibonacci æ°ï¼

å¿ èç­ç¥æ¯ï¼å¦æå¯ä»¥ï¼ç§»èµ°ææå©ä½ç³å­ï¼å¦åï¼ç§»èµ°åè§£ä¸­æå°ç Fibonacci æ°ï¼ç±äºåè§£ä¸­ï¼æ¬¡å°ç Fibonacci æ°ä¸å®ä¸¥æ ¼å¤§äºæå°ç Fibonacci æ°çä¸¤åï¼æä»¥ï¼åªè¦å¤äºå¿ èç¶æçå½ååååä¸èµ°ææç³å­ï¼å¯¹æå¨ä¸ä¸ååä¹åä¸èµ°æ¬¡å°ç Fibonacci æ°ï¼ä¹å°±æ¯ä¸ä¸ååæå°ç Fibonacci æ°ï¼ï¼å¯¹æä¸å®å¤äºå¿ è´¥ç¶æï¼

åè¿æ¥ï¼å¦æå½åå¤äºå¿ è´¥ç¶æï¼é£ä¹ï¼è®¾å½ååèµ°çæ°ç®ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¸å®ä¸¥æ ¼å°äºå½ååè§£ä¸­çæå° Fibonacci æ° ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾ä¸ä¸ååæå°ç Fibonacci æ°æ¯ ð¹â²Fâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¸å®ä¹æ¯ ð¹ âðFâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçåè§£ä¸­æå°ç Fibonacci æ°ï¼è®¾ ð¹â² =ð¹â³ +ð¹â´Fâ²=Fâ³+Fâ´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¹â³ >ð¹â´Fâ³>Fâ´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ð¹â´,ð¹â³,ð¹â²Fâ´,Fâ³,Fâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Fibonacci æ°åä¸­ç¸é»ä¸é¡¹ï¼å¦æ ð <ð¹â³k<Fâ³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å©ç¨ Fibonacci ç¼ç è®¡ç® ð +(ð¹ âð)k+(Fâk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ä¸éè¦è¿ä½ï¼èªç¶å¾ä¸å° ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼ä¸å®æ ð â¥ð¹â³kâ¥Fâ³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æï¼ä¸ä¸ååçéé¢ 2ð >ð¹â³ +ð¹â´ =ð¹â²2k>Fâ³+Fâ´=Fâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯å¿ èç¶æï¼

### Wythoff æ¸¸æ

Wythoff æ¸¸æå è®¸åæ¶ä»å¤å ç³å­ä¸­ç§»é¤ï¼ä½æ¯è¦æ±æ¯å ç§»é¤ç¸åæ°éçç³å­ï¼

Wythoff æ¸¸æ

æä¸¤å ç³å­ï¼åå«æ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼ä¸¤åç©å®¶è½®æµä»å ¶ä¸­ä¸å æä¸¤å ä¸­åç³å­ï¼ä¸è½ä¸åï¼ä½è¦æ±ä»ä¸¤å é½åç³å­æ¶ï¼åèµ°çç³å­æ°éå¿ é¡»ç¸åï¼åèµ°æåä¸æç³å­çç©å®¶è·èï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

ä¸å¦¨è®¾ ð1 â¤ð2a1â¤a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å æå¿ è´¥ï¼å½ä¸ä» å½ ð1 =â(ð2 âð1)ðâa1=â(a2âa1)Ïâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð =(â5 +1)/2Ï=(5+1)/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é»éåå²æ¯ï¼

ä¸ºäºè¯æè¿ä¸ç»è®ºï¼éè¦ç¨å°å¦ä¸å¼çï¼

Beatty åºå

è®¾ ð >1r>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ çæ°ï¼å®çæç Beatty åºåæ¯ Bð ={âððâ :ð âð+}Br={âkrâ:kâN+}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

Rayleigh å®ç

è®¾ ð,ð  >1r,s>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸¤ä¸ªæ çæ°ï¼ä¸ 1ð +1ð  =11r+1s=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åºå BðBr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å Bð Bs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æææ­£æ´æ°é ð+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªååï¼æ­¤æ¶ï¼å®ä»¬ä¹ç§°ä¸ºäºè¡¥ç Beatty åºåï¼

è¯æ

è®¾ Að ={ðð :ð âð+}Ar={kr:kâN+}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèå°éå A =Að âªAâA=ArâªAâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éçå ç´ æåºå¾å°åºå {ðð}ðâð+{ai}iâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éè¦è¯æçæ¯ï¼ð =âððâi=âaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ð âð+iâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å°±è½å¾å° Bð âªBð BrâªBs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ­£æ´æ°é ð+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªååï¼

é¦å ï¼è¯æåºåéæ²¡æéå¤çå ç´ ï¼åè®¾ä¸ç¶ï¼å­å¨ ð,â âð+k,ââN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð =âð kr=âs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼é£ä¹ï¼æ

âð=ðð =ðâ1.âk=rs=râ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯ï¼ç­å¼å·¦ä¾§æ¯æçæ°ï¼ç­å¼å³ä¾§æ¯æ çæ°ï¼çç¾ï¼å æ­¤ï¼åºåçæ°å­åä¸ç¸åï¼

ç¶åï¼è¯æéå AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å°äºç­äº ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°æ°æ âððââaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼ä¸å¦¨è®¾ ðð âAðaiâAr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ðð =ððai=kr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯¹éå AðAr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å AâAâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ åå«è®¡æ°ï¼å°±å¾å°å°äºç­äº ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ´æ°æ°æ

ð+âððð â=ð+âð(ðâ1)â=âððâ=âððâk+âkrsâ=k+âk(râ1)â=âkrâ=âaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ªï¼è¿èï¼ç±äºåºå {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸¥æ ¼éå¢çï¼å°äºç­äº ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°æ°æ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼è¿å°±å¾å° ð =âððâi=âaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±æ­¤ï¼å¯ä»¥å¾å°åè¿°ç»è®ºçè¯æï¼

Wythoff æ¸¸æç»è®ºçè¯æ

å¯¹äºææ ð1 <ð2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å æå¿ è´¥çç¶æ (ð1,ð2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ð =ð2 âð1 âð+k=a2âa1âN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð1 =âððâa1=âkÏâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð2 =âð(ð +1)âa2=âk(Ï+1)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é»éåå²æ¯ï¼æä»¥ 1ð +1ð+1 =11Ï+1Ï+1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± Rayleigh å®çå¯ç¥ï¼åºå {âððâ}{âkÏâ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å âð(ð +1)ââk(Ï+1)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æææ­£æ´æ°é ð+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªååï¼è¿å ¶å®è¯´æï¼ææ ð1 <ð2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å æå¿ è´¥çç¶æ (ð1,ð2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼åé ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°åéå ¨ä½æ­£æ´æ°ä¸æ¬¡ï¼ä¸å®ä»¬çå·® ð2 âð1a2âa1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ°åéå ¨ä½æ­£æ´æ°ä¸æ¬¡ï¼

ç±äº Wythoff æ¸¸æä¸­ï¼ä¸æ¬¡åæ³çæä½è¦ä¹ä¿æåéä¹ä¸ä¸åï¼è¦ä¹ä¿æåéä¹å·®ä¸åï¼æä»¥ï¼ä»ä¸ä¸ªå æå¿ è´¥ç¶æå¼å§ï¼ç¡®å®æ æ³ç±ä¸æ¬¡åæ³çæä½ä¸­å¾å°å¦ä¸ä¸ªå æå¿ è´¥ç¶æï¼åè¿æ¥ï¼å¯¹äºä»»ä½å æå¿ èç¶æ (ð1,ð2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¦¨è®¾ ð1 â¤ð2a1â¤a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä»¤ ð =ð2 âð1k=a2âa1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð1 >âððâa1>âkÏâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å æç©å®¶å¯ä»¥ä»ä¸¤å ç³å­åå (ð1 ââððâ)(a1ââkÏâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼å°å±é¢åä¸ºå¿ è´¥ç¶æï¼åè¿æ¥ï¼ç±åä¸æ®µçç»è®ºï¼å¯¹äºè¿ä¸ª ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶å­å¨å¯ä¸ä¸ä¸ªå¿ è´¥ç¶æ (ð1,ðâ²2)(a1,a2â²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿èï¼å¦æ ð1 >ðâ²2a1>a2â²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶æ ðâ²2 <ð2a2â²<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼å¦æ ð1 <ðâ²2a1<a2â²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯ä»¥å ðâ² =ðâ²2 âð1kâ²=a2â²âa1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð1 =âðâ²ðâa1=âkâ²Ïâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ð1 <âððâa1<âkÏâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ è ðâ² <ðkâ²<k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ ðâ²2 =ð1 +ðâ² <ð1 +ð =ð2a2â²=a1+kâ²<a1+k=a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼åªè¦ ð1 <âððâa1<âkÏâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ä¸å®æ ðâ²2 <ð2a2â²<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æç©å®¶åªéè¦ä»ç¬¬äºå ç³å­ä¸­åèµ° (ð2 âðâ²2)(a2âa2â²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­å°±å¯ä»¥ä½¿å¾å±é¢åä¸ºå¿ è´¥ç¶æï¼

### ç¿»ç¡¬å¸æ¸¸æ

ç¿»ç¡¬å¸æ¸¸æä¹æ¯ä¸ç±»å¸¸è§çå ¬å¹³ç»åæ¸¸æï¼

ç¿»ç¡¬å¸æ¸¸æ

è®¾ (ð, âª¯)(S,âª¯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª [è¯åºååºé](../../order-theory/)ï¼æ å° ð :ð âPPðf:SâPPS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å¯¹äºææ ð  âðsâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåé½æ ð(ð )f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éç©ºï¼å¯¹äº ð âð(ð )Tâf(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ ð  âðsâT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸å¯¹äºææ ð¡ âðtâT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð¡ âª¯ð tâª¯s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ªå ç´ å¤é½æä¸æç¡¬å¸ï¼å¯è½æ­£é¢æä¸ä¹å¯è½èé¢æä¸ï¼ç©å®¶è½®æµè¡å¨ï¼éæ©ä¸ææ­£é¢æä¸çç¡¬å¸ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åéå ð âð(ð )Tâf(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶å°éå ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ææç¡¬å¸ç¿»è½¬ï¼å°ææç¡¬å¸é½ç¿»è½¬å°èé¢æä¸çç©å®¶è·èï¼

ç¿»ç¡¬å¸æ¸¸æå ¶å®æ¯ä¸å¤§ç±»æ¸¸æï¼åå³äºå ·ä½çååºé ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ©ï¼ç¿»ç¡¬å¸æ¸¸æçå ·ä½å½¢å¼ä¹ææä¸åï¼æ¸¸ææè¿°ä¸­ï¼æ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦æ»¡è¶³çæ¡ä»¶æ¯å¨è¯´ï¼æ¯æ¬¡ç©å®¶éæ©ç¿»è½¬ç¡¬å¸çéå ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼ä¸å®å­å¨ä¸ææ­£é¢æä¸çç¡¬å¸ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾éå ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ææå ç´ é½æå¨ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¢ï¼è¿ä¿è¯äºæ¸¸æå¯ä»¥å¨è¥å¹²æ­¥åç»æ­¢ï¼

ä¾å­

  1. è®¾ ð ={1,2,â¯,ð}S={1,2,â¯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð(ð ) ={{ð¡,ð } :ð¡ â¤ð }f(s)={{t,s}:tâ¤s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ç¸å½äºè¯´ï¼æä¸æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç¡¬å¸ï¼æ¯æ¬¡ç¿»è½¬ä¸ææ­£é¢æä¸çç¡¬å¸ï¼å¹¶ä¸å¯ä»¥éæ©ä¸æå®å·¦ä¾§çç¡¬å¸ç¿»è½¬ï¼
  2. è®¾ ð ={1,2,â¯,ð}S={1,2,â¯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð(ð ) ={[ð¡,ð ] :ð¡ â¤ð }f(s)={[t,s]:tâ¤s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ç¸å½äºè¯´ï¼æä¸æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç¡¬å¸ï¼æ¯æ¬¡ç¿»è½¬ä¸æ®µè¿ç»­çç¡¬å¸ï¼ä½æ¯å¿ é¡»ä¿è¯è¿äºç¡¬å¸ä¸­æå³ä¾§çé£æç¡¬å¸å¨ç¿»è½¬åæ¯æ­£é¢æä¸çï¼
  3. è®¾ ð ={1,2,â¯,ð}2S={1,2,â¯,n}2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð(ð ) ={{ð }}f(s)={{s}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ç¸å½äºè¯´ï¼æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç¡¬å¸ï¼æ¯æ¬¡åªè½ç¿»è½¬ä¸ææ­£é¢æä¸çç¡¬å¸ï¼
  4. è®¾ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸æ£µææ ¹æ çç»ç¹éåï¼ä¸ ð(ð )f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é¡¶ç¹ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°æ æ ¹çè·¯å¾ç»è¿çç»ç¹éåçå­éä¸­ï¼ææå å« ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èªèº«çå­éçéåï¼è¿ç¸å½äºè¯´ï¼æä¸æ£µææ ¹æ ï¼æ¯ä¸ªç»ç¹å¤æ¾ç½®ä¸æç¡¬å¸ï¼æ¯æ¬¡ç¿»è½¬ä¸ææ­£é¢æä¸çç¡¬å¸ï¼å¹¶ä¸å¯ä»¥éæ©å®çè¥å¹²ä¸ªç¥å ç»ç¹å¤çç¡¬å¸ç¿»è½¬ï¼

å°½ç®¡ç¿»ç¡¬å¸æ¸¸æç§ç±»ç¹å¤ï¼ä½æ¯å®ä»¬çæ±è§£æè·¯æ¯ä¸è´çï¼å¯¹äºç¿»ç¡¬å¸æ¸¸æ (ð,ð)(S,f)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ ðºð Gs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåªæå ç´ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çç¡¬å¸æ­£é¢æä¸çå±é¢ï¼è¿äºå±é¢ç§°ä¸ºåºç¡å±é¢ï¼é£ä¹ï¼ä»»æä¸ä¸ªå±é¢ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥çåæ¯è¿äºåºç¡å±é¢å¯¹åºçæ¸¸æçåï¼ä¹å°±æ¯è¯´ï¼ä»¥ä¸ç»è®ºæç«ï¼

å®ç

å¯¹äºç¿»ç¡¬å¸æ¸¸æ (ð,ð)(S,f)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå±é¢ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å ¶ä¸­æ­£é¢æä¸çç¡¬å¸æå¤ä½ç½®çéåä¸º ð»(ðº) âðH(G)âS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å±é¢ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç SG å½æ°å¼å°±æ¯

SGâ¡(ðº)=â¨ð âð»(ðº)SGâ¡(ðºð ).SGâ¡(G)=â¨sâH(G)SGâ¡(Gs).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

èèä¸ä¸ªç¸å ³çæ¸¸æï¼ä¸ä¸ªå±é¢ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼éå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ªå ç´ å¤é½æ¾ç½®æè¥å¹²æç³å­ï¼ç©å®¶æ¯æ¬¡è¡å¨æ¶ï¼é½å¯ä»¥åèµ° ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çä¸æç³å­ï¼å¹¶éåéå ð âð(ð )Tâf(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¨éå ð â{ð }Tâ{s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çåä¸ªå ç´ å¤åæ¾ç½®ä¸æç³å­ï¼å¯¹äºè¿ç±»æ¸¸æï¼ä»ç¶å¯ä»¥å®ä¹åºç¡å±é¢ ðºâ²ð Gsâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ä» å¨ä½ç½® ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤æ¾ç½®æä¸æç³å­çå±é¢ï¼è¿ç±»æ¸¸æä¸­ï¼æ¯ä¸ªå±é¢åä¸ºå ¶ææç³å­å¯¹åºåºç¡å±é¢çåï¼è¿æ¯å ä¸ºåªè¦æ¾ç½®æ°ç³å­æ¶å°å®å¯¹åºå°åèµ°çç³å­ä¸ï¼å°±å¯ä»¥å°æ¸¸æè¿ç¨ä¸­åºç°çæ¯æç³å­é½å¯¹åºå°åå§å±é¢ä¸­çåä¸ªç³å­ä¸ï¼è¿èå¯¹åºåå§å±é¢ä¸åç³å­çå­æ¸¸æè¿ç¨äºä¸å¹²æ°ï¼æ´ä¸ªæ¸¸æå°±å¯ä»¥çä½æ¯è¿äºå­æ¸¸æçåï¼ç±äºç¸åä½ç½®ç³å­å¯¹åºåºç¡å±é¢ç SG å¼æ¯ä¸æ ·çï¼æä»¥å©ç¨å¼æå¼çç¹æ§å¯ç¥ï¼å±é¢ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç SG å¼ä» ç±åå ç³å­æ°éçå¥å¶æ§å³å®ï¼èä¸å ·ä½æ°éæ å ³ï¼å æ­¤ï¼å¯¹äºæ¸¸æå±é¢ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æè®°å ¶ç³å­æ°éä¸ºå¥æ°çä½ç½®éåä¸º ð»(ðºâ²)H(Gâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ¬æ®µçåæå¯ä»¥æ»ç»ä¸ºå ¬å¼ï¼

SGâ¡(ðºâ²)=â¨ð âð»(ðºâ²)SGâ¡(ðºâ²ð ).SGâ¡(Gâ²)=â¨sâH(Gâ²)SGâ¡(Gsâ²).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ­¤ï¼ä¸æåªéè¦å»ºç«æ¸¸æ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¸¸æ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç­ä»·æ§å°±å¯ä»¥è¯æå®çä¸­çå ¬å¼ï¼

éè¦è¯´æçæ¯ï¼å¯¹äºæ°æ¸¸æçå±é¢ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç¿»ç¡¬å¸æ¸¸æçå±é¢ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç³å­æ°éä¸ºå¥æ°çä½ç½®ä¸ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç¡¬å¸æ­£é¢æä¸çä½ç½®å¤ç¸åï¼å°±æ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­ä»·ï¼æ ¹æ® SpragueâGrundy å®ççå¼ç 2ï¼è¿ç­ä»·äºè¯æå±é¢ ðº +ðºâ²G+Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥ç¶æï¼åæç©å®¶çèå©ç­ç¥å¾ç®åï¼å¦æå æç©å®¶éæ©åèµ° ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çç³å­ä¸è¯¥å¤ä¸æ­¢ä¸æç³å­ï¼é£ä¹åæç©å®¶ç´æ¥æ¨¡ä»¿å æç©å®¶çè¡ä¸ºï¼å¦åï¼åæç©å®¶éæ©åå æç©å®¶åæ ·ç ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âð(ð )Tâf(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯éæ©åå æç©å®¶ä¸åçå­æ¸¸æï¼å³å æåç³å­åæå°±åç¡¬å¸ï¼å æåç¡¬å¸åæå°±ç¿»ç³å­ï¼ç±äºå æç©å®¶æ è®ºä»»ä½æä½ï¼åæç©å®¶å°±å¯ä»¥ç»§ç»­æä½ï¼å¹¶ä¿è¯æ®ä½å±é¢ä¸­ç³å­æ°éä¸ºå¥æ°çä½ç½®ä¸ç¡¬å¸æ­£é¢æä¸çä½ç½®ç¸åï¼è¿æ ·ï¼æ¸¸æå¿ ç¶ç»æå¨å æç©å®¶æ²¡æåæ³æä½æ¶ï¼å æ­¤ï¼å æå¿ è´¥ï¼å®çç±æ­¤å¾è¯ï¼

å©ç¨è¿ä¸ç»è®ºï¼å¤æ­æä¸å±é¢æ¯å¦å¿ èï¼åªéè¦è®¡ç®å ¶ä¸­æææ­£é¢æä¸çç¡¬å¸å¯¹åºçåºç¡å±é¢ç SG å½æ°å¼ï¼åæ± Nim åå³å¯ï¼è¿äºåºç¡å±é¢ç SG å½æ°å¼ä¹ä¸é¾è®¡ç®ï¼å ä¸ºå®ä»¬çåç»§å±é¢å·²ç»ç±æ å° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»åºï¼ä¸åç»§å±é¢ç SG å¼å¯ä»¥å½çº³å°è®¡ç®ï¼

SGâ¡(ðºð )=mexðâð(ð )â¡â¨ð¡âðâ{ð }SGâ¡(ðºð¡).SGâ¡(Gs)=mexTâf(s)â¡â¨tâTâ{s}SGâ¡(Gt).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ç¸å½äºæä¾äºä¸ä¸ªåºç¡å±é¢ SG å½æ°å¼çéæ¨å ¬å¼ï¼

### äºåå¾åå¼

åç½®ç¥è¯ï¼[äºåå¾æå¤§å¹é ](../../../graph/graph-matching/bigraph-match/)

æ¬èçæåï¼è®¨è®ºäºåå¾åå¼ï¼å°½ç®¡è¿ä¸ªæ¸¸æå¸¸ç§°ä½äºåå¾åå¼ï¼ä½æ¯å®çæè¿°åç»è®ºçè¯æé½ä¸äºåå¾çç»ææ å ³ï¼æä»¥ï¼å®çç»è®ºå®é ä¸å¯¹äºä¸è¬çæ åå¾é½æç«ï¼ä½æ¯ï¼ä¸è¬å¾çæå¤§å¹é è¾ä¸ºå¤æï¼æä»¥è¿ä¸ç»è®ºå¸¸åºç°å¨äºåå¾çé¢ç®ä¸­ï¼

äºåå¾åå¼

ä¸¤ä¸ªç©å®¶è½®æµè¡å¨ï¼æ¯ä¸ªç©å®¶é¢ä¸´çå±é¢é½ç±ä¸ä¸ªæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå®çä¸ä¸ªé¡¶ç¹ ð£ âðvâV![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææï¼å¨ä¸åç©å®¶çååä¸­ï¼è¥å½åå±é¢ä¸º (ðº,ð£)(G,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¯¥ç©å®¶å¿ é¡»éæ©ä¸ä¸ªä¸ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸é»çé¡¶ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éåï¼å°é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ææå ³èè¾¹ä»å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å é¤ï¼å¾å°æ®ä½å¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ°çå±é¢å³ä¸º (ðºâ²,ð¢)(Gâ²,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¤ç±ä¸ä¸ä½ç©å®¶ï¼è¥æä½ç©å®¶å¨å ¶ååå¼å§æ¶ï¼å½åé¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨å¾ä¸­æ²¡æç¸é»é¡¶ç¹ï¼å³ä¸å­å¨åæ³éæ©ï¼ï¼åè¯¥ç©å®¶æ æ³è¡å¨ï¼å¹¶å æ­¤è¾ææ¸¸æï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

æ¸¸æå æå¿ èï¼å½ä¸ä» å½é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§å¹é å ³é®ç¹ï¼ä¹å°±æ¯è¯´ï¼å¨å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæææå¤§å¹é ä¸­ï¼é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯å¹é ç¹ï¼

è¯æ

é¦å ï¼é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§å¹é å ³é®ç¹ï¼è®¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªæå¤§å¹é ä¸º ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼å æå¯ä»¥å°å±é¢ç§»å¨å°å¨ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹é çé¡¶ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºé¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºç°å¨ææå¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§å¹é ä¸­ï¼æä»¥ï¼æ®ä½å¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§å¹é çå¤§å°è³å¤æ¯ |ð| â1|M|â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸å° ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å»æè¾¹ (ð£,ð£)(v,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±è½å¾å°å¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå¤§å°ä¸º |ð| â1|M|â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹é  ðâ²Mâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç»åè¿ä¸¤ç¹å°±ç¥éï¼ðâ²Mâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªæå¤§å¹é ï¼ä½æ¯ï¼åæç©å®¶æå¤çå±é¢ä¸­ï¼é¡¶ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸æ¯å¹é  ðâ²Mâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå¹é ç¹ï¼å æ­¤ï¼åæç©å®¶å¿ ç¶å¤äºä¸ä¸ªå¿ è´¥ç¶æï¼

åè¿æ¥ï¼åè®¾å­å¨æå¤§å¹é  ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æªå¹é ç¹ï¼ç±äº ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æå¤§å¹é ï¼ä¸é¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸é»çé¡¶ç¹ä¸å®æ¯å¹é ç¹ï¼å¦åï¼å°±å¯ä»¥å°å®ä»¬ä¹é´çè¿è¾¹æ·»å å° ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼å¾å°ä¸ä¸ªæ´å¤§çå¹é ï¼å æ­¤ï¼æ è®ºå ææä¹éæ©ï¼åæé½å¤äºä¸ä¸ªå¿ èç¶æï¼

æ±åºäºåå¾æå¤§å¹é å ³é®ç¹çç®æ³è¯¦è§ [äºåå¾æå¤§å¹é é¡µé¢](../../../graph/graph-matching/bigraph-match/#æå¤§å¹é)ï¼

å¦å¤ï¼äºåå¾åå¼è¿æä¸ä¸ªåä½ï¼

äºåå¾åå¼çåä½

è®¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªæ åå¾ï¼ä¸å¾çæ¯ä¸ªé¡¶ç¹ä¸é½æ¾ç½®äºä¸æç³å­ï¼ä¸¤åç©å®¶è½®æµè¡å¨åèµ°ç³å­ï¼æ¸¸æå¼å§æ¶ï¼å æç©å®¶å¯ä»¥åèµ°ä»»ä½ä¸æç³å­ï¼åç»­çååä¸­ï¼æ¯åç©å®¶åèµ°ç³å­çé¡¶ç¹å¿ é¡»ä¸ä¸ä¸ååä¸­å¯¹æ¹åèµ°ç³å­çé¡¶ç¹ç¸é»ï¼æå æ æ³åèµ°ç³å­çç©å®¶è¾ææ¸¸æï¼

æ¾ç¶ï¼è¿ä¸ªåä½ç¸å½äºå¨åææè¿°äºåå¾åå¼ä¸­ï¼è®©å æç©å®¶éæ©åå§å±é¢ï¼ç¶åä»åæç©å®¶å¼å§äºåå¾åå¼ï¼å æ­¤ï¼è¿ä¸ªåä½ä¸­ï¼å æç©å®¶å¿ è´¥ï¼å½ä¸ä» å½æ¯ä¸ªé¡¶ç¹é½æ¯æå¤§å¹é å ³é®ç¹ï¼äº¦å³å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ [å®ç¾å¹é ](../../../graph/graph-matching/graph-match/#å®ä¹)ï¼

## åå¸¸ Nim æ¸¸æ

æ¬èè®¨è®ºåå¸¸ Nim æ¸¸æçæ±è§£ï¼

Nim æ¸¸æ

å ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­ï¼ä¸¤åç©å®¶è½®æµåèµ°ä»»æä¸å ä¸­çä»»æå¤æç³å­ï¼ä½ä¸è½ä¸åï¼åèµ°æåä¸æç³å­çç©å®¶å¤±è´¥ï¼

å¯¹æ­¤ï¼æå¦ä¸ç»è®ºï¼

å®ç

åå¸¸ Nim æ¸¸æä¸­ï¼ç¶æ (ð1,ð2,â¯,ðð)(a1,a2,â¯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¿ è´¥ç¶æ PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ä¸ä» å½

  1. å­å¨ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð >1ai>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ Nim å ð1 âð2 ââ¯ âðð =0a1âa2ââ¯âan=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æè 
  2. å¯¹äºææ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ ðð â¤1aiâ¤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å©ä½çéç©ºç³å­å æ°æ¯å¥æ°ï¼

è¯æ

ç±äºæ æ³æä½æ¯å æå¿ èæ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å¯ä»¥å½çº³å°è¯æï¼å¦ææ¯å ç³å­é½åªæä¸æï¼é£ä¹ç³å­å æ°æ¯å¥æ°å°±å¯¹åºçå æå¿ è´¥æ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç³å­å æ°æ¯å¶æ°å°±å¯¹åºçå æå¿ èæ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¥ä¸æ¥ï¼èå¯æäºå ç³å­çæ°éä¸¥æ ¼å¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼

æ å½¢ Aï¼å¦æåªæä¸å ç³å­çæ°éä¸¥æ ¼å¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ­¤æ¶ Nim åä¸å®ä¸ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ï¼ç±äºå æç©å®¶å¯ä»¥éæ©è½¬ç§»å°å ¨é¨å çç³å­æ°éåä¸è¶ è¿ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå±é¢ï¼èä¸å¯ä»¥æ§å¶å©ä½çéç©ºç³å­å çå¥å¶æ§ï¼å æ­¤ï¼æ­¤æ¶ä¸ºå æå¿ èæ NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ å½¢ Bï¼ç°å¨ï¼æä¸æ­¢ä¸å ç³å­çæ°éä¸¥æ ¼å¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ è®ºæä¹æä½ï¼ä¸ä¸ä¸ªå±é¢ä¸­ï¼é½è³å°æä¸å ç³å­çæ°éä¸¥æ ¼å¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å½çº³åè®¾ï¼ä¸ä¸å±é¢ä¸­ï¼å æå¿ è´¥å¯¹åºç Nim åä¸ºé¶ï¼å æå¿ èå¯¹åºç Nim åä¸ä¸ºé¶ï¼è¿ä¸æ­£å¸¸ Nim æ¸¸æçå½çº³åè®¾å®å ¨ç¸åï¼å æ­¤ï¼éå¤ Nim æ¸¸æçè®ºè¯ï¼å°±è½ç¥éï¼å½åå±é¢åæ ·ç¬¦å Nim åä¸ºé¶å¯¹åºå æå¿ è´¥ç¶æçç»è®ºï¼

## æåå¾æ¸¸æ

æ¬æè®¨è®ºçå ¬å¹³ç»åæ¸¸æï¼è¦æ±åä¸å±é¢ä¸è½åºç°ä¸¤æ¬¡ï¼ä¹ä¸å­å¨å¹³å±çå¯è½æ§ï¼å æ­¤ï¼å¯¹åºçåå¼å¾æ»æ¯æåæ ç¯å¾ï¼æ¬èæ¾å®½äºè¿ä¸éå¶ï¼è®¨è®ºå¦ä½å¨ä¸è¬çæåå¾ä¸å¤å®åä¸ªç¶ææ¯å æå¿ èãå æå¿ è´¥æå¹³å±ï¼

æåå¾æ¸¸æçè§ååå ¶ä»çå ¬å¹³ç»åæ¸¸æå¤§ä½ä¸è´ï¼ä»èµ·å§ç¶æåºåï¼è½®æµæ²¿çæåå¾çè¾¹ç§»å¨ä¸æ­¥ï¼ç´å°æ è·¯å¯èµ°ï¼æ ¹æ®æ¸¸ææ¯æ­£å¸¸è§åè¿æ¯åå¸¸è§åï¼æåä¸ä¸ªä¸è½ç§»å¨çç©å®¶åå«æ¯è´¥è åèè ï¼å¨è¿æ ·çæ¸¸æéï¼æ¯ä¸ªç¶æçèè´æ åµå ±æä¸ç§å¯è½æ§ï¼å æå¿ èãå æå¿ è´¥ãå¹³å±ï¼å¹³å±ä¸­æ¸¸ææ°¸è¿ä¸ä¼ç»æ­¢ï¼å°½ç®¡ç¨å¾®å¤æä¸äºï¼ä½æ¯å ³äºå¿ è´¥ç¶æåå¿ èç¶æç å¼ç ä¾ç¶æç«ï¼èå©ä¸çç¶æå°±æ¯å¹³å±ç¶æï¼

  * ä¸ä¸ªç¶ææåç»§ç¶æå æå¿ èï¼å½ä¸ä» å½åç»§ç¶æä¹ä¸æ¯å¿ è´¥ç¶æï¼
  * å¦æä¸ä¸ªç¶ææåç»§ç¶æï¼é£ä¹å®å æå¿ è´¥ï¼å½ä¸ä» å½ææåç»§ç¶æé½æ¯å¿ èç¶æï¼
  * å¦æä¸ä¸ªç¶ææ æ³åç±»ä¸ºå¿ èç¶æåå¿ è´¥ç¶æï¼é£ä¹å®å°±æ¯å¹³å±ç¶æï¼

è¦å°ææç¶æåç±»ä¸ºè¿ä¸ç§ç¶æï¼åªéè¦éç¨ç±»ä¼¼ [æææåº](../../../graph/topo/) çæè·¯ï¼

  1. åå§åæ¶ï¼è®°å½ææç¶æçåºåº¦ï¼å°ææåºåº¦ä¸ºé¶çç¶æåå ¥éåï¼å¹¶æ ¹æ®æ¸¸ææ¯æ­£å¸¸è§åææ¯åå¸¸è§ååå«è®¾ä¸ºå¿ è´¥ç¶ææå¿ èç¶æï¼
  2. å¼¹åºéé¦ç¶æï¼å¦ææ¯å¿ è´¥ç¶æï¼åè®¾åé©±ç¶æä¸ºå¿ èç¶æï¼å¦åï¼å½åç¶ææ¯å¿ èç¶æï¼å°å®çææåé©±ç¶æçåºåº¦åä¸ï¼å¹¶å°åºåº¦ä¸ºé¶çåé©±ç¶æè®¾ä¸ºå¿ è´¥ç¶æï¼å°å¯ä»¥å¤æ­æ¯å¿ èæå¿ è´¥ç¶æçåé©±ç¶æåå ¥éåï¼
  3. ç®æ³å¨éåä¸ºç©ºæ¶ç»æ­¢ï¼å°æªå¤æ­ä¸ºå¿ èæå¿ è´¥ç¶æçç¶æåä¸ºå¹³å±ç¶æï¼

è¿ä¸ç®æ³å¯ä»¥å¨ ð(|ð| +|ð¸|)O(|V|+|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å å°ææç¶æåç±»ï¼

## ä¾é¢

æ¬èè®¨è®ºä¸äºå ¸åçä¾é¢ï¼

[Luogu P2148 [SDOI2009] E&D](https://www.luogu.com.cn/problem/P2148)

æ 2ð2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼å¯¹äº ð =1,2,â¯,ðk=1,2,â¯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç³å­å  2ð â12kâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 2ð2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ºä¸ç»ï¼ä¸¤åç©å®¶è½®æµæä½ï¼æ¯æ¬¡éæ©ä¸ç»ç³å­å ï¼å°å ¶ä¸­ä¸å ç§»èµ°ï¼å¹¶å°å¦ä¸å åä¸ºéç©ºçä¸¤å ï¼æ¾å°è¯¥ç»ç³å­å æå¨çä¸¤ä¸ªä½ç½®ï¼å¦æææç³å­å é½åªæä¸æç³å­ï¼å½åç©å®¶å°±æ²¡æåæ³æä½ï¼è¾ææ¸¸æï¼ç»å®æ¯å ç³å­çæ°é {ðð}2ðð=1{ai}i=12n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é®æ¯å¦ä¸ºå æå¿ èç¶æï¼

è§£ç­

æ¾ç¶ï¼ä¸åç»ç³å­å çæ¸¸æç¸äºç¬ç«ï¼æä»¥ï¼åªè¦è®¡ç®æ¯ç»æ¸¸æç SG å½æ°å¼ï¼å°±è½è®¡ç®åºæ´ä¸ªæ¸¸æç SG å¼ï¼è¿èå¤æ­æ¯å¦ä¸ºå¿ èç¶æï¼å ³é®å¨äºå¦ä½è®¡ç®æ¯ç»ç³å­å ç SG å½æ°å¼ï¼è¿å¹¶ä¸å®¹æï¼è§£å³è¿ç±»åå¼è®ºé®é¢çå¸¸è§æè·¯æ¯æè¡¨ï¼è®¾ä¸ç»ç³å­å ä¸­ç³å­æ°éåå«ä¸º (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼SG å¼ä¸º ð(ð,ð)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åä¸ä¸ªæ´åæè¡¨çç¨åºï¼å°±å¾å°å¦ä¸ç»æï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 1 1 2 2 1 1 3 3 1 1 2 2 1 1 4 4 0 2 0 2 0 3 0 3 0 2 0 2 0 4 0 4 2 2 2 2 3 3 3 3 2 2 2 2 4 4 4 4 0 1 0 3 0 1 0 3 0 1 0 4 0 1 0 4 1 1 3 3 1 1 3 3 1 1 4 4 1 1 4 4 0 3 0 3 0 3 0 3 0 4 0 4 0 4 0 4 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 4 1 1 2 2 1 1 4 4 1 1 2 2 1 1 4 4 0 2 0 2 0 4 0 4 0 2 0 2 0 4 0 4 2 2 2 2 4 4 4 4 2 2 2 2 4 4 4 4 0 1 0 4 0 1 0 4 0 1 0 4 0 1 0 4 1 1 4 4 1 1 4 4 1 1 4 4 1 1 4 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 ```   
---|---  
  
è¿ä¸ªè¡¨å¾å ·æè§å¾æ§ï¼æä¸ä¸ªç®åçè§å¯ï¼è¡¨æ ¼åæè¥å¹²ä¸ª 2 Ã22Ã2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼ä¸å·¦ä¸è§å¤æ»æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå ¶ä½ä¸ä¸ªå¼æ»æ¯ä¸æ ·çï¼äºæ¯ï¼ä¸å¦¨å°è¿ä¸ªè¡¨æ ¼åç¼©ï¼å°æ¯ä¸ª 2 Ã22Ã2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµé½åç¼©ä¸ºé¤äºå·¦ä¸è§ä¹å¤é£ä¸ªå ±åçæ°å¼ï¼

```text 1 2 3 4 5 6 7 8 ``` |  ```text 1 2 1 3 1 2 1 4 2 2 3 3 2 2 4 4 1 3 1 3 1 4 1 4 3 3 3 3 4 4 4 4 1 2 1 4 1 2 1 4 2 2 4 4 2 2 4 4 1 4 1 4 1 4 1 4 4 4 4 4 4 4 4 4 ```   
---|---  
  
å¯ä»¥åç°ï¼è¿ä¸ªåç¼©çè¡¨æ ¼æ¯åé¢å®æ´è¡¨æ ¼ç¸åä½ç½®çå¼å ä¸ï¼å ¶å®é®é¢å·²ç»è§£å³äºï¼è®¾ä¸æ ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼é£ä¹è¡¨æ ¼ä¸­ (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çå¼ ð(ð,ð)g(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥ç±å¦ä¸éæ¨å ¬å¼ç»åºï¼

ð(ð,ð)={0,ifÂ 2â£ðÂ andÂ 2â£ð,ð(âð/2â,âð/2â)+1,otherwise.g(i,j)={0,ifÂ 2â£iÂ andÂ 2â£j,g(âi/2â,âj/2â)+1,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦æ±ç SG å½æ° ð(ð,ð) =ð(ð â1,ð â1)f(i,j)=g(iâ1,jâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨è¿ä¸éæ¨å ¬å¼ï¼ç®æ³å¯ä»¥å¨ ð(logâ¡min{ð,ð})O(logâ¡min{i,j})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±åº ð(ð,ð)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼

å½ç¶ï¼å¯ä»¥éè¿ç®åçå½çº³æ³å¾å° ð(ð,ð)g(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ¶å®å°±æ¯å° ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¤åæ¶é¤ä»¥ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°ä¸¤ä¸ªå¶æ°çæå°æ¬¡æ°ï¼æ¢å¥è¯è¯´ï¼å®å°±æ¯ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½æä¸­æ«å°¾ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼ç±æ­¤ï¼ä¹å¯ä»¥ç´æ¥å©ç¨ `__builtin_ctz(~(i | j))` ç®åºè¯¥å¼ï¼

è¿ç±»é¢ç®ä¸­ï¼åªè¦éè¿æè¡¨è§å¯çæ¹æ³å¾å° SG å½æ°è¡¨è¾¾å¼ï¼å®é½å¾å®¹æéè¿å½çº³æ³è¯æï¼å èè§£é¢çå ³é®å¨äºä»¥æç§å½¢å¼è·å¾è¿äºç»è®ºèéæ¨å¯¼ï¼ä¾å¦ï¼å·²ç¥ç»è®ºåï¼æ¬é¢ä¸­çéæ¨å ³ç³»å¯ä»¥å½çº³è¯æå¦ä¸ï¼è®¾ ððSk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç³å­åæéç©ºçä¸¤å è½å¾å°çå±é¢ç SG å¼éåï¼é£ä¹ï¼ð(ð,ð) =mexâ¡(ðð âªðð)f(i,j)=mexâ¡(SiâªSj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èï¼ððSk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æéæ¨å ³ç³»ï¼

ðð={mexâ¡(ððâªðð):ð+ð=ð,Â ð,ðâð+}.Sk={mexâ¡(SiâªSj):i+j=k,Â i,jâN+}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éè¦è¯æçæ¯ï¼ð âððdâSk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½ä¸ä» å½ (ð â1)(kâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºä¸­ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼æä½ä½æ¯ç¬¬ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å©ç¨æ°å­¦å½çº³æ³ï¼å½çº³èµ·ç¹ ð1 =â S1=â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¾ç¶æç«ï¼åè®¾å½é¢å¯¹å°äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ´æ°é½æç«ï¼é£ä¹ï¼ð âððdâSk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ä¸ä» å½å­å¨ ð,ð âð+i,jâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð +ð =ði+j=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ (ð â1)(iâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð â1)(jâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸ªæ°çç¬¬ ðâ² <ðdâ²<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½è³å°æä¸ä¸ªä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶ï¼å­å¨è¿æ ·ä¸ç§æåï¼å½ä¸ä» å½åªèèç¬¬ 0 â¼ð0â¼d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çé¨åï¼å³æ¨¡ 2ð+12d+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼(ð â1) =(ð â1) +(ð â1) +1(kâ1)=(iâ1)+(jâ1)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼èå´ä¸º [2ð,2ð+1 â1)[2d,2d+1â1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼è¿ä¸æ¡ä»¶å°±ç­ä»·äº (ð â1)(kâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼å½çº³æ­¥éª¤æç«ï¼åå½é¢å¾è¯ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text #include <iostream> #include <vector> int g ( int i , int j ) { return i % 2 == 0 && j % 2 == 0 ? 0 : g ( i / 2 , j / 2 ) \+ 1 ; } int f ( int i , int j ) { return g ( i \- 1 , j \- 1 ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n ; int v = 0 ; for ( int i = 0 ; i < n / 2 ; ++ i ) { int x , y ; std :: cin >> x >> y ; v ^= f ( x , y ); } std :: cout << ( v ? "YES" : "NO" ) << '\n' ; } return 0 ; } ```   
---|---  
  
[Luogu P5675 [GZOI2017] åç³å­æ¸¸æ](https://www.luogu.com.cn/problem/P5675)

æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼ä¸¤äººç© Nim æ¸¸æï¼ç°å¨ï¼å¯ä»¥ä»»ææå®è¥å¹²å ç³å­ä½ä¸ºåå§å±é¢ï¼å¹¶æå®å ¶ä¸­ä¸å ç³å­è¦æ±å æç©å®¶é¦è½®å¿ é¡»ä»ä¸­åèµ°ç³å­ï¼ä½ä¸è½æå®åèµ°ç³å­çæ°ç®ï¼é®æå¤å°ç§æå®æ¹å¼ï¼ä½¿å¾å ææ æ³è·å¾èå©ï¼æ°æ®æ»¡è¶³ ð,ðð â¤200n,aiâ¤200![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

å¯¹äºè¿ç±»é®é¢ï¼éè¦å©ç¨å¸¸è§æ¸¸æçç»è®ºï¼å¹¶ç»åå ¶ä»é¨åç¥è¯æ¥è¿è¡è§£ç­ï¼åè®¾æå®å æå¿ é¡»åèµ°ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ä¸æå®çææç³å­å æ°é Nim åä¸º ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å ææ æ³è·å¾èå©ï¼å½ä¸ä» å½ ðð â¤ðð âð£aiâ¤aiâv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­æ°é ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è¶ è¿é¤ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å¤å©ä½ç³å­å æ°é Nim å ðð âð£aiâv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºæ°æ®èå´å¾å°ï¼ç´æ¥æä¸¾æå®é¦è½®åç³å­çå ï¼æä¸¾å°ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ¶ï¼å©ä½æ¯ä¸ªå éæä¸éï¼å¯ä»¥å¾å°ä¸å Nim åçæ¹æ¡æ°å¯ä»¥éè¿ DP è®¡ç®åºæ¥ï¼å°æåå¾å°çæ¹æ¡æ°ä¸­å¤§äºç­äº ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¨åå æ»èµ·æ¥å³å¯ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text #include <array> #include <iostream> #include <vector> int main () { constexpr int M = 1e9 \+ 7 ; constexpr int L = 256 ; int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( auto & x : a ) std :: cin >> x ; int res = 0 ; for ( int i = 0 ; i < n ; ++ i ) { std :: array < int , L > dp = {}; dp [ 0 ] = 1 ; for ( int j = 0 ; j < n ; ++ j ) { if ( j == i ) continue ; std :: array < int , L > _dp = {}; for ( int v = 0 ; v < L ; ++ v ) { _dp [ v ] = ( dp [ v ] \+ dp [ v ^ a [ j ]]) % M ; } dp = std :: move ( _dp ); } for ( int v = a [ i ]; v < L ; ++ v ) { res = ( res \+ dp [ v ]) % M ; } } std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
[Luogu P2599 [ZJOI2009] åç³å­æ¸¸æ](https://www.luogu.com.cn/problem/P2599)

æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼ä¸¤äººè½®æµåèµ°ç³å­ï¼æ¯æ¬¡é½åªè½ä»æå·¦ææå³çä¸¤å ä¸­éæ©ä¸å åèµ°ä»»ææç³å­ï¼ä½ä¸è½ä¸åï¼åèµ°æåä¸æç³å­çç©å®¶èå©ï¼é®å ææ¯å¦å¿ èï¼

è§£ç­

ç±äºæ¬é¢ä¸­å¹¶ä¸å­å¨ç¸äºç¬ç«çå­æ¸¸æï¼ææè¿éé¢ç®ååä¸åªç¨å° å¤æ­å¿ è´¥åå¿ èç¶æçå¼çï¼ä»æç®åçæ å½¢å¼å§åæï¼å½ ð â¤2nâ¤2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å°±æ¯ Nim æ¸¸æï¼å½ ð â¥3nâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼é®é¢åå¾å¤æï¼ä½æ¯ï¼ç±äºå¯æä½çç³å­å åªè½æ¯ä¸¤ç«¯çç³å­å ï¼ä¸å¦¨è®¾å®ä»¬ä¸­ç³å­æ°éåå«ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ­¥å°ï¼è®¾ ð(ð¥,ð¦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå æå¿ èç¶æçæç¤ºå½æ°ï¼å³å æå¿ èæ¶ ð(ð¥,ð¦) =1f(x,y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦å ð(ð¥,ð¦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®¹æåç°ï¼ð(ð¥,ð¦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼æ»¡è¶³éæ¨å ³ç³»ï¼ð(ð¥,ð¦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ä¸ä» å½å¯¹äºææ ð  <ð¥s<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¡ <ð¦t<y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ ð(ð¥,ð¡) =ð(ð ,ð¦) =1f(x,t)=f(s,y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éæ¨èµ·ç¹å¨ ð¥ =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð¦ =0y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ­¤æ¶ï¼æ¸¸æå·²ç»ä¸è¶³ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼éè¦è¿ä¸æ­¥èèä¸­é´ç³å­å çæ°éï¼å æ­¤ï¼ä¸å¦¨ææ¶åè®¾ ð(ð¥,0)f(x,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð(0,ð¦)f(0,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å·²ç¥çï¼èèå¦ä½ä»å®ä»¬çåå¼æ¨åºææ ð(ð¥,ð¦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼è¿å¹¶ä¸å°é¾ï¼èèä¸æ éåä¸º ð ÃðNÃN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ ç©·å¤§ç©éµï¼æ± ð(ð¥,ð¦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸å½äºåéé¢å¡« 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éè¦æ»¡è¶³çæ¡ä»¶æ¯ï¼æ¯è¡åæ¯åé½è³å¤ä¸ä¸ª 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¦æåè¡æååä¸­ä¹åçä½ç½®é½æ²¡æåºç°è¿ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥ä½ç½®ä¸å®æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯è¡ä¸­ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½ç½®å®é ä¸å®ä¹äºä¸ä¸ªä»è¡å· ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°åå· ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½æ°ï¼ç®åå°è¯å ä¸ªä¾å­ï¼å³æè¡¨ï¼ä¹åå°±å¯ä»¥åç°ï¼å¦æè®¾ä½¿å¾ ð(ð¥,0) =0f(x,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯ä¸ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð(0,ð¦) =0f(0,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯ä¸ç ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯¹äºä»»ä½ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð(ð¥,ð¦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ç

ð¦=â§{ { {â¨{ { {â©0,ð¥=ð¥0,ð¥â1,ð¥0<ð¥<ð¦0,ð¥+1,ð¦0<ð¥<ð¥0,ð¥,otherwise.y={0,x=x0,xâ1,x0<x<y0,x+1,y0<x<x0,x,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼åªè¦ç¥é ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å¨ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®åºä»»æ ð(ð¥,ð¦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å¤æ­å½åç¶ææ¯å¦ä¸ºå æå¿ èç¶æï¼è ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥éå½è®¡ç®ï¼ä¾å¦ï¼ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä½¿å¾ ð(ð¥,0) =0f(x,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯ä¸è§£ï¼ä½åæ¶ï¼ð(ð¥,0)f(x,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼å¯ä»¥éè¿ç§»é¤æå³ä¾§ç³å­å åï¼åªèèå©ä¸ç ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­æ¥è®¡ç®ï¼ä¹å°±æ¯è¯´ï¼åªèèå ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç³å­ï¼åæ ·å¯ä»¥è®¡ç®ä¸ä¸ª ð1,ðâ1(ð¥,ð¦)f1,nâ1(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ¾ç¶æ ð(ð¥,0) =ð1,ðâ1(ð¥,ððâ1)f(x,0)=f1,nâ1(x,anâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±»ä¼¼å°ï¼ç§»é¤æå·¦ä¾§ç³å­å å¹¶è®¡ç®å¾åº ð2,ð(ð¥,ð¦)f2,n(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼å°±å¾å° ð(0,ð¦) =ð2,ð(ð1,ð¦)f(0,y)=f2,n(a1,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ç¶ï¼å å±çå½æ° ð1,ðâ1(ð¥,ð¦)f1,nâ1(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2,ð(ð¥,ð¦)f2,n(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡ç®ä¾èµäºæ´å å±çå½æ°ï¼è¿æ¯å ¸åç [åºé´ DP](../../../dp/interval/)ï¼æ¯å±åªéè¦ç»´æ¤ç¸åºå½æ°ç ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text #include <array> #include <iostream> #include <vector> int main () { // Transition helper as explained above. auto calc = []( int x0 , int y0 , int x ) -> int { return x == x0 ? 0 : (( x < x0 && x < y0 ) || ( x > x0 && x > y0 ) ? x : ( x0 < y0 ? x \- 1 : x \+ 1 )); }; int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( auto & x : a ) std :: cin >> x ; // dp[i][j][0] = the unique value x such that // f_{i-1,j}(x, a_j) = 0 // i.e. the interval game [i, j] is in a P-position // when a pile of size x is attached to the LEFT. // // dp[i][j][1] = the unique value y such that // f_{i,j+1}(a_i, y) = 0 // i.e. the interval game [i, j] is in a P-position // when a pile of size y is attached to the RIGHT. std :: vector < std :: vector < std :: array < int , 2 >>> dp ( n , std :: vector < std :: array < int , 2 >> ( n )); // Base case: single-element interval [i, i]. // The "left" and "right" pile values both equal a[i]. for ( int i = 0 ; i < n ; ++ i ) dp [ i ][ i ][ 0 ] = dp [ i ][ i ][ 1 ] = a [ i ]; // Build up intervals of increasing length d. for ( int d = 1 ; d < n ; ++ d ) { for ( int i = 0 ; i \+ d < n ; ++ i ) { dp [ i ][ i \+ d ][ 0 ] = calc ( dp [ i ][ i \+ d \- 1 ][ 1 ], dp [ i ][ i \+ d \- 1 ][ 0 ], a [ i \+ d ]); dp [ i ][ i \+ d ][ 1 ] = calc ( dp [ i \+ 1 ][ i \+ d ][ 0 ], dp [ i \+ 1 ][ i \+ d ][ 1 ], a [ i ]); } } // The original game corresponds to attaching nothing on the left. // It is a P-position if and only if the unique value y satisfying // f_{-1, n-1}(0, y) = 0 // is y = 0. std :: cout << ( dp [ 0 ][ n \- 1 ][ 0 ] != 0 ) << '\n' ; } return 0 ; } ```   
---|---  
  
## ä¹ é¢

é¦å æ¯ä¸äºæ¨¡æ¿é¢ï¼å®ä»¬æ¯å¯¹æ¬é¡µé¢çç»è®ºçç®ååºç¨ï¼

  * [Luogu P2197ãæ¨¡æ¿ãNim æ¸¸æ](https://www.luogu.com.cn/problem/P2197)
  * [Luogu P2252 [SHOI2002] åç³å­æ¸¸æ](https://www.luogu.com.cn/problem/P2252)
  * [Luogu P2594 [ZJOI2009] æè²æ¸¸æ](https://www.luogu.com.cn/problem/P2594)
  * [Luogu P3185 [HNOI2007] åè£æ¸¸æ](https://www.luogu.com.cn/problem/P3185)
  * [Luogu P3480 [POI 2009] KAM-Pebbles](https://www.luogu.com.cn/problem/P3480)
  * [Luogu P4101 [HEOI2014] äººäººå°½è¯´æ±åå¥½](https://www.luogu.com.cn/problem/P4101)
  * [Luogu P4279 [SHOI2008] å°çº¦ç¿°çæ¸¸æ](https://www.luogu.com.cn/problem/P4279)
  * [Luogu P6487 [COCI 2010/2011 #4] HRPA](https://www.luogu.com.cn/problem/P6487)
  * [Luogu P6560 [SBCOI2020] æ¶å çæµé](https://www.luogu.com.cn/problem/P6560)
  * [Luogu P7589 é»ç½æ£ï¼2021 CoE-II Bï¼](https://www.luogu.com.cn/problem/P7589)
  * [AtCoder Regular Contest 168 B - Arbitrary Nim](https://atcoder.jp/contests/arc168/tasks/arc168_b)

ç¶åæ¯ä¸äºæç»´æ§æ´å¼ºææ´ä¸ºç»¼åçé¢ç®ï¼

  * [Luogu P2490 [SDOI2011] é»ç½æ£](https://www.luogu.com.cn/problem/P2490)
  * [Luogu P3179 [HAOI2015] æ°ç»æ¸¸æ](https://www.luogu.com.cn/problem/P3179)
  * [Luogu P5363 [SDOI2019] ç§»å¨éå¸](https://www.luogu.com.cn/problem/P5363)
  * [Luogu P5970 [POI 2016] Nim z utrudnieniem](https://www.luogu.com.cn/problem/P5970)
  * [Luogu P6791 [SNOI2020] åç³å­](https://www.luogu.com.cn/problem/P6791)
  * [Luogu P7864ãEVOI-RD1ãæå¶å­](https://www.luogu.com.cn/problem/P7864)
  * [Luogu P8347ãWdoi-6ãå¦ä¸ä¾§çæ](https://www.luogu.com.cn/problem/P8347)
  * [AtCoder Grand Contest 002 E - Candy Piles](https://atcoder.jp/contests/agc002/tasks/agc002_e)
  * [AtCoder Grand Contest 010 F - Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)
  * [AtCoder Grand Contest 017 D - Game on Tree](https://atcoder.jp/contests/agc017/tasks/agc017_d)
  * [AtCoder Beginner Contest 278 G - Generalized Subtraction Game](https://atcoder.jp/contests/abc278/tasks/abc278_g)
  * [SPOJ COT3 - Combat on a tree](https://www.spoj.com/problems/COT3/)
  * [Codeforces 494 E. Sharti](https://codeforces.com/problemset/problem/494/E)
  * [Codeforces 1149 E. Election Promises](https://www.luogu.com.cn/problem/CF1149E)
  * [Codeforces 1451 F. Nullify The Matrix](https://codeforces.com/problemset/problem/1451/F)
  * [Codeforces 1704 F. Colouring Game](https://codeforces.com/problemset/problem/1704/F)

æåæ¯ä¸äºäºåå¾åå¼çé¢ç®ï¼ç±äºéè¦ç¨å°ä¸äºäºåå¾å¹é çç®æ³ï¼æ å°å®ä»¬åç¬ååºï¼

  * [Luogu P4136 è°è½èµ¢å¢ï¼](https://www.luogu.com.cn/problem/P4136)
  * [Luogu P4617 [COCI 2017/2018 #5] Planinarenje](https://www.luogu.com.cn/problem/P4617)
  * [Luogu P4055 [JSOI2009] æ¸¸æ](https://www.luogu.com.cn/problem/P4055)
  * [Luogu P1971 [NOI2011] å å ä¸èèæ¸¸æ](https://www.luogu.com.cn/problem/P1971)
  * [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## åèèµæä¸æ³¨é

  * [ï¼è½¬è½½ï¼Nim æ¸¸æåå¼ï¼æ¶éå®å ¨çï¼by exponent - åå®¢å­](http://www.cnblogs.com/exponent/articles/2141477.html)
  * [[ç»åæ¸¸æä¸åå¼è®º]ãå­¦ä¹ ç¬è®°ãby Candy? - åå®¢å­](https://www.cnblogs.com/candy99/p/6548836.html)
  * [Nim - Wikipedia](https://en.wikipedia.org/wiki/Nim)
  * [SpragueâGrundy theorem - Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
  * [Nimber - Wikipedia](https://en.wikipedia.org/wiki/Nimber)
  * [Beatty Sequence - Wikipedia](https://en.wikipedia.org/wiki/Beatty_sequence)
  * [Games on arbitrary graphs - CP Algorithms](https://cp-algorithms.com/game_theory/games_on_graphs.html)
  * [ç®æ³å­¦ä¹ ç¬è®°ï¼74): äºåå¾åå¼ by Pecco - ç¥ä¹](https://zhuanlan.zhihu.com/p/359334008)
  * Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
  * Berlekamp, Elwyn R., John H. Conway, and Richard K. Guy. Winning ways for your mathematical plays, volume 1-4. AK Peters/CRC Press, 2001-2004.

* * *

  1. ãNN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æãåãPP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æãè¿ä¸¤ä¸ªåç§°åå«è¡¨ç¤ºãä¸ä¸åç©å®¶èå©ãï¼Next player winsï¼åãåä¸åç©å®¶èå©ãï¼Previous player winsï¼ï¼Â â©

  2. æ¬æè®¨è®ºçãåãé½æ¯ **é¿è§å** ï¼long ruleï¼ä¸ç **æåå** ï¼disjunctive sumï¼ï¼è¿ä¹æ¯æå¸¸è§çä¸ç§æ¸¸æç»åæ¹å¼ï¼é¤æ­¤ä¹å¤ï¼è¿æå ¶ä»å¯è½çæ¸¸æç»åæ¹å¼ï¼å ³äºå®ä»¬çè¯¦ç»è®¨è®ºï¼å¯ä»¥åè Conway, John H. On numbers and games. AK Peters/CRC Press, 2000. ä¸ä¹¦çç¬¬ 14 ç« ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/27 12:26:08ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/game-theory/impartial-game.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/game-theory/impartial-game.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [MegaOwIer](https://github.com/MegaOwIer), [ouuan](https://github.com/ouuan), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [woruo27](https://github.com/woruo27), [AngelKitty](https://github.com/AngelKitty), [chu-yuehan](https://github.com/chu-yuehan), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [tinjyu](https://github.com/tinjyu), [weiyong1024](https://github.com/weiyong1024), [2008verser](https://github.com/2008verser), [billchenchina](https://github.com/billchenchina), [ChungZH](https://github.com/ChungZH), [cutekibry](mailto:cutekibry@yahoo.com), [cutekibry](https://github.com/cutekibry), [FFjet](https://github.com/FFjet), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hhc0001](https://github.com/hhc0001), [isdanni](https://github.com/isdanni), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Molmin](https://github.com/Molmin), [orzAtalod](https://github.com/orzAtalod), [Peanut-Tang](https://github.com/Peanut-Tang), [SaMiiKaaaa](https://github.com/SaMiiKaaaa), [ShizuhaAki](https://github.com/ShizuhaAki), [SukkaW](https://github.com/SukkaW), [TOMWT-qwq](https://github.com/TOMWT-qwq)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
