# çº¿æ§è§ååºç¡ - OI Wiki

- Source: https://oi-wiki.org/math/linear-programming/

# çº¿æ§è§ååºç¡

## å¼å ¥

çº¿æ§è§åï¼linear programming, LPï¼æ¯ç ç©¶çº¿æ§çº¦ææ¡ä»¶ä¸çº¿æ§ç®æ å½æ°æå¼é®é¢çæ¹æ³æ»ç§°ï¼æ¯è¿ç­¹å­¦çä¸ä¸ªåæ¯ï¼å¨å¤æ¹é¢åæåºç¨ï¼çº¿æ§è§åçæäºç¹æ®æ åµï¼å¦ç½ç»æµãå¤ååæµéç­é®é¢é½æå¯è½å¨ç®æ³ç«èµé¢ç®ä¸­åºç°ï¼ç®æ³ç«èµå¾å°ä¼åºç°åªè½ç¨çº¿æ§è§åç®æ³è§£å³çé®é¢ï¼ç»å¤§å¤æ°è¿ç±»é®é¢å¯ä»¥éè¿ç½ç»æµå»ºæ¨¡ç­æ¹æ³æ´é«æå°è§£å³ï¼

### ä¸ä¸ªç®åçä¾å­

ä¸ä¸ªé®é¢è½å¤åæçº¿æ§è§åçå½¢å¼ï¼æ¢è¦æè¥å¹²ä¸ªçº¿æ§çº¦ææ¡ä»¶ï¼åè¦æçº¿æ§çç®æ å½æ°ï¼

èèä¸é¢çä¾å­ï¼

ä¾å­

æ©ç¹å¸å æ¯å¤©å¯ä»¥å¶ä½ä¸å®æ°éçå å­åæ²¹æ¡ï¼è¿ä¸¤ç§æ©é¤æ·±åé¡¾å®¢åç±ï¼ä¸ºäºæå¤§åå©æ¶¦ï¼å¸å å¸æå°½å¯è½å¤å°å¶ä½æ©ç¹ï¼ä½å¨å®é æä½ä¸­åå°é£æãæ¶é´ç­å¤ç§èµæºçéå¶ï¼ä¸ºæ­¤ï¼å¸å ç»è®¡äºå¶ä½æ¯ä»½æ©ç¹æéçé£æç¨éãå¶ä½æ¶é´åå ¶å¯¹åºçå©æ¶¦ï¼å ·ä½å¦ä¸è¡¨æç¤ºï¼

