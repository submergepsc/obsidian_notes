# ç©éµ - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/matrix/

# ç©éµ

æ¬æä»ç»çº¿æ§ä»£æ°ä¸­ä¸ä¸ªéå¸¸éè¦çå å®¹ââç©éµï¼Matrixï¼ï¼ä¸»è¦è®²è§£ç©éµçæ§è´¨ãè¿ç®ï¼ä»¥åç©éµä¹æ³çä¸äºåºç¨ï¼

## åéä¸ç©éµ

å¨çº¿æ§ä»£æ°ä¸­ï¼åéåä¸ºååéåè¡åéï¼

Warning

å¨ä¸­å½å°æ¹¾å°åºå ³äºãåãä¸ãè¡ãçç¿»è¯ï¼æ°å¥½ä¸ä¸­å½å¤§éå°åºç¸åï¼å¨ **OI Wiki** æç §ä¸­å½å¤§éå°åºçä¹ æ¯ï¼éç¨åï¼columnï¼ä¸è¡ï¼rowï¼çç¿»è¯ï¼

çº¿æ§ä»£æ°çä¸»è¦ç ç©¶å¯¹è±¡æ¯ååéï¼çº¦å®ä½¿ç¨ç²ä½å°åå­æ¯è¡¨ç¤ºååéï¼å¨ç¨å°å¤§éåéä¸ç©éµççº¿æ§ä»£æ°ä¸­ï¼ä¸å¼èµ·æ··æ·çæ åµä¸ï¼å¨æåæ¶ï¼å­æ¯ä¸æ¹çåéè®°å·å¯ä»¥çç¥ä¸åï¼

åéä¹æ¯ç¹æ®çç©éµï¼å¦ææ³è¦è¡¨ç¤ºè¡åéï¼éè¦å¨ç²ä½å°åå­æ¯å³ä¸æ¹åè½¬ç½®è®°å·ï¼è¡åéå¨çº¿æ§ä»£æ°ä¸­ä¸è¬è¡¨ç¤ºæ¹ç¨ï¼

## å¼å ¥

ç©éµçå¼å ¥æ¥èªäºçº¿æ§æ¹ç¨ç»ï¼ä¸åéç±»ä¼¼ï¼ç©éµä½ç°äºä¸ç§å¯¹æ°æ®ãæå å¤çãçææ³ï¼

ä¾å¦ï¼å°çº¿æ§æ¹ç¨ç»ï¼

