# è¿åæ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/continued-fraction/

# è¿åæ°

## å¼å ¥

è¿åæ°å¯ä»¥å°å®æ°è¡¨ç¤ºä¸ºä¸ä¸ªæ¶æçæçæ°æ°åçæéï¼è¿ä¸ªæ°åä¸­çæçæ°æäºè®¡ç®ï¼èä¸æä¾äºè¿ä¸ªå®æ°çæä½³é¼è¿ï¼å èå¨ç®æ³ç«èµä¸­å¸¸å¸¸ä¼ç¨å°è¿åæ°ï¼é¤æ­¤ä¹å¤ï¼è¿åæ°è¿åæ¬§å éå¾ç®æ³å¯åç¸å ³ï¼å èå¯ä»¥åºç¨å°ä¸ç³»åæ°è®ºé®é¢ä¸­ï¼

å ³äºè¿åæ°ç¸å ³çç®æ³å®ç°

æ¬æä¼æä¾ä¸ç³»åçè¿åæ°çç®æ³å®ç°ï¼å ¶ä¸­é¨åç®æ³å¯è½æ æ³ä¿è¯è®¡ç®ä¸­é´è¿ç¨ææ¶åçæ´æ°é½å¨ 32 ä½æ 64 ä½æ´ååéçåå¼èå´å ï¼å¯¹äºè¿ç§æ å½¢ï¼è¯·åèç¸åºç Python çå®ç°ï¼æå° C++ å®ç°ä¸­çæ´ååéæ¿æ¢ä¸º [é«ç²¾åº¦æ´æ°ç±»](../../bignum/)ï¼ä¸ºçªåºéç¹ï¼æ¬æè¡æè¿ç¨ä¸­çé¨åä»£ç å¯è½ä¼è°ç¨åæå®ç°è¿çå½æ°èä¸åéå¤ç»åºå®ç°ï¼

## è¿åæ°

**è¿åæ°** ï¼continued fractionï¼æ¬èº«åªæ¯ä¸ç§å½¢å¼è®°å·ï¼

æéè¿åæ°