æ©ç¹| æ¤ç©æ²¹| é¢ç²| æ¶é´| å©æ¶¦  
---|---|---|---|---  
å å­| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
æ²¹æ¡| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
åè®¾å¸å æ¯å¤©æå¤å¯ä»¥è´­å ¥ 6666![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½çæ¤ç©æ²¹å 6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½çé¢ç²ï¼å¹¶ä¸æå¤å¯ä»¥æå ¥ 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½çå¶ä½æ¶é´ï¼é£ä¹ï¼å¸å åºå¦ä½åçå®æå å­åæ²¹æ¡ççäº§æ°éï¼æè½ä½¿æ¯å¤©çå©æ¶¦æå¤§åï¼

ç¨æ°å­¦è¯­è¨æè¿°ï¼å¯ä»¥è®¾ ð¥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯å¸å å¶ä½å å­åæ²¹æ¡çæ°éï¼é£ä¹ï¼ãæ»å ±éè¦çæ¤ç©æ²¹ä¸è¶ è¿ 6666![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½ãå°±å¯ä»¥è¡¨ç¤ºä¸º

4ð¥1+7ð¥2â¤66.4x1+7x2â¤66.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±»ä¼¼å°ï¼ãæ»å ±éè¦çé¢ç²ä¸è¶ è¿ 6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½ãåãæ»å ±éè¦çæ¶é´ä¸è¶ è¿ 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½ãå¯ä»¥è¡¨ç¤ºä¸º

7ð¥1+3ð¥2â¤60,8ð¥1+6ð¥2â¤96.7x1+3x2â¤60,8x1+6x2â¤96.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦å¤ï¼å¸å ä¸å¯è½çäº§åºè´æ°åä½çæ©ç¹ï¼æä»¥ï¼è¿ææ¡ä»¶

ð¥1,ð¥2â¥0.x1,x2â¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¸å å°±æ¯è¦å¨è¿äºéå¶ä¸ï¼æå¤§åå©æ¶¦ï¼

ð§=5ð¥1+6ð¥2.z=5x1+6x2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯ä¸ä¸ªå ¸åççº¿æ§è§åé®é¢ï¼å®çç®æ å½æ°æ¯å ³äºå³ç­åéççº¿æ§å½æ°ï¼çº¦ææ¡ä»¶åç±å³ç­åéææççº¿æ§ç­å¼æä¸ç­å¼ç»æï¼

### å¾è§£æ³

å¯¹äºåªæä¸¤ä¸ªå³ç­åéççº¿æ§è§åé®é¢ï¼å¯ä»¥éè¿å¾è§£æ³ç´è§å°è§£å³é®é¢ï¼

èèæ¬èçé®é¢

maxð¥1,ð¥2ð§=5ð¥1+6ð¥2subject toÂ 4ð¥1+7ð¥2â¤66,7ð¥1+3ð¥2â¤60,8ð¥1+6ð¥2â¤96,ð¥1,ð¥2â¥0maxx1,x2z=5x1+6x2subject toÂ 4x1+7x2â¤66,7x1+3x2â¤60,8x1+6x2â¤96,x1,x2â¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹åºçå ä½å¾åï¼æåä¸è¡çº¦æè¡¨ç¤ºå¯éçç¹ (ð¥1,ð¥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½åºç°å¨ç¬¬ä¸è±¡éï¼å¦å¤çä¸ä¸ªçº¦æåè¡¨ç¤ºå¯éçç¹ä¸å®å¨ç´çº¿ 4ð¥1 +7ð¥2 =664x1+7x2=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãç´çº¿ 7ð¥1 +3ð¥2 =607x1+3x2=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç´çº¿ 8ð¥1 +6ð¥2 =968x1+6x2=96![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ¹ï¼è¿äºåºåçäº¤éï¼å¦ä¸å¾ç»¿è²åºåæç¤ºï¼å°±æ¯ææå¯ä¾éæ©çç¹çéåï¼

![](./images/linear-programming.svg)

æ¥ä¸æ¥è¦æå¤§å ð§ =5ð¥1 +6ð¥2z=5x1+6x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼å¦æå°è¯¥ç­å¼è§ä½ç´çº¿ 5ð¥1 +6ð¥2 =ð§5x1+6x2=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹ç¨ï¼åéç ð§z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååï¼å°å¾å°ä¸æå¹³è¡ç´çº¿ï¼ä¸ ð§z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¶å¤§ï¼ç´çº¿å°±è¶é è¿å³ä¸æ¹ï¼å æ­¤ï¼åªéè¦ä¸æ­ç§»å¨ç´çº¿ç´è³è¾¾å°æä¸ä¸´çä½ç½®ï¼ä½¿å¾ååå³ä¸ç§»å¨ä¸ç¹ç¹ï¼ç´çº¿å°±ä¸ååå¾ä¸­æç¤ºåºåç¸äº¤ï¼æ­¤æ¶ç´çº¿å¯¹åºç ð§z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ææ±çæå¤§å¼ï¼

å¦å¾æç¤ºï¼è¿æ ·çæ å½¢åçå¨çº¢ç¹æç¤ºä½ç½®ï¼å®æ¯ç´çº¿ 4ð¥1 +7ð¥2 =664x1+7x2=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç´çº¿ 7ð¥1 +3ð¥2 =607x1+3x2=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäº¤ç¹ï¼èç«ä¸¤ç´çº¿æ¹ç¨å¯ç¥ï¼å®çåæ æ¯ (6,6)(6,6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¯æ¬é®é¢å¯ä¸çæä¼è§£ï¼æ©ç¹å¸å çæå¤§å©æ¶¦æ¯ ð§ =66z=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å½é®é¢æ¶åå¤äºä¸¤ä¸ªå³ç­åéæ¶ï¼å¾è§£æ³ä¸åéç¨ï¼ä½æ¯ï¼æ¬èçä¾å­ä¸­çä¸äºè§å¯ä»ç¶ææï¼çº¿æ§è§åé®é¢ä¸­çæ¯ä¸ªä¸ç­å¼çº¦æé½æè¿°äºä¸ä¸ªãåå¹³é¢ãï¼ææå¯è¡çè§£çéåå°±æ¯è¿äºãåå¹³é¢ãçäº¤éï¼å æ­¤ï¼æ»æ¯ä¸ä¸ªãå¸å¤è¾¹å½¢ãï¼è§åé®é¢çæä¼è§£æ»æ¯å¯ä»¥å¨è¯¥ãå¸å¤è¾¹å½¢ãçæä¸ªãé¡¶ç¹ãå¤åå¾ï¼è¿äºãé¡¶ç¹ãçåæ å¯ä»¥éè¿èç«è¿äºãåå¹³é¢ãçãè¾¹çãçæ¹ç¨æ±å¾ï¼å°è¿äºè§å¯æå±å°é«ç»´ç©ºé´ï¼å°±åå±åºäºä¸ä¸ªé«æçæ±è§£çº¿æ§è§åé®é¢çæ¹æ³ââåçº¯å½¢æ³ï¼è¿ä¹æ¯ç®æ³ç«èµä¸­æå¸¸åºç¨çæ¹æ³ï¼

å¦å¤ä¸ä¸ªå¼å¾æ³¨æçé®é¢æ¯ï¼ååä¸ï¼æ©ç¹å¸å å¶ä½çå å­åæ²¹æ¡é½ä¸æ¯æ éå¯åçï¼åºå½æ¯æä¸ªæ´æ°ï¼è½ç¶æ¬é¢æ±è§£è¿ç¨ä¸­æ²¡ææç¡®å°éå¶è¿ä¸ç¹ï¼ä½æ¯ç±äºæç»çæä¼è§£çç¡®æ¯æ´æ°ï¼æä»¥ï¼å³ä½¿å ä¸æ´æ°éå¶ï¼æ¬é¢çç­æ¡ä»ç¶æ¯å¯è¡çï¼ä½æ¯å¯¹äºå¾å¤è§åé®é¢ï¼æä¼è§£å¯è½æ æ³åå¾å¨æ´ç¹å¤ï¼è¿äºé®é¢å®é ä¸æ¯ä¸ç±»æ´æ°è§åé®é¢ï¼èéç®åççº¿æ§è§åé®é¢ï¼æ¬æçç»å°¾ç®åå°è®¨è®ºäºè¿ä¸ç±»é®é¢ï¼

## åºæ¬æ¦å¿µ

æ¬èä»ç»çº¿æ§è§åé®é¢çåºæ¬æ¦å¿µï¼

### çº¿æ§è§åé®é¢

ä¸ä¸ªçº¿æ§è§åé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éå¸¸ç±å¦ä¸ä¸¤é¨åç»æï¼

  * çº¿æ§ç®æ å½æ°ï¼å³å½¢å¦

ð(ð¥1,ð¥2,â¯,ð¥ð)=ð1ð¥1+ð2ð¥2+â¯+ððð¥ðf(x1,x2,â¯,xn)=c1x1+c2x2+â¯+cnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½æ°ï¼å ¶ä¸­ï¼ðð âðciâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸¸æ°ï¼

  * çº¿æ§çº¦æï¼å³å½¢å¦

ðð(ð¥1,ð¥2,â¯,ð¥ð)=ðð1ð¥1+ðð2ð¥2+â¯+ðððð¥ðâ¤(=,â¥)ððgj(x1,x2,â¯,xn)=aj1x1+aj2x2+â¯+ajnxnâ¤(=,â¥)bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çä¸ç­å¼æç­å¼çº¦æï¼å ¶ä¸­ï¼ððð,ðð âðaji,bjâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯å¸¸æ°ï¼

çº¿æ§è§åé®é¢ï¼å°±æ¯è¦å¨æ»¡è¶³æç»çº¦æçåæä¸ï¼æå¤§åæè æå°åç®æ å½æ°ï¼æ»¡è¶³æç»çº¦æçè§£ (ð¥1,ð¥2,â¯,ð¥ð) âðð(x1,x2,â¯,xn)âRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º **å¯è¡è§£** ï¼feasible solutionï¼ï¼å¨ææå¯è¡è§£ä¸­ï¼ä½¿å¾ç®æ å½æ°åå¾æå¼çè§£ç§°ä¸º **æä¼è§£** ï¼optimal solutionï¼ï¼

### æ åå½¢å¼

ä¸ºäºæ¹ä¾¿æè¿°åè¿ä¸æ­¥å¤çï¼éå¸¸éè¦æå®ä¸ä¸ªçº¿æ§è§åé®é¢çæ åå½¢å¼ï¼ä¸åæç®å¯è½æä¸åçè§å®æ¹å¼ï¼æ¬æè§å®çº¿æ§è§åçæ åå½¢å¼å¦ä¸ï¼

min{ð¥ð}ðâð=1ððð¥ðsubject toÂ ðâð=1ðððð¥ð=ððâ¥0,Â ð=1,â¯,ð,ð¥ðâ¥0,Â ð=1,â¯,ð.min{xi}âi=1ncixisubject toÂ âi=1najixi=biâ¥0,Â j=1,â¯,m,xiâ¥0,Â i=1,â¯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼çº¿æ§è§åé®é¢æ¯æå°åé®é¢ï¼ææå³ç­åéé½æéè´çº¦æï¼ä¸é¤æ­¤ä¹å¤åªå å«è¥å¹²å³ä¾§å¸¸ééè´çç­å¼çº¦æï¼å©ç¨ [ç©éµ](../linear-algebra/matrix/) å¯ä»¥æ´ä¸ºç®æ´å°è¡¨è¾¾è¿ä¸é®é¢ï¼

max{ððð¥:ð´ð¥=ðâ¥0,Â ð¥â¥0}.max{cTx:Ax=bâ¥0,Â xâ¥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð¥ =(ð¥ð) âððx=(xi)âRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å³ç­åéï¼ð =(ðð) âððb=(bj)âRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð´ =(ððð) âððÃðA=(aji)âRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯çº¦æä¸­æ¶åçå¸¸éï¼çº¿æ§è§åé®é¢çè§æ¨¡å°±æ¯æå®çå³ç­åéçæ°ç®åå®ççº¦æçä¸ªæ°ï¼

åéä¸ç­å¼

æ¬æä¸­ä¼å¤æ¬¡åºç°å ð â¥0bâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ ·çåéä¸ç­å¼ï¼ä¸è¬å°ï¼å¯¹äºåé ð¥,ð¦ âððx,yâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç­å¼ ð¥ â¤ð¦xâ¤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º âð(ð¥ð â¤ð¦ð)âi(xiâ¤yi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³éç»´å°è¿è¡å®æ°æä¹ä¸çæ¯è¾ï¼è¿ä¸å ³ç³»æ¯åéç©ºé´ä¸ç [ååºå ³ç³»](../order-theory/#äºå)ï¼ä¹å°±æ¯è¯´ï¼å­å¨ä¸¤ä¸ªåéæ æ³æ¯è¾çæ å½¢ï¼

æ åå½¢å¼çéååªæ¯ä¸ºäºè¡ææ¹ä¾¿ï¼èå¹¶æ²¡æä»»ä½ç¹å«ä¹å¤ï¼å ä¸ºä»»ä½çº¿æ§è§åé®é¢é½å¯ä»¥ç­ä»·å°åæä¸é¢çå ­ç§å½¢å¼ï¼

min{ððð¥:ð´ð¥=ð,Â ð¥â¥0},min{ððð¥:ð´ð¥â¥ð},min{ððð¥:ð´ð¥â¥ð,Â ð¥â¥0},max{ððð¥:ð´ð¥=ð,Â ð¥â¥0},max{ððð¥:ð´ð¥â¤ð},max{ððð¥:ð´ð¥â¤ð,Â ð¥â¥0}.min{cTx:Ax=b,Â xâ¥0},min{cTx:Axâ¥b},min{cTx:Axâ¥b,Â xâ¥0},max{cTx:Ax=b,Â xâ¥0},max{cTx:Axâ¤b},max{cTx:Axâ¤b,Â xâ¥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸åæä½å¯ä»¥å°ææçº¿æ§è§åé®é¢é½ç­ä»·å°è½¬åä¸ºè¿å ­ç§å½¢å¼ä¹ä¸ï¼

  1. éè¿æ·»å è´å·ï¼å³å° ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º âðâc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å®ææå¤§åé®é¢åæå°åé®é¢çç¸äºè½¬åï¼
  2. éè¿æ·»å è´å·ï¼å³å° ðððð¥ âªððajTxâªbj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢æ âðððð¥ âª âððâajTxâªâbj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å®æä¸ç­å¼çº¦æçä¸¤ç§æ¹åçç¸äºè½¬åï¼æå°ç­å¼çº¦æçå³ä¾§å¸¸éåä¸ºéè´æ°ï¼
  3. ææçç­å¼çº¦æ ðððð¥ =ððajTx=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥æ¿æ¢æä¸¤ä¸ªç¸åæ¹åçä¸ç­å¼çº¦æ ðððð¥ â¥ððajTxâ¥bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðððð¥ â¤ððajTxâ¤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. ææçä¸ç­å¼çº¦æ ðððð¥ â¤( â¥)ððajTxâ¤(â¥)bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥éè¿æ·»å éè´æ¾å¼åé ð ðsj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹å¼ï¼è½¬åä¸ºç­å¼çº¦æ ðððð¥ +( â)ð ð =ððajTx+(â)sj=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥åç¸åºçéè´çº¦æ ð ð â¥0sjâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  5. å¦ææä¸ªå³ç­åé ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ²¡æéè´çº¦æï¼é£ä¹ï¼å¯ä»¥å°å®æ¿æ¢æä¸¤ä¸ªéè´åéçå·®å¼ï¼å³ ð¥ð =ð¥+ð âð¥âðxj=xj+âxjâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¥+ð,ð¥âð â¥0xj+,xjââ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

éè¿è¿äºæä½è½¬åå¾å°ççº¿æ§è§åé®é¢çè§æ¨¡ä¸è¶ è¿åé®é¢çè§æ¨¡çäºåï¼èä¸è¿äºé®é¢çå¯è¡è§£åæä¼è§£é½å¾å®¹æç¸äºè½¬åï¼å æ­¤ï¼å¯¹äºä¸è¬å½¢å¼ççº¿æ§è§åé®é¢ï¼æ»æ¯å¯ä»¥é¦å å°å®è½¬åä¸ºæ åå½¢å¼ï¼æä¸è¿°å ­ç§å½¢å¼ä¹ä¸ï¼åè¿è¡æ±è§£ï¼

ä¾å­

èèçº¿æ§è§åé®é¢

max3ð¥1â2ð¥2+ð¥3subject toÂ 2ð¥1+3ð¥2+4ð¥3â¥1,3ð¥1+4ð¥2â¤5,5ð¥2âð¥3=â1,ð¥1,ð¥2â¥0.max3x1â2x2+x3subject toÂ 2x1+3x2+4x3â¥1,3x1+4x2â¤5,5x2âx3=â1,x1,x2â¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éè¿æä½ 1ã2 å 3 å¯ä»¥å°å®è½¬åä¸ºå½¢å¼ min{ððð¥ :ð´ð¥ â¥ð}min{cTx:Axâ¥b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³

minâ3ð¥1+2ð¥2âð¥3subject toÂ 2ð¥1+3ð¥2+4ð¥3â¥1,â3ð¥1â4ð¥2â¥â5,5ð¥2âð¥3â¥â1,â5ð¥2+ð¥3â¥1,ð¥1â¥0,ð¥2â¥0.minâ3x1+2x2âx3subject toÂ 2x1+3x2+4x3â¥1,â3x1â4x2â¥â5,5x2âx3â¥â1,â5x2+x3â¥1,x1â¥0,x2â¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éè¿æä½ 4 å 5 å¯ä»¥å°å®è½¬åä¸ºå½¢å¼ max{ððð¥ :ð´ð¥ =ð,Â ð¥ â¥0}max{cTx:Ax=b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³

max3ð¥1â2ð¥2+ð¥+3âð¥â3subject toÂ 2ð¥1+3ð¥2+4ð¥+3â4ð¥â3âð¥4=1,3ð¥1+4ð¥2+ð¥5=5,5ð¥2âð¥+3+ð¥â3=â1,ð¥1,ð¥2,ð¥+3,ð¥â3,ð¥4,ð¥5â¥0.max3x1â2x2+x3+âx3âsubject toÂ 2x1+3x2+4x3+â4x3ââx4=1,3x1+4x2+x5=5,5x2âx3++x3â=â1,x1,x2,x3+,x3â,x4,x5â¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å¯è¡åä¸é®é¢çè§£

ææå¯è¡è§£çéå D âððDâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºçº¿æ§è§åé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **å¯è¡å** ï¼feasible regionï¼ï¼ä»å ä½è§åº¦çï¼æ¯ä¸ªä¸ç­å¼çº¦æ ðððð¥ â¤ððajTxâ¤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æè¿°äºä¸ä¸ªåç©ºé´ {ð¥ âðð :ðððð¥ â¤ðð}{xâRn:ajTxâ¤bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ªç­å¼çº¦æ ðððð¥ =ððajTx=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æè¿°äºä¸ä¸ªè¶ å¹³é¢ {ð¥ âðð :ðððð¥ =ðð}{xâRn:ajTx=bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å¯è¡åä¸å®æ¯æéå¤ä¸ªåç©ºé´åè¶ å¹³é¢çäº¤éï¼å¨ä¼åé¢å1ï¼è¿æ ·çå ä½ä½éå¸¸ç§°ä¸º ððRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç **å¤é¢ä½** ï¼polyhedronï¼ï¼å¤é¢ä½ä¸å®æ¯é­å¸éï¼ä½æªå¿ æ¯æççï¼æççå¤é¢ä½ä¹ç§°ä¸º **å¤èå½¢** ï¼polytopeï¼ï¼å¤èå½¢å¯ä»¥çä½æ¯å¹³é¢ä¸çå¤è¾¹å½¢å¨é«ç»´ç©ºé´çæ¨å¹¿ï¼èå¤é¢ä½å°å®è¿ä¸æ­¥æ¨å¹¿å°å¯è½æ ççæ å½¢ï¼

å¤é¢ä½çä¾å­

æ­¤å¤åä¸¾äºä¸äºå¸¸è§çå¤é¢ä½ï¼

  1. ç©ºé â â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§°ä¸º **é¶èå½¢** ï¼nullitopeï¼ï¼ç»´åº¦è§å®ä¸º â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. **ä»¿å°å­ç©ºé´** ï¼affine subspaceï¼ï¼å³è¥å¹²è¶ å¹³é¢çäº¤é {ð¥ âðð :ð´ð¥ =ð}{xâRn:Ax=b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ç¸å½äºçº¿æ§æ¹ç¨ç» ð´ð¥ =ðAx=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£éï¼å½æ¹ç¨ç»æ è§£æ¶ï¼å®å°±æ¯ç©ºéï¼å¦åï¼å®æ»æ¯å¯ä»¥åæ ð¥0 +ðx0+V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼å ¶ä¸­ï¼ð¥0 âððx0âRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âððVâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð ârankâ¡(ð´)nârankâ¡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çº¿æ§å­ç©ºé´ï¼ç¹å«å°ï¼è¶ å¹³é¢ä¹æ¯ä»¿å°å­ç©ºé´ï¼
  3. **å¤é¢ä½é¥** ï¼polyhedral coneï¼ï¼å³ç©ºé´ä¸­æéå¤ä¸ªç¹ {ð¥ð}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½éè´çº¿æ§ç»å {âðð¼ðð¥ð :ð¼ð â¥0}{âiÎ±ixi:Î±iâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®æ¯é¡¶ç¹ä½äºåç¹çå¸é¥ä½ï¼ç­ä»·å°ï¼å®å¯ä»¥çä½æ¯ç±è¥å¹²ä¸ªç»è¿åç¹çè¶ å¹³é¢å´æçå¤é¢ä½ï¼å³ {ð¥ âðð :ð´ð¥ â¤0}{xâRn:Axâ¤0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¹å«å°ï¼åç©ºé´ä¹æ¯å¤é¢ä½é¥ï¼
  4. å¤èå½¢ï¼å³æççå¤é¢ä½ï¼ç¹å«å°ï¼â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çå¤èå½¢å°±æ¯å¸¸è§çç©ºéãç¹ãçº¿æ®µãå¤è¾¹å½¢åï¼éå¸¸æä¹ä¸çï¼å¤é¢ä½ï¼ä¸ä¸ªéåæ¯å¤èå½¢ï¼å½ä¸ä» å½å®æ¯æéå¤ä¸ªç¹ {ð¥ð}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¸å {âðð¼ðð¥ð :ð¼ð â¥0,Â âðð¼ð =1}{âiÎ±ixi:Î±iâ¥0,Â âiÎ±i=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ä¸ª ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çå¤èå½¢è³å°æ¯ç± ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹çæçå¸å ï¼
  5. **åçº¯å½¢** ï¼simplexï¼ï¼å³æ°ç± ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹çæç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´å¤èå½¢ï¼å®æ¯æç®åç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´å¤èå½¢ï¼ç¹å«å°ï¼â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çå¤èå½¢åå«æ¯ç©ºéãç¹ãçº¿æ®µãä¸è§å½¢ååé¢ä½ï¼æç®åç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´åçº¯å½¢çä¾å­ï¼å°±æ¯ {ð¥ âðð :ð¥ð â¥0,Â âðð¥ð =1}{xâRk:xiâ¥0,Â âixi=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®é ä¸ï¼ä»»ä½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´åçº¯å½¢é½å¯ä»¥éè¿ä»¿å°åæ¢ï¼å³å¹³ç§»åä¼¸ç¼©ï¼åä¸ºè¿æ ·ä¸ç§ç¹æ®æ å½¢ï¼å¼å¾æ³¨æçæ¯ï¼åçº¯å½¢æ³å¹¶ä¸æ¯ççå¨åçº¯å½¢ä¸è¿è¡çï¼

ä»»ä½å¤é¢ä½ï¼é½å¯ä»¥çä½æ¯ä¸ä¸ªå¤é¢ä½é¥åä¸ä¸ªå¤èå½¢ç [Minkowski å](../../geometry/convex-hull/#éµå¯å¤«æ¯åºå)ï¼åè æè¿°äºå¤é¢ä½æ ççé¨åï¼åè æè¿°äºå¤é¢ä½æçé¨åçå½¢ç¶ï¼è¿ä¸ªå¤é¢ä½é¥æ¯å¯ä¸çï¼å¤é¢ä½ {ð¥ âðð :ð´ð¥ â¤ð}{xâRn:Axâ¤b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè§£å¾å°çå¤é¢ä½é¥ä¸å®æ¯ {ð¥ âRð :ð´ð¥ â¤0}{xâRn:Axâ¤0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

çº¿æ§è§åçè§£ä¸å¤é¢ä½çç»æç´§å¯ç¸å ³ï¼å¯¹äºå¤é¢ä½ D âððDâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååé ð âðð â{0}câRnâ{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèå¦ä¸ççº¿æ§è§åé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å¯¹æå°åçæ å½¢ä¹å¯ä»¥ç±»ä¼¼å°è®¨è®ºï¼

max{ððð¥:ð¥âD}.max{cTx:xâD}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»å ä½è§åº¦çï¼è¿ç¸å½äºå¨è¶ å¹³é¢ ð» :ððð¥ =ð§H:cTx=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡å DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å°æä¸ä¸ªäº¤ç¹çåæä¸ï¼æ²¿çåé ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹åç§»å¨è¶ å¹³é¢ ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð§z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°½å¯è½å¤§ï¼è¿å°±å­å¨ä¸ç§å¯è½æ§ï¼

  * å¯è¡å DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç©ºéï¼è¿è¯´æé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ²¡æå¯è¡è§£ï¼å®çæäºçº¦ææ¯ç¸äºçç¾çï¼æ­¤æ¶ï¼ç§°é®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ **ä¸å¯è¡ç** ï¼infeasibleï¼ï¼å®çæä¼ä»·å¼è§å®ä¸º ââââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å¯è¡å DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éç©ºï¼ä½æ¯å®å å«ä¸æ¡æ¹ååéä¸º ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå°çº¿ï¼å³å­å¨ ð¥0 âððx0âRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð¥0 +ð¡ð âDx0+tcâD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºææ ð¡ â¥0tâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å ä¸ºæ²¿çåé ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹åå¯ä»¥ä¸æ­å°ç§»å¨è¶ å¹³é¢ ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ç§»å¨è¿ç¨ä¸­ï¼éå ð» â©DHâ©D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å°å«æè¿æ¡å°çº¿ä¸­çæä¸ªç¹ï¼ä¸å®æ¯éç©ºçï¼æä»¥ï¼ç®æ å½æ° ððð¥ =ððð¥0 +ð¡ðððcTx=cTx0+tcTc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åå¾ä»»æå¤§çå¼ï¼æ­¤æ¶ï¼ç§°é®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ **æ çç** ï¼unboundedï¼ï¼å®çæä¼ä»·å¼è§å®ä¸º +â+â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å¯è¡å DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éç©ºï¼ä¸ä¸å«æä»»ä½æ¹ååéä¸º ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå°çº¿ï¼æ­¤æ¶ï¼é®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º **æçç** ï¼boundedï¼ï¼è®° ð§â âðzââR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¼ä»·å¼ï¼è¶ å¹³é¢ ð»â :ððð¥ =ð§âHâ:cTx=zâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤äºä¸ç§ä¸´çä½ç½®ï¼å®ä¸å¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸äº¤ï¼ä¸ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«äºåç©ºé´ {ð¥ :ððð¥ â¤ð§â}{x:cTxâ¤zâ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼è¿æ ·çè¶ å¹³é¢ç§°ä¸ºå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ª **æ¯æè¶ å¹³é¢** ï¼supporting hyperlaneï¼ï¼é®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¼è§£éå°±æ¯ ð»â â©DHââ©D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½ä¸ºæ¯æè¶ å¹³é¢åå¤é¢ä½çäº¤éï¼éå ð»â â©DHââ©D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æ¯å¤é¢ä½ï¼ä¸å å«å¨ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹çä¸­ï¼å®ç§°ä¸ºå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ª **é¢** ï¼faceï¼ï¼å½¢è±¡å°è¯´ï¼å¤é¢ä½å°±æ¯ç±è¿äºé¢å´æçï¼é¤äºè¿äºç±æ¯æè¶ å¹³é¢åå¤é¢ä½ç¸äº¤å½¢æçé¢ä¹å¤ï¼ä¸è¬æ¥è¯´ï¼å¤é¢ä½è¿æä¸¤ä¸ªé¢ï¼ç©ºéåå¤é¢ä½æ¬èº«ï¼å¤é¢ä½çææé¢å¨éåçå å«å ³ç³»ä¸ï¼å½¢æäº [æ ¼](../order-theory/#æåéä¸æ) çç»æï¼

ä¸ä¸ª ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´çå¤é¢ä½çé¢çç»´åº¦ä¸å®æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çæ´æ°ï¼ç»´åº¦ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¢ï¼å³ä¸ä¸ªç¹ï¼ç§°ä¸ºå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **é¡¶ç¹** ï¼vertexï¼æ **è§ç¹** ï¼corner pointï¼ï¼ç»´åº¦ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¢ç§°ä¸ºå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **è¾¹** ï¼edgeï¼ï¼ç»´åº¦ä¸º ð â1dâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¢åç§°ä¸ºå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ç»´é¢** ï¼facetï¼ï¼ä½æ¯ï¼å¹¶éææå¤é¢ä½é½æé¡¶ç¹ï¼å ä¸ºå¤é¢ä½çé¢çé¢ä»ç¶æ¯å¤é¢ä½çé¢ï¼èåªæä»¿å°å­ç©ºé´ææ²¡æä¸¥æ ¼æ´å°çéç©ºé¢ï¼æä»¥ï¼å¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæææå°é¢é½æ¯ä»¿å°å­ç©ºé´ï¼èä¸ï¼åä¸ä¸ªå¤é¢ä½çæå°é¢çç»´åº¦æ¯ç¸åçï¼ç¹å«å°ï¼å¤é¢ä½ D ={ð¥ âðð :ð´ð¥ â¤ð}D={xâRn:Axâ¤b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°é¢çç»´åº¦æ¯ ð ârankâ¡ð´nârankâ¡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å ä¸ºå¤é¢ä½çé¢å°±æ¯æççº¿æ§è§åé®é¢çè§£éï¼æä»¥ï¼éè¦ææ¸ æ¥å¦ä½ç¡®å®å¤é¢ä½çé¢çæ¹ç¨ï¼è®¾å¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç±è¥å¹²ä¸ªçº¦æ ðððð¥ âªððajTxâªbj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè¿°ï¼ä¸ ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªé¢ï¼å¦ææä¸ªçº¦æå¨ææ ð¥ âð¹xâF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤é½åå¾ç­å·ï¼å°±ç§°è¯¥çº¦æå¨é¢ ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ **ç´§ç** ï¼tightï¼ï¼é¢ ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çç¹æ¾ç¶æ»¡è¶³è¿äºç´§çº¦æåç­å·å¾å°çæ¹ç¨ç»ï¼èè¿ä¸ªæ¹ç¨ç»ç¡®å®çä»¿å°å­ç©ºé´åå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäº¤éï¼å°±æ¯é¢ ð¹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè¿æ¥ï¼ä»»æéåå¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æçä¸ä¸ªå­éï¼å°è¿äºçº¦æåç­ãèç«ãæ±è§£å¾å°çä»¿å°å­ç©ºé´åå¤é¢ä½çäº¤éï¼å°±æ¯ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªé¢ï¼èä¸ï¼éåçç´§çº¦æè¶å¤ï¼å¾å°çé¢ï¼å¨å å«æä¹ä¸ï¼å°±è¶å°ï¼

ç¹å«å°ï¼æ åå½¢å¼ççº¿æ§è§åçå¯è¡å D ={ð¥ âðð :ð´ð¥ =ð,Â ð¥ â¥0}D={xâRn:Ax=b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°ç©éµ (ð´ð¼)(AI)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç§©æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å®çæå°é¢å°±æ¯å®çé¡¶ç¹ï¼ä¹å°±æ¯è¯´ï¼å¦æé®é¢æçï¼é£ä¹å®çæä¼è§£ä¸å®å¯ä»¥éåä¸ºæä¸ªé¡¶ç¹ï¼èä¸ï¼è¿ä¸ªé¡¶ç¹å¯ä»¥éè¿éå ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªçº¿æ§ç¬ç«çç´§çº¦æèç«å¾å°ï¼è¿æ­£æ¯çº¿æ§è§åçæ åå½¢å¼çæ¹ä¾¿ä¹å¤ï¼

ä¾å­

ä¸å¾ä¸­ï¼DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¯è¡åï¼ç®æ å½æ°ä¸­çç³»æ°æ¯ ð1,ð2,ð3c1,c2,c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åå«å¯¹åºçå¯ä¸æä¼è§£ãå¤ç»æä¼è§£åæ çä¸ç§æ å½¢ï¼å¯¹äºåä¸¤ç§æ å½¢ï¼ç¸åºççº¢è²ç²å®çº¿å°±æ¯è§£éå¯¹åºçæ¯æè¶ å¹³é¢ï¼ä¹ä¸ï¼ï¼æä¼è§£éåå«æ¯å¤é¢ä½ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¡¶ç¹ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè¾¹ âââð¶ð·CDâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºç¬¬ä¸ç§æ å½¢ï¼å ä¸ºå¯è¡å DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å å«æ¹åä¸º ð3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå°çº¿ï¼æä»¥ï¼ä»¥ ð3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ³åéçè¶ å¹³é¢å¯ä»¥ä¸æ­æ²¿ç ð3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¹åç§»å¨ï¼è¿èé®é¢æ¯æ ççï¼

![](./images/lp-feasible.svg)

è¿äºè®¨è®ºå¿½ç¥äº ð =0c=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼çº¿æ§è§åé®é¢æ¾ç¶ä¸è½æ¯æ ççï¼æä»¥è¦ä¹é®é¢æ¬èº«æ¯ä¸å¯è¡çï¼è¦ä¹æä¼ä»·å¼ç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æä¼è§£éå°±æ¯ DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬èº«ï¼è¿ç±»ç¹æ®ççº¿æ§è§åä¹ç§°ä¸º **å¯è¡æ§çº¿æ§è§å** ï¼feasibility linear programmingï¼ï¼

å¼å¾æåºçæ¯ï¼å¤å®çº¿æ§è§åé®é¢æ¯å¦å¯è¡ãæ¯å¦æçï¼ä»¥åæ±åºä¸ç­å¼ç»çå¯è¡è§£ç­é®é¢ï¼é½åè§£çº¿æ§è§åé®é¢æ¬èº«åæ ·å°é¾2ï¼æ¯å¦è¯´ï¼ä¸æä¸­å¼ºå¯¹å¶å®ççè¯æå°±è¯´æï¼è§£ä¸ä¸ªæçççº¿æ§è§åé®é¢ï¼å°±ç¸å½äºå¯»æ¾ä¸ç»ä¸ç­å¼çå¯è¡è§£ï¼å æ­¤ï¼å¯¹äºå¤æ­ä¸ç­å¼ç»æ¯å¦æè§£åå¤æ­æ¹ç¨ç»æ¯å¦æéè´è§£ç­ä»»å¡ï¼æææçæ¹å¼å°±æ¯æ±è§£ç¸åºçå¯è¡æ§çº¿æ§è§å3ï¼

å¦å¤ï¼å¦æçº¿æ§è§åé®é¢çä¸ä¸ªçº¦æï¼å¨å¯è¡åçææé¢ä¸é½ä¸æ¯ç´§çï¼é£ä¹è¿ä¸ªçº¦æå°±æ¯ **åä½ç** ï¼redundantï¼ï¼æ¬æå¼å¤´æ©ç¹å¸å çä¾å­ä¸­ï¼å·¥ä½æ¶é´ççº¦æå°±æ¯ä¸ä¸ªåä½çº¦æï¼å¨ç»å®çä¸ç­å¼ç»ä¸­å¤å®æä¸ªä¸ç­å¼ ðððð¥ â¤ððajTxâ¤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦åä½è¿ä¸é®é¢ï¼å¯ä»¥éè¿æ±è§£çº¿æ§è§åé®é¢ max{ðððð¥ :ð¥ âD}max{ajTx:xâD}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶å°å®ä¸ ððbj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸æ¯è¾æ¥è§£å³ï¼

## å¸¸è§ç®æ³

ç®æ³ç«èµä¸­ï¼å¾å°æé®é¢åªè½éè¿çº¿æ§è§åçç®æ³è§£å³ï¼å¤§å¤æ°å¯ä»¥ç¨çº¿æ§è§åæ¹æ³æ±è§£çé¢ç®ï¼éå¸¸ä¹å¯ä»¥éè¿ç½ç»æµç­æ´ä¸ºä¸é¨ä¹æ´ä¸ºé«æçç®æ³æ¥è§£å³ï¼

è§£å³çº¿æ§è§åé®é¢çå¸¸è§ç®æ³å¦ä¸ï¼

  * [åçº¯å½¢æ³](../simplex/)
  * æ¤­çæ³
  * å ç¹æ³

å°½ç®¡åçº¯å½¢æ³çæå·®æ å½¢å¤æåº¦æ¯ææ°çº§çï¼èå ç¹æ³çå¤æåº¦æ¯å¤é¡¹å¼çï¼ä½è¿ä¸¤ç±»ç®æ³å¨å¤§å¤æ°å®é é®é¢ä¸­çè¡¨ç°é½éå¸¸åºè²ï¼ç¸æ¯ä¹ä¸ï¼è½ç¶æ¤­çæ³ççè®ºå¤æåº¦æ¯å¤é¡¹å¼çº§å«çï¼ä½æ¯éå¸¸è¿è¡ç¼æ ¢ï¼å¹¶ä¸å®ç¨ï¼

ç®åå°ä¸æ¸ æ¥çº¿æ§è§åé®é¢æ¯å¦å­å¨å¼ºå¤é¡¹å¼å¤æåº¦çç®æ³ï¼

## å¯¹å¶é®é¢

æ¯ä¸ªçº¿æ§è§åé®é¢é½å¯¹åºçä¸ä¸ªå¯¹å¶é®é¢ï¼åé®é¢åå¯¹å¶é®é¢çè§£æçç´§å¯çèç³»ï¼éè¿å¯¹å¶é®é¢ï¼ä¸ä» æå©äºæ´æ·±å ¥å°çè§£é®é¢çç»æï¼è¿å¸¸å¸¸å¯ä»¥æååé®é¢çæ±è§£æçï¼

å¯¹äºçº¿æ§è§åé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ææ¶å°åå­æ¯åéåä¸ºåéï¼

minð¥1,ð¥2,ð¥3ðð1ð¥1+ðð2ð¥2+ðð3ð¥3subject toÂ ð´11ð¥1+ð´12ð¥2+ð´13ð¥3â¥ð1,ð´21ð¥1+ð´22ð¥2+ð´23ð¥3=ð2,ð´31ð¥1+ð´32ð¥2+ð´33ð¥3â¤ð3,ð¥1â¥0,Â ð¥3â¤0,minx1,x2,x3c1Tx1+c2Tx2+c3Tx3subject toÂ A11x1+A12x2+A13x3â¥b1,A21x1+A22x2+A23x3=b2,A31x1+A32x2+A33x3â¤b3,x1â¥0,Â x3â¤0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®çå¯¹å¶é®é¢ ð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æçº¿æ§è§åé®é¢

maxð¦1,ð¦2,ð¦3ðð1ð¦1+ðð2ð¦2+ðð3ð¦3subject toÂ ð´ð11ð¦1+ð´ð21ð¦2+ð´ð31ð¦3â¤ð1,ð´ð12ð¦1+ð´ð22ð¦2+ð´ð32ð¦3=ð2,ð´ð13ð¦1+ð´ð23ð¦2+ð´ð33ð¦3â¥ð3,ð¦1â¥0,Â ð¦3â¤0.maxy1,y2,y3b1Ty1+b2Ty2+b3Ty3subject toÂ A11Ty1+A21Ty2+A31Ty3â¤c1,A12Ty1+A22Ty2+A32Ty3=c2,A13Ty1+A23Ty2+A33Ty3â¥c3,y1â¥0,Â y3â¤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼å¯¹å¶é®é¢çå³ç­åé ð¦1,ð¦2,ð¦3y1,y2,y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯åé®é¢çä¸ç±»çº¦æç Lagrange ä¹å­ï¼åè¿æ¥ï¼åé®é¢çå³ç­åé ð¥1,ð¥2,ð¥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åå«æ¯å¯¹å¶é®é¢çä¸ç±»çº¦æç Lagrange ä¹å­ï¼å®¹æéªè¯ï¼å¯¹å¶é®é¢çå¯¹å¶é®é¢å°±æ¯åé®é¢ï¼

åé®é¢ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¯¹å¶é®é¢ ð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹åºå ³ç³»å¦ä¸ï¼

æå°åé®é¢| æå¤§åé®é¢  
---|---  
å¤§äºç­äºçº¦æ| éè´åé  
å°äºç­äºçº¦æ| éæ­£åé  
ç­å¼çº¦æ| æ çº¦æåé  
éè´åé| å°äºç­äºçº¦æ  
éæ­£åé| å¤§äºç­äºçº¦æ  
æ çº¦æåé| ç­å¼çº¦æ  
ç®æ å½æ°ç³»æ°| çº¦æå³ä¾§å¸¸é  
çº¦æå³ä¾§å¸¸é| ç®æ å½æ°ç³»æ°  
  
ç¹å«å°ï¼æ åå½¢å¼ççº¿æ§è§åé®é¢

min{ððð¥:ð´ð¥=ð,Â ð¥â¥0}min{cTx:Ax=b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå¯¹å¶é®é¢æ¯

max{ððð¦:ð´ðð¦â¤ð}.max{bTy:ATyâ¤c}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å¯¹å¶åç

åé®é¢åå¯¹å¶é®é¢ä¸ä» å¨å½¢å¼ä¸äºä¸ºéåï¼èä¸ä¸¤è çè§£ä¹ç´§å¯ç¸å ³ï¼è¿ç§°ä¸º **å¯¹å¶åç** ï¼duality principalï¼ï¼ä¸ºè¡¨è¿°æ¹ä¾¿ï¼æ¬èå¨åè¿°åè¯æå®çæ¶ï¼å°éç¨æ åå½¢å¼çåé®é¢ï¼

é¦å ï¼**å¼±å¯¹å¶å®ç** ï¼weak duality theoremï¼è¯´æï¼å¯¹å¶é®é¢çæå¤§å¼ä¸è¶ è¿åé®é¢çæå°å¼ï¼

å¼±å¯¹å¶å®ç

å¯¹äºææ ð´ âððÃðAâRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð âððbâRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âððcâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»æ

max{ððð¦:ð´ðð¦â¤ð}â¤min{ððð¥:ð´ð¥=ð,Â ð¥â¥0}.max{bTy:ATyâ¤c}â¤min{cTx:Ax=b,Â xâ¥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å¦æåé®é¢åå¯¹å¶é®é¢ä¸­çä»»ä½ä¸ä¸ªä¸å¯è¡ï¼é£ä¹è¯¥ä¸ç­å¼å°±æ¯å¹³å¡çï¼åè®¾ä¸¤ä¸ªé®é¢é½æ¯å¯è¡çï¼é£ä¹ï¼å¯¹äºææå¯è¡ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

ððð¦=ð¥ðð´ðð¦â¤ð¥ðð.bTy=xTATyâ¤xTc.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼å°ä¸¤ä¾§åæå¼ï¼å°±å¾å°å¼±å¯¹å¶å®çæç«ï¼

åºäºå¼±å¯¹å¶å®çï¼åé®é¢åå¯¹å¶é®é¢çè§£çæ åµåªè½æä¸é¢åç§æ å½¢ï¼

  1. åé®é¢åå¯¹å¶é®é¢åä¸å¯è¡ï¼å³ ââ â¤ +ââââ¤+â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. åé®é¢ä¸å¯è¡ï¼å¯¹å¶é®é¢æ çï¼å³ +â â¤ +â+ââ¤+â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. åé®é¢æ çï¼å¯¹å¶é®é¢ä¸å¯è¡ï¼å³ ââ â¤ âââââ¤ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. åé®é¢åå¯¹å¶é®é¢åæçï¼

å¼±å¯¹å¶å®çæå¾å¤æ¨è®ºï¼ä¾å¦ï¼å®å®é ä¸ç»åºäºå©ç¨åé®é¢åå¯¹å¶é®é¢çå¯è¡æ§å¤å®åé®é¢æ ççæ¹æ³ï¼

æ¨è®º

çº¿æ§è§åé®é¢æ çï¼å½ä¸ä» å½å®å¯è¡ï¼ä¸å®çå¯¹å¶é®é¢ä¸å¯è¡ï¼

å°å¼±å¯¹å¶å®çåºç¨äºå¯è¡æ§çº¿æ§è§åé®é¢ï¼å°±å¾å° Farkas å¼çï¼åå®çåç§åä½ï¼ï¼

Farkas å¼ç

å¯¹äº ð´ âððÃðAâRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âððbâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸åæ å½¢ä¸­æ°æä¸ç§æç«ï¼

  1. å­å¨ ð¥ âððxâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð´ð¥ =ðAx=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¥ â¥0xâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å­å¨ ð¦ âððyâRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð´ðð¦ â¥0ATyâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ððð¦ <0bTy<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

èèçº¿æ§è§åé®é¢ max{0 :ð´ð¥ =ð,Â ð¥ â¥0}max{0:Ax=b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çå¯¹å¶é®é¢æ¯ min{ððð¦ :ð´ðð¦ â¥0}min{bTy:ATyâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹å¶é®é¢æ¾ç¶æ¯å¯è¡çï¼å ä¸ºè³å° 0 âðð0âRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ç»å¯è¡è§£ï¼å æ­¤ï¼æ ¹æ®å¼±å¯¹å¶å®çï¼è¦ä¹åé®é¢å¯è¡ï¼è¦ä¹å¯¹å¶é®é¢æ çï¼äºè å¿ æ©å ¶ä¸ï¼åé®é¢å¯è¡å°±æ¯ Farkas å¼çä¸­çæ å½¢ 1ï¼èå¯¹å¶é®é¢æ çå°±ç­ä»·äº Farkas å¼çä¸­çæ å½¢ 2ï¼è¿å°±è¯æäº Farkas å¼çï¼

Farkas å®é ä¸æ¯ä¸ç§ [è¶ å¹³é¢åç¦»å®ç](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)ï¼æ å½¢ 1 æ¯å¨è¯´ï¼ç¹ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½äº ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååéçæçå¤é¢ä½é¥ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éï¼å æ­¤ï¼Farkas å¼çè¯´æï¼å½ä¸ä» å½ç¹ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¨è¿ä¸å¸é¥ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ¶ï¼å­å¨ç»è¿åç¹ä¸æ³åéä¸º ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¶ å¹³é¢ ð» :ð¦ðð¥ =0H:yTx=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼ºåç¦»äºç¹ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¤é¢ä½é¥ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

äºå®ä¸ï¼å¯¹äºå¼±å¯¹å¶å®çå è®¸çç¬¬åç§æ å½¢ï¼ææ´å¼ºçç»è®ºæç«ï¼åé®é¢åå¯¹å¶é®é¢çæä¼å¼æ¯ç¸ç­çï¼å°åä¸ç§æ å½¢åå¨ä¸èµ·ï¼å°±å¾å° **å¼ºå¯¹å¶å®ç** ï¼strong duality theoremï¼ï¼åªè¦åé®é¢æå¯¹å¶é®é¢ä¹ä¸æ¯å¯è¡çï¼å®ä»¬çæä¼å¼å°±å¿ ç¶ç¸ç­ï¼

å¼ºå¯¹å¶å®ç

å¯¹äºææ ð´ âððÃðAâRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð âððbâRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âððcâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

max{ððð¦:ð´ðð¦â¤ð}=min{ððð¥:ð´ð¥=ð,Â ð¥â¥0}.max{bTy:ATyâ¤c}=min{cTx:Ax=b,Â xâ¥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åªè¦ä¸¤ä¸ªéåä¹ä¸éç©ºï¼

è¯æ

å¼±å¯¹å¶å®çå¯ä¸æ²¡æå å«çæ å½¢ï¼å°±æ¯åé®é¢åå¯¹å¶é®é¢é½å¯è¡çæ å½¢ï¼æ­¤æ¶ï¼èèå¦ä¸å¯è¡æ§çº¿æ§è§åé®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

max{0:ððð¥â¤ððð¦,Â ð´ð¥=ð,Â ð¥â¥0,Â ð´ðð¦â¤ð}.max{0:cTxâ¤bTy,Â Ax=b,Â xâ¥0,Â ATyâ¤c}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æé®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¯è¡è§£ (ð¥â,ð¦â) âðð Ãðð(xâ,yâ)âRnÃRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ç±å¼±å¯¹å¶å®çåæä¼æ§å¯ç¥

ððð¦ââ¤max{ððð¦:ð´ðð¦â¤ð}â¤min{ððð¥:ð´ð¥=ð,Â ð¥â¥0}â¤ððð¥â,bTyââ¤max{bTy:ATyâ¤c}â¤min{cTx:Ax=b,Â xâ¥0}â¤cTxâ,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯ ððð¥â â¤ððð¦âcTxââ¤bTyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èææè¿äºä¸ç­å¼é½å¯ä»¥åå¾ç­å·ï¼ä¹å°±æ¯è¯´ï¼ä¸ä» å¼ºå¯¹å¶æç«ï¼èä¸ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯åé®é¢åå¯¹å¶é®é¢çæä¼è§£ï¼

å æ­¤ï¼åªéè¦è¯æé®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯è¡çï¼åè®¾ä¸ç¶ï¼ä»¿ç § Farkas å¼ççè¯æï¼å¯ä»¥èèé®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹å¶é®é¢ ð·ðDQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

min{ðððâððð:ðð¡âð´ððâ¥0,Â âðð¡+ð´ð=0,Â ð¡â¥0,Â ðâ¥0}.min{cTÎ¼âbTÎ»:ctâATÎ»â¥0,Â âbt+AÎ¼=0,Â tâ¥0,Â Î¼â¥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º (ð¡,ð,ð) =(0,0,0)(t,Î»,Î¼)=(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯¹å¶é®é¢ ð·ðDQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç»å¯è¡è§£ï¼æä»¥ç±å¼±å¯¹å¶å®çå¯ç¥ï¼é®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡ï¼å°±æå³çå¯¹å¶é®é¢ ð·ðDQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ çï¼å³å­å¨ä¸ç» (ð¡â,ðâ,ðâ)(tâ,Î»â,Î¼â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ðððââðððâ<0,Â ðð¡ââð´ððââ¥0,Â âðð¡â+ð´ðâ=0,Â ð¡ââ¥0,Â ðââ¥0.cTÎ¼ââbTÎ»â<0,Â ctââATÎ»ââ¥0,Â âbtâ+AÎ¼â=0,Â tââ¥0,Â Î¼ââ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼å¦æ ð¡â >0tâ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹è¿äºä¸ç­å¼å®é è¯´æ (ð¥,ð¦) =(ðâ/ð¡â,ðâ/ð¡â)(x,y)=(Î¼â/tâ,Î»â/tâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åè¿°é®é¢çä¸ç»å¯è¡è§£ï¼ä¸åè®¾çç¾ï¼æä»¥ï¼åªè½æ ð¡â =0tâ=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æ

ðððâ<ðððâ,Â ð´ððââ¤0,Â ð´ðâ=0,Â ðââ¥0.cTÎ¼â<bTÎ»â,Â ATÎ»ââ¤0,Â AÎ¼â=0,Â Î¼ââ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯ï¼å ä¸ºå·²ç»åè®¾å®çä¸­çåé®é¢åå¯¹å¶é®é¢é½å¯è¡ï¼ä¹å°±æ¯è¯´ï¼å­å¨ (ð¥0,ð¦0)(x0,y0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

ð´ð¥0=ð,Â ð¥0â¥0,Â ð´ðð¦0â¤ðAx0=b,Â x0â¥0,Â ATy0â¤c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼æä»¥ï¼æ

0=(ð´ðâ)ðð¦0=(ð´ðð¦0)ððââ¤ðððâ<ðððâ=ð¥ð0ð´ððââ¤0.0=(AÎ¼â)Ty0=(ATy0)TÎ¼ââ¤cTÎ¼â<bTÎ»â=x0TATÎ»ââ¤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¾ç¶çç¾ï¼è¿ä¸çç¾è¯´æé®é¢ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯è¡çï¼è¿èè¯´æå¼ºå¯¹å¶æç«ï¼

ä»å¼ºå¯¹å¶å®ççè¯æè¿ç¨è¿è½å¾å°å¦ä¸æ¨è®ºï¼

æ¨è®º

è®¾åé®é¢åå¯¹å¶é®é¢çä¸ç»å¯è¡è§£ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å¼ºå¯¹å¶æ§ï¼å³ ððð¥â =ððð¦âcTxâ=bTyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å®ä»¬åæ ·åå«æ¯åé®é¢åå¯¹å¶é®é¢çæä¼è§£ï¼

å¼ºå¯¹å¶å®çè¯´æï¼å¯¹äºå¯è¡ççº¿æ§è§åé®é¢ï¼åªéè¦æ±è§£å®çå¯¹å¶é®é¢ï¼å°±è½å¤å¾å°åé®é¢çæä¼ä»·å¼ï¼

### äºè¡¥æ¾å¼æ¡ä»¶

åå ¶å®çä¼åé®é¢ä¸æ ·ï¼äºè¡¥æ¾å¼æ¡ä»¶æ¯çº¿æ§è§åé®é¢çæä¼æ§æ¡ä»¶çä¸é¨åï¼èä¸ï¼å ä¸ºç®æ å½æ°æ¯çº¿æ§çï¼æä»¥å¯¹äºçº¿æ§è§åé®é¢æ¥è¯´ï¼äºè¡¥æ¾å¼æ¡ä»¶æ¯å¯è¡è§£æä¸ºæä¼è§£çå åå¿ è¦æ¡ä»¶ï¼

æè° **äºè¡¥æ¾å¼** ï¼complementary slacknessï¼æ¡ä»¶ï¼å°±æ¯æåªæå¨åé®é¢ï¼å¯¹å¶é®é¢ï¼ä¸­ççº¦æåå¾ç­å·ï¼å³çº¦ææ¯ç´§çï¼çæ¶åï¼å¯¹å¶é®é¢ï¼åé®é¢ï¼ä¸­ä¸ä¹å¯¹åºçåéæè½åéé¶å¼ï¼å¦æå°åéåéé¶å¼ä¹å½æä¸æ¡æ¾å¼ççº¦æï¼é£ä¹è¿å°±ç¸å½äºè¯´ï¼åé®é¢åå¯¹å¶é®é¢ä¸­ç¸å¯¹åºçåéåçº¦æä¸è½åæ¶æ¯æ¾å¼çï¼å æ­¤ï¼è¿ä¸æ¡ä»¶ç§°ä¸ºäºè¡¥æ¾å¼æ¡ä»¶ï¼

ä»¥æ åå½¢å¼ççº¿æ§è§åé®é¢ä¸ºä¾ï¼å¦ä¸ç»è®ºæç«ï¼

å®ç

åè®¾ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯åé®é¢ min{ððð¥ :ð´ð¥ =ð,Â ð¥ â¥0}min{cTx:Ax=b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¯¹å¶é®é¢ max{ððð¦ :ð´ðð¦ â¤ð}max{bTy:ATyâ¤c}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è¡è§£ï¼é£ä¹ï¼å½ä¸ä» å½äºè¡¥æ¾å¼æ¡ä»¶æç«ï¼å³

ð¥ð(ð´ðð¦âð)=0xT(ATyâc)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¶ï¼ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åå«æ¯åé®é¢åå¯¹å¶é®é¢çæä¼è§£ï¼

è¯æ

å ä¸º ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯å¯è¡è§£ï¼æä»¥ï¼æ

ððð¦ââððð¥â=(ð¥â)ð(ð´ðð¦ââð).bTyââcTxâ=(xâ)T(ATyââc).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼äºè¡¥æ¾å¼æ¡ä»¶æç«ï¼å½ä¸ä» å½ ððð¦â =ððð¥âbTyâ=cTxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å¼ºå¯¹å¶å®ççæ¨è®ºï¼è¿ä¸æ¡ä»¶æç«ï¼å½ä¸ä» å½ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯åé®é¢çæä¼è§£ï¼

æ åå½¢å¼å¯è½å¤ªè¿ç¹æ®ï¼è¯¥å®ççç¨å¾®ä¸è¬çå½¢å¼å¦ä¸ï¼

å®ç

åè®¾ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«æ¯åé®é¢ min{ððð¥ :ð´ð¥ â¥ð,Â ð¥ â¥0}min{cTx:Axâ¥b,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¯¹å¶é®é¢ max{ððð¦ :ð´ðð¦ â¤ð,Â ð¦ â¥0}max{bTy:ATyâ¤c,Â yâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è¡è§£ï¼é£ä¹ï¼å½ä¸ä» å½äºè¡¥æ¾å¼æ¡ä»¶æç«ï¼å³

ð¥ð(ð´ðð¦âð)=ð¦ð(ð´ð¥âð)=0xT(ATyâc)=yT(Axâb)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¶ï¼ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦âyâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åå«æ¯åé®é¢åå¯¹å¶é®é¢çæä¼è§£ï¼

è¯æ

è¯æåºæ¬åä¸ï¼åªæ¯è¿æ¬¡è¦å°å·®å¼åæ

ððð¦ââððð¥â=(ð¥â)ð(ð´ðð¦ââð)â(ð¦â)ð(ð´ð¥ââð).bTyââcTxâ=(xâ)T(ATyââc)â(yâ)T(Axââb).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºè¡¥æ¾å¼æ¡ä»¶æä¾äºå¤æ­çº¿æ§è§åé®é¢çå¯è¡è§£çæä¼æ§çç®åæ¡ä»¶ï¼

### åå§âå¯¹å¶æ¹æ³

å¯¹å¶é®é¢å¯ä»¥è¾ å©åé®é¢çæ±è§£ï¼å¨è§£å³çº¿æ§è§åé®é¢æ¶ï¼å¸¸å¸¸ä¼ç¨å°çä¸ç§æ¹æ³æ¯ **åå§âå¯¹å¶æ¹æ³** ï¼primal-dual methodï¼ï¼å®éè¿æ±è§£ä¸ç³»åç¸å¯¹ç®åçè¾ å©é®é¢ï¼éæ­¥æ¹è¿å¯¹å¶é®é¢çè§£ï¼è¿èè·å¾åå§é®é¢çæä¼è§£ï¼

å¯¹äºæ åå½¢å¼çåé®é¢

(ð)min{ððð¥:ð´ð¥=ðâ¥0,Â ð¥â¥0}(P)min{cTx:Ax=bâ¥0,Â xâ¥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå®çå¯¹å¶é®é¢

(ð·)max{ððð¦:ð´ðð¦â¤ð},(D)max{bTy:ATyâ¤c},![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ä¸èå·²ç»è¯´æï¼è¦æ¾å°å®ä»¬çæä¼è§£ï¼åªéè¦æ¾å°é®é¢ (ð)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç»å¯è¡è§£ï¼ä½¿å¾å®ä»¬æ»¡è¶³äºè¡¥æ¾å¼æ¡ä»¶ ð¥ð(ð´ðð¦ âð) =0xT(ATyâc)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¸å¦¨èèå¦ä¸æµç¨ï¼

  1. ä»å¯¹å¶é®é¢ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå¯è¡è§£ ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼è®¡ç®å¯¹å¶é®é¢çç´§çº¦æçéå

ð¼={ð:(ð´ðð¦âð)ð=0}.I={i:(ATyâc)i=0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. æ ¹æ®äºè¡¥æ¾å¼æ¡ä»¶ï¼å¦æå­å¨é®é¢ (ð)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è¡è§£ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð¥ð >0xi>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä» å¨ ð âð¼iâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æç«ï¼å°±æå³çå·²ç»æ¾å°ä¸ç»æä¼è§£ï¼å æ­¤ï¼èèçº¿æ§è§åé®é¢

(ð ð)minð¥,ð ððð subject toÂ ð´ð¥+ð =ð,ð¥ðâ¥0,Â âðâð¼,ð¥ð=0,Â âðâð¼,ð â¥0.(RP)minx,s1Tssubject toÂ Ax+s=b,xiâ¥0,Â âiâI,xi=0,Â âiâI,sâ¥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. å¦æé®é¢ (ð ð)(RP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å¼æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æä¼è§£ (ð¥â,0)(xâ,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯åé®é¢ (ð)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¼è§£ï¼å¦åï¼å¯ä»¥æ±åºå®çå¯¹å¶é®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ Â¯ð¦yÂ¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

(ð·ð ð)maxð¦ððð¦subject toÂ âððððð¦ðâ¤0,Â âðâð¼,ð¦â¤1.(DRP)maxybTysubject toÂ âjajiyjâ¤0,Â âiâI,yâ¤1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®å¼ºå¯¹å¶å®çå¯ç¥ï¼ððÂ¯ð¦ =1ðð â >0bTyÂ¯=1Tsâ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  4. æ ¹æ®é®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£æ¹è¿å¯¹å¶é®é¢ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è¡è§£ï¼è®¾ ð¦â² =ð¦ +ðÂ¯ð¦yâ²=y+ÎµyÂ¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð >0Îµ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸å®æ ððð¦â² =ððð¦ +ðððÂ¯ð¦ >ððð¦bTyâ²=bTy+ÎµbTyÂ¯>bTy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼åªè¦ä¿è¯ ð¦â²yâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»ç¶æ¯å¯¹å¶é®é¢çå¯è¡è§£ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±è¦å°½å¯è½å¤§å°éå ðÎµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

å¯¹äº ð âð¼iâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

âððððð¦â²ð=âððððð¦ð+ðâððððÂ¯ð¦ðâ¤ðð,âjajiyjâ²=âjajiyj+ÎµâjajiyÂ¯jâ¤ci,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼é®é¢ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿äºçº¦ææ»æ¯å¯ä»¥æ»¡è¶³çï¼

å¯¹äºå©ä¸ççº¦æï¼å³ ð âð¼iâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åªéè¦å

ð=min{ððââððððð¦ðâððððÂ¯ð¦ð:ðâð¼,Â âððððÂ¯ð¦ð>0}Îµ=min{ciââjajiyjâjajiyÂ¯j:iâI,Â âjajiyÂ¯j>0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±å¯ä»¥å¨ä¿è¯å¯è¡æ§çåæä¸ï¼å°½å¯è½å¤§å°æ¹è¿å¯¹å¶é®é¢çè§£ï¼ç¶ååå°æ­¥éª¤ 1 ç»§ç»­è¿­ä»£ï¼ç¹å«å°ï¼å¦æä¸å¼ä¸­çéåä¸ºç©ºéï¼å³ ð = +âÎµ=+â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼å¯¹å¶é®é¢ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ çï¼åé®é¢ (ð)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡ï¼

è¿ä¸ªè¿ç¨ä¸­å ¶å®åªæé®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¡®å®éè¦æ±è§£çï¼å®ä¸é®é¢ (ð ð)(RP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿å¼ºå¯¹å¶å®çç¸äºèç³»ï¼é®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¾äºä¸ä¸ªæ¹è¿å¯¹å¶é®é¢è§£çæ¹åï¼èä¸ç¸å¯¹äºå¯¹å¶é®é¢ (ð·)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬èº«ï¼é®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼æ´å ç®åï¼é®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è¡æ§ç± Farkas å¼çä¿è¯ï¼èçº¦æ ð¦ â¤1yâ¤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªæ¯ä¸ç»è§èåæ¡ä»¶ï¼ä¿è¯äºé®é¢ (ð·ð ð)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æçï¼

ç®æ³ç«èµä¸­ï¼åå§âå¯¹å¶æ¹æ³å¹¿æ³å°åºç¨äºåç±»ç»åä¼åé®é¢ï¼ä¾å¦äºåå¾æå¤§æå¹é ç [åçå©ç®æ³](../../graph/graph-matching/bigraph-weight-match/#hungarian-algorithmkuhnmunkres-algorithm)ãæå°è´¹ç¨æµç [æ¶åç®æ³](../../graph/flow/min-cost/) å [SSP ç®æ³ï¼åå§âå¯¹å¶ç®æ³ï¼](../../graph/flow/min-cost/#ssp-ç®æ³)ãæç­è·¯ç [Dijkstra ç®æ³](../../graph/shortest-path/#dijkstra-ç®æ³)ãæå¤§æµç [FordâFulkerson å¢å¹¿ç®æ³](../../graph/flow/max-flow/#fordfulkerson-å¢å¹¿) ç­ï¼é½å¯ä»¥çä½æ¯åå§âå¯¹å¶æ¹æ³çç´æ¥åºç¨ï¼

## æ´æ°è§å

**æ´æ°è§å** ï¼integer programmingï¼éå¸¸æ **æ´æ°çº¿æ§è§å** ï¼integer linear programming, ILPï¼ï¼æ åå½¢å¼çæ´æ°çº¿æ§è§åå¦ä¸ï¼

minð¥ððð¥subject toÂ ð´ð¥=ðâ¥0,ð¥â¥0,ð¥âðð,minxcTxsubject toÂ Ax=bâ¥0,xâ¥0,xâZn,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð´ âððÃðAâRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð âððbâRm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð âððcâRn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼æ´æ°çº¿æ§è§åæ¯å¨çº¿æ§è§åé®é¢ä¸æ·»å å³ç­åéå¿ é¡»ä¸ºæ´æ°è¿ä¸çº¦ææ¡ä»¶æå¾å°çé®é¢ï¼

æ´æ°çº¦ææ¾èå¢å äºæ´æ°è§åé®é¢çå¤ææ§ï¼è®¸å¤ç»åä¼åé®é¢ï¼ä¾å¦èå é®é¢ãéå®æ§é®é¢ä»¥åä¼å¤å¾è®ºä¸­çä¼åé®é¢ï¼é½å¯ä»¥è¡¨ç¤ºä¸ºæ´æ°è§åæ¨¡åï¼èè¿äºé®é¢ä¸­çå¤æ°è¢«è¯ææ¯ NP å°é¾çï¼

### å ¨å¹ºæ¨¡ç©éµ

æ­£å å¦æ­¤ï¼å¯¹äºå¾å¤å¤§è§æ¨¡çæ´æ°ä¼åé®é¢ï¼ææ¶åä¼èèå°å®çæ´æ°çº¦ææ¾å¼æï¼è½¬èæ±è§£ä¸ä¸ªçº¿æ§è§åé®é¢ï¼éå¸¸æ¥è¯´ï¼æ¾å¼åççº¿æ§è§åé®é¢çæä¼ä»·å¼åªæ¯åæ¥çæ´æ°è§åé®é¢çä¸ä¸ªä¸çä¼°è®¡ï¼åè®¾é®é¢æ¯æå°åé®é¢ï¼ï¼ä½æ¯ï¼å¦ææ¾å¼åççº¿æ§è§åé®é¢çæä¼è§£æ°å¥½æ¯æ´æ°è§£ï¼é£ä¹ï¼å®ä¹ä¸å®æ¯åæ¥çæ´æ°è§åé®é¢çæä¼è§£ï¼

ä¸ä¸ªèªç¶çé®é¢æ¯ï¼æ¯å¦å­å¨æ¡ä»¶ï¼è½å¤ä¿è¯çº¿æ§è§åé®é¢çæä¼è§£é½æ¯æ´æ°è§£ï¼å ¨å¹ºæ¨¡ç©éµçæ¦å¿µå°±æä¾äºè¿æ ·çä¸ä¸ªæ¡ä»¶ï¼

å ¨å¹ºæ¨¡ç©éµ

å¦æç©éµ ð´ âððÃðAâRmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå­æ¹éµçè¡åå¼é½æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ç§°ä¸ºä¸ä¸ª **å ¨å¹ºæ¨¡ç©éµ** ï¼totally unimodular matrixï¼ï¼

ç¹å«å°ï¼å ¨å¹ºæ¨¡ç©éµçææå ç´ é½æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨å ¨å¹ºæ¨¡ç©éµçæ¦å¿µï¼å¯ä»¥åè¿°å¦ä¸ç»è®ºï¼

å®ç

å¯¹äºå ¨å¹ºæ¨¡ç©éµ ð´ âððÃðAâZmÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð âððbâZm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âððcâZn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çº¿æ§è§åé®é¢åå ¶å¯¹å¶é®é¢

min{ððð¥:ð´ð¥=ð,ð¥â¥0}=max{ððð¦:ð´ðð¦â¤ð}min{cTx:Ax=b,xâ¥0}=max{bTy:ATyâ¤c}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é½ææ´æ°æä¼è§£ï¼åªè¦å®ä»¬é½æçï¼

è¯æ

åæå·²ç»è¯´æï¼çº¿æ§è§åé®é¢çæä¼è§£éå¯ä»¥åä½å®çä¸ä¸ªæå°é¢ï¼èåè æ¯ç±è¥å¹²çº¿æ§ç¬ç«çç´§çº¦æä½ä¸ºç­å¼èç«å¾å°çæ¹ç¨ç»çè§£ï¼

{ð¥âðð:ðððð¥=ðð,Â âðâð½}.{xâRn:ajTx=bj,Â âjâJ}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®°è¿ä¸ªæ¹ç¨ç»ä¸º ð´ð½ð¥ =ðð½AJx=bJ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ ð´ð½ =(ð´1,ð´2)AJ=(A1,A2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð´1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ»¡ç§©çæ¹éµï¼è¡åå¼ä¸º Â±1Â±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ç± Cramer æ³åï¼è§£

ð¥=(ð´â11ðð½0)x=(A1â1bJ0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±æ¯æå°é¢ä¸çä¸ä¸ªæ´æ°è§£ï¼

å¸¸è§çå¾è®ºæ¨¡åä¸­ï¼ç½ç»æµãæç­è·¯ãäºåå¾ç­å¯¹åºççº¿æ§è§åé®é¢çç³»æ°ç©éµé½æ¯å ¨å¹ºæ¨¡ç©éµï¼å æ­¤ï¼åªéè¦è¿äºé®é¢ä» æ¶åæ´æ°åæ°ï¼å®ä»¬çæä¼è§£å°±å¯ä»¥åä½æ´æ°ï¼èä¸ç¨æ å¿çº¿æ§è§åé®é¢çè§£å¯¹åºçåæ°æµãåæ°å¹é ç­æ å½¢ï¼æä»¥ï¼[æå¤§æµ](../../graph/flow/max-flow/)ã[æå°å²](../../graph/flow/min-cut/)ã[æå°è´¹ç¨æµ](../../graph/flow/min-cost/)ã[æç­è·¯](../../graph/shortest-path/)ã[å·®åçº¦æ](../../graph/diff-constraints/)ã[äºåå¾æå¤§ï¼æï¼å¹é åæå°ç¹è¦ç](../../graph/graph-matching/bigraph-match/#çº¿æ§è§åå½¢å¼) ç­é®é¢ï¼é½å¯ä»¥è½¬åä¸ºçº¿æ§è§åé®é¢æ±è§£ï¼èä¸ï¼æå¤§æµä¸æå°å²ãæç­è·¯ä¸å·®åçº¦æãäºåå¾æå¤§å¹é åæå°ç¹è¦çï¼ä¸¤ä¸¤äºä¸ºå¯¹å¶é®é¢ï¼

é¤æ­¤ä¹å¤ï¼è¿æä¸äºå¸¸è§çå¾è®ºæ¨¡åï¼å®ææçå¯è¡è§£æ°å·§æ¯æä¸ªé¡¶ç¹åä¸ºæ´ç¹çå¤èå½¢çå ¨ä½é¡¶ç¹ï¼å æ­¤ï¼å¯ä»¥éè¿å·§å¦å°éåçº¦æï¼ä½¿å¾ç¸åºçç»åä¼åé®é¢çè§£ï¼æ°ä¸ºæä¸ªçº¿æ§è§åé®é¢çæä¼è§£ï¼ä¾å¦ï¼ä¸è¬å¾å¹é åçææ ç­å¾è®ºæ¨¡åé½å±äºè¿ç§æ åµï¼å æ­¤ [ä¸è¬å¾æå¤§ï¼æï¼å¹é ](../../graph/graph-matching/general-weight-match/) å [æå°çææ ](../../graph/mst/) ç­é®é¢åæ ·å¯ä»¥è½¬åä¸ºçº¿æ§è§åé®é¢ï¼

## åèæç®ä¸æ³¨é

  * Schrijver, Alexander. Theory of linear and integer programming. John Wiley & Sons, 1998.
  * Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
  * [Duality in linear programming. Part 1âdefinition and construction. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105049)
  * [Duality in linear programming. Part 2âin competitive programming. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105789)

* * *

  1. ä¸åæç®å¯è½å¯¹è¿ä¸¤ä¸ªåè¯çå®ä¹æçä¸åçå®ä¹ï¼æäºæç®ä¼å°æççæ å½¢ç§°ä½ãå¤é¢ä½ãï¼èå°æ ççæ å½¢ç§°ä½ãå¤èå½¢ãï¼æäºæç®ä¸ä¼åå®å®ä»¬ä¸å®æ¯å¸éï¼æäºæç®ä¼ç¨ãå¤é¢ä½ãç§°å¼ä¸ç»´ç©ºé´ä¸­çå¤èå½¢ï¼æ¬æéåäºä¸ Schrijver (1998) å Boyd and Vandenberghe (2004) ç­æç®ä¸è´çå®ä¹ï¼Â â©

  2. æ´ä¸¥æ ¼çè¡¨è¿°æ¯ï¼å®ä»¬ä¹é´å¯ä»¥å¨å¤é¡¹å¼æ¶é´å ç¸äºå½çº¦ï¼Â â©

  3. å ¶å®ç¨äºè§£å³ä¸ç­å¼ç»çæ¹æ³è¿å æ¬ FourierâMotzkin æ¶å æ³å AgmonâMotzkinâSchoenberg æ¾å¼æ³ç­ï¼å®ä»¬æ´ä¸ºç´æ¥ï¼ä½æ¯æçå¾å¾ä¸é«ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/3/9 02:30:31ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-programming.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/linear-programming.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [zryi2003](https://github.com/zryi2003), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [huhaoo](https://github.com/huhaoo), [Konano](https://github.com/Konano), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [partychicken](https://github.com/partychicken), [Suyun514](mailto:suyun514@qq.com), [AngelKitty](https://github.com/AngelKitty), [baker221](https://github.com/baker221), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [isdanni](https://github.com/isdanni), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [QAQAutoMaton](https://github.com/QAQAutoMaton), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [c-forrest](https://github.com/c-forrest), [eleven-mile](https://github.com/eleven-mile), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [xiaodong2077](https://github.com/xiaodong2077), [yusancky](https://github.com/yusancky), [YZircon](https://github.com/YZircon), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
