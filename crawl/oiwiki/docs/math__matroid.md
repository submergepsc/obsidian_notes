# æéµ - OI Wiki

- Source: https://oi-wiki.org/math/matroid/

# æéµ

## å¼è¨

**æéµï¼Matroidï¼** æ¯åæ¯åÂ·æ ç¹å°¼ï¼Hassler Whitneyï¼äº 1935 å¹´æåºçä¸ç§æ½è±¡ä»£æ°ç»æï¼æ¨å¨ç»ä¸åæ¨å¹¿å ³äºç¬ç«æ§çæ¦å¿µï¼ä¾å¦çº¿æ§ä»£æ°ä¸­ççº¿æ§æ å ³æ§åå¾è®ºä¸­çæ ç¯æ§ï¼

æéµä¸ºå¤çä¸ç¬ç«æ§ç¸å ³çä¼åé®é¢æä¾äºå¼ºå¤§ççè®ºå·¥å ·ï¼å¹¿æ³åºç¨äºç»åæ°å­¦ãå¾è®ºãç®æ³è®¾è®¡ç­é¢åï¼å°¤å ¶å¨ä¸ºè´ªå¿ç®æ³ç­ä¼åæ¹æ³æä¾æ°å­¦çè®ºæ¯ææ¹é¢åæ¥äºéè¦ä½ç¨ï¼

## å®ä¹

### æéµ