å¯¹äºæ°å {ðð}ðð=0{ak}i=0n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿åæ° [ð0,ð1,â¯,ðð][a0,a1,â¯,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå±å¼å¼

ð¥=ð0+1ð1+1ð2+1â¯+1ðð.x=a0+1a1+1a2+1â¯+1an.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿åæ°ææä¹ï¼å½ä¸ä» å½å¯¹åºçå±å¼å¼ææä¹ï¼è¿äº ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºè¿åæ°ç **é¡¹** ï¼termï¼æ **ç³»æ°** ï¼coefficientï¼ï¼

è®°å·

æ´ä¸è¬çè¿åæ°å è®¸å±å¼å¼ä¸­çåå­ä¸æä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¸åºçè¿åæ°è®°å·ä¹éè¦ä¿®æ¹ï¼è¿è¶ åºäºæ¬æçèç´ï¼å¦å¤ï¼æäºæç®ä¸­ä¼å°ç¬¬ä¸ä¸ªéå·ã,,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãåä½åå·ã;;![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãï¼è¿ä¸æ¬æçè®°å·å¨å«ä¹ä¸æ²¡æå·®å¼ï¼

å½ç¶ï¼è¿åæ°è¿å¯ä»¥æ¨å¹¿å°æ ç©·æ°åçæ å½¢ï¼

æ éè¿åæ°

å¯¹äºæ ç©·æ°å {ðð}âð=0{ak}i=0â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿åæ° [ð0,ð1,â¯][a0,a1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºæé

ð¥=limðââð¥ð=limðââ[ð0,ð1,â¯,ðð].x=limkââxk=limkââ[a0,a1,â¯,ak].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿åæ°ææä¹ï¼å½ä¸ä» å½å¯¹åºçæéææä¹ï¼å ¶ä¸­ï¼ð¥ð =[ð0,ð1,â¯,ðð]xk=[a0,a1,â¯,ak]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª **æ¸è¿åæ°** ï¼convergentï¼æ **æ¶æå­** ï¼è ðð =[ðð,ðð+1,â¯]rk=[ak,ak+1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª **ä½é¡¹** æ **å®å ¨å** ï¼complete quotientï¼ï¼ç¸åºå°ï¼é¡¹ ððak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ¶ä¹ç§°ä¸ºç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª **é¨åå** ï¼partial quotientï¼ï¼

### ç®åè¿åæ°

æ°è®ºä¸­ï¼ä¸»è¦èèè¿åæ°çé¡¹é½æ¯æ´æ°çæ å½¢ï¼

ç®åè¿åæ°

å¯¹äºè¿åæ° [ð0,ð1,â¯][a0,a1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð0a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´æ°ï¼ð1,ð2,â¯a1,a2,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ­£æ´æ°ï¼åç§°å®ä¸º **ç®åè¿åæ°** ï¼simple continued fractionï¼ï¼ä¹ç®ç§° **è¿åæ°** ï¼å¦ææ°å {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æéï¼åç§°ä¸º **æéï¼ç®åï¼è¿åæ°** ï¼å¦åç§°ä¸º **æ éï¼ç®åï¼è¿åæ°** ï¼èä¸ï¼ð0a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºå®ç **æ´æ°é¨å** ï¼integer partï¼ï¼

é¤éç¹å«è¯´æï¼æ¬ææå°çè¿åæ°é½æçæ¯ç®åè¿åæ°ï¼å¯ä»¥è¯æï¼æ éçç®åè¿åæ°å¿ ç¶æ¯æ¶æçï¼èä¸ç®åè¿åæ°çä½é¡¹ä¹ä¸å®æ¯æ­£çï¼

è¿åæ°æå¦ä¸åºæ¬æ§è´¨ï¼

æ§è´¨

è®¾å®æ° ð¥ =[ð0,ð1,ð2,â¯]x=[a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æç«å¦ä¸æ§è´¨ï¼

  1. å¯¹äºä»»æ ð âðkâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð¥ +ð =[ð0 +ð,ð1,ð2,â¯]x+k=[a0+k,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å¯¹å®æ° ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð0 >0a0>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å®çåæ° ð¥â1 =[0,ð0,ð1,ð2,â¯]xâ1=[0,a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æéè¿åæ°å¯¹åºçæ¯æçæ°ï¼æ¯ä¸ªæçæ°é½æä¸ä» æä¸¤ç§æ¹å¼å¯ä»¥è¡¨ç¤ºæè¿åæ°ï¼é¿åº¦å¿ ç¶ä¸å¥ä¸å¶ï¼è¿ä¸¤ç§æ¹å¼å¯ä¸çåºå«å¨äºæåä¸é¡¹æ¯å¦ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³

ð¥=[ð0,ð1,â¯,ðð]=[ð0,ð1,â¯,ððâ1,1].x=[a0,a1,â¯,an]=[a0,a1,â¯,anâ1,1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸¤ä¸ªè¿åæ°ç§°ä¸ºæçæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **è¿åæ°è¡¨ç¤º** ï¼continued fraction representationï¼ï¼å ¶ä¸­ï¼æ«é¡¹ä¸ä¸ºä¸çç§°ä¸ºæ åè¡¨ç¤ºï¼æ«é¡¹ä¸ºä¸çç§°ä¸ºéæ åè¡¨ç¤ºï¼1

ä¾å­

æçæ° ð¥ =53x=53![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºä¸º

ð¥=[1,1,1,1]=1+11+11+11,ð¥=[1,1,2]=1+11+12.x=[1,1,1,1]=1+11+11+11,x=[1,1,2]=1+11+12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ éè¿åæ°å¯¹åºçæ¯æ çæ°ï¼èä¸ï¼æ¯ä¸ªæ çæ°ä» æå¯ä¸çæ¹å¼è¡¨ç¤ºä¸ºè¿åæ°ï¼ç§°ä¸ºæ çæ°çè¿åæ°è¡¨ç¤ºï¼

### è¿åæ°è¡¨ç¤ºçæ±æ³

è¦æ±æä¸ªå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºï¼åªéè¦æ³¨æå°å®çä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¦æä¸æ¯æ´æ°ï¼å°±ä¸å®æ»¡è¶³

ðð=[ðð,ðð+1,â¯]=[ðð,ðð+1]=ðð+1ðð+1.rk=[ak,ak+1,â¯]=[ak,rk+1]=ak+1rk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èä¸ï¼ðð+1 >1rk+1>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¯ä»¥ä» ð0 =ð¥r0=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§éå½å°è®¡ç®

ðð=âððâ,Â ðð+1=1ððâðð.ak=ârkâ,Â rk+1=1rkâak.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªè¿ç¨äº§ççæ°å {ðð}{ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯å¯ä¸ç¡®å®çï¼é¤éæä¸ªä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸ºæ´æ°ï¼å¦æåºç°äº ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´æ°ï¼åè¯´æè¿ç¨åºå½ç»æ­¢ï¼å¯ä»¥éæ©è¾åºç¸åºçæ åè¡¨ç¤ºæè éæ åè¡¨ç¤ºï¼

å¨ç®æ³ç«èµä¸­ï¼å¾å¾å¤ççé½æ¯æçæ° ð¥ =ððx=pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼æ¯ä¸ªä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æçæ° ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸å¯¹äº ð >0k>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ðð >1rk>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ»æ ðð >ððpk>qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ·ä½è®¡ç®ä¸è¿°éæ¨å ³ç³»ï¼å¯ä»¥åç°

ðð=âððððâ,Â ðð+1=1ððâðð=ððððâðððð=ððððmodðð.ak=âpkqkâ,Â rk+1=1rkâak=qkpkâakqk=qkpkmodqk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶çè®¡ç®è¿ç¨å®é ä¸æ¯å¯¹ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å [è¾è½¬ç¸é¤æ³](../gcd/#æ¬§å)ï¼è¿ä¹è¯´æï¼å¯¹äºæçæ° ð =ððr=pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿åæ°è¡¨ç¤ºçé¿åº¦æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{p,q})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼è®¡ç®æçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤æåº¦ä¹æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{p,q})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

åèå®ç°

ç»å®åæ°çåå­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååæ¯ ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¾åºè¿åæ°çç³»æ°åºå [ð0,ð1,â¯,ðð][a0,a1,â¯,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // Find the continued fraction representation of P/Q. auto fraction ( int p , int q ) { std :: vector < int > a ; while ( q ) { a . push_back ( p / q ); std :: tie ( p , q ) = std :: make_pair ( q , p % q ); } return a ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # Find the continued fraction representation of P/Q. def fraction ( p , q ): a = [] while q : a . append ( p // q ) p , q = q , p % q return a ```   
---|---  
  
## æ¸è¿åæ°

å¨è¿åæ°çå®ä¹ä¸­ä»ç»äºæ¸è¿åæ°çæ¦å¿µï¼å®æ°çæ¸è¿åæ°å°±æ¯å®çè¿åæ°è¡¨ç¤ºçæ¸è¿åæ°ï¼å¨å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºä¸­ï¼åªä¿çå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¡¹ï¼å¾å°çè¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ç§°ä¸ºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ°ï¼å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æçæ°ï¼èä¸åºå {ð¥ð}{xk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶æäºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¾å­ï¼é»éåå²æ¯çæ¸è¿åæ°

è¿åæ° ð¥ =[1,1,1,1,â¯]x=[1,1,1,1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå ä¸ªæ¸è¿åæ°åå«æ¯

ð¥0=[1]=1,ð¥1=[1,1]=2,ð¥2=[1,1,1]=32,ð¥3=[1,1,1,1]=53,ð¥4=[1,1,1,1,1]=85.x0=[1]=1,x1=[1,1]=2,x2=[1,1,1]=32,x3=[1,1,1,1]=53,x4=[1,1,1,1,1]=85.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥å½çº³å°è¯æ

ð¥ð=ð¹ð+2ð¹ð+1,xk=Fk+2Fk+1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼{ð¹ð}{Fk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ [ææ³¢é£å¥æ°å](../../combinatorics/fibonacci/)ï¼æ ¹æ®å®çéé¡¹å ¬å¼å¯ç¥ï¼

ð¥ð=ðð+2â(âð)â(ð+2)ðð+1â(âð)â(ð+1),xk=Ïk+2â(âÏ)â(k+2)Ïk+1â(âÏ)â(k+1),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ç ð =1+â52Ï=1+52![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é»éåå²æ¯ï¼å½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¶äºæ ç©·æ¶ï¼æ

ð¥=limðââð¥ð=ð.x=limkââxk=Ï.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å èï¼è¿åæ° ð¥ =[1,1,1,1,â¯]x=[1,1,1,1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºçæ¯é»éåå²æ¯ ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿äºæ¸è¿åæ°è¶è¿äºç¸åºçå®æ°ï¼æä»¥å¯ä»¥ç¨äºé¼è¿è¯¥å®æ°ï¼ä¸ºæ­¤ï¼æå¿ è¦äºè§£æ¸è¿åæ°çæ§è´¨ï¼

### éæ¨å ³ç³»

é¦å ï¼è¦è§£å³è¿äºæ¸è¿åæ°çè®¡ç®é®é¢ï¼è½ç¶æ¸è¿åæ°æ»æ¯å¨è¿åæ°çåé¢æ·»å ä¸é¡¹ï¼ä½æ¯å¹¶ä¸éè¦æ¯æ¬¡é½éæ°è®¡ç®å®çå¼ï¼å ¶å®ï¼æ¸è¿åæ°æå¦ä¸éæ¨å ³ç³»ï¼

éæ¨å ¬å¼

å¯¹äºè¿åæ° ð¥ =[ð0,ð1,ð2,â¯]x=[a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å®çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åæåæ° ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ

ðð=ððððâ1+ððâ2,ðð=ððððâ1+ððâ2.pk=akpkâ1+pkâ2,qk=akqkâ1+qkâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éæ¨çèµ·ç¹æ¯ï¼å½¢å¼ï¼åæ°

ð¥â1=ðâ1ðâ1=10,Â ð¥â2=ðâ2ðâ2=01.xâ1=pâ1qâ1=10,Â xâ2=pâ2qâ2=01.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

æ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå­ååæ¯å¯ä»¥çä½ ð0,ð1,â¯,ðða0,a1,â¯,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤å å¤é¡¹å¼ï¼

ðð=ðð(ð0,ð1,â¯,ðð)ðð(ð0,ð1,â¯,ðð).rk=Pk(a0,a1,â¯,ak)Qk(a0,a1,â¯,ak).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®æ¸è¿åæ°çå®ä¹ï¼æ

ðð=ð0+1[ð1,ð2,â¯,ðð]=ð0+ððâ1(ð1,â¯,ðð)ððâ1(ð1,â¯,ðð)=ð0ððâ1(ð1,â¦,ðð)+ððâ1(ð1,â¯,ðð)ððâ1(ð1,â¯,ðð).rk=a0+1[a1,a2,â¯,ak]=a0+Qkâ1(a1,â¯,ak)Pkâ1(a1,â¯,ak)=a0Pkâ1(a1,â¦,ak)+Qkâ1(a1,â¯,ak)Pkâ1(a1,â¯,ak).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä¸å¼æ¯è¾ï¼ä¸å¦¨è®¾ ðð(ð0,â¯,ðð) =ððâ1(ð1,â¯,ðð)Qk(a0,â¯,ak)=Pkâ1(a1,â¯,ak)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¯ä»¥å°æ¸è¿åæ°åä½

ðð=ðð(ð0,ð1,â¯,ðð)ððâ1(ð1,â¯,ðð)rk=Pk(a0,a1,â¯,ak)Pkâ1(a1,â¯,ak)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸å¤é¡¹å¼ ððPk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æéæ¨å ³ç³»

ðð(ð0,â¯,ðð)=ð0ððâ1(ð1,â¯,ðð)+ððâ2(ð2,â¯,ðð).Pk(a0,â¯,ak)=a0Pkâ1(a1,â¯,ak)+Pkâ2(a2,â¯,ak).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º

ð0=ð0,Â ð1=ð0+1ð1=ð0ð1+1ð1,r0=a0,Â r1=a0+1a1=a0a1+1a1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼éæ¨çèµ·ç¹æ¯

ð0(ð0)=ð0,Â ð1(ð0,ð1)=ð0ð1+1.P0(a0)=a0,Â P1(a0,a1)=a0a1+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æè®¾

ðâ1=1,Â ðâ2=0,Pâ1=1,Â Pâ2=0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥éªè¯å¯¹äº ð =0,1k=0,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç«ä¸è¿°éæ¨å ³ç³»ï¼è¿ç¸å½äºè§å®äºå½¢å¼åæ° ðâ1 =10râ1=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðâ2 =01râ2=01![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ»¡è¶³ä¸è¿°éæ¨å ³ç³»çå¤é¡¹å¼å ððPk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º **è¿é¡¹å¼**3ï¼continuantï¼ï¼å®å¯ä»¥åä½è¡åå¼çå½¢å¼ï¼

ðð(ð0,â¯,ðð)=detâ¡ââ â â â â â â â â ââð010â¯0â1ð11â±â®0â1ð2â±0â®â±â±â±10â¯0â1ððââ â â â â â â â â ââ .Pk(a0,â¯,ak)=detâ¡(a010â¯0â1a11â±â®0â1a2â±0â®â±â±â±10â¯0â1ak).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸ä¸ª [ä¸å¯¹è§ç©éµ](https://en.wikipedia.org/wiki/Tridiagonal_matrix) çè¡åå¼ï¼ä»å·¦ä¸è§å¼å§å±å¼ï¼å¯ä»¥éªè¯å®å ·æä¸é¢çéæ¨å ³ç³»ååå¼æ¡ä»¶ï¼åè¿æ¥ï¼ä»å³ä¸è§å¼å§å±å¼ï¼ååè½å¾å°éæ¨å ³ç³»

ðð(ð0,â¯,ðð)=ððððâ1(ð0,â¯,ððâ1)+ððâ2(ð0,â¯,ððâ2),Pk(a0,â¯,ak)=akPkâ1(a0,â¯,akâ1)+Pkâ2(a0,â¯,akâ2),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯æè¦æ±è¯çï¼

è®°å·

æ¬æå°æ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®°ä½ ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ»æ¯é»è®¤åå­ ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç±ä¸é¢çéæ¨å ³ç³»ç»åºï¼ä¸æè¿è¦è¯´æï¼è¿æ ·æ»è½å¾å°æ¸è¿åæ°çæ¢çº¦è¡¨ç¤ºï¼

è¿ä¸ªéæ¨å¼è¯´æ

ð¥ð=ððððâ1+ððâ2ððððâ1+ððâ2xk=akpkâ1+pkâ2akqkâ1+qkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»äº ð¥ðâ1xkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ðâ2xkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼

ä½ä¸ºæ¸è¿åæ°çéæ¨å ³ç³»çæ¨è®ºï¼æç«å¦ä¸çååºå®çååæ°å®çï¼

ååºå®ç

è®¾å®æ° ð¥ =[ð0,ð1,ð2,â¯]x=[a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ°æ¯ ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç¸é»ä¸¤ä¸ªæ¸è¿åæ°çåå­ååæ¯çæ¯å¼åå«ä¸º

ððððâ1=[ðð,ððâ1,â¯,ð1,ð0],ððððâ1=[ðð,ððâ1,â¯,ð1].pkpkâ1=[ak,akâ1,â¯,a1,a0],qkqkâ1=[ak,akâ1,â¯,a1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æ ð0 =0a0=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç¬¬ä¸ä¸ªè¿åæ°åºå½çè§£ä¸ºå¨åæ°ç¬¬äºé¡¹å¤æªæ­ï¼å³ [ðð,ððâ1,â¯,ð2][ak,akâ1,â¯,a2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¨ ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨å ³ç³»ä¸­ï¼å·¦å³ä¸¤ä¾§åå«åé¤ä»¥ ððâ1pkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððâ1qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°

ððððâ1=ðð+ððâ2ððâ1,ððððâ1=ðð+ððâ2ððâ1.pkpkâ1=ak+pkâ2pkâ1,qkqkâ1=ak+qkâ2qkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿­ä»£è¿ä¸¤ä¸ªå¼å­ï¼å°±å¯ä»¥å¾å°ä¸¤ä¸ªè¿åæ°ï¼åä»£å ¥åå§å¼ ð0ðâ1 =ð0p0pâ1=a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1ð0 =ð1q1q0=a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼è³äº ð0 =0a0=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å°å¾å°çè¿åæ°çè§£ä¸ºå½¢å¼è¡¨è¾¾å¼ï¼åå®çä½é¡¹

[ð2,ð1,0]=ð2+1ð1+10=ð2+00ð1+1=ð2.[a2,a1,0]=a2+1a1+10=a2+00a1+1=a2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å èå¯ä»¥ç´æ¥ç¥å»æåä¸¤é¡¹ï¼å¦æéè¦ä¸¥æ ¼çè¯æï¼åªè¦æ³¨æå°è¿ä¸ªå¼å­å¯ä»¥çä½ ð0 â0a0â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæéå³å¯ï¼

åæ°å®ç

å®æ° ð¥ >0x>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°çåæ°æ¯ ð¥â1xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°ï¼

è¯æ

ä¸å¦¨è®¾ ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æè¿åæ°è¡¨ç¤º [ð0,ð1,ð2,â¯][a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¥â1xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºæ¯ [0,ð0,ð1,ð2,â¯][0,a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬çæ¸è¿åæ°å¯ä»¥ä»éæ¨å ³ç³»ä¸­æ±å¾ï¼èä¸ï¼å¯¹äº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æåå¼æ¡ä»¶ ð¥â2 =01xâ2=01![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥â1 =10xâ1=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äº ð¦ =ð¥â1y=xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æåå¼æ¡ä»¶ ð¦â1 =10yâ1=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦0 =01y0=01![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æ ð¥â2 =(ð¦â1)â1xâ2=(yâ1)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥â1 =(ð¦0)â1xâ1=(y0)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®éæ¨å ³ç³»ï¼å¯ä»¥å¾å° ð¥ð =ð¦â1ð+1xk=yk+1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°çåæ°æ¯ ð¦ =ð¥â1y=xâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°ï¼å¯¹äº 0 <ð¥ â¤10<xâ¤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼ä¹å¯ä»¥åç±»ä¼¼è®¨è®ºï¼

å©ç¨æ¬èå¾å°çéæ¨å ³ç³»ï¼å¯ä»¥å¾å°è®¡ç®æ¸è¿åæ°çç®æ³å¦ä¸ï¼

åèå®ç°

ç»å®è¿åæ°çç³»æ° ð0,ð1,â¯,ðða0,a1,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±æ¸è¿åæ°çåå­ååæ¯åºå (ð0,ð0),(ð1,ð1),â¯,(ðð,ðð)(p0,q0),(p1,q1),â¯,(pn,qn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text // Find the convergents of a continued fraction A. // Numerators and denominators stored separately in P and Q. auto convergents ( std :: vector < int > a ) { std :: vector < int > p = { 0 , 1 }; std :: vector < int > q = { 1 , 0 }; for ( auto it : a ) { p . push_back ( p . back () * it \+ p . end ()[ -2 ]); q . push_back ( q . back () * it \+ q . end ()[ -2 ]); } return std :: make_pair ( p , q ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text # Find the convergents of a continued fraction A. # Numerators and denominators stored separately in P and Q. def convergents ( a ): p = [ 0 , 1 ] q = [ 1 , 0 ] for it in a : p . append ( p [ \- 1 ] * it \+ p [ \- 2 ]) q . append ( q [ \- 1 ] * it \+ q [ \- 2 ]) return p , q ```   
---|---  
  
### è¯¯å·®ä¼°è®¡

å©ç¨æ¸è¿åæ°çéæ¨å ¬å¼ï¼å¯ä»¥ä¼°è®¡ç¨æ¸è¿åæ°é¼è¿å®æ°äº§ççè¯¯å·®ï¼

é¦å ï¼å¯ä»¥è®¡ç®ç¸é»çæ¸è¿åæ°çå·®å¼ï¼

æ¸è¿åæ°çå·®å

è®¾ ð¥ð =ððððxk=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ°ï¼é£ä¹ï¼æ

ðð+1ððâðððð+1=(â1)ð.pk+1qkâpkqk+1=(â1)k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ç¸é»ä¸¤é¡¹çæ¸è¿åæ°çå·®åæ¯

ð¥ð+1âð¥ð=(â1)ððð+1ðð.xk+1âxk=(â1)kqk+1qk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

æ ¹æ®éæ¨å ³ç³»ï¼æ

detâ¡(ðð+1ðððð+1ðð)=detâ¡(ðð+1ðð+ððâ1ðððð+1ðð+ððâ1ðð)=detâ¡(ððâ1ððððâ1ðð)=âdetâ¡(ððððâ1ððððâ1)=(â1)ð+2detâ¡(1001)=(â1)ð.detâ¡(pk+1pkqk+1qk)=detâ¡(ak+1pk+pkâ1pkak+1qk+qkâ1qk)=detâ¡(pkâ1pkqkâ1qk)=âdetâ¡(pkpkâ1qkqkâ1)=(â1)k+2detâ¡(1001)=(â1)k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯ ðð+1ðð âðððð+1 =( â1)ðpk+1qkâpkqk+1=(â1)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ä¸¤è¾¹åé¤ä»¥ ðð+1ððqk+1qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°å ³äº ð¥ð+1 âð¥ðxk+1âxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»è®ºï¼

å èï¼å¥æ°é¡¹æ¸è¿åæ°æ»æ¯å¤§äºç¸é»ä¸¤é¡¹ï¼å¶æ°é¡¹æ¸è¿åæ°æ»æ¯å°äºç¸é»ä¸¤é¡¹ï¼æ¸è¿åæ°æ¯äº¤éååçï¼

å¦æåªçå¶æ°é¡¹ï¼å¥æ°é¡¹ï¼æ¸è¿åæ°ï¼åºåä¹æ¯åè°éå¢ï¼éåï¼çï¼è¿æ¯å ä¸º

ð¥ð+2âð¥ð=(â1)ð+1ðð+2ðð+1+(â1)ððð+1ðð=(â1)ð(ðð+2âðð)ðð+2ðð+1ðð=(â1)ððð+2ðð+2ððxk+2âxk=(â1)k+1qk+2qk+1+(â1)kqk+1qk=(â1)k(qk+2âqk)qk+2qk+1qk=(â1)kak+2qk+2qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°ï¼å¥æ°ï¼æ¶ä¸ºæ­£ï¼è´ï¼ï¼åæ¶ï¼å ä¸ºæç«éæ¨å ³ç³» ðð =ððððâ1 +ððâ2qk=akqkâ1+qkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¯ ððqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¢é¿éåº¦ä¸ä¼æ ¢äºææ³¢é£å¥æ°åçéåº¦ï¼æä»¥ï¼ç¸é»ä¸¤é¡¹çå·®ä¸å®è¶è¿äºé¶ï¼è¿å°±è¯´æï¼å¶æ°é¡¹åå¥æ°é¡¹æ¸è¿åæ°åå«èªä¸èä¸åèªä¸èä¸å°é¼è¿åä¸æéï¼è¿å°±è¯æäºæ éç®åè¿åæ°ä¸å®æ¶æï¼æ¸è¿åæ°è¶è¿äºç¸åºå®æ°çå¨æå¯ä»¥è§ä¸å¾ï¼

![](./images/golden-ratio-convergents.svg)

ä¸ï¼ä¸ï¼æ¸è¿åæ°

å¯¹äºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå®çæ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð¥ð >ð¥xk>x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¥ð <ð¥xk<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å°±ç§° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ä¸ï¼ä¸ï¼æ¸è¿åæ°** ï¼upper (lower) convergentï¼ï¼

åé¢å·²ç»è¯´æï¼ä¸æ¸è¿åæ°å°±æ¯å¥æ°é¡¹æ¸è¿åæ°ï¼ä¸æ¸è¿åæ°å°±æ¯å¶æ°é¡¹æ¸è¿åæ°ï¼

å©ç¨å·®åå ¬å¼ï¼å¯ä»¥å°å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæäº¤éçº§æ°çå½¢å¼ï¼

ð¥=ð0+ââð=0(â1)ððð+1ðð.x=a0+âk=0â(â1)kqk+1qk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿åæ°å®ä¹ä¸­çæ¸è¿åæ°åä½é¡¹å°±æ¯è¯¥çº§æ°çé¨åååä½é¡¹ï¼

å©ç¨å·®åå ¬å¼ï¼è¿å¯ä»¥ç´æ¥å¯¹æ¸è¿åæ°é¼è¿å®æ°äº§ççè¯¯å·®ååºä¼°è®¡ï¼

è¯¯å·®

è®¾ ð¥ð =ðððð â ð¥xk=pkqkâ x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ°ï¼é£ä¹ï¼æ

ð¥ðâð¥=(â1)ððð(ðð+1ðð+ððâ1),xkâx=(â1)kqk(rk+1qk+qkâ1),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð+1rk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä½é¡¹ï¼è¿èï¼æ

12ð2ð+1â¤1ðð(ðð+ðð+1)â¤â£ð¥âððððâ£â¤1ðððð+1â¤1ð2ð.12qk+12â¤1qk(qk+qk+1)â¤|xâpkqk|â¤1qkqk+1â¤1qk2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

å ä¸º ð¥ =[ð0,ð1,â¯,ðð,ðð+1]x=[a0,a1,â¯,ak,rk+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸å¯¹å½¢å¼è¿åæ°ä¹æç«æ¸è¿åæ°çå·®åå ¬å¼ï¼æä»¥æ

ð¥âð¥ð=(â1)ððð(ðð+1ðð+ððâ1),xâxk=(â1)kqk(rk+1qk+qkâ1),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð+1ðð +ððâ1rk+1qk+qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯æç §éæ¨å ¬å¼å¾å°çè¿ä¸ªå½¢å¼è¿åæ°çç¬¬ ð +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ°çåæ¯ï¼

è¦å®æéåçä¸ç­å¼ä¼°è®¡ï¼åªéè¦æ³¨æå°å½ ð¥ð â ð¥xkâ x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ»æç«

1â¤ðð+1â¤ðð+1â¤ðð+1+1,1â¤ak+1â¤rk+1â¤ak+1+1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥æ

ðð+1=ðð+1ðð+ððâ1â¤ðð+1ðð+ððâ1â¤ðð+(ðð+1ðð+ððâ1)=ðð+ðð+1.qk+1=ak+1qk+qkâ1â¤rk+1qk+qkâ1â¤qk+(ak+1qk+qkâ1)=qk+qk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼æä¸ç­å¼

1ðð(ðð+ðð+1)â¤â£ð¥âððððâ£=1ðð(ðð+1ðð+ððâ1)â¤1ðððð+1.1qk(qk+qk+1)â¤|xâpkqk|=1qk(rk+1qk+qkâ1)â¤1qkqk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦å¾å°å¤ä¾§çæ¾ç¼©ï¼åæ³¨æå° ðð â¤ðð+1qkâ¤qk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥äºï¼

æ¬èçå·®åå ¬å¼è¿æä¸ä¸ªç®åæ¨è®ºï¼æ¸è¿åæ° ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ¢çº¦çï¼

æ¨è®º

å¯¹äºä»»ä½å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æ¸è¿åæ° ð¥ð =ððððxk=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå­ååæ¯ç±éæ¨å ¬å¼ç»åºï¼å ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¢çº¦åæ°ï¼å³ gcd(ðð,ðð) =1gcd(pk,qk)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¯¹å·®åå ¬å¼åºç¨ [è£´èå®ç](../bezouts/) å³å¯ï¼

å ¶å®ï¼äºå ä¸æ¬¡ä¸å®æ¹ç¨çè§£å¯ä»¥éè¿è¿åæ°çæ¹æ³æ±è§£ï¼

äºå ä¸æ¬¡ä¸å®æ¹ç¨çæ±è§£

ç»å® ð´,ðµ,ð¶ âðA,B,CâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¥æ¾ ð¥,ð¦ âðx,yâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ð´ð¥ +ðµð¦ =ð¶Ax+By=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

è§£ç­

è½ç¶è¿ä¸ªé®é¢éå¸¸æ¯ç¨ [æ©å±æ¬§å éå¾ç®æ³](../bezouts/#ä¸¤ä¸ªåéçæ) è§£å³çï¼ä½æ¯åæ ·å¯ä»¥éè¿è¿åæ°æ±è§£ï¼

è®¾ ð´ðµ =[ð0,ð1,â¯,ðð]AB=[a0,a1,â¯,ak]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸é¢è¯æäº ððððâ1 âððâ1ðð =( â1)ðâ1pkqkâ1âpkâ1qk=(â1)kâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢ä¸º ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å°

ð´ððâ1âðµððâ1=(â1)ðâ1ð,Aqkâ1âBpkâ1=(â1)kâ1g,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð =gcd(ð´,ðµ)g=gcd(A,B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´é¤ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸ç»è§£ä¸º ð¥ =( â1)ðâ1ð¶ðððâ1x=(â1)kâ1Cgqkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦ =( â1)ðð¶ðððâ1y=(â1)kCgpkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åæ è§£ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // Return (x,y) such that Ax+By=C. // Assume that such (x,y) exists. auto dio ( int A , int B , int C ) { std :: vector < int > p , q ; std :: tie ( p , q ) = convergents ( fraction ( A , B )); C /= A / p . back (); int t = p . size () % 2 ? -1 : 1 ; return std :: make_pair ( t * C * q . end ()[ -2 ], \- t * C * p . end ()[ -2 ]); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # Return (x, y) such that Ax+By=C. # Assume that such (x, y) exists. def dio ( A , B , C ): p , q = convergents ( fraction ( A , B )) C //= A // p [ \- 1 ] # divide by gcd(A, B) t = ( \- 1 ) if len ( p ) % 2 else 1 return t * C * q [ \- 2 ], \- t * C * p [ \- 2 ] ```   
---|---  
  
## ä¸¢çªå¾é¼è¿

è¿åæ°çè®ºçä¸ä¸ªéè¦åºç¨å°±æ¯ä¸¢çªå¾é¼è¿çè®ºï¼ä¸¢çªå¾é¼è¿ï¼Diophantine approximationï¼æ¯æç¨æçæ°é¼è¿å®æ°ï¼å½ç¶ï¼ç±äºæçæ°çç¨ å¯æ§ï¼å¦æä¸å ä»¥éå¶ï¼å¯ä»¥å¾å°è¯¯å·®ä»»æå°çé¼è¿ï¼å æ­¤ï¼éè¦å¯¹å¯ä»¥ä½¿ç¨çæçæ°ååºéå¶ï¼æ¯å¦åªè½éæ©åæ¯å°äºæä¸ªå¼çæçæ°ï¼æ¬èå°±è®¨è®ºäºè¿ç§éå¶ä¸çæä½³é¼è¿åè¿åæ°çå ³ç³»ï¼

### ç¨æ¸è¿åæ°é¼è¿å®æ°

é¦å ï¼å©ç¨æ¸è¿åæ°çè¯¯å·®ä¼°è®¡ï¼ç«å»å¾å°å¦ä¸ç»æï¼

å®çï¼Dirichletï¼

å¯¹äºæ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å­å¨æ ç©·å¤ä¸ªæ¢çº¦åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

â£ð¥âððâ£<1ð2|xâpq|<1q2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼

è¯æ

æ ¹æ®æ¸è¿åæ°çè¯¯å·®ä¼°è®¡ï¼å¯¹äºæ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ° ð¥ð =ððððxk=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

â£ð¥âððððâ£â¤1ð2ð.|xâpkqk|â¤1qk2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ£æ¥è¯¯å·®å ¬å¼çè¯æå³å¯ç¥ï¼å¯¹äºä»»ä¸æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç­æ¡ä»¶å¹¶ä¸æç«ï¼å æ­¤ï¼å®çæææ¸è¿åæ°çåå­ååæ¯é½æ»¡è¶³è¦æ±ï¼

è¿ä¸ªå®çä¹å¯ä»¥çä½æ¯ [Dirichlet é¼è¿å®ç](https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem) çæ¨è®ºï¼è¿å ä¹å·²ç»æ¯æå¥½çç»æäºï¼ä¸ç­å¼å³ä¾§åæ¯ä¸­çææ° 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·²ç»ä¸è½åæ¹è¿ï¼ä½æ¯å¸¸æ°ä¸å¯ä»¥åå¾æ´å¥½ï¼Hurwitz å®çè¯´æï¼ä¸ç­å¼å³ä¾§å¯ä»¥ç¼©å°å° 1â5ð215q2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è¿æ¯æå¥½ççï¼

Hurwitz å®ç

å¯¹äºæ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å­å¨æ ç©·å¤ä¸ªæ¢çº¦åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

â£ð¥âððâ£<1â5ð2|xâpq|<15q2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼èä¸ä¸ç­å¼å³ä¾§ç â55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è½æ¢ææ´å¤§çå®æ°ï¼

è¯æï¼Borelï¼

Borel å®é ä¸è¯æäºï¼æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿ç»­ä¸ä¸ªæ¸è¿åæ°ä¸­ï¼å¿ ç¶æè³å°ä¸ä¸ªæ»¡è¶³ä¸è¿°æ¡ä»¶ï¼å ä¸ºæ¸è¿åæ°æ ç©·å¤ï¼ä¸é½æ¯æ¢çº¦åæ°ï¼é£ä¹ Hurwitz å®ççç¬¬ä¸é¨åå°±å¿ ç¶æç«ï¼

åè¯æ³ï¼ä¸å¦¨è®¾å­å¨æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå®çæ¸è¿åæ° ð¥ðâ1,ð¥ð,ð¥ð+1xkâ1,xk,xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾

â£ð¥âððâ1ððâ1â£â¥1â5ð2ðâ1,Â â£ð¥âððððâ£â¥1â5ð2ð,Â â£ð¥âðð+1ðð+1â£â¥1â5ð2ð+1|xâpkâ1qkâ1|â¥15qkâ12,Â |xâpkqk|â¥15qk2,Â |xâpk+1qk+1|â¥15qk+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼å ä¸ºç¸é»çæ¸è¿åæ°å¿ ç¶ä½äº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¾§ï¼æä»¥ç±å·®åå ¬å¼ç¥

1ððâ1ðð=â£ððâ1ððâ1âððððâ£=â£ð¥âððâ1ððâ1â£+â£ð¥âððððâ£â¥1â5ð2ðâ1+1â5ð2ð.1qkâ1qk=|pkâ1qkâ1âpkqk|=|xâpkâ1qkâ1|+|xâpkqk|â¥15qkâ12+15qk2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®å¯ä»¥åæå ³äºå ððððâ1qkqkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç­å¼

ððððâ1+ððâ1ððâ¤â5.qkqkâ1+qkâ1qkâ¤5.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºå·¦ä¾§æ¯æçæ°ï¼å³ä¾§æ¯æ çæ°ï¼ç­å·å¿ ç¶æ æ³åå¾ï¼åå ä¸º ðð â¥ððâ1qkâ¥qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥å¯ä»¥è§£å¾

1â¤ððððâ1<â5+12.1â¤qkqkâ1<5+12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åçï¼å¯ä»¥è¯æ

1â¤ðð+1ðð<â5+12.1â¤qk+1qk<5+12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯æ ¹æ®éæ¨å ¬å¼ï¼å¹¶ç»åä¸¤å¼å¯ç¥ï¼

ðð+1=ðð+1ððâððâ1ðð<â5+12ââ5â12=1ak+1=qk+1qkâqkâ1qk<5+12â5â12=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ç®åè¿åæ°çå®ä¹çç¾ï¼æä»¥ï¼Borel çç»è®ºæç«ï¼

è¦è¯´æè¿æ ·å¾å°ççæ¯æå¥½çï¼åªéè¦æ¾å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾å¯¹äºä»»ä½ ð¶ >â5C>5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½åªå­å¨æéå¤ä¸ªæ¢çº¦åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ä¸ç­å¼

â£ð¥âððâ£<1ð¶ð2|xâpq|<1Cq2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼ä¸é¢è¯æ ð =â5+12Ï=5+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¿æ ·ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼4

è®¾ ðâ² =ââ5+12Ïâ²=â5+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ±è½­æ ¹ï¼å®ä»¬é½æ¯æ¹ç¨ ð¥2 âð¥ â1 =0x2âxâ1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ ¹ï¼å èï¼å¯¹ä»»æå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

ð¥2âð¥â1=(ð¥âð)(ð¥âðâ²).x2âxâ1=(xâÏ)(xâÏâ²).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥æ¢çº¦åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°

1ð2â¤|ð2âððâð2|ð2=â£ððâðâ£â£ððâðâ²â£â¤â£ððâðâ£(â£ððâðâ£+|ðâðâ²|)<1ð¶ð2(1ð¶ð2+â5).1q2â¤|p2âpqâq2|q2=|pqâÏ||pqâÏâ²|â¤|pqâÏ|(|pqâÏ|+|ÏâÏâ²|)<1Cq2(1Cq2+5).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äº ð¶ >â5C>5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥ç´æ¥è§£åº ð <âð¶(ð¶ââ5)q<C(Câ5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èä¸å¯è½å­å¨æ ç©·å¤ç»è§£æ»¡è¶³ä¸è¿°ä¸ç­å¼ï¼

è¿äºå®ççè¯æè¯´æï¼æ¸è¿åæ°æä¾äºç¸å½å¥½çä¸¢çªå¾é¼è¿ï¼ä½æ¯ï¼è¿æªå¿ æ¯æä½³é¼è¿ï¼è¦è®¨è®ºæä½³é¼è¿ï¼éè¦è¯´æé¼è¿ç¨åº¦çåº¦éï¼è¿å¸¸å¸¸æä¸¤ç§éæ©ï¼

å¯è½å­å¨æä½³é¼è¿ç¸å ³ç»è®ºä¸æç«çæ å½¢

æ¥ä¸æ¥çä¸¤èï¼ä¼åè¿°ä¸äºå ³äºæä½³é¼è¿çç»æï¼è¿äºç»æå¯è½å¯¹ä¸ªå«æ è¶£çæ å½¢å¹¶ä¸æç«ï¼æ¯å¦ï¼æä½³é¼è¿çä¸¤ç±»å®ä¹é½è¦æ±ä¸¥æ ¼ä¸ç­å·ï¼ä½æ¯å¯¹äºåå¥æ° ð¥ =ð +12x=n+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð âðnâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çè¿åæ°çå½¢å¼å¯ä»¥æ¯ [ð,1,1][n,1,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼å®çåä¸¤ä¸ªæ¸è¿åæ° ð¥0 =ðx0=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥1 =ð +1x1=n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯é½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·ç¦»æ¯ä¸æ ·çï¼è¿è¯´æï¼å®ä»¬é½ä¸æ¯æä½³é¼è¿ï¼å¯¹äºæ¬èçç»è®ºçåè¿°ï¼è¯»è åºå½é»è®¤è¿æ ·çæ å½¢å·²ç»æé¤å¨å¤ï¼å¦æè¯»è ä¸å ³å¿ææ«å°¾çå ä¸ªæ¸è¿åæ°ï¼æææ¯åªå ³å¿æ çæ°çé¼è¿ï¼é£ä¹ä¸å¿ çä¼è¿äºé¢å¤çå¤ææ å½¢ï¼

### ç¬¬ä¸ç±»æä½³é¼è¿ï¼ä¸­é´åæ°

ç¬¬ä¸ç±»æä½³é¼è¿ä½¿ç¨

â£ð¥âððâ£|xâpq|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¡¡éé¼è¿çç¨åº¦ï¼

ç¬¬ä¸ç±»æä½³é¼è¿

å¯¹äºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå¯¹äºä»»æç ðâ²ðâ² â ððpâ²qâ²â pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 0 <ðâ² â¤ð0<qâ²â¤q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ

â£ð¥âððâ£<â£ð¥âðâ²ðâ²â£,|xâpq|<|xâpâ²qâ²|,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±ç§°æçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ç¬¬ä¸ç±»æä½³é¼è¿** ï¼best approximation of the first kindï¼ï¼

ç¬¬ä¸ç±»æä½³é¼è¿æªå¿ æ¯æ¸è¿åæ°ï¼èæ¯ä¸ç±»æ´å®½æ³çåæ°ï¼

ä¸­é´åæ°

è®¾å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ¸è¿åæ° ð¥ð+1 =[ð0,ð1,â¯,ðð,ðð+1]xk+1=[a0,a1,â¯,ak,ak+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æ´æ° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ 0 â¤ð¡ â¤ðð+10â¤tâ¤ak+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)5ï¼ååæ° ð¥ð,ð¡ =[ð0,ð1,â¯,ðð,ð¡]xk,t=[a0,a1,â¯,ak,t]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ä¸­é´åæ°** ï¼intermediate fractionï¼ã**åæ¶æå­** ï¼semiconvergentï¼æ **æ¬¡æ¸è¿åæ°** ï¼secondary convergentï¼ï¼6

ç±»ä¼¼äºæ¸è¿åæ°çæ å½¢ï¼å¤§äºï¼å°äºï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸­é´åæ°ç§°ä¸º **ä¸ï¼ä¸ï¼ä¸­é´åæ°** ï¼upper (lower) semiconvergentï¼ï¼

æ ¹æ®éæ¨å ¬å¼ï¼ä¸­é´åæ°å¯ä»¥åæ

ð¥ð,ð¡=ð¡ðð+ððâ1ð¡ðð+ððâ1.xk,t=tpk+pkâ1tqk+qkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®å¿ ç¶æ¯æ¢çº¦åæ°ï¼èä¸ä½äºæ¸è¿åæ° ð¥ðâ1xkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ð+1xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼éç ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¢å¤§ï¼å®ä¹éæ¸å ð¥ð+1xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é æ¢ï¼ï¼ä»¥ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°çæ å½¢ä¸ºä¾ï¼

ð¥ðâ1=ð¥ð,0<ð¥ð,1<ð¥ð,2<â¯<ð¥ð,ðð+1=ð¥ð+1.xkâ1=xk,0<xk,1<xk,2<â¯<xk,ak+1=xk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºæ¸è¿åæ°çåå­ååæ¯é½æ¯éå¢çï¼ä¸­é´åæ° ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¡ â 0tâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çåå­ååæ¯è½å¨äº ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ð+1xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼å¦æå°è¿äºåæ°æç §åæ¯å¤§å°æåï¼ä¸­é´åæ°å°±æ¯ä½äºç¸é»çæ¸è¿åæ°ä¸­é´çä¸äºåæ°ï¼

ææçç¬¬ä¸ç±»æä½³é¼è¿é½æ¯ä¸­é´åæ°ï¼ä½æ¯å¹¶ä¸æ¯ææçä¸­é´åæ°é½æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼

å®ç

ææçç¬¬ä¸ç±»æä½³é¼è¿é½æ¯ä¸­é´åæ°ï¼

è¯æ

å ä¸º ð0 â¤ð¥ â¤ð0 +1a0â¤xâ¤a0+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç¬¬ä¸ç±»æä½³é¼è¿å¿ ç¶ä½äº ð¥1,0 =ð0x1,0=a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¥0,1 =ð0 +1x0,1=a0+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼ææä¸­é´åæ°ä»å°å°å¤§å¯ä»¥æåæ

ð¥1,0<ð¥1,1<â¯<ð¥1,ð2=ð¥3,0<â¦<ð¥<â¦<ð¥2,0=ð¥0,ð1<â¯<ð¥0,1.x1,0<x1,1<â¯<x1,a2=x3,0<â¦<x<â¦<x2,0=x0,a1<â¯<x0,1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åé¶çä¸­é´åæ°æ¯è¿ç»­åºç°çï¼èä¸åé¶çä¸­é´åæ°ä¹é´åæ²¡æé´éï¼è¿æå³çï¼ä»»ä½ä½äº ð¥1,0 =ð0x1,0=a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¥0,1 =ð0 +1x0,1=a0+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çæçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶è½å¨ä¸¤ä¸ªåé¶çä¸­é´åæ° ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ð,ð¡+1xk,t+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼ä¸å¦¨è®¾å®ä¸æ¯ä¸­é´åæ°ä¸å°äº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èæ

ð¥ð,ð¡<ðð<ð¥ð,ð¡+1<ð¥.xk,t<pq<xk,t+1<x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼ä¸æ¹é¢æ

â£ð¥ð,ð¡âððâ£â¤|ð¥ð,ð¡âð¥ð,ð¡+1|=1((ð¡+1)ðð+ððâ1)(ð¡ðð+ððâ1).|xk,tâpq|â¤|xk,tâxk,t+1|=1((t+1)qk+qkâ1)(tqk+qkâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦ä¸æ¹é¢æ

â£ð¥ð,ð¡âððâ£=|ð(ð¡ðð+ððâ1)âð((ð¡+1)ðð+ððâ1)|ð(ð¡ðð+ððâ1)â¥1ð(ð¡ðð+ððâ1).|xk,tâpq|=|q(tpk+pkâ1)âp((t+1)qk+qkâ1)|q(tqk+qkâ1)â¥1q(tqk+qkâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼å¿ ç¶æ

ð>(ð¡+1)ðð+ððâ1.q>(t+1)qk+qkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼æçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯ä¸å®å¤§äº ð¥ð,ð¡+1xk,t+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯ï¼ä½æ¯å®å¹¶ä¸æ¯æ´å¥½çé¼è¿ï¼

â£ð¥âððâ£>|ð¥âð¥ð,ð¡+1||xâpq|>|xâxk,t+1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼å®ä¸å¯è½æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼è¿å°±è¯´æï¼ä¸æ¯ä¸­é´åæ°ï¼å°±ä¸æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼äº¦å³ææç¬¬ä¸ç±»æä½³é¼è¿é½æ¯ä¸­é´åæ°ï¼

åè¿æ¥ï¼å¹¶ä¸è½æ­è¨ææçä¸­é´åæ°é½æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼ä½æ¯ï¼çç¡®å¯ä»¥ç»åºä¸­é´åæ°æä¸ºç¬¬ä¸ç±»æä½³é¼è¿çæ¡ä»¶ï¼

å®ç

æææ¸è¿åæ°é½æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼é¤æ­¤ä¹å¤ï¼è®¾ 0 <ð¡ <ðð+10<t<ak+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸­é´åæ° ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼å½ä¸ä» å½ ð¡ >ðð+12t>ak+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè ð¡ =ðð+12t=ak+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð+2 >ððððâ1rk+2>qkqkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

ä¸é¢ä¼è¯æï¼æ¸è¿åæ°é½æ¯ç¬¬äºç±»æä½³é¼è¿ï¼å èå¿ ç¶æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼å ³é®å¨äºé£äºä¸æ¯æ¸è¿åæ°çä¸­é´åæ°ï¼

åæå·²ç»è¯´è¿ï¼ä¸­é´åæ° ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯ä½äº ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ð+1xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼ä¸éç ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¢å éæ¸å¢å¤§ï¼ä½æ¯ ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å´éæ¸æ¥è¿ ð¥ð+1xk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èæ´æ¥è¿ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥ ð¥ð,ð¡ <ð¥xk,t<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¾ï¼å®ä¸ç¸é»çä¸­é´åæ°çç¸å¯¹ä½ç½®å ³ç³»æ»¡è¶³ï¼

ð¥ðâ1<ð¥ð,ð¡<ð¥ð+1<ð¥<ð¥ð.xkâ1<xk,t<xk+1<x<xk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¯å°äº ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸ºç¬¬ä¸ç±»æä½³é¼è¿çå¿ è¦æ¡ä»¶å°±æ¯ï¼å®æ¯ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ¥è¿ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¹æ¯å åæ¡ä»¶ï¼å ä¸ºä½ä¸ºæ¸è¿åæ°ï¼æ²¡ææ¯ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¯æ´å°ä½æ¯è·ç¦»æ´è¿çäºï¼èé£äºæ¯ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¯è¿è¦å¤§çä¸­é´åæ°ï¼å¿ ç¶ä¸ ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¶ï¼ä½æ¯åæ¯æ´å°ï¼å°±å¿ ç¶è·ç¦» ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´è¿ï¼å¯¹äºæ¸è¿åæ°åä¸­é´åæ°çè¯¯å·®ï¼ç»è®¡ç®å¯ç¥

|ð¥ðâð¥|=1ðð(ðð+1ðð+ððâ1),|ð¥ð,ð¡âð¥|=â£ð¡ðð+ððâ1ð¡ðð+ððâ1âðð+1ðð+ððâ1ðð+1ðð+ððâ1â£=ðð+1âð¡(ð¡ðð+ððâ1)(ðð+1ðð+ððâ1).|xkâx|=1qk(rk+1qk+qkâ1),|xk,tâx|=|tpk+pkâ1tqk+qkâ1ârk+1pk+pkâ1rk+1qk+qkâ1|=rk+1ât(tqk+qkâ1)(rk+1qk+qkâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ç¨å°äº ðð+1 â¥ðð+1 >ð¡rk+1â¥ak+1>t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ¥è¿ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¸ºç¬¬ä¸ç±»æä½³é¼è¿ï¼å½ä¸ä» å½

ðð+1âð¡ð¡ðð+ððâ1<1ððâºðð+1<2ð¡+ððâ1ðð.rk+1âttqk+qkâ1<1qkâºrk+1<2t+qkâ1qk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼æä¸ç§å¯è½çæ åµï¼

  1. å¦æ ð¡ <ðð¡+12t<at+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ 2ð¡ <ðð¡+12t<at+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºä¸¤ä¾§é½æ¯æ´æ°ï¼æä»¥ 2ð¡ â¤ðð+1 â12tâ¤ak+1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ è 2ð¡ +ððâ1ðð â¤2ð¡ +1 â¤ðð+1 â¤ðð¡+12t+qkâ1qkâ¤2t+1â¤ak+1â¤rt+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼
  2. å¦æ ð¡ >ðð¡+12t>at+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ 2ð¡ >ðð¡+12t>at+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºä¸¤ä¾§é½æ¯æ´æ°ï¼æä»¥ 2ð¡ â¥ðð¡+1 +1 >ðð¡+12tâ¥at+1+1>rt+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼
  3. å¦æ ðð¡+1at+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¶æ°ï¼è¿æç¬¬ä¸ç§æ åµï¼å³ ð¡ =ðð¡+12t=at+12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è¿°æ¡ä»¶ç­ä»·äº 1ðð+1 =ðð+1 âðð+1 <ððâ1ðð1rk+1=rk+1âak+1<qkâ1qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ðð+2 >ððððâ1rk+2>qkqkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æä»¥ï¼å¦æå°å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææç¬¬ä¸ç±»æä½³é¼è¿æç §åæ¯èªå°å°å¤§çé¡ºåºæåï¼é£ä¹å®ä¼æ ¹æ®ä¸ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°å ³ç³»åæè¥å¹²æ®µï¼æ¯ä¸æ®µæ»æ¯ç±è¥å¹²ä¸ªï¼å¯ä»¥æ¯é¶ä¸ªï¼è¿ç»­çåé¶çä¸­é´åæ°ç»æï¼ä¸æ»ä»¥æ¸è¿åæ°ç»å°¾ï¼æ®µå æ»è½ä¿æå¨å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¾§ï¼æ®µä¸æ®µä¹é´åäº¤éæåå¨ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¾§ï¼

ä¾å­ï¼åå¨ç ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ä¸ç±»æä½³é¼è¿

åå¨ç ð =[3,7,15,1,292,â¯]Ï=[3,7,15,1,292,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èå®åæ¯æå°çå 15 ä¸ªç¬¬ä¸ç±»æä½³é¼è¿æ¯ï¼

ð¥0=31,Â ð¥0,4=134,Â ð¥0,5=165,Â ð¥0,6=196,Â ð¥1=227,ð¥1,8=17957,Â ð¥1,9=20164,Â ð¥1,10=22371,Â ð¥1,11=24578,Â ð¥1,12=26785,ð¥1,13=28992,ð¥1,14=31199,Â ð¥2=333106,Â ð¥3=355113,Â ð¥3,146=5216316604.x0=31,Â x0,4=134,Â x0,5=165,Â x0,6=196,Â x1=227,x1,8=17957,Â x1,9=20164,Â x1,10=22371,Â x1,11=24578,Â x1,12=26785,x1,13=28992,x1,14=31199,Â x2=333106,Â x3=355113,Â x3,146=5216316604.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ç¬¬äºç±»æä½³é¼è¿

ç¬¬äºç±»æä½³é¼è¿ä½¿ç¨ |ðð¥ âð||qxâp|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥è¡¡éé¼è¿çç¨åº¦ï¼

ç¬¬äºç±»æä½³é¼è¿

å¯¹äºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå¯¹äºä»»æç ðâ²ðâ² â ððpâ²qâ²â pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 0 <ðâ² â¤ð0<qâ²â¤q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ

|ðð¥âð|<|ðâ²ð¥âðâ²|,|qxâp|<|qâ²xâpâ²|,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±ç§°æçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **ç¬¬äºç±»æä½³é¼è¿** ï¼best approximation of the second kindï¼ï¼

ç¬¬äºç±»æä½³é¼è¿çæ¡ä»¶ç­ä»·äº

â£ð¥âððâ£<ðâ²ðâ£ð¥âðâ²ðâ²â£.|xâpq|<qâ²q|xâpâ²qâ²|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ðâ² â¤ðqâ²â¤q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç¬¬äºç±»æä½³é¼è¿çæ¡ä»¶æ¯ç¬¬ä¸ç±»æä½³é¼è¿æ´ä¸ºä¸¥èï¼

ç¬¬äºç±»æä½³é¼è¿è½ä¸ä» è½æ¯æ¸è¿åæ°ï¼

å®ç

ææçç¬¬äºç±»æä½³é¼è¿ä¸å®æ¯æ¸è¿åæ°ï¼ææçæ¸è¿åæ°ä¹ä¸å®æ¯ç¬¬äºç±»æä½³é¼è¿ï¼

è¯æ

è¦è¯æç¬¬ä¸é¨åï¼å ä¸ºç¬¬äºç±»æä½³é¼è¿ä¹ä¸å®æ¯ç¬¬ä¸ç±»æä½³é¼è¿ï¼æä»¥åªéè¦è¯æä¸æ¯æ¸è¿åæ°çä¸­é´åæ°ä¸è½æä¸ºç¬¬äºç±»æä½³é¼è¿å°±å¯ä»¥äºï¼ä¸ºæ­¤ï¼è®¾ ð¥ð,ð¡ =ððxk,t=pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸­é´åæ°ä½æ¯ä¸æ¯æ¸è¿åæ°ï¼é£ä¹ï¼è®¾ ð¥ð,ð¡ <ð¥xk,t<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð¥ðâ1<ð¥ð,ð¡<ð¥ð+1<ð¥<ð¥ð.xkâ1<xk,t<xk+1<x<xk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çè¯¯å·®

|ð¥ð,ð¡âð¥|â¥|ð¥ð,ð¡âð¥ð+1|=â£ððâðð+1ðð+1â£=|ððð+1âðð+1ð|ððð+1â¥1ððð+1,|xk,tâx|â¥|xk,tâxk+1|=|pqâpk+1qk+1|=|pqk+1âpk+1q|qqk+1â¥1qqk+1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¹¶å©ç¨æ¸è¿åæ°çè¯¯å·®ä¼°è®¡ï¼æä»¥æ»æ¯æ

|ðð¥ð,ð¡âð|â¥1ðð+1â¥|ððð¥ðâðð|,|qxk,tâp|â¥1qk+1â¥|qkxkâpk|,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³ ð¥ð,ð¡xk,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¼è¿ç¨åº¦ä¸ä¼äºåæ¯æ´å°ç ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¼è¿ç¨åº¦ï¼æä»¥ä¸å¯è½æ¯ç¬¬äºç±»æä½³é¼è¿ï¼

åè¿æ¥ï¼è¦è¯æç¬¬äºé¨åï¼å³æ¯ä¸ªæ¸è¿åæ° ð¥ð =ððððxk=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ç¬¬äºç±»æä½³é¼è¿ï¼è¿å°±æ¯è¦è¯´æï¼å¯¹äºææåæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â¤ððqâ¤qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ |ððð¥ âðð| <|ðð¥ âð||qkxâpk|<|qxâp|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸èèåå¥æ°çæ å½¢ï¼åå¯ä»¥åå® ð >0k>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¦å ï¼æ ¹æ®æ¸è¿åæ°é¼è¿å®æ°çè¯¯å·®ä¼°è®¡ï¼æ

|ððâ1ð¥âððâ1|â¥1ððâ1+ððâ¥1ðð+1â¥|ððð¥âðð|.|qkâ1xâpkâ1|â¥1qkâ1+qkâ¥1qk+1â¥|qkxâpk|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ç­å¼å ¨é¨æç«ç­å·ï¼å½ä¸ä» å½ ðð+1 =1ak+1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯è¿åæ°çæ«é¡¹ï¼ä¸èèè¿æ ·çæ å½¢ï¼é£ä¹ ð¥ðâ1 =ððâ1ððâ1xkâ1=pkâ1qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¥æ ¼å£äº ð¥ð =ððððxk=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»»åä¸åæ° ðð â ð¥ðpqâ xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 0 <ð â¤ðð0<qâ¤qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºæå·®åå ¬å¼ ððððâ1 âððâ1ðð =( â1)ðâ1pkqkâ1âpkâ1qk=(â1)kâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç± Cramer æ³åå¯ç¥ï¼çº¿æ§æ¹ç¨ç»

{ððð+ðððâ1=ð,ððð+ðððâ1=ð{Î»pk+Î¼pkâ1=p,Î»qk+Î¼qkâ1=q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¿ ç¶å­å¨å¯ä¸çæ´æ°è§£ (ð,ð)(Î»,Î¼)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ðð >0Î»Î¼>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ ð >|ð|ðð â¥ððq>|Î»|qkâ¥qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çç¾ï¼å¦åï¼ðð â¤0Î»Î¼â¤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ðÎ»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðÎ¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å·ï¼é£ä¹å ä¸º ððâ1ð¥ âððâ1qkâ1xâpkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððð¥ âððqkxâpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å¼å·ï¼å°±æ ð(ððâ1ð¥ âððâ1)Î»(qkâ1xâpkâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð(ððð¥ âðð)Î¼(qkxâpk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå·ï¼æ è

|ðð¥âð|=|ð||ððð¥âðð|+|ð||ððâ1ð¥âððâ1|>|ððð¥âðð|.|qxâp|=|Î»||qkxâpk|+|Î¼||qkâ1xâpkâ1|>|qkxâpk|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æåçä¸ç­å·æ¯ä¸¥æ ¼çï¼å ä¸º ð¥ðâ1xkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¥æ ¼å£äº ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ ðð â ð¥ðpqâ xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯´æï¼ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬äºç±»æä½³é¼è¿ï¼

è¿ä¸ªæ§è´¨è¡¨æï¼æ¸è¿åæ°ç¡®å®æ¯ç¸å½å¥½çä¸¢çªå¾é¼è¿ï¼

### æ¸è¿åæ°çå¤å®

ç¬¬äºç±»æä½³é¼è¿æä¾äºå¤æ­æä¸ªåæ°æ¯å¦æ¯æ¸è¿åæ°çå åå¿ è¦æ¡ä»¶ï¼è¿è¯´æï¼å¯ä»¥éè¿æ£æ¥æä¸ªåæ°é¼è¿çç¸å¯¹ç¨åº¦æ¥å¤æ­å®æ¯å¦æ¯æ¸è¿åæ°ï¼Legendre å¤å«æ³åæä¾äºæ ¹æ®é¼è¿çç»å¯¹ç¨åº¦æ¥å¤æ­æ¸è¿åæ°çæ¹æ³ï¼Legendre å¤å«æ³çåå§è¡¨è¿°æä¾äºå åå¿ è¦æ¡ä»¶ï¼ä½æ¯å®çå½¢å¼å¹¶ä¸å®ç¨ï¼æ¬èæä¾äº Legendre å¤å«æ³çç®åçæ¬ï¼å¹¶è¯´æå®å¹¶æ²¡ææ¼æå¤ªå¤çæ¸è¿åæ°ï¼

å®çï¼Legendreï¼

å¯¹äºå®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ææ

â£ð¥âððâ£<12ð2|xâpq|<12q2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æ¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°ï¼

è¯æ

è®¾ ð â{ â1,1}Ïµâ{â1,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð â(0,1/2)Î¸â(0,1/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä½¿å¾

ð¥âðð=ððð2xâpq=ÏµÎ¸q2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«çå¸¸æ°ï¼å°æçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å±å¼æè¿åæ° [ð0,ð1,â¯,ðð][a0,a1,â¯,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤å¤ï¼æçæ°æä¸¤ç§è¿åæ°è¡¨ç¤ºï¼å ¶ä¸­ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°å¥½ç¸å·®ä¸ï¼æä»¥å¯ä»¥åè¿åæ°è¡¨ç¤ºä½¿å¾ ( â1)ð =ð(â1)n=Ïµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®°è¿ä¸ªè¿åæ°è¡¨ç¤ºçæ¸è¿åæ°ä¸º ððððpkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å®æ° ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³

ð¥=ððð+ððâ1ððð+ððâ1.x=Ïpn+pnâ1Ïqn+qnâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼å¿ ç¶æ

ððð2=ð¥âðð=ð¥âðððð=ððâ1ððâððððâ1(ððð+ððâ1)ðð=(â1)ð(ððð+ððâ1)ðð.ÏµÎ¸q2=xâpq=xâpnqn=pnâ1qnâpnqnâ1(Ïqn+qnâ1)qn=(â1)n(Ïqn+qnâ1)qn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ èï¼æ

ð=ððððð+ððâ1.Î¸=qnÏqn+qnâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æ

ð=1ðâððâ1ðð>1.Ï=1Î¸âqnâ1qn>1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å° ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å±æè¿åæ° [ð0,ð1,â¯][b0,b1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å

ð¥=ððð+ððâ1ððð+ððâ1=[ð0,ð1,â¯,ðð,ð]=[ð0,ð1,â¯,ðð,ð0,ð1,â¯].x=Ïpn+pnâ1Ïqn+qnâ1=[a0,a1,â¯,an,Ï]=[a0,a1,â¯,an,b0,b1,â¯].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯åæ³çç®åè¿åæ°ï¼æä»¥ ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°ï¼

è¿ä¸ªè¯æå®é è¯´æ ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸ºæ¸è¿åæ°çå åå¿ è¦æ¡ä»¶æ¯ä¸è¿°è¯æä¸­ç ð >1Ï>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ­£æ¯ Legendre å¤å«æ³çåå§å½¢å¼ï¼

è¿ä¸ªå¤å«æ³è¯´æï¼åªè¦é¼è¿çç¨åº¦è¶³å¤å¥½ï¼å°±ä¸å®æ¯æ¸è¿åæ°ï¼ä¸ä¸ä¸ªå®çè¯´æï¼è¿æ ·å¥½çæ¸è¿åæ°è¶³å¤å¤ï¼è³å°æä¸åçæ¸è¿åæ°é½ç¬¦åè¿ä¸ªæ¡ä»¶ï¼

å®çï¼Valhenï¼

å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¸é»ä¸¤ä¸ªæ¸è¿åæ°ä¸­è³å°æä¸ä¸ªæ»¡è¶³

â£ð¥âððâ£<12ð2.|xâpq|<12q2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¯æ

åè®¾ä¸ç¶ï¼å­å¨å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸¤ä¸ªç¸é»çæ¸è¿åæ° ð¥ðâ1xkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³

â£ð¥âððððâ£â¥12ð2ð,Â â£ð¥âðð+1ðð+1â£â¥12ð2ð+1.|xâpkqk|â¥12qk2,Â |xâpk+1qk+1|â¥12qk+12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½äº ð¥ðâ1xkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼æä»¥

12ð2ð+12ð2ð+1â¤â£ð¥âððððâ£+â£ð¥âðð+1ðð+1â£=â£ððððâðð+1ðð+1â£=1ðððð+1.12qk2+12qk+12â¤|xâpkqk|+|xâpk+1qk+1|=|pkqkâpk+1qk+1|=1qkqk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æ ðð =ðð+1qk=qk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èå¿ ç¶æ ð =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð1 =1a1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶åä¸¤ä¸ªæ¸è¿åæ°æ¯ ð¥0 =ð0x0=a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥1 =ð0 +1x1=a0+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èå½é¢çå¯ä¸åä¾æ¯åå¥æ°ï¼æç §åæçè¯´æï¼æ¬æä¸èèè¿ç§æ å½¢ï¼

## å ä½è§£é

è¿åæ°çè®ºæçä¼ç¾çå ä½è§£éï¼

![](./images/continued-convergents-geometry.svg)

å¦å¾æç¤ºï¼å¯¹äºå®æ° ð >0Î¾>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°ç¬¬ä¸è±¡éï¼å æ¬ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ è½´ä¸çç¹ä½ä¸å æ¬åç¹ï¼ä¸åï¼ä¸çæ´ç¹ï¼lattice pointï¼åæä¸ä¸ä¸¤é¨åï¼å¯¹äºæçæ° ðÎ¾![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çç¹æ¢ç®ä½ç´çº¿ä¸æ¹çç¹ï¼åç®ä½ç´çº¿ä¸æ¹çç¹ï¼èèè¿ä¸¤é¨åçç¹çå¸å ï¼é£ä¹ï¼å¥æ°é¡¹æ¸è¿åæ°æ¯ä¸åé¨åçå¸å çé¡¶ç¹ï¼å¶æ°é¡¹æ¸è¿åæ°æ¯ä¸åé¨åçå¸å çé¡¶ç¹ï¼å¸å ä¸ä¸¤ä¸ªç¸é»é¡¶ç¹ä¹é´çè¿çº¿ä¸çæ´ç¹å°±æ¯ä¸­é´åæ°ï¼å¾ä¸­å±ç¤ºäº ð =97Î¾=97![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¸è¿åæ°åä¸­é´åæ°ï¼ç°ç¹ï¼ï¼

åæå ³äºè¿åæ°çå¤§é¨åç»è®ºé½æç¸åºçå ä½è§£éï¼

å ä½è§£é

  * æ¯ä¸ªåæ° ð =ððÎ½=pq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯¹åºçç¬¬ä¸è±¡éå çä¸ä¸ªæ´ç¹ âð =(ð,ð)Î½â=(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ°çå¤§å°å¯¹åºçä¸åç¹è¿çº¿çæçï¼
  * ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹ååéæ¯ âð =(1,ð)Î¾â=(1,Î¾)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨ [åç§¯](../../linear-algebra/product/#äºç»´åéçæ) (ð¥1,ð¦1) Ã(ð¥2,ð¦2) =ð¥1ð¦2 âð¥2ð¦1(x1,y1)Ã(x2,y2)=x1y2âx2y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¦å¿µï¼å¯ä»¥éè¿ âð Ãâð =ð âððÎ¾âÃÎ½â=pâqÎ¾![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£è´å¤æ­ç¹å¨ç´çº¿ä¸æ¹è¿æ¯ä¸æ¹ï¼å èï¼å¨ç´çº¿ä¸æ¹çç¹å°±å¯¹åºçå¤§äºç­äº ðÎ¾![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å¨ç´çº¿ä¸æ¹çç¹å°±å¯¹åºçå°äºç­äº ðÎ¾![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼åç§¯çç»å¯¹å¼ |âð Ãâð||Î¾âÃÎ½â|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­£æ¯äºç¹ âðÎ½â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·ç¦»

|ðâðð¥|â1+ð2,|pâqx|1+Î¾2,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹åºçåæ° ðÎ½![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹å®æ° ðÎ¾![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¼è¿ç¨åº¦ï¼

  * å°æ¸è¿åæ° ðð =ððððÎ¾k=pkqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçç¹è®°ä½ âðð =(ðð,ðð)Î¾âk=(pk,qk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åéæ¨å ¬å¼å°±å¯ä»¥åä½

âðð=ððâððâ1+âððâ2.Î¾âk=akÎ¾âkâ1+Î¾âkâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éå½çèµ·ç¹æ¯ ðâ2 =(1,0)Î¾â2=(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðâ1 =(0,1)Î¾â1=(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å¯¹äºæ´æ° ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ 0 â¤ð¡ â¤ðð0â¤tâ¤ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ç¹

âððâ1,ð¡=ð¡âððâ1+âððâ2Î¾âkâ1,t=tÎ¾âkâ1+Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±è½å¨è¿ç»ç¹ âððâ2Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç¹ âððÎ¾âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ®µä¸ï¼å®ä»¬å¯¹åºçä¸­é´åæ° ððâ1,ð¡Î¾kâ1,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å©ç¨å ä½çæ¹æ³å¯ä»¥æé åºææçæ¸è¿åæ°åä¸­é´åæ°ï¼ä»ç¹ âðâ2 =(1,0)Î¾ââ2=(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç¹ âðâ1 =(0,1)Î¾ââ1=(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼ä¸¤ä¸ªç¹ä½äºç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¾§ï¼è¿æå³ç âð Ãâðâ2Î¾âÃÎ¾ââ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å âð Ãâðâ1Î¾âÃÎ¾ââ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¦å·ç¸åï¼å° âðâ1Î¾ââ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç §åéçå æ³æ·»å å° âðâ2Î¾ââ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼ç´å°æ æ³ç»§ç»­æ·»å èä¸ç©¿è¿ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­¢ï¼å°ç»æè®°ä½ âð0Î¾â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ä»ä¸ âðâ1Î¾ââ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åä¾§ï¼åå° âð0Î¾â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ·»å å° âðâ1Î¾ââ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼ç´å°æ æ³ç»§ç»­æ·»å èä¸ç©¿è¿ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­¢ï¼å°ç»æè®°ä½ âð1Î¾â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ä»ä¸ âð0Î¾â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åä¾§ï¼è¿ä¸ªè¿ç¨å¯ä»¥ä¸ç´æç»­å°æ ç©·ï¼é¤éå¨æéæ­¥å æä¸ª âððÎ¾ân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ°å¥½è½å¨ç´çº¿ ð¦ =ðð¥y=Î¾x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼åè æå³çåé âðÎ¾â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ âððÎ¾ân![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ±çº¿ï¼å³ ð =ððððÎ¾=pnqn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæçç¹ï¼è¿ä¸ªè¿ç¨å°±å¯ä»¥å¾å°åé¢ç¤ºæå¾ä¸­çå¾å½¢ï¼Boris Delaunay å°è¿ä¸ªè¿ç¨å½¢è±¡å°ç§°ä¸ºé¼»å­æä¼¸ç®æ³ï¼nose-streching algorithmï¼9ï¼

  * å¦æéè¦å¿«éè®¡ç®æ¯ä¸æ­¥å° âððâ1Î¾âkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ·»å å° âððâ2Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦çæ¬¡æ°ï¼å¯ä»¥åå©åç§¯ï¼å ä¸º âð Ãâððâ1Î¾âÃÎ¾âkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ âð Ãâððâ2Î¾âÃÎ¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¬¦å·ç¸åï¼æä»¥å¦æè®° âððâ1,ð¡ =ð¡âððâ1 +âððâ2Î¾âkâ1,t=tÎ¾âkâ1+Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå âððâ2Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ·»å ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ âððâ1Î¾âkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°çç»æï¼å âð Ãâððâ1,ð¡ =ð¡(âð Ãâððâ1) +(âð Ãâððâ2)Î¾âÃÎ¾âkâ1,t=t(Î¾âÃÎ¾âkâ1)+(Î¾âÃÎ¾âkâ2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¹åç¬¦å·ï¼å°±æå³çæ²¡æç©¿è¿ç´çº¿ï¼å¨ä¸åå·ä¹åï¼âð Ãâððâ1,ð¡Î¾âÃÎ¾âkâ1,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»å¯¹å¼ä¼éæ¸ä¸éï¼è®°

ðð=â£âðÃâððâ2âðÃâððâ1â£=ââðÃâððâ2âðÃâððâ1.rk=|Î¾âÃÎ¾âkâ2Î¾âÃÎ¾âkâ1|=âÎ¾âÃÎ¾âkâ2Î¾âÃÎ¾âkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼æå¤§å¯ä»¥ä¸éçæ¬¡æ°å°±æ¯

ðð=âððâ=ââ£ððâ1ðâððâ1ððâ2ðâððâ2â£â.ak=ârkâ=â|qkâ1Î¾âpkâ1qkâ2Î¾âpkâ2|â.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯è¿åæ°å±å¼çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ï¼èä¸ï¼ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¿åæ°å±å¼çä½é¡¹ï¼å®æ»¡è¶³å ³ç³»å¼ï¼

ðð=âððâ1ðâððâ1ððâ2ðâððâ2âºð=ððâ1ðð+ððâ2ððâ1ðð+ððâ2.rk=âqkâ1Î¾âpkâ1qkâ2Î¾âpkâ2âºÎ¾=pkâ1rk+pkâ2qkâ1rk+qkâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯è¿åæ°å ³ç³»å¼ ð =[ð0,ð1,â¯,ððâ1,ðð]Î¾=[a0,a1,â¯,akâ1,rk]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å ä¸ºæ¯æ¬¡æ·»å åéé æç âð Ãâððâ1,ð¡Î¾âÃÎ¾âkâ1,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååçæ­¥é¿é½æ¯ |âð Ãâððâ1||Î¾âÃÎ¾âkâ1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æåå©ä½çè·ç¦» |âð Ãâðð||Î¾âÃÎ¾âk|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶ä¸¥æ ¼å°äº |âð Ãâððâ1||Î¾âÃÎ¾âkâ1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æï¼æ¸è¿åæ°çé¼è¿ç¨åº¦ï¼ç± |ðð¥ âð||qxâp|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¡éï¼æ¯éç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¢å ä¸¥æ ¼æ´ä¼çï¼

  * å©ç¨åç§¯çè¿ç®æ³åï¼æ

âððÃâðð+1=âððÃ(ðð+1âðð+âððâ1)=âððÃâððâ1=ââððâ1Ãâðð.Î¾âkÃÎ¾âk+1=Î¾âkÃ(ak+1Î¾âk+Î¾âkâ1)=Î¾âkÃÎ¾âkâ1=âÎ¾âkâ1ÃÎ¾âk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½çº³å¯ç¥

âððÃâðð+1=(â1)ð+2âððâ2Ãâððâ1=(â1)ð.Î¾âkÃÎ¾âk+1=(â1)k+2Î¾âkâ2ÃÎ¾âkâ1=(â1)k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯æ¸è¿åæ°çå·®åå ¬å¼ ðð+1ðð âðððð+1 =( â1)ðpk+1qkâpkqk+1=(â1)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * ä¸ä¸ä¸¤ä¸ªå¸å ä¹é´çé¢ç§¯å¯ä»¥ååæè¥å¹²ä¸ªï¼å¯è½æ¯æ ç©·å¤ä¸ªï¼ä¸è§å½¢ï¼å ¶ä¸­æ¯ä¸ªä¸è§å½¢çé¡¶ç¹åå«æ¯ âððâ2Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãâððÎ¾âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â00â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·çä¸è§å½¢çé¢ç§¯æ¯

12|âððâ2Ãâðð|=12|âððâ2Ã(ððâððâ1+âððâ2)|=ðð2|âððâ2Ãâððâ1|=ðð2.12|Î¾âkâ2ÃÎ¾âk|=12|Î¾âkâ2Ã(akÎ¾âkâ1+Î¾âkâ2)|=ak2|Î¾âkâ2ÃÎ¾âkâ1|=ak2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ® [Pick å®ç](../../../geometry/pick/)ï¼è¿æå³çå¦æè®¾ ð¼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«ä¸ºä¸è§å½¢å é¨åè¾¹çä¸çæ´ç¹ä¸ªæ°ï¼å

ð¼+ðµ2â1=ðð2.I+B2â1=ak2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå·²ç¥ä¸è§å½¢è¾¹çä¸å·²ç»æäº {â0} âª{âððâ1,ð¡ :0 â¤ð¡ â¤ðð}{0â}âª{Î¾âkâ1,t:0â¤tâ¤ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å ±è®¡ ðð +2ak+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ´ç¹ï¼è¿è¯´æï¼å°±ä¸å®æ ð¼ =0I=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðµ =ðð +2B=ak+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èï¼ä¸è§å½¢çè¾¹ä¸æ²¡ææ´å¤çæ´ç¹ï¼ä¸è§å½¢å é¨ä¹æ²¡ææ´ç¹ï¼ä¹å°±æ¯è¯´ï¼ððqk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¢çº¦çï¼ä¸­é´åæ°æ¯è¿ç» âððâ2Î¾âkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å âððÎ¾âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹ä¸çå ¨é¨æ´ç¹ï¼ä¸ç¬¬ä¸è±¡éçæææ´ç¹é½å¨ä¸ä¸ä¸¤ä¸ªå¸å å ï¼

è¿æ ·å¾å°çä¸ä¸ä¸¤ä¸ªå¸å ç§°ä¸º Klein å¤è¾¹å½¢ï¼å¨é«ç»´ç©ºé´å ä¹å¯ä»¥åç±»ä¼¼å®ä¹ï¼å¾å° [Klein å¤é¢ä½](https://en.wikipedia.org/wiki/Klein_polyhedron)ï¼Klein polyhedronï¼ï¼å®å¯ä»¥å°è¿åæ°çæ¦å¿µæ¨å¹¿å°é«ç»´ç©ºé´å ï¼

## è¿åæ°çæ 

ä¸»æ¡ç®ï¼[SternâBrocot æ ä¸ Farey åºå](../stern-brocot/)

SternâBrocot æ æ¯å­å¨äºææä½äº [0,â][0,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çåæ°ç [äºåæç´¢æ ](../../../ds/bst/)ï¼æéè¿åæ°å®é ä¸ç¼ç äº SternâBrocot æ ä¸ä»æ ¹å°æä¸ªåæ°æå¨ä½ç½®çè·¯å¾ï¼ä¹å°±æ¯è¯´ï¼æçæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤º [ð0,ð1,â¯,ððâ1,1][a0,a1,â¯,anâ1,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³çä»æ æ ¹ 1111![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼éè¦å åå³å­èç¹ç§»å¨ ð0a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼ååå·¦å­èç¹ç§»å¨ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ï¼äº¤æ¿æ¹åç§»å¨ï¼ç´å°åæä¸ªæ¹åç§»å¨äº ððâ1anâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡ä¸ºæ­¢ï¼åºå½æ³¨æï¼æ­¤å¤åªè½ä½¿ç¨æ«å°¾ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºï¼

å°è¿åæ°è¡¨ç¤ºçè§£ä¸º SternâBrocot æ ä¸çè·¯å¾ï¼å¯ä»¥å¾å°æ¯è¾è¿åæ°å¤§å°çç®æ³ï¼

è¿åæ°å¤§å°æ¯è¾

ç»å®è¿åæ° ð¼ =[ð¼0,ð¼1,â¯,ð¼ð]Î±=[Î±0,Î±1,â¯,Î±n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð½ =[ð½0,ð½1,â¯,ð½ð]Î²=[Î²0,Î²1,â¯,Î²m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯è¾ä¸¤è å¤§å°ï¼

è§£ç­

é¦å å°ä¸¤ä¸ªè¿åæ°è¡¨ç¤ºé½è½¬åææ«å°¾æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼ä¸å¦¨è®¾é¢ç®æç»çå·²ç»æ¯è¿æ ·å½¢å¼çè¿åæ°ï¼å³ ð¼ð =ð½ð =1Î±n=Î²m=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºå¶æ°ä½ç½®ï¼ä¸æ ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼æ¯åå³ç§»å¨çæ­¥æ°ï¼å¥æ°ä½ç½®æ¯åå·¦ç§»å¨çæ­¥æ°ï¼æä»¥ï¼ð¼ <ð½Î±<Î²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½ä¸ä» å½æç § [å­å ¸åº](../../../string/basic/#å­å) æ¯è¾æ¶ï¼æ

(ð¼0,âð¼1,ð¼2,â¯,(â1)ðâ1ð¼ðâ1,0,â¯)<(ð½0,âð½1,ð½2,â¯,(â1)ðâ1ð½ðâ1,0,â¯).(Î±0,âÎ±1,Î±2,â¯,(â1)nâ1Î±nâ1,0,â¯)<(Î²0,âÎ²1,Î²2,â¯,(â1)mâ1Î²mâ1,0,â¯).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¸è¾äºè¿åæ°è¡¨ç¤ºï¼äº¤æ¿å°æ·»å æ­£è´å·ï¼å å»æ«å°¾ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸é¿åº¦ä¸è¶³çä½ç½®ç¨ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¥é½ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text // Expand [..., n] to [..., n-1, 1] if needed. void expand ( std :: vector < int >& a ) { if ( a . size () == 1 || a . back () > 1 ) { \-- a . back (); a . push_back ( 1 ); } } // Check if a is smaller than b. bool less_than ( std :: vector < int > a , std :: vector < int > b ) { expand ( a ); expand ( b ); for ( int i = 0 ; i < a . size () \- 1 || i < b . size () \- 1 ; ++ i ) { int d = ( i < a . size () \- 1 ? a [ i ] : 0 ) \- ( i < b . size () \- 1 ? b [ i ] : 0 ); if ( i & 1 ) d = \- d ; if ( d < 0 ) { return true ; } else if ( d > 0 ) { return false ; } } return false ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text # Expand [..., n] to [..., n-1, 1] if needed. def expand ( a ): if a [ \- 1 ] != 1 or len ( a ) == 1 : a [ \- 1 ] -= 1 a . append ( 1 ) return a # Check if a is smaller than b. def less_than ( a , b ): a = expand ( a ) b = expand ( b ) a = [( \- 1 ) ** i * a [ i ] for i in range ( len ( a ))] b = [( \- 1 ) ** i * b [ i ] for i in range ( len ( b ))] return a < b ```   
---|---  
  
æä½³å ç¹

å¯¹äº 01 â¤ð0ð0 <ð1ð1 â¤1001â¤p0q0<p1q1â¤10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±ä½¿å¾ ð0ð0 <ðð <ð1ð1p0q0<pq<p1q1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ä¸ (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çæçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

å ä¸º SternâBrocot æ æ¢æ¯ [0,â][0,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çåæ°çäºåæç´¢æ ï¼åæ¯äºå ç» (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [ç¬å¡å°æ ](../../../ds/cartesian-tree/)ï¼æä»¥é¢æå ä¹å¯ä»¥è½¬åä¸ºæ± SternâBrocot æ ä¸ä¸¤ä¸ªç¹ç LCAï¼æè¿å ¬å ±ç¥å ï¼ï¼ä½æ¯ï¼LCA åªè½å¤çé­åºé´å çæ å½¢ï¼LCA å¯è½æ¯ç«¯ç¹æ¬èº«ï¼ä¸ºäºé¿å é¢å¤çè®¨è®ºï¼å¯ä»¥é¦å æé åº ð0ð0 +ðp0q0+Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1ð1 âðp1q1âÎµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¡ç® LCAï¼å¨å·²ç»éè¿è¿åæ°è®¡ç®åºæ ¹å°èç¹çè·¯å¾çæ åµä¸ï¼LCA åªè¦åæé¿çå ¬å ±è·¯å¾å³å¯ï¼

è¦æé åº ð¥ Â±ðxÂ±Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªéè¦å¨èç¹ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤é¦å åå³ï¼å·¦ï¼ç§»å¨ä¸æ¬¡ï¼ååå·¦ï¼å³ï¼ç§»å¨ ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å³å¯ï¼è½¬åæè¿åæ°çè¯­è¨ï¼å¯¹äºåæ° ð¥ =[ð0,ð1,â¯,ððâ1,1]x=[a0,a1,â¯,anâ1,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥ç¥é ð¥ Â±ðxÂ±Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶æ¯ [ð0,ð1,â¯,ððâ1 +1,â][a0,a1,â¯,anâ1+1,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å [ð0,ð1,â¯,ððâ1,1,â][a0,a1,â¯,anâ1,1,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èåªéè¦æ¯è¾è¿ä¸¤ä¸ªè¿åæ°ï¼å°è¾å¤§ï¼å°ï¼çå®ä¹ä¸º ð¥ Â±ðxÂ±Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text // Get X +- EPSILON. auto pm_eps ( std :: vector < int > a ) { constexpr int inf = 0x3f3f3f3f ; // Deal with empty continued fraction for 1/0. if ( a . empty ()) { a . emplace_back ( inf ); } auto b = a ; expand ( b ); a . emplace_back ( inf ); b . emplace_back ( inf ); return less_than ( a , b ) ? std :: make_pair ( a , b ) : std :: make_pair ( b , a ); } // Find the lexicographically smallest (q, p) // such that p0/q0 < p/q < p1/q1. auto middle ( int p0 , int q0 , int p1 , int q1 ) { auto a0 = pm_eps ( fraction ( p0 , q0 )). second ; auto a1 = pm_eps ( fraction ( p1 , q1 )). first ; std :: vector < int > a ; for ( int i = 0 ; i < a0 . size () || i < a1 . size (); ++ i ) { if ( a0 [ i ] == a1 [ i ]) { a . emplace_back ( a0 [ i ]); } else { a . emplace_back ( std :: min ( a0 [ i ], a1 [ i ]) \+ 1 ); break ; } } auto pq = convergents ( a ); return std :: make_pair ( pq . first . back (), pq . second . back ()); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text # Get X +- EPSILON. def pm_eps ( a ): # Deal with empty continued fraction for 1/0. if not a : a . append ( float ( "inf" )) b = expand ( a . copy ()) a . append ( float ( "inf" )) b . append ( float ( "inf" )) return ( a , b ) if less_than ( a , b ) else ( b , a ) # Find the lexicographically smallest (q, p) # such that p0/q0 < p/q < p1/q1. def middle ( p0 , q0 , p1 , q1 ): a0 = pm_eps ( fraction ( p0 , q0 ))[ 1 ] a1 = pm_eps ( fraction ( p1 , q1 ))[ 0 ] a = [] for i in range ( min ( len ( a0 ), len ( a1 ))): if a0 [ i ] == a1 [ i ]: a . append ( a0 [ i ]) else : a . append ( int ( min ( a0 [ i ], a1 [ i ])) \+ 1 ) break p , q = convergents ( a ) return p [ \- 1 ], q [ \- 1 ] ```   
---|---  
  
[GCJ 2019, Round 2 - New Elements: Part 2](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_2/new_elements_part_2/statement.pdf)

ç»å® ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ­£æ´æ°å¯¹ (ð¶ð,ð½ð)(Ci,Ji)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±æ­£æ´æ°å¯¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ {ð¶ðð¥ +ð½ðð¦}{Cix+Jiy}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¥æ ¼éå¢ï¼å¨ææç¬¦åè¦æ±çæ°å¯¹ä¸­ï¼è¾åºå­å ¸åºæå°çä¸å¯¹ï¼

è§£ç­

ä¸å¦¨è®¾ ð´ð =ð¶ð âð¶ðâ1Ai=CiâCiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðµð =ð½ð âð½ðâ1Bi=JiâJiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é®é¢è½¬åä¸ºæ± (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ææ ð´ðð¥ +ðµðð¦Aix+Biy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ´æ°ï¼è¿äºæ°å¯¹å¯ä»¥åä¸ºåç§æ å½¢ï¼

  1. ð´ð,ðµð >0Ai,Bi>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢å¯ä»¥å¿½ç¥ï¼å ä¸ºå·²ç»åè®¾ (ð¥,ð¦) >0(x,y)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. ð´ð,ðµð â¤0Ai,Biâ¤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ç´æ¥è¾åºãIMPOSSIBLEãï¼
  3. ð´ð >0,ðµð â¤0Ai>0,Biâ¤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ç¸å½äºçº¦æ ð¦ð¥ <ð´ðâðµðyx<AiâBi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. ð´ð â¤0,ðµð >0Aiâ¤0,Bi>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ç¸å½äºçº¦æ ð¦ð¥ >âð´ððµðyx>âAiBi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å æ­¤ï¼å ð0ð0p0q0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬åç§æ å½¢ä¸­æå¤§ç âð´ððµðâAiBi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå ð1ð1p1q1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¬¬ä¸ç§æ å½¢ä¸­æå°ç ð´ðâðµðAiâBi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åé®é¢å°±åæäºæ¾å°å­å ¸åºæå°ç (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð0ð0 <ðð <ð1ð1p0q0<pq<p1q1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text void solve () { int n ; std :: cin >> n ; std :: vector < int > C ( n ), J ( n ); // p0/q0 < y/x < p1/q1 int p0 = 0 , q0 = 1 , p1 = 1 , q1 = 0 ; bool fail = false ; for ( int i = 0 ; i < n ; ++ i ) { std :: cin >> C [ i ] >> J [ i ]; if ( i ) { int A = C [ i ] \- C [ i \- 1 ]; int B = J [ i ] \- J [ i \- 1 ]; if ( A <= 0 && B <= 0 ) { fail = true ; break ; } else if ( B > 0 && A < 0 ) { // y/x > (-A)/B if B > 0 if (( \- A ) * q0 > p0 * B ) { p0 = \- A ; q0 = B ; } } else if ( B < 0 && A > 0 ) { // y/x < A/(-B) if B < 0 if ( A * q1 < p1 * ( \- B )) { p1 = A ; q1 = \- B ; } } } } if ( fail || p0 * q1 >= p1 * q0 ) { printf ( "IMPOSSIBLE \n " ); } else { auto pq = middle ( p0 , q0 , p1 , q1 ); printf ( "%d %d \n " , pq . first , pq . second ); } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text def solve (): n = int ( input ()) C = [ 0 ] * n J = [ 0 ] * n # p0/q0 < y/x < p1/q1 p0 , q0 = 0 , 1 p1 , q1 = 1 , 0 fail = False for i in range ( n ): C [ i ], J [ i ] = map ( int , input () . split ()) if i > 0 : A = C [ i ] \- C [ i \- 1 ] B = J [ i ] \- J [ i \- 1 ] if A <= 0 and B <= 0 : fail = True break elif B > 0 and A < 0 : # y/x > (-A)/B if B > 0 if ( \- A ) * q0 > p0 * B : p0 , q0 = \- A , B elif B < 0 and A > 0 : # y/x < A/(-B) if B < 0 if A * q1 < p1 * ( \- B ): p1 , q1 = A , \- B if fail or p0 * q1 >= p1 * q0 : return "IMPOSSIBLE" p , q = middle ( p0 , q0 , p1 , q1 ) return str ( p ) \+ " " \+ str ( q ) ```   
---|---  
  
æ³è¦äºè§£æ´å¤ SternâBrocot æ çæ§è´¨ååºç¨ï¼å¯ä»¥åèå ¶ä¸»æ¡ç®é¡µé¢ï¼

## åå¼çº¿æ§åæ¢

åè¿åæ°ç¸å ³çå¦ä¸ä¸ªéè¦æ¦å¿µæ¯æè°çåå¼çº¿æ§åæ¢ï¼

åå¼çº¿æ§åæ¢

**åå¼çº¿æ§åæ¢** ï¼fractional linear transformationï¼æ¯æå½æ° ð¿ :ð âðL:RâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾

ð¿(ð¥)=ðð¥+ððð¥+ð,L(x)=ax+bcx+d,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð,ð,ð,ð âða,b,c,dâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð âðð â 0adâbcâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å ³äºæ¡ä»¶ ðð âðð â 0adâbcâ 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®¹æéªè¯ï¼å½ ðð âðð =0adâbc=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å½æ°å¯è½æ²¡æå®ä¹æè æ¯å¸¸å½æ°ï¼

åå¼çº¿æ§åæ¢æå¦ä¸æ§è´¨ï¼

åå¼çº¿æ§åæ¢çæ§è´¨

è®¾ ð¿1,ð¿2,ð¿3L1,L2,L3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åå¼çº¿æ§åæ¢ï¼å¹¶è®° ð¿ðLi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°å½¢æçç©éµä¸º

ðð=(ðððððððð)Mi=(aibicidi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå®ä»¬æå¦ä¸æ§è´¨ï¼7

  1. åå¼çº¿æ§åæ¢çå¤å ð¿1 âð¿2L1âL2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åéåæ¢ ð¿â11L1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»ç¶æ¯åå¼çº¿æ§åæ¢ï¼å³å ¨ä½åå¼çº¿æ§åæ¢ææ [ç¾¤](../../algebra/basic/#ç¾¤)ï¼
  2. åå¼çº¿æ§åæ¢å¨ç³»æ°åä¹ä»¥éé¶å¸¸æ°åä¿æä¸åï¼å³å¯¹äºä»»æ ð â 0Î»â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð2 =ðð1M2=Î»M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¿2 =ð¿1L2=L1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. åå¼çº¿æ§åæ¢çå¤åçç³»æ°ç©éµï¼å¯¹åºçç³»æ°ç©éµçä¹ç§¯ï¼å³å¦æ ð1ð2 =ð3M1M2=M3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¿1 âð¿2 =ð¿3L1âL2=L3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. åå¼çº¿æ§åæ¢çéåæ¢çç³»æ°ç©éµï¼å¯¹åºçç³»æ°ç©éµçéç©éµï¼å³å¦æ ðâ11 =ð2M1â1=M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¿â11 =ð¿2L1â1=L2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

æ­¤å¤ä» æä¾åå¼çº¿æ§åæ¢çå¤ååéåæ¢çå½¢å¼ï¼å¾å°è¿ä¸ªå½¢å¼åï¼æææ§è´¨é½æ¯å®¹æéªè¯çï¼

åå¼çº¿æ§åæ¢ ð¿1L1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿2L2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤åï¼

ð¿1âð¿2=ð1ð2ð¥+ð2ð2ð¥+ð2+ð1ð1ð2ð¥+ð2ð2ð¥+ð2+ð1=(ð1ð2+ð1ð2)ð¥+(ð1ð2+ð1ð2)(ð1ð2+ð1ð2)ð¥+(ð1ð2+ð1ð2).L1âL2=a1a2x+b2c2x+d2+b1c1a2x+b2c2x+d2+d1=(a1a2+b1c2)x+(a1b2+b1d2)(c1a2+d1c2)x+(c1b2+d1d2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¼çº¿æ§åæ¢ ð¿1(ð¥)L1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåæ¢ï¼

ð¦=ð¿1(ð¥)=ð1ð¥+ð1ð1ð¥+ð1âºð¥=ð¿â11(ð¦)=ð1ð¦âð1âð1ð¦+ð1.y=L1(x)=a1x+b1c1x+d1âºx=L1â1(y)=d1yâb1âc1y+a1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æéè¿åæ° [ð0,ð1,â¯,ðð][a0,a1,â¯,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥çåæ¯ä¸ç³»ååå¼çº¿æ§åæ¢å¤åçç»æï¼è®¾

ð¿ð(ð¥)=ððð¥+1ð¥=[ðð,ð¥].Li(x)=aix+1x=[ai,x].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼æéè¿åæ°

[ð0,ð1,â¯,ðð]=ð¿0âð¿1ââ¯ð¿ð(â).[a0,a1,â¯,an]=L0âL1ââ¯Ln(â).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼åå¼çº¿æ§åæ¢ ð¿(ð¥) =ðð¥+ððð¥+ðL(x)=ax+bcx+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¢å¨ ð¥ =âx=â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çåå¼æ¯ ððac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ¯å½æ°å¨ ð¥ â Â±âxâÂ±â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çæéå¼ï¼

å¯¹äºä¸è¬çè¿åæ°ï¼è®¾å®æ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½é¡¹ä¸º ðð+1rk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð¥ =[ð0,â¯,ðð,ðð+1]x=[a0,â¯,ak,rk+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ

ð¥=ð¿0âð¿1ââ¯ð¿ð(ðð+1)=ðððð+1+ððâ1ðððð+1+ððâ1.x=L0âL1ââ¯Lk(rk+1)=pkrk+1+pkâ1qkrk+1+qkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿åæ¶ä¹ç»åºäºåå¼çº¿æ§åæ¢ ð¿0 âð¿1 ââ¯ âð¿ðL0âL1ââ¯âLk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼

å½ç¶ä¹å¯ä»¥ç´æ¥éªè¯è¿ä¸ªè¡¨è¾¾å¼ï¼æå¼å§çæ¶åæ¯

ð¥=ð¥+00ð¥+1=ðâ1ð¥+ðâ2ðâ1ð¥+ðâ2.x=x+00x+1=pâ1x+pâ2qâ1x+qâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éåï¼å¦æ ð¿0 âð¿1 ââ¯ âð¿ðâ1L0âL1ââ¯âLkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ·æ

ððâ1ð¥+ððâ2ððâ1ð¥+ððâ2pkâ1x+pkâ2qkâ1x+qkâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½¢å¼ï¼é£ä¹æ ¹æ®åå¼çº¿æ§åæ¢çå¤åå ¬å¼ï¼æ

ð¿0âð¿1ââ¯âð¿ðâ1âð¿ð=(ððâ1ðð+ððâ2)ð¥+ððâ1(ððâ1ðð+ððâ2)ð¥+ððâ1=ððð¥+ððâ1ððð¥+ððâ1.L0âL1ââ¯âLkâ1âLk=(pkâ1ak+pkâ2)x+pkâ1(qkâ1ak+qkâ2)x+qkâ1=pkx+pkâ1qkx+qkâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±å¯ä»¥å½çº³å°å¾å°äºä¸è¿°å½¢å¼ï¼åå¼çº¿æ§åæ¢ä¹æä¾äºéæ¨å ¬å¼ååå¼æ¡ä»¶çå¦ä¸ä¸ªè§åº¦ççè§£ï¼

[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)

ç»å®æ­£æ´æ°æ°ç» ð1,â¯,ðða1,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æ¥è¯¢ï¼æ¯æ¬¡æ¥è¯¢ç»å® ð â¤ðlâ¤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è¦æ±è®¡ç® [ðð,â¯,ðð][al,â¯,ar]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è§£ç­

å°è¿åæ°çè§£ä¸ºä¸ååå¼çº¿æ§åæ¢çå¤åå¨ ð¥ =âx=â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤åå¼çç»æï¼åªéè¦è½å¤å¤æ¬¡æ¥è¯¢ä¸æ®µåå¼çº¿æ§åæ¢çå¤åå³å¯ï¼å ä¸ºæ¯ä¸ªåå¼çº¿æ§åæ¢é½å¯ä»¥åéï¼æä»¥å¯ä»¥é¢å¤çåç¼ååç¨å·®åçæ¹æ³æ¥è¯¢ï¼å¤æåº¦ä¸º ð(ð +ð)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼å¦æéè¦ä¿®æ¹ï¼ä¹å¯ä»¥ç¨çº¿æ®µæ ç­ç»æå­å¨ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` |  ```text #include <algorithm> #include <iostream> #include <tuple> #include <vector> constexpr int M = 1e9 \+ 7 ; // FLTs. Essentially 2x2 matrix. struct FracLinearTrans { int mat [ 4 ]; FracLinearTrans () : mat {} {} FracLinearTrans ( int x ) : mat { x , 1 , 1 , 0 } {} FracLinearTrans ( int a , int b , int c , int d ) : mat { a , b , c , d } {} FracLinearTrans operator * ( const FracLinearTrans & rhs ) const { return FracLinearTrans ( (( long long ) mat [ 0 ] * rhs . mat [ 0 ] \+ ( long long ) mat [ 1 ] * rhs . mat [ 2 ]) % M , (( long long ) mat [ 0 ] * rhs . mat [ 1 ] \+ ( long long ) mat [ 1 ] * rhs . mat [ 3 ]) % M , (( long long ) mat [ 2 ] * rhs . mat [ 0 ] \+ ( long long ) mat [ 3 ] * rhs . mat [ 2 ]) % M , (( long long ) mat [ 2 ] * rhs . mat [ 1 ] \+ ( long long ) mat [ 3 ] * rhs . mat [ 3 ]) % M ); } FracLinearTrans inv () const { return FracLinearTrans ( mat [ 3 ], M \- mat [ 1 ], M \- mat [ 2 ], mat [ 0 ]); } }; int main () { int n , q ; std :: cin >> n >> q ; // Get prefix sum of FLTs. std :: vector < FracLinearTrans > ps ( 1 , { 1 , 0 , 0 , 1 }); ps . reserve ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) { int a ; std :: cin >> a ; ps [ i ] = ps [ i \- 1 ] * FracLinearTrans ( a ); } // Query. for (; q ; \-- q ) { int l , r ; std :: cin >> l >> r ; // Difference. auto res = ps [ l \- 1 ]. inv () * ps [ r ]; int u = res . mat [ 0 ], d = res . mat [ 2 ]; // Correct signs. if ( ! ( l & 1 )) { if ( u ) u = M \- u ; if ( d ) d = M \- d ; } printf ( "%d %d \n " , u , d ); } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` |  ```text # PYTHON IS TOO SLOW TO PASS THIS PROBLEM. # JUST FOR REFERENCE. M = 10 ** 9 \+ 7 def mul ( a , b ): return ( ( a [ 0 ] * b [ 0 ] \+ a [ 1 ] * b [ 2 ]) % M , ( a [ 0 ] * b [ 1 ] \+ a [ 1 ] * b [ 3 ]) % M , ( a [ 2 ] * b [ 0 ] \+ a [ 3 ] * b [ 2 ]) % M , ( a [ 2 ] * b [ 1 ] \+ a [ 3 ] * b [ 3 ]) % M , ) def inv ( a ): return ( a [ 3 ], M \- a [ 1 ], M \- a [ 2 ], a [ 0 ]) n , q = map ( int , input () . split ()) ps = [( 1 , 0 , 0 , 1 )] # Get presum. for a in map ( int , input () . split ()): ps . append ( mul ( ps [ \- 1 ], ( a , 1 , 1 , 0 ))) for _ in range ( q ): l , r = map ( int , input () . split ()) res = mul ( inv ( ps [ l \- 1 ]), ps [ r ]) u , d = res [ 0 ], res [ 2 ] if l % 2 == 0 : if u : u = M \- u if d : d = M \- d print ( u , d ) ```   
---|---  
  
### è¿åæ°çååè¿ç®

å©ç¨åå¼çº¿æ§åæ¢ï¼å¯ä»¥å®æè¿åæ°çååè¿ç®ï¼è¿ä¸ªç®æ³ææ©ç± Gosper æåºï¼

ç®æ³çåºç³æ¯è®¡ç®è¿åæ°çåå¼çº¿æ§åæ¢ï¼æ¬èä»¥æéè¿åæ°ä¸ºä¾ï¼ä½æ¯å ä¸ºç®æ³æ¯è¾åºä¸ä½ï¼åªéè¦è¯»å ¥æéå¤ä¸ªè¿åæ°çé¡¹ï¼æä»¥å¯¹äºæ éè¿åæ°ä¹æ¯éç¨çï¼èä¸å¯ä»¥ç®å°ä»»æç²¾åº¦ï¼ç»ååæçè¿åæ°æ¯è¾ç®æ³ï¼å¯ä»¥ç²¾ç¡®å°æ¯è¾ä»»æç²¾åº¦çå®æ°å·®å¼ï¼

è¿åæ°çåå¼çº¿æ§åæ¢

ç»å®åå¼çº¿æ§åæ¢ ð¿(ð¥) =ðð¥+ððð¥+ðL(x)=ax+bcx+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè¿åæ° ð¼ =[ð¼0,ð¼1,â¯,ð¼ð]Î±=[Î±0,Î±1,â¯,Î±n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ð½ =ð¿(ð¼)Î²=L(Î±)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤º [ð½0,ð½1,â¯,ð½ð][Î²0,Î²1,â¯,Î²m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

ç®æ³çåºæ¬æè·¯å°±æ¯éä¸ªç¡®å® ð½ðÎ²i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼è®°

ð¿ð¾(ð¥)=ð¾+1ð¥=ð¾ð¥+1ð¥.LÎ³(x)=Î³+1x=Î³x+1x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºè¿åæ°

ð¿(ð¼)=ð¿âð¿ð¼0âð¿ð¼1ââ¯âð¿ð¼ð(â),L(Î±)=LâLÎ±0âLÎ±1ââ¯âLÎ±n(â),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å¯ä»¥å ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿éæ­¥å¤å ð¿ð¼ðLÎ±k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹å¼è®¡ç® ð¿(ð¼)L(Î±)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°ï¼ä½æ¯ï¼å¦ææ¯å¸æå¾å° ð¿(ð¼)L(Î±)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºï¼é£ä¹å¹¶ä¸éè¦å®å ¨è®¡ç® ð¿(ð¼)L(Î±)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼åæ±åºè¿åæ°è¡¨ç¤ºï¼å¯ä»¥å¨å¤å ð¿ð¼ðLÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿ç¨ä¸­å°±è½å¤æ­ ð½0,ð½1,â¯Î²0,Î²1,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

æ¯å¦ï¼åè®¾å½åè®¡ç®å°

ð¿âð¿ð¼0âð¿ð¼1ââ¯âð¿ð¼ð(ð¥)=ððð¥+ððððð¥+ððLâLÎ±0âLÎ±1ââ¯âLÎ±k(x)=akx+bkckx+dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ ðð,ððck,dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå·ï¼é£ä¹ï¼ð¿ âð¿ð¼0 âð¿ð¼1 ââ¯ âð¿ð¼ð(ð¥)LâLÎ±0âLÎ±1ââ¯âLÎ±k(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ [0,â][0,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åè°ï¼ä¸å¿ ç¶åå¼å¨ ððððakck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððððbkdk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼æä»¥ï¼å¦æ

âððððâ=âððððâ,âakckâ=âbkdkâ,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°±å¯ä»¥ç¡®å®å®å°±æ¯ ð¿ âð¿ð¼0 âð¿ð¼1 ââ¯ âð¿ð¼ð(ð¥)LâLÎ±0âLÎ±1ââ¯âLÎ±k(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°é¨å ð½0Î²0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼å¨å·¦ä¾§å¤å ð¿â1ð½0LÎ²0â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥å¾å°

ð¿â1ð½0âð¿âð¿ð¼0âð¿ð¼1ââ¯âð¿ð¼ð.LÎ²0â1âLâLÎ±0âLÎ±1ââ¯âLÎ±k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶ï¼ç»§ç»­æ·»å ð¿ð¼ð+1,ð¿ð¼ð+2,â¯LÎ±k+1,LÎ±k+2,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥ç¡®å®æ°çæ´æ°é¨åï¼å³ ð½1Î²1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·è®¡ç®ä¸å»ï¼ç´å°ç¡®å®åºææç ð½ðÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

ç®æ³è¦æ± ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå·ï¼æ¯å ä¸ºè¦ä¿è¯å½æ°çä¸è¿ç»­ç¹ä¸å¨ [0,â][0,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èå´å ï¼è¿æ»æ¯å¯è½çï¼å ä¸ºç®åè¿åæ°çå®ä¹è¦æ±ï¼é¤äº ð¼0Î±0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çï¼ç³»æ°é½æ¯æ­£æ´æ°ï¼ç±æ­¤å¯ä»¥è¯æï¼å¿ ç¶å¨æéæ­¥å æç« ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå·ï¼ä¸å°å¨ä¹åä¸ç´ä¿æåå·ï¼

å ·ä½å®ç°æ¶ï¼åªéè¦ç»´æ¤å½åçåå¼çº¿æ§åæ¢çç³»æ°ç©éµ (ðððð)(abcd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶æ£æ¥ ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦åå·ä»¥å ððac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððbd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦æç¸åçæ´æ°é¨åï¼å³å¤å ð¿ð¼ðLÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å°±å¯ä»¥å¾å° (ðð¼ð+ðððð¼ð+ðð)(aÎ±i+bacÎ±i+dc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æä¸¤è æ´æ°é¨åç¸åä¸º ð½ðÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¨ç»æçè¿åæ°å æ·»å ð½ðÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸å·¦å¤å ð¿â1ð½ðLÎ²jâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ç¸å½äºè®¡ç® (ðððmodððmodð)(cdamodcbmodd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿åæ°çåå¼çº¿æ§åæ¢å·²ç»å¯ä»¥ç¨äºè®¡ç®åæ°åè¿åæ°çååè¿ç®é®é¢ï¼

ððÂ±ð¥=Â±ðð¥+ð0ð¥+ð,Â ððð¥=ðð¥+00ð¥+ð,Â ðð/ð¥=0ð¥+ððð¥+0.pqÂ±x=Â±qx+p0x+q,Â pqx=px+00x+q,Â pq/x=0x+pqx+0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºä¸è¬çè¿åæ°ä¹é´çååè¿ç®ï¼éè¦ç¨å°ååå¼çº¿æ§åæ¢ï¼

ð¥+ð¦=0ð¥ð¦+ð¥+ð¦+00ð¥ð¦+0ð¥+0ð¦+1,Â ð¥ð¦=1ð¥ð¦+0ð¥+0ð¦+00ð¥ð¦+0ð¥+0ð¦+1,Â ð¥ð¦=0ð¥ð¦+ð¥+0ð¦+00ð¥ð¦+0ð¥+ð¦+0.x+y=0xy+x+y+00xy+0x+0y+1,Â xy=1xy+0x+0y+00xy+0x+0y+1,Â xy=0xy+x+0y+00xy+0x+y+0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è¿åæ°çååå¼çº¿æ§åæ¢

ç»å®ååå¼çº¿æ§åæ¢ ð¿(ð¥,ð¦) =ðð¥ð¦+ðð¥+ðð¦+ððð¥ð¦+ðð¥+ðð¦+âL(x,y)=axy+bx+cy+dexy+fx+gy+h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè¿åæ° ð¼ =[ð¼0,ð¼1,â¯,ð¼ð]Î±=[Î±0,Î±1,â¯,Î±n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð½ =[ð½0,ð½1,â¯,ð½ð]Î²=[Î²0,Î²1,â¯,Î²m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ð¾ =ð¿(ð¼,ð½)Î³=L(Î±,Î²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤º [ð¾0,ð¾1,â¯,ð¾â][Î³0,Î³1,â¯,Î³â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

ä¸ååéçåå¼çº¿æ§åæ¢çæ å½¢ç±»ä¼¼ï¼è¦ç¡®å®æ´æ°é¨ååªéè¦ä¿è¯å½åçåå¼çº¿æ§åæ¢å¨ (ð¥,ð¦) â[0,â] Ã[0,â](x,y)â[0,â]Ã[0,â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å çæ´æ°é¨åä¿æä¸åï¼å³ ð,ð,ð,âe,f,g,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå·ï¼ä¸

âððâ=âððâ=âððâ=âðââ.âaeâ=âbfâ=âcgâ=âdhâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³å¤åè¦æ¿æ¢æè®¡ç® ð¿(ð¥,ð¦) â¦ð¿(ð¿ð¼ð(ð¥),ð¦)L(x,y)â¦L(LÎ±i(x),y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿(ð¥,ð¦) â¦ð¿(ð¥,ð¿ð½ð(ð¦))L(x,y)â¦L(x,LÎ²j(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿åæ ·è¡¨ç¤ºæç³»æ°ççº¿æ§åæ¢ï¼å·¦å¤åååååéçæ å½¢å®å ¨ä¸è´ï¼åªéè¦è®¡ç®åæ¨¡å°±å¯ä»¥äºï¼

ç¸è¾äºååéçæ å½¢ï¼ååéçæ å½¢éè¦å³å®è¦å å¤å ð¿ð¼ðLÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ¯ ð¿ð½ðLÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºå¤åçé¡ºåºä¸æåçç»ææ å ³ï¼æä»¥å¯ä»¥èªç±éæ©å¤åé¡ºåºï¼æ¯å¦äº¤æ¿å°å¤å ð¿ð¼ðLÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿ð½ðLÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æè éç¨ç»éªæ³åï¼ä¼å å¤åæ¯å¼å·®è·æ´å¤§çç»´åº¦ï¼å¦æ â£ððâðââ£ >â£ððâðââ£|bfâdh|>|cgâdh|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å°±å å¤å ð¿ð¼ðLÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼å°±å å¤å ð¿ð½ðLÎ²j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å¾ªç¯è¿åæ°

ç±»ä¼¼äºå¾ªç¯å°æ°çæ¦å¿µï¼å¦æè¿åæ°çç³»æ°å½¢æäºå¾ªç¯ï¼å°±ç§°ä¸ºå¾ªç¯è¿åæ°ï¼

å¾ªç¯è¿åæ°

è®¾è¿åæ° ð¥ =[ð0,ð1,ð2,â¯]x=[a0,a1,a2,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å­å¨èªç¶æ° ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ­£æ´æ° ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾å¯¹äºä»»ä½ ð â¥ð¾kâ¥K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðð =ðð+ð¿ak=ak+L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç§°è¿åæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º **å¾ªç¯è¿åæ°** ï¼periodic continued fractionï¼ï¼æ»¡è¶³è¿ä¸ªæ¡ä»¶çæå°ç ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºå®çæå°æ­£å¨æï¼èå¨è¿åæ°ä¸­éå¤åºç°ç ðð,â¯,ðð+ð¿â1ak,â¯,ak+Lâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåå°±ç§°ä¸ºå®çå¾ªç¯èï¼å©ç¨å¾ªç¯èï¼å¾ªç¯è¿åæ°å¯ä»¥åä½ ð¥ =[ð0,â¯,ððâ1,âââââââðð,â¯,ðð+ð¿â1]x=[a0,â¯,akâ1,ak,â¯,ak+Lâ1â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð¾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åä½ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð¥ =[ââââââð0,â¯,ðð¿â1]x=[a0,â¯,aLâ1â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç§°å®ä¸º **çº¯å¾ªç¯è¿åæ°** ï¼purely periodic continued fractionï¼ï¼å¦åç§°å®ä¸º **æ··å¾ªç¯è¿åæ°** ï¼eventually periodic continued fractionï¼ï¼

### äºæ¬¡æ çæ°

ä¸å¾ªç¯è¿åæ°å¯åç¸å ³çæ¦å¿µæ¯ [ï¼å®ï¼äºæ¬¡æ çæ°](../quadratic/)ï¼quadratic irrationalï¼ï¼å³æ´ç³»æ°äºæ¬¡æ¹ç¨çæ çæ°è§£ï¼ææçäºæ¬¡æ çæ°é½å¯ä»¥è¡¨ç¤ºæ

ð+ðâð·a+bD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½¢å¼ï¼å ¶ä¸­ï¼ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æçæ°ä¸ ð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ å¹³æ¹å å­çæ­£æ´æ°ï¼æ¬ææå°çäºæ¬¡æ çæ°é½é»è®¤æ¯å®æ°ï¼èä¸ï¼ð +ðâð·a+bD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ±è½­æ¯æ ð âðâð·aâbD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

Euler çç»æè¯´æï¼ææå¾ªç¯è¿åæ°é½æ¯äºæ¬¡æ çæ°ï¼

å®çï¼Eulerï¼

å¾ªç¯è¿åæ°è¡¨ç¤ºçé½æ¯äºæ¬¡æ çæ°ï¼

è¯æ

å¯¹äºä¸è¬çå¾ªç¯è¿åæ° ð¥ =[ð0,â¯,ððâ1,âââââââðð,â¯,ðð+ð¿â1]x=[a0,â¯,akâ1,ak,â¯,ak+Lâ1â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è®¾ ð¦ =[âââââââðð,â¯,ðð+ð¿â1]y=[ak,â¯,ak+Lâ1â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å

ð¥=[ð0,â¯,ððâ1,ð¦]=ð¿0(ð¦),ð¦=[ðð,â¯,ðð+ð¿â1,ð¦]=ð¿1(ð¦),x=[a0,â¯,akâ1,y]=L0(y),y=[ak,â¯,ak+Lâ1,y]=L1(y),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð¿0( â )L0(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¿1( â )L1(â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯åå¼çº¿æ§åæ¢ï¼äºæ¯ï¼å¾å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³çæ¹ç¨

ð¥=ð¿0âð¿1âð¿â10(ð¥).x=L0âL1âL0â1(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸å¦¨è®¾åå¼çº¿æ§åæ¢ ð¿0 âð¿1 âð¿â10(ð¥) =ðð¥+ððð¥+ðL0âL1âL0â1(x)=ax+bcx+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¾å° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³çæ¹ç¨

ðð¥2+(ðâð)ð¥âð=0.cx2+(dâa)xâb=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å èï¼å¾ªç¯è¿åæ°é½æ¯æ´ç³»æ°äºæ¬¡æ¹ç¨çè§£ï¼åå ä¸ºæ éè¿åæ°é½æ¯æ çæ°ï¼æä»¥å¾ªç¯è¿åæ°é½è¡¨ç¤ºäºäºæ¬¡æ çæ°ï¼

Lagrange çç»æè¯´æåè¿æ¥ä¹æç«ï¼å èäºæ¬¡æ çæ°åå¾ªç¯è¿åæ°æ¯ç­ä»·çï¼

å®çï¼Lagrangeï¼

äºæ¬¡æ çæ°å¯ä»¥è¡¨ç¤ºæå¾ªç¯è¿åæ°ï¼

è¯æ

æè·¯æ¯è¯æä½é¡¹ä¼éå¤åºç°ï¼è®¾äºæ¬¡æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åä½

ð¥=ð0+âð·ð0x=P0+DQ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½¢å¼ï¼å ¶ä¸­ï¼ð0,ð0,ð·P0,Q0,D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ´æ°ä¸ ð0 â£ð· âð20Q0â£DâP02![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ»æ¯å¯è½çï¼æ¯å¦äºæ¬¡æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»å¯ä»¥åæ

ð+ðâð·â²=ðððð+ððððâð·â²=ðððð+ððððâð·â²ðððð=ðððððððð+â(ðððð)2ð·â²(ðððð)2a+bDâ²=paqa+pbqbDâ²=paqb+pbqaDâ²qaqb=papbqaqb+(qaqb)2Dâ²(qaqb)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä»¤ ð =ððððððððP=papbqaqb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð =(ðððð)2Q=(qaqb)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð· =ðð·â²D=QDâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

å°å®åæè¿ç§å½¢å¼çå¥½å¤æ¯ï¼å¯ä»¥è¯æå®çææä½é¡¹é½å ·æç±»ä¼¼çå½¢å¼ï¼

ðð=ðð+âð·ðð,rk=Pk+DQk,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðð,ððPk,Qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´æ°ä¸ ðð â£ð· âð2ðQkâ£DâPk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼æ¡ä»¶ ðð â£ð· âð2ðQkâ£DâPk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¿è¯äºææä½é¡¹çåå­ä¸­ï¼âð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¢çç³»æ°é½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºå¾å°ä½é¡¹çå½¢å¼ï¼å¯ä»¥ä½¿ç¨æ°å­¦å½çº³æ³ï¼å½ ð =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ¾ç¶ï¼åè®¾å·²ç»å¾å°äº ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼å¹¶è®¾ ðð =âððâak=ârkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

ðð=ðð+1ðð+1.rk=ak+1rk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ðð+1rk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç±»ä¼¼å½¢å¼ï¼å¹¶å ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸èµ·ä»£å ¥ä¸å¼ï¼æ

ðð+âð·ðð=ðð+ðð+1ðð+1+âð·=ðð+ðð+1ðð+1âðð+1âð·ð2ð+1âð·.Pk+DQk=ak+Qk+1Pk+1+D=ak+Qk+1Pk+1âQk+1DPk+12âD.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºäºæ¬¡æ çæ°è¡¨ç¤ºæ ð +ðâð·a+bD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¹å¼æ¯å¯ä¸çï¼æä»¥æ¯è¾ä¸¤ä¾§ç³»æ°å¯ç¥

ðððð=ðð+ðð+1ðð+1ð2ð+1âð·,Â 1ðð=âðð+1ð2ð+1âð·.PkQk=ak+Qk+1Pk+1Pk+12âD,Â 1Qk=âQk+1Pk+12âD.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°ç¬¬äºä¸ªç­å¼ä»£å ¥ç¬¬ä¸ä¸ªç­å¼å¯ä»¥è§£åº ðð+1Pk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ðððð=ððâðð+1ððâºðð+1=ððððâðð.PkQk=akâPk+1QkâºPk+1=akQkâPk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä»£å ¥ç¬¬äºä¸ªç­å¼ï¼å°±å¯ä»¥è§£åº ðð+1Qk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ðð+1=ð·âð2ð+1ðð=ð·â(ððððâðð)2ðð=âð2ððð+2ðððð+ð·âð2ððð.Qk+1=DâPk+12Qk=Dâ(akQkâPk)2Qk=âak2Qk+2akPk+DâPk2Qk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®å½çº³åè®¾ï¼ðð â£ð· âð2ðQkâ£DâPk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ç¡®å® ðð+1Pk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð+1Qk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ´æ°ï¼å³ ðð+1rk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹å ·ææè¦æ±çå½¢å¼ï¼

æåï¼è¯æä½é¡¹åªè½åå¾æéå¤ä¸ªå¼ï¼æ èå¿ ç¶éå¤ï¼åæå·²ç»æ±å¾ä½é¡¹

ðð+âð·ðð=ðð=âððâ2ð¥âððâ2ððâ1ð¥âððâ1Pk+DQk=rk=âqkâ2xâpkâ2qkâ1xâpkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èä¸å¯¹äºæ çæ°ï¼æ»æ ðð >1rk>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ï¼å®çå ±è½­

ððââð·ðð=ðâð=âððâ2ð¥ââððâ2ððâ1ð¥ââððâ1=âððâ2ððâ1ð¥ââððâ2ððâ2ð¥ââððâ1ððâ1PkâDQk=rkâ=âqkâ2xââpkâ2qkâ1xââpkâ1=âqkâ2qkâ1xââpkâ2qkâ2xââpkâ1qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºå åå¤§ç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶å°äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º

ððâ2ððâ1>0,Â limðââð¥ââððâ2ððâ2ð¥ââððâ1ððâ1=ð¥ââð¥ð¥ââð¥=1.qkâ2qkâ1>0,Â limkââxââpkâ2qkâ2xââpkâ1qkâ1=xââxxââx=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±è¯´æ

2âð·ðð=ððâðâð>1âº0<ððâ¤2âð·.2DQk=rkârkâ>1âº0<Qkâ¤2D.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ððQk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªè½åæéå¤ä¸ªå¼ï¼è¿èï¼

ð·âð2ð=ððððâ1>0âº|ðð|<âð·,DâPk2=QkQkâ1>0âº|Pk|<D,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼ððPk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åªè½åæéå¤ä¸ªå¼ï¼æ èï¼ä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªææéå¤ä¸ªå¯è½çåå¼ï¼å¿ ç¶å¨æ éé¡¹å éå¤ï¼

å®ççè¯æä¹æä¾äºä¸ä¸ªè®¡ç®äºæ¬¡æ çæ°çä½é¡¹çéæ¨å ¬å¼ï¼

äºæ¬¡æ çæ°çä½é¡¹éæ¨å ¬å¼

äºæ¬¡æ çæ°æ»å¯ä»¥è¡¨ç¤ºæ

ð¥=ð0+âð·ð0x=P0+DQ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½¢å¼ï¼ä¸ ð0 â£ð· âð20Q0â£DâP02![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çä½é¡¹

ðð=ðð+âð·ððrk=Pk+DQk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸­ï¼ðð,ððPk,Qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ´æ°ï¼ä¸æ»¡è¶³éæ¨å ³ç³»

ðð+1=ððððâðð,ðð+1=ð·âð2ð+1ðð.Pk+1=akQkâPk,Qk+1=DâPk+12Qk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªéæ¨å ¬å¼å¯ä»¥ç´æ¥ç¨äºäºæ¬¡æ çæ°çè¿åæ°çè®¡ç®ï¼èä¸æ ¹æ®å®ççè¯æï¼|ðð| <âð·|Pk|<D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðð â¤2âð·Qkâ¤2D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¥ç®æ³çå¤æåº¦åå³äºå¾ªç¯èçé¿åº¦ï¼èåè å¯ä»¥è¯ææ¯ ð(âð·logâ¡ð·)O(Dlogâ¡D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç2ï¼

äºæ¬¡æ çæ°

ç»å®äºæ¬¡æ çæ° ð¼ =ð¥+ð¦âðð§Î±=x+ynz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±åºå ¶è¿åæ°çè¡¨ç¤ºï¼å ¶ä¸­ï¼ð¥,ð¦,ð§,ð âðx,y,z,nâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð >0n>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯å®å ¨å¹³æ¹ï¼

è§£ç­

é¦å å°äºæ¬¡æ çæ°è¡¨ç¤ºæä¸è¿°å½¢å¼ï¼åå©ç¨éæ¨å ¬å¼è®¡ç®å³å¯ï¼è¿åæ°çé¡¹ç± ðð =âððâak=ârkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»åºï¼ä¸ºäºæ±åºå¾ªç¯èï¼éè¦å­å¨ (ðð,ðð)(Pk,Qk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¦æ¬¡åºç°çä¸æ ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text // Return the continued fraction and minimal positive period // of a quadratic irrational (x + y * sqrt(n)) / z. auto quadratic_irrational ( int x , int y , int z , int n ) { int p = x * z ; int d = n * y * y * z * z ; int q = z * z ; int dd = ( int ) sqrt ( n ) * y * z ; int i = 0 ; std :: vector < int > a ; std :: unordered_map < size_t , int > used ; while ( ! used . count ((( 1L L << 32 ) * p ) | q )) { a . emplace_back (( p \+ dd ) / q ); used [(( 1L L << 32 ) * p ) | q ] = i ++ ; p = a . back () * q \- p ; q = ( d \- p * p ) / q ; } return std :: make_pair ( a , i \- used [(( 1L L << 32 ) * p ) | q ]); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # Return the continued fraction and minimal positive period # of a quadratic irrational (x + y * sqrt(n)) / z. def quadratic_irrational ( x , y , z , n ): p = x * z d = n * y * y * z * z q = z * z dd = floor ( sqrt ( n )) * y * z i = 0 a = [] used = dict () while ( p , q ) not in used : a . append (( p \+ dd ) // q ) used [ p , q ] = i p = a [ \- 1 ] * q \- p q = ( d \- p * p ) // q i += 1 return a , i \- used [ p , q ] ```   
---|---  
  
[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)

ç»å® ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯å®å ¨å¹³æ¹æ°ï¼0 â¤ð â¤1090â¤kâ¤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±åº âð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¸è¿åæ° ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

é¦å å©ç¨ä¸è¿°ç®æ³è§£åº âð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¨æï¼å°å¾ªç¯èè¡¨ç¤ºæåå¼çº¿æ§åæ¢ï¼å°±å¯ä»¥ç¨ [å¿«éå¹](../../binary-exponentiation/) è·å¾ ð¥ðxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å½ç¶ï¼å¯¹äºæ²¡æè¿å ¥å¾ªç¯èåä¸è¶³ä¸ä¸ªå¾ªç¯èçé¨åï¼éè¦åç¬å¤çï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> #include <tuple> #include <unordered_map> #include <vector> // Return the continued fraction and minimal positive period // of a quadratic irrational (x + y * sqrt(n)) / z. auto quadratic_irrational ( int x , int y , int z , int n ) { int p = x * z ; int d = n * y * y * z * z ; int q = z * z ; int dd = ( int ) sqrt ( n ) * y * z ; int i = 0 ; std :: vector < int > a ; std :: unordered_map < size_t , int > used ; while ( ! used . count ((( 1L L << 32 ) * p ) | q )) { a . emplace_back (( p \+ dd ) / q ); used [(( 1L L << 32 ) * p ) | q ] = i ++ ; p = a . back () * q \- p ; q = ( d \- p * p ) / q ; } return std :: make_pair ( a , i \- used [(( 1L L << 32 ) * p ) | q ]); } // Fractional Linear Transformation. struct FracLinearTrans { static constexpr int M = 1e9 \+ 7 ; int mat [ 4 ]; FracLinearTrans ( int a , int b , int c , int d ) : mat { a , b , c , d } {} FracLinearTrans operator * ( const FracLinearTrans & rhs ) const { return FracLinearTrans ( (( long long ) mat [ 0 ] * rhs . mat [ 0 ] \+ ( long long ) mat [ 1 ] * rhs . mat [ 2 ]) % M , (( long long ) mat [ 0 ] * rhs . mat [ 1 ] \+ ( long long ) mat [ 1 ] * rhs . mat [ 3 ]) % M , (( long long ) mat [ 2 ] * rhs . mat [ 0 ] \+ ( long long ) mat [ 3 ] * rhs . mat [ 2 ]) % M , (( long long ) mat [ 2 ] * rhs . mat [ 1 ] \+ ( long long ) mat [ 3 ] * rhs . mat [ 3 ]) % M ); } }; int main () { int x , k , L ; std :: cin >> x >> k ; std :: vector < int > a ; std :: tie ( a , L ) = quadratic_irrational ( 0 , 1 , 1 , x ); // L==a.size()-1 for sqrt(x) FracLinearTrans cyc ( 1 , 0 , 0 , 1 ); for ( int i = a . size () \- 1 ; i ; \-- i ) { cyc = FracLinearTrans ( a [ i ], 1 , 1 , 0 ) * cyc ; } // 1/0=Inf. FracLinearTrans res ( 0 , 1 , 0 , 0 ); // Tail terms. for ( int i = k % L ; i ; \-- i ) { res = FracLinearTrans ( a [ i ], 1 , 1 , 0 ) * res ; } // Binary exponentiation. for ( int b = k / L ; b ; b >>= 1 ) { if ( b & 1 ) res = cyc * res ; cyc = cyc * cyc ; } // First term. res = FracLinearTrans ( a [ 0 ], 1 , 1 , 0 ) * res ; printf ( "%d/%d" , res . mat [ 1 ], res . mat [ 3 ]); return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 ``` |  ```text from math import sqrt , floor # Return the continued fraction and minimal positive period # of a quadratic irrational (x + y * sqrt(n)) / z. def quadratic_irrational ( x , y , z , n ): p = x * z d = n * y * y * z * z q = z * z dd = floor ( sqrt ( n )) * y * z i = 0 a = [] used = dict () while ( p , q ) not in used : a . append (( p \+ dd ) // q ) used [ p , q ] = i p = a [ \- 1 ] * q \- p q = ( d \- p * p ) // q i += 1 return a , i \- used [ p , q ] # Compose (A[0]*x + A[1]) / (A[2]*x + A[3]) and (B[0]*x + B[1]) / (B[2]*x + B[3]) def combine ( A , B ): return [ t % mod for t in [ A [ 0 ] * B [ 0 ] \+ A [ 1 ] * B [ 2 ], A [ 0 ] * B [ 1 ] \+ A [ 1 ] * B [ 3 ], A [ 2 ] * B [ 0 ] \+ A [ 3 ] * B [ 2 ], A [ 2 ] * B [ 1 ] \+ A [ 3 ] * B [ 3 ], ] ] # Binary exponentiation. def bpow ( A , n ): return ( [ 1 , 0 , 0 , 1 ] if not n else combine ( A , bpow ( A , n \- 1 )) if n % 2 else bpow ( combine ( A , A ), n // 2 ) ) mod = 10 ** 9 \+ 7 x , k = map ( int , input () . split ()) a , T = quadratic_irrational ( 0 , 1 , 1 , x ) A = ( 1 , 0 , 0 , 1 ) # (x + 0) / (0*x + 1) = x # apply ak + 1/x = (ak*x+1)/(1x+0) to (Ax + B) / (Cx + D) for i in reversed ( range ( 1 , len ( a ))): A = combine ([ a [ i ], 1 , 1 , 0 ], A ) C = ( 0 , 1 , 0 , 0 ) # = 1 / 0 while k % T : i = k % T C = combine ([ a [ i ], 1 , 1 , 0 ], C ) k -= 1 C = combine ( bpow ( A , k // T ), C ) C = combine (( a [ 0 ], 1 , 1 , 0 ), C ) print ( str ( C [ 1 ]) \+ "/" \+ str ( C [ 3 ])) ```   
---|---  
  
### çº¯å¾ªç¯è¿åæ°

äºæ¬¡æ çæ°æ¯æå¾ªç¯è¿åæ°è¡¨ç¤ºçå åå¿ è¦æ¡ä»¶ï¼æ¬èçè®¨è®ºåç»åºäºå®æ°å ·æçº¯å¾ªç¯è¿åæ°è¡¨ç¤ºçå åå¿ è¦æ¡ä»¶ï¼

é¦å ï¼å ä¸ºçº¯å¾ªç¯è¿åæ°å ·æç±»ä¼¼æéè¿åæ°çå½¢å¼ï¼æä»¥å¯ä»¥åãååºãæä½ï¼ç±»ä¼¼äºååºå®çï¼è¿æ ·å¾å°çè¿åæ°è¡¨ç¤ºååæ¥çè¿åæ°è¡¨ç¤ºä¹é´æç¡®å®çå ³ç³»ï¼

å®çï¼Galoisï¼

å¯¹äºçº¯å¾ªç¯è¿åæ°

ð¥=[ââââââð0,ð1,â¯,ðâ],x=[a0,a1,â¯,aââ],![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®°

ð¥â²=[ââââââðâ,â¯,ð1,ð0].xâ²=[aâ,â¯,a1,a0â].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºä¸ºãåæ°è´å ±è½­ãï¼å³ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ±è½­çåæ°çç¸åæ°æ¯ ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å ä¸ºä¸è¦æ± â +1â+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æå°æ­£å¨æï¼æä»¥ä¸å¦¨è®¾ â >0â>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨ååºå®çå¯ç¥ï¼

ðâðââ1=[ðâ,â¯,ð1,ð0]=ðâ²âðâ²â,ðâðââ1=[ðâ,â¯,ð1]=ðâ²ââ1ðâ²ââ1.pâpââ1=[aâ,â¯,a1,a0]=pââ²qââ²,qâqââ1=[aâ,â¯,a1]=pââ1â²qââ1â².![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºç­å¼ä¸¤ä¾§é½æ¯æ¢çº¦åæ°ï¼æä»¥

ðâ²â=ðâ,Â ðâ²â=ðââ1,Â ðâ²ââ1=ðâ,Â ðâ²ââ1=ðââ1.pââ²=pâ,Â qââ²=pââ1,Â pââ1â²=qâ,Â qââ1â²=qââ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºçº¯å¾ªç¯è¿åæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çç¬¬ â +1â+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä½é¡¹å°±æ¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æ

ð¥=ð¥ðâ+ðââ1ð¥ðâ+ðââ1.x=xpâ+pââ1xqâ+qââ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å®æ»¡è¶³äºæ¬¡æ¹ç¨

ðâð¥2+(ðââ1âðâ)ð¥âðââ1=0.qâx2+(qââ1âpâ)xâpââ1=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åçï¼ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³äºæ¬¡æ¹ç¨

ðâ²â(ð¥â²)2+(ðâ²ââ1âðâ²â)ð¥â²âðâ²ââ1=0.qââ²(xâ²)2+(qââ1â²âpââ²)xâ²âpââ1â²=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨ç³»æ°çå ³ç³»å¯ç¥ï¼è¿ä¸ªæ¹ç¨å¯ä»¥åä½

ðââ1(ð¥â²)2+(ðââ1âðâ)ð¥â²âðâ=0.pââ1(xâ²)2+(qââ1âpâ)xâ²âqâ=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤ ð¦ = â1ð¥â²y=â1xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³åä¸ä¸ªæ¹ç¨ï¼ä½æ¯ï¼ð¥ >0 >ð¦x>0>y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å®ä»¬å¹¶éåä¸ä¸ªæ ¹ï¼èæ¯äºä¸ºå ±è½­çå ³ç³»ï¼è¿å°±è¯æäºåå½é¢ï¼

Galois å©ç¨è¿ä¸ªè§å¯ï¼è¿ä¸æ­¥å°ç»åºäºäºæ¬¡æ çæ°æçº¯å¾ªç¯è¿åæ°è¡¨ç¤ºçå åå¿ è¦æ¡ä»¶ï¼

å®çï¼Galoisï¼

äºæ¬¡æ çæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¡¨ç¤ºä¸ºçº¯å¾ªç¯è¿åæ°ï¼å½ä¸ä» å½ ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®çå ±è½­ â1 <ð¥â <0â1<xâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¦æ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯çº¯å¾ªç¯è¿åæ°ï¼é£ä¹å©ç¨åæçè®°å·ï¼æ ð0 =ðâ+1 â¥1a0=aâ+1â¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ è ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå ä¸ºå®çåæ°è´å ±è½­ä¹æ¯å¾ªç¯è¿åæ°ï¼æä»¥å®çå ±è½­ ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ â1ð¥â >1â1xâ>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ â1 <ð¥â <0â1<xâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±è¯æäºçº¯å¾ªç¯è¿åæ°é½æ»¡è¶³è¯¥æ¡ä»¶ï¼

åè¿æ¥ï¼è®¾äºæ¬¡æ çæ° ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ â1 <ð¥â <0â1<xâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æéæ¨å ³ç³»

ðð=ðð+1ðð+1.rk=ak+1rk+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç­å¼ä¸¤è¾¹é½æ¯äºæ¬¡æ çæ°ï¼åå ±è½­å¯ç¥

ðâð=ðð+1ðâð+1.rkâ=ak+1rk+1â.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿ä¸ªéæ¨å ³ç³»ï¼å¯ä»¥è¯æ â1 <ðâð <0â1<rkâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ð â¥0kâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼

é¦å ï¼å¯¹äº ð =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ â1 <ðâ0 =ð¥â0 <0â1<r0â=x0â<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶ï¼å¯¹äº ð â¥0kâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±ç®åè¿åæ°å®ä¹å ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ï¼ðð â¥1akâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èï¼åè®¾ â1 <ðâð <0â1<rkâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

â1<â1ðð<ðâð+1=1ðâðâðð<â11+ðð<0.â1<â1ak<rk+1â=1rkââak<â11+ak<0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±å½çº³å°è¯æäº â1 <ðâð <0â1<rkâ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ð â¥0kâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼å æ­¤ï¼æ

ðð=â1ðâð+1+ðâð=ââ1ðâð+1â.ak=â1rk+1â+rkâ=ââ1rk+1ââ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºäºæ¬¡æ çæ°ä¸å®æ¯å¾ªç¯è¿åæ°ï¼æä»¥å­å¨æ­£æ´æ° ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè³å°æä¸ªå åå¤§ç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ðð =ðð+ð¿rk=rk+L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼æ­¤æ¶å¿ ç¶ä¹æ

ððâ1=ââ1ðâðâ=ââ1ðâð+ð¿â=ðð+ð¿â1.akâ1=ââ1rkââ=ââ1rk+Lââ=ak+Lâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ èï¼

ððâ1=ððâ1+1ðð=ðð+ð¿â1+1ðð+ð¿=ðð+ð¿â1.rkâ1=akâ1+1rk=ak+Lâ1+1rk+L=rk+Lâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æå³çæå°çè½å¤ä½¿å¾ ðð =ðð+ð¿rk=rk+L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¡¨ç¤ºæçº¯å¾ªç¯è¿åæ°ï¼

Galois å®çæ­ç¤ºäºçº¯äºæ¬¡ä¸å°½æ ¹ï¼pure quadratic surdï¼ââå³å½¢å¦ âðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡æ çæ°ââçè¿åæ°è¡¨ç¤ºçè§å¾ï¼

æ¨è®º

å¯¹äºæçæ° ð >1r>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ âðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ çæ°ï¼é£ä¹

âð=[ââðâ,ââââââââð1,â¯,ðâ,2ââðâ]r=[ârâ,a1,â¯,aâ,2ârââ]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸å¯¹äºä»»æ 1 â¤ð â¤â1â¤kâ¤â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðð =ðâ+1âðak=aâ+1âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å¯¹äºäºæ¬¡æ çæ° âðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ââðâ +âð >1ârâ+r>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ â1 <ââðâ ââð <0â1<ârââr<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ââðâ +âðârâ+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯çº¯å¾ªç¯è¿åæ°ï¼

ââðâ+âð=[ââââââââ2ââðâ,ð1,â¯,ðâ].ârâ+r=[2ârâ,a1,â¯,aââ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®ä¸è¿°å®çï¼å®çåæ°è´å ±è½­å ·æå½¢å¼

1âðâââðâ=[ââââââââðâ,â¯,ð1,2ââðâ].1râârâ=[aâ,â¯,a1,2ârââ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨è¿åæ°çåºæ¬æ§è´¨å¯ç¥

âð=ââðâ+11âðâââðâ=[ââðâ,ââââââââðâ,â¯,ð1,2ââðâ].r=ârâ+11râârâ=[ârâ,aâ,â¯,a1,2ârââ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¯ï¼åç± ââðâ +âðârâ+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°è¡¨ç¤ºå¯ç¥ï¼

âð=âââðâ+(ââðâ+âð)=[ââðâ,ââââââââð1,â¯,ðâ,2ââðâ].r=âârâ+(ârâ+r)=[ârâ,a1,â¯,aâ,2ârââ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸ºæ çæ°çè¿åæ°è¡¨ç¤ºæ¯å¯ä¸çï¼æä»¥æ¯è¾ä¸­é´çç³»æ°å°±ç¥éï¼ðð =ðâ+1âðak=aâ+1âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ 1 â¤ð â¤â1â¤kâ¤â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼

ä¾å­ï¼â7474![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°å±å¼

â7474![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°å¯ä»¥è®¡ç®å¦ä¸ï¼ï¼æ­¤å¤ä» æ¯ä¸ºäºè¯´æï¼ç¼ç¨è®¡ç®åºä½¿ç¨åææå°çéå½ç®æ³ï¼

â74=8+(â8)+â74=[8,8+â7410]=[8,1+â2+â7410]=[8,1,2+â747]=[8,1,1+â5+â747]=[8,1,1,5+â747]=[8,1,1,1+â2+â747]=[8,1,1,1,2+â7410]=[8,1,1,1,1+â8+â7410]=[8,1,1,1,1,8+â74]=[8,1,1,1,1,16+(â8)+â74]=[8,ââââââ1,1,1,1,16]74=8+(â8)+74=[8,8+7410]=[8,1+â2+7410]=[8,1,2+747]=[8,1,1+â5+747]=[8,1,1,5+747]=[8,1,1,1+â2+747]=[8,1,1,1,2+7410]=[8,1,1,1,1+â8+7410]=[8,1,1,1,1,8+74]=[8,1,1,1,1,16+(â8)+74]=[8,1,1,1,1,16â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä¸ªä½é¡¹åå«æ¯ï¼

ð1=8+â7410=[ââââââ1,1,1,1,16]ð2=2+â747=[ââââââ1,1,1,16,1]ð3=5+â747=[ââââââ1,1,16,1,1]ð4=2+â7410=[ââââââ1,16,1,1,1]ð5=8+â74=[ââââââ16,1,1,1,1]r1=8+7410=[1,1,1,1,16â]r2=2+747=[1,1,1,16,1â]r3=5+747=[1,1,16,1,1â]r4=2+7410=[1,16,1,1,1â]r5=8+74=[16,1,1,1,1â]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ® Galois çç»è®ºï¼ä½é¡¹ ððrk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð¿+1âðrL+1âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾ªç¯é¨åæ°å¥½ç¸åï¼å æ­¤äºä¸ºåæ°è´å ±è½­ï¼å¦æ âð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¾ªç¯èé¿åº¦ ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥æ°ï¼é£ä¹ä¸­é´çä¸é¡¹å°±ä¸èªèº«äºä¸ºåæ°è´å ±è½­ï¼å¦æå¾ªç¯èé¿åº¦ ð¿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°ï¼å°±ä¸å­å¨è¿æ ·çé¡¹ï¼Pell æ¹ç¨ä¸èçè®¨è®ºä¼è¯´æï¼å¾ªç¯èé¿åº¦çå¥å¶æ§å°å³å®äºæ¹ç¨ ð¥2 âð·ð¦2 = â1x2âDy2=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¦æè§£ï¼

äºæ¬¡æ çæ° âð·D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°å±å¼ä¸»è¦åºç¨å¨ [Pell æ¹ç¨](../pell-equation/) çæ±è§£ä¸­ï¼

## ä¾é¢

å¨ææ¡äºåºç¡æ¦å¿µåï¼éè¦ç ç©¶ä¸äºå ·ä½çä¾é¢æ¥çè§£å¦ä½å¨ç®æ³ç«èµä¸­åºç¨è¿åæ°çæ¹æ³ï¼

çº¿ä¸å¸å 

ç»å® ð =[ð0,ð1,â¯,ðð]r=[a0,a1,â¯,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±åºæ»¡è¶³ 0 â¤ð¥ â¤ð0â¤xâ¤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 0 â¤ð¦ â¤ðð¥0â¤yâ¤rx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´ç¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåçå¸å ï¼

è§£ç­

å¯¹äºæ çéå ð¥ â¥0xâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¸å£³å°±æ¯ç´çº¿ ð¦ =ðð¥y=rx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬èº«ï¼ç¶èï¼å¦ä¸å¾æç¤ºï¼å¦æè¿è¦æ± ð¥ â¤ðxâ¤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ä¸å¸å£³æç»ä¼åç¦»ç´çº¿ï¼

![](./images/lattice-hull.svg)

ä» (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼å¯ä»¥èªå·¦åå³å°æ±åºä¸å¸å£³çæææ´ç¹ï¼åè®¾å½åå·²ç»æ±åºçä¸å¸å£³çæåä¸ä¸ªæ´ç¹æ¯ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç°å¨è¦æ±åºä¸ä¸ä¸ªæ´ç¹ (ð¥â²,ð¦â²)(xâ²,yâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¡¶ç¹ (ð¥â²,ð¦â²)(xâ²,yâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸æ¹ï¼è®° (Îð¥,Îð¦) =(ð¥â² âð¥,ð¦â² âð¦)(Îx,Îy)=(xâ²âx,yâ²ây)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¸¤è çå·®å¼ï¼é£ä¹ï¼å¿ ç¶æ

0<Îð¥â¤ðâð¥,Â 0â¤Îð¦â¤ðÎð¥.0<Îxâ¤Nâx,Â 0â¤Îyâ¤rÎx.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¬¬äºä¸ªä¸ç­å¼æç«ï¼å ä¸ºæ¡ä»¶ Îð¦ >ðÎð¥Îy>rÎx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·²ç»å¨ä¸å¸å£³ä¸è¿ä»¶äºçç¾ï¼è§å¯ (Îð¥,Îð¦)(Îx,Îy)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦æ»¡è¶³çæ¡ä»¶ï¼å¯¹äºä¸åçç¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªæ Îð¥Îx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸çå¨ååï¼æä»¥ï¼åªè¦è½è§£å³è¿ä¸ªå­é®é¢ï¼å°±å¯ä»¥éå½å°æ±åºåé®é¢çæææ´ç¹ï¼

è¿èï¼èèå­é®é¢çè§£æ³ï¼å¯¹æ¯äºåé®é¢ï¼å­é®é¢ç¸å½äºå° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸çä¿®æ¹ä¸º ðâ²Nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶æ±åºä¸å¸å£³ä¸­ä¸åç¹ç¸é»çç¬¬ä¸ä¸ªæ´ç¹ï¼è®°å­é®é¢çè§£ä¸º (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶æ¯äºç´ çï¼å¦åä¸æ¯ç¬¬ä¸ä¸ªæ´ç¹ï¼ï¼ä¸ä¸åç¹è¿çº¿çæç ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ææä½äºç´çº¿ ð¦ =ðð¥y=rx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¹ä¸æ¨ªåæ ä¸è¶ è¿ ðâ²Nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´ç¹ä¸­æå¤§çï¼å¦åä¸å¨å¸å ä¸ï¼ï¼ç»ååæç å ä½è§£é å¯ç¥ï¼è¿æ ·çç¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¿ ç¶å¯¹åºäº ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªä¸ä¸­é´åæ°ï¼å ä¸ºåæ¯è¶å¤§çä¸ä¸­é´åæ°ç¦» ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¶è¿ï¼æä»¥å­é®é¢çè§£ (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçææåæ¯ä¸è¶ è¿ ðâ²Nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸­é´åæ°ä¸­åæ¯æå¤§çé£ä¸ªï¼

å½ç¶ï¼å®é æ±è§£æ¶ï¼æ²¡å¿ è¦å¯¹æ¯ä¸ªå­é®é¢é½éæ°æ±åºè¿æ ·çä¸ä¸­é´åæ°ï¼åºè¯¥é¦å æ±åºææçæ¸è¿åæ°ï¼è¿ç¸å½äºæä¾äºéåææçä¸ä¸­é´åæ°çæ¹æ³ï¼ç¶ååæ¯ä»å¤§å°å°å°éåä¸ä¸­é´åæ°ï¼æ¯æ¬¡é½å°è¯å°å®å å°åä¸ä¸ªæ´ç¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼ç´å°ä¸è½æ·»å ä¸ºæ­¢æç»§ç»­å°è¯ä¸ä¸ä¸ªä¸ä¸­é´åæ°ï¼

æ­¤å¤æä¸äºæ¾ç¶çä¼åï¼é¦å ï¼å¯¹äºä¸ä¸­é´åæ° (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ ç¶å­å¨å¥æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 0 â¤ð¡ <ðð0â¤t<ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ (ð,ð) =(ððâ1,ððâ1) +ð¡(ðð,ðð)(q,p)=(qkâ1,pkâ1)+t(qk,pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦æ¾å°æå¤§ç ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ððâ1 +ð¡ðð +ð¥ â¤ðqkâ1+tqk+xâ¤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å°±å¥½äºï¼äº¦å³ ð¡ =âðâððâ1âð¥ððât=âNâqkâ1âxqkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç¨æ å¿ ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¶çï¼å ä¸ºæ´å¤§çä¸æ¸è¿åæ° (ðð+2,ðð+2)(qk+2,pk+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·²ç»æ·»å å®äºï¼èæ¯æ¬¡ç¡®å®æ·»å çæ¬¡æ°çæ¶åï¼ç´æ¥è®¡ç® âðâð¥ðââNâxqâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼ä¸å¿ éä¸ªå°è¯ï¼

ä¼ååçç®æ³çå¤æåº¦æ¯ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼è½ç¶ä¸ä¸­é´åæ°å¯¹åºçæ´ç¹å¯è½æå¾å¤ï¼ä½æ¯çæ­£æä¸ºå¢éçå¹¶ä¸å¤ï¼ä¸é¢è¦è¯´æï¼ææ 0 â¤ð¡ <ðð0â¤t<ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸­é´åæ° (ð,ð) =(ððâ1,ððâ1) +ð¡(ðð,ðð)(q,p)=(qkâ1,pkâ1)+t(qk,pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼è³å¤ä¼åºç°ä¸¤ä¸ªå¢éï¼åè®¾è¿äºä¸ä¸­é´åæ°ä¸­ç¡®å®åºç°äºå¢éï¼åæ­¤æ¶å¿ ç¶æ ððâ1 â¤ð âð¥ <ðð+1qkâ1â¤Nâx<qk+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¦¨è®¾ ð¡ =âðâððâ1âð¥ððât=âNâqkâ1âxqkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð¡ =0t=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¢éå°±æ Îð¥ =ððâ1Îx=qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ èæ·»å å®å¢éåï¼å°±æ ð âð¥â² <ððâ1Nâxâ²<qkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ä¼åå¨è¿äºä¸ä¸­é´åæ°ä¸­åºç°æ°çå¢éï¼å¦æ ð¡ >0t>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ·»å å®å¢éåï¼å¿ ç¶æ ð âð¥â² =(ð âððâ1 âð¥)modðð <ððNâxâ²=(Nâqkâ1âx)modqk<qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ä½¿è¿ä¼å¨åä¸æ®µä¸ä¸­é´åæ°ä¸­åºç°æ°çå¢éï¼ä¸æ¬¡ä¹åªè½æ ð¡â² =0tâ²=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¨è¿æ ·çä¸æ®µä¸ä¸­é´åæ°ä¸­ï¼è³å¤åªè½åºç°ä¸¤ä¸ªå¢éï¼è¿å°±è¯´æï¼æ»çæ¶é´å¤æåº¦æ¯ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text // Find [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute // upper convex hull of lattice points on 0 <= x <= N and 0 <= y <= r * x, // where r = [a0, a1, a2, ...] and there are ah[i]-1 integer points on the // segment between r[i] and r[i+1]. auto hull ( std :: vector < int > a , int N ) { std :: vector < int > p , q ; std :: tie ( p , q ) = convergents ( a ); int t = N / q . back (); std :: vector < int > ah = { t }; std :: vector < int > ph = { 0 , t * p . back ()}; std :: vector < int > qh = { 0 , t * q . back ()}; for ( int i = q . size () \- 1 ; i ; \-- i ) { if ( i % 2 ) { while ( qh . back () \+ q [ i \- 1 ] <= N ) { t = ( N \- qh . back () \- q [ i \- 1 ]) / q [ i ]; int dp = p [ i \- 1 ] \+ t * p [ i ]; int dq = q [ i \- 1 ] \+ t * q [ i ]; int k = ( N \- qh . back ()) / dq ; ah . push_back ( k ); ph . push_back ( ph . back () \+ k * dp ); qh . push_back ( qh . back () \+ k * dq ); } } } return make_tuple ( ah , ph , qh ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text # Find [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute # upper convex hull of lattice points on 0 <= x <= N and 0 <= y <= r * x, # where r = [a0, a1, a2, ...] and there are ah[i]-1 integer points on the # segment between r[i] and r[i+1]. def hull ( a , N ): p , q = convergents ( a ) t = N // q [ \- 1 ] ah = [ t ] ph = [ 0 , t * p [ \- 1 ]] qh = [ 0 , t * q [ \- 1 ]] for i in reversed ( range ( len ( q ))): if i % 2 == 1 : while qh [ \- 1 ] \+ q [ i \- 1 ] <= N : t = ( N \- qh [ \- 1 ] \- q [ i \- 1 ]) // q [ i ] dp = p [ i \- 1 ] \+ t * p [ i ] dq = q [ i \- 1 ] \+ t * q [ i ] k = ( N \- qh [ \- 1 ]) // dq ah . append ( k ) ph . append ( ph [ \- 1 ] \+ k * dp ) qh . append ( qh [ \- 1 ] \+ k * dq ) return ah , ph , qh ```   
---|---  
  
[Timus - Crime and Punishment](https://timus.online/problem.aspx?space=1&num=1430)

ç»å®æ­£æ´æ° ð´,ðµ,ð â¤2 Ã109A,B,Nâ¤2Ã109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ð¥,ð¦ â¥0x,yâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð´ð¥ +ðµð¦ â¤ðAx+Byâ¤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð´ð¥ +ðµð¦Ax+By![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°½å¯è½å¤§ï¼

è§£ç­

è¿ä¸ªé®é¢æä¸ä¸ªå¤æåº¦ä¸º ð(âð)O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£æ³ï¼ä¸å¦¨è®¾ ð´ â¥ðµAâ¥B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ð´(ðµ +ð¥) +ðµð¦ =ð´ð¥ +ðµ(ð´ +ð¦)A(B+x)+By=Ax+B(A+y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥åªéè¦å¨ ð¥ â¤min{ð/ð´,ðµ}xâ¤min{N/A,B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æç´¢ç­æ¡å³å¯ï¼è¿è¶³å¤éè¿æ¬é¢ï¼ä½æ¯ï¼å¦æåºç¨è¿åæ°æ¹æ³ï¼é£ä¹æ¶é´å¤æåº¦å°±å¯ä»¥éä½å° ð(logâ¡ð)O(logâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºäºè®¨è®ºæ¹ä¾¿ï¼é¦å éè¿ä»£æ¢ ð¥ â¦âð/ð´â âð¥xâ¦âN/Aââx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¥æ¹å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¦å·ï¼ä»¤ ð¶ =ðmodð´C=NmodA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð =âð/ð´âM=âN/Aâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ååé®é¢è½¬åä¸ºå¨ 0 â¤ð¥ â¤ð0â¤xâ¤M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðµð¦ âð´ð¥ â¤ð¶ByâAxâ¤C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¡ä»¶ä¸ï¼æ±æä¼ç (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðµð¦ âð´ð¥ByâAx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¤§ï¼å¯¹äºæ¯ä¸ªåºå®ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¼ç ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ä¸º âð´ð¥+ð¶ðµââAx+CBâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¥ä¸æ¥è¦è¯´æçæ¯ï¼è¿ä¸ªé®é¢åä¸ä¸ä¸ªä¾é¢å ·æç±»ä¼¼çè§£æ³ï¼ä½æ¯ï¼ä¸ä¸ä¸ä¸ªä¾é¢ä¸­ä½¿ç¨ä¸ä¸­é´åæ°åç¦»ç´çº¿ä¸åï¼æ¬é¢éè¦ä½¿ç¨ä¸ä¸­é´åæ°æ¥æ¥è¿ç´çº¿ï¼å ·ä½æ¥è¯´ï¼ð¶ â(ðµð¦ âð´ð¥)Câ(ByâAx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼æ­£æ¯äºç¹ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç´çº¿ ðµð¦ âð´ð¥ =ð¶ByâAx=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè·ç¦»ï¼è¦æå¤§å ðµð¦ âð´ð¥ByâAx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç­ä»·äºæå°åè¿ä¸ªè·ç¦»ï¼ç®æ³çç®æ æ¯è¦æ¾å°ç´çº¿ ðµð¦ âð´ð¥ =ð¶ByâAx=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¹è·ç¦»å®æè¿çå¯è¡çæ´ç¹ï¼ç®æ³çæè·¯å°±æ¯ä»æå·¦ä¾§çç¹å¼å§ï¼æ²¿çè¿äºæ´ç¹çä¸å¸å£³æç´¢ï¼éæ­¥ç¼©å°ä¸ç´çº¿çè·ç¦»ï¼ç´å°å¾å°æä¼è§£ï¼

å¨ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ ç³»å ï¼ç®æ³ä» (0,âð¶/ðµâ)(0,âC/Bâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼éå½å°å¯»æ¾å¹¶æ·»å æä¼çå¢é (Îð¥,Îð¦)(Îx,Îy)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ä¿è¯æ·»å åçç¹æ¯èµ·ä¹åæ´é è¿ç´çº¿ ðµð¦ âð´ð¥ =ð¶ByâAx=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ä¸è½å°è¾¾ç´çº¿çå¦ä¸ä¾§ï¼ä¹ä¸è½è®©æ¨ªåæ å¤§äº ðM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®¾å·²ç»å¾å°çç¹æ¯ (ð¥,ð¦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å¢é (Îð¥,Îð¦)(Îx,Îy)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³çæ¡ä»¶å°±æ¯

0<ðµÎð¦âð´Îð¥â¤ð¶â(ðµð¦âð´ð¥),Â 0<Îð¥â¤ðâð¥.0<BÎyâAÎxâ¤Câ(ByâAx),Â 0<Îxâ¤Mâx.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç §æ²¿ä¸å¸å£³æç´¢çæè·¯ï¼åªéè¦æ¾å°æ»¡è¶³è¿äºæ¡ä»¶çç¹ä¸­ Îð¥Îx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çå³å¯ï¼å°ç¬¬ä¸ä¸ªä¸ç­å¼æ¹åæ

Îð¦â¤ð´ðµÎð¥+ð¶â(ðµð¦âð´ð¥)ðµ.Îyâ¤ABÎx+Câ(ByâAx)B.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»ååæç å ä½è§£é å¯ç¥ï¼åªè¦åé¢çå¸¸æ°é¡¹å°äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æ»¡è¶³è¿ä¸ªä¸ç­å¼çæ´ç¹ (Îð¥,Îð¦)(Îx,Îy)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ¨ªåæ æå°çï¼ä¸å®å¯¹åºçæä¸ªä¸ä¸­é´åæ°ï¼è¿æ¯å ä¸ºå®æ¯ææåæ¯ä¸è¶ è¿å®çåæ¯çåæ°ä¸­ï¼ä»ä¸æ¹é¼è¿æä¸ªå®æ°æææå¥½çï¼è¿åªè½æ¯ä¸ä¸­é´åæ°ï¼èæ¯æ¬¡æ·»å å¢éåï¼é½ä¼å¯¼è´ Îð¦Îy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸çåå¾æ´ç´§ï¼è¿æå³çå¿ é¡»èå¯åæ¯æ´å¤§çä¸ä¸­é´åæ°ï¼

ä»¿ç §ä¸ä¸ä¸ªä¾é¢çæè·¯ï¼åæ¯ä»å°å°å¤§èå¯ææä¸ä¸­é´åæ°ï¼å¦æè½å¤æ¾å°æ¨ªåæ åçºµåæ é½ä¸è¶ççä¸ä¸­é´åæ°ï¼å°±æ·»å è¿å»ï¼å¹¶æ´æ°ç¸åºçä¸çï¼å½ææå¯è¡çä¸ä¸­é´åæ°é½æ·»å ç»æåï¼å¾å°çå°±æ¯æä¼è§£ï¼ç¸è¾äºä¹åï¼è¿ä¸ªé¢ç®éè¦åæ¶ä¿è¯æ¨ªçºµåæ é½ä¸è¶çï¼éè¦æ ¼å¤æ³¨æï¼åºäºåä¸ä¸ä¸ªä¾é¢ç±»ä¼¼çè®ºè¿°ï¼ä¸è¿è¿æ¬¡æ¯ä½¿ç¨ ðµÎð¦ âð´Îð¥BÎyâAÎx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»£æ¿ä¹åç Îð¥Îx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è¯´æè¿ä¸ªç®æ³çå¤æåº¦æ¯ ð(logâ¡min{ð´,ðµ})O(logâ¡min{A,B})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text // Find ( x , y ) such that y = ( A * x \+ B ) / C , // such that Cy \- Ax is max and 0 <= x <= N . auto closest ( int A , int B , int C , int N ) { // y <= ( A * x \+ B ) / C <=> diff ( x , y ) <= B auto diff = [ & ]( int x , int y ) -> int { return C * y \- A * x ; }; std :: vector < int > p , q ; std :: tie ( p , q ) = convergents ( fraction ( A , C )); int qh = 0 , ph = B / C ; for ( int i = 2 ; i < q . size () \- 1 ; ++ i ) { if ( i % 2 == 0 ) { while ( diff ( qh \+ q [ i \+ 1 ], ph \+ p [ i \+ 1 ]) <= B ) { int t = 1 \+ ( diff ( qh \+ q [ i \- 1 ], ph \+ p [ i \- 1 ]) \- B \- 1 ) / ( \- diff ( q [ i ], p [ i ])); int dp = p [ i \- 1 ] \+ t * p [ i ]; int dq = q [ i \- 1 ] \+ t * q [ i ]; int k = ( N \- qh ) / dq ; if ( k == 0 ) { return std :: make_pair ( qh , ph ); } if ( diff ( dq , dp ) != 0 ) { k = std :: min ( k , ( B \- diff ( qh , ph )) / diff ( dq , dp )); } qh += k * dq ; ph += k * dp ; } } } return std :: make_pair ( qh , ph ); } auto solve ( int A , int B , int N ) { int x , y ; std :: tie ( x , y ) = closest ( A , N % A , B , N / A ); return std :: make_pair ( N / A \- x , y ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text # Find (x, y) such that y = (A*x+B) // C, # such that Cy - Ax is max and 0 <= x <= N. def closest ( A , B , C , N ): # y <= (A*x + B)/C <=> diff(x, y) <= B def diff ( x , y ): return C * y \- A * x p , q = convergents ( fraction ( A , C )) qh , ph = 0 , B // C for i in range ( 2 , len ( q ) \- 1 ): if i % 2 == 0 : while diff ( qh \+ q [ i \+ 1 ], ph \+ p [ i \+ 1 ]) <= B : t = 1 \+ ( diff ( qh \+ q [ i \- 1 ], ph \+ p [ i \- 1 ]) \- B \- 1 ) // ( \- diff ( q [ i ], p [ i ]) ) dp = p [ i \- 1 ] \+ t * p [ i ] dq = q [ i \- 1 ] \+ t * q [ i ] k = ( N \- qh ) // dq if k == 0 : return qh , ph if diff ( dq , dp ) != 0 : k = min ( k , ( B \- diff ( qh , ph )) // diff ( dq , dp )) qh , ph = qh \+ k * dq , ph \+ k * dp return qh , ph def solve ( A , B , N ): x , y = closest ( A , N % A , B , N // A ) return N // A \- x , y ```   
---|---  
  
[June Challenge 2017 - Euler Sum](https://www.codechef.com/problems/ES)

æ± ðâð¥=1âeð¥ââx=1Nâexâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å ¶ä¸­ï¼ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯èªç¶å¯¹æ°çåºï¼

æç¤ºï¼ð =[2,1,2,1,1,4,1,1,6,1,â¯,1,2ð,1,â¯]e=[2,1,2,1,1,4,1,1,6,1,â¯,1,2n,1,â¯]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼8

è§£ç­

è¿ä¸ªåç­äºéå {(ð¥,ð¦) :1 â¤ð¥ â¤ð,1 â¤ð¦ â¤eð¥}{(x,y):1â¤xâ¤N,1â¤yâ¤ex}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çæ´ç¹ä¸ªæ°ï¼å¨æå»ºå®ç´çº¿ ð¦ =eð¥y=ex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çæ´ç¹çå¸å åï¼å¯ä»¥ä½¿ç¨ [Pick å®ç](../../../geometry/pick/) è®¡ç®æ´ç¹ä¸ªæ°ï¼æ¶é´å¤æåº¦ä¸º ð(logâ¡ð)O(logâ¡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åé®é¢è¦æ± ð â¤104000Nâ¤104000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤å¤ C++ ä»£ç ä» ä½ç¤ºæï¼å¹¶æ²¡æå®ç°é«ç²¾åº¦è®¡ç®ç±»ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // Find sum of floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...] int sum_floor ( std :: vector < int > a , int N ) { N ++ ; std :: vector < int > ah , ph , qh ; std :: tie ( ah , ph , qh ) = hull ( a , N ); // The number of lattice points within a vertical right trapezoid // on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has // a+1 integer points on the segment (0; y1) - (dx; y2). auto picks = []( int y1 , int y2 , int dx , int a ) -> int { int b = y1 \+ y2 \+ a \+ dx ; int A = ( y1 \+ y2 ) * dx ; return ( A \+ b ) / 2 \- y2 ; // = (A - b + 2) // 2 + b - (y2 + 1) }; int ans = 0 ; for ( size_t i = 1 ; i < qh . size (); i ++ ) { ans += picks ( ph [ i \- 1 ], ph [ i ], qh [ i ] \- qh [ i \- 1 ], ah [ i \- 1 ]); } return ans \- N ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text # Find sum of floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...]. def sum_floor ( a , N ): N += 1 ah , ph , qh = hull ( a , N ) # The number of lattice points within a vertical right trapezoid # on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has # a+1 integer points on the segment (0; y1) - (dx; y2) but with # the number of points on the vertical right line excluded. def picks ( y1 , y2 , dx , a ): b = y1 \+ y2 \+ a \+ dx A = ( y1 \+ y2 ) * dx return ( A \+ b ) // 2 \- y2 # = (A - b + 2) // 2 + b - (y2 + 1) ans = 0 for i in range ( 1 , len ( qh )): ans += picks ( ph [ i \- 1 ], ph [ i ], qh [ i ] \- qh [ i \- 1 ], ah [ i \- 1 ]) return ans \- N ```   
---|---  
  
[NAIPC 2019 - It's a Mod, Mod, Mod, Mod World](https://open.kattis.com/problems/itsamodmodmodmodworld)

ç»å®æ­£æ´æ° ð,ð,ðp,q,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ðâð=1[ððmodð]âi=1n[pimodq]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è§£ç­

å ä¸ºåå¼å¯ä»¥åå½¢ä¸º

ðâð=1[ððmodð]=ðâð=1(ððâðâðððâ)=ðð(ð+1)2âððâð=1âðððâ,âi=1n[pimodq]=âi=1n(piâqâpiqâ)=pn(n+1)2âqâi=1nâpqiâ,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªé®é¢å¯ä»¥è½¬åä¸ºä¸ä¸ä¸ªé®é¢ï¼åªè¦ç¨ ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿ä»£ ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼åæ¬¡æ¥è¯¢çæ¶é´å¤æåº¦ä¸º ð(logâ¡min{ð,ð})O(logâ¡min{p,q})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 ``` |  ```text int solve ( int p , int q , int n ) { return p * n * ( n \+ 1 ) / 2 \- q * sum_floor ( fraction ( p , q ), n ); } ```   
---|---  
  
```text 1 2 ``` |  ```text def solve ( p , q , N ): return p * N * ( N \+ 1 ) // 2 \- q * sum_floor ( fraction ( p , q ), N ) ```   
---|---  
  
[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)

ç»å®æ­£æ´æ° ð,ð,ð´,ðµN,M,A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ± ðâ1âð=0âð´â ð+ðµðââi=0Nâ1âAâ i+BMâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è§£ç­

è¿æ¯å°ç®åä¸ºæ­¢æä¸ºå¤æçé¢ç®ï¼å®å¯ä»¥éè¿ [ç±»æ¬§å éå¾ç®æ³](../euclidean/) è®¡ç®ï¼æ­¤å¤ç»åºåºäºè¿åæ°çç®æ³ï¼æ¶é´å¤æåº¦æ¯ ð(logâ¡min{ð´,ðµ})O(logâ¡min{A,B})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯ä»¥éè¿æé ç´çº¿ ð¦ =ð´ð¥+ðµðy=Ax+BM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥ä¸ä¸ 0 â¤ð¥ <ð0â¤x<N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨é¨æ´ç¹çå¸å ï¼å¹¶ç¨ Pick å®çè®¡ç®æ´ç¹çä¸ªæ°ï¼ä¹åå·²ç»è§£å³ ðµ =0B=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å¯¹äºä¸è¬çæ å½¢ï¼å¯ä»¥åä¸ºä¸¤æ­¥è¿è¡ï¼é¦å éè¿æ·»å ä¸ä¸­é´åæ°æ¥éæ­¥æ¥è¿ç´çº¿ï¼å³ç¬¬äºä¸ªä¾é¢ï¼ï¼ç´å°æ¾å°ææ¥è¿ç´çº¿çç¹ï¼åéè¿æ·»å ä¸ä¸­é´åæ°æ¥éæ­¥è¿ç¦»ç´çº¿ï¼å³ç¬¬ä¸ä¸ªä¾é¢ï¼ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text // Find convex hull of lattice ( x , y ) such that C * y <= A * x \+ B . auto hull ( int A , int B , int C , int N ) { auto diff = [ & ]( int x , int y ) -> int { return C * y \- A * x ; }; auto a = fraction ( A , C ); std :: vector < int > p , q ; std :: tie ( p , q ) = convergents ( a ); std :: vector < int > ah ( 0 ), ph ( 1 , B / C ), qh ( 1 , 0 ); auto insert = [ & ]( int dq , int dp ) -> void { int k = ( N \- qh . back ()) / dq ; if ( diff ( dq , dp ) > 0 ) { k = std :: min (( int ) k , ( B \- diff ( qh . back (), ph . back ())) / diff ( dq , dp )); } ah . emplace_back ( k ); qh . emplace_back ( qh . back () \+ k * dq ); ph . emplace_back ( ph . back () \+ k * dp ); }; for ( int i = 1 ; i < q . size () \- 1 ; ++ i ) { if ( i % 2 == 0 ) { while ( diff ( qh . back () \+ q [ i \+ 1 ], ph . back () \+ p [ i \+ 1 ]) <= B ) { int t = ( B \- diff ( qh . back () \+ q [ i \+ 1 ], ph . back () \+ p [ i \+ 1 ])) / ( \- diff ( q [ i ], p [ i ])); int dp = p [ i \+ 1 ] \- t * p [ i ]; int dq = q [ i \+ 1 ] \- t * q [ i ]; if ( dq < 0 || qh . back () \+ dq > N ) break ; insert ( dq , dp ); } } } insert ( q . back (), p . back ()); for ( int i = q . size () \- 1 ; i ; \-- i ) { if ( i % 2 == 1 ) { while ( qh . back () \+ q [ i \- 1 ] <= N ) { int t = ( N \- qh . back () \- q [ i \- 1 ]) / q [ i ]; int dp = p [ i \- 1 ] \+ t * p [ i ]; int dq = q [ i \- 1 ] \+ t * q [ i ]; insert ( dq , dp ); } } } return std :: make_tuple ( ah , ph , qh ); } // Sum of floor ( Ax \+ B ) / M from 0 to N \- 1\. auto solve ( int N , int M , int A , int B ) { std :: vector < int > ah , ph , qh ; std :: tie ( ah , ph , qh ) = hull ( A , B , M , N ); // The number of lattice points within a vertical right trapezoid // on points ( 0 ; 0 ) \- ( 0 ; y1 ) \- ( dx ; y2 ) \- ( dx ; 0 ) that has // a \+ 1 integer points on the segment ( 0 ; y1 ) \- ( dx ; y2 ) but with // the number of points on the vertical right line excluded . auto picks = [ & ]( int y1 , int y2 , int dx , int a ) -> int { int b = y1 \+ y2 \+ a \+ dx ; int A = ( y1 \+ y2 ) * dx ; return ( A \+ b ) / 2 \- y2 ; // = ( A \- b \+ 2 ) // 2 \+ b \- ( y2 \+ 1 ) }; int ans = 0 ; for ( int i = 1 ; i < qh . size (); ++ i ) { ans += picks ( ph [ i \- 1 ], ph [ i ], qh [ i ] \- qh [ i \- 1 ], ah [ i \- 1 ]); } return ans \- N ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 ``` |  ```text # Find convex hull of lattice (x, y) such that C*y <= A*x+B. def hull ( A , B , C , N ): def diff ( x , y ): return C * y \- A * x a = fraction ( A , C ) p , q = convergents ( a ) ah = [] ph = [ B // C ] qh = [ 0 ] def insert ( dq , dp ): k = ( N \- qh [ \- 1 ]) // dq if diff ( dq , dp ) > 0 : k = min ( k , ( B \- diff ( qh [ \- 1 ], ph [ \- 1 ])) // diff ( dq , dp )) ah . append ( k ) qh . append ( qh [ \- 1 ] \+ k * dq ) ph . append ( ph [ \- 1 ] \+ k * dp ) for i in range ( 1 , len ( q ) \- 1 ): if i % 2 == 0 : while diff ( qh [ \- 1 ] \+ q [ i \+ 1 ], ph [ \- 1 ] \+ p [ i \+ 1 ]) <= B : t = ( B \- diff ( qh [ \- 1 ] \+ q [ i \+ 1 ], ph [ \- 1 ] \+ p [ i \+ 1 ])) // ( \- diff ( q [ i ], p [ i ]) ) dp = p [ i \+ 1 ] \- t * p [ i ] dq = q [ i \+ 1 ] \- t * q [ i ] if dq < 0 or qh [ \- 1 ] \+ dq > N : break insert ( dq , dp ) insert ( q [ \- 1 ], p [ \- 1 ]) for i in reversed ( range ( len ( q ))): if i % 2 == 1 : while qh [ \- 1 ] \+ q [ i \- 1 ] <= N : t = ( N \- qh [ \- 1 ] \- q [ i \- 1 ]) // q [ i ] dp = p [ i \- 1 ] \+ t * p [ i ] dq = q [ i \- 1 ] \+ t * q [ i ] insert ( dq , dp ) return ah , ph , qh def solve ( N , M , A , B ): ah , ph , qh = hull ( A , B , M , N ) # The number of lattice points within a vertical right trapezoid # on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has # a+1 integer points on the segment (0; y1) - (dx; y2) but with # the number of points on the vertical right line excluded. def picks ( y1 , y2 , dx , a ): b = y1 \+ y2 \+ a \+ dx A = ( y1 \+ y2 ) * dx return ( A \+ b ) // 2 \- y2 # = (A - b + 2) // 2 + b - (y2 + 1) ans = 0 for i in range ( 1 , len ( qh )): ans += picks ( ph [ i \- 1 ], ph [ i ], qh [ i ] \- qh [ i \- 1 ], ah [ i \- 1 ]) return ans \- N ```   
---|---  
  
[OKC 2 - From Modular to Rational](https://codeforces.com/gym/102354/problem/I)

æä¸ªæªç¥çæçæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ 1 â¤ð,ð â¤1091â¤p,qâ¤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è¯¢é®å¯¹æä¸ªç´ æ° ð â[109,1012]mâ[109,1012]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡åç ððâ1pqâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼è¯·å¨ä¸è¶ è¿åæ¬¡è¯¢é®å ç¡®å® ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è¿ä¸ªé®é¢ç­ä»·äºæ¾å° [1,ð][1,N]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä½¿å¾ ð´ð¥modðAxmodM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

æ ¹æ® [ä¸­å½å©ä½å®ç](../crt/)ï¼è¯¢é®å¯¹å¤ä¸ªç´ æ°åæ¨¡åçç»æï¼ç¸å½äºè¯¢é®å¯¹è¿äºç´ æ°çä¹ç§¯åæ¨¡çç»æï¼å æ­¤ï¼æ¬é¢å¯ä»¥çä½æ¯è¯¢é®åæ°å¯¹è¶³å¤å¤§çæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡åçç»æï¼è¦æ±ç¡®å®åæ°çåå­ååæ¯ï¼

å¯¹äºæä¸ªæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ðð â¡ð(modð)qrâ¡p(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«çæ°å¯¹ (ð,ð)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½å¹¶ä¸å¯ä¸ï¼åè®¾ (ð1,ð1)(p1,q1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð2,ð2)(p2,q2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥ä½¿å¾è¿ä¸ªç­å¼æç«ï¼é£ä¹å¿ ç¶æ (ð1ð2 âð2ð1)ð â¡0(modð)(p1q2âp2q1)râ¡0(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ® ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæé å¯ç¥ï¼ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼æä»¥ ð1ð2 âð2ð1 â¡0(modð)p1q2âp2q1â¡0(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ð â£(ð1ð2 âð2ð1)mâ£(p1q2âp2q1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð1ð2 âð2ð1p1q2âp2q1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ºé¶ï¼é£ä¹å®çç»å¯¹å¼è³å°æ¯ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é®é¢ä¸­éå¶äº ð,ð â[1,109]p,qâ[1,109]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æå³çè¿ä¸ªå·®å¼ä¸åºè¯¥è¶ è¿ 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤åªè¦å ð >1018m>1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥ä¿è¯æ±åºç (ð,ð)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¯ä¸çï¼

ç°å¨çé®é¢å½ç»ä¸ºï¼ç»å®æ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä½æ° ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±ä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ´æ°å¯¹ (ð,ð)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð â¡ð(modð)qrâ¡p(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨å·²ç¥è¿æ ·çè§£æ¯å¯ä¸çæ åµä¸ï¼å ¶å®åªè¦æ¾å° ð â[1,ð]qâ[1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ä½¿å¾ ððmodðqrmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°ç ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼å ä¸ºæ­¤æ¶æä¸ä» æä¸ä¸ª ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ä½æ°ä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ­£æ¯åé¢æå°çç­ä»·è¡¨è¿°ï¼

å¨ (ð,ð)(q,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¨çå¹³é¢åæ ç³»å ï¼è¿ç¸å½äºè¦æ¾å° ð â[1,ð]qâ[1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶å¨ç´çº¿ ðð âðð =0qrâkm=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¹ææ¥è¿å®çæ´ç¹ï¼å ä¸ºä½æ° ððmodðqrmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ­£æ¯äºæ´ç¹ä¸ç´çº¿çè·ç¦»ï¼ç»ååæç å ä½è§£é å¯ç¥ï¼è¿æ ·çæ´ç¹å¿ ç¶å¯¹åºçæçåæ° ððrm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¸ªä¸ä¸­é´åæ°ï¼ç®æ³å¤æåº¦æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{r,m})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text // Find Q that minimizes Q*r mod m for 1 <= k <= n < m. int mod_min ( int r , int n , int m ) { auto a = fraction ( r , m ); std :: vector < int > p , q ; std :: tie ( p , q ) = convergents ( a ); for ( int i = 2 ; i < q . size (); ++ i ) { if ( i % 2 == 1 && ( i \+ 1 == q . size () || q [ i \+ 1 ] > n )) { int t = ( n \- q [ i \- 1 ]) / q [ i ]; return q [ i \- 1 ] \+ t * q [ i ]; } } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text # Find Q that minimizes Q*r mod m for 1 <= k <= n < m. def mod_min ( r , n , m ): a = fraction ( r , m ) p , q = convergents ( a ) for i in range ( 2 , len ( q )): if i % 2 == 1 and ( i \+ 1 == len ( q ) or q [ i \+ 1 ] > n ): t = ( n \- q [ i \- 1 ]) // q [ i ] return q [ i \- 1 ] \+ t * q [ i ] return 0 ```   
---|---  
  
## ä¹ é¢

  * [UVa OJ - Continued Fractions](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=775)
  * [ProjectEuler+ #64: Odd period square roots](https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem)
  * [ãLibreOJ NOI Round #2ãåæªå¹é©¬](https://loj.ac/p/573)
  * [Codeforces Round #184 (Div. 2) - Continued Fractions](https://codeforces.com/contest/305/problem/B)
  * [Codeforces Round #201 (Div. 1) - Doodle Jump](https://codeforces.com/contest/346/problem/E)
  * [Codeforces Round #325 (Div. 1) - Alice, Bob, Oranges and Apples](https://codeforces.com/contest/585/problem/C)
  * [POJ Founder Monthly Contest 2008.03.16 - A Modular Arithmetic Challenge](http://poj.org/problem?id=3530)
  * [2019 Multi-University Training Contest 5 - fraction](http://acm.hdu.edu.cn/showproblem.php?pid=6624)
  * [SnackDown 2019 Elimination Round - Election Bait](https://www.codechef.com/SNCKEL19/problems/EBAIT)
  * [Luogu P5179. Fraction](https://www.luogu.com.cn/problem/P5179)
  * [Luogu P7739. [NOI2021] å¯ç ç®±](https://www.luogu.com.cn/problem/P7739)

## åèæç®ä¸æå±é è¯»

  * Hardy, G. H., Wright, E. M., Heath-Brown, R., & Silverman, J. (2008). An Introduction to the Theory of Numbers. Oxford Mathematics.
  * æ±å°§è¾°ï¼çè¿ç¥¥ãä¸¢çªå¾é¼è¿å¼è®ºã
  * [FatFish çåå®¢ - è¿åæ°å ¥é¨](https://chaoli.club/index.php/2756)
  * [Simple continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Simple_continued_fraction)
  * [Periodic continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Periodic_continued_fraction)
  * [Gosper's original notes on continued fraction arithmetic algorithms](https://perl.plover.com/yak/cftalk/INFO/gosper.txt)
  * [Understanding Bill Gosper's continued fraction arithmetic (implemented in Python)](https://hsinhaoyu.github.io/cont_frac/)

**æ¬é¡µé¢ä¸»è¦å å®¹è¯èªåæ[Continued fractions](https://cp-algorithms.com/algebra/continued-fractions.html)ï¼çæåè®®ä¸º CC-BY-SA 4.0ï¼å å®¹ææ¹å¨ï¼**

* * *

  1. èªç¶æ° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªæéæ åè¡¨ç¤ºï¼1 =[1] =[0,1]1=[1]=[0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Â â©

  2. è¯æè§ [ç»´åºç¾ç§é¡µé¢](https://en.wikipedia.org/wiki/Periodic_continued_fraction#Length_of_the_repeating_block) çåèæç®ï¼Â â©

  3. è¯åæ¥èªå¼ æå°§ãå¼ å¡ç¿»è¯çãå ·ä½æ°å­¦ãç¬¬ 6.7 èï¼Â â©

  4. æ­¤æ¶ä¸è½é»è®¤æ¢çº¦åæ° ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æ¯æ¸è¿åæ°ï¼è½ç¶ Legendre å®çè¡¨æ ððpq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¡®å®åªè½æ¯æä¸ªæ¸è¿åæ°ï¼å¯¹äºæ¸è¿åæ°çæ å½¢ï¼å¯ä»¥éè¿æ¸è¿åæ°é¼è¿å®æ°çè¯¯å·®å ¥æå ä»¥è¯æï¼Â â©

  5. ä¸åæç®å¯è½å¯¹æ­¤å¤ç ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼èå´æ¯å¦å æ¬ç«¯ç¹æä¸åçå¤çï¼Â â©

  6. ð¡ =0t=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼åºçè§£ä¸ºå½¢å¼è¿åæ°ï¼ç¸å½äºæªæ­å°è¿åæ°çåæ°ç¬¬äºé¡¹ï¼Â â©

  7. è¿äºæ§è´¨è¡¨æï¼å ¨ä½åå¼çº¿æ§åæ¢çç¾¤åæäº [å°å½±çº¿æ§ç¾¤](https://en.wikipedia.org/wiki/Projective_linear_group) ððºð¿2(ð)PGL2(R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Â â©

  8. å ³äºèªç¶å¯¹æ°çåº ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°å±å¼çè¯æå¯ä»¥åè [æ­¤å¤](https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Euler%27s_Number)ï¼Â â©

  9. æ­¤è¯´æ³å¹¶éä¸ä¸æ¯è¯­ï¼å¯è½è½¬è¯èªä¿ææç® [Ð¦ÐÐÐÐ«Ð ÐÐ ÐÐÐ](https://old.mccme.ru/free-books/mmmf-lectures/book.14-full.pdf)ï¼å¨ ÐÐ»Ð³Ð¾ÑÐ¸ÑÐ¼ Â«Ð²ÑÑÑÐ³Ð¸Ð²Ð°Ð½Ð¸Ñ Ð½Ð¾ÑÐ¾Ð²Â» ä¸èï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/continued-fraction.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/continued-fraction.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[c-forrest](https://github.com/c-forrest), [Great-designer](https://github.com/Great-designer), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [383494](https://github.com/383494), [CCXXXI](https://github.com/CCXXXI), [chunibyo-wly](https://github.com/chunibyo-wly), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [untitledunrevised](https://github.com/untitledunrevised), [Xeonacid](https://github.com/Xeonacid)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
