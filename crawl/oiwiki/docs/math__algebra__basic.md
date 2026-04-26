# åºæ¬æ¦å¿µ - OI Wiki

- Source: https://oi-wiki.org/math/algebra/basic/

# åºæ¬æ¦å¿µ

æ¬ç« èå°ç®è¦ä»ç»æ½è±¡ä»£æ°çç¸å ³ç¥è¯ï¼ç°é¶æ®µç®æ³ç«èµçä¸»è¦å å®¹å¹¶ä¸ç´æ¥èå¯æ½è±¡ä»£æ°çç¥è¯ï¼ä½æ¯å¨ç®æ³çæè¿°ææ¯é®é¢çé¢è§£ä¸­å¸¸å¸¸ä¼çµæ¶ä¸äºæ½è±¡å½æ°çåºæ¬æ¦å¿µï¼è¿ä½¿å¾ææ¡äºåºç¡æ½è±¡ä»£æ°æ¦å¿µçè¯»è è½å¤æ´å¿«éçè§£ä¸äºç®æ³ï¼å æ­¤ï¼è¿é¨åå å®¹å¹¶ä¸æ¯ä»»ä½éæçå¿ ä¿®ç¥è¯ï¼èä» ä¾é£äºæå ´è¶£æè å¯è½ä»ä¸­åççè¯»è åèä½¿ç¨ï¼åæ¶ï¼æ¬ç« èå°é¿å è¿å ¨è¿æ·±çä»ç»æ½è±¡ä»£æ°çç¥è¯1ï¼èä¼éä¸­å¨åºç¡æ¦å¿µä»¥åä¸ OI å ¶ä»é¨åç¥è¯èç³»æä¸ºç´§å¯çé¨åï¼æ³ç³»ç»å­¦ä¹ æ½è±¡ä»£æ°ç¥è¯çè¯»è ï¼åºå½åèä¸ä¸çæ½è±¡ä»£æ°æç§ä¹¦å­¦ä¹ ï¼

ä¸ºäºæ´å¥½å¸®å©è¯»è çè§£é è¯»æ¬é¨åå å®¹å¯è½çæ¶è·ï¼åä¸¾ä¸äºç®æ³ç«èµä¸­å¯è½çµæ¶å°æ½è±¡ä»£æ°ç¥è¯çä¾å­ï¼

  * æ°è®ºåå¤é¡¹å¼çå¾å¤å®çæ¯æ½è±¡ä»£æ°ä¸­ç»è®ºçç¹ä¾ï¼
  * æ°æ®ç»æä¸­ï¼[çº¿æ®µæ ](../../../ds/seg/) ç­ç»æå¯ä»¥ç»´æ¤å¹ºåç¾¤çä¿¡æ¯ï¼èå¾å¤ DP é®é¢çéæ¨å ³ç³»å¯ä»¥æ½è±¡æè¿æ ·çå¹ºåç¾¤ç»æï¼
  * ç»åæ°å­¦ä¸­ï¼[PÃ³lya è®¡æ°åç](../../combinatorics/polya/) çä¸¥æ ¼è¡¨è¿°åè¯æéè¦ç¨å°ç¾¤è®ºçç¸å ³æ¦å¿µï¼

åºäºæ­¤ï¼æ¬ç« èå°çéä»ç»æ æ³è·³è¿çåºç¡ç¥è¯åä¸è¿äºåºç¨ç´æ¥ç¸å ³çé¨åï¼ä½ä¸ºå¼å§ï¼æ¬æä»ç»ç¾¤ãç¯ãåçåºæ¬æ¦å¿µï¼

## ç¾¤

ç¾¤çå®ä¹å¦ä¸ï¼

ç¾¤

