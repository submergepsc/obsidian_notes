# å®¹æ¥åç - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/inclusion-exclusion-principle/

# å®¹æ¥åç

## å¼å ¥

å ¥é¨ä¾é¢

åè®¾ç­éæ 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­¦çåæ¬¢æ°å­¦ï¼1515![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­¦çåæ¬¢è¯­æï¼2121![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­¦çåæ¬¢ç¼ç¨ï¼ç­éè³å°åæ¬¢ä¸é¨å­¦ç§çæå¤å°ä¸ªå­¦çå¢ï¼

æ¯ 10 +15 +21 =4610+15+21=46![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªåï¼ä¸æ¯çï¼å ä¸ºæäºå­¦çå¯è½åæ¶åæ¬¢æ°å­¦åè¯­æï¼æè è¯­æåç¼ç¨ï¼çè³è¿æå¯è½ä¸è é½åæ¬¢ï¼

ä¸ºäºåè¿°æ¹ä¾¿ï¼æä»¬æåæ¬¢è¯­æãæ°å­¦ãç¼ç¨çå­¦çéååå«ç¨ ð´,ðµ,ð¶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºï¼åå­¦çæ»æ°ç­äº |ð´ âªðµ âªð¶||AâªBâªC|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæå·²ç»è®²è¿ï¼å¦ææè¿ä¸ä¸ªéåçå ç´ ä¸ªæ° |ð´|,|ðµ|,|ð¶||A|,|B|,|C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç´æ¥å èµ·æ¥ï¼ä¼æä¸äºå ç´ éå¤ç»è®¡äºï¼å æ­¤éè¦æ£æ |ð´ â©ðµ|,|ðµ â©ð¶|,|ð¶ â©ð´||Aâ©B|,|Bâ©C|,|Câ©A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½è¿æ ·ä¸æ¥ï¼åæä¸å°é¨åå¤æ£äºï¼éè¦å åæ¥ï¼å³ |ð´ â©ðµ â©ð¶||Aâ©Bâ©C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³

|ð´âªðµâªð¶|=|ð´|+|ðµ|+|ð¶|â|ð´â©ðµ|â|ðµâ©ð¶|â|ð¶â©ð´|+|ð´â©ðµâ©ð¶||AâªBâªC|=|A|+|B|+|C|â|Aâ©B|â|Bâ©C|â|Câ©A|+|Aâ©Bâ©C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![å®¹æ¥åç - venn å¾ç¤ºä¾](./images/incexcp.png)

æä¸è¿°é®é¢æ¨å¹¿å°ä¸è¬æ åµï¼å°±æ¯æä»¬çç¥çå®¹æ¥åçï¼

## å®ä¹

è®¾ U ä¸­å ç´ æ n ç§ä¸åçå±æ§ï¼èç¬¬ i ç§å±æ§ç§°ä¸º ððPi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¥æå±æ§ ððPi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ç´ ææéå ððSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹

â£ðâð=1ððâ£=âð|ðð|ââð<ð|ððâ©ðð|+âð<ð<ð|ððâ©ððâ©ðð|ââ¯+(â1)ðâ1âðð<ðð+1â£ðâð=1ðððâ£+â¯+(â1)ðâ1|ð1â©â¯â©ðð||âi=1nSi|=âi|Si|ââi<j|Siâ©Sj|+âi<j<k|Siâ©Sjâ©Sk|ââ¯+(â1)mâ1âai<ai+1|âi=1mSai|+â¯+(â1)nâ1|S1â©â¯â©Sn|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³

â£ðâð=1ððâ£=ðâð=1(â1)ðâ1âðð<ðð+1â£ðâð=1ðððâ£|âi=1nSi|=âm=1n(â1)mâ1âai<ai+1|âi=1mSai|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### è¯æ

å¯¹äºæ¯ä¸ªå ç´ ä½¿ç¨äºé¡¹å¼å®çè®¡ç®å ¶åºç°çæ¬¡æ°ï¼å¯¹äºå ç´ xï¼åè®¾å®åºç°å¨ ð1,ð2,â¯,ððT1,T2,â¯,Tm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¸­ï¼é£ä¹å®çåºç°æ¬¡æ°ä¸º

ð¶ðð¡=|{ðð}|â|{ððâ©ðð|ð<ð}|+â¯+(â1)ðâ1â£{ðâð=1ððð|ðð<ðð+1}â£+â¯+(â1)ðâ1|{ð1â©â¯â©ðð}|=(ð1)â(ð2)+â¯+(â1)ðâ1(ðð)=(ð0)âðâð=0(â1)ð(ðð)=1â(1â1)ð=1Cnt=|{Ti}|â|{Tiâ©Tj|i<j}|+â¯+(â1)kâ1|{âi=1kTai|ai<ai+1}|+â¯+(â1)mâ1|{T1â©â¯â©Tm}|=(m1)â(m2)+â¯+(â1)mâ1(mm)=(m0)ââi=0m(â1)i(mi)=1â(1â1)m=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯æ¯ä¸ªå ç´ åºç°çæ¬¡æ°ä¸º 1ï¼é£ä¹åå¹¶èµ·æ¥å°±æ¯å¹¶éï¼è¯æ¯ï¼

### è¡¥é

å¯¹äºå ¨é U ä¸ç **éåçå¹¶** å¯ä»¥ä½¿ç¨å®¹æ¥åçè®¡ç®ï¼èéåçäº¤åç¨å ¨éåå» **è¡¥éçå¹¶é** æ±å¾ï¼

â£ðâð=1ððâ£=|ð|ââ£ðâð=1ââððâ£|âi=1nSi|=|U|â|âi=1nSiâ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³è¾¹ä½¿ç¨å®¹æ¥å³å¯ï¼

å¯è½æ¥è§¦è¿å®¹æ¥çè¯»è é½æ¸ æ¥ä¸è¿°å å®¹ï¼èæ´å ³å¿çæ¯å®¹æ¥çåºç¨ï¼

é£ä¹æ¥ä¸æ¥æä»¬ç»åº 3 ä¸ªå±æ¬¡ä¸åçä¾é¢æ¥ä¸ºå¤§å®¶å±ç¤ºå®¹æ¥åççåºç¨ï¼

## ä¸å®æ¹ç¨éè´æ´æ°è§£è®¡æ°

ä¸å®æ¹ç¨éè´æ´æ°è§£è®¡æ°

ç»åºä¸å®æ¹ç¨ âðð=1ð¥ð =ðâi=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéå¶æ¡ä»¶ ð¥ð â¤ððxiâ¤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð,ðð ââm,biâN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). æ±æ¹ç¨çéè´æ´æ°è§£çä¸ªæ°ï¼

### æ²¡æéå¶æ¶

å¦ææ²¡æ ð¥ð â¤ððxiâ¤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå¶ï¼é£ä¹ä¸å®æ¹ç¨ âðð=1ð¥ð =ðâi=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°è§£çæ°ç®ä¸º (ð+ðâ1ðâ1)(m+nâ1nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

ç¥è¯ï¼ææ¿æ³ï¼

ç¸å½äºä½ æ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçè¦åç» ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçå­ï¼å è®¸æä¸ªçå­æ¯ç©ºçï¼è¿ä¸ªé®é¢ä¸è½ç´æ¥ç¨ç»åæ°è§£å³ï¼

äºæ¯æä»¬åå å ¥ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçï¼äºæ¯é®é¢å°±åæäºå¨ä¸ä¸ªé¿åº¦ä¸º ð +ð â1m+nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççåºåä¸­éæ© ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçï¼ç¶åè¿ä¸ª ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçæè¿ä¸ªåºåéæäº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»½ï¼æ°å¥½å¯ä»¥ä¸ä¸å¯¹åºæ¾å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçå­ä¸­ï¼é£ä¹å¨ ð +ð â1m+nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçä¸­éæ© ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªççæ¹æ¡æ°å°±æ¯ (ð+ðâ1ðâ1)(m+nâ1nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å®¹æ¥æ¨¡å

æ¥çæä»¬å°è¯æ½è±¡åºå®¹æ¥åççæ¨¡åï¼

  1. å ¨é Uï¼ä¸å®æ¹ç¨ âðð=1ð¥ð =ðâi=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°è§£
  2. å ç´ ï¼åé ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).
  3. å±æ§ï¼ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå±æ§å³ ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³çæ¡ä»¶ï¼å³ ð¥ð â¤ððxiâ¤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¡ä»¶

ç®æ ï¼ææåéæ»¡è¶³å¯¹åºå±æ§æ¶éåçå¤§å°ï¼å³ |âðð=1ðð||âi=1nSi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

è¿ä¸ªä¸è¥¿å¯ä»¥ç¨ |âðð=1ðð| =|ð| ââ£âðð=1ââððâ£|âi=1nSi|=|U|â|âi=1nSiâ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±è§£ï¼|ð||U|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥ç¨ç»åæ°è®¡ç®ï¼ååé¨åèªç¶ä½¿ç¨å®¹æ¥åçå±å¼ï¼

é£ä¹é®é¢åæï¼å¯¹äºä¸äº âââðððSaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäº¤éæ±å¤§å°ï¼èè âââðððSaiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå«ä¹ï¼è¡¨ç¤º ð¥ðð â¥ððð +1xaiâ¥bai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£çæ°ç®ï¼èäº¤éè¡¨ç¤ºåæ¶æ»¡è¶³è¿äºæ¡ä»¶ï¼å æ­¤è¿ä¸ªäº¤éå¯¹åºçä¸å®æ¹ç¨ä¸­ï¼æäºåéæ **ä¸çéå¶** ï¼èæäºåæ²¡æéå¶ï¼

è½å¦æ¶é¤è¿äºä¸çéå¶å¢ï¼æ¢ç¶è¦æ±çæ¯éè´æ´æ°è§£ï¼èæäºåéçä¸çåå¤§äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æä»¬ç´æ¥ **æè¿ä¸ªä¸çåæ** ï¼å°±å¯ä»¥ä½¿å¾è¿äºåéçä¸çåæ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³æ²¡æä¸çå¦ï¼å æ­¤å¯¹äº

â£1â¤ðâ¤ðâðð<ðð+1ðððâ£|âai<ai+11â¤iâ¤kSai|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çä¸å®æ¹ç¨å½¢å¼ä¸º

ðâð=1ð¥ð=ðâðâð=1(ððð+1)âi=1nxi=mââi=1k(bai+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯è¿ä¸ªä¹å¯ä»¥ç»åæ°è®¡ç®å¦ï¼è¿ä¸ªé¿åº¦ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°ç»ç¸å½äºå¨æä¸¾å­éï¼

## HAOI2008 ç¡¬å¸è´­ç©

HAOI2008 ç¡¬å¸è´­ç©

4 ç§é¢å¼çç¡¬å¸ï¼ç¬¬ i ç§çé¢å¼æ¯ ð¶ðCi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡è¯¢é®ï¼æ¯æ¬¡è¯¢é®ç»åºæ¯ç§ç¡¬å¸çæ°é ð·ðDi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ä¸ªä»·æ ¼ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é®ä»æ¬¾æ¹å¼ï¼

ð â¤103,ð â¤105nâ¤103,Sâ¤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

å¦æç¨èå åçè¯å¤æåº¦æ¯ ð(4ðð)O(4nS)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ æ³æ¿åï¼è¿éé¢æææ¾çç¹ç¹å°±æ¯ç¡¬å¸ä¸å ±åªæåç§ï¼æ½è±¡æ¨¡åï¼å ¶å®å°±æ¯è®©æä»¬æ±æ¹ç¨ â4ð=1ð¶ðð¥ð =ð,ð¥ð â¤ð·ðâi=14Cixi=S,xiâ¤Di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°è§£çä¸ªæ°ï¼

éç¨åæ ·çå®¹æ¥æ¹å¼ï¼ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå±æ§ä¸º ð¥ð â¤ð·ðxiâ¤Di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å¥ç¨å®¹æ¥åççå ¬å¼ï¼æåæä»¬è¦æ±è§£

4âð=1ð¶ðð¥ð=ðâðâð=1ð¶ðð(ð·ðð+1)âi=14Cixi=Sââi=1kCai(Dai+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯æ éèå é®é¢ï¼è¿ä¸ªé®é¢å¯ä»¥é¢å¤çï¼ç®ä¸è¯¢é®ï¼æ»å¤æåº¦ ð(4ð +24ð)O(4S+24n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»£ç å®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <iostream> using namespace std ; constexpr long long S = 1e5 \+ 5 ; long long c [ 5 ], d [ 5 ], n , s ; long long f [ S ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> c [ 1 ] >> c [ 2 ] >> c [ 3 ] >> c [ 4 ] >> n ; f [ 0 ] = 1 ; for ( long long j = 1 ; j <= 4 ; j ++ ) for ( long long i = 1 ; i < S ; i ++ ) if ( i >= c [ j ]) f [ i ] += f [ i \- c [ j ]]; // f[i]ï¼ä»·æ ¼ä¸ºiæ¶çç¡¬å¸ç»ææ¹æ³æ° for ( long long k = 1 ; k <= n ; k ++ ) { cin >> d [ 1 ] >> d [ 2 ] >> d [ 3 ] >> d [ 4 ] >> s ; long long ans = 0 ; for ( long long i = 1 ; i < 16 ; i ++ ) { // å®¹æ¥ï¼å ä¸ºç©åä¸å ±æ4ç§ï¼æä»¥ä»1å°2^4-1=15å¾ªç¯ long long m = s , bit = 0 ; for ( long long j = 1 ; j <= 4 ; j ++ ) { if (( i >> ( j \- 1 )) % 2 == 1 ) { m -= ( d [ j ] \+ 1 ) * c [ j ]; bit ++ ; } } if ( m >= 0 ) ans += ( bit % 2 * 2 \- 1 ) * f [ m ]; } cout << f [ s ] \- ans << '\n' ; } return 0 ; } ```   
---|---  
  
## å®å ¨å¾å­å¾æè²é®é¢

åé¢çä¸éé¢é½æ¯å®¹æ¥åççæ­£åè¿ç¨ï¼è¿éé¢åéè¦ç¨å°å®¹æ¥åçéååæï¼

å®å ¨å¾å­å¾æè²é®é¢

A å B åæ¬¢å¯¹å¾ï¼ä¸ä¸å®è¿éï¼è¿è¡æè²ï¼èä»ä»¬çè§åæ¯ï¼ç¸é»çç»ç¹å¿ é¡»æåä¸ç§é¢è²ï¼ä»å¤© A å B ç©æ¸¸æï¼å¯¹äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶ **å®å ¨å¾** ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»ä»¬å®ä¹ä¸ä¸ªä¼°ä»·å½æ° ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ S æ¯è¾¹éï¼ð âð¸SâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼æ¯å¯¹å¾ ðºâ² =(ð,ð)Gâ²=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¨ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§é¢è²æè²çæ»æ¹æ¡æ°ï¼ä»ä»¬çå¦ä¸ä¸ªè§åæ¯ï¼å¦æ |ð||S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°ï¼é£ä¹ A çå¾åå¢å ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦å B çå¾åå¢å ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). é® A å B çå¾åå·®å¼ï¼

### æ°å­¦å½¢å¼

ä¸çè¿éé¢çç®æ³è¶åå¹¶ä¸ææ¾ï¼å æ­¤å¯¹äºæ£æçé¢ç®é¦å æ½è±¡åºæ°å­¦å½¢å¼ï¼å¾åå·®å³ä¸ºå¥å¶å¯¹ç§°å·®ï¼å¯ä»¥ç¨ -1 çå¹æ¬¡æ¥ä½ä¸ºç³»æ°ï¼æä»¬æ±çæ¯

ð´ðð =âðâð¸(â1)|ð|â1ð¹(ð)Ans=âSâE(â1)|S|â1F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å®¹æ¥æ¨¡å

ç¸é»ç»ç¹æåä¸ç§é¢è²ï¼æä»¬æå®å½ä½å±æ§ï¼å¨è¿éæä»¬å ä¸éµå®æè²çè§åï¼åå®æä»¬ç¨ m ç§é¢è²ç´æ¥å¯¹å¾æè²ï¼å¯¹äºå¾ ðºâ² =(ð,ð)Gâ²=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬æå®å½ä½ **å ç´** ï¼**å±æ§** ð¥ð =ð¥ðxi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå«ä¹æ¯ç»ç¹ i,j æåè²ï¼æ³¨æï¼å¹¶æªè¦æ± i,j ä¹é´æè¿è¾¹ï¼ï¼

èå±æ§ ð¥ð =ð¥ðxi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºç **éå** å®ä¹ä¸º ðð,ðQi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶å«ä¹æ¯æææ»¡è¶³è¯¥å±æ§çå¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæè²æ¹æ¡ï¼éåçå¤§å°å°±æ¯æ»¡è¶³è¯¥å±æ§çæè²æ¹æ¡æ°ï¼éåå çå ç´ ç¸å½äºæææ»¡è¶³è¯¥å±æ§çå¾ ðºâ²Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæè²å¾ï¼

åå°é¢ç®ï¼ãç¸é»çç»ç¹å¿ é¡»æåä¸ç§é¢è²ãï¼å¯ä»¥çè§£ä¸ºè¥å¹²ä¸ª ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåçäº¤éï¼å æ­¤å¯ä»¥ååº

ð¹(ð)=â£â(ð,ð)âððð,ðâ£F(S)=|â(i,j)âSQi,j|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸è¿°å¼å­å³è¾¹çå«ä¹å°±æ¯è¯´å¯¹äº S å çæ¯ä¸æ¡è¾¹ (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ»¡è¶³ ð¥ð =ð¥ðxi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæè²æ¹æ¡æ°ï¼ä¹å°±æ¯ ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æ¯ä¸æ¯å¾æå®¹æ¥çå³éäºï¼ç±äºå®¹æ¥åçæ¬èº«æ²¡æäºå ç»çå½¢å¼ï¼å æ­¤æä»¬æ **ææ** çè¾¹ (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å°å° ð =ð(ð+1)2T=n(n+1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ´æ°ä¸ï¼åè®¾å° (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å°ä¸º ð,1 â¤ð â¤ðk,1â¤kâ¤T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ ðð,ðQi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å°ä¸º ððQk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). é£ä¹å±æ§ ð¥ð =ð¥ðxi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå®ä¹ä¸º ððPk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

åæ¶ S å¯ä»¥è¡¨ç¤ºä¸ºè¥å¹²ä¸ª k ç»æçéåï¼å³ ð âº ð¾ ={ð1,ð2,â¯,ðð}SâºK={k1,k2,â¯,km}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).ï¼ä¹å°±æ¯è¯´æä»¬å¨è¾¹éä¸æ°éé´å»ºç«äºç­ä»·å ³ç³»ï¼ï¼

è E å¯¹åºéå ð ={1,2,â¯,ð(ð+1)2}M={1,2,â¯,n(n+1)2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). äºæ¯ä¹

ð¹(ð)âºð¹({ðð})=â£âðððððâ£F(S)âºF({ki})=|âkiQki|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### éååæ

é£ä¹è¦æ±çå¼å­å±å¼

ð´ðð =âð¾âð(â1)|ð¾|â1â£âððâð¾ðððâ£=âð|ðð|ââð<ð|ððâ©ðð|+âð<ð<ð|ððâ©ððâ©ðð|ââ¯+(â1)ðâ1â£ðâð=1ððâ£Ans=âKâM(â1)|K|â1|âkiâKQki|=âi|Qi|ââi<j|Qiâ©Qj|+âi<j<k|Qiâ©Qjâ©Qk|ââ¯+(â1)Tâ1|âi=1TQi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯å°±åºç°äºå®¹æ¥åççå±å¼å½¢å¼ï¼å æ­¤å¯¹è¿ä¸ªå¼å­éåæ¨å¯¼

ð´ðð =â£ðâð=1ððâ£Ans=|âi=1TQi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åèèç­å¼å³è¾¹çå«ä¹ï¼åªè¦æ»¡è¶³ 1 â¼ð1â¼T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»»ä¸æ¡ä»¶å³å¯ï¼ä¹å°±æ¯å­å¨ä¸¤ä¸ªç¹åè²ï¼ä¸ä¸å®ç¸é»ï¼çæè²æ¹æ¡æ°ï¼èæä»¬ç¥éæè²æ¹æ¡çå ¨éæ¯ ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶ |ð| =ðð|U|=mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). èè½¬åä¸ºè¡¥éï¼å°±æ¯æ±ä¸¤ä¸¤å¼è²çæè²æ¹æ¡æ°ï¼å³ ð´ðð =ð!(ðâð)!Amn=m!(mân)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). å æ­¤

ð´ðð =ððâð´ððAns=mnâAmn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§£å³è¿éé¢ï¼æä»¬é¦å æ½è±¡åºé¢ç®æ°å­¦å½¢å¼ï¼ç¶åä»é¢ç®ä¸­ä¿¡æ¯éæå¤§çæ¡ä»¶ï¼ð¹(ð)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½æ°çå®ä¹å ¥æï¼å°å ¶è½¬åä¸ºéåçäº¤å¹¶è¡¥ï¼ç¶åå°å¼å­è½¬åä¸ºå®¹æ¥åççå½¢å¼ï¼å¹¶ **éåæ¨å¯¼** åºæç»çç»æï¼è¿éé¢ä½ç°çæ­£æ¯å®¹æ¥åççéç¨ï¼

## æ°è®ºä¸­çå®¹æ¥

ä½¿ç¨å®¹æ¥åçè½å¤å·§å¦å°æ±è§£ä¸äºæ°è®ºé®é¢ï¼

### å®¹æ¥åçæ±æå¤§å ¬çº¦æ°ä¸º k çæ°å¯¹ä¸ªæ°

èèä¸é¢çé®é¢ï¼

æ±æå¤§å ¬çº¦æ°ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°å¯¹ä¸ªæ°

è®¾ 1 â¤ð¥,ð¦ â¤ð1â¤x,yâ¤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(ð)f(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºæå¤§å ¬çº¦æ°ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæåºæ°å¯¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼æ± ð(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð(ð)f(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è¿éé¢åºç¶å¯ä»¥ç¨æ¬§æå½æ°æè«æ¯ä¹æ¯åæ¼çæ¹æ³æ¥åï¼ä½æ¯é½ä¸å¦ç¨å®¹æ¥åçæ¥çç®åï¼

ç±å®¹æ¥åçå¯ä»¥å¾ç¥ï¼å æ¾å°ææä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **å ¬çº¦æ°** çæ°å¯¹ï¼åä»ä¸­åé¤ææä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä¸º **å ¬çº¦æ°** çæ°å¯¹ï¼ä½ä¸çæ°å¯¹å°±æ¯ä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **æå¤§å ¬çº¦æ°** çæ°å¯¹ï¼å³ ð(ð) =f(k)=![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **å ¬çº¦æ°** çæ°å¯¹ä¸ªæ° ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä¸º **å ¬çº¦æ°** çæ°å¯¹ä¸ªæ°ï¼

è¿ä¸æ­¥å¯åç°ï¼ä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä¸º **å ¬çº¦æ°** çæ°å¯¹ä¸ªæ°ç­äºææä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä¸º **æå¤§å ¬çº¦æ°** çæ°å¯¹ä¸ªæ°ä¹åï¼äºæ¯ï¼å¯ä»¥ååºå¦ä¸è¡¨è¾¾å¼ï¼

ð(ð)=â(ð/ð)â2âðâðâ¤ðâð=2ð(ðâð)f(k)=â(N/k)â2ââi=2iâkâ¤Nf(iâk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºå½ ð >ð/2k>N/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æä»¬å¯ä»¥ç´æ¥ç®åº ð(ð) =â(ð/ð)â2f(k)=â(N/k)â2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤æä»¬å¯ä»¥åè¿æ¥ï¼ä» ð(ð)f(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç®å° ð(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥äºï¼äºæ¯ï¼æä»¬ä½¿ç¨å®¹æ¥åçå®æäºæ¬é¢ï¼

```text 1 2 3 4 ``` |  ```text for ( long long k = N ; k >= 1 ; k \-- ) { f [ k ] = ( N / k ) * ( N / k ); for ( long long i = k \+ k ; i <= N ; i += k ) f [ k ] -= f [ i ]; } ```   
---|---  
  
ä¸è¿°æ¹æ³çæ¶é´å¤æåº¦ä¸º ð(âðð=1ð/ð) =ð(ðâðð=11/ð) =ð(ðlogâ¡ð)O(âi=1NN/i)=O(Nâi=1N1/i)=O(Nlogâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

éèµ ä¸åç»éªä¾å¤§å®¶ç»æï¼

  * [Luogu P2398 GCD SUM](https://www.luogu.com.cn/problem/P2398)
  * [Luogu P2158[SDOI2008] ä»ªä»é](https://www.luogu.com.cn/problem/P2158)
  * [Luogu P1447[NOI2010] è½ééé](https://www.luogu.com.cn/problem/P1447)

### å®¹æ¥åçæ¨å¯¼æ¬§æå½æ°

èèä¸é¢çé®é¢ï¼

æ¬§æå½æ°å ¬å¼

æ±æ¬§æå½æ° ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð(ð) =|{1 â¤ð¥ â¤ð|gcd(ð¥,ð) =1}|Ï(n)=|{1â¤xâ¤n|gcd(x,n)=1}|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç´æ¥è®¡ç®æ¯ ð(ðlogâ¡ð)O(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼ç¨çº¿æ§ç­æ¯ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼ææç­æ¯ ð(ð23)O(n23)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼è¯è¯´ä¸éæ°è®ºå ¥é¨é¢ç¨å®¹æ¥åä¸ºä»ä¹è¿è¦æ¯å°ææç­ä¸ï¼ï¼æ¥ä¸æ¥èèç¨å®¹æ¥æ¨åºæ¬§æå½æ°çå ¬å¼

å¤æ­ä¸¤ä¸ªæ°æ¯å¦äºè´¨ï¼é¦å åè§£è´¨å æ°

ð=ðâð=1ððððn=âi=1kpici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹å°±è¦æ±å¯¹äºä»»æ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ä¸æ¯ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å³ ðð â¤ð¥piâ¤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). æå®å½ä½å±æ§ï¼å¯¹åºçéåä¸º ððSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤æ

ð(ð)=â£ðâð=1ððâ£=|ð|ââ£ðâð=1ââððâ£Ï(n)=|âi=1kSi|=|U|â|âi=1kSiâ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¨éå¤§å° |ð| =ð|U|=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è ââððSiâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºçæ¯ ðð â£ð¥piâ£x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææçéåï¼æ¾ç¶ |ââðð| =ððð|Siâ|=npi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ç±æ­¤æ¨åº

â£âðð<ðð+1ðððâ£=ðâððð|âai<ai+1Sai|=nâpai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤å¯å¾

ð(ð)=ðââðððð+âð<ððððððââ¯+(â1)ððð1ð2â¯ðð=ð(1â1ð1)(1â1ð2)â¯(1â1ðð)=ððâð=1(1â1ðð)Ï(n)=nââinpi+âi<jnpipjââ¯+(â1)knp1p2â¯pk=n(1â1p1)(1â1p2)â¯(1â1pk)=nâi=1k(1â1pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯æ¬§æå½æ°çæ°å­¦è¡¨ç¤ºå¦

## å®¹æ¥åçä¸è¬å

å®¹æ¥åçå¸¸ç¨äºéåçè®¡æ°é®é¢ï¼èå¯¹äºä¸¤ä¸ªéåçå½æ° ð(ð),ð(ð)f(S),g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¥

ð(ð)=âðâðð(ð)f(S)=âTâSg(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹å°±æ

ð(ð)=âðâð(â1)|ð|â|ð|ð(ð)g(S)=âTâS(â1)|S|â|T|f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### è¯æ

æ¥ä¸æ¥æä»¬ç®åè¯æä¸ä¸ï¼æä»¬ä»ç­å¼çå³è¾¹å¼å§æ¨ï¼

âðâð(â1)|ð|â|ð|ð(ð)=âðâð(â1)|ð|â|ð|âðâðð(ð)=âðð(ð)âðâðâð(â1)|ð|â|ð|âTâS(â1)|S|â|T|f(T)=âTâS(â1)|S|â|T|âQâTg(Q)=âQg(Q)âQâTâS(â1)|S|â|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬åç°ååé¨åçæ±åä¸ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å ³ï¼å æ­¤æååé¨åç ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¤ï¼

=âðð(ð)âðâ(ðâð)(â1)|ðâð|â|ð|=âQg(Q)âTâ(SâQ)(â1)|SâQ|â|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®°å ³äºéå ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½æ° ð¹(ð) =âðâð( â1)|ð|â|ð|F(P)=âTâP(â1)|P|â|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶åç®è¿ä¸ªå½æ°ï¼

ð¹(ð)=âðâð(â1)|ð|â|ð|=|ð|âð=0(|ð|ð)(â1)|ð|âð=|ð|âð=0(|ð|ð)1ð(â1)|ð|âð=(1â1)|ð|=0|ð|F(P)=âTâP(â1)|P|â|T|=âi=0|P|(|P|i)(â1)|P|âi=âi=0|P|(|P|i)1i(â1)|P|âi=(1â1)|P|=0|P|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤åæ¥çå¼å­çå¼æ¯

âðð(ð)âðâ(ðâð)(â1)|ðâð|â|ð|=âðð(ð)ð¹(ðâð)=âðð(ð)â 0|ðâð|âQg(Q)âTâ(SâQ)(â1)|SâQ|â|T|=âQg(Q)F(SâQ)=âQg(Q)â 0|SâQ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæåç°ï¼ä» å½ |ð âð| =0|SâQ|=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶æ 00 =100=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¶ ð =ðQ=S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ç­æ¡çè´¡ç®å°±æ¯ ð(ð)g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä»æ¶ä¾¯ 0|ðâð| =00|SâQ|=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯¹ç­æ¡æ è´¡ç®ï¼äºæ¯å¾å°

âðð(ð)â 0|ðâð|=ð(ð)âQg(Q)â 0|SâQ|=g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»¼ä¸æè¿°ï¼å¾è¯ï¼

### æ¨è®º

è¯¥å½¢å¼è¿æè¿æ ·ä¸ä¸ªæ¨è®ºï¼å¨å ¨é ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼å¯¹äºå½æ° ð(ð),ð(ð)f(S),g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ

ð(ð)=âðâðð(ð)f(S)=âSâTg(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹

ð(ð)=âðâð(â1)|ð|â|ð|ð(ð)g(S)=âSâT(â1)|T|â|S|f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªæ¨è®ºå ¶å®å°±æ¯è¡¥éå½¢å¼ï¼è¯æ³ç±»ä¼¼ï¼

## DAG è®¡æ°

DAG è®¡æ°

å¯¹ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹å¸¦æ å·çæåæ ç¯å¾è¿è¡è®¡æ°ï¼å¯¹ 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼ð â¤5 Ã103nâ¤5Ã103![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### ç´æ¥ DP

èè DPï¼å®ä¹ ð[ð,ð]f[i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ç DAGï¼æ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¹ä¸ªå ¥åº¦ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¾çä¸ªæ°ï¼åè®¾å»æè¿ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹åï¼æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹å ¥åº¦ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å¨å»æåè¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹è³å°ä¸è¿ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ä¸­çæå ä¸ªæè¿è¾¹ï¼å³ 2ð â12jâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§æ åµï¼èè¿ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹é¤äºä¸ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹è¿è¾¹ï¼è¿å¯ä»¥ä¸å©ä¸çç¹ä»»æè¿è¾¹ï¼æ 2ðâðâð2iâjâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§æ åµï¼å æ­¤æ¹ç¨å¦ä¸ï¼

ð[ð,ð]=(ðð)ðâðâð=1(2ðâ1)ð2(ðâðâð)ðð[ðâð,ð]f[i,j]=(ij)âk=1iâj(2jâ1)k2(iâjâk)jf[iâj,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¡ç®ä¸å¼çå¤æåº¦æ¯ ð(ð3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

### æ¾å®½éå¶

ä¸è¿° DP çå®ä¹æ¯æ°å¥½ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹å ¥åº¦ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), å¤ªè¿äºä¸¥æ ¼ï¼å¯ä»¥æ¾å®½ä¸ºè³å° ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹å ¥åº¦ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´æ¥å®ä¹ ð[ð]f[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ç DAG ä¸ªæ°ï¼å¯ä»¥ç´æ¥å®¹æ¥ï¼èèéåºç ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ï¼è¿ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹å¯ä»¥åå©ä¸ç ð âðiâj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹æä»»æçè¿è¾¹ï¼å³ (2ðâð)ð =2(ðâð)ð(2iâj)j=2(iâj)j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§æ åµï¼

ð[ð]=ðâð=1(â1)ðâ1(ðð)2(ðâð)ðð[ðâð]f[i]=âj=1i(â1)jâ1(ij)2(iâj)jf[iâj]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¡ç®ä¸å¼çå¤æåº¦æ¯ ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

## Min-max å®¹æ¥

å¯¹äºæ»¡è¶³ [å ¨åº](../../order-theory/#ååºé) å ³ç³»å¹¶ä¸å ¶ä¸­å ç´ æ»¡è¶³å¯å åæ§çåºå {ð¥ð}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å ¶é¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®¾ ð ={1,2,3,â¯,ð}S={1,2,3,â¯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæï¼

maxðâðð¥ð=âðâð(â1)|ð|â1minðâðð¥ðmaxiâSxi=âTâS(â1)|T|â1minjâTxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)minðâðð¥ð=âðâð(â1)|ð|â1maxðâðð¥ðminiâSxi=âTâS(â1)|T|â1maxjâTxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**è¯æï¼** èèåä¸ä¸ªå°ä¸è¬å®¹æ¥åççæ å°ï¼å¯¹äº ð¥ âðxâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°çå ç´ ï¼é£ä¹æä»¬å®ä¹ä¸ä¸ªæ å° ð :ð¥ â¦{1,2,â¯,ð}f:xâ¦{1,2,â¯,k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶è¿æ¯ä¸ä¸ªåå°ï¼

é£ä¹å®¹æåç°ï¼å¯¹äº ð¥,ð¦ âðx,yâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(min(ð¥,ð¦)) =ð(ð¥) â©ð(ð¦)f(min(x,y))=f(x)â©f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(max(ð¥,ð¦)) =ð(ð¥) âªð(ð¦)f(max(x,y))=f(x)âªf(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤æä»¬å¾å°ï¼

â£ð(maxðâðð¥ð)â£=â£âðâðð(ð¥ð)â£=âðâð(â1)|ð|â1â£âðâðð(ð¥ð)â£=âðâð(â1)|ð|â1â£ð(minðâðð¥ð)â£|f(maxiâSxi)|=|âiâSf(xi)|=âTâS(â1)|T|â1|âjâTf(xj)|=âTâS(â1)|T|â1|f(minjâTxj)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¶ååæ |ð(maxðâðð¥ð)||f(maxiâSxi)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ å°å maxðâðð¥ðmaxiâSxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç±»ä¼¼çï¼

è¯æ¯ï¼

ä½æ¯ä½ å¯è½è§å¾è¿ä¸ªå¼å­éå¸¸è ¢ï¼æå¤§å¼ææå¯ä»¥ç´æ¥æ±ï¼ä¹æä»¥ min-max å®¹æ¥è¿ä¹éè¦ï¼æ¯å ä¸ºå®å¨ææä¸ä¹æ¯æç«çï¼å³ï¼

ð¸(maxðâðð¥ð)=âðâð(â1)|ð|â1ð¸(minðâðð¥ð)E(maxiâSxi)=âTâS(â1)|T|â1E(minjâTxj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¸(minðâðð¥ð)=âðâð(â1)|ð|â1ð¸(maxðâðð¥ð)E(miniâSxi)=âTâS(â1)|T|â1E(maxjâTxj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**è¯æï¼** æä»¬èèè®¡ç®ææçä¸ç§æ¹æ³ï¼

ð¸(maxðâðð¥ð)=âð¦ð(ð¦=ð¥)maxðâðð¦ðE(maxiâSxi)=âyP(y=x)maxjâSyj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªé¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºåï¼

æä»¬å¯¹åé¢ç maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿ç¨ä¹åçå¼å­ï¼

ð¸(maxðâðð¥ð)=âð¦ð(ð¦=ð¥)maxðâðð¦ð=âð¦ð(ð¦=ð¥)âðâð(â1)|ð|â1minðâðð¦ðE(maxiâSxi)=âyP(y=x)maxjâSyj=âyP(y=x)âTâS(â1)|T|â1minjâTyj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è°æ¢æ±åé¡ºåºï¼

ð¸(maxðâðð¥ð)=âð¦ð(ð¦=ð¥)âðâð(â1)|ð|â1minðâðð¦ð=âðâð(â1)|ð|â1âð¦ð(ð¦=ð¥)minðâðð¦ð=âðâð(â1)|ð|â1ð¸(minðâðð¦ð)E(maxiâSxi)=âyP(y=x)âTâS(â1)|T|â1minjâTyj=âTâS(â1)|T|â1âyP(y=x)minjâTyj=âTâS(â1)|T|â1E(minjâTyj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç±»ä¼¼çï¼

è¯æ¯ï¼

è¿ææ´å¼ºçï¼

kthmaxâ¡ð¥ððâð=âðâð(â1)|ð|âð(|ð|â1ðâ1)minðâðð¥ðkthmaxâ¡xiiâS=âTâS(â1)|T|âk(|T|â1kâ1)minjâTxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)kthminâ¡ð¥ððâð=âðâð(â1)|ð|âð(|ð|â1ðâ1)maxðâðð¥ðkthminâ¡xiiâS=âTâS(â1)|T|âk(|T|â1kâ1)maxjâTxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¸(kthmaxâ¡ð¥ððâð)=âðâð(â1)|ð|âð(|ð|â1ðâ1)ð¸(minðâðð¥ð)E(kthmaxâ¡xiiâS)=âTâS(â1)|T|âk(|T|â1kâ1)E(minjâTxj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¸(kthminâ¡ð¥ððâð)=âðâð(â1)|ð|âð(|ð|â1ðâ1)ð¸(maxðâðð¥ð)E(kthminâ¡xiiâS)=âTâS(â1)|T|âk(|T|â1kâ1)E(maxjâTxj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§å®è¥ ð <ðn<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å (ðð) =0(nm)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**è¯æï¼** ä¸å¦¨è®¾ â1 â¤ð <ð,ð¥ð â¤ð¥ð+1â1â¤i<n,xiâ¤xi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæï¼

âðâð(â1)|ð|âð(|ð|â1ðâ1)minðâðð¥ð=âðâðð¥ðâðâð(â1)|ð|âð(|ð|â1ðâ1)[ð¥ð=minðâðð¥ð]=âðâðð¥ððâð=ð(ðâððâ1)(ðâ1ðâ1)(â1)ðâðâTâS(â1)|T|âk(|T|â1kâ1)minjâTxj=âiâSxiâTâS(â1)|T|âk(|T|â1kâ1)[xi=minjâTxj]=âiâSxiâj=kn(nâijâ1)(jâ1kâ1)(â1)jâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå ä¸ºæç»åæç­å¼ï¼(ðð)(ðð) =(ðð)(ðâððâð)(ab)(bc)=(ac)(aâcbâc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æï¼

âðâð(â1)|ð|âð(|ð|â1ðâ1)minðâðð¥ð=âðâðð¥ððâð=ð(ðâððâ1)(ðâ1ðâ1)(â1)ðâð=âðâðð¥ððâð=ð(ðâððâ1)(ðâðâð+1ðâð)(â1)ðâð=âðâð(ðâððâ1)ð¥ððâð=ð(ðâðâð+1ðâð)(â1)ðâð=âðâð(ðâððâ1)ð¥ððâðâð+1âð=0(ðâðâð+1ð)(â1)ðâTâS(â1)|T|âk(|T|â1kâ1)minjâTxj=âiâSxiâj=kn(nâijâ1)(jâ1kâ1)(â1)jâk=âiâSxiâj=kn(nâikâ1)(nâiâk+1jâk)(â1)jâk=âiâS(nâikâ1)xiâj=kn(nâiâk+1jâk)(â1)jâk=âiâS(nâikâ1)xiâj=0nâiâk+1(nâiâk+1j)(â1)j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ ð =ð âð +1i=nâk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼

(ðâððâ1)ðâðâð+1âð=0(ðâðâð+1ð)(â1)ð=1(nâikâ1)âj=0nâiâk+1(nâiâk+1j)(â1)j=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦åï¼

(ðâððâ1)ðâðâð+1âð=0(ðâðâð+1ð)(â1)ð=0(nâikâ1)âj=0nâiâk+1(nâiâk+1j)(â1)j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼

âðâð(ðâððâ1)ð¥ððâðâð+1âð=0(ðâðâð+1ð)(â1)ð=kthmaxðâðð¥ðâiâS(nâikâ1)xiâj=0nâiâk+1(nâiâk+1j)(â1)j=kthmaxiâSxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ä¸ä¸ä¸ªæ¯ç±»ä¼¼çï¼

è¯æ¯ï¼

æ ¹æ® min-max å®¹æ¥ï¼æä»¬è¿å¯ä»¥å¾å°ä¸é¢çå¼å­ï¼

lcmðâðð¥ð=âðâð(gcdðâðð¥ð)(â1)|ð|â1lcmiâSxi=âTâS(gcdjâTxj)(â1)|T|â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º lcm,gcd,ð1,ðâ1lcm,gcd,a1,aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«ç¸å½äº max,min, +, âmax,min,+,â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ¯è¯´ç¸å½äºå¯¹äºææ°åäºä¸ä¸ª min-max å®¹æ¥ï¼èªç¶å°±æ¯å¯¹çäº

## PKUWC2018 éæºæ¸¸èµ°

[PKUWC2018 éæºæ¸¸èµ°](https://loj.ac/problem/2542)

ç»å®ä¸æ£µ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹çæ ï¼ä½ ä» ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼æ¯æ¬¡ç­æ¦çéæºéæ©ä¸æ¡ä¸æå¨ç¹ç¸é»çè¾¹èµ°è¿å»ï¼

æ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡è¯¢é®ï¼æ¯æ¬¡è¯¢é®ç»åºä¸ä¸ªéå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±å¦æä» ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåä¸ç´éæºæ¸¸èµ°ï¼ç´å°ç¹é ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çç¹é½è³å°ç»è¿ä¸æ¬¡çè¯ï¼æææ¸¸èµ°å æ­¥ï¼

ç¹å«å°ï¼ç¹ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³èµ·ç¹ï¼è§ä¸ºä¸å¼å§å°±è¢«ç»è¿äºä¸æ¬¡ï¼

å¯¹ 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼

1 â¤ð â¤18,1 â¤ð â¤5000,1 â¤|ð| â¤ð1â¤nâ¤18,1â¤Qâ¤5000,1â¤|S|â¤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æææ¸¸èµ°çæ­¥æ°ä¹å°±æ¯æ¸¸èµ°çæ¶é´ï¼é£ä¹è®¾éæºåé ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç¬¬ä¸æ¬¡èµ°å°ç»ç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´ï¼é£ä¹æä»¬è¦æ±çå°±æ¯

ð¸(maxðâðð¥ð)E(maxiâSxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½¿ç¨ min-max å®¹æ¥å¯ä»¥å¾å°

ð¸(maxðâðð¥ð)=ð¸(âðâð(â1)|ð|â1minðâðð¥ð)=âðâð(â1)|ð|â1ð¸(minðâðð¥ð)E(maxiâSxi)=E(âTâS(â1)|T|â1miniâTxi)=âTâS(â1)|T|â1E(miniâTxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºä¸ä¸ªéå ð â[ð]Tâ[n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèæ±åº ð¹(ð) =ð¸(minðâðð¥ð)F(T)=E(miniâTxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

èè ð¸(minðâðð¥ð)E(miniâTxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå«ä¹ï¼æ¯ç¬¬ä¸æ¬¡èµ°å° ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æä¸ä¸ªç¹çæææ¶é´ï¼ä¸å¦¨è®¾ ð(ð)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºä»ç»ç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼ç¬¬ä¸æ¬¡èµ°å° ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æä¸ªç»ç¹çæææ¶é´ï¼

  * å¯¹äº ð âðiâT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) =0f(i)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å¯¹äº ð âðiâT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) =1 +1deg(ð)â(ð,ð)âð¸ð(ð)f(i)=1+1deg(i)â(i,j)âEf(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦æç´æ¥é«æ¯æ¶å ï¼å¤æåº¦ ð(ð3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æä»¬å¯¹æ¯ä¸ª ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½è®¡ç® ð¹(ð)F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ»å¤æåº¦å°±æ¯ ð(2ðð3)O(2nn3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è½æ¥åï¼æä»¬ä½¿ç¨æ ä¸æ¶å çæå·§ï¼

ä¸å¦¨è®¾æ ¹ç»ç¹æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç»ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¶äº²æ¯ ðð¢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºå¶å­ç»ç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(ð)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªä¼å ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¶äº²æå ³ï¼ä¹å¯è½ ð(ð) =0f(i)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£æ ·æ´å¥½ï¼ï¼å æ­¤æä»¬å¯ä»¥æ ð(ð)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºæ ð(ð) =ð´ð +ðµðð(ðð)f(i)=Ai+Bif(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼å ¶ä¸­ ð´ð,ðµðAi,Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥å¿«éè®¡ç®ï¼

å¯¹äºéå¶ç»ç¹ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèå®çå¿å­åºå ð1,â¯,ððj1,â¯,jk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ð(ðð) =ð´ðð +ðµððð(ð)f(je)=Aje+Bjef(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å¯ä»¥å¾å°

ð(ð)=1+1degâ¡(ð)ðâð=1(ð´ðð+ðµððð(ð))+ð(ðð)degâ¡(ð)f(i)=1+1degâ¡(i)âe=1k(Aje+Bjef(i))+f(pi)degâ¡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹åæ¢ä¸ä¸å¯ä»¥å¾å°

ð(ð)=degâ¡(ð)+âðð=1ð´ððdegâ¡(ð)ââðð=1ðµðð+ð(ðð)degâ¡(ð)ââðð=1ðµððf(i)=degâ¡(i)+âe=1kAjedegâ¡(i)ââe=1kBje+f(pi)degâ¡(i)ââe=1kBje![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯æä»¬æ ð(ð)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åæäº ð´ð +ðµðð(ðð)Ai+Bif(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼è¿æ ·å¯ä»¥ä¸ç´åæ¨å°æ ¹ç»ç¹ï¼èæ ¹ç»ç¹æ²¡æç¶äº²ï¼ä¹å°±æ¯è¯´

ð(1)=degâ¡(1)+âðð=1ð´ððdegâ¡(1)ââðð=1ðµððf(1)=degâ¡(1)+âe=1kAjedegâ¡(1)ââe=1kBje![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§£ä¸ä¸è¿ä¸ªæ¹ç¨æä»¬å°±å¾å°äº ð(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä»ä¸å¾ä¸æ¨ä¸æ¬¡å°±å¾å°äºæ¯ä¸ªç¹ç ð(ð)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ ð¹(ð) =ð(ð¥)F(T)=f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¶é´å¤æåº¦ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿æ ·ï¼æä»¬å¯ä»¥å¯¹äºæ¯ä¸ä¸ª ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç®åº ð¹(ð)F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¶é´å¤æåº¦ ð(2ðð)O(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åå°å®¹æ¥çé¨åï¼æä»¬ç¥é ð¸(maxðâðð¥ð) =âðâð( â1)|ð|â1ð¹(ð)E(maxiâSxi)=âTâS(â1)|T|â1F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸å¦¨è®¾ ð¹â²(ð) =( â1)|ð|â1ð¹(ð)Fâ²(T)=(â1)|T|â1F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹è¿ä¸æ­¥å¾å° ð¸(maxðâðð¥ð) =âðâðð¹â²(ð)E(maxiâSxi)=âTâSFâ²(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å¯ä»¥ä½¿ç¨ FMTï¼ä¹å«å­éåç¼åï¼æè FWT æåæ¢ï¼å¨ ð(2ðð)O(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å å¯¹æ¯ä¸ª ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç®åº ð¸(maxðâðð¥ð)E(maxiâSxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·å°±å¯ä»¥ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç­è¯¢é®äºï¼

### ä¹ é¢

  * [ABC331- G - Collect Them All](https://atcoder.jp/contests/abc331/tasks/abc331_g)
  * [æ´è°· P4707 éè¿ç°ä¸](https://www.luogu.com.cn/problem/P4707)

## åèæç®

[æµ æ¢å®¹æ¥åç - çè¿ª](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf)ï¼2013 å¹´ä¿¡æ¯å­¦å¥¥æå¹å ä¸­å½å½å®¶éåééåè®ºæé

[ææ å·ç DAG è®¡æ°ç³»åé®é¢ - Cyhlnj](https://www.cnblogs.com/cjoieryl/p/10078167.html)

[å ¨åºå ³ç³» - Wikipedia](https://en.wikipedia.org/wiki/Total_order)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/inclusion-exclusion-principle.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/inclusion-exclusion-principle.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Peanut-Tang](https://github.com/Peanut-Tang), [HeRaNO](https://github.com/HeRaNO), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [ComeIntoCalm](https://github.com/ComeIntoCalm), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [Jerrycyx](https://github.com/Jerrycyx), [Jiangkangping](https://github.com/Jiangkangping), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [Lumos-exe](https://github.com/Lumos-exe), [lychees](https://github.com/lychees), [megakite](https://github.com/megakite), [ouuan](https://github.com/ouuan), [sbofgayschool](https://github.com/sbofgayschool), [ShizuhaAki](https://github.com/ShizuhaAki), [StableAgOH](https://github.com/StableAgOH), [StudyingFather](https://github.com/StudyingFather), [tder6](https://github.com/tder6), [untitledunrevised](https://github.com/untitledunrevised), [UserUnauthorized](https://github.com/UserUnauthorized), [ZYStream](https://github.com/ZYStream)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