ä¸ä¸ª **æéµï¼Matroidï¼** å¯ä»¥è¡¨ç¤ºä¸º ð =(ð¸,I)M=(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼

  * ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªæééï¼ç§°ä¸º **åºç¡éï¼Ground Setï¼** ï¼
  * II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éæï¼ç§°ä¸º **ç¬ç«éæï¼Family of Independent Setsï¼** ï¼å ¶ä¸­çéåç§°ä¸º **ç¬ç«éï¼Independent Setï¼** ï¼æä»¥ä¸ä¸ä¸ªæ§è´¨ï¼

    * **éç©ºæ§** ï¼ç©ºéæ¯ç¬ç«çï¼å³ â  âIâ âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

    * **éä¼ æ§** ï¼ç¬ç«éçä»»æå­éä¹æ¯ç¬ç«éï¼è¥ ð¼ âIIâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯¹äºä»»æ ð¼â² âð¼Iâ²âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð¼â² âIIâ²âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

    * **æ©å¼ æ§** ï¼è¥ ð¼,ð½ âII,JâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ |ð¼| <|ð½||I|<|J|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå­å¨ ð âð½ âð¼jâJâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð¼ âª{ð} âIIâª{j}âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦æä¸ä¸ªå½¢å¦ (ð¸,I)(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»ææ»¡è¶³ä¸è¿°ä¸ä¸ªæ§è´¨ï¼åç§°å ¶ä¸ºä¸ä¸ªæéµï¼

### åº

**åºï¼Basisï¼** æ¯æéµä¸­æå¤§çç¬ç«éï¼å³æ æ³åæ·»å å ç´ èä¿æç¬ç«æ§çç¬ç«éï¼ææåºçéåç§°ä¸º **åºéæ** ï¼è®°ä¸º BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**æ§è´¨** ï¼

  1. **ç­åºæ°æ§** ï¼ææåºçå¤§å°é½ç¸åï¼ç§°ä¸ºæéµç **ç§©ï¼Rankï¼** ï¼

  2. **æ©å¼ æ§** ï¼ä»»ä½ç¬ç«ééè¿æ·»å åºä¸­çå ç´ é½å¯ä»¥æ©å¼ ä¸ºä¸ä¸ªåºï¼

### å

**åï¼Circuitï¼** æ¯æéµä¸­æå°çä¾èµéï¼å³å ¶ææçå­éé½æ¯ç¬ç«çï¼ä½èªèº«ä¸æ¯ç¬ç«éï¼ä»»æä¸¤ä¸ªåä¹é´ä¸å­å¨å å«å ³ç³»ï¼

### ç§©

**ç§©å½æ°ï¼Rank Functionï¼** ð :2ð¸ ââ¤â¥0r:2EâZâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éæ å°å°éè´æ´æ°ï¼å¯¹äºä»»æ ð âð¸SâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(ð)r(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å®ä¹ä¸º ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æå¤§ç¬ç«éçå¤§å°ï¼å³

ð(ð)=max{|ð¼|â£ð¼âðâ§ð¼âI}.r(S)=max{|I|â£IâSâ§IâI}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**æ§è´¨** ï¼

  1. **éè´æ§** ï¼å¯¹äºä»»æ ð âð¸SâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ 0 â¤ð(ð) â¤|ð|0â¤r(S)â¤|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  2. **åè°æ§** ï¼è¥ ð´ âðµ âð¸AâBâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð(ð´) â¤ð(ðµ)r(A)â¤r(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  3. **æ¬¡æ¨¡æ§** ï¼å¯¹äºä»»æ ð´,ðµ âð¸A,BâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð´ âªðµ) +ð(ð´ â©ðµ) â¤ð(ð´) +ð(ðµ)r(AâªB)+r(Aâ©B)â¤r(A)+r(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å ¸åç¤ºä¾

### 1\. ååæéµï¼Uniform Matroidï¼

**å®ä¹** ï¼ç»å®åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åéè´æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ååæéµ ðð,ð¸Uk,E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬ç«éææ¯ææå¤§å°ä¸è¶ è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼è¡¨ç¤ºä¸ºï¼

I={ð¼âð¸â£|ð¼|â¤ð}ï¼I={IâEâ£|I|â¤k}ï¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * **åºï¼Basesï¼** ï¼ææå¤§å°ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼

  * **åï¼Circuitsï¼** ï¼ææå¤§å°ä¸º ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼

  * **ç§©ï¼Rankï¼** ï¼ð(ð¸) =min(ð,|ð¸|)r(E)=min(k,|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ç¬ç«éä¸­æå¤è½æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼

### 2\. å¾æéµï¼Graphical Matroidï¼

**å®ä¹** ï¼ç»å®ä¸ä¸ªæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾æéµ ð(ðº)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºç¡éæ¯è¾¹é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ç¬ç«éææ¯ææä¸å å«ç¯çè¾¹éï¼å³ææçæ£®æï¼

  * **åº** ï¼å¾ä¸­ççææ ï¼å¨è¿éå¾çæ åµä¸ï¼ï¼çææ æ¯æå¤§çç¬ç«éï¼æ æ³åå¢å è¾¹èä¸å½¢æç¯ï¼

  * **å** ï¼å¾ä¸­çç®åç¯ï¼å»æç¯ä¸­çä»»æä¸æ¡è¾¹ï¼å©ä½é¨åé½ä¸ºç¬ç«éï¼

  * **ç§©** ï¼ð(ð¸) =|ð| âðr(E)=|V|âc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾çè¿éåæ¯æ°ï¼å¯¹äºä¸ä¸ªè¿éçæ åå¾ï¼å ¶ç§©ç­äºé¡¶ç¹æ°åä¸ï¼å³ |ð| â1|V|â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### 3\. çº¿æ§æéµï¼Linear Matroidï¼

**å®ä¹** ï¼çº¿æ§æéµåºäºåéç©ºé´ï¼ç»å®åéç©ºé´ ðV![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðV![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çä¸ç»æéåéï¼å ¶ç¬ç«éææ¯ ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ææçº¿æ§æ å ³çåéå­éï¼

  * **åº** ï¼æå¤§ççº¿æ§æ å ³åééï¼å ¶å¤§å°ç­äºåéç©ºé´çç»´æ°ï¼

  * **å** ï¼æå°ççº¿æ§ç¸å ³åééåï¼å ¶ä»»æçå­éé½æ¯ç¬ç«çï¼èèªèº«æ¯çº¿æ§ç¸å ³çï¼

  * **ç§©** ï¼çº¿æ§æéµçç§© ð(ð¸) =dimâ¡(ð)r(E)=dimâ¡(V)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³åéç©ºé´çç»´æ°ï¼ç¬ç«éçå¤§å°ä¸è½è¶ è¿åéç©ºé´çç»´æ°ï¼

### 4\. ååæéµï¼Partition Matroidï¼

**å®ä¹** ï¼å°åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååä¸ºä¸ç¸äº¤çå­é ð¸1,ð¸2,â¦,ð¸ðE1,E2,â¦,Em![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸ºæ¯ä¸ªå­é ð¸ðEi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå®ä¸ä¸ªéè´æ´æ° ððki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ååæéµçç¬ç«éæç±æ»¡è¶³æ¯ä¸ªé¨åéåå ç´ æ°éä¸è¶ è¿ ððki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éç»æï¼è¡¨ç¤ºä¸ºï¼

I={ð¼âð¸â£âð,|ð¼â©ð¸ð|â¤ðð}ï¼I={IâEâ£âi,|Iâ©Ei|â¤ki}ï¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * **åº** ï¼æ»¡è¶³ |ð¼ â©ð¸ð| =ðð|Iâ©Ei|=ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬ç«éæ¯ååæéµçåºï¼æ¯ä¸ªåºå¨æ¯ä¸ªå­éä¸­éåäºæ°å¥½ ððki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼

  * **å** ï¼ååæéµçåæ¯æå°çä¾èµéï¼å³å å«è³å°ä¸ä¸ªå ç´ æ°éè¶ è¿ ððki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼

  * **ç§©** ï¼ååæéµçç§©ä¸º ð(ð¸) =âðð=1ððr(E)=âi=1mki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³æå¤§ç¬ç«éçå¤§å°ç­äºæ¯ä¸ªå­éä¸­å è®¸éåçæå¤§å ç´ æ°çæ»åï¼

### 5\. æè²æéµï¼Colored Matroidï¼

**å®ä¹** ï¼æè²æéµæ¯ååæéµçä¸ç§ç¹æ®å½¢å¼ï¼å ¶ä¸­æ¯ä¸ªå ç´ é½èµäºäºé¢è²ï¼ç»å®åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¢è²é ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ªå ç´ ð âð¸eâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ä¸æä¸ªé¢è² ð âð¶câC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸å ³èï¼æè²æéµçç¬ç«éä¸ä» éè¦æ»¡è¶³æ®éæéµçç¬ç«æ§æ¡ä»¶ï¼è¿å¿ é¡»éµå®é¢è²ä¸æå®çéå¶ï¼ä¾å¦åä¸ç§é¢è²çå ç´ å¨ç¬ç«éä¸­æå¤éåä¸å®æ°éï¼

  * **åº** ï¼æè²æéµçåºæ¯ç¬¦åé¢è²éå¶åç¬ç«æ§æ¡ä»¶çæå¤§ç¬ç«éï¼

  * **å** ï¼åæ¯æå°çä¾èµéï¼å å«è³å°ä¸ä¸ªè¿åç¬ç«æ§æé¢è²éå¶çå ç´ éåï¼

  * **ç§©** ï¼æè²æéµçç§©æ¯æ»¡è¶³é¢è²éå¶æ¡ä»¶ä¸çæå¤§ç¬ç«éå¤§å°ï¼å®æ¢ä¾èµäºæéµçç»æï¼ä¹ä¾èµäºé¢è²éå¶çå ·ä½è§å®ï¼

## æé åè¿ç®

### å¯¹å¶

ç»å®æéµ ð =(ð¸,I)M=(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ **å¯¹å¶æéµ** ðâ =(ð¸,Iâ)Mâ=(E,Iâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å®ä¹ä¸ºï¼

Iâ={ð¼ââð¸â£âðµâI,|ðµ|=ð(ð¸),ðµâð¸âð¼â}ï¼Iâ={IââEâ£âBâI,|B|=r(E),BâEâIâ}ï¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**æ§è´¨** ï¼

  * **åº** ï¼å¯¹å¶æéµ ðâMâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºæ¯ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºå¨åºç¡é ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çè¡¥éï¼æ¢å¥è¯è¯´ï¼å¦æ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºï¼é£ä¹ ð¸ âðµEâB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ ðâMâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºï¼

  * **ç§©å½æ°** ï¼å¯¹å¶æéµçç§©å½æ°ä¸º ðâ(ð) =|ð| âð(ð¸) +ð(ð¸ âð)râ(S)=|S|âr(E)+r(EâS)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼è¿æå³çå¯¹å¶æéµçç§©å¯ä»¥éè¿åºç¡éçå¤§å°ãåæéµçç§©ä»¥åä»åºç¡éä¸­ç§»é¤ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åçç§©æ¥è®¡ç®ï¼

  * **èªåæ§** ï¼å¯¹å¶æéµçå¯¹å¶ä»æ¯åæéµï¼å³ (ðâ)â =ð(Mâ)â=M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**ç¤ºä¾** ï¼

å¯¹äºä¸ä¸ªæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾æéµ ð(ðº)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹å¶ ð(ðº)âM(G)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç±å¾çå²éç»æçæéµï¼å¾æéµ ð(ðº)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºæ¯å¾ä¸­ççææ ï¼èå ¶å¯¹å¶ ð(ðº)âM(G)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºæ¯è¿äºçææ çè¡¥éï¼å¯¹å¶ ð(ðº)âM(G)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååæ¯å¾çæå°å²éï¼å³å°å¾åæä¸¤ä¸ªä¸è¿éé¨åçæå°è¾¹éï¼

ä¾å¦ï¼èèä¸ä¸ªç®åçä¸è§å½¢å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶è¾¹éä¸º ð¸ ={ð1,ð2,ð3}E={e1,e2,e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾æéµ ð(ðº)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºæ¯ä¸¤æ¡è¾¹çéåï¼å¦ {ð1,ð2}{e1,e2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼èå¯¹å¶æéµ ð(ðº)âM(G)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºæ¯åæ¡è¾¹çéåï¼å¦ {ð3}{e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼ð(ðº)âM(G)â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯ä¸¤æ¡è¾¹çéåï¼å³æå°å²éï¼å¦ {ð2,ð3}{e2,e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å ä¸ºç§»é¤å ¶ä¸­çä¸æ¡è¾¹å°±ä¼å°å¾åå²ä¸ºä¸¤ä¸ªè¿éåæ¯ï¼

### å é¤åæ¶ç¼©

**å é¤ï¼Deletionï¼** ï¼

å¯¹äº ð´ âð¸AâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æéµ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å é¤ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¾å°æ°çæéµ ð âð´MâA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ç¬ç«éæ Iâ²Iâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å®ä¹ä¸ºï¼

Iâ²={ð¼âð¸âð´â£ð¼âI}ï¼Iâ²={IâEâAâ£IâI}ï¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥çåºï¼å é¤æä½å°±æ¯ä»æéµä¸­ç§»é¤æäºå ç´ ï¼å¹¶ä¿çå©ä½å ç´ å½¢æçç¬ç«éï¼å ¶ä¿æåç¬ç«éä¸åï¼åªæ¯ç§»é¤äºå ç´ ï¼

**æ¶ç¼©ï¼Contractionï¼** ï¼

å¯¹äº ð´ âð¸AâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æéµ ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ç¼© ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¾å°æéµ ð/ð´M/A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ç¬ç«éæ Iâ³Iâ³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å®ä¹ä¸ºï¼

Iâ³={ð¼âð¸âð´â£âðµâð´,ðµâI,ð(ðµ)=ð(ð´),ð¼âªðµâI}Iâ³={IâEâA|âBâA,BâI,r(B)=r(A),IâªBâI}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¶ç¼©æä½å¯ä»¥çè§£ä¸ºå°éå ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ç¼©çº¦ï¼å¹¶èèå©ä¸çå ç´ ä¸ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºä¸èµ·å½¢æçç¬ç«éï¼æ¶ç¼©çç»æä¾èµäºéå ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåºï¼ç¼©çº¦åçç¬ç«éå®é ä¸æ¯å¯¹åæéµä¸­æ´é«ç§©çå­éè¿è¡çº¦ç®åå¾å°çç¬ç«éï¼

**ç¤ºä¾ - å¾æéµ** ï¼

  * **å é¤** ï¼å¨å¾æéµä¸­ï¼å é¤æä½å³ä»å¾ä¸­å é¤ä¸äºè¾¹ï¼ä¸ä¸ªå¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å é¤ææ¡è¾¹åï¼èèçæ¯å©ä½è¾¹æå½¢æçç¬ç«éï¼å³é£äºä¸å å«ç¯çè¾¹éï¼ä¾å¦ï¼å¦æä»ä¸ä¸ªä¸è§å½¢å¾ä¸­å é¤ä¸æ¡è¾¹ï¼å©ä¸çä¸¤ä¸ªè¾¹ä»ç¶æ¯ä¸ä¸ªæ£®æï¼

  * **æ¶ç¼©** ï¼æ¶ç¼©æä½åæ¯å°ææ¡è¾¹æ¶ç¼©ä¸ºä¸ä¸ªé¡¶ç¹ï¼å¯¹äºå¾æéµï¼æ¶ç¼©ä¸æ¡è¾¹ç¸å½äºå°è¿æ¡è¾¹çä¸¤ä¸ªé¡¶ç¹åå¹¶æä¸ä¸ªé¡¶ç¹ï¼å¹¶å é¤è¯¥è¾¹ï¼åå¹¶é¡¶ç¹åï¼å¾ä¸­çå ¶ä»è¾¹ä»ç¶å¯ä»¥å½¢æç¬ç«éï¼ä¾å¦ï¼å¨ä¸ä¸ªä¸è§å½¢å¾ä¸­ï¼æ¶ç¼©ä»»æä¸æ¡è¾¹å°æä¸¤ä¸ªé¡¶ç¹åå¹¶æä¸ä¸ªï¼å©ä¸çä¸¤æ¡è¾¹å°ææä¸ä¸ªæ°çæéµï¼

## æéµåè´ªå¿

**é®é¢æè¿°** ï¼

æéµçåºç¨ä¹ä¸æ¯è§£å³è´ªå¿ç®æ³ä¸­çæä¼åé®é¢ï¼å ·ä½èè¨ï¼ç»å®ä¸ä¸ªæéµ ð =(ð,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åºç¡éï¼II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬ç«éæï¼å¯¹äºæ¯ä¸ªå ç´ ð¥ âðxâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èµäºä¸ä¸ªæ­£æ´æ°æå¼ ð¤(ð¥)w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç®æ æ¯æ¾å°æå¼æå¤§çç¬ç«éï¼å½¢å¼åä¸ºï¼

maxð´âIð¤(ð´)=maxð´âIâð¥âð´ð¤(ð¥)maxAâIw(A)=maxAâIâxâAw(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¾ç¶ï¼æå¼æå¤§ç¬ç«éå¿ é¡»æ¯æå¤§ç¬ç«éï¼å¦æä¸ä¸ªç¬ç«é ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯æå¤§ç¬ç«éï¼åå­å¨ä¸ä¸ªå¯ä»¥å å ¥ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ç´ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç±äº ð¤(ð¥) >0w(x)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å å ¥è¯¥å ç´ åæå¼ä¼å¢å ï¼è¯´æ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯æå¼æå¤§çç¬ç«éï¼

### æ­¥éª¤

è´ªå¿ç®æ³æ±è§£æå¼æå¤§ç¬ç«éçæ­¥éª¤å¦ä¸ï¼

  1. **å ç´ æåº** ï¼å°åºç¡é ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç §æå¼ä»å¤§å°å°æåºï¼è®°ä¸ºåºå ð1,ð2,â¦,ððe1,e2,â¦,en![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. **åå§å** ï¼è®¾ç¬ç«é ð´ =â A=â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. **æå»ºç¬ç«é** ï¼ä¾æ¬¡èèæåºåçå ç´ ððei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð´ âª{ðð} âIAâª{ei}âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ´æ° ð´ =ð´ âª{ðð}A=Aâª{ei}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. **è¾åºç»æ** ï¼æç»çéå ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸ºæå¼æå¤§çç¬ç«éï¼

**å¤æåº¦åæ** ï¼

è®¾ ð =|ð|n=|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåºç¡éçå¤§å°ï¼ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå¤æ­ä¸ä¸ªéåæ¯å¦ä¸ºç¬ç«éçå¤æåº¦ï¼è´ªå¿ç®æ³çæ¶é´å¤æåº¦ä¸ºï¼

ð(ðlogâ¡ð+ðð(ð))O(nlogâ¡n+nf(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð(ðlogâ¡ð)O(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æåºçå¤æåº¦ï¼ð(ðð(ð))O(nf(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯éä¸å¤æ­ç¬ç«æ§çå¤æåº¦ï¼

å¤æ³¨

  * å¨å¾æéµä¸­ï¼å¯ä»¥ä½¿ç¨ [å¹¶æ¥é](../../ds/dsu/) æ¥é«ææ£æµæ¯å¦å½¢æç¯ï¼ä»èä½¿ ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥è¿å¸¸æ°æ¶é´ï¼
  * å¨çº¿æ§æéµä¸­ï¼ç¬ç«æ§æ£æµéå¸¸æ¶åç©éµè¿ç®ï¼å ¶å¤æåº¦ä¾èµäºå ·ä½å®ç°æ¹å¼ï¼

**æ­£ç¡®æ§è¯æ** ï¼

è®¾ ð =(ð,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªæéµï¼ð´ âIAâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªç¬ç«éï¼ä¸ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æä¸ªæå¼æå¤§ç¬ç«é ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼å®ä¹éå ð ={ð¥ âð âð´ â£ð´ âª{ð¥} âI}P={xâSâAâ£Aâª{x}âI}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ææå å ¥ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼ä»ç¶ä½¿ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¿æç¬ç«æ§çå ç´ æææçéåï¼

è®¾ ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æå¼æå¤§çå ç´ ï¼å ð´â² =ð´ âª{ð¦}Aâ²=Aâª{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯æä¸ªæå¼æå¤§ç¬ç«éçå­éï¼è¯æå¦ä¸ï¼

åè®¾ ð´â² =ð´ âª{ð¦}Aâ²=Aâª{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ä»»ä½æå¼æå¤§ç¬ç«éçå­éï¼åå­å¨ä¸ä¸ªæå¼æå¤§çç¬ç«é ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ |ð´â²| <|ð||Aâ²|<|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±äº |ð´â²| <|ð||Aâ²|<|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®æéµç **æ©å¼ æ§** ï¼å­å¨ ð¥ âð âð´â²xâTâAâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð´â² âª{ð¥} âIAâ²âª{x}âI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å©ç¨ **æ©å¼ æ§** ï¼ä¸æ­å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å ¥ ð´â²Aâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç»æé åºä¸ä¸ªæ°çç¬ç«é ð´â³Aâ³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ |ð´â³| =|ð||Aâ³|=|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è®¾ ð¾ =ð´â³ â©ðK=Aâ³â©T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶æ ð¥ =ð âð¾x=TâK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¦ =ð´â³ âð¾y=Aâ³âK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æå¼æå¤§çå ç´ ï¼æ ð¤(ð¥) â¤ð¤(ð¦)w(x)â¤w(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å æ­¤ï¼ð¤(ð´â³) =ð¤(ð¾) +ð¤(ð¦) â¥ð¤(ð¾) +ð¤(ð¥) =ð¤(ð)w(Aâ³)=w(K)+w(y)â¥w(K)+w(x)=w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼

  * è¥ ð¤(ð´â³) >ð¤(ð)w(Aâ³)>w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ðT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯æå¼æå¤§ç¬ç«éï¼ä¸åè®¾çç¾ï¼
  * è¥ ð¤(ð´â³) =ð¤(ð)w(Aâ³)=w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð´â³Aâ³![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæå¼æå¤§ç¬ç«éï¼ä¸ ð´â²Aâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå ¶å­éï¼ä¸åè®¾ ð´â²Aâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ä»»ä½æå¼æå¤§ç¬ç«éçå­éçç¾ï¼

ç»¼ä¸ï¼åè®¾ä¸æç«ï¼å³ ð´â² =ð´ âª{ð¦}Aâ²=Aâª{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ é¡»æ¯æä¸ªæå¼æå¤§ç¬ç«éçå­éï¼å æ­¤éè¿ä¸æ­ä½¿ç¨è´ªå¿ç­ç¥ï¼æç»å¯ä»¥æ¾å°æå¼æå¤§çç¬ç«éï¼

### ç¤ºä¾

**æå°çææ ** ï¼

ç»å®ä¸ä¸ªè¿éæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯æ¡è¾¹ ð âð¸eâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å ·ææå¼ ð¤(ð)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç®æ ä¸ºæ¾å°ä¸æ£µçææ ï¼ä½¿å ¶å å«ææé¡¶ç¹ä¸æ»æå¼æå°ï¼

**æéµçæå»º** ï¼

ä¸ºäºå°æå°çææ é®é¢å½¢å¼åä¸ºæéµé®é¢ï¼å¯ä»¥æå»ºå¾æéµ ð(ðº)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **åºç¡é** ï¼ð =ð¸S=E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å¾ä¸­çææè¾¹ï¼
  * **ç¬ç«éæ** ï¼II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºææä¸å å«ç¯çè¾¹éï¼å³æææ£®æï¼ï¼

**è´ªå¿ç®æ³** ï¼

å¨å¾æéµçæ¡æ¶ä¸ï¼[Kruskal ç®æ³](../../graph/mst/#kruskal-ç®æ³) æ¯ä¸ä¸ªå ¸åçåºäºæéµçè®ºçè´ªå¿ç®æ³ï¼å¯ä»¥ç¨äºæå»ºæå°çææ ï¼è½ç¶ [Prim ç®æ³](../../graph/mst/#prim-ç®æ³) ä¹æ¯ä¸ç§ææçè´ªå¿ç®æ³ï¼åæ ·è½å¤æ¾å°æå°çææ ï¼ä½å®å¹¶ä¸ä¸¥æ ¼ä¾èµäºæéµçè´ªå¿ï¼å æ­¤ï¼å¨æéµçè®ºçè®¨è®ºä¸­ï¼Kruskal ç®æ³æ¯ä¸»è¦çè´ªå¿ç®æ³å®ä¾ï¼

  * **Kruskal ç®æ³** ï¼

    1. **è¾¹æåº** ï¼å°ææè¾¹ææå¼ä»å°å°å¤§æåºï¼
    2. **éæ­¥éæ©** ï¼ä¾æ¬¡éæ©æå¼æå°çè¾¹ï¼è¥å å ¥åä¸å½¢æç¯ï¼åå°å ¶å å ¥çææ ï¼
    3. **ç»æ­¢æ¡ä»¶** ï¼éå¤ä¸è¿°è¿ç¨ï¼ç´å°çææ å å« |ð| â1|V|â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡è¾¹ï¼
  * **Prim ç®æ³** ï¼

    * **åç** ï¼Prim ç®æ³éè¿ä»ä¸ä¸ªèµ·å§é¡¶ç¹å¼å§ï¼éæ­¥æ©å±çææ ï¼æ¯æ¬¡éæ©è¿æ¥æ å ä¸æ å¤çæå°æå¼è¾¹ï¼
    * è½ç¶ Prim ç®æ³ä¹æ¯è´ªå¿çï¼ä½å ¶éæ©ç­ç¥ä¸åäºå ¶ä»åºäºæéµæ©å¼ æ§è´¨çè´ªå¿ç®æ³ï¼å æ­¤ï¼å¨æéµçè®ºçä¸¥æ ¼æä¹ä¸ï¼Prim ç®æ³ä¸è¢«è§ä¸ºå ¸åçæéµè´ªå¿ç®æ³ï¼

## æéµäº¤

å¯¹äºå®ä¹å¨åä¸åºç¡é ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸¤ä¸ªæéµ ð1 =(ð,I1)M1=(S,I1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2 =(ð,I2)M2=(S,I2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¥ I =I1 â©I2I=I1â©I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³æéµç¬ç«éæçä¸æ¡æ§è´¨ï¼åç§° ð =(ð,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **äº¤** ï¼

**æ³¨æ** ï¼å¹¶éä»»æä¸¤ä¸ªæéµçäº¤é½æ¯ä¸ä¸ªæéµï¼åªæå½å ¶ç¬ç«éæçäº¤éæ»¡è¶³æéµç¬ç«éæå®ä¹ä¸­çä¸æ¡æ§è´¨æ¶ï¼å ¶äº¤æææä¸ä¸ªæéµï¼

### é®é¢æè¿°

  1. **æå¤§ç¬ç«é** ï¼å¨ I1 â©I2I1â©I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ¾å°æå¤§çç¬ç«éï¼å³å ·ææå¤§åºæ°çç¬ç«éï¼ï¼
  2. **å ææå¤§ç¬ç«é** ï¼ç»å®æå¼å½æ° ð¤ :ð ââw:SâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ I1 â©I2I1â©I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ¾å°æå¼åæå¤§çç¬ç«éï¼

### ç®æ³

**æ æçæ¬** ï¼

  1. **åå§å** ï¼éæ©ä¸ä¸ªåå§ç¬ç«é ð¼ âI1 â©I2IâI1â©I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éå¸¸è®¾å® ð¼ =â I=â ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. **è¿­ä»£** ï¼
     * **æå»ºäº¤æ¢å¾** ï¼æ ¹æ®å½åç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå»ºäº¤æ¢å¾ ð·ð1,ð2(ð¼)DM1,M2(I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * **è·¯å¾éæ©** ï¼å¨äº¤æ¢å¾ä¸­ï¼å¯»æ¾ä»æºç¹ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°æ±ç¹ ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¢å¹¿è·¯å¾ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * **å¢å¹¿** ï¼æ²¿è·¯å¾ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä» ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåæ¯ä¸ä¸ªèç¹ï¼
       * å¦æèç¹å±äºå·¦é¨é¡¶ç¹ï¼å³ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼åå°è¯¥å ç´ ä» ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç§»é¤ï¼
       * å¦æèç¹å±äºå³é¨é¡¶ç¹ï¼å³ ð âð¼SâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼åå°è¯¥å ç´ å å ¥ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼
     * **éå¤** ï¼æ´æ°ç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼éå¤ä¸è¿°æ­¥éª¤ï¼ç´å°æ æ³æ¾å°æ°çå¢å¹¿è·¯å¾ä¸ºæ­¢ï¼
  3. **ç»æ** ï¼æç»å¾å°çç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸ºæéµäº¤ ð =ð1 â©ð2M=M1â©M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çä¸ä¸ªæå¤§ç¬ç«éï¼

**å æçæ¬** ï¼

ä¸ºäºæ¾å°æå¼åæå¤§çç¬ç«éï¼ç®æ³éè¦å¨å¢å¹¿è·¯å¾çéæ©ä¸è¿è¡ä¼åï¼

  1. **æå¼è®¾ç½®** ï¼å¯¹äºæ¯ä¸ªå ç´ ð âðeâS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹å ¶å¨äº¤æ¢å¾ä¸­çæå¼ ð¤â²(ð)wâ²(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * **å·¦é¨é¡¶ç¹** ï¼ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼ð¤â²(ð) = âð¤(ð)wâ²(e)=âw(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     * **å³é¨é¡¶ç¹** ï¼ð âð¼SâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼ð¤â²(ð) =ð¤(ð)wâ²(e)=w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. **è·¯å¾éæ©** ï¼å¨äº¤æ¢å¾ ð·ð1,ð2(ð¼)DM1,M2(I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼å¯»æ¾ä¸æ¡ä»æºç¹ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°æ±ç¹ ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **å¢å¹¿è·¯å¾** ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾æ²¿è·¯å¾è¿è¡å¢å¹¿æä½åï¼ç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ»æå¼å¢å æå¤§ï¼
     * **å¢å¹¿æ¡ä»¶** ï¼è·¯å¾ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å å ¥çå ç´ çæå¼æ»åå¤§äºç§»é¤çå ç´ çæå¼æ»åï¼å³ âð¦âå å ¥çå ç´ ð¤(ð¦) >âð¥âç§»é¤çå ç´ ð¤(ð¥)âyâå å ¥çå ç´ w(y)>âxâç§»é¤çå ç´ w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. **å¢å¹¿æä½** ï¼æ²¿è·¯å¾ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä» ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåæ¯ä¸ä¸ªèç¹ï¼
     * å¦æèç¹å±äºå·¦é¨é¡¶ç¹ï¼å³ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼åå°è¯¥å ç´ ä» ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ç§»é¤ï¼
     * å¦æèç¹å±äºå³é¨é¡¶ç¹ï¼å³ ð âð¼SâI![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ç´ ï¼ï¼åå°è¯¥å ç´ å å ¥ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼
  4. **è¿­ä»£** ï¼éå¤æ­¥éª¤ 1 è³ 3ï¼ä¸æ­æå»ºäº¤æ¢å¾å¹¶å¯»æ¾å¢å¹¿è·¯å¾ï¼éæ­¥ä¼åç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ»æå¼ï¼
  5. **ç»æ­¢æ¡ä»¶** ï¼å½æ æ³å¨äº¤æ¢å¾ä¸­æ¾å°æ»¡è¶³å¢å¹¿æ¡ä»¶çè·¯å¾æ¶ï¼ç®æ³ç»æ­¢ï¼
  6. **ç»æ** ï¼æç»å¾å°çç¬ç«é ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸ºæéµäº¤ ð =ð1 â©ð2M=M1â©M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çä¸ä¸ª **æå¼æå¤§ç¬ç«é** ï¼

**å¤æåº¦** ï¼

  * **å¢å¹¿æ¬¡æ°** ï¼è®¾ä¸¤ä¸ªæéµçæå¤§ç§©åå«ä¸º ð1r1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2r2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæå¤§å¢å¹¿æ¬¡æ°ä¸º min(ð1,ð2)min(r1,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * **æ¯æ¬¡å¢å¹¿çå¤æåº¦** ï¼

    * æå»ºäº¤æ¢å¾çå¤æåº¦ä¸º ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð =|ð|n=|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
    * å¯»æ¾å¢å¹¿è·¯å¾çå¤æåº¦åå³äºè·¯å¾æç´¢ç­ç¥ï¼éå¸¸ä¸º ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾å¦ä½¿ç¨å¹¿åº¦ä¼å æç´¢ï¼
  * **æ»æ¶é´å¤æåº¦** ï¼æ»ä½çæ¶é´å¤æåº¦ä¸º ð(ð â ð2)O(râ n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð =min(ð1,ð2)r=min(r1,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## ä¾é¢

**æå°çææ ** ï¼

ç»å®ä¸ä¸ªæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯æ¡è¾¹ ð âð¸eâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æä¸ä¸ªæå¼ ð¤(ð)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯»æ¾ä¸æ£µçææ ï¼ä½¿å ¶å å«ææé¡¶ç¹ä¸æ»æå¼æå°ï¼

  * è¯¦ç»ä»ç»ï¼[æå°çææ ](../../graph/mst/)ï¼
  * é¢ç®æ¨¡æ¿ï¼[æ´è°· P3366ãæ¨¡æ¿ãæå°çææ ](https://www.luogu.com.cn/problem/P3366)ï¼

è§£é¢æè·¯

ä½¿ç¨ Kruskal ç®æ³ï¼å°ææè¾¹ææå¼ä»å°å°å¤§æåºï¼ç¶åéæ­¥éæ©è¾¹ï¼è¥å å ¥åä¸å½¢æç¯ï¼åå°å ¶å å ¥çææ ï¼æç»å¾å°ççææ å³ä¸ºæå°çææ ï¼

**Colorful Graph** ï¼

ç»å®ä¸å¼ å¸¦æå¤ç§é¢è²çæ åå¾ ðº =(ð,ð¸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯æ¡è¾¹æä¸ä¸ªé¢è²å±æ§ï¼å¯»æ¾ä¸ä¸ªæå¤§çè¾¹éï¼ä½¿å¾ï¼

  1. æéè¾¹ä¸å½¢æä»»ä½ç¯ï¼
  2. æ¯ç§é¢è²çè¾¹æ°ä¸è¶ è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºç»å®çæ­£æ´æ°ï¼ï¼

è§£é¢æè·¯

  1. **æéµå»ºæ¨¡** ï¼

     * **å¾æéµ ( ð1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**ï¼å®ä¹ä¸ºææä¸å½¢æç¯çè¾¹éï¼å³ç¬ç«éæ I1I1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«ææä¸ææç¯çè¾¹éåï¼
     * **é¢è²æéµ ( ð2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**ï¼å®ä¹ä¸ºæ¯ç§é¢è²çè¾¹æ°ä¸è¶ è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹éï¼å³ç¬ç«éæ I2I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«æææ»¡è¶³æ¯ç§é¢è²è¾¹æ° â¤ðâ¤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹éåï¼
  2. **æ±è§£æéµäº¤** ï¼éè¿æ±è§£ ð =ð1 â©ð2M=M1â©M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾å°æ¢ä¸å½¢æç¯åæ»¡è¶³æ¯ç§é¢è²è¾¹æ°ä¸è¶ è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§è¾¹éï¼

**çº¦æçèµæºåé é®é¢** :

å¨ä¸ä¸ªèµæºåé é®é¢ä¸­ï¼æä¸ç»èµæº ð  ={ð1,ð2,â¦,ðð}R={r1,r2,â¦,rn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ç»é¡¹ç® ð ={ð1,ð2,â¦,ðð}P={p1,p2,â¦,pm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ªé¡¹ç® ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦åé ä¸å®æ°éçèµæºï¼ä¸æ¯ç§èµæºçæ»åé éä¸è½è¶ è¿å ¶ä¾åºéï¼

**ç®æ ** ï¼å¯»æ¾ä¸ä¸ªèµæºåé æ¹æ¡ï¼ä½¿å ¶æ»¡è¶³ææé¡¹ç®éæ±ä¸ä¸è¶ è¿èµæºä¾åºéï¼

è§£é¢æè·¯

  1. **æéµå»ºæ¨¡** ï¼

     * **éæ±æéµ ( ð1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**ï¼å®ä¹ä¸ºæ»¡è¶³åé¡¹ç®èµæºéæ±çåé æ¹æ¡ï¼å³ç¬ç«éæ I1I1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«æææ»¡è¶³é¡¹ç®éæ±çèµæºåé éåï¼
     * **ä¾åºæéµ ( ð2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**ï¼å®ä¹ä¸ºä¸è¶ è¿æ¯ç§èµæºä¾åºéçåé æ¹æ¡ï¼å³ç¬ç«éæ I2I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«æææ»¡è¶³èµæºä¾åºéå¶çèµæºåé éåï¼
  2. **æ±è§£æéµäº¤** ï¼éè¿æ±è§£ ð =ð1 â©ð2M=M1â©M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾å°æ¢æ»¡è¶³ææé¡¹ç®éæ±åä¸è¶ è¿èµæºä¾åºéçèµæºåé æ¹æ¡ï¼

## åèèµæä¸æ³¨é

  1. [Wikipedia - Matroid](https://en.wikipedia.org/wiki/Matroid)
  2. [ç¾åº¦ç¾ç§ - æéµ](https://baike.baidu.com/item/%E6%8B%9F%E9%98%B5)
  3. [æ´è°· - æéµä¸æä¼åé®é¢](https://www.luogu.com.cn/article/87d02q9f)
  4. [æ´è°· - ä»æéµåºç¡å° Shannon å¼å ³æ¸¸æ](https://www.luogu.com.cn/article/fuj3x886)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/matroid.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/matroid.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [yyyu-star](https://github.com/yyyu-star)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