â§{ {â¨{ {â©7ð¥1+8ð¥2+9ð¥3=134ð¥1+5ð¥2+6ð¥3=12ð¥1+2ð¥2+3ð¥3=11{7x1+8x2+9x3=134x1+5x2+6x3=12x1+2x2+3x3=11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸è¬ç¨åæ¬å·ææ¹æ¬å·è¡¨ç¤ºç©éµï¼å°ä¸è¿°ç³»æ°æ½åºæ¥ï¼åæç©éµä¹æ³çå½¢å¼ï¼

ââ â ââ789456123ââ â ââ ââ â ââð¥1ð¥2ð¥3ââ â ââ =ââ â ââ131211ââ â ââ (789456123)(x1x2x3)=(131211)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç®è®°ä¸ºï¼

ð´ð¥=ðAx=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³æªç¥æ°ååé xï¼å·¦ä¹ä¸ä¸ªç©éµ Aï¼å¾å°ååé bï¼è¿ä¸ªå¼å­å¯ä»¥è®¤ä¸ºæ¯çº¿æ§ä»£æ°çåºæ¬å½¢å¼ï¼

çº¿æ§ä»£æ°ä¸»è¦ç ç©¶çè¿ç®æ¨¡åæ¯å ç§¯ï¼å ç§¯æ¯å ç¸ä¹åç¸å ï¼æ¯è¡åéå·¦ä¹ååéï¼å¾å°ä¸ä¸ªæ°çè¿ç¨ï¼

ç©éµä¹æ³æ¯å ç§¯çæå±ï¼ç©éµä¹æ³ç­ä»·äºå·¦è¾¹ç©éµæ½åºä¸è¡ï¼ä¸å³è¾¹ç©éµæ½åºä¸åè¿è¡å ç§¯ï¼å¾å°ç»æç©éµçå¯¹åºå ç´ ï¼å£è¯ãå·¦è¡å³åãï¼

å½ç ç©¶å¯¹è±¡æ¯å³è¾¹çååéæ¶ï¼ç©éµä¹æ³ç¸å½äºå¯¹ååéè¿è¡å·¦ä¹ï¼å¨å·¦ä¹çè§ç¹ä¸ï¼ç©éµå°±æ¯å¯¹ååéçåæ¢ï¼å°ç©éµä¹æ³ä¸­å³è¾¹ç©éµçæ¯ä¸ä¸ªååéè¿è¡åæ¢ï¼å¯¹åºå°å¾å°ç»æç©éµä¸­æ¯ä¸ä¸ªååéï¼

ç©éµå¯ä»¥å¯¹ä¸ä¸ªååéè¿è¡åæ¢ï¼ä¹å¯ä»¥å¯¹ä¸ç»ååéè¿è¡ãæå ãåæ¢ï¼çè³å¯ä»¥å¯¹æ´ä¸ªç©ºé´ââå³å ¨ä½ååéè¿è¡åæ¢ï¼å½ç©éµè¢«è§ä¸ºå¯¹æ´ä¸ªç©ºé´åæ¢çæ¶åï¼ä¹å°±è±ç¦»äºç©ºé´ï¼æä¸ºäºçº¯ç²¹åæ¢çå­å¨ï¼

## å®ä¹

å¯¹äºç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸»å¯¹è§çº¿æ¯æ ð´ð,ðAi,i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ç´ ï¼

ä¸è¬ç¨ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥è¡¨ç¤ºåä½ç©éµï¼å°±æ¯ä¸»å¯¹è§çº¿ä¸ä¸º 1ï¼å ¶ä½ä½ç½®ä¸º 0ï¼

### ååç©éµ

ä¸¤ä¸ªç©éµï¼è¡æ°ä¸åæ°å¯¹åºç¸åï¼ç§°ä¸ºååç©éµï¼

### æ¹éµ

è¡æ°ç­äºåæ°çç©éµç§°ä¸ºæ¹éµï¼æ¹éµæ¯ä¸ç§ç¹æ®çç©éµï¼å¯¹äºãðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶ç©éµãçä¹ æ¯è¡¨è¿°ï¼å®é ä¸è®²çæ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶æ¹éµï¼é¶æ°ç¸åçæ¹éµä¸ºååç©éµï¼

ç ç©¶æ¹ç¨ç»ãåéç»ãç©éµçç§©çæ¶åï¼ä½¿ç¨ä¸è¬çç©éµï¼ç ç©¶ç¹å¾å¼åç¹å¾åéãäºæ¬¡åçæ¶åï¼ä½¿ç¨æ¹éµï¼

#### ä¸»å¯¹è§çº¿

æ¹éµä¸­è¡æ°ç­äºåæ°çå ç´ ææä¸»å¯¹è§çº¿ï¼

#### å¯¹ç§°ç©éµ

å¦ææ¹éµçå ç´ å ³äºä¸»å¯¹è§çº¿å¯¹ç§°ï¼å³å¯¹äºä»»æç ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçå ç´ ä¸ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçå ç´ ç¸ç­ï¼åå°æ¹éµç§°ä¸ºå¯¹ç§°ç©éµï¼

#### å¯¹è§ç©éµ

ä¸»å¯¹è§çº¿ä¹å¤çå ç´ åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹éµç§°ä¸ºå¯¹è§ç©éµï¼ä¸è¬è®°ä½ï¼

diagâ¡{ð1,â¯,ðð}diagâ¡{Î»1,â¯,Î»n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¼ä¸­ç ð1,â¯,ððÎ»1,â¯,Î»n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸»å¯¹è§çº¿ä¸çå ç´ ï¼

å¯¹è§ç©éµæ¯å¯¹ç§°ç©éµï¼

å¦æå¯¹è§ç©éµçå ç´ åä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç§°ä¸ºåä½ç©éµï¼è®°ä¸º ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦ä¹æ³å¯ä»¥è¿è¡ï¼æ è®ºå½¢ç¶ï¼ä»»ä½ç©éµä¹åä½ç©éµä»ç¶ä¿æä¸åï¼

#### ä¸è§ç©éµ

å¦ææ¹éµä¸»å¯¹è§çº¿å·¦ä¸æ¹çå ç´ åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç§°ä¸ºä¸ä¸è§ç©éµï¼å¦ææ¹éµä¸»å¯¹è§çº¿å³ä¸æ¹çå ç´ åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç§°ä¸ºä¸ä¸è§ç©éµï¼

ä¸¤ä¸ªä¸ï¼ä¸ï¼ä¸è§ç©éµçä¹ç§¯ä»ç¶æ¯ä¸ï¼ä¸ï¼ä¸è§ç©éµï¼å¦æå¯¹è§çº¿å ç´ åé 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸ï¼ä¸ï¼ä¸è§ç©éµå¯éï¼éä¹æ¯ä¸ï¼ä¸ï¼ä¸è§ç©éµï¼

#### åä½ä¸è§ç©éµ

å¦æä¸ä¸è§ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹è§çº¿å ¨ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§° ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åä½ä¸ä¸è§ç©éµï¼å¦æä¸ä¸è§ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹è§çº¿å ¨ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§° ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åä½ä¸ä¸è§ç©éµï¼

ä¸¤ä¸ªåä½ä¸ï¼ä¸ï¼ä¸è§ç©éµçä¹ç§¯ä»ç¶æ¯åä½ä¸ï¼ä¸ï¼ä¸è§ç©éµï¼åä½ä¸ï¼ä¸ï¼ä¸è§ç©éµçéä¹æ¯åä½ä¸ï¼ä¸ï¼ä¸è§ç©éµï¼

## è¿ç®

### ç©éµççº¿æ§è¿ç®

ç©éµççº¿æ§è¿ç®åä¸ºå åæ³ä¸æ°ä¹ï¼å®ä»¬åä¸ºéä¸ªå ç´ è¿è¡ï¼åªæååç©éµä¹é´å¯ä»¥å¯¹åºç¸å åï¼

### ç©éµçè½¬ç½®

ç©éµçè½¬ç½®ï¼å°±æ¯å¨ç©éµçå³ä¸è§åä¸è½¬ç½®ãTãè®°å·ï¼è¡¨ç¤ºå°ç©éµçè¡ä¸åäºæ¢ï¼

å¯¹ç§°ç©éµè½¬ç½®ååä¿æä¸åï¼

### ç©éµä¹æ³

ç©éµçä¹æ³æ¯åéå ç§¯çæ¨å¹¿ï¼

ç©éµç¸ä¹åªæå¨ç¬¬ä¸ä¸ªç©éµçåæ°åç¬¬äºä¸ªç©éµçè¡æ°ç¸åæ¶æææä¹ï¼

è®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð ÃðPÃM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð ÃðMÃQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼è®¾ç©éµ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹ç§¯ï¼

å ¶ä¸­ç©éµ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ç´ å¯ä»¥è¡¨ç¤ºä¸ºï¼

ð¶ð,ð=ðâð=1ð´ð,ððµð,ðCi,j=âk=1MAi,kBk,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¨ç©éµä¹æ³ä¸­ï¼ç»æ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç©éµçç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçæ°ï¼å°±æ¯ç±ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°ä¸ç©éµ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°åå« **ç¸ä¹åç¸å** å¾å°çï¼è¿éç **ç¸ä¹åç¸å** ï¼å°±æ¯åéçå ç§¯ï¼ä¹ç§¯ç©éµä¸­ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçæ°æ°å¥½æ¯ä¹æ°ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªè¡åéä¸ä¹æ°ç©éµ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªååéçå ç§¯ï¼å£è¯ä¸º **å·¦è¡å³å** ï¼

çº¿æ§ä»£æ°ç ç©¶çåéå¤ä¸ºååéï¼æ ¹æ®è¿æ ·çå¯¹ç©éµä¹æ³çå®ä¹æ¹æ³ï¼ç»å¸¸ç ç©¶å¯¹ååéå·¦ä¹ä¸ä¸ªç©éµçå·¦ä¹è¿ç®ï¼åæ¶ä¹å¯ä»¥å¨è¿éçåºãæå å¤çãçææ³ï¼åæ¶å¤çå¾å¤ä¸ªåéå ç§¯ï¼

ç©éµä¹æ³æ»¡è¶³ç»åå¾ï¼ä¸æ»¡è¶³ä¸è¬çäº¤æ¢å¾ï¼

å©ç¨ç»åå¾ï¼ç©éµä¹æ³å¯ä»¥å©ç¨ [å¿«éå¹](../../binary-exponentiation/) çææ³æ¥ä¼åï¼

å¨æ¯èµä¸­ï¼ç±äºçº¿æ§éæ¨å¼å¯ä»¥è¡¨ç¤ºæç©éµä¹æ³çå½¢å¼ï¼ä¹éå¸¸ç¨ç©éµå¿«éå¹æ¥æ±çº¿æ§éæ¨æ°åçæä¸é¡¹ï¼

#### ä¼å

é¦å å¯¹äºæ¯è¾å°çç©éµï¼å¯ä»¥èèç´æ¥æå¨å±å¼å¾ªç¯ä»¥åå°å¸¸æ°ï¼

å¯ä»¥éæ°æåå¾ªç¯ä»¥æé«ç©ºé´å±é¨æ§ï¼è¿æ ·çä¼åä¸ä¼æ¹åç©éµä¹æ³çæ¶é´å¤æåº¦ï¼ä½æ¯ä¼å¾å°å¸¸æ°çº§å«çæåï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text // ä»¥ä¸æçåèä»£ç ä¸ºä¾ mat operator * ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) for ( int k = 0 ; k < sz ; ++ k ) { res . a [ i ][ j ] += mul ( a [ i ][ k ], T . a [ k ][ j ]); res . a [ i ][ j ] %= MOD ; } return res ; } // ä¸å¦ mat operator * ( const mat & T ) const { mat res ; int r ; for ( int i = 0 ; i < sz ; ++ i ) for ( int k = 0 ; k < sz ; ++ k ) { r = a [ i ][ k ]; for ( int j = 0 ; j < sz ; ++ j ) res . a [ i ][ j ] += T . a [ k ][ j ] * r , res . a [ i ][ j ] %= MOD ; } return res ; } ```   
---|---  
  
### æ¹éµçé

æ¹éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéç©éµ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä½¿å¾ ð´ Ãð =ð¼AÃP=I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼

éç©éµä¸ä¸å®å­å¨ï¼å¦æå­å¨ï¼å¯ä»¥ä½¿ç¨ [é«æ¯æ¶å ](../../numerical/gauss/) è¿è¡æ±è§£ï¼

### æ¹éµçè¡åå¼

è¡åå¼æ¯æ¹éµçä¸ç§è¿ç®ï¼

## åèä»£ç 

ä¸è¬æ¥è¯´ï¼å¯ä»¥ç¨ä¸ä¸ªäºç»´æ°ç»æ¥æ¨¡æç©éµï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` |  ```text struct mat { LL a [ sz ][ sz ]; mat () { memset ( a , 0 , sizeof a ); } mat operator \- ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) { res . a [ i ][ j ] = ( a [ i ][ j ] \- T . a [ i ][ j ]) % MOD ; } return res ; } mat operator \+ ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) { res . a [ i ][ j ] = ( a [ i ][ j ] \+ T . a [ i ][ j ]) % MOD ; } return res ; } mat operator * ( const mat & T ) const { mat res ; int r ; for ( int i = 0 ; i < sz ; ++ i ) for ( int k = 0 ; k < sz ; ++ k ) { r = a [ i ][ k ]; for ( int j = 0 ; j < sz ; ++ j ) res . a [ i ][ j ] += T . a [ k ][ j ] * r , res . a [ i ][ j ] %= MOD ; } return res ; } mat operator ^ ( LL x ) const { mat res , bas ; for ( int i = 0 ; i < sz ; ++ i ) res . a [ i ][ i ] = 1 ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) bas . a [ i ][ j ] = a [ i ][ j ] % MOD ; while ( x ) { if ( x & 1 ) res = res * bas ; bas = bas * bas ; x >>= 1 ; } return res ; } }; ```   
---|---  
  
## çå¾ çº¿æ§æ¹ç¨ç»çä¸¤ç§è§è§

çå¾ ç©éµ Aï¼æè åæ¢ Aï¼æä¸¤ç§è§è§ï¼

ç¬¬ä¸ç§è§ç¹ï¼æè¡çï¼è§å¯ A çæ¯ä¸è¡ï¼è¿æ ·ä¸æ¥æ A çä½æ¹ç¨ç»ï¼äºæ¯å°±æäºæ¶å æ³è§£æ¹ç¨çè¿ç¨ï¼

ç¬¬äºç§è§ç¹ï¼æåçï¼è§å¯ A çæ¯ä¸åï¼A æ¬èº«ä¹æ¯ç±ååéææçï¼æ­¤æ¶ç¸å½äºæåæ¢ A æ¬èº«çæäºååéç»ï¼è x æ¯æªç¥æ°ç³»æ°ï¼æè A å½ä¸­çè¿ç»ååéè½ä¸è½é ä¸æªç¥æ°ï¼ååºååé bï¼

ä¾å¦ï¼æç« å¼å¤´çä¾å­åä¸ºï¼

ââ â ââ741ââ â ââ ð¥1+ââ â ââ852ââ â ââ ð¥2+ââ â ââ963ââ â ââ ð¥3=ââ â ââ131211ââ â ââ (741)x1+(852)x2+(963)x3=(131211)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è§£æ¹ç¨åä¸ºç ç©¶ï¼æ¯å¦å¯ä»¥éè¿è°æ´ä¸ä¸ªç³»æ° xï¼ä½¿å¾ç»å®çä¸ä¸ªåºåéè½å¤ååºç»æçåéï¼

æåçæ¯æè¡çæ´æ°é¢ï¼å¨æåççè§è§ä¸ï¼å¯ä»¥ç ç©¶çº¿æ§æ å ³ä¸çº¿æ§ç¸å ³ï¼

## ç©éµä¹æ³çåºç¨

### ç©éµå ééæ¨

ä»¥ [ææ³¢é£å¥æ°åï¼Fibonacci Sequenceï¼](../../combinatorics/fibonacci/) ä¸ºä¾ï¼å¨ææ³¢é£å¥æ°åå½ä¸­ï¼ð¹1 =ð¹2 =1F1=F2=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¹ð =ð¹ðâ1 +ð¹ðâ2(ð â¥3)Fi=Fiâ1+Fiâ2(iâ¥3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦ææä¸éé¢ç®è®©ä½ æ±ææ³¢é£å¥æ°åç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹çå¼ï¼æç®åçæ¹æ³è«è¿äºç´æ¥éæ¨äºï¼ä½æ¯å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çèå´è¾¾å°äº 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çº§å«ï¼éæ¨å°±ä¸è¡äºï¼æ­¤æ¶æä»¬å¯ä»¥èèç©éµå ééæ¨ï¼

æ ¹æ®ææ³¢é£å¥æ°å [éæ¨å ¬å¼çç©éµå½¢å¼](../../combinatorics/fibonacci/#ç©éµå½¢å¼):

[ð¹ðâ1ð¹ðâ2][1110]=[ð¹ðð¹ðâ1][Fnâ1Fnâ2][1110]=[FnFnâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®ä¹åå§ç©éµ ans =[ð¹2ð¹1] =[11],base =[1110]ans=[F2F1]=[11],base=[1110]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ð¹ðFn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ç­äº ansbaseðâ2ansbasenâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸ªç©éµçç¬¬ä¸è¡ç¬¬ä¸åå ç´ ï¼ä¹å°±æ¯ [11][1110]ðâ2[11][1110]nâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ä¸è¡ç¬¬ä¸åå ç´ ï¼

æ³¨æ

ç©éµä¹æ³ä¸æ»¡è¶³äº¤æ¢å¾ï¼æä»¥ä¸å®ä¸è½åæ [1110]ðâ2[11][1110]nâ2[11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ä¸è¡ç¬¬ä¸åå ç´ ï¼å¦å¤ï¼å¯¹äº ð â¤2nâ¤2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼ç´æ¥è¾åº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼ä¸éè¦æ§è¡ç©éµå¿«éå¹ï¼

ä¸ºä»ä¹è¦ä¹ä¸ basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç©éµç ð â2nâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡æ¹èä¸æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡æ¹å¢ï¼å ä¸º ð¹1,ð¹2F1,F2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸éè¦è¿è¡ç©éµä¹æ³å°±è½æ±çï¼ä¹å°±æ¯è¯´ï¼å¦æåªè¿è¡ä¸æ¬¡ä¹æ³ï¼å°±å·²ç»æ±åº ð¹3F3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºï¼å¦æè¿ä¸æ¯å¾çè§£ä¸ºä»ä¹å¹æ¯ ð â2nâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å»ºè®®æç®ä¸ä¸ï¼

ä¸é¢æ¯æ±ææ³¢é£å¥æ°åç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹å¯¹ 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡çç¤ºä¾ä»£ç ï¼æ ¸å¿é¨åï¼ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text constexpr int mod = 1000000007 ; struct Matrix { int a [ 3 ][ 3 ]; Matrix () { memset ( a , 0 , sizeof a ); } Matrix operator * ( const Matrix & b ) const { Matrix res ; for ( int i = 1 ; i <= 2 ; ++ i ) for ( int j = 1 ; j <= 2 ; ++ j ) for ( int k = 1 ; k <= 2 ; ++ k ) res . a [ i ][ j ] = ( res . a [ i ][ j ] \+ a [ i ][ k ] * b . a [ k ][ j ]) % mod ; return res ; } } ans , base ; void init () { base . a [ 1 ][ 1 ] = base . a [ 1 ][ 2 ] = base . a [ 2 ][ 1 ] = 1 ; ans . a [ 1 ][ 1 ] = ans . a [ 1 ][ 2 ] = 1 ; } void qpow ( int b ) { while ( b ) { if ( b & 1 ) ans = ans * base ; base = base * base ; b >>= 1 ; } } int main () { int n = read (); if ( n <= 2 ) return puts ( "1" ), 0 ; init (); qpow ( n \- 2 ); println ( ans . a [ 1 ][ 1 ] % mod ); } ```   
---|---  
  
è¿æ¯ä¸ä¸ªç¨å¾®å¤æä¸äºçä¾å­ï¼

ð1=ð2=0ðð=7ððâ1+6ððâ2+5ð+4Ã3ðf1=f2=0fn=7fnâ1+6fnâ2+5n+4Ã3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬åç°ï¼ððfn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððâ1,ððâ2,ðfnâ1,fnâ2,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå ³ï¼äºæ¯èèæé ä¸ä¸ªç©éµæè¿°ç¶æï¼

ä½æ¯åç°å¦æç©éµä» æè¿ä¸ä¸ªå ç´ [ððððâ1ð][fnfnâ1n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é¾ä»¥æé åºè½¬ç§»æ¹ç¨çï¼å ä¸ºä¹æ¹è¿ç®å +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ æ³ç¨ç©éµæè¿°ï¼

äºæ¯èèæé ä¸ä¸ªæ´å¤§çç©éµï¼

[ððððâ1ð3ð1][fnfnâ1n3n1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬å¸ææé ä¸ä¸ªéæ¨ç©éµå¯ä»¥è½¬ç§»å°

[ðð+1ððð+13ð+11][fn+1fnn+13n+11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è½¬ç§»ç©éµå³ä¸º

â¡â¢ â¢ â¢ â¢ â¢â£71000600005010012003050101â¤â¥ â¥ â¥ â¥ â¥â¦[71000600005010012003050101]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ç©éµè¡¨è¾¾ä¿®æ¹

[ãTHUSCH 2017ãå¤§é­æ³å¸](https://loj.ac/p/2980)

å¤§é­æ³å¸å° L å¶ä½äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé­åæ°´æ¶çï¼æ¯ä¸ªæ°´æ¶çææ°´ãç«ãåä¸ä¸ªå±æ§çè½éå¼ï¼å° L æè¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°´æ¶çå¨å°ä¸ä»åååææä¸è¡ï¼ç¶åå¼å§ä»å¤©çé­æ³è¡¨æ¼ï¼

æä»¬ç¨ ð´ð,Â ðµð,Â ð¶ðAi,Â Bi,Â Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«è¡¨ç¤ºä»åååç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°´æ¶çï¼ä¸æ ä» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼çæ°´ãç«ãåçè½éå¼ï¼

å° L è®¡åæ½å± ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡é­æ³ï¼æ¯æ¬¡ï¼ä»ä¼éæ©ä¸ä¸ªåºé´ [ð,ð][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶åæ½å±ä»¥ä¸ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤§ç±»ã77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§é­æ³ä¹ä¸ï¼

  1. é­åæ¿åï¼ä»¤åºé´éæ¯ä¸ªæ°´æ¶çä¸­ **ç¹å®å±æ§** çè½éçåï¼ä»èä½¿å¦ä¸ä¸ª **ç¹å®å±æ§** çè½éå¢å¼ºï¼å ·ä½æ¥è¯´ï¼æä»¥ä¸ä¸ç§å¯è½çè¡¨ç°å½¢å¼ï¼

     * ç«å ç´ æ¿åæ°´å ç´ è½éï¼ä»¤ ð´ð =ð´ð +ðµðAi=Ai+Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * åå ç´ æ¿åç«å ç´ è½éï¼ä»¤ ðµð =ðµð +ð¶ðBi=Bi+Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * æ°´å ç´ æ¿ååå ç´ è½éï¼ä»¤ ð¶ð =ð¶ð +ð´ðCi=Ci+Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**éè¦æ³¨æçæ¯ï¼å¢å¼ºä¸ç§å±æ§çè½éå¹¶ä¸ä¼æ¹åå¦ä¸ç§å±æ§çè½éï¼ä¾å¦ ð´ð =ð´ð +ðµðAi=Ai+Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸ä¼ä½¿ ðµðBi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¢å æåå°ï¼**

  2. é­åå¢å¼ºï¼å° L æ¥èæ³æï¼æ¶èèªèº« ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¹æ³åå¼ï¼æ¥æ¹ååºé´éæ¯ä¸ªæ°´æ¶çç **ç¹å®å±æ§** çè½éï¼å ·ä½æ¥è¯´ï¼æä»¥ä¸ä¸ç§å¯è½çè¡¨ç°å½¢å¼ï¼

     * ç«å ç´ è½éå®å¼å¢å¼ºï¼ä»¤ ð´ð =ð´ð +ð£Ai=Ai+v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * æ°´å ç´ è½éç¿»åå¢å¼ºï¼ä»¤ ðµð =ðµð â ð£Bi=Biâ v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * åå ç´ è½éå¸æ¶èåï¼ä»¤ ð¶ð =ð£Ci=v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. é­åéæ¾ï¼å° L å°åºé´éæææ°´æ¶ççè½éèéå¨ä¸èµ·ï¼èåæä¸ä¸ªæ°çæ°´æ¶çï¼ç¶åéç»åºå¤è§ä¼ï¼çæçæ°´æ¶çæ¯ç§å±æ§çè½éå¼ç­äºåºé´å æææ°´æ¶çå¯¹åºè½éå¼çä»£æ°åï¼**éè¦æ³¨æçæ¯ï¼é­åéæ¾çè¿ç¨ä¸ä¼çæ­£æ¹ååºé´å æ°´æ¶ççè½é** ï¼

å¼å¾ä¸æçæ¯ï¼å° L å¶é åèåçæ°´æ¶ççåææé½æ¯å®å¶çç OI å·¥åæ°´æ¶ï¼æä»¥è¿äºæ°´æ¶çæä¸ä¸ªè½ééå¼ 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å½æ°´æ¶çä¸­æç§å±æ§çè½éå¼å¤§äºç­äºè¿ä¸ªéå¼æ¶ï¼è½éå¼ä¼èªå¨å¯¹éå¼åæ¨¡ï¼ä»èé¿å æ°´æ¶ççç¸ï¼

å° W ä¸ºå° Lï¼å¯ä¸çï¼è§ä¼ï¼å´è§äºæ´ä¸ªè¡¨æ¼ï¼å¹¶ä¸æ¶å°äºå° L å¨è¡¨æ¼ä¸­èåçæ¯ä¸ªæ°´æ¶çï¼å° W æ³ç¥éï¼è¿äºæ°´æ¶çè´æ¶µçä¸ç§å±æ§çè½éå¼åå«æ¯å¤å°ï¼

ç±äºç©éµçç»åå¾ååé å¾æç«ï¼åç¹ä¿®æ¹å¯ä»¥èªç¶å°æ¨å¹¿å°åºé´ï¼å³æ¨åºç©éµåç´æ¥ç¨çº¿æ®µæ ç»´æ¤åºé´ç©éµä¹ç§¯å³å¯ï¼

ä¸é¢å°ä¸¾å ä¸ªä¾å­ï¼

ð´ð =ð´ð +ð£Ai=Ai+v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè½¬ç§»

[ð´ðµð¶1]â¡â¢ â¢ â¢ â¢â£100001000010ð£001â¤â¥ â¥ â¥ â¥â¦=[ð´+ð£ðµð¶1][ABC1][100001000010v001]=[A+vBC1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ðµð =ðµð â ð£Bi=Biâ v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè½¬ç§»

[ð´ðµð¶1]â¡â¢ â¢ â¢ â¢â£10000ð£0000100001â¤â¥ â¥ â¥ â¥â¦=[ð´ðµâ ð£ð¶1][ABC1][10000v0000100001]=[ABâ vC1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)[ãLibreOJ 6208ãæ ä¸è¯¢é®](https://loj.ac/p/6208)

æä¸æ£µ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èç¹çæ ï¼æ ¹ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·èç¹ï¼æ¯ä¸ªèç¹æä¸¤ä¸ªæå¼ ðð,ð¡ðki,ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå§å¼åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç»åºä¸ç§æä½ï¼

  1. Addâ¡(ð¥,ð)Addâ¡(x,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä½ï¼å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°æ ¹çè·¯å¾ä¸ææç¹ç ðð âðð +ðkiâki+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. Mulâ¡(ð¥,ð)Mulâ¡(x,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä½ï¼å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°æ ¹çè·¯å¾ä¸ææç¹ç ð¡ð âð¡ð +ð Ãððtiâti+dÃki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. Queryâ¡(ð¥)Queryâ¡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä½ï¼è¯¢é®ç¹ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¼ ð¡ð¥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ð,Â ð â¤100000,Â  â10 â¤ð â¤10n,Â mâ¤100000,Â â10â¤dâ¤10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¥ç´æ¥æèï¼ä¸æ¾æä½åç»´æ¤ä¿¡æ¯å¹¶ä¸æ¯å¾å¥½æ³ï¼ä½æ¯ç©éµå¯ä»¥è½»æ¾å°è¡¨è¾¾ï¼

[ðð¡1]â¡â¢ â¢â£100010ð01â¤â¥ â¥â¦=[ð+ðð¡1][ðð¡1]â¡â¢ â¢â£1ð0010001â¤â¥ â¥â¦=[ðð¡+ðÃð1][kt1][100010d01]=[k+dt1][kt1][1d0010001]=[kt+dÃk1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å®é¿è·¯å¾ç»è®¡

é®é¢æè¿°

ç»ä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶æåå¾ï¼æ¯æ¡è¾¹çè¾¹æåä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶åç»ä¸ä¸ªæ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½ çä»»å¡æ¯å¯¹äºææç¹å¯¹ (ð¢,ð£)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±åºä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¿åº¦ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ°éï¼ä¸ä¸å®æ¯ç®åè·¯å¾ï¼å³è·¯å¾ä¸çç¹æè è¾¹å¯è½èµ°å¤æ¬¡ï¼ï¼

æä»¬å°è¿ä¸ªå¾ç¨é»æ¥ç©éµ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºå¾ä¸­çè¾¹ (ð¢ âð£)(uâv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ðº[ð¢,ð£] =1G[u,v]=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä½ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼å¦ææéè¾¹ï¼åè®¾ ðº[ð¢,ð£]G[u,v]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºéè¾¹çæ°éï¼è¡¨ç¤ºè¿ä¸ªæåå¾ï¼ä¸è¿°ç®æ³åæ ·éç¨äºå¾æèªç¯çæ åµï¼

æ¾ç¶ï¼è¯¥é»æ¥ç©éµå¯¹åº ð =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çç­æ¡ï¼

åè®¾æä»¬ç¥éé¿åº¦ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾æ¡æ°ææçç©éµï¼è®°ä¸ºç©éµ ð¶ðCk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬æ³æ± ð¶ð+1Ck+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶æ DP è½¬ç§»æ¹ç¨

ð¶ð+1[ð,ð]=ðâð=1ð¶ð[ð,ð]â ðº[ð,ð]Ck+1[i,j]=âp=1nCk[i,p]â G[p,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬å¯ä»¥æå®çä½ç©éµä¹æ³çè¿ç®ï¼äºæ¯ä¸è¿°è½¬ç§»å¯ä»¥æè¿°ä¸º

ð¶ð+1=ð¶ðâ ðºCk+1=Ckâ G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹æè¿ä¸ªéæ¨å¼å±å¼å¯ä»¥å¾å°

ð¶ð=ðºâ ðºâ¯ðºâðÂ æ¬¡=ðºðCk=Gâ Gâ¯GâkÂ æ¬¡=Gk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦è®¡ç®è¿ä¸ªç©éµå¹ï¼æä»¬å¯ä»¥ä½¿ç¨å¿«éå¹ï¼äºè¿å¶åå¹ï¼çææ³ï¼å¨ ð(ð3logâ¡ð)O(n3logâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤æåº¦å è®¡ç®ç»æï¼

### å®é¿æç­è·¯

é®é¢æè¿°

ç»ä½ ä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å ææåå¾åä¸ä¸ªæ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºæ¯ä¸ªç¹å¯¹ (ð¢,ð£)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¾å°ä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°å¥½å å« ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡è¾¹çæç­è·¯çé¿åº¦ï¼ï¼ä¸ä¸å®æ¯ç®åè·¯å¾ï¼å³è·¯å¾ä¸çç¹æè è¾¹å¯è½èµ°å¤æ¬¡ï¼

æä»¬ä»æé è¿ä¸ªå¾çé»æ¥ç©éµ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðº[ð,ð]G[i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºä» ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹æï¼å¦æ ð,ði,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ç¹ä¹é´æ²¡æè¾¹ï¼é£ä¹ ðº[ð,ð] =âG[i,j]=â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼æéè¾¹çæ åµåè¾¹æçæå°å¼ï¼

æ¾ç¶ä¸è¿°ç©éµå¯¹åº ð =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é®é¢çç­æ¡ï¼æä»¬ä»åè®¾æä»¬ç¥é ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç­æ¡ï¼è®°ä¸ºç©éµ ð¿ðLk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç°å¨æä»¬æ³æ± ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç­æ¡ï¼æ¾ç¶æè½¬ç§»æ¹ç¨

ð¿ð+1[ð,ð]=min1â¤ðâ¤ð{ð¿ð[ð,ð]+ðº[ð,ð]}Lk+1[i,j]=min1â¤pâ¤n{Lk[i,p]+G[p,j]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºå®ä¸æä»¬å¯ä»¥ç±»æ¯ç©éµä¹æ³ï¼ä½ åç°ä¸è¿°è½¬ç§»åªæ¯æç©éµä¹æ³çä¹ç§¯æ±ååæç¸å åæå°å¼ï¼äºæ¯æä»¬å®ä¹è¿ä¸ªè¿ç®ä¸º ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³

ð´âðµ=ð¶Â Â âºÂ Â ð¶[ð,ð]=min1â¤ðâ¤ð{ð´[ð,ð]+ðµ[ð,ð]}AâB=CÂ Â âºÂ Â C[i,j]=min1â¤pâ¤n{A[i,p]+B[p,j]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯å¾å°

ð¿ð+1=ð¿ðâðºLk+1=LkâG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å±å¼éæ¨å¼å¾å°

ð¿ð=ðºââ¦âðºâðÂ æ¬¡=ðºâðLk=Gââ¦âGâkÂ æ¬¡=Gâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬ä»ç¶å¯ä»¥ç¨ç©éµå¿«éå¹çæ¹æ³è®¡ç®ä¸å¼ï¼å ä¸ºå®æ¾ç¶æ¯å ·æç»åå¾çï¼æ¶é´å¤æåº¦ ð(ð3logâ¡ð)O(n3logâ¡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### éé¿è·¯å¾è®¡æ°/æç­è·¯

ä¸è¿°ç®æ³åªéç¨äºè¾¹æ°åºå®çæ åµï¼ç¶èæä»¬å¯ä»¥æ¹è¿ç®æ³ä»¥è§£å³è¾¹æ°å°äºç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼å ·ä½å°ï¼èèä»¥ä¸é®é¢ï¼

é®é¢æè¿°

ç»ä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶æåå¾ï¼è¾¹æä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶åç»ä¸ä¸ªæ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½ çä»»å¡æ¯å¯¹äºæ¯ä¸ªç¹å¯¹ (ð¢,ð£)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¾å°ä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¿åº¦å°äºç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ°éï¼ä¸ä¸å®æ¯ç®åè·¯å¾ï¼å³è·¯å¾ä¸çç¹æè è¾¹å¯è½èµ°å¤æ¬¡ï¼ï¼

æä»¬å¯¹äºæ¯ä¸ªç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å»ºç«ä¸ä¸ªèç¹ ð£â²vâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¨äºè®°å½ç­æ¡ï¼å¹¶å¨å¾ä¸­å å ¥ (ð£,ð£â²)(v,vâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð£â²,ð£â²)(vâ²,vâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸¤æ¡è¾¹ï¼é£ä¹å¯¹äºç¹å¯¹ (ð¢,ð£)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹æ°å°äºç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ°éï¼å°±åä» ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð£â²vâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¾¹æ°æ°å¥½ç­äº ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾çæ°éç¸ç­ï¼è¿æ¯å ä¸ºå¯¹äºä»»æä¸æ¡è¾¹æ°ä¸º ð(ð â¤ð)m(mâ¤k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾ (ð0 =ð¢) âð1 âð2 ââ¯ âððâ1 â(ðð =ð£)(p0=u)âp1âp2ââ¯âpmâ1â(pm=v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½å­å¨ä¸æ¡è¾¹æ°ä¸º ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·¯å¾ (ð0 =ð¢) âð1 âð2 ââ¯ âððâ1 â(ðð =ð£) âð£â² ââ¯ âð£â²(p0=u)âp1âp2ââ¯âpmâ1â(pm=v)âvâ²ââ¯âvâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¹ä¸ä¸å¯¹åºï¼

å¯¹äºæ±è¾¹æ°å°äºç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­è·¯ï¼åªéå¯¹æ¯ä¸ªç¹å ä¸ä¸ªè¾¹æä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çèªç¯å³å¯ï¼

## ä¹ é¢

  * [æ´è°· P1962 ææ³¢é£å¥æ°å](https://www.luogu.com.cn/problem/P1962)ï¼å³ä¸é¢çä¾é¢ï¼åé¢ POJ3070
  * [æ´è°· P1349 å¹¿ä¹ææ³¢é£å¥æ°å](https://www.luogu.com.cn/problem/P1349)ï¼basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç©éµéè¦ååä¸ä¸
  * [æ´è°· P1939ãæ¨¡æ¿ãç©éµå éï¼æ°åï¼](https://www.luogu.com.cn/problem/P1939)ï¼basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç©éµåæäº 3 Ã33Ã3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼æ¨å¯¼è¿ç¨ä¸ä¸é¢å·®ä¸å¤ï¼

**æ¬é¡µé¢é¨åå å®¹è¯èªåæ[ÐÑÐ°ÑÑÐ°Ð¹ÑÐ¸Ðµ Ð¿ÑÑÐ¸ ÑÐ¸ÐºÑÐ¸ÑÐ¾Ð²Ð°Ð½Ð½Ð¾Ð¹ Ð´Ð»Ð¸Ð½Ñ, ÐºÐ¾Ð»Ð¸ÑÐµÑÑÐ²Ð° Ð¿ÑÑÐµÐ¹ ÑÐ¸ÐºÑÐ¸ÑÐ¾Ð²Ð°Ð½Ð½Ð¾Ð¹ Ð´Ð»Ð¸Ð½Ñ](http://e-maxx.ru/algo/fixed_length_paths) ä¸å ¶è±æç¿»è¯ç [Number of paths of fixed length/Shortest paths of fixed length](https://cp-algorithms.com/graph/fixed_length_paths.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/matrix.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/matrix.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Gesrua](https://github.com/Gesrua), [Anguei](https://github.com/Anguei), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [MegaOwIer](https://github.com/MegaOwIer), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [countercurrent-time](https://github.com/countercurrent-time), [Henry-ZHR](https://github.com/Henry-ZHR), [kxccc](https://github.com/kxccc), [NachtgeistW](https://github.com/NachtgeistW), [369Pai](https://github.com/369Pai), [AngelKitty](https://github.com/AngelKitty), [Chrogeek](https://github.com/Chrogeek), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [InsZVA](https://github.com/InsZVA), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [leoleoasd](https://github.com/leoleoasd), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [oldherd](https://github.com/oldherd), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [weiyong1024](https://github.com/weiyong1024), [xcmvec](https://github.com/xcmvec)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
