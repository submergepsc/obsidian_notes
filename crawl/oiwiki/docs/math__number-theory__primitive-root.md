# é¶ & åæ ¹ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/primitive-root/

# é¶ & åæ ¹

åç½®ç¥è¯ï¼[è´¹é©¬å°å®ç](../fermat/#è´¹é©¬å°å®ç)ã[æ¬§æå®ç](../fermat/#æ¬§æå®ç)ã[ææ ¼ææ¥å®ç](../congruence-equation/#å®ç-3lagrange-å®ç)

é¶ååæ ¹ï¼æ¯çè§£æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) [æ¢çº¦å©ä½ç³»](../basic/#åä½ç±»ä¸å©ä½ç³») ðâðZmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ³ç»æçéè¦å·¥å ·ï¼åºäºæ­¤ï¼å¯ä»¥å®ä¹ [ç¦»æ£å¯¹æ°](../discrete-logarithm/) ç­æ¦å¿µï¼æ´ä¸ºä¸è¬çè®¨è®ºå¯ä»¥åè§æ½è±¡ä»£æ°é¨å [ç¾¤è®º](../../algebra/group-theory/#é¶) å [ç¯è®º](../../algebra/ring-theory/#åºç¨æ´æ°åä½ç±»çä¹æ³ç¾¤) ç­é¡µé¢ç¸å ³ç« èï¼

## é¶

æ¬èä¸­ï¼æ»æ¯åè®¾æ¨¡æ° ð âð+mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååºæ° ð âðaâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å³ (ð,ð) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹è®°ä½ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äº ð âðnâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹æ¬¡ ððmodðanmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç°ä¸ç§å¾ªç¯ç»æï¼è¿ä¸ªå¾ªç¯èçæå°é¿åº¦ï¼å°±æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ï¼é¶å°±å®ä¹ä¸ºå¹ ððmodðanmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¬ä¸æ¬¡åå°èµ·ç¹ ð0modð =1a0modm=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çææ°ï¼

é¶

å¯¹äº ð âð,ð âð+aâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»¡è¶³åä½å¼ ðð â¡1(modð)anâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°æ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä½ **ð a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶**ï¼the order of ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) modulo ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼è®°ä½ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ordðâ¡(ð)ordmâ¡(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ³¨

å¨ [æ½è±¡ä»£æ°](../../algebra/group-theory/#é¶) ä¸­ï¼è¿éçãé¶ãå°±æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»å ³äºä¹æ³å½¢æçç¾¤ä¸­ï¼å ç´ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ï¼ç¨è®°å· ð¿Î´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºé¶åªéç¨äºè¿ä¸ªç¹æ®çç¾¤ï¼ä¸é¢çè¯¸å¤æ§è´¨å¯ä»¥ç´æ¥æ¨å¹¿å°æ½è±¡ä»£æ°ä¸­ç¾¤å ç´ çé¶çæ§è´¨ï¼

å¦å¤è¿æãåé¶ãçæ¦å¿µï¼å¨æ°è®ºä¸­ä¼ç¨ ð¿âÎ´â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®°å·è¡¨ç¤ºï¼å®æ¯æ»¡è¶³åä½å¼ ðð â¡ â1(modð)anâ¡â1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°æ­£æ´æ°ï¼åé¶ä¸æ¯ç¾¤è®ºä¸­çæ¦å¿µï¼é¶ä¸å®å­å¨ï¼åé¶ä¸ä¸å®å­å¨ï¼

### å¹çå¾ªç¯ç»æ

å©ç¨é¶ï¼å¯ä»¥å»ç»å¹çå¾ªç¯ç»æï¼å¯¹äºå¹ ððmodðanmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å°ææ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹é¶ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¸¦ä½é¤æ³ï¼

ð=ð¿ð(ð)ð+ð,Â 0â¤ð<ð¿ð(ð).n=Î´m(a)q+r,Â 0â¤r<Î´m(a).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿èï¼å©ç¨å¹çè¿ç®å¾ï¼å°±å¾å°

ðð=ðð¿ð(ð)ð+ð=(ðð¿ð(ð))ðâ ððâ¡ðð(modð).an=aÎ´m(a)q+r=(aÎ´m(a))qâ arâ¡ar(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æï¼å¯¹äºä»»æææ°çå¹ï¼å¯ä»¥å°å®å¹³ç§»å°ç¬¬ä¸ä¸ªéè´çå¾ªç¯èï¼ç±æ­¤ï¼å¯ä»¥å¾å°ä¸ç³»åå ³äºé¶çæ§è´¨ï¼

æ§è´¨ 1

å¯¹äº ð âð,ð âð+aâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹æ¬¡ ð0( =1),ð,ð2,â¯,ðð¿ð(ð)â1a0(=1),a,a2,â¯,aÎ´m(a)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤ä¸åä½ï¼

è¯æ

èèåè¯ï¼åè®¾å­å¨ä¸¤ä¸ªæ° 0 â¤ð <ð <ð¿ð(ð)0â¤i<j<Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ ðð â¡ðð(modð)aiâ¡aj(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ððâð â¡1(modð)ajâiâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼0 <ð âð <ð¿ð(ð)0<jâi<Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸é¶çæå°æ§çç¾ï¼æ åå½é¢æç«ï¼

æ§è´¨ 2

å¯¹äº ð,ð âð,ð âð+a,nâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½å ³ç³» ðð â¡1(modð)anâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼å½ä¸ä» å½ ð¿ð(ð) â£ðÎ´m(a)â£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¦åææè¿°ï¼ðð â¡ððmodð¿ð(ð)(modð)anâ¡anmodÎ´m(a)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± æ§è´¨ 1 å¯ç¥ï¼0 â¤ð <ð¿ð(ð)0â¤r<Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å¯ä¸ä¸ä¸ªä½¿å¾ ðð â¡1(modð)arâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ç ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ ð =0r=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ðð â¡1(modð)anâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ä¸ä» å½ ðmodð¿ð(ð) =0nmodÎ´m(a)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯ ð¿ð(ð) â£ðÎ´m(a)â£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

[æ¬§æå®ç](../fermat/#æ¬§æå®ç) ä¸­ï¼åä½å ³ç³» ðð(ð) â¡1(modð)aÏ(m)â¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼ç»å æ§è´¨ 2ï¼è¿è¯´æå¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð¿ð(ð) â£ð(ð)Î´m(a)â£Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¢å¥è¯è¯´ï¼ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶çä¸ä¸ªå ¬åæ°ï¼å¯¹äºä¸ä¸ªæ­£æ´æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å ¬åæ°ï¼è®°ä½ ð(ð)Î»(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ¯ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Carmichael å½æ°ï¼åæä¼è¯¦ç»è®¨è®ºå®çæ§è´¨ï¼

åå ¶ä»çå¾ªç¯ç»æç±»ä¼¼ï¼å¯ä»¥æ ¹æ® ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶è®¡ç® ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ï¼

æ§è´¨ 3

å¯¹äº ð,ð âð,ð âð+k,aâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð¿ð(ðð)=ð¿ð(ð)(ð¿ð(ð),ð).Î´m(ak)=Î´m(a)(Î´m(a),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

ç± æ§è´¨ 2ï¼åä½å ³ç³» (ðð)ð =ððð â¡1(modð)(ak)n=aknâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼å½ä¸ä» å½ ð¿ð(ð) â£ððÎ´m(a)â£kn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ¡ä»¶å°±ç­ä»·äº

ð¿ð(ð)(ð¿ð(ð),ð)â£ð.Î´m(a)(Î´m(a),k)â£n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½¿å¾è¿ä¸æ¡ä»¶æç«çæå°æ­£æ´æ°å°±æ¯

ð¿ð(ðð)=ð¿ð(ð)(ð¿ð(ð),ð).Î´m(ak)=Î´m(a)(Î´m(a),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ä¹ç§¯çé¶

è®¾ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çä¸åæ´æ°ï¼å¦æå·²ç¥é¶ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿ð(ð)Î´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼åæ ·å¯ä»¥è·å¾ä¸äºå ³äºå®ä»¬ä¹ç§¯ ððab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ ð¿ð(ðð)Î´m(ab)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¿¡æ¯ï¼

æ§è´¨ 4

å¯¹äº ð,ð âð,ð âð+a,bâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð,ð âða,bâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ

[ð¿ð(ð),ð¿ð(ð)](ð¿ð(ð),ð¿ð(ð))â£ð¿ð(ðð)â£[ð¿ð(ð),ð¿ð(ð)].[Î´m(a),Î´m(b)](Î´m(a),Î´m(b))â£Î´m(ab)â£[Î´m(a),Î´m(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å ä¸º [ð¿ð(ð),ð¿ð(ð)][Î´m(a),Î´m(b)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿ð(ð)Î´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼æä»¥ï¼ç± æ§è´¨ 2 å¯ç¥

(ðð)[ð¿ð(ð),ð¿ð(ð)]=ð[ð¿ð(ð),ð¿ð(ð)]ð[ð¿ð(ð),ð¿ð(ð)]â¡1(modð).(ab)[Î´m(a),Î´m(b)]=a[Î´m(a),Î´m(b)]b[Î´m(a),Î´m(b)]â¡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ¬¡åºç¨æ§è´¨ 2ï¼å°±å¾å°

ð¿ð(ðð)â£[ð¿ð(ð),ð¿ð(ð)].Î´m(ab)â£[Î´m(a),Î´m(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±å¾å°å³ä¾§çæ´é¤å ³ç³»ï¼

åè¿æ¥ï¼ç±äº

1â¡(ðð)ð¿ð(ðð)ð¿ð(ð)â¡ðð¿ð(ðð)ð¿ð(ð)(modð),1â¡(ab)Î´m(ab)Î´m(b)â¡aÎ´m(ab)Î´m(b)(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼åºç¨æ§è´¨ 2ï¼å°±å¾å° ð¿ð(ð) â£ð¿ð(ðð)ð¿ð(ð)Î´m(a)â£Î´m(ab)Î´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¤ä¾§æ¶å» (ð¿ð(ð),ð¿ð(ð))(Î´m(a),Î´m(b))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°

ð¿ð(ð)(ð¿ð(ð),ð¿ð(ð))â£ð¿ð(ðð)ð¿ð(ð)(ð¿ð(ð),ð¿ð(ð)).Î´m(a)(Î´m(a),Î´m(b))â£Î´m(ab)Î´m(b)(Î´m(a),Î´m(b)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¶å»å ¬å å­åï¼ä¸¤ä¸ªåå¼äºç´ ï¼è¿å°±å¾å°

ð¿ð(ð)(ð¿ð(ð),ð¿ð(ð))â£ð¿ð(ðð).Î´m(a)(Î´m(a),Î´m(b))â£Î´m(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åçï¼ä¹æ

ð¿ð(ð)(ð¿ð(ð),ð¿ð(ð))â£ð¿ð(ðð).Î´m(b)(Î´m(a),Î´m(b))â£Î´m(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºä¸¤ä¸ªæ´é¤å ³ç³»çå·¦ä¾§äºç´ ï¼æ

[ð¿ð(ð),ð¿ð(ð)](ð¿ð(ð),ð¿ð(ð))=ð¿ð(ð)ð¿ð(ð)(ð¿ð(ð),ð¿ð(ð))2â£ð¿ð(ðð).[Î´m(a),Î´m(b)](Î´m(a),Î´m(b))=Î´m(a)Î´m(b)(Î´m(a),Î´m(b))2â£Î´m(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±å¾å°å·¦ä¾§çæ´é¤å ³ç³»ï¼

å¯¹äº ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶äºç´ çæ å½¢ï¼è¿ä¸ç»è®ºæçæ´ä¸ºç®åçå½¢å¼ï¼

æ§è´¨ 4'

å¯¹äº ð,ð âð,ð âð+a,bâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð,ð âða,bâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ

ð¿ð(ðð)=ð¿ð(ð)ð¿ð(ð)âºð¿ð(ð)âð¿ð(ð).Î´m(ab)=Î´m(a)Î´m(b)âºÎ´m(a)âÎ´m(b).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å¦æ ð¿ð(ð) âð¿ð(ð)Î´m(a)âÎ´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ æ§è´¨ 4 ä¸­æææ´é¤å ³ç³»é½æ¯ç­å¼ï¼æä»¥æ

ð¿ð(ðð)=[ð¿ð(ð),ð¿ð(ð)]=ð¿ð(ð)ð¿ð(ð).Î´m(ab)=[Î´m(a),Î´m(b)]=Î´m(a)Î´m(b).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åè¿æ¥ï¼å¦æ ð¿ð(ðð) =ð¿ð(ð)ð¿ð(ð)Î´m(ab)=Î´m(a)Î´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ ¹æ®æ§è´¨ 4ï¼å°±æ

ð¿ð(ð)ð¿ð(ð)=ð¿ð(ðð)â£[ð¿ð(ð),ð¿ð(ð)].Î´m(a)Î´m(b)=Î´m(ab)â£[Î´m(a),Î´m(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ç«é©¬è¯´æ (ð¿ð(ð),ð¿ð(ð)) =1(Î´m(a),Î´m(b))=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð¿ð(ð) âð¿ð(ð)Î´m(a)âÎ´m(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸è¬æ å½¢ä¸­ï¼æ§è´¨ 4 å¾å°ççå·²ç»æ¯ç´§çï¼ä¹ç§¯çé¶åå¾ä¸ççæ å½¢å¾å®¹ææé ï¼ä¾å¦ (ð,ð,ð) =(3,5,7)(a,b,m)=(3,5,7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ð¿ð(ð) =ð¿ð(ð) =6Î´m(a)=Î´m(b)=6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯å®ä»¬çä¹ç§¯çé¶ ð¿ð(ðð) =1Î´m(ab)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å°½ç®¡ä¸è¬æ å½¢ä¸­ï¼ä¹ç§¯ ððab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶æªå¿ æ¯å®ä»¬çé¶çæå°å ¬åæ°ï¼ä½æ¯æ»è½æ¾å°ä¸ä¸ªå ç´ ä½¿å¾å®çé¶ç­äºè¿ä¸ªæå°å ¬åæ°ï¼

æ§è´¨ 5

å¯¹äº ð,ð âð,ð âð+a,bâZ,mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð,ð âða,bâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»æ¯å­å¨ ð âðcâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðcâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ð¿ð(ð)=[ð¿ð(ð),ð¿ð(ð)].Î´m(c)=[Î´m(a),Î´m(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

èèç´ å æ°åè§£ï¼

ð¿ð(ð)=âððð¼ð,Â ð¿ð(ð)=âððð½ð.Î´m(a)=âppÎ±p,Â Î´m(b)=âppÎ²p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨ ð¼ðÎ±p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð½ðÎ²p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°å ³ç³»ï¼å¯ä»¥å°ææç´ å å­åä¸ºä¸¤ç±»ï¼

ð´={ð:ð¼ðâ¥ð½ð},Â ðµ={ð:ð¼ð<ð½ð}.A={p:Î±pâ¥Î²p},Â B={p:Î±p<Î²p}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ­¤ï¼åå«è®¾

ð¾ð´=âðâð´ðð¼ð,Â ð¾ðµ=âðâðµðð¼ð,Â ðð´=âðâð´ðð½ð,Â ððµ=âðâðµðð½ð,Î³A=âpâApÎ±p,Â Î³B=âpâBpÎ±p,Â Î·A=âpâApÎ²p,Â Î·B=âpâBpÎ²p,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±æ ð¿ð(ð) =ð¾ð´ð¾ðµÎ´m(a)=Î³AÎ³B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿ð(ð) =ðð´ððµÎ´m(b)=Î·AÎ·B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ® æ§è´¨ 3ï¼å¯ç¥

ð¿ð(ðð¾ðµ)=ð¿ð(ð)(ð¿ð(ð),ð¾ðµ)=ð¿ð(ð)ð¾ðµ=ð¾ð´,ð¿ð(ððð´)=ð¿ð(ð)(ð¿ð(ð),ðð´)=ð¿ð(ð)ðð´=ððµ.Î´m(aÎ³B)=Î´m(a)(Î´m(a),Î³B)=Î´m(a)Î³B=Î³A,Î´m(bÎ·A)=Î´m(b)(Î´m(b),Î·A)=Î´m(b)Î·A=Î·B.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð¾ð´ âððµÎ³AâÎ·B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± æ§è´¨ 4'ï¼å°±æ

ð¿ð(ðð¾ðµððð´)=ð¾ð´ððµ=âððmax{ð¼ð,ð½ð}=[ð¿ð(ð),ð¿ð(ð)].Î´m(aÎ³BbÎ·A)=Î³AÎ·B=âppmax{Î±p,Î²p}=[Î´m(a),Î´m(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ð =ðð¾ðµððð´c=aÎ³BbÎ·A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯é¶ä¸º [ð¿ð(ð),ð¿ð(ð)][Î´m(a),Î´m(b)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ç´ ï¼

è¿ä¸ç»è®ºå¸¸ç¨äºæé åºæå®é¶çå ç´ ï¼

## åæ ¹

åæ ¹æ¯ä¸äºç¹æ®å ç´ ââå®çé¶å°±ç­äºæææ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»çä¸ªæ°ï¼

åæ ¹

å¯¹äº ð âð+mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå­å¨ ð âðgâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðgâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð¿ð(ð) =|ðâð| =ð(ð)Î´m(g)=|Zmâ|=Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç§° ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹**ï¼primitive root modulo ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å ¶ä¸­ï¼ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ [æ¬§æå½æ°](../euler-totient/)ï¼

å¹¶éæææ­£æ´æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å­å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼ç±ä¸æç æ§è´¨ 1ï¼å¦ææ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼é£ä¹ï¼ð,ð2,â¯,ðð(ð)g,g2,â¯,gÏ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¨çåä½ç±»äºä¸ç¸åï¼æææ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»ï¼ç¹å«å°ï¼å¯¹äºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ° ððmodðgimodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äº ð =1,2,â¯,ð â1i=1,2,â¯,pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤ä¸åï¼

æ³¨

å¨ [æ½è±¡ä»£æ°](../../algebra/ring-theory/#åºç¨æ´æ°åä½ç±»çä¹æ³ç¾¤) ä¸­ï¼åæ ¹å°±æ¯å¾ªç¯ç¾¤ççæå ï¼è¿ä¸ªæ¦å¿µåªå¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»å ³äºä¹æ³å½¢æçç¾¤ä¸­æãåæ ¹ãè¿ä¸ªåå­ï¼å¨ä¸è¬çå¾ªç¯ç¾¤ä¸­é½ç§°ä½ãçæå ãï¼å¹¶éæ¯ä¸ªæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»å ³äºä¹æ³å½¢æçç¾¤é½æ¯å¾ªç¯ç¾¤ï¼å­å¨åæ ¹å°±è¡¨æå®åæäºå¾ªç¯ç¾¤ï¼å¦æä¸å­å¨åæ ¹å°±è¡¨æä¸åæï¼

æ¨¡ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ¨¡ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°ä¹æ³ç¾¤å°±æ¯ {0}{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¾ç¶æ¯å¾ªç¯ç¾¤ï¼æä»¥åæ ¹å°±æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### åæ ¹å¤å®å®ç

å¦æå·²ç¥æ¨¡æ° ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½ç´ å å­ï¼é£ä¹å¾å®¹æå¤æ­æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹æ¯å¦å­å¨ï¼

å®ç

å¯¹äºæ´æ° ð â¥3mâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âðgâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼å½ä¸ä» å½å¯¹äº ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ªç´ å æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

ðð(ð)ðâ¢1(modð).gÏ(m)pâ¢1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å¿ è¦æ§æ¾ç¶ï¼ä¸ºè¯æå åæ§ï¼èèä½¿ç¨åè¯æ³ï¼å¦æ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼é£ä¹ä¸å®æ ð¿ð(ð) <ð(ð)Î´m(g)<Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± æ§è´¨ 2 åæ¬§æå®çå¯ç¥ï¼ð¿ð(ð) â£ð(ð)Î´m(g)â£Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼è®¾ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð(ð)ð¿ð(ð)Ï(m)Î´m(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªç´ å å­ï¼å°±æ ð¿ð(ð) â£ð(ð)ðÎ´m(g)â£Ï(m)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¬¡åºç¨æ§è´¨ 2 å°±å¾å°

ðð(ð)ðâ¡1(modð).gÏ(m)pâ¡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯ ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå å­ï¼è¿å°±ä¸é¢è®¾æ¡ä»¶çç¾ï¼ç±æ­¤ï¼åå½é¢çå åæ§æç«ï¼

### åæ ¹ä¸ªæ°

åæ ¹å¦æå­å¨ï¼ä¹æªå¿ å¯ä¸ï¼ä¸è¬å°ï¼å¯¹äºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»ä¸­ææå ç´ å¯è½çé¶åæä¸ªé¶çå ç´ æ°éï¼æå¦ä¸ç»è®ºï¼

å®ç

å¦ææ­£æ´æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å½ä¸ä» å½ ð â£ð(ð)dâ£Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ å­å¨ï¼ä¸æ°æ ð(ð)Ï(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼ç¹å«å°ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ä¸ªæ°ä¸º ð(ð(ð))Ï(Ï(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

æ ¹æ®åæ ¹çå®ä¹ï¼æææ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¢çº¦åä½ç±»é½å¯ä»¥åä½ ððmodðgkmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼ä¸ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ 1,2,â¯,ð(ð)1,2,â¯,Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ï¼ç± æ§è´¨ 3ï¼è¿äºå ç´ çé¶ç­äº

ð¿ð(ðð)=ð(ð)(ð(ð),ð).Î´m(gk)=Ï(m)(Ï(m),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ å­å¨ï¼å½ä¸ä» å½ ð â£ð(ð)dâ£Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ï¼å¯¹äº ð â£ð(ð)dâ£Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ðâ² =ð(ð)/ðdâ²=Ï(m)/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿äºå ç´ çéåå°±æ¯

ð´={ðð:(ð(ð),ð)=ðâ²,Â 1â¤ðâ¤ð(ð)}={ðð:ðâ²â£ð,Â (ð,ð/ðâ²)=1,Â 1â¤ð/ðâ²â¤ð}.A={gk:(Ï(m),k)=dâ²,Â 1â¤kâ¤Ï(m)}={gk:dâ²â£k,Â (d,k/dâ²)=1,Â 1â¤k/dâ²â¤d}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿äºå ç´ å¯¹åºç ðâ² =ð/ðâ²kâ²=k/dâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°ä¸ºé£äºä¸è¶ è¿ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çæ­£æ´æ°ï¼ç±æ¬§æå½æ°çå®ä¹ï¼è¿å°±æ¯ ð(ð)Ï(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### åæ ¹å­å¨å®ç

æ¬èå°å»ºç«å¦ä¸åæ ¹å­å¨å®çï¼

å®ç

æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼å½ä¸ä» å½ ð =1,2,4,ðð,2ððm=1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ä¸ ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºè¯´æè¿ä¸ç»è®ºï¼éè¦åå«è®¨è®ºå¦ä¸åç§æ å½¢ï¼

  1. ð =1,2,4m=1,2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ¹åå«æ¯ ð =0,1,3g=0,1,3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶å­å¨ï¼

  2. ð =ððm=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°çå¹ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥ç´ æ°ï¼ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¼ç 1

å¯¹äºå¥ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼

è¯æ

è¯æåä¸ºä¸¤æ­¥ï¼

**ç¬¬ä¸æ­¥** ï¼å¯¹äº ð â£(ð â1)dâ£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä½æ¹ç¨ ð¥ð â¡1(modð)xdâ¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°æ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçè§£ï¼

ä»¤ ð â1 =ððpâ1=kd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤é¡¹å¼

ð(ð¥)=ð¥ð(ðâ1)+ð¥ð(ðâ2)+â¯+ð¥ð+1.f(x)=xd(kâ1)+xd(kâ2)+â¯+xd+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ® [æ¬§æå®ç](../fermat/#æ¬§æå®ç)ï¼åä½æ¹ç¨ (ð¥ð â1)ð(ð¥) =ð¥ðâ1 â1 â¡0(modð)(xdâ1)f(x)=xpâ1â1â¡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°æ ð â1pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçè§£ï¼è¿äºè§£åå«æ¯ ð¥ð â1xdâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð(ð¥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ç¹ï¼ç± [Lagrange å®ç](../congruence-equation/#å®ç-3lagrange-å®ç)ï¼å®ä»¬åå«è³å¤åªè½æ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ð(ð â1)d(kâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçé¶ç¹ï¼ç±äº ð +ð(ð â1) =ð â1d+d(kâ1)=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè åªè½æ°å¥½æ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçé¶ç¹ï¼è¿è¯´æåä½æ¹ç¨ ð¥ð â¡1(modð)xdâ¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°æ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçè§£ï¼

**ç¬¬äºæ­¥** ï¼å¯¹äº ð â£(ð â1)dâ£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ æ°å¥½æ ð(ð)Ï(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼

å¯¹äº ð(ð)Ï(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå å­æåºï¼ç¶ååºç¨å½çº³æ³ï¼å ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ åªè½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªæä¸ä¸ªï¼å½çº³èµ·ç¹æç«ï¼å¯¹äº ð â£(ð â1)dâ£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®åæç æ§è´¨ 2ï¼åä½æ¹ç¨ ð¥ð â¡1(modð)xdâ¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ä¸å®æ»¡è¶³ ð¿ð(ð¥) â£ðÎ´p(x)â£d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å ¶ä¸­ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ ä¸ªæ°ä¸º

ð(ð)=ðââðâ£ð,Â ðâ ðð(ð)=ðââðâ£ð,Â ðâ ðð(ð)=ð(ð).N(d)=dââeâ£d,Â eâ dN(e)=dââeâ£d,Â eâ dÏ(e)=Ï(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¬¬äºä¸ªç­å·æ¯å½çº³åè®¾ï¼ç¬¬ä¸ä¸ªç­å·æ¯æ¬§æå½æ°çæ§è´¨ï¼ç±æ°å­¦å½çº³æ³ï¼å°±ç¥éå¯¹äºææ ð â£(ð â1)dâ£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ°æ ð(ð)Ï(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ ï¼

ç¹å«å°ï¼å¯¹äº ð =ð â1d=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ°æ ð(ð â1)Ï(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª (ð â1)(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ ï¼å æ­¤ï¼æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼

å¼ç 2

å¯¹äºå¥ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¨¡ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼

è¯æ

è¯æåä¸ºä¸æ­¥ï¼

**ç¬¬ä¸æ­¥** ï¼å­å¨æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ððâ1 â¢1(modð2)gpâ1â¢1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»»åä¸ä¸ªæ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå®ä¸ç¬¦åæ¡ä»¶ï¼å³ ððâ1 â¡1(modð2)gpâ1â¡1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯ä»¥è¯æ ð +ðg+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¦åæ¡ä»¶ï¼ð +ðg+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼ä¸

(ð+ð)ðâ1â¡(ðâ10)ððâ1+(ðâ11)ððâ2ð=ððâ1+ððâ2ð(ðâ1)â¡1âðððâ2â¢1(modð2).(g+p)pâ1â¡(pâ10)gpâ1+(pâ11)gpâ2p=gpâ1+gpâ2p(pâ1)â¡1âpgpâ2â¢1(modp2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**ç¬¬äºæ­¥** ï¼ä¸æéåç ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºä»»æ ð â¥1eâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðð(ðð) â¢1(modðð+1)gÏ(pe)â¢1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¿è¯äº ð =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è¯¥å¼æç«ï¼åè®¾è¯¥å¼å¯¹äº ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢æç«ï¼ç°è¦è¯æ ð +1e+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ä¹æç«ï¼å¯¹äºä»»æ ð â¥1eâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ¬§æå®çå¯ç¥ï¼å­å¨ ðÎ»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ðð(ðð)=1+ðððgÏ(pe)=1+Î»pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼ç±å½çº³åè®¾ï¼ð âðÎ»âp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ð(ðð+1) =ðð(ðð)Ï(pe+1)=pÏ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥

ðð(ðð+1)=(ðð(ðð))ð=(1+ððð)ðâ¡1+ððð+1(modðð+2).gÏ(pe+1)=(gÏ(pe))p=(1+Î»pe)pâ¡1+Î»pe+1(modpe+2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»å ð âðÎ»âp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ï¼ðð(ðð+1) â¢1(modðð+2)gÏ(pe+1)â¢1(modpe+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ°å­¦å½çº³æ³å¯ç¥ï¼å½é¢æç«ï¼

**ç¬¬ä¸æ­¥** ï¼ä¸æéåç ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºä»»æ ð â¥1eâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ¯æ¨¡ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼

å¯¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¿è¯äº ð =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å½é¢æç«ï¼åè®¾å½é¢å¯¹äº ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼ç°å¨è¦è¯æå½é¢å¯¹äº ð +1e+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç«ï¼å° ð¿ðð+1(ð)Î´pe+1(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç®è®°ä¸º ð¿Î´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ðð¿ â¡1(modðð+1)gÎ´â¡1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ ç¶ä¹æ ðð¿ â¡1(modðð)gÎ´â¡1(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±å½çº³åè®¾å¯ç¥ï¼ð¿ðð(ð) =ð(ðð)Î´pe(g)=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ç±åæé¶ç æ§è´¨ 2ï¼å°±æ ð(ðð) â£ð¿Ï(pe)â£Î´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç±æ¬§æå®çå¯ç¥ï¼ð¿ â£ð(ðð+1)Î´â£Ï(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼ð(ðð+1) =ðð(ðð)Ï(pe+1)=pÏ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼åªæä¸¤ç§å¯è½ï¼ð¿ =ð(ðð)Î´=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð¿ =ð(ðð+1)Î´=Ï(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼ç¬¬äºæ­¥çç»è®ºè¯´æï¼ðð(ðð) â¢1(modðð+1)gÏ(pe)â¢1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¯è½æ§ ð¿ =ð(ðð)Î´=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸æç«ï¼å¯ä¸çå¯è½æ§å°±æ¯ ð¿ =ð(ðð+1)Î´=Ï(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðð+1pe+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼ç±æ°å­¦å½çº³æ³ï¼å½é¢å¯¹äºææ ð â¥1eâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼

  3. ð =2ððm=2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥ç´ æ°ï¼ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¼ç 3

å¯¹äºå¥ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¨¡ 2ðð2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼

è¯æ

è®¾ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼å ð +ððg+pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯æ¨¡ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼ä¸¤è ä¹é´å¿ ç¶æä¸ä¸ªæ¯å¥æ°ï¼ä¸å¦¨è®¾å®å°±æ¯ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶ï¼(ð,2ðð) =1(g,2pe)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾ ð¿ =ð¿2ðð(ð)Î´=Î´2pe(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éè¦è¯æ ð¿ =ð(2ðð)Î´=Ï(2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ¬§æå®çï¼ð¿ â£ð(2ðð)Î´â£Ï(2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ï¼æ ¹æ®å®ä¹ ðð¿ â¡1(mod2ðð)gÎ´â¡1(mod2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼ðð¿ â¡1(modðð)gÎ´â¡1(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ç±é¶ç æ§è´¨ 2 å ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåå¯ç¥ï¼ð¿ðð(ð) =ð(ðð) â£ð¿Î´pe(g)=Ï(pe)â£Î´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ¬§æå½æ°è¡¨è¾¾å¼å¯ç¥ï¼ð(2ðð) =ð(ðð)Ï(2pe)=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼ð¿ =ð¿2ðð(ð) =ð(ðð)Î´=Î´2pe(g)=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æ ð¿Î´![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ 2ðð2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼

  4. ð â 1,2,4,ðð,2ððmâ 1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥ç´ æ°ï¼ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¼ç 4

åè®¾ ð â 1,2,4mâ 1,2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸å­å¨å¥ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ­£æ´æ° ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð =ððm=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð =2ððm=2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ä¸å­å¨ï¼

è¯æ

å¯¹äº ð =2ðm=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â¥3eâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼ç±äº ð âðgâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¸å®æ¯å¥æ°ï¼åè®¾ ð =2ð +1g=2k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðkâN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ

ð2ðâ2=(2ð+1)2ðâ2â¡1+(2ðâ21)(2ð)+(2ðâ22)(2ð)2=1+2ðâ1ð+2ðâ1(2ðâ2â1)ð2=1+2ðâ1(ð+(2ðâ2â1)ð2)â¡1(mod2ð).g2eâ2=(2k+1)2eâ2â¡1+(2eâ21)(2k)+(2eâ22)(2k)2=1+2eâ1k+2eâ1(2eâ2â1)k2=1+2eâ1(k+(2eâ2â1)k2)â¡1(mod2e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ°ç¬¬äºè¡ä¸­ï¼å ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ (2ðâ2 â1)ð2(2eâ2â1)k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¥å¶æ§ç¸åï¼æä»¥å®ä»¬çåæ¯å¶æ°ï¼ç±é¶çå®ä¹å¯ç¥ï¼ð¿2ð(ð) â¤2ðâ2 <ð(2ð) =2ðâ1Î´2e(g)â¤2eâ2<Ï(2e)=2eâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸åè®¾ä¸­ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åæ ¹çç¾ï¼ç±åè¯æ³ï¼è¿æ ·çåæ ¹å¹¶ä¸å­å¨ï¼

åè®¾ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³æè¿°æ¡ä»¶ï¼ä¸ä¸æ¯ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹ï¼é£ä¹ï¼ä¸å®å­å¨ 2 <ð1 <ð22<m1<m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð1 âð2m1âm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð =ð1ð2m=m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼åè®¾æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼å ä¸º ð âðgâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥å¯¹äº ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð âððgâmi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ¬§æå®çå¯ç¥ï¼

ðð(ðð)â¡1(modðð).gÏ(mi)â¡1(modmi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äº ðð >2mi>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ð(ðð)Ï(mi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°ï¼æä»¥ï¼å¯¹äº ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð12ð(ð1)ð(ð2)â¡1(modðð).g12Ï(m1)Ï(m2)â¡1(modmi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç± [ä¸­å½å©ä½å®ç](../crt/) å¯ç¥

ð12ð(ð1)ð(ð2)â¡1(modð).g12Ï(m1)Ï(m2)â¡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå ä¸º ð(ð) =ð(ð1)ð(ð2)Ï(m)=Ï(m1)Ï(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç±é¶çå®ä¹å¯ç¥

ð¿ð(ð)â¤12ð(ð1)ð(ð2)=12ð(ð)<ð(ð).Î´m(g)â¤12Ï(m1)Ï(m2)=12Ï(m)<Ï(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹çåè®¾çç¾ï¼æ èï¼ç±åè¯æ³ç¥ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ä¸å­å¨ï¼

ç»¼åä»¥ä¸åä¸ªå¼çï¼æä»¬ä¾¿ç»åºäºä¸ä¸ªæ°å­å¨åæ ¹çå è¦æ¡ä»¶ï¼

### æ±åæ ¹çç®æ³

å¯¹äºä»»ä½å­å¨åæ ¹çæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦æ±å¾å®çåæ ¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªéè¦æä¸¾å¯è½çæ­£æ´æ°ï¼å¹¶éä¸ªå¤æ­å®æ¯å¦ä¸ºåæ ¹å³å¯ï¼æä¸¾æ¶ï¼éå¸¸æä¸¤ç§å¤çæ¹å¼ï¼ä»å°å°å¤§éä¸æä¸¾ãéæºçæä¸äºæ­£æ´æ°ï¼è¿ä¸¤ç§æä¸¾æ¹å¼çå®é æçç¸å½ï¼

ä»å°å°å¤§éä¸æä¸¾æ¶ï¼å¾å°çæ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°åæ ¹ ððgm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æä¸¾é¨åçå¤æåº¦åå³äº ððgm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°ï¼å¯¹æ­¤ï¼æå¦ä¸ä¼°è®¡ï¼

  * ä¸ççä¼°è®¡ï¼çå 5å Burgess6è¯æäºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°åæ ¹ ðð =ð(ð0.25+ð)gp=O(p0.25+Ïµ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð >0Ïµ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Cohen, Odoni, and Stothers7å Elliott and Murata8åå«è¯æäºè¯¥ä¼°è®¡å¯¹äºæ¨¡æ° ð2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 2ð22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç«ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ï¼ç±äºå¯¹äº ð >2e>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¨¡ ð2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ 2ð22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çåæ ¹ä¹æ¯æ¨¡ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ 2ðð2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çåæ ¹ï¼æä»¥ï¼æå°åæ ¹çä¸ç ð(ð0.25+ð)O(p0.25+Ïµ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºæææ å½¢é½æç«ï¼
  * ä¸ççä¼°è®¡ï¼Fridlander9å SaliÃ©10è¯æäºå­å¨ ð¶ >0C>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾å¯¹äºæ ç©·å¤ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½ææå°åæ ¹ ðð >ð¶logâ¡ðgp>Clogâ¡p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼
  * å¹³åæ å½¢çä¼°è®¡ï¼Burgess and Elliott11è¯æäºå¹³åæ å½¢ä¸ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°åæ ¹ ðð =ð((logâ¡ð)2(logâ¡logâ¡ð)4)gp=O((logâ¡p)2(logâ¡logâ¡p)4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Elliott and Murata12è¿ä¸æ­¥çæ³ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°åæ ¹çå¹³åå¼æ¯ä¸ä¸ªå¸¸æ°ï¼ä¸éè¿æ°å¼éªè¯13å¾å°å®å¤§æ¦ä¸º 4.9264.926![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éåï¼Elliott and Murata8å°è¿ä¸çæ³æ¨å¹¿å°æ¨¡ 2ð22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

æ ¹æ®è¿äºåæï¼æ´åå¯»æ¾æå°åæ ¹æ¶ï¼æä¸¾é¨åçå¤æåº¦ ð(ðð(logâ¡ð)2)O(gm(logâ¡m)2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯ä»¥æ¥åçï¼

é¤äºä»å°å°å¤§æä¸¾å¤ï¼è¿å¯ä»¥éè¿éæºçææ­£æ´æ°å¹¶éªè¯çæ¹æ³å¯»æ¾åæ ¹ï¼åæ ¹çå¯åº¦å¹¶ä¸ä½ï¼1

ð(ð(ð))ð=Î©(1logâ¡logâ¡ð).Ï(Ï(m))m=Î©(1logâ¡logâ¡m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼éè¿éæºæ¹æ³å¯»æ¾åæ ¹æ¶ï¼æä¸¾é¨åçææå¤æåº¦ä¸º ð((logâ¡ð)2logâ¡logâ¡ð)O((logâ¡m)2logâ¡logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

éè¦æ³¨æçæ¯ï¼å¤å®åæ ¹æ¶éè¦å·²ç¥ ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè´¨å æ°åè§£ï¼ç®æ³ç«èµ [å¸¸ç¨è´¨å æ°åè§£ç®æ³](../pollard-rho/) ä¸­ï¼å¤æåº¦æä¼ç Pollard Rho ç®æ³ä¹éè¦ ð(ð1/4+ð)O(m1/4+Îµ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´ï¼å æ­¤ï¼åªè¦ ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè´¨å æ°åè§£æ¯æªç¥çï¼æ è®ºéç¨åªç§æä¸¾æ¹å¼ï¼æ±åæ ¹çå¤æåº¦ç¶é¢é½å¨äºè´¨å æ°åè§£è¿ä¸æ­¥ï¼èéæä¸¾éªè¯çé¨åï¼

## Carmichael å½æ°

ç¸å¯¹äºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ç´ çé¶è¿ä¸å±é¨æ¦å¿µï¼Carmichael å½æ°æ¯ä¸ä¸ªå ¨å±æ¦å¿µï¼å®æ¯ææä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çæ´æ°çå¹æ¬¡çæå°å ¬å ±å¾ªç¯èï¼

Carmichael å½æ°

å¯¹äº ð âð+mâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹ ð(ð)Î»(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè½å¤ä½¿å¾åä½å ³ç³» ðð â¡1(modð)anâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«çæå°æ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½æ° ð :ð+ âð+Î»:N+âN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ç§°ä¸º **Carmichael å½æ°** ï¼

æ ¹æ® æ§è´¨ 2ï¼è½å¤ä½¿å¾ ðð â¡1(modð)anâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼æå³ç ð¿ð(ð) â£ðÎ´m(a)â£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼ä¹å°±æ¯è¯´ï¼ç¬¦åè¿ä¸æ¡ä»¶çæ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å®æ¯å ¨ä½ ð¿ð(ð)Î´m(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¬åæ°ï¼å æ­¤ï¼æå°çè¿æ ·ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯å®ä»¬çæå°å ¬åæ°ï¼

ð(ð)=lcmâ¡{ð¿ð(ð):ðâð}.Î»(m)=lcmâ¡{Î´m(a):aâm}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¹å¸¸ç¨ä½ Carmichael å½æ°çç­ä»·å®ä¹ï¼

åå¤åºç¨ æ§è´¨ 5 å¯ç¥ï¼ä¸å®å­å¨æä¸ªå ç´ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð¿ð(ð) =ð(ð)Î´m(a)=Î»(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ä¸å¼ä¹å¯ä»¥åä½

ð(ð)=max{ð¿ð(ð):ðâð}.Î»(m)=max{Î´m(a):aâm}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¾è¿ä¸æå¼çå ç´ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ç§°ä¸ºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ð Î»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)âåæ ¹**ï¼å®å¯¹äºæææ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å­å¨ï¼

### éæ¨å ¬å¼

Carmichael å½æ°æ¯ä¸ä¸ª [æ°è®ºå½æ°](../basic/#æ°è®ºå½æ°)ï¼æ¬èè®¨è®ºå®çä¸ä¸ªéæ¨å ¬å¼ï¼å¹¶ç±æ­¤ç»åºåæ ¹å­å¨å®ççå¦ä¸ä¸ªè¯æï¼

è½ç¶ä¸æ¯ç§¯æ§å½æ°ï¼ä½æ¯è®¡ç® Carmichael å½æ°æ¶ï¼åæ ·å¯ä»¥å¯¹äºç´ çå å­åå«å¤çï¼

å¼ç

å¯¹äºäºç´ çæ­£æ´æ° ð1,ð2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð1ð2) =[ð(ð1),ð(ð2)]Î»(m1m2)=[Î»(m1),Î»(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®¾ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«ä¸ºæ¨¡ ð1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ ð2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ðÎ»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)âåæ ¹ï¼ä»¤ ð =ð1ð2m=m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± [ä¸­å½å©ä½å®ç](../crt/) å¯ç¥ï¼å­å¨ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð â¡ðð(modðð)aâ¡ai(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äº ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼ç±äº ðð(ð) â¡1(modð)aÎ»(m)â¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥å¯¹äº ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðð(ð)ð â¡1(modðð)aiÎ»(m)â¡1(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿èç± æ§è´¨ 2 å ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåå¯ç¥ï¼ð(ðð) =ð¿ðð(ðð) â£ð(ð)Î»(mi)=Î´mi(ai)â£Î»(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æ [ð(ð1),ð(ð2)] â£ð(ð)[Î»(m1),Î»(m2)]â£Î»(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åè¿æ¥ï¼å¯¹äºä»»æ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð[ð(ð1),ð(ð2)] â¡1(modðð)a[Î»(m1),Î»(m2)]â¡1(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºç¨ä¸­å½å©ä½å®çï¼å°±å¾å° ð[ð(ð1),ð(ð2)] â¡1(modð)a[Î»(m1),Î»(m2)]â¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼æ ¹æ® Carmichael å½æ°çå®ä¹å¯ç¥ï¼ð(ð) â£[ð(ð1),ð(ð2)]Î»(m)â£[Î»(m1),Î»(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±æ­¤ï¼å½é¢ä¸­çç­å¼æç«ï¼

å æ­¤ï¼æ¥ä¸æ¥åªè¦è®¡ç® Carmichael å½æ°å¨ç´ æ°å¹å¤çåå¼ï¼é¦å ï¼å¤ç 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡çæ å½¢ï¼

å¼ç

å¯¹äº ð =2ðm=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(2) =1Î»(2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(4) =2Î»(4)=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¯¹äº ð â¥3eâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ ð(ð) =2ðâ2Î»(m)=2eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¯¹äº ð =2,4m=2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼åç¬è®¨è®ºå³å¯ï¼å¯¹äº ð =2ðm=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â¥3eâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼é¦å éå¤åæ å¼ç 4 çè¯æçç¬¬ä¸é¨åï¼å°±å¾å° ð(ð) â¤2ðâ2Î»(m)â¤2eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿èï¼åªéè¦è¯æå­å¨ 2ðâ22eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ å³å¯ï¼ä¸ºæ­¤ï¼æ

52ðâ3=(1+22)2ðâ3=1+22Ã2ðâ3=1+2ðâ1â¢1(mod2ð).52eâ3=(1+22)2eâ3=1+22Ã2eâ3=1+2eâ1â¢1(mod2e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æ ð¿ð(5) â¤2ðâ3Î´m(5)â¤2eâ3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå ä¸º ð¿ð(5) â£2ðâ2Î´m(5)â£2eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªè½æ¯ 2ðâ22eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ç´ ï¼è¿å°±è¯´æï¼ð(ð) =2ðâ2Î»(m)=2eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¨è¿ä¸ªå¼ççè¯æè¿ç¨ä¸­ï¼å®é ä¸å¾å°äºå ³äºæ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢çº¦å©ä½ç³»ç»æçå»ç»ï¼

æ¨è®º

è®¾æ¨¡æ°ä¸º 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â¥2eâ¥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ææå¥æ°é½åä½äºå¯ä¸ä¸ä¸ª Â±5ðÂ±5k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½¢å¼çæ´æ°åä½ï¼å ¶ä¸­ï¼ð âðkâN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð <2ðâ2k<2eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼Â±1, Â±5,â¯, Â±52ðâ2â1Â±1,Â±5,â¯,Â±52eâ2â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤ä¸åä½ï¼ä¸ææä¸ä¸ªæ¢çº¦å©ä½ç³»ï¼

è¯æ

å®¹æéªè¯ï¼ð =2e=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢æç«ï¼å¯¹äº ð â¥3eâ¥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼ç±äºåè¿°è¯æä¸­å·²ç»å¾å° 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶æ¯ 2ðâ22eâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼1,5,â¯,52ðâ2â11,5,â¯,52eâ2â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤ä¸åä½ï¼å ä¸ºè¿äºæ´æ°é½æ¨¡ 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬çç¸åæ°é½æ¨¡ 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ Â±1, Â±5,â¯, Â±52ðâ2â1Â±1,Â±5,â¯,Â±52eâ2â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤ä¸åä½ï¼ç±äºå®ä»¬å ±è®¡ 2ðâ12eâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼æ°ä¸ºæ¨¡ 2ð2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¢çº¦å©ä½ç³»çå¤§å°ï¼æä»¥ï¼å®ä»¬å°±ææäºæ¢çº¦å©ä½ç³»æ¬èº«ï¼

ç¶åï¼å¤çå¥ç´ æ°å¹çæ å½¢ï¼

å¼ç

å¯¹äº ð =ððm=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ä¸ ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) =ððâ1(ð â1)Î»(m)=peâ1(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

é¦å è¯æå½é¢å¯¹äº ð =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð =ðm=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°çæ å½¢æç«ï¼ä¸ºæ­¤ï¼ç± Carmichael å½æ°çå®ä¹å¯ç¥ï¼ä¸ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çæææ´æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯åä½æ¹ç¨ ð¥ð(ð) â¡1(modð)xÎ»(p)â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ï¼å¨æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¹ä¸ï¼è¯¥æ¹ç¨å ±æ ð â1pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºä¸ç¸åçè§£ï¼æ ¹æ® [Lagrange å®ç](../congruence-equation/#å®ç-3lagrange-å®ç) å¯ç¥ï¼ð â1 â¤ð(ð)pâ1â¤Î»(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ï¼æ¬§æå®çè¦æ±ï¼ð(ð) â£ð(ð) =ð â1Î»(p)â£Ï(p)=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ð(ð) =ð â1Î»(p)=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äº ð =ððm=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å¯ä»¥ä»è¯æ 1 +ð1+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ððâ1peâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å å¼å§ï¼ä¸ºæ­¤ï¼æ

(1+ð)ððâ1â¡1,(1+ð)ððâ2â¡1+ððâ1â¢1(modðð).(1+p)peâ1â¡1,(1+p)peâ2â¡1+peâ1â¢1(modpe).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼ð¿ð(1 +ð) =ððâ1Î´m(1+p)=peâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦å¤ï¼è®¾æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ä¸º ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ç±äº ðð¿ð(ð) â¡1(modð)gÎ´m(g)â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼ç±é¶ç æ§è´¨ 2 å¯ç¥ï¼ð â1 â£ð¿ð(ð)pâ1â£Î´m(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± Carmichael å½æ°çå®ä¹åæ¬§æå®çå¯ç¥

ððâ1(ðâ1)=[ð¿ð(ð),ððâ1]â£ð(ð)â£ð(ð)=ððâ1(ðâ1).peâ1(pâ1)=[Î´m(p),peâ1]â£Î»(m)â£Ï(m)=peâ1(pâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ð(ð) =ððâ1(ð â1)Î»(m)=peâ1(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å°æ¬èçç»æç®åå½çº³ï¼å°±å¾å° Carmichael å½æ°çéæ¨å ¬å¼ï¼

å®ç

å¯¹äºä»»ææ­£æ´æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð(ð)=â§{ {â¨{ {â©ð(ð),ifÂ ð=1,2,4,ððÂ for odd primeÂ ðÂ andÂ ðâ¥1,12ð(ð),ifÂ ð=2ð,Â ðâ¥3,lcmâ¡{ð(ðð11),ð(ðð22),â¯,ð(ððð ð )},ifÂ ð=ðð11ðð22â¯ððð ð Â for distinctÂ ð1,ð2,â¯,ðð .Î»(m)={Ï(m),ifÂ m=1,2,4,peÂ for odd primeÂ pÂ andÂ eâ¥1,12Ï(m),ifÂ m=2e,Â eâ¥3,lcmâ¡{Î»(p1e1),Î»(p2e2),â¯,Î»(pses)},ifÂ m=p1e1p2e2â¯psesÂ for distinctÂ p1,p2,â¯,ps.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¯¥éæ¨å ¬å¼å¯ä»¥å å¼ºåæçç»æï¼

æ¨è®º

å¯¹äºæ­£æ´æ° ð1,ð2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð([ð1,ð2]) =[ð(ð1),ð(ð2)]Î»([m1,m2])=[Î»(m1),Î»(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¯è¾åæ ¹å Carmichael å½æ°çå®ä¹å¯ç¥ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼å½ä¸ä» å½ ð(ð) =ð(ð)Î»(m)=Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä» Carmichael å½æ°çéæ¨å ¬å¼ä¸­ï¼å®¹æå½çº³åºå¦ä¸ç»æï¼

æ¨è®º

æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼å½ä¸ä» å½ ð =1,2,4,ðð,2ððm=1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ä¸ ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±äºæ¬èå¯¹äºéæ¨å ¬å¼çè¯æå¹¶æ²¡æç¨å°åæ ¹å­å¨å®çï¼å æ­¤ï¼è¿å°±ææäºå¯¹è¯¥å®ççåä¸ä¸ªè¯æï¼

### Carmichael æ°

å©ç¨ Carmichael å½æ°ï¼å¯ä»¥è®¨è®º Carmichael æ°ï¼å¡è¿å å°æ°ï¼OEIS:[A002997](https://oeis.org/A002997)ï¼çæ§è´¨ä¸åå¸ï¼è¿æ¯ [Fermat ç´ æ§æµè¯](../prime/#fermat-ç´) ä¸å®æ æ³æ­£ç¡®æé¤çåæ°ï¼

Carmichael æ°

å¯¹äºåæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå¯¹äºæææ´æ° ð âðaân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æåä½å¼ ððâ1 â¡1(modð)anâ1â¡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼å°±ç§° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **Carmichael æ°** ï¼

æå°ç Carmichael æ°æ¯ 561 =3 Ã11 Ã17561=3Ã11Ã17![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç± Carmichael å½æ°çå®ä¹å¯ç¥ï¼åæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Carmichael æ°å½ä¸ä» å½ ð(ð) â£ð â1Î»(n)â£nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð(ð)Î»(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º Carmichael å½æ°ï¼è¿ä¸æ­¥å°ï¼å¯ä»¥å¾å°å¦ä¸å¤æ­åæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦ä¸º Carmichael æ°çæ¹æ³ï¼

Korselt å¤å«æ³14

åæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Carmichael æ°å½ä¸ä» å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å¹³æ¹å å­ä¸å¯¹ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä»»æè´¨å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ (ð â1) â£(ð â1)(pâ1)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

é¦å è¯ææ¡ä»¶çå¿ è¦æ§ï¼åè®¾ ð(ð) â£(ð â1)Î»(n)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ£æ¥ Carmichael å½æ°çéæ¨å ¬å¼å¯ç¥ï¼å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¹³æ¹å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ä¸å®æ ð â£ð(ð)pâ£Î»(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ ð â¤(ð â1)pâ¤(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çç¾ï¼åçï¼Carmichael å½æ°çéæ¨å ¬å¼è¯´æï¼(ð â1) â£ð(ð)(pâ1)â£Î»(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼ä¹æ (ð â1) â£(ð â1)(pâ1)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¶åè¯ææ¡ä»¶çå åæ§ï¼å ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åæ°ï¼æä»¥å®ä¸å®æå¥ç´ å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¶æ°ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å°±ä¸å®æ¯å¥æ°ï¼å¯¹äºæ å¹³æ¹å å­çå¥åæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± Carmichael å½æ°çéæ¨å ¬å¼å¯ç¥ï¼ð(ð) =lcmâ¡{ð â1 :ð â£ð}Î»(n)=lcmâ¡{pâ1:pâ£n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼åªè¦ (ð â1) â£(ð â1)(pâ1)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææç´ å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å°±ä¸å®æ ð(ð) â£(ð â1)Î»(n)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»è¿ä¸å¤å«æ³åºåï¼å¯ä»¥å»ºç« Carmichael æ°çä¸äºç®åæ§è´¨ï¼

æ¨è®º

Carmichael æ°æ¯å¥æ°ï¼æ²¡æå¹³æ¹å å­ï¼èä¸è³å°æ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¸åçç´ å å­ï¼

è¯æ

åä¸¤æ¡æ§è´¨å¯ä»¥ç´æ¥ä» Korselt å¤å«æ³åå ¶è¯æä¸­å¾å°ï¼è¦å¾å°ç¬¬ä¸æ¡æ§è´¨ï¼åªéè¦åè¯æï¼äºå¼ç´ æ° ð1,ð2p1,p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹ç§¯ ð =ð1ð2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®ä¸æ¯ Carmichael æ°ï¼åè®¾ ð =ð1ð2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Carmichael æ°ï¼ç± Korselt å¤å«æ³å¯ç¥ï¼(ðð â1) â£(ð â1)(piâ1)â£(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼æ

ðâ1=ð1ð2â1â¡ð2â1(modð1â1).nâ1=p1p2â1â¡p2â1(modp1â1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼(ð1 â1) â£(ð2 â1)(p1â1)â£(p2â1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åçï¼(ð2 â1) â£(ð1 â1)(p2â1)â£(p1â1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ð1 =ð2p1=p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸åè®¾çç¾ï¼å æ­¤ï¼Carmichael æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å°æ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªäºå¼ç´ å å­ï¼

å©ç¨è§£ææ°è®ºè¿å¯ä»¥å¾å° Carmichael æ°åå¸çä¸äºæ§è´¨ï¼è®¾ ð¶(ð)C(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Carmichael æ°ä¸ªæ°ï¼Alford, Granville, and Pomerance2è¯æï¼å¯¹äºå åå¤§ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð¶(ð) >ð2/7C(n)>n2/7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼Carmichael æ°ææ éå¤ä¸ªï¼å¨è¿ä¹åï¼ErdÅs3å·²ç»è¯æï¼ð¶(ð) <ðexpâ¡(âðlnâ¡ðlnâ¡lnâ¡lnâ¡ðlnâ¡lnâ¡ð)C(n)<nexpâ¡(âclnâ¡nlnâ¡lnâ¡lnâ¡nlnâ¡lnâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¸¸æ°ï¼å æ­¤ï¼Carmichael æ°çåå¸ï¼ç¸å¯¹äºç´ æ°æ¥è¯´ï¼ååç¨çï¼å®é ä¸ï¼æ4 ð¶(109) =646C(109)=646![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¶(1018) =1Â 401Â 644C(1018)=1Â 401Â 644![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## åèèµæä¸æ³¨é

  * [Primitive root modulo n - Wikipedia](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
  * [The order of a unit - Course Notes](https://crypto.stanford.edu/pbc/notes/numbertheory/order.html)
  * [The primitive root theorem - Amin Witno's notes](http://witno.com/philadelphia/notes/won5.pdf)
  * [Carmichael function - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_function)
  * [Carmichael's Lambda Function - Brilliant Math & Science Wiki](https://brilliant.org/wiki/carmichaels-lambda-function/)
  * [Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)
  * [Carmichael Number - Wolfram MathWorld](https://mathworld.wolfram.com/CarmichaelNumber.html)

* * *

  1. å¦ææ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹å­å¨ï¼é£ä¹ï¼ð(ð) â¥13ðÏ(m)â¥13m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç­å·ä» å¨ ð =2 Ã3ðÂ (ð âð+)m=2Ã3eÂ (eâN+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤åå¾ï¼è¿ä¸æ­¥å°ï¼å½ ð >2m>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¯¹æ¬§æå½æ° ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¼°è®¡ï¼ð(ð) >ððð¾logâ¡logâ¡ð+3logâ¡logâ¡ðÏ(m)>meÎ³logâ¡logâ¡m+3logâ¡logâ¡m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°è¿ä¸¤è ç»åï¼å°±å¾å°æä¸­çè¡¨è¾¾å¼ï¼å ³äºæ¬§æå½æ°çè¯¥ä¼°è®¡ï¼å¯ä»¥åèè®ºæ Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94ï¼Â â©

  2. W. R. Alford; Andrew Granville; Carl Pomerance (1994). "There are Infinitely Many Carmichael Numbers." Annals of Mathematics. 140 (3): 703â722.Â â©

  3. ErdÅs, P. (1956). "On pseudoprimes and Carmichael numbers." Publ. Math. Debrecen. 4 (3â4): 201â206.Â â©

  4. PINCH, Richard GE. The Carmichael numbers up to 10201020![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).Â â©

  5. Wang Y. "On the least primitive root of a prime." (in Chinese). Acta Math Sinica, 1959, 4: 432â441; English transl. in _Sci. Sinica_ , 1961, 10: 1â14.Â â©

  6. BURGESS, David A. "On character sums and primitive roots." Proceedings of the London Mathematical Society, 1962, 3.1: 179-192.Â â©

  7. Cohen, S. D., R. W. K. Odoni, and W. W. Stothers. "On the least primitive root modulo p 2." Bulletin of the London Mathematical Society 6, no. 1 (1974): 42-46.Â â©

  8. Elliott, P. D. T. A., and L. Murata. "The least primitive root mod 2p2." Mathematika 45, no. 2 (1998): 371-379.Â â©â©

  9. FRIDLENDER, V. R. "On the least n-th power non-residue." Dokl. Akad. Nauk SSSR. 1949. p. 351-352.Â â©

  10. SALIÃ, Hans. "Ãber den kleinsten positiven quadratischen Nichtrest nach einer Primzahl." Mathematische Nachrichten, 1949, 3.1: 7-8.Â â©

  11. Burgess, D. A., and P. D. T. A. Elliott. "The average of the least primitive root." Mathematika 15, no. 1 (1968): 39-50.Â â©

  12. Elliott, Peter DTA, and Leo Murata. "On the average of the least primitive root modulo p." Journal of The london Mathematical Society 56, no. 3 (1997): 435-454.Â â©

  13. æ´å¤ç»æå¯ä»¥åè [Least prime primitive root of prime numbers](https://sweet.ua.pt/tos/p_roots.html)ï¼Â â©

  14. Korselt, A. R. (1899). "ProblÃ¨me chinois." L'IntermÃ©diaire des MathÃ©maticiens. 6: 142â143.Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2025/11/1 11:21:19ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/primitive-root.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/primitive-root.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Peanut-Tang](https://github.com/Peanut-Tang), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [2008verser](https://github.com/2008verser), [Enter-tainer](https://github.com/Enter-tainer), [bobhan1](https://github.com/bobhan1), [CCXXXI](https://github.com/CCXXXI), [chuxin0816](https://github.com/chuxin0816), [CroMarmot](https://github.com/CroMarmot), [GavinZhengOI](https://github.com/GavinZhengOI), [GeorgePlover](https://github.com/GeorgePlover), [hhc0001](https://github.com/hhc0001), [huhaoo](https://github.com/huhaoo), [Larry0716](https://github.com/Larry0716), [Marcythm](https://github.com/Marcythm), [opsiff](https://github.com/opsiff), [ouuan](https://github.com/ouuan), [PeterlitsZo](https://github.com/PeterlitsZo), [ShelpAm](https://github.com/ShelpAm), [tml104](https://github.com/tml104), [wty-yy](https://github.com/wty-yy)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