è®¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯éç©ºéåï¼å ¶ä¸æäºå è¿ç® â  :ðº Ãðº âðºâ :GÃGâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä»¬æ»¡è¶³ä»¥ä¸æ§è´¨ï¼åç§° (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **ç¾¤** ï¼groupï¼ï¼

  1. ç»åå¾ï¼associative propertyï¼ï¼å¯¹äºææ ð,ð,ð âðºa,b,câG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç« ð â (ð â ð) =(ð â ð) â ðaâ (bâ c)=(aâ b)â c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. æåä½å ï¼å­å¨ ð âðºeâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾å¯¹äºä»»æ ð âðºaâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æç« ð â ð =ð â ð =ðaâ e=eâ a=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éï¼ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **åä½å ** ï¼identity elementï¼ï¼ä¹ç§°å¹ºå ï¼
  3. å­å¨éå ï¼å¯¹äºææ ð âðºaâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½å­å¨ç¸åºç ð âðºbâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð â ð =ð â ð =ðaâ b=bâ a=e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éï¼ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **éå ** ï¼inverse elementï¼ï¼

å ³äºå®ä¹ä¸­çå°é­æ§æ¡ä»¶

è¿éçäºå è¿ç®å°±éå«äºæè°çå°é­æ§æ¡ä»¶ï¼å³å¯¹äºä»»ä½ ð,ð âðºa,bâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð â ð âðºaâ bâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æäºæç« ä¼å°å ¶åç¬ååºï¼

ç¾¤çåºæ¬æ§è´¨

å¯¹äºç¾¤ (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥ä¸æ§è´¨æ»æ¯æç«ï¼

  1. å¯¹äºä»»ä½æéé¿çå {ðð}ðð=1 âðº{gi}i=1kâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹ç§¯ ð1 â ð2 â â¯ â ððg1â g2â â¯â gk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿ç®ç»æä¸å æ¬å·çæ¹å¼æ å ³ï¼
  2. åä½å  ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯å¯ä¸çï¼
  3. å¯¹äºä»»ä½å ç´ ð âðºaâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çé ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯å¯ä¸çï¼
  4. æ¶å»å¾ï¼cancellation lawï¼ï¼å¯¹äº ð,ð,ð âðºa,b,câG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð â ð =ð â ðaâ c=bâ c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð â ð =ð â ðcâ a=câ b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ ð =ða=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¾¤ç¸å½å¸¸è§ï¼éä¿å°è¯´ï¼ææä¸æå¤±ç»æçåæ¢é½èªå¨ææç¾¤ï¼ä»¥å¸¸è§çå ç§ç±»åçç¾¤ä¸ºä¾ï¼

ç¾¤çä¾å­

  * **å¯¹ç§°ç¾¤** ï¼symmetric groupï¼ï¼éå ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çææ [ç½®æ¢](../../permutation/)ï¼å³èª ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èªèº«çåå°ï¼å°±å¨æ å°çå¤åä¸ææç¾¤ ððSM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½å æ¯æç­åæ¢ï¼éå æ¯éæ å°ï¼åå°å¿ ç¶å­å¨éæ å°ï¼ï¼å¦æéå ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æéï¼å¤§å°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å¸¸è®°ä½ ððSn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç§°ä½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¯¹ç§°ç¾¤ï¼
  * ç©ºé´å¯¹ç§°ç¾¤ï¼symmetry groupï¼ï¼å¯¹äºä¸ä¸ªå ä½å¾å½¢ï¼è½å¤ä½¿å ¶ä¸èªèº«éåçåæ¢å ¨ä½ä¹å¨æ å°çå¤åä¸ææç¾¤ï¼è¿æè¿°äºè¯¥å ä½å¾å½¢çç©ºé´å¯¹ç§°æ§ï¼å ·ä½ä¾å­å¯ä»¥åè [å¸¸è§ç©ºé´å¯¹ç§°ç¾¤](../../combinatorics/polya/#å¸¸è§ç©ºé´å¯¹ç§°ç¾¤)ï¼
  * æ´æ°çå æ³ç¾¤ï¼æ´æ°é ðZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨å æ³ ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ç®ä¸ææç¾¤ (ð, +)(Z,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½å æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éå æ¯ç¸åæ°ï¼
  * æ´æ°æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ³ç¾¤ï¼multiplicative group of integers modulo ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å¯¹äºä¸ä¸ªæ¨¡æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ææä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè´¨çæ´æ°å¯¹åºç [åä½ç±»](../../number-theory/basic/#åä½ç±»ä¸å©ä½ç³»)ï¼å¨ä¹æ³è¿ç®ä¸ææç¾¤ ((ð/ðð)Ã, Ã)((Z/nZ)Ã,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½å æ¯ Â¯11Â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éå å°±æ¯æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [ä¹æ³éå ](../../number-theory/inverse/)ï¼å¯¹åºçåä½ç±»ï¼ï¼å ¶å­å¨æ§ç± [è£´èå®ç](../../number-theory/bezouts/) ä¿è¯ï¼å ·ä½ç»æåæåè [æ´æ°æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ³ç¾¤](../ring-theory/#åºç¨æ´æ°åä½ç±»çä¹æ³ç¾¤)ï¼
  * ä¸è¬çº¿æ§ç¾¤ï¼general linear groupï¼ï¼æ°å ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çå ¨ä½å¯éæ¹éµå¨ä¹æ³è¿ç®ä¸ææç¾¤ ðºð¿ð(ð¹)GLn(F)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½å æ¯åä½ç©éµï¼éå æ¯éç©éµï¼

è¦æ´å¥½å°çè§£ç¾¤çå®ä¹ï¼ä¸å¦¨å¯¹æ¯ççå ä¸ªä¸å±äºç¾¤çä¾å­ï¼

ä¸æ¯ç¾¤çä¾å­

  * ææ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°èªèº«çæ å°ï¼ä¸ä¸å®æ¯åå°ï¼ï¼å¹¶ä¸ææç¾¤ï¼å ä¸ºé£äºä¸æ¯åå°çæ å°ä¸å­å¨éå ï¼
  * æ´æ°å¨ä¹æ³ä¸å¹¶ä¸ææç¾¤ï¼å ä¸º 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ´æ°èå´å æ²¡æä¹æ³éå ï¼
  * æ­£æ´æ°å¨å æ³ä¸ä¹ä¸ææç¾¤ï¼å ä¸ºæ­£æ´æ°æ²¡æå æ³åä½å ï¼
  * æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææéé¶åä½ç±»å¨ä¹æ³æä¹ä¸å¾å¾ä¸ææç¾¤ï¼æ¯å¦è¯´ (ð/6ð) â{ââ0}(Z/6Z)â{0â}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼ââ2 Ãââ3 =ââ02âÃ3â=0â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å±äºè¿ä¸ªéåï¼è¿æå³çä¹æ³é½ä¸æ¯è¿ä¸ªéåä¸è¯å®ä¹çäºå è¿ç®ï¼æè è¯´ï¼å®ä¸æ»¡è¶³å°é­æ§ï¼ï¼

ææ¶ï¼ä¹éè¦è®¨è®ºè¿äºæ´ä¸å®åçç»æçæ§è´¨ï¼å æ­¤ï¼å¯ä»¥å®ä¹å¦ä¸æ¦å¿µï¼å®ä»¬æ¯ç¾¤æ´å®½æ³ï¼

åç¾¤

å¯¹äºéç©ºéå ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ä¸çäºå è¿ç® â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æè¯¥è¿ç®æ»¡è¶³ç»åå¾ï¼åç§° (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **åç¾¤** ï¼semigroupï¼ï¼

å¹ºåç¾¤

å¯¹äºåç¾¤ (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®è¿å­å¨åä½å ï¼åç§° (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **å¹ºåç¾¤** ï¼monoidï¼ï¼

å¹ºåç¾¤ååç¾¤çä¾å­

ä¸é¢çä¾å­ä¸­ï¼(ð+, +)(N+,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åç¾¤ï¼è (ð, Ã)(Z,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¹ºåç¾¤ï¼

æåï¼å¾å¤çæçç¾¤ä¸çè¿ç®é¤äºæ»¡è¶³ç»åå¾å¤ï¼è¿æ»¡è¶³äº¤æ¢å¾ï¼è¿ç±»ç¾¤çç»æç¸å¯¹ç®åï¼å®ä»¬ç§°ä½ Abel ç¾¤ï¼ä¹ç§°ä½äº¤æ¢ç¾¤ï¼

Abel ç¾¤

å¯¹äºç¾¤ (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æè¿ç® â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ»¡è¶³äº¤æ¢å¾ï¼commutative propertyï¼ï¼å³å¯¹äºææ ð,ð âðºa,bâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æç« ð â ð =ð â ðaâ b=bâ a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§° (ðº, â )(G,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **Abel ç¾¤** ï¼Abelian groupï¼æ **äº¤æ¢ç¾¤** ï¼communicate groupï¼ï¼

Abel ç¾¤åé Abel ç¾¤çä¾å­

  * æ´æ°å æ³ç¾¤ (ð, +)(Z,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ä¸ä¸ª Abel ç¾¤ï¼
  * å½ ð â¥3nâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¯¹ç§°ç¾¤ ððSn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸æ¯ Abel ç¾¤ï¼

è¿äºå°±æ¯ç¾¤è®ºç¸å ³çåºæ¬å®ä¹ï¼ç¾¤è®ºçæ´å¤å å®¹ï¼å¯ä»¥åè [ç¾¤è®º](../group-theory/) æç¸å ³ä¹¦ç±ï¼

## ç¯

ç¯çå®ä¹å¦ä¸ï¼

ç¯

å¯¹äºéç©ºéå ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ä¸çä¸¤ä¸ªäºå è¿ç® + :ð  Ãð  âð +:RÃRâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â  :ð  Ãð  âð â :RÃRâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä»¬æ»¡è¶³ä»¥ä¸æ§è´¨ï¼åç§° (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **ç¯** ï¼ringï¼ï¼

  1. (ð , +)(R,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ Abel ç¾¤ï¼å ¶åä½å è®°ä½ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ç´ ð âð aâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çéå è®°ä½ âðâa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. (ð , â )(R,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææåç¾¤ï¼å³ â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ç»åå¾ï¼
  3. åé å¾ï¼distributive propertyï¼ï¼å¯¹äºææ ð,ð,ð âð a,b,câR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç« ð â (ð +ð) =ð â ð +ð â ðaâ (b+c)=aâ b+aâ c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð +ð) â ð =ð â ð +ð â ð(a+b)â c=aâ c+bâ c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºè¡¨è¿°æ¹ä¾¿ï¼è¿ä¸¤ä¸ªäºå è¿ç® ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¸¸ç§°ä½è¯¥ç¯çå æ³åä¹æ³ï¼ç¸åºå°ï¼å æ³åä½å ç§°ä½ **é¶å ** ï¼zeroï¼ï¼ä¹æ³åä½å ï¼å¦æå­å¨ï¼ç§°ä½ **å¹ºå ** ï¼identityï¼ï¼åºé¿å åå ·ä½çæ°éä¸­çå æ³ãä¹æ³ï¼ä»¥åèªç¶æ°é¶åä¸äº§çæ··æ·ï¼

å ³äºå®ä¹ä¸­æ¯å¦è¦æ±ä¹æ³åä½å 

å¨æçå®ä¹ä¸­ï¼ç¯å¿ é¡»å­å¨ä¹æ³åä½å ï¼ç¸å¯¹å°ï¼ä¸å­å¨ä¹æ³åä½å çåè¢«ç§°ä¸º **ä¼ªç¯** ï¼rng æ pseudo-ringï¼ï¼éå°çæ¶åéæ ¹æ®ä¸ä¸æå ä»¥å¤æ­ï¼ç»´åºç¾ç§éç¨çå°±æ¯è¿ç§å®ä¹3ï¼

ç¯çå æ³ç»æç¸å½ç®åï¼ä½æ¯ä¹æ³ç»æåååå§ï¼å èå¦æç±»æ¯ç¾¤ï¼å¨ä¹æ³ä¸åæ´å¤è¦æ±ï¼å¯ä»¥å¾å°å¦ä¸ç¸å ³å®ä¹ï¼

å¹ºç¯

å¯¹äºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®å«å¹ºï¼å³å­å¨ä¹æ³åä½å ï¼è®°ä½ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§° (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **å¹ºç¯** ï¼ring with identityï¼ï¼

é¤ç¯

å¯¹äºéé¶å¹ºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå¯¹äºææé 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç´ ð âð aâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½å­å¨ä¹æ³éå ï¼è®°ä½ ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼åç§° (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **é¤ç¯** ï¼division ringï¼ï¼

äº¤æ¢ç¯

å¯¹äºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®çä¹æ³æ»¡è¶³äº¤æ¢å¾ï¼åç§° (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **äº¤æ¢ç¯** ï¼commutative ringï¼ï¼

è¿éé¤ç¯çå®ä¹ä¸­æè¶£çä¸ç¹æ¯ï¼å®å° 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è§ä¸ºä¹æ³ç»æä¸­çç¹æ®å ç´ ï¼è¿æ¯å ä¸º 0 =0 â ð =ð â 00=0â a=aâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2ï¼ä¹å°±æ¯è¯´ï¼ç¯ä¸­å æ³åä½å ä¹ä»¥ä»»ä½å ç´ é½å¾å°å ¶èªèº«ï¼è¿æ ·ï¼å®èªç¶ä¸ä¼å­å¨ä¹æ³éå ï¼é¤éå®æ¬èº«å°±æ¯ä¹æ³åä½å ï¼è¿æ ·çç¯åªæé¶ç¯ï¼è§ä¸é¢çä¾å­ï¼ï¼

è¿éçå¯ç¤ºæ¯ï¼çè§£ä¸è¬çç¯çä¹æ³ç»ææ¶ï¼è¦å»é¤å æ³åä½å çå½±åï¼èå¯ ð  â{0}Râ{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºäºè¿ä¸æ³æ³ï¼æå¦ä¸å®ä¹ï¼

é¶å å­

å¯¹äºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå­å¨ ð âð bâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â 0bâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç« ð â ð =0aâ b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð â ð =0bâ a=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§°éé¶å ç´ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¸ä¸ª **é¶å å­** ï¼zero divisorï¼ï¼

å¯éå ï¼åä½ï¼

å¯¹äºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå ç´ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹æ³éå ï¼å³å­å¨ ð âð bâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç« ð â ð =ð â ð =1aâ b=bâ a=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§°å ç´ ð âð aâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **å¯éå ** ï¼æç§° **åä½** ï¼unitï¼ï¼

ãåä½ãä¸ãåä½å ã

è¯·ä¸è¦æ··æ·è¿ä¸¤ä¸ªæ¦å¿µï¼ä¸ºé¿å æ··æ·ï¼æ½è±¡ä»£æ°é¨åå°ä½¿ç¨ãå¯éå ãçåç§°ä»£æ¿ãåä½ãï¼

é¶å å­ä¸å¯è½æ¯å¯éå ï¼å¯éå ä¸å¯è½æ¯é¶å å­ï¼ä½æ¯ï¼ä¸ä¸ªéé¶å ç´ å¯ä»¥æ¢ä¸æ¯é¶å å­ï¼ä¹ä¸æ¯å¯éå ï¼

å¦æä¸ä¸ªç¯æ²¡æé¶å å­ï¼å°±è¯´æææéé¶å ç´ çéåå¨ä¹æ³è¿ç®ä¸å°é­ï¼å³ (ð  â{0}, â )(Râ{0},â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææåç¾¤ï¼è¿ä¸æ­¥å°ï¼å¦æè¿è¦æ±å®æä¸ºäº¤æ¢å¹ºåç¾¤ï¼å°±å¯ä»¥å¾å°æ´ç¯çå®ä¹ï¼

æ´ç¯

å¯¹äºéé¶ç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®æ¯äº¤æ¢ç¯ï¼æä¹æ³åä½å ï¼ä¸æ é¶å å­ï¼åç§°å®ä¸ºæ´ç¯ï¼integral domainï¼ï¼

è½ç¶æ´ç¯ä¸­çå ç´ ä¸ä¸å®å­å¨éå ï¼ä½æ¯æ²¡æé¶å å­è¿ä¸ç¹æ§å·²ç»è¶³å¤å¨æ´ç¯ä¸å»ºç«æ¶å»å¾ï¼

æ´ç¯çæ¶å»å¾

è®¾æ´ç¯ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå ç´ ð,ð,ð âð a,b,câR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â 0aâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ðð =ððab=ac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¿ ç¶æ ð =ðb=c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äºä¸è¬çå¹ºç¯ï¼å¦æåªèèå®çå ¨ä½å¯éå ï¼é£ä¹åæ ·å¯ä»¥å¾å°ç¾¤ç»æï¼è¿ç§°ä¸ºç¯çä¹æ³ç¾¤ææ¯åä½ç¾¤ï¼

ä¹æ³ç¾¤ï¼åä½ç¾¤ï¼

å¯¹äºå¹ºç¯ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ ð ÃRÃ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å ¨ä½å¯éå çéåï¼å (ð Ã, â )(RÃ,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææç¾¤ï¼ç§°ä¸ºå¹ºç¯ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ä¹æ³ç¾¤** ï¼multiplicative groupï¼ï¼ææ¯ **åä½ç¾¤** ï¼unit groupï¼ï¼

æç®åçä¸äºç¯çä¾å­å¦ä¸ï¼

ç¯çä¾å­

  * é¶ç¯ï¼zero ringï¼ï¼éå {0}{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨éå¸¸æä¹çå æ³ ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¹æ³ ÃÃ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ææç¯ï¼ç§°ä¸ºé¶ç¯ï¼å®æ¯å¯ä¸çåªæä¸ä¸ªå ç´ çç¯ï¼ä¹æ¯å¯ä¸çå æ³åä½å åä¹æ³åä½å ç¸ç­çç¯ï¼
  * æ´æ°ç¯ï¼æ´æ°é ðZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ä¸éå¸¸å®ä¹çå æ³ ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¹æ³ ÃÃ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææäºç¯ (ð, +, Ã)(Z,+,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®é ä¸ï¼è¿æ¯ä¸ä¸ªæ´ç¯ï¼ä½æ¯å®ä¸æ¯é¤ç¯ï¼
  * å¤é¡¹å¼ç¯ï¼å¯¹äºä¸ä¸ªç¯ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å¨ä¸é¢å®ä¹ [å¤é¡¹å¼ç¯](../ring-theory/#å¤é¡¹å¼ç¯) ð [ð¥]R[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´ç¯ï¼åè¯¥å¤é¡¹å¼ç¯å¿ ç¶æ¯æ´ç¯ï¼
  * åå æ°ï¼quaternionï¼ï¼ç±»æ¯å¤æ°ï¼å¯ä»¥èèéå ð ={ð +ði +ðj +ðk :ð,ð,ð,ð âð}H={a+bi+cj+dk:a,b,c,dâR}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸å®ä¹å ¶ä¸çå æ³åä¹æ³ï¼è¿éï¼i,j,ki,j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹æ³è¿ç®æ»¡è¶³

i2=j2=k2=â1,Â ij=âji=k,Â jk=âkj=i,Â ki=âik=j.i2=j2=k2=â1,Â ij=âji=k,Â jk=âkj=i,Â ki=âik=j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹å¯ä»¥éªè¯ï¼ðH![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææç¯ï¼èä¸ï¼å®æ¯ä¸ä¸ªéäº¤æ¢çé¤ç¯ï¼

  * æ´æ°éçå­é 2ð2Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨éå¸¸æä¹çå æ³åä¹æ³ä¸ææç¯ï¼å®æ¯äº¤æ¢ç¯ï¼æ²¡æé¶å å­ï¼ä½æ¯å¹¶ä¸å«å¹ºï¼

  * æ´æ°æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½ç±» ð/ððZ/nZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨åä½ç±»çå æ³åä¹æ³è¿ç®ä¸ææç¯ï¼å®æ¯äº¤æ¢ç¯ï¼å«å¹ºï¼å³ Â¯11Â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼è¿æ ·çç¯å«æé¶å å­ï¼å½ä¸ä» å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åæ°ï¼æä»¥ï¼å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç´ æ°æ¶ï¼ç¯ (ð/ðð, +, Ã)(Z/nZ,+,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´ç¯ï¼èä¸ï¼æ­¤æ¶å®ä¹æ¯é¤ç¯ï¼æä»¥å®å®é ææä¸ºäºä¸ä¸ªåï¼å®çä¹æ³ç¾¤ ((ð/ðð)Ã, Ã)((Z/nZ)Ã,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯æ´æ°æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ³ç¾¤ï¼
  * ç©éµç¯ï¼ç¯ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çå ¨ä½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´æ¹éµå¨ç©éµçå æ³åä¹æ³ä¸ææä¸ä¸ªç¯ ðð(ð )Mn(R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è¬å°ï¼è¿ä¸ªç¯æé¶å å­ï¼ä¸ä¸æ¯äº¤æ¢ç¯ï¼
  * å¯¹äºä¸ä¸ªéå ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½å­é P(ð´)P(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä¹éåçå¯¹ç§°å·® â³â³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åäº¤ â©â©![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«ä¸ºå ¶å æ³åä¹æ³è¿ç®ï¼å (P(ð´),â³, â©)(P(A),â³,â©)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææç¯ï¼ä¸è¬å°ï¼è¿ä¸ªç¯å«å¹ºï¼æé¶å å­ï¼ä¸æ¯äº¤æ¢ç¯ï¼

å½ç¶ï¼å¯¹äºç¯çç»æçè®¨è®ºè¿ä¸æ­¢è¿äºï¼è¦äºè§£æ´å¤å å®¹ï¼å¯ä»¥åè [ç¯è®º](../ring-theory/) æç¸å ³ä¹¦ç±ï¼

## å

åæ¯ä¸ä¸ªæ¯ç¯æ§è´¨æ´å¼ºçä»£æ°ç»æï¼å ·ä½å°ï¼åæ¯äº¤æ¢é¤ç¯ï¼å½ç¶ä¹å¯ä»¥ååºå®å®æ´çå®ä¹ï¼

å

å¯¹äºéç©ºéå ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ä¸çä¸¤ä¸ªäºå è¿ç® + :ð¹ Ãð¹ âð¹+:FÃFâF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â  :ð¹ Ãð¹ âð¹â :FÃFâF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä»¬æ»¡è¶³ä»¥ä¸æ§è´¨ï¼åç§° (ð¹, +, â )(F,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª **å** ï¼fieldï¼ï¼

  1. (ð¹, +)(F,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ Abel ç¾¤ï¼å ¶åä½å è®°ä½ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ç´ ð âð¹aâF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çéå è®°ä½ âðâa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. (ð¹ â{0}, â )(Fâ{0},â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ Abel ç¾¤ï¼å ¶åä½å è®°ä½ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ç´ ð âð¹ â{0}aâFâ{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çéå è®°ä½ ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¢å¥è¯è¯´ï¼åæ¯å¯¹å ãåãä¹ãé¤ååè¿ç®é½å°é­çä»£æ°ç»æï¼

å¸¸è§çåçä¾å­å¦ä¸ï¼

åçä¾å­

  * æ°åï¼æçæ°é ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®æ°é ðR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¤æ°é ðC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨éå¸¸æä¹çå æ³åä¹æ³ä¸é½ææåï¼
  * æéåï¼finite fieldï¼ï¼ä»¥è´¨æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ¨¡çæ´æ°åä½ç±»çéå ð/ððZ/pZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨åä½ç±»çå æ³åä¹æ³ä¸ææåï¼å½ç¶ï¼é¤æ­¤ä¹å¤è¿æå ¶ä»çæéåï¼å®ä»¬çç»æç±å ¶å¤§å°å¯ä¸ç¡®å®ï¼ä¸å¤§å°å¿ ç¶æ¯è´¨æ°å¹çå½¢å¼ï¼
  * **åå¼å** ï¼fraction fieldï¼ï¼è®¾ (ð , +, â )(R,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ´ç¯ï¼å¯ä»¥èèå½¢å¦ ððâ1abâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ç´ ææçéå ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¥æ ¼å°è¯´ï¼å¨éå ð  Ã(ð  â{0})RÃ(Râ{0})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®ä¹ç­ä»·å ³ç³»ï¼(ð1,ð1) â¼(ð2,ð2)(a1,b1)â¼(a2,b2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½ä¸ä» å½ ð1ð2 =ð2ð1a1b2=a2b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼éå ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¿ä¸å ³ç³»ä¸çç­ä»·ç±»ææçéå ð  Ã(ð  â{0})/ â¼RÃ(Râ{0})/â¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼(ð,ð)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¨ç­ä»·ç±»å°±è®°ä½ ððâ1abâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä¹å®ä¸é¢çè¿ç®ä¸º

ð1ðâ11+ð2ðâ12=(ð1â ð2+ð2â ð1)(ð1â ð2)â1,(ð1ðâ11)â (ð2ðâ12)=(ð1â ð2)(ð1â ð2)â1a1b1â1+a2b2â1=(a1â b2+a2â b1)(b1â b2)â1,(a1b1â1)â (a2b2â1)=(a1â a2)(b1â b2)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å (ð, +, â )(Q,+,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææåï¼ç§°ä¸º ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼åï¼ä¾å¦ï¼æçæ°å (ð, +, Ã)(Q,+,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯æ´æ°ç¯ (ð, +, Ã)(Z,+,Ã)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼åï¼

  * äºæ¬¡åï¼quadratic fieldï¼ï¼å®æ¯å¨æçæ°å ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ·»å äº âðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èæ©å¼ æçï¼è¿é ð â 0,1dâ 0,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ²¡æå¹³æ¹å å­ï¼ç¸å ³å å®¹å¯ä»¥åè [äºæ¬¡å](../../number-theory/quadratic/)ï¼

åç¸è¾äºç¯ï¼æ¥æçéå¸¸ç®åçå æ³åä¹æ³ç»æï¼æä»¥ï¼åæ¬èº«çç»æå¾å¾å¾ç®åï¼è¿ä½¿å¾åçç ç©¶åç¯çç ç©¶å¤§ä¸ç¸åï¼éå¸¸ä¼è½¬èç ç©¶åçæ©å¼ ï¼ä»¥åç¸åºç Galois çè®ºï¼å¨ç®æ³ç«èµä¸­ï¼ææ¶ä¼éè¦å¨æçæ°åæè æéåçæ©åä¸è¿è¡è®¡ç®ï¼åè®ºçç¸å ³å å®¹ï¼å¯ä»¥åè [åè®º](../field-theory/) æç¸å ³ä¹¦ç±ï¼

## åºç¨

æåï¼ä»¥ä¸é¢çé¢ç®ä¸ºä¾ï¼è¯´ææ½è±¡çä»£æ°å¯¹è±¡æ¯ææ ·è¾ å©åæå ·ä½çé®é¢çï¼

[ãæ¨¡æ¿ã"å¨æ DP"& å¨ææ åæ²»ï¼å å¼ºçï¼](https://www.luogu.com.cn/problem/P4751)

ç»å®å¤§å°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¸¦ç¹æçæ ï¼è¿è¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ç¹æä¿®æ¹ï¼æ¯æ¬¡ä¿®æ¹åè¦è¾åºæ ä¸æå¤§å¸¦æç¬ç«éçæå¼ä¹åï¼é®é¢å¼ºå¶å¨çº¿ï¼

æè·¯åæ

è¿éé¢æ¯å¨æ DP æ¨¡æ¿ï¼ä¸ç§å¤æåº¦æ­£ç¡®çä»£ç å®ç°éè¦ç¨å° [å ¨å±å¹³è¡¡äºåæ ](../../../ds/global-bst/)ï¼å ·ä½æ ·ä¾ä»£ç ä¹å¨å¯¹åºé¡µé¢ï¼è¿éä» ä» ç»åè¯¥é¢æ æ¯ï¼åæå»ºæ¨¡çè¿ç¨ï¼

ä¸ºäºçªåºéç¹ï¼è¿éæä¸èèå ¨å±å¹³è¡¡äºåæ å¯¹äºæ å½¢ç»æçå¤çï¼è½¬èèèé¾ä¸çæå¤§å¸¦æç¬ç«éç DP é®é¢ï¼é¡ºæ¬¡èèé¾ [1,ð][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çæ¯ä¸ªç¹ï¼å¯¹äºç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥éï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¸éï¼00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼åå«è®¾è¿ä¸¤ç§æ å½¢ä¸ï¼[1,ð][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å­é®é¢çæä¼è§£ä¸º ðð,1fi,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð,0fi,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å¯ä»¥ååº DP æ¹ç¨ä¸º

ðð,1=ð¤ð+ððâ1,0,ðð,0=max{ððâ1,1,ððâ1,0}.fi,1=wi+fiâ1,0,fi,0=max{fiâ1,1,fiâ1,0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®çåå¼ä¸º (ð0,1,ð0,0) =(0,0)(f0,1,f0,0)=(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èæç»ç­æ¡å°±æ¯ max{ðð,1,ðð,0}max{fn,1,fn,0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦è¡¨ç¤ºç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºæç»ç»æçå½±åï¼åªéè¦æ³¨æå°è¿ä¸éå½å ³ç³»å¯ä»¥åä½

(ðð,1,ðð,0)=ð(ððâ1,1,ððâ1,0;ð¤ð).(fi,1,fi,0)=g(fiâ1,1,fiâ1,0;wi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸è¿ä¸² ð2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å°ï¼å®å° (ððâ1,1,ððâ1,0)(fiâ1,1,fiâ1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å°å° (ðð,1,ðð,0)(fi,1,fi,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨ç¾¤çè¯­è¨æè¿°ï¼è¿äºåæ¢å¨æ å°çå¤åä¹ä¸ææå¹ºåç¾¤ï¼è¿æ­£æ¯çº¿æ®µæ å¯ä»¥ç»´æ¤çï¼

ä½æ¯ï¼è¿æ ·çå«ååæ¢ ð( â ;ð¤ð)g(â ;wi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¦ææ²¡æç¹æ®çç»æï¼ä¸è¬ç ð2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å°æ¯ä¸å¯è½ç¨æéç»´çæ°æ®æè¿°çï¼è¿éå°±éè¦å¦ä¸é¡¹è§å¯ï¼å³å¦æå¨ ð âª{ ââ}Râª{ââ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼å®ä¹ maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºå æ³ã++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºä¹æ³ï¼é£ä¹ ð âª{ ââ}Râª{ââ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææä¸ç§ç±»ä¼¼ç¯çç»æï¼è¿éï¼ââââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å æ³åä½å ï¼00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¹æ³åä½å ï¼ä½æ¯å®ä¸æ¯ç¯ï¼å ä¸ºå ¶ä¸­çå ç´ å¹¶éé½æå æ³éå ï¼è¿æ ·çç»æå«ååç¯4ï¼è¿é (ð âª{ ââ},max, +)(Râª{ââ},max,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½¢æçåç¯å«å **ç­å¸¦åç¯** ï¼tropical semiringï¼ï¼

åºäºç­å¸¦åç¯ (ð , â, â)(R,â,â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å®ä¹å®ä¸é¢çç©éµä¹æ³ï¼å³å¯¹äº ð ÃðmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´ç©éµ ð´ =(ððð)A=(aij)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð ÃðnÃp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´ç©éµ ðµ =(ððð)B=(bjk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å®ä¹å ¶ä¹ç§¯ ð´ðµAB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º (ððð)(cik)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çæ¯é¡¹å ç´ ç­äº

ððð=ðâ¨ð=1(ðððâððð)=max1â¤ðâ¤ð(ððð+ððð).cik=â¨j=1n(bijâcjk)=max1â¤jâ¤n(bij+cjk).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æäºè¿äºè®°å·ï¼å¯ä»¥å°ä¸è¿°éæ¨å ³ç³»çä½æ¯ç­å¸¦åç¯ä¸ççº¿æ§åæ¢ï¼å¹¶ç¨ç©éµè¯­è¨åä½

(ðð,1ðð,0)=(ââð¤ð00)(ððâ1,1ððâ1,0).(fi,1fi,0)=(ââwi00)(fiâ1,1fiâ1,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ­¤ï¼åªè¦ç¨çº¿æ®µæ ç»´æ¤è¿ä¸ç­å¸¦åç¯ä¸çç©éµçä¹ç§¯å°±å¯ä»¥åç­å¤æ¬¡ä¿®æ¹çé¾ä¸çå¨æ DP é®é¢ï¼

ç°å¨åå°è¯¥é®é¢çæ ä¸çæ¬ï¼å¯¹äºæ ä¸çèç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶å­èç¹éåè®°ä½ ð(ð)S(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¯¥å¤ç DP æ¹ç¨ä¸º

ðð,1=ð¤ð+âðâð(ð)ðð,0,ðð,0=âðâð(ð)max{ðð,1,ðð,0}.fi,1=wi+âjâS(i)fj,0,fi,0=âjâS(i)max{fj,1,fj,0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é¦å ï¼éè¿æ é¾ååå°é®é¢è½¬åä¸ºé¾ä¸çæ¬ï¼è®¾ âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå­èç¹ï¼é£ä¹ä¸è¿°éæ¨æ¹ç¨å¯ä»¥åä½

ðð,1=ð¤ð+ðâ,0+ðð,1,ðð,0=max{ðð,0,ðð,1}+ðð,0,fi,1=wi+fh,0+gi,1,fi,0=max{fj,0,fj,1}+gi,0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éï¼

ðð,1=âðâð(ð),Â ðâ âðð,0,ðð,0=âðâð(ð),Â ðâ âmax{ðð,1,ðð,0}gi,1=âjâS(i),Â jâ hfj,0,gi,0=âjâS(i),Â jâ hmax{fj,1,fj,0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ»ç»äºè½»å­èç¹çè´¡ç®ï¼æ ¹æ®ä¸ææè¿°ï¼è¿äºåæ¢é½å¯ä»¥åä½ç­å¸¦åç¯ä¸çç©éµå½¢å¼ï¼æä»¥ï¼æ´ä¸ªé®é¢ä¹å°±å¯ä»¥å¨æ ååççº¿æ®µæ ä¸ç»´æ¤ï¼ä½æ¯ï¼ç´æ¥ç¨æ åå çº¿æ®µæ çåæ¬¡ä¿®æ¹æ¯ ð(log2â¡ð)O(log2â¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼æä»¥éè¦ç¨å°ä¸ææå°çå ¨å±å¹³è¡¡äºåæ ä¼åå° ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ç¶ä¹å¯ä»¥ç¨ LCT ç»´æ¤ï¼

è¿éæå°çç­å¸¦åç¯ä»¥åä¸é¢çç©éµè¿ç®å ¶å®å¹¶ä¸ç½è§ï¼å¦æå°ä¸æä¸­ç maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢ä½ minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç¸åºçç­å¸¦åç¯å¸¸ç¨äºæç­è·¯é®é¢ä¸­ï¼å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´æ¹éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»åºäºé¡¶ç¹æ°ç®ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¸ªå¾çä¸¤ç¹é´çï¼æç­ï¼è¾¹æï¼é£ä¹ï¼ð´ðAk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çå ç´ å°±æ¯èªç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»è³å¤ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡è¾¹å°ç¹ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­è·ç¦»ï¼ç¹å«å°ï¼ð´ðAn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¯¥å¾çè·ç¦»ç©éµï¼å½ç¶å®é å®ç°çæ¶åå¹¶ä¸ä¼ççæ´åè®¡ç®è¿ä¸ç©éµçå¹ï¼èæ¯ä½¿ç¨å¤æåº¦ä¸º ð(ð3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Floyd ç®æ³ï¼

## åèèµæä¸æ³¨é

  * Dummitt, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
  * [Tropical semiring - Wikipedia](https://en.wikipedia.org/wiki/Tropical_semiring)

* * *

  1. å ä¸º [OI Wiki ä¸æ¯ç¾ç§å ¨ä¹¦](../../../intro/what-oi-wiki-is-not/#oi-wiki-ä¸æ¯ç¾ç§å)ï¼Â â©

  2. è¯¥å¼çæ¨å¯¼å³ 0 â ð +0 =0 â ð =(0 +0) â ð =0 â ð +0 â ð0â a+0=0â a=(0+0)â a=0â a+0â a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿éï¼ç¬¬ä¸ä¸ªç­å·åç¬¬äºä¸ªç­å·æ¯å æ³åä½å çå®ä¹ï¼ç¬¬ä¸ä¸ªç­å·æ¯åé å¾ï¼æåçè´æ¶µå ³ç³»æ¯å æ³çæ¶å»å¾ï¼å¦ä¸ä¾§çä¹æ³ç±»ä¼¼ï¼Â â©

  3. [Ringï¼mathematicsï¼- Wikipedia](https://en.wikipedia.org/wiki/Ring_%28mathematics%29)Â â©

  4. åç¯ï¼semiringï¼æ¯å¨å¹ºç¯çå®ä¹ä¸­æ¾æ¾äºå æ³è¿ç®ä¸å®å­å¨éå çè¦æ±ï¼å³å æ³ç»ææ¯äº¤æ¢å¹ºåç¾¤ãä¹æ³ç»ææ¯å¹ºåç¾¤çä»£æ°ç»æï¼æ´å¤ä¿¡æ¯åè§ [Wikipedia](https://en.wikipedia.org/wiki/Semiring)ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/algebra/basic.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/algebra/basic.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [isdanni](https://github.com/isdanni), [jifbt](https://github.com/jifbt), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [warzone-oier](https://github.com/warzone-oier), [Xeonacid](https://github.com/Xeonacid)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
