# é¶åæ¸¸æ - OI Wiki

- Source: https://oi-wiki.org/math/game-theory/zero-sum-game/

# é¶åæ¸¸æ

åç½®ç¥è¯ï¼[åå¼è®ºç®ä»](../intro/)

æ¬æè®¨è®ºï¼äºäººï¼[é¶åæ¸¸æ](../intro/#é¶åéé¶ååå¼)ï¼

å¨é¶åæ¸¸æä¸­ï¼ä¸¤åç©å®¶çæ¶çä¹åæä¸ºé¶ï¼ä¸æ¹çæ¶çå¿ ç¶æå³çå¦ä¸æ¹çæå¤±ï¼é¶åæ¸¸æå¯ä»¥è§ä¸ºå¸¸åæ¸¸æçç¹æ®æ å½¢ï¼ä¸è¿ï¼ä»»ä½å¸¸åæ¸¸æé½å¯ä»¥éè¿å¯¹æä¸æ¹çæ¶çæ´ä½å ä¸æåå»ä¸ä¸ªå¸¸æ°ï¼ç­ä»·å°è½¬åä¸ºé¶åæ¸¸æï¼æä»¥ä» éè¦è®¨è®ºé¶åæ¸¸æï¼

å¨ç®æ³ç«èµä¸­å¸¸è§çé¶åæ¸¸æå¤§è´å¯åä¸ºä¸¤ç±»ï¼åºè´¯é¶åæ¸¸æä¸åæ¶é¶åæ¸¸æï¼

## åºè´¯é¶åæ¸¸æ

åºè´¯é¶åæ¸¸æä¸­ï¼ä¸¤åç©å®¶è½®æµè¡å¨ï¼ç´å°æ¸¸æç»æ­¢ï¼

åºè´¯é¶åæ¸¸æä¸­ï¼ç©å®¶çæ¶çå½æ°åç°éå½ç»æï¼æ¸¸æå±é¢ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åä¸ºä¸ç±»ï¼å³ç»æ­¢å±é¢ ð0S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡å¨çå±é¢ ð1S1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡å¨çå±é¢ ð2S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾ç»æ­¢å±é¢ ð  âð0sâS0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çä¸º ð£(ð )v(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¸åºå°ï¼ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çä¸º âð£(ð )âv(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼è½®å°ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡å¨æ¶ï¼æå¤§åå®çæ¶çå°±ç¸å½äºæå°åç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çï¼ç±æ­¤ï¼åè®¾åæ¹é½éåæä¼ç­ç¥ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨å±é¢ ð  âðsâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤è½å¤è·å¾çæå¤§æ¶ç ð(ð )V(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å¦ä¸éæ¨å ³ç³»ï¼

ð(ð )=â§{ {â¨{ {â©ð£(ð ),ð âð0,maxð¡âð ð(ð¡),ð âð1,minð¡âð ð(ð¡),ð âð2.V(s)={v(s),sâS0,maxtâsV(t),sâS1,mintâsV(t),sâS2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð¡ âð tâs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåç»§å±é¢ï¼è¿å°±æ¯ [æå°åæå¤§ææ³](../../../search/alpha-beta/#minimax-ç®æ³)ï¼

å°è¿ä¸ç®æ³åºç¨äºå®é é®é¢ä¸­ï¼éå¸¸æå¦ä¸å ·ä½æ¹æ³ï¼

  * å¦ææ¸¸æä¸­æ¶åçå±é¢æ°éè¾å°ï¼ç´æ¥æ´åå®ç°è¿ä¸ç®æ³å³å¯ï¼

  * å¦ææ¸¸æä¸­æ¶åçå±é¢æ°éè¾ä¸ºåºå¤§ä¸æ²¡æç¹æ®ç»æï¼å¯ä»¥èè [AlphaâBeta åªæ](../../../search/alpha-beta/#alphabeta-åªæ) å¹¶ç»åå ¶ä»æç´¢åªæç®æ³ä½¿ç¨ï¼

  * å¦ææ¸¸æä¸­åä¸ªå±é¢ç»å¸¸æ¯å¤ä¸ªå±é¢çåç»§å±é¢ï¼ä¸ºé¿å éå¤æç´¢ï¼å¯ä»¥èèè®°å¿åæç´¢æå ¶ä»å¨æè§åç®æ³ï¼

  * å¦ææ¸¸æä¸­ç©å®¶çæç»æ¶çæ¯ç»å±åææè¡å¨çæ¶çåï¼å¯ä»¥éå½ä¼åå»ºæ¨¡æ¹å¼ï¼å ·ä½å°ï¼åè®¾å°è¾¾ç»å± ð  âð0sâS0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç©å®¶ ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨åºååå«ä¸º {ð(ð)ð}ððð=1{aj(i)}j=1ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¡å¨ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçæ¶çä¸º ð¤(ð)w(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çå½æ°ä¸º

ð£(ð )=ð1âð=1ð¤(ð(1)ð)âð2âð=1ð¤(ð(2)ð).v(s)=âj=1k1w(aj(1))ââj=1k2w(aj(2)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼å¯ä»¥è®¾ Ëð(ð )V~(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå½åç©å®¶å¨å±é¢ ð  âðsâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åçæ¸¸æä¸­è½å¤åå¾çæå¤§åæ°ï¼å¯¹äºåå§ç¶æ ð 0s0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð 0) =Ëð(ð 0)V(s0)=V~(s0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤æ±åº Ëð( â )V~(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¶³ä»¥æ±è§£åé®é¢ï¼å¯¹äº Ëð( â )V~(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æå¦ä¸éæ¨å ³ç³»ï¼

Ëð(ð )={0,ð âð0,maxð¡âð ð¤(ðð âð¡)âËð(ð¡),ð âð1âªð2.V~(s)={0,sâS0,maxtâsw(asât)âV~(t),sâS1âªS2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð âð¡asât![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå¯ä»¥ä½¿å¾ç¶æä» ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½¬ç§»å° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨ï¼å¦ææå¤ä¸ªè¿æ ·çè¡å¨ï¼åæ¶ç ð¤(ð)w(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æé«çé£ä¸ªï¼

  * å ¬å¹³ç»åæ¸¸æé½æ¯åºè´¯é¶åæ¸¸æï¼åªéè¦è®¾æ¸¸æä¸­èå©æ¹åå¤±è´¥æ¹çæ¶çåå«ä¸º +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼æ¶çå½æ° ð( â )V(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨å ³ç³»å ¶å®å°±æ¯å¤å®å¿ èç¶æåå¿ è´¥ç¶æç [å¼ç](../impartial-game/#åå¼å¾åç¶æ)ï¼

è¿ç±»é®é¢è¿æä¸ç§å¸¸è§çåå½¢ï¼å³æ±èå©æ¹æå°éè¦çååæ°åå¤±è´¥æ¹æå¤å¯ä»¥åæçååæ°ï¼ä¸ºæ­¤ï¼åªéè¦æ³¨æå°ä»ç»æ­¢ç¶æå¼å§å BFS å¹¶æç §å¼çå¤å®å¿ èç¶æåå¿ è´¥ç¶ææ¶ï¼è®°å½å¤å®å¿ èç¶æåå¿ è´¥ç¶ææ¶ BFS è¿è¡å°çè½®æ¬¡æ°ï¼å°±æ¯ææ±çååæ°ï¼è¿æ¯å ä¸ºå¤å®ä¸ºå¿ èç¶æåªéè¦ä¸ä¸ªåç»§ç¶ææ¯å¿ è´¥ç¶æå³å¯ï¼å®æ»æ¯ç±åç»§ç¶æä¸­è½®æ¬¡æ°æå°çå¿ è´¥ç¶æè½¬ç§»èæ¥ï¼èå¤å®ä¸ºå¿ è´¥ç¶æéè¦ææåç»§ç¶æé½æ¯å¿ èç¶æï¼å®æ»æ¯ç±åç»§ç¶æä¸­è½®æ¬¡æ°æå¤§çå¿ èç¶æè½¬ç§»èæ¥ï¼

è¿ä¸æ¹æ³åæ ·å¯ä»¥æ¨å¹¿å°ä¸è¬ç [æåå¾æ¸¸æ](../impartial-game/#æåå¾æ¸¸æ)ï¼

### ä¾é¢

[Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)

è®¾æä¸ä¸ªé¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°å ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¤åç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½®æµä»æ°åçä¸¤ç«¯åèµ°ä¸ä¸ªæ°ï¼ç´å°æ°åä¸­ä» å©ä¸æåä¸ä¸ªæ°å­ä¸ºæ­¢ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç®æ æ¯æå¤§åè¿ä¸ªæåå©ä¸çæ°å­ï¼ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç®æ æ¯æå°åå®ï¼å¨æ¸¸ææ­£å¼å¼å§åï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å¯ä»¥å è¿è¡ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡è¡å¨ï¼åè®¾ä¸¤åç©å®¶å¨æ´ä¸ªè¿ç¨ä¸­é½éåæä¼ç­ç¥ï¼å¯¹äºæ¯ä¸ä¸ª ð =0,1,2,â¯,ð â1k=0,1,2,â¯,nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±åºæ¸¸æç»ææ¶æåå©ä¸çæ°å­ï¼å ¶ä¸­ï¼1 â¤ð â¤3 Ã1051â¤nâ¤3Ã105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

å ä¸ºæ è®ºåæ¹ææ ·åèµ°æ°å­ï¼æ°åå©ä½é¨åé½æ¯ä¸æ®µå®æ´çåºé´ï¼æä»¥ï¼æ¸¸æä¸­çå±é¢å¯ä»¥ä» ç±åºé´ [ð,ð][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå½åè¡å¨çç©å®¶ ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè¿°ï¼å¯ä»¥ä½¿ç¨å¨æè§åç®æ³æ±è§£ï¼è®¾ ð(ð,ð,ð)f(l,r,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå±é¢ç± (ð,ð,ð)(l,r,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè¿°æ¶ï¼æ¸¸ææåå©ä¸çæ°å­ï¼ç±åæåæå¯ç¥ï¼å½ ð <ðl<r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è¿ä¸å½æ°æ»¡è¶³ç¶æè½¬ç§»æ¹ç¨ï¼

ð(ð,ð,1)=max{ð(ð+1,ð,2),ð(ð,ðâ1,2)},ð(ð,ð,2)=min{ð(ð+1,ð,1),ð(ð,ðâ1,1)}.f(l,r,1)=max{f(l+1,r,2),f(l,râ1,2)},f(l,r,2)=min{f(l+1,r,1),f(l,râ1,1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»å¼æ¡ä»¶ä¸º ð(ð,ð,1) =ð(ð,ð,2) =ððf(l,l,1)=f(l,l,2)=al![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ®æ­¤ï¼å¯ä»¥å¨ Î(ð2)Î(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±åºææå¯è½å±é¢çå½æ°å¼ï¼å¯¹äºæ¯ä¸ª ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç­æ¡å°±æ¯

ð(ð)=maxð(ð,ð,1)Â subject toÂ ðâð+1=ð.g(k)=maxf(l,r,1)Â subject toÂ râl+1=k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ç®æ³æ æ³éè¿åé¢æè®¾çæ°æ®èå´ï¼å æ­¤éè¦èèä¼åè½¬ç§»ï¼æ­¤å¤æå¾å¤ç§å¤çæ¹æ³ï¼æ¬æåªæä¾å ¶ä¸­ä¸ç§ï¼

å°ç¶æè½¬ç§»æ¹ç¨çä½æ¯å¯¹æ°åæ´ä½çæä½ï¼ä¸¤ä¸ªè½¬ç§»æ¹ç¨åå«è¡¨ç¤ºå°ç¸é»æ°å­åæå¤§å¼åæå°å¼å¾å°æ°æ°åï¼å°å®ä»¬åå«ç§°ä¸ºãæå¤§åæä½ãåãæå°åæä½ãï¼æ¯æ¬¡æä½é½ä¼ä½¿å¾æ°åé¿åº¦åä¸ï¼ææé¿åº¦ä¸º ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºé´å¯¹åºç»æå ±è®¡ (ð âð +1)(nâd+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼è¿å°±ç¸å½äºå¯¹åºåè¿è¡ (ð â1)(dâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡æä½å¾å°çåºåï¼å¦å¤ï¼è¦å¾å° ð(ð,ð,1)f(l,r,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»æï¼å°±éè¦ä¿è¯æåä¸æ¬¡æä½æ¯æå¤§åæä½ï¼å æ­¤ï¼è¿äºæä½åºåçç»å°¾æ»æ¯æå¤§åæä½ï¼

èèè¿ç»­ä¸¤æ¬¡æä½ç»æ°åå¸¦æ¥çååï¼ä¸å¦¨èèé¦å åæå°åæä½ï¼ååæå¤§åæä½ï¼æ­¤æ¶ï¼æ°å ð1,ð2,ð3a1,a2,a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°åä¸º

max{min{ð1,ð2},min{ð2,ð3}}.max{min{a1,a2},min{a2,a3}}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä¸¾ ð1,ð2,ð3a1,a2,a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ªæ°å­ä¹é´ææå¯è½çå¤§å°å ³ç³»å¯ç¥ï¼é¤äº ð1 <ð2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð2 >ð3a2>a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸¥æ ¼æå¤§å¼ï¼è¿ç§æ å½¢å¤ï¼è¿ä¸è¡¨è¾¾å¼æ»æ¯ç­äº ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼å¦æä¸ä¸ªæ°åä¸å­å¨ä»»ä½ä¸¥æ ¼æå¤§å¼ç¹ï¼é£ä¹ï¼è¿ç»­ä¸¤æ¬¡æä½å¯¹å®çå¯ä¸å½±åå°±æ¯å å»äºæ°åé¦å°¾åä¸ä¸ªæ°å­ï¼è¿æ¾ç¶å¤§å¹ ç®åäºè½¬ç§»ï¼å©ä¸å¯ä¸çé®é¢å°±æ¯ï¼å¦ä½ä¿è¯æ°åä¸å­å¨ä»»ä½ä¸¥æ ¼æå¤§å¼ç¹ï¼äºå®ä¸ï¼åªè¦å¯¹åºååä¸æ¬¡æå¤§åæä½ï¼å°±è½ä¿è¯ä¸å­å¨ä¸¥æ ¼æå¤§å¼ç¹ï¼æ èï¼ææå¶æ°æ¬¡æä½çç»æï¼å¯ä»¥éè¿å¯¹åå§æ°åè¿è¡ä¸¤æ¬¡æä½å¾å°çåºåï¼éå¯¹å å»é¦å°¾æ°å­å¾å°ï¼ææå¥æ°æ¬¡æä½çç»æï¼å¯ä»¥éè¿å¯¹åå§æ°åè¿è¡ä¸æ¬¡æä½å¾å°çåºåï¼éå¯¹å å»é¦å°¾æ°å­å¾å°ï¼

ç±äºå¯¹åºåçå®æ´æä½è³å¤åªéè¦è¿è¡ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼èåç»­ç»è®¡ç­æ¡åªéè¦ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡éåï¼æä»¥è¯¥ç®æ³çæ»æ¶é´å¤æåº¦ä¸º Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> int main () { int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( int & x : a ) std :: cin >> x ; std :: vector < int > ans ( n ), tmp ; tmp = a ; for ( int i = 0 ; i < n \- 1 ; ++ i ) { tmp [ i ] = std :: max ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int l = n / 2 \- 1 , r = ( n \- 1 ) / 2 , ma = 0 ; l >= 0 ; \-- l , ++ r ) { ma = std :: max ({ ma , tmp [ l ], tmp [ r ]}); ans [ r \- l ] = ma ; } tmp = a ; for ( int i = 0 ; i < n \- 1 ; ++ i ) { tmp [ i ] = std :: min ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int i = 0 ; i < n \- 2 ; ++ i ) { tmp [ i ] = std :: max ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int l = ( n \- 3 ) / 2 , r = n / 2 \- 1 , ma = 0 ; l >= 0 ; \-- l , ++ r ) { ma = std :: max ({ ma , tmp [ l ], tmp [ r ]}); ans [ r \- l ] = ma ; } ans [ n \- 1 ] = * std :: max_element ( a . begin (), a . end ()); for ( auto x : ans ) std :: cout << x << ' ' ; std :: cout << std :: endl ; return 0 ; } ```   
---|---  
  
### ä¹ é¢

  * [Luogu P2734 [USACO3.3] æ¸¸æ A Game](https://www.luogu.com.cn/problem/P2734)
  * [Luogu P4576 [CQOI2013] æ£çæ¸¸æ](https://www.luogu.com.cn/problem/P4576)
  * [Luogu P7097 [yLOI2020] çµä¸æ](https://www.luogu.com.cn/problem/P7097)
  * [Codeforces 388 C. Fox and Card Game](https://codeforces.com/problemset/problem/388/C)
  * [Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)
  * [Codeforces 1628 D2. Game on Sum (Hard Version)](https://codeforces.com/problemset/problem/1628/D2)
  * [Luogu P3210 [HNOI2010] åç³å¤´æ¸¸æ](https://www.luogu.com.cn/problem/P3210)

## åæ¶é¶åæ¸¸æ

åæ¶é¶ååå¼ä¸­ï¼ä¸¤åç©å®¶åæ¶è¡å¨ï¼

åæ¶é¶åæ¸¸æéå¸¸éç¨æ¶çç©éµè¡¨ç¤ºï¼åè®¾ç©å®¶ ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨éåä¸º ð´ðAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å½ç©å®¶ ð =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«éåè¡å¨ ðð âð´ðaiâAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ä¸¤äººçæ¶çåå«æ¯ ð£(ð1,ð2)v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å âð£(ð1,ð2)âv(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¾å­

èèç³å¤´åªåå¸æ¸¸æï¼åå®èå©å¾ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼å¤±è´¥å¾ â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼å¹³å±å¾ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼é£ä¹ï¼æ¸¸æä¸­ä¸¤äººçæ¶çå¯ä»¥è¡¨ç¤ºä¸º

ââ â ââ0,01,â1â1,1â1,10,01,â11,â1â1,10,0ââ â ââ .(0,01,â1â1,1â1,10,01,â11,â1â1,10,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸è¬çäºäººåæ¶æ¸¸æä¹å¯ä»¥è¡¨ç¤ºä¸ºç±»ä¼¼å½¢å¼ï¼æ èä¹ç§°ä¸º [åç©éµæ¸¸æ](https://en.wikipedia.org/wiki/Bimatrix_game)ï¼bimatrix gameï¼ï¼å¯¹äºé¶ååå¼ï¼ç±äºç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çç©éµåç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çç©éµäºä¸ºç¸åæ°ï¼æä»¥å¯ä»¥åªèèç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çç©éµï¼

ð=(ð£(ð1,ð2))(ð1,ð2)âð´1Ãð´2=ââ â ââ01â1â1011â10ââ â ââ .V=(v(a1,a2))(a1,a2)âA1ÃA2=(01â1â1011â10).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éè¦è§£å³çé®é¢æ¯ï¼ç»å®æ¶çç©éµ ð =(ð£(ð1,ð2))(ð1,ð2)âð´1Ãð´2V=(v(a1,a2))(a1,a2)âA1ÃA2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ä½æ±åºä¸¤åç©å®¶çæä¼ç­ç¥åæå¤§æ¶çï¼

### æ··åç­ç¥

ç¸è¾äºåºè´¯é¶åæ¸¸æï¼åæ¶æ¸¸æä¸­ä¸¤åç©å®¶çè§è²æ¯å¯¹ç§°çï¼ä½æ¯ï¼æ¢ç¶å·²ç»è§£å³äºåºè´¯é¶åæ¸¸æï¼é£ä¹ä¸å¦¨èèåæ¶æ¸¸æçåºè´¯çæ¬ï¼ä¾å¦ï¼å¦æåå®ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¦å ååºè¡å¨ï¼ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åååºè¡å¨ï¼é£ä¹ï¼æ ¹æ®åæè®¨è®ºï¼æ¸¸æç»ææ¶ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çå°ç±

ð¤â=maxð1âð´1minð2âð´2ð£(ð1,ð2)wâ=maxa1âA1mina2âA2v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»åºï¼ç±äºç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨å¯¹äºç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååéæï¼è¿åºè¯¥æ¯ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè½è·å¾çæå·®ç»æï¼å¯¹ç§°å°ï¼å¦æåå®ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¦å è¡å¨ï¼é£ä¹ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çå°ç±

ð¤+=minð2âð´2maxð1âð´1ð£(ð1,ð2)w+=mina2âA2maxa1âA1v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»åºï¼ç±äºç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨å¯¹äºç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååéæï¼è¿åºè¯¥æ¯ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè½è·å¾çæå¥½ç»æï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºè¯¥æå¾ å®é è¿è¡æ¸¸ææ¶ï¼æè½è·å¾çæ¶ç ð¤ â[ð¤â,ð¤+]wâ[wâ,w+]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°½ç®¡ä¸ç­å¼ ð¤â â¤ð¤+wââ¤w+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯æç«ï¼è¯æåè§ [å¼±å¯¹å¶å®ç](../../linear-programming/#å¯¹å¶åç)ï¼ï¼ä½æ¯ç±äºç­å·æªå¿ æç«ï¼æä»¥ï¼ä» éç¨åºè´¯æ¸¸æçåæææ®µï¼ä¸è¬æ åµä¸æ²¡æåæ³å¯ä¸ç¡®å®æ¸¸æç»æï¼

ä¾å­ï¼ç»­ï¼

ç³å¤´åªåå¸æ¸¸æä¸­ï¼å¦æåºææå åï¼é£ä¹å æå¿ è¾ï¼åæå¿ èµ¢ï¼è½¬æ¢ä¸ºæ°å­¦è¯­è¨ï¼è¿å°±æ¯ä¸åä¸ç­å¼ï¼

ð¤â=â1â¤+1=ð¤+.wâ=â1â¤+1=w+.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼ð¤â â ð¤+wââ w+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸æç«ï¼

ä¸è¿°åæè¿ç¨éæ¼äºåæ¶æ¸¸æçä¸ä¸ªå ³é®å ç´ ï¼å°±æ¯ç©å®¶æ æ³åç¡®é¢æµå¯¹æçè¡å¨ï¼å½¢å¼ä¸ï¼è¿æå³çåæ¹å¯ä»¥éåæç§éæºç­ç¥ï¼è¿ä¸æ³æ³å¨åºè´¯åå¼çè¯­å¢ä¸å¹¶ä¸æç«ï¼å ä¸ºæ è®ºå æç©å®¶å¦ä½éæºéæ©è¡å¨ï¼åæç©å®¶æ»è½åç¡®å°è§æµå°è¿ä¸è¡å¨ï¼å¹¶æéå¯¹æ§å°ååºï¼ä½æ¯ï¼å¯¹äºåæ¶æ¸¸æï¼éæºç­ç¥å¼å ¥çæç¥æ¨¡ç³å°ä½¿å¾å¯¹ææ æ³ææå°éå¯¹å·±æ¹çè¡å¨ï¼

ä¾å­ï¼ç»­ï¼

ç³å¤´åªåå¸æ¸¸æä¸­ï¼å¦æç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååéæºå°éæ©åªåãç³å¤´ãå¸ä¸ä¸ªè¡å¨ä¹ä¸ï¼é£ä¹ï¼æ ¹æ®ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨ä¸åï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½è·å¾çæ¶çæ¯

13(0,1,â1)ð+13(â1,0,1)ð+13(1,â1,0)ð=(0,0,0)ð.13(0,1,â1)T+13(â1,0,1)T+13(1,â1,0)T=(0,0,0)T.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼æ è®ºç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¦ä½éæ©è¡å¨ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæææ¶çæ»æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¾ç¶å¥½äºç¡®å®æ§å°éæ©åä¸ªè¡å¨ï¼

ç±æ­¤ï¼å°±å¼å ¥äºæ··åç­ç¥çæ¦å¿µï¼

æ··åç­ç¥

åæ¶æ¸¸æä¸­ï¼ç©å®¶ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **æ··åç­ç¥** ï¼mixed strategyï¼ï¼ç®ç§° **ç­ç¥** ï¼æ¯æå½æ° ð ð :ð´ð â[0,1]si:Aiâ[0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å®æ»¡è¶³ âððâð´ðð ð(ðð) =1âaiâAisi(ai)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ç­ç¥ ð ðsi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ç©å®¶ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡å¨éå ð´ðAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸ä¸ªæ¦çåå¸ï¼ç©å®¶ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ¨ä½æ··åç­ç¥çéåè®°ä½ ðð =Î(ð´ð)Si=Î(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼Î(ð´ð)Î(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ð´ðAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çå ¨ä½æ¦çåå¸çéåï¼å¦æ ð ðsi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯éåçæ¦çåå¸ï¼å³å­å¨ ð âð´ðaâAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð ð(ð) =1si(a)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ä¹ç§°ç­ç¥ ð ðsi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **çº¯ç­ç¥** ï¼pure strategyï¼ï¼

æ··åç­ç¥çæ¶çå°±æ¯åä¸ªè¡å¨æ¶ççææï¼

ð£(ð 1,ð 2)=âð1âð´1âð2âð´2ð 1(ð1)ð 2(ð2)ð£(ð1,ð2).v(s1,s2)=âa1âA1âa2âA2s1(a1)s2(a2)v(a1,a2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°åä¸ªè¡å¨çä½å¯¹åºççº¯ç­ç¥ï¼é£ä¹ï¼å°±å¯ä»¥å°è¡å¨éå ð´ðAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åµå ¥ï¼æ··åï¼ç­ç¥éå ððSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼ä¸ä¸å¼å®ä¹ç ð£(ð 1,ð 2)v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥çä½æ¯å° ð£(ð1,ð2)v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä» ð´1 Ãð´2A1ÃA2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å»¶æå° ð1 Ãð2S1ÃS2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼

### von Neumann å®ç

å¼å ¥æ··åç­ç¥åï¼æå¤§åæå°ææ³åæå°åæå¤§ææ³å¾å°çç»ææ¯ä¸è´çï¼ç±æ­¤ï¼åæ¶é¶åæ¸¸æçç»æä¹æ¯å¯ä¸ç¡®å®çï¼

å®çï¼von Neumannï¼

å è®¸æ··åç­ç¥çåæ¶é¶åæ¸¸æä¸­ï¼å¦æåæ¹é½éåæä¼ç­ç¥ï¼é£ä¹ï¼ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§æ¶çä¸º

ð¤=maxð 1âð1minð 2âð2ð£(ð 1,ð 2)=minð 2âð2maxð 1âð1ð£(ð 1,ð 2),w=maxs1âS1mins2âS2v(s1,s2)=mins2âS2maxs1âS1v(s1,s2),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§æ¶çä¸º âð¤âw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

è®¾ ð¤ =maxð 1âð1minð 2âð2ð£(ð 1,ð 2)w=maxs1âS1mins2âS2v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèå å±æå°åé®é¢ï¼å ä¸º ð£(ð 1,ð 2) =âð2âð´2ð 2(ð2)ð£(ð 1,ð2)v(s1,s2)=âa2âA2s2(a2)v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼maxð 2âð2ð£(ð 1,ð 2) =maxð2âð´2ð£(ð 1,ð2)maxs2âS2v(s1,s2)=maxa2âA2v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè çæä¼è§£å°±æ¯åè çæä¼è§£å¯¹åºççº¯ç­ç¥ï¼å æ­¤ï¼æ ð¤ =maxð 1âð1minð2âð´2ð£(ð 1,ð2)w=maxs1âS1mina2âA2v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿èï¼å¼å ¥è¾ å©åé ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é®é¢å°±å¯ä»¥æ¹åä¸º

ð¤=maxð 1âð1ð¢Â subject toÂ ð¢â¤minð2âð´2ð£(ð 1,ð2).w=maxs1âS1uÂ subject toÂ uâ¤mina2âA2v(s1,a2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºè¿ä¸ªçº¦æå°±ç­ä»·äº ð¢ â¤ð£(ð 1,ð2)uâ¤v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð2 âð´2a2âA2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼æåï¼å¼å ¥æ··åç­ç¥ ð 1s1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå®ä¹åæ¶çå½æ° ð£(ð 1,ð2)v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼åé®é¢å°±ç­ä»·äº [çº¿æ§è§åé®é¢](../../linear-programming/)

(ð)ð¤=maxð¢,ð 1ð¢subject toÂ âð1âð´1ð 1(ð1)ð£(ð1,ð2)â¥ð¢,Â âð2âð´2,âð1âð´1ð 1(ð1)=1,ð 1(ð1)â¥0,Â âð1âð´1.(P)w=maxu,s1usubject toÂ âa1âA1s1(a1)v(a1,a2)â¥u,Â âa2âA2,âa1âA1s1(a1)=1,s1(a1)â¥0,Â âa1âA1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªé®é¢æ¾ç¶æ¯å¯è¡çï¼ä¸æä¼è§£æè§£ï¼æ ¹æ® [å¯¹å¶åç](../../linear-programming/#å¯¹å¶åç) å¯ç¥ï¼å®çæä¼è§£å°±ç­äºå¯¹å¶é®é¢çæä¼è§£ï¼

(ð·)ð¤=minð¡,ð 2ð¡subject toÂ âð2âð´2ð 2(ð2)ð£(ð1,ð2)â¤ð¡,Â âð1âð´1,âð2âð´2ð 2(ð2)=1,ð 2(ð2)â¥0,Â âð2âð´2.(D)w=mint,s2tsubject toÂ âa2âA2s2(a2)v(a1,a2)â¤t,Â âa1âA1,âa2âA2s2(a2)=1,s2(a2)â¥0,Â âa2âA2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éå¤åæçæ­¥éª¤ï¼è¿ä¸é®é¢å°±ç­ä»·äº minð 2âð´2minð 1âð1ð£(ð 1,ð 2)mins2âA2mins1âS1v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çå¾è¯ï¼

è¿ä¸ç»ææ­£æ¯è¿ä¸æ¸¸æç [Nash åè¡¡](https://en.wikipedia.org/wiki/Nash_equilibrium)ï¼ä¹å°±æ¯è¯´ï¼åå®åæ¹é½éæ©åè¡¡ä¸­çæä¼ç­ç¥ï¼é£ä¹ï¼æ²¡æä»»ä½ç©å®¶è½å¤ä»åç¦»åè¡¡ç­ç¥ä¸­ä¸¥æ ¼è·çï¼

### è½¬åä¸ºçº¿æ§è§åé®é¢

von Neumann å®ççè¯æåæ¶ä¹æåºäºåæ¶é¶åæ¸¸æçæ±è§£æ¹æ³ï¼è®¾ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯éåçè¡å¨æ°ç®ï¼ç»å®ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶çç©éµ ð âððÃðVâRnÃm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥æ±è§£å¦ä¸çº¿æ§è§åé®é¢ï¼

ð¤=max(ð¢,ð )âðÃððð¢subject toÂ ððð â¥ð¢ð,ððð =1,ð â¥0.w=max(u,s)âRÃRnusubject toÂ VTsâ¥u1,1Ts=1,sâ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸ä¸ªè§æ¨¡ä¸º Î(ð +ð)Î(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ§è§åé®é¢ï¼å¯ä»¥ç¨ [åçº¯å½¢æ³](../../simplex/) é«ææ±è§£ï¼ç®æ³å¾å°çæä¼è§£ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ç©å®¶ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¼ï¼æ··åï¼ç­ç¥ï¼è¦æ±å¾ç©å®¶ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¼ç­ç¥ï¼åªéè¦ä»åçº¯å½¢è¡¨ä¸­è·å¾è¯¥é®é¢æä¼è§£çå¯¹å¶åéï¼å³å½±å­ä»·æ ¼ï¼å³å¯ï¼

### ä¹ é¢

  * [Luogu P4232 æ æè¯ä¹å¤çæè¿·è](https://www.luogu.com.cn/problem/P4232)

## åèèµæä¸æ³¨é

  * [Zero-sum game - Wikipedia](https://en.wikipedia.org/wiki/Zero-sum_game)
  * [Minimax theorem - Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2025/10/17 09:50:13ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/game-theory/zero-sum-game.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/game-theory/zero-sum-game.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[c-forrest](https://github.com/c-forrest)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
