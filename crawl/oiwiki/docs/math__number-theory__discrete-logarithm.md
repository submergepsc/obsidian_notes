# ç¦»æ£å¯¹æ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/discrete-logarithm/

# ç¦»æ£å¯¹æ°

## å®ä¹

åç½®ç¥è¯ï¼[é¶ä¸åæ ¹](../primitive-root/)ï¼

ç¦»æ£å¯¹æ°çå®ä¹æ¹å¼åå¯¹æ°ç±»ä¼¼ï¼åæåæ ¹çæ­£æ´æ°æ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å ¶ä¸ä¸ªåæ ¹ä¸º ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å¯¹æ»¡è¶³ (ð,ð) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬ç¥éå¿ å­å¨å¯ä¸çæ´æ° 0 â¤ð <ð(ð)0â¤k<Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ððâ¡ð(modð)gkâ¡a(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬ç§°è¿ä¸ª ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä»¥ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåºï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¦»æ£å¯¹æ°ï¼è®°ä½ ð =indðâ¡ðk=indgâ¡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ä¸å¼èµ·æ··æ·çæ åµä¸å¯è®°ä½ indâ¡ðindâ¡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æ¾ç¶ indðâ¡1 =0indgâ¡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼indðâ¡ð =1indgâ¡g=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## æ§è´¨

ç¦»æ£å¯¹æ°çæ§è´¨ä¹åå¯¹æ°æè¯¸å¤ç±»ä¼¼ä¹å¤ï¼

æ§è´¨

è®¾ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼(ð,ð) =(ð,ð) =1(a,m)=(b,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åï¼

  1. indðâ¡(ðð) â¡indðâ¡ð +indðâ¡ð(modð(ð))indgâ¡(ab)â¡indgâ¡a+indgâ¡b(modÏ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è (âð âð),Â Â indðâ¡ðð â¡ðindðâ¡ð(modð(ð))(ânâN),Â Â indgâ¡anâ¡nindgâ¡a(modÏ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  2. è¥ ð1g1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ¹ï¼å indðâ¡ð â¡indð1â¡ð â indðâ¡ð1(modð(ð))indgâ¡aâ¡indg1â¡aâ indgâ¡g1(modÏ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  3. ð â¡ð(modð) âº indðâ¡ð =indðâ¡ðaâ¡b(modm)âºindgâ¡a=indgâ¡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æ

  1. ðindðâ¡(ðð) â¡ðð â¡ðindðâ¡ððindðâ¡ð â¡ðindðâ¡ð+indðâ¡ð(modð)gindgâ¡(ab)â¡abâ¡gindgâ¡agindgâ¡bâ¡gindgâ¡a+indgâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. ä»¤ ð¥ =indð1â¡ðx=indg1â¡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð â¡ðð¥1(modð)aâ¡g1x(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). åä»¤ ð¦ =indðâ¡ð1y=indgâ¡g1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð1 â¡ðð¦(modð)g1â¡gy(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æ ð â¡ðð¥ð¦(modð)aâ¡gxy(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ indðâ¡ð â¡ð¥ð¦ â¡indð1â¡ð â indðâ¡ð1(modð(ð))indgâ¡aâ¡xyâ¡indg1â¡aâ indgâ¡g1(modÏ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  3. æ³¨æå°

indðâ¡ð=indðâ¡ðâºindðâ¡ðâ¡indðâ¡ð(modð(ð))âºðindðâ¡ðâ¡ðindðâ¡ð(modð)âºðâ¡ð(modð)indgâ¡a=indgâ¡bâºindgâ¡aâ¡indgâ¡b(modÏ(m))âºgindgâ¡aâ¡gindgâ¡b(modm)âºaâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## å¤§æ­¥å°æ­¥ç®æ³

ç®åç¦»æ£å¯¹æ°é®é¢ä»ä¸å­å¨å¤é¡¹å¼æ¶é´ç»å ¸ç®æ³ï¼ç¦»æ£å¯¹æ°é®é¢çè¾å ¥è§æ¨¡æ¯è¾å ¥æ°æ®çä½æ°ï¼ï¼å¨å¯ç å­¦ä¸­ï¼åºäºè¿ä¸ç¹äººä»¬è®¾è®¡äºè®¸å¤éå¯¹ç§°å å¯ç®æ³ï¼å¦ [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519)ï¼

å¨ç®æ³ç«èµä¸­ï¼BSGSï¼baby-step giant-stepï¼å¤§æ­¥å°æ­¥ç®æ³ï¼å¸¸ç¨äºæ±è§£ç¦»æ£å¯¹æ°é®é¢ï¼å½¢å¼åå°è¯´ï¼å¯¹ ð,ð,ð âð+a,b,mâZ+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥ç®æ³å¯ä»¥å¨ ð(âð)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å æ±è§£

ðð¥â¡ð(modð)axâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¹ç¨çè§£ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ 0 â¤ð¥ <ð0â¤x<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).ï¼æ³¨æ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸å®æ¯ç´ æ°ï¼

### ç®æ³æè¿°

ä»¤ ð¥ =ð´ââðâ âðµx=AâmââB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ 0 â¤ð´,ðµ â¤ââðâ0â¤A,Bâ¤âmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ðð´ââðââðµ â¡ð(modð)aAâmââBâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨å åæ¢ï¼åæ ðð´ââðâ â¡ðððµ(modð)aAâmââ¡baB(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æä»¬å·²ç¥çæ¯ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æä»¬å¯ä»¥å ç®åºç­å¼å³è¾¹ç ðððµbaB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææåå¼ï¼æä¸¾ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨ `hash`/`map` å­ä¸æ¥ï¼ç¶åéä¸è®¡ç® ðð´ââðâaAâmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¸¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯»æ¾æ¯å¦æä¸ä¹ç¸ç­ç ðððµbaB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»èæä»¬å¯ä»¥å¾å°ææç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¥ =ð´ââðâ âðµx=AâmââB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æ³¨æå° ð´,ðµA,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå°äº ââðââmâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æ¶é´å¤æåº¦ä¸º Î(âð)Î(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¨ `map` åå¤ä¸ä¸ª loglog![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

ä¸ºä»ä¹è¦æ± ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè´¨

æ³¨æå°æä»¬æ±åºçæ¯ ð´,ðµA,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬éè¦ä¿è¯ä» ðð´ââðâ â¡ðððµ(modð)aAâmââ¡baB(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥æ¨å ðð´ââðââðµ â¡ð(modð)aAâmââBâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¼æ¯åå¼å·¦å³ä¸¤è¾¹é¤ä»¥ ððµaB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°ï¼æä»¥å¿ é¡»æ ððµ âðaBâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ ð âðaâm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## æ©å± BSGS ç®æ³

å¯¹ ð,ð,ð âð+a,b,mâZ+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±è§£

ðð¥â¡ð(modð)axâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ð,ða,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸å®äºè´¨ï¼

å½ (ð,ð) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨éå ï¼å æ­¤å¯ä»¥ä½¿ç¨ BSGS ç®æ³æ±è§£ï¼äºæ¯æä»¬æ³åæ³è®©ä»ä»¬åå¾äºè´¨ï¼

å ·ä½å°ï¼è®¾ ð1 =(ð,ð)d1=(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å¦æ ð1 â¤ðd1â¤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ååæ¹ç¨æ è§£ï¼å¦åæä»¬ææ¹ç¨åæ¶é¤ä»¥ ð1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å°

ðð1â ðð¥â1â¡ðð1(modðð1)ad1â axâ1â¡bd1(modmd1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð1md1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»ä¸äºè´¨å°±åé¤ï¼è®¾ ð2 =(ð,ðð1)d2=(a,md1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å¦æ ð2 â¤ðð1d2â¤bd1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¹ç¨æ è§£ï¼å¦ååæ¶é¤ä»¥ ð2d2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°

ð2ð1ð2â ðð¥â2â¡ðð1ð2(modðð1ð2)a2d1d2â axâ2â¡bd1d2(modmd1d2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åçï¼è¿æ ·ä¸åçå¤æ­ä¸å»ï¼ç´å° ð âðð1ð2â¯ððaâmd1d2â¯dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

è®° ð· =âðð=1ððD=âi=1kdi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯æ¹ç¨å°±åæäºè¿æ ·ï¼

ððð·â ðð¥âðâ¡ðð·(modðð·)akDâ axâkâ¡bD(modmD)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äº ð âðð·aâmD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯æ¨åº ððð· âðð·akDâmD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). è¿æ · ððð·akD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æéå äºï¼äºæ¯æå®ä¸¢å°æ¹ç¨å³è¾¹ï¼è¿å°±æ¯ä¸ä¸ªæ®éç BSGS é®é¢äºï¼äºæ¯æ±è§£ ð¥ âðxâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååå ä¸ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯åæ¹ç¨çè§£å¦ï¼

æ³¨æï¼ä¸æé¤è§£å°äºç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼æä»¥å¨æ¶å å­ä¹ååä¸ä¸ Î(ð)Î(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸¾ï¼ç´æ¥éªè¯ ðð â¡ð(modð)aiâ¡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·å°±è½é¿å è¿ç§æ åµï¼

## ä¹ é¢

  * [SPOJ MOD](https://www.spoj.com/problems/MOD/) æ¨¡æ¿
  * [SDOI2013 éæºæ°çæå¨](https://www.luogu.com.cn/problem/P3306)
  * [SGU261 Discrete Roots](https://codeforces.com/problemsets/acmsguru/problem/99999/261) æ¨¡æ¿
  * [SDOI2011 è®¡ç®å¨](https://loj.ac/problem/10214) æ¨¡æ¿
  * [Luogu4195ãæ¨¡æ¿ãexBSGS/Spoj3105 Mod](https://www.luogu.com.cn/problem/P4195) æ¨¡æ¿
  * [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
  * [LOJ6542 ç¦»æ£å¯¹æ°](https://loj.ac/problem/6542) index calculus æ¹æ³ï¼éæ¨¡æ¿

**æ¬é¡µé¢é¨åå å®¹ä»¥åä»£ç è¯èªåæ[ÐÐ¸ÑÐºÑÐµÑÐ½Ð¾Ðµ Ð¸Ð·Ð²Ð»ÐµÑÐµÐ½Ð¸Ðµ ÐºÐ¾ÑÐ½Ñ](http://e-maxx.ru/algo/discrete_root) ä¸å ¶è±æç¿»è¯ç [Discrete Root](https://cp-algorithms.com/algebra/discrete-root.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

## åèèµæ

  1. [Discrete logarithm - Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm)
  2. æ½æ¿æ´ï¼æ½æ¿å½ªï¼åç­æ°è®ºï¼
  3. å¯å å¤ï¼åç­æ°è®ºåå ¶åºç¨ï¼

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/discrete-logarithm.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/discrete-logarithm.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [sshwy](https://github.com/sshwy), [Steaunk](https://github.com/Steaunk), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [countercurrent-time](https://github.com/countercurrent-time), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [Xeonacid](https://github.com/Xeonacid), [Alpha1022](https://github.com/Alpha1022), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [FFjet](https://github.com/FFjet), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [isdanni](https://github.com/isdanni), [Kelatte](https://github.com/Kelatte), [kxccc](https://github.com/kxccc), [Lampese](https://github.com/Lampese), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [purple-vine](https://github.com/purple-vine), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [xyf007](https://github.com/xyf007), [YOYO-UIAT](https://github.com/YOYO-UIAT)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
