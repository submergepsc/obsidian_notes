# å¢å¡æ¯å®ç - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/lucas/

# å¢å¡æ¯å®ç

åç½®ç¥è¯ï¼[é¶ä¹åæ¨¡](../factorial/)

## å¼å ¥

æ¬æè®¨è®ºå¤§ç»åæ°åæ¨¡çæ±è§£ï¼ç»åæ°ï¼åç§°äºé¡¹å¼ç³»æ°ï¼æè¡¨è¾¾å¼ï¼

(ðð)=ð!ð!(ðâð)!.(nk)=n!k!(nâk)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§æ¨¡ä¸å¤§æ¶ï¼ç»åæ°å¯ä»¥éè¿ [éæ¨å ¬å¼](../../combinatorics/combination/#ç»åæ°æ§è´¨--äºé¡¹å¼æ¨è®º) æ±è§£ï¼æ¶é´å¤æåº¦ä¸º ð(ðð)O(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å¯ä»¥å¨è¾å¤§çç´ æ°æ¨¡æ° ð >ðp>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼éè¿è®¡ç®åå­ååæ¯çé¶ä¹å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±è§£ï¼ä½å½é®é¢è§æ¨¡å¾å¤§ï¼ð â¼1018nâ¼1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¶ï¼è¿äºæ¹æ³ä¸åéç¨ï¼

åºäº Lucas å®çåå ¶æ¨å¹¿ï¼æ¬æè®¨è®ºä¸ç§å¯ä»¥å¨æ¨¡æ°ä¸å¤ªå¤§ (ð â¼106mâ¼106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) æ¶æ±è§£ç»åæ°çæ¹æ³ï¼æ´åç¡®å°è¯´ï¼åªè¦æ¨¡æ°çå¯ä¸åè§£ ð =âððððm=âpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ææç´ æ°å¹çåï¼å³ âððððâpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ 106106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è§æ¨¡æ¶å°±å¯ä»¥ä½¿ç¨è¯¥æ¹æ³ï¼å ä¸ºç®æ³çé¢å¤çå¤§è´ç¸å½äºè¿ä¸è§æ¨¡ï¼

## Lucas å®ç

é¦å è®¨è®ºæ¨¡æ°ä¸ºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼æ Lucas å®çï¼

Lucas å®ç

å¯¹äºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

(ðð)â¡(âð/ðââð/ðâ)(ðmodððmodð)(modð).(nk)â¡(ân/pââk/pâ)(nmodpkmodp)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼å½ ð <ðn<k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼äºé¡¹å¼ç³»æ° (ðð)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è§å®ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å©ç¨çæå½æ°è¯æ

èè (ðð)modð(pn)modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼å ä¸º

(ðð)=ð!ð!(ðâð)!,(pn)=p!n!(pân)!,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å½ ð â 0,ðnâ 0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åæ¯ä¸­é½æ²¡æå å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½åå­ä¸­æå å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥åå¼ä¸å®æ¯ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ°æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½ ð =0,ðn=0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åå¼å°±æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼

(ðð)â¡[ð=0â¨ð=ð](modð).(pn)â¡[n=0â¨n=p](modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®° ð(ð¥) =ðð¥ð +ðð¥ðf(x)=axn+bxm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è¬å°ï¼ç± [äºé¡¹å¼å±å¼](../../combinatorics/combination/#äºé¡¹å¼å®ç) å [è´¹é©¬å°å®ç](../fermat/#è´¹é©¬å°å®ç) æ

(ð(ð¥))ð=(ðð¥ð+ðð¥ð)ð=ðâð=0(ðð)(ðð¥ð)ð(ðð¥ð)ðâðâ¡ððð¥ðð+ððð¥ððâ¡ð(ð¥ð)ð+ð(ð¥ð)ð=ð(ð¥ð)(modð).(f(x))p=(axn+bxm)p=âk=0p(pk)(axn)k(bxm)pâkâ¡apxpn+bpxpmâ¡a(xp)n+b(xp)m=f(xp)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ç¬¬ä¸è¡çåä½å©ç¨äºåæè¯´æçç»è®ºï¼å³åªæ ð =0,ðk=0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç»åæ°æä¸æ¯ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼

å©ç¨è¿ä¸ç»è®ºï¼èå¯äºé¡¹å¼å±å¼ï¼

(1+ð¥)ð=(1+ð¥)ðâð/ðâ(1+ð¥)ðmodðâ¡(1+ð¥ð)âð/ðâ(1+ð¥)ðmodð(modð).(1+x)n=(1+x)pân/pâ(1+x)nmodpâ¡(1+xp)ân/pâ(1+x)nmodp(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç­å¼å·¦ä¾§ä¸­ï¼é¡¹ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°ä¸º

(ðð)modð.(nk)modp.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è½¬èè®¡ç®ç­å¼å³ä¾§ä¸­é¡¹ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°ï¼ç¬¬ä¸ä¸ªå å­ä¸­åé¡¹çæ¬¡æ°å¿ ç¶æ¯ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼ç¬¬äºä¸ªå å­ä¸­åé¡¹çæ¬¡æ°å¿ ç¶å°äº ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£æè¿æ ·ä¸¤é¨åçåçæ¹å¼æ¯å¯ä¸çï¼å³å¸¦ä½é¤æ³ï¼ð =ðâð/ðâ +(ðmodð)k=pâk/pâ+(kmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ç¬¬ä¸ä¸ªå å­åªè½è´¡ç®å ¶ ðâð/ðâpâk/pâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡é¡¹ï¼ç¬¬äºä¸ªå å­åªè½è´¡ç®å ¶ ðmodðkmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡é¡¹ï¼æä»¥ï¼å³ä¾§ç­å¼ä¸­ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç³»æ°ä¸ºä¸¤ä¸ªå å­åèªè´¡ç®çé¡¹çç³»æ°çä¹ç§¯ï¼

(âð/ðââð/ðâ)(ðmodððmodð)modð.(ân/pââk/pâ)(nmodpkmodp)modp.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤ä¸¤ä¾§ç³»æ°ç¸ç­ï¼å°±å¾å° Lucas å®çï¼

å©ç¨é¶ä¹åæ¨¡çç»è®ºè¯æ

æ­¤å¤æä¾ä¸ç§åºäº [é¶ä¹åæ¨¡](../factorial/#ç´) ç¸å ³ç»è®ºçè¯ææ¹æ³ï¼ä»¥æ¹ä¾¿ååæ exLucas é¨åçæ¹æ³å»ºç«èç³»ï¼å·²ç¥äºé¡¹å¼ç³»æ°

(ðð)=ð!ð!(ðâð)!.(nk)=n!k!(nâk)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°é¶ä¹ ð!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡åå ¶ä»å å­åç¦»ï¼å¾å°åè§£ï¼

ð!=ððð(ð!)(ð!)ð.n!=pÎ½p(n!)(n!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±å¾å°äºé¡¹å¼ç³»æ°çè¡¨è¾¾å¼ï¼

(ðð)=ððð(ð!)âðð(ð!)âðð((ðâð)!)(ð!)ð(ð!)ð((ðâð)!)ð.(nk)=pÎ½p(n!)âÎ½p(k!)âÎ½p((nâk)!)(n!)p(k!)p((nâk)!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¹æ¬¡ ðð(ð!)Î½p(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¶ä¹ä½æ° (ð!)ðmodð(n!)pmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æéæ¨å ¬å¼ï¼

ðð(ð!)=âð/ðâ+ðð(âð/ðâ!),(ð!)ðâ¡(â1)âð/ðââ (ðmodð)!â (âð/ðâ!)ð(modð).Î½p(n!)=ân/pâ+Î½p(ân/pâ!),(n!)pâ¡(â1)ân/pââ (nmodp)!â (ân/pâ!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åè æ¯ Legendre å ¬å¼çæ¨è®ºï¼åè æ¯ Wilson å®ççæ¨è®ºï¼

å°éæ¨å ¬å¼ä»£å ¥äºé¡¹å¼ç³»æ°çè¡¨è¾¾å¼å¹¶æ´çï¼å°±å¾å°ï¼

(ðð)â¡(âð)âð/ðâââð/ðâââ(ðâð)/ðââ (ðmodð)!(ðmodð)!((ðâð)modð)!â ððð(âð/ðâ!)âðð(âð/ðâ!)âðð(â(ðâð)/ðâ!)(âð/ðâ!)ð(âð/ðâ!)ð(â(ðâð)/ðâ!)ð(modð).(nk)â¡(âp)ân/pâââk/pâââ(nâk)/pââ (nmodp)!(kmodp)!((nâk)modp)!â pÎ½p(ân/pâ!)âÎ½p(âk/pâ!)âÎ½p(â(nâk)/pâ!)(ân/pâ!)p(âk/pâ!)p(â(nâk)/pâ!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç°å¨èå¯ âð/ðâ ââð/ðâ ââ(ð âð)/ðâân/pâââk/pâââ(nâk)/pâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼å ä¸ºæ

ð=âð/ðâð+(ðmodð),ð=âð/ðâð+(ðmodð),ðâð=â(ðâð)/ðâð+((ðâð)modð),n=ân/pâp+(nmodp),k=âk/pâp+(kmodp),nâk=â(nâk)/pâp+((nâk)modp),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å©ç¨ç¬¬ä¸å¼åå»åä¸¤å¼ï¼å°±å¾å°

(âð/ðâââð/ðâââ(ðâð)/ðâ)ð=(ðmodð)+((ðâð)modð)â(ðmodð).(ân/pâââk/pâââ(nâk)/pâ)p=(kmodp)+((nâk)modp)â(nmodp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç­å¼å³ä¾§ï¼åä¸¤é¡¹çåä¸¥æ ¼å°äº 2ð2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èç¬¬ä¸é¡¹ ðmodðnmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­£æ¯åä¸¤é¡¹çåçä½æ°ï¼æä»¥å³ä¾§å¿ ç¶éè´ï¼ä½å°äº 2ð2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åéè¦æ¯ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å°±åªè½æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æ âð/ðâ ââð/ðâ ââ(ð âð)/ðâân/pâââk/pâââ(nâk)/pâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªè½æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å¦æå®æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ­¤æ¶ä¹æç« (ðmodð) =(ðmodð) +((ð âð)modð)(nmodp)=(kmodp)+((nâk)modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ä¸å¼ä¸­çç¬¬ä¸ä¸ªå å­çææ°ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥å å­å°±ç­äºä¸ï¼ç¬¬äºä¸ªå å­å°±æ¯ (ðmodððmodð)(nmodpkmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¬¬ä¸ä¸ªå å­åç±åæçå±å¼å¼å¯ç¥ï¼å°±ç­äº (âð/ðââð/ðâ)(ân/pââk/pâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼Lucas å ¬å¼æç«ï¼
  * å¦æå®æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ç¬¬ä¸ä¸ªå å­çææ°ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥å å­å°±ç­äºé¶ï¼æä»¥äºé¡¹å¼ç³»æ°çä½æ°ä¸ºé¶ï¼åæ¶ï¼Lucas å®çæè¦è¯æçç­å¼å³ä¾§ç (ðmodððmodð)(nmodpkmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¿ ç¶æ¯é¶ï¼å ä¸ºæ­¤æ¶å¿ ç¶æ (ðmodð) <(ðmodð)(nmodp)<(kmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼å°æ

((ðâð)modð)=ð+(ðmodð)â(ðmodð)â¥ð.((nâk)modp)=p+(nmodp)â(kmodp)â¥p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¾ç¶ä¸ä½æ°çå®ä¹çç¾ï¼

ç»¼åä¸¤ç§æ å½¢ï¼å°±å¾å°äºæè¦æ±è¯ç Lucas å®çï¼è¿ä¸è¯æè¯´æï¼å¨æ±è§£ç´ æ°æ¨¡ä¸ç»åæ°æ¶ï¼å©ç¨ Lucas å®çåå©ç¨ exLucas ç®æ³å¾å°çç»ææ¯ç­ä»·çï¼

Lucas å®çæåºï¼æ¨¡æ°ä¸ºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¤§ç»åæ°çè®¡ç®å¯ä»¥è½¬åä¸ºè§æ¨¡æ´å°çç»åæ°çè®¡ç®ï¼å¨å³å¼ä¸­ï¼ç¬¬ä¸ä¸ªç»åæ°å¯ä»¥ç»§ç»­éå½ï¼ç´å° ð,ð <ðn,k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­¢ï¼ç¬¬äºä¸ªç»åæ°åå¯ä»¥ç´æ¥è®¡ç®ï¼æè æåé¢å¤çåºæ¥ï¼åæä»£ç çå½¢å¼å°±æ¯ï¼

ç¤ºæ

```text 1 2 3 4 ``` |  ```text long long Lucas ( long long n , long long k , long long p ) { if ( k == 0 ) return 1 ; return ( C ( n % p , k % p , p ) * Lucas ( n / p , k / p , p )) % p ; } ```   
---|---  
  
å ¶ä¸­ï¼`C(n, k, p)` ç¨äºè®¡ç®å°è§æ¨¡çç»åæ°ï¼

éå½è³å¤è¿è¡ ð(logðâ¡ð)O(logpâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼å èç®æ³çå¤æåº¦ä¸º ð(ð(ð) +ð(ð)logðâ¡ð)O(f(p)+g(p)logpâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð(ð)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºé¢å¤çç»åæ°çå¤æåº¦ï¼ð(ð)g(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåæ¬¡è®¡ç®ç»åæ°çå¤æåº¦ï¼

### åèå®ç°

æ­¤å¤ç»åºçåèå®ç°å¨ ð(ð)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å é¢å¤ç ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥å çé¶ä¹åå ¶éå åï¼å¯ä»¥å¨ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®åä¸ªç»åæ°ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <iostream> #include <vector> class BinomModPrime { int p ; std :: vector < int > fa , ifa ; // Calculate binom(n, k) mod p for n, k < p. int calc ( int n , int k ) { if ( n < k ) return 0 ; long long res = fa [ n ]; res = ( res * ifa [ k ]) % p ; res = ( res * ifa [ n \- k ]) % p ; return res ; } public : BinomModPrime ( int p ) : p ( p ), fa ( p ), ifa ( p ) { // Factorials mod p till p. fa [ 0 ] = 1 ; for ( int i = 1 ; i < p ; ++ i ) { fa [ i ] = ( long long ) fa [ i \- 1 ] * i % p ; } // Inverse of factorials mod p till p. ifa [ p \- 1 ] = p \- 1 ; // Wilson's theorem. for ( int i = p \- 1 ; i ; \-- i ) { ifa [ i \- 1 ] = ( long long ) ifa [ i ] * i % p ; } } // Calculate binom(n, k) mod p. int binomial ( long long n , long long k ) { long long res = 1 ; while ( n || k ) { res = ( res * calc ( n % p , k % p )) % p ; n /= p ; k /= p ; } return res ; } }; int main () { int t , p ; std :: cin >> t >> p ; BinomModPrime bm ( p ); for (; t ; \-- t ) { long long n , k ; std :: cin >> n >> k ; std :: cout << bm . binomial ( n , k ) << '\n' ; } return 0 ; } ```   
---|---  
  
è¯¥å®ç°çæ¶é´å¤æåº¦ä¸º ð(ð +ðlogðâ¡ð)O(p+Tlogpâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè¯¢é®æ¬¡æ°ï¼

## exLucas ç®æ³

Lucas å®çä¸­å¯¹äºæ¨¡æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¦æ±å¿ é¡»ä¸ºç´ æ°ï¼é£ä¹å¯¹äº ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ç´ æ°çæ åµï¼å°±éè¦ç¨å° exLucas ç®æ³ï¼è½ç¶åå­å¦æ­¤ï¼è¯¥ç®æ³å®é æä½æ¶å¹¶æ²¡æç¨å° Lucas å®çï¼å®çå ³é®æ­¥éª¤æ¯ [è®¡ç®ç´ æ°å¹æ¨¡ä¸çé¶ä¹](../factorial/)ï¼ä¸æçç¬¬äºä¸ªè¯ææåºäºå®ä¸ Lucas å®ççèç³»ï¼

### ç´ æ°å¹æ¨¡çæ å½¢

é¦å èèæ¨¡æ°ä¸ºç´ æ°å¹ ðð¼pÎ±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å°é¶ä¹ ð!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡åå ¶ä»å¹æ¬¡åå¼ï¼å¯ä»¥å¾å°åè§£ï¼

ð!=ððð(ð!)(ð!)ð.n!=pÎ½p(n!)(n!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð(ð!)Î½p(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å æ°åè§£ä¸­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡ï¼è (ð!)ð(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¾ç¶ä¸ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å æ­¤ï¼ç»åæ°å¯ä»¥åä½ï¼

(ðð)=ððð(ð!)âðð(ð!)âðð((ðâð)!)(ð!)ð(ð!)ð((ðâð)!)ð.(nk)=pÎ½p(n!)âÎ½p(k!)âÎ½p((nâk)!)(n!)p(k!)p((nâk)!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¼å­ä¸­ç ðð(ð!)Î½p(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­å¯ä»¥éè¿ [Legendre å ¬å¼](../factorial/#legendre-å) è®¡ç®ï¼(ð!)ð(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­åå¯ä»¥éè¿ [éæ¨å ³ç³»](../factorial/#ç´) è®¡ç®ï¼å ä¸ºåè ä¸ ðð¼pÎ±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼æä»¥åæ¯ä¸çä¹ç§¯çéå å¯ä»¥éè¿ [æ©å±æ¬§å éå¾ç®æ³](../inverse/#æ©å±æ¬§å) è®¡ç®ï¼é®é¢å°±å¾ä»¥è§£å³ï¼

æ³¨æï¼å¦æå¹æ¬¡ ðð(ð!) âðð(ð!) âðð((ð âð)!) â¥ð¼Î½p(n!)âÎ½p(k!)âÎ½p((nâk)!)â¥Î±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ°ä¸å®ä¸ºé¶ï¼ä¸å¿ ååæ´å¤è®¡ç®ï¼

### ä¸è¬æ¨¡æ°çæ å½¢

å¯¹äº ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸è¬çåæ°çæ å½¢ï¼åªéè¦é¦å å¯¹å®å [ç´ å æ°åè§£](../pollard-rho/)ï¼

ð=ðð¼11ðð¼22â¯ðð¼ð ð .m=p1Î±1p2Î±2â¯psÎ±s.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¶åï¼åå«è®¡ç®åºæ¨¡ ðð¼ððpiÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç»åæ° (ðð)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ°ï¼å°±å¾å° ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªåä½æ¹ç¨ï¼

â§{ { { { {â¨{ { { { {â©(ðð)â¡ð1,(modðð¼11),(ðð)â¡ð2,(modðð¼22),â¯(ðð)â¡ðð ,(modðð¼ð ð ).{(nk)â¡r1,(modp1Î±1),(nk)â¡r2,(modp2Î±2),â¯(nk)â¡rs,(modpsÎ±s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æåï¼å©ç¨ [ä¸­å½å©ä½å®ç](../crt/) æ±åºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ°ï¼

### åèå®ç°

æåï¼ç»åºæ¨¡æ¿é¢ç® [äºé¡¹å¼ç³»æ°](https://loj.ac/p/181) çåèå®ç°ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 ``` |  ```text #include <iostream> #include <vector> // Extended Euclid. void ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; } else { ex_gcd ( b , a % b , y , x ); y -= a / b * x ; } } // Inverse of a mod m. int inverse ( int a , int m ) { int x , y ; ex_gcd ( a , m , x , y ); return ( x % m \+ m ) % m ; } // Coefficient in CRT. int crt_coeff ( int m_i , int m ) { long long mm = m / m_i ; mm *= inverse ( mm , m_i ); return mm % m ; } // Binominal Coefficient Calculator Modulo Prime Power. class BinomModPrimePower { int p , a , pa ; std :: vector < int > f ; // Obtain multiplicity of p in n!. long long nu ( long long n ) { long long count = 0 ; do { n /= p ; count += n ; } while ( n ); return count ; } // Calculate (n!)_p mod pa. long long fact_mod ( long long n ) { bool neg = p != 2 || pa <= 4 ; long long res = 1 ; while ( n > 1 ) { if (( n / pa ) & neg ) res = pa \- res ; res = res * f [ n % pa ] % pa ; n /= p ; } return res ; } public : BinomModPrimePower ( int p , int a , int pa ) : p ( p ), a ( a ), pa ( pa ), f ( pa ) { // Pretreatment. f [ 0 ] = 1 ; for ( int i = 1 ; i < pa ; ++ i ) { f [ i ] = i % p ? ( long long ) f [ i \- 1 ] * i % pa : f [ i \- 1 ]; } } // Calculate Binom(n, k) mod pa. int binomial ( long long n , long long k ) { long long v = nu ( n ) \- nu ( n \- k ) \- nu ( k ); if ( v >= a ) return 0 ; auto res = fact_mod ( n \- k ) * fact_mod ( k ) % pa ; res = fact_mod ( n ) * inverse ( res , pa ) % pa ; for (; v ; \-- v ) res *= p ; return res % pa ; } }; // Binominal Coefficient Calculator. class BinomMod { int m ; std :: vector < BinomModPrimePower > bp ; std :: vector < long long > crt_m ; public : BinomMod ( int n ) : m ( n ) { // Factorize. for ( int p = 2 ; p * p <= n ; ++ p ) { if ( n % p == 0 ) { int a = 0 , pa = 1 ; for (; n % p == 0 ; n /= p , ++ a , pa *= p ); bp . emplace_back ( p , a , pa ); crt_m . emplace_back ( crt_coeff ( pa , m )); } } if ( n > 1 ) { bp . emplace_back ( n , 1 , n ); crt_m . emplace_back ( crt_coeff ( n , m )); } } // Calculate Binom(n, k) mod m. int binomial ( long long n , long long k ) { long long res = 0 ; for ( size_t i = 0 ; i != bp . size (); ++ i ) { res = ( bp [ i ]. binomial ( n , k ) * crt_m [ i ] \+ res ) % m ; } return res ; } }; int main () { int t , m ; std :: cin >> t >> m ; BinomMod bm ( m ); for (; t ; \-- t ) { long long n , k ; std :: cin >> n >> k ; std :: cout << bm . binomial ( n , k ) << '\n' ; } return 0 ; } ```   
---|---  
  
è¯¥ç®æ³å¨é¢å¤çæ¶å°æ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£ä¸ºç´ æ°å¹ï¼ç¶åå¯¹ææ ðð¼pÎ±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¢å¤çäºèª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³ ðð¼pÎ±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææé ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ°çèªç¶æ°çä¹ç§¯ï¼ä»¥åå®å¨ä¸­å½å©ä½å®çåå¹¶ç­æ¡æ¶å¯¹åºçç³»æ°ï¼é¢å¤ççæ¶é´å¤æåº¦ä¸º ð(âð +âððð¼ðð)O(m+âipiÎ±i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯æ¬¡è¯¢é®æ¶ï¼å¤æåº¦ä¸º ð(logâ¡ð +âðlogððâ¡ð)O(logâ¡m+âilogpiâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤æåº¦ä¸­çä¸¤é¡¹åå«æ¯è®¡ç®éå åè®¡ç®å¹æ¬¡ãé¶ä¹ä½æ°çå¤æåº¦ï¼

## ä¹ é¢

  * [Luogu3807ãæ¨¡æ¿ãå¢å¡æ¯å®ç](https://www.luogu.com.cn/problem/P3807)
  * [SDOI2010 å¤ä»£çªæ å¢å¡æ¯å®ç](https://loj.ac/problem/10229)
  * [Luogu4720ãæ¨¡æ¿ãæ©å±å¢å¡æ¯](https://www.luogu.com.cn/problem/P4720)
  * [Ceizenpokâs formula](http://codeforces.com/gym/100633/problem/J)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/lucas.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/lucas.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Enter-tainer](https://github.com/Enter-tainer), [c-forrest](https://github.com/c-forrest), [GitPinkRabbit](https://github.com/GitPinkRabbit), [Great-designer](https://github.com/Great-designer), [TonyYin0418](https://github.com/TonyYin0418), [Xeonacid](https://github.com/Xeonacid), [EntropyIncreaser](https://github.com/EntropyIncreaser), [ksyx](https://github.com/ksyx), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [ouuan](https://github.com/ouuan), [Sheng-Horizon](https://github.com/Sheng-Horizon), [Tiphereth-A](https://github.com/Tiphereth-A), [CornWorld](https://github.com/CornWorld), [IceySakura](https://github.com/IceySakura), [Ir1d](https://github.com/Ir1d), [LuoYisu](https://github.com/LuoYisu), [Marcythm](https://github.com/Marcythm), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [whongzhong](https://github.com/whongzhong), [YOYO-UIAT](https://github.com/YOYO-UIAT)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
