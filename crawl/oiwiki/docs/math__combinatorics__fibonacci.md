# ææ³¢é£å¥æ°å - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/fibonacci/

# ææ³¢é£å¥æ°å

ææ³¢é£å¥æ°åï¼The Fibonacci sequenceï¼[OEIS A000045](http://oeis.org/A000045)ï¼çå®ä¹å¦ä¸ï¼

ð¹0=0,ð¹1=1,ð¹ð=ð¹ðâ1+ð¹ðâ2F0=0,F1=1,Fn=Fnâ1+Fnâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯¥æ°åçåå é¡¹å¦ä¸ï¼

0,1,1,2,3,5,8,13,21,34,55,89,â¦0,1,1,2,3,5,8,13,21,34,55,89,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## å¢å¡æ¯æ°å

å¢å¡æ¯æ°åï¼The Lucas sequenceï¼[OEIS A000032](http://oeis.org/A000032)ï¼çå®ä¹å¦ä¸ï¼

ð¿0=2,ð¿1=1,ð¿ð=ð¿ðâ1+ð¿ðâ2L0=2,L1=1,Ln=Lnâ1+Lnâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯¥æ°åçåå é¡¹å¦ä¸ï¼

2,1,3,4,7,11,18,29,47,76,123,199,â¦2,1,3,4,7,11,18,29,47,76,123,199,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç ç©¶ææ³¢é£å¥æ°åï¼å¾å¤æ¶åéè¦åå©å¢å¡æ¯æ°åä¸ºå·¥å ·ï¼

## ææ³¢é£å¥æ°åéé¡¹å ¬å¼

ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªææ³¢é£å¥æ°å¯ä»¥å¨ Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å ä½¿ç¨éæ¨å ¬å¼è®¡ç®ï¼ä½æä»¬ä»ææ´å¿«éçæ¹æ³è®¡ç®ï¼

### è§£æè§£

è§£æè§£å³å ¬å¼è§£ï¼æä»¬æææ³¢é£å¥æ°åçéé¡¹å ¬å¼ï¼Binet's Formulaï¼ï¼

ð¹ð=(1+â52)ðâ(1ââ52)ðâ5Fn=(1+52)nâ(1â52)n5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªå ¬å¼å¯ä»¥å¾å®¹æå°ç¨å½çº³æ³è¯æï¼å½ç¶ä¹å¯ä»¥éè¿çæå½æ°çæ¦å¿µæ¨å¯¼ï¼æè è§£ä¸ä¸ªæ¹ç¨å¾å°ï¼

å½ç¶ä½ å¯è½åç°ï¼è¿ä¸ªå ¬å¼åå­çç¬¬äºé¡¹æ»æ¯å°äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸å®ä»¥ææ°çº§çéåº¦åå°ï¼å æ­¤æä»¬å¯ä»¥æè¿ä¸ªå ¬å¼åæ

ð¹ð=â¡â¢ â¢ â¢â£(1+â52)ðâ5â¤â¥ â¥ â¥â¦Fn=[(1+52)n5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éçä¸­æ¬å·è¡¨ç¤ºåç¦»å®æè¿çæ´æ°ï¼

è¿ä¸¤ä¸ªå ¬å¼å¨è®¡ç®çæ¶åè¦æ±æé«çç²¾ç¡®åº¦ï¼å æ­¤å¨å®è·µä¸­å¾å°ç¨å°ï¼ä½æ¯è¯·ä¸è¦å¿½è§ï¼ç»åæ¨¡æä¹ä¸äºæ¬¡å©ä½åéå çæ¦å¿µï¼å¨ OI ä¸­ä½¿ç¨è¿ä¸ªå ¬å¼ä»æ¯æç¨çï¼

### å¢å¡æ¯æ°åéé¡¹å ¬å¼

æä»¬æå¢å¡æ¯æ°åçéé¡¹å ¬å¼ï¼

ð¿ð=(1+â52)ð+(1ââ52)ðLn=(1+52)n+(1â52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ææ³¢é£å¥æ°åéå¸¸ç¸ä¼¼ï¼äºå®ä¸æï¼

ð¿ð+ð¹ðâ52=(1+â52)ðLn+Fn52=(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼ð¿ðLn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¹ðFn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ°å¥½ææ (1+â52)ð(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºé¡¹å¼å±å¼ååå¹¶åç±»é¡¹åçåå­ç³»æ°ï¼ä¹å°±æ¯è¯´ï¼Pell æ¹ç¨

ð¥2â5ð¦2=â4x2â5y2=â4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå ¨ä½è§£ï¼æ°å¥½æ¯

ð¥ð+ð¦ðâ52=ð¿ð+ð¹ðâ52xn+yn52=Ln+Fn52![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ°å¥½æ¯å¢å¡æ¯æ°ååææ³¢é£å¥æ°åï¼å æ­¤æ

ð¿ð2â5ð¹ð2=â4Ln2â5Fn2=â4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ç©éµå½¢å¼

ææ³¢é£å¥æ°åçéæ¨å¯ä»¥ç¨ç©éµä¹æ³çå½¢å¼è¡¨è¾¾ï¼

[ð¹ðâ1ð¹ð]=[ð¹ðâ2ð¹ðâ1][0111][Fnâ1Fn]=[Fnâ2Fnâ1][0111]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ð =[0111]P=[0111]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å¾å°

[ð¹ðð¹ð+1]=[ð¹0ð¹1]ðð[FnFn+1]=[F0F1]Pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯æä»¬å¯ä»¥ç¨ç©éµä¹æ³å¨ Î(logâ¡ð)Î(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å è®¡ç®ææ³¢é£å¥æ°åï¼æ­¤å¤ï¼åä¸èè®²è¿°çå ¬å¼ä¹å¯éè¿ç©éµå¯¹è§åçæå·§æ¥å¾å°ï¼

### å¿«éåå¢æ³

ä½¿ç¨ä¸é¢çæ¹æ³æä»¬å¯ä»¥å¾å°ä»¥ä¸ç­å¼ï¼

ð¹2ð=ð¹ð(2ð¹ð+1âð¹ð)ð¹2ð+1=ð¹2ð+1+ð¹2ðF2k=Fk(2Fk+1âFk)F2k+1=Fk+12+Fk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯å¯ä»¥éè¿è¿æ ·çæ¹æ³å¿«éè®¡ç®ä¸¤ä¸ªç¸é»çææ³¢é£å¥æ°ï¼å¸¸æ°æ¯ç©ä¹å°ï¼ï¼ä»£ç å¦ä¸ï¼è¿åå¼æ¯ä¸ä¸ªäºå ç» (ð¹ð,ð¹ð+1)(Fn,Fn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text pair < int , int > fib ( int n ) { if ( n == 0 ) return { 0 , 1 }; auto p = fib ( n >> 1 ); int c = p . first * ( 2 * p . second \- p . first ); int d = p . first * p . first \+ p . second * p . second ; if ( n & 1 ) return { d , c \+ d }; else return { c , d }; } ```   
---|---  
  
## æ§è´¨

ææ³¢é£å¥æ°åæ¥æè®¸å¤æè¶£çæ§è´¨ï¼è¿éåä¸¾åºä¸é¨åç®åçæ§è´¨ï¼

  1. å¡è¥¿å°¼æ§è´¨ï¼Cassini's identityï¼ï¼ð¹ðâ1ð¹ð+1 âð¹2ð =( â1)ðFnâ1Fn+1âFn2=(â1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. éå æ§è´¨ï¼ð¹ð+ð =ð¹ðð¹ð+1 +ð¹ðâ1ð¹ðFn+k=FkFn+1+Fkâ1Fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. åä¸ä¸æ¡æ§è´¨ä¸­ ð =ðk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å¾å° ð¹2ð =ð¹ð(ð¹ð+1 +ð¹ðâ1)F2n=Fn(Fn+1+Fnâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. ç±ä¸ä¸æ¡æ§è´¨å¯ä»¥å½çº³è¯æï¼âð ââ,ð¹ð|ð¹ððâkâN,Fn|Fnk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  5. ä¸è¿°æ§è´¨å¯éï¼å³ âð¹ð|ð¹ð,ð|ðâFa|Fb,a|b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  6. GCD æ§è´¨ï¼(ð¹ð,ð¹ð) =ð¹(ð,ð)(Fm,Fn)=F(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  7. ä»¥ææ³¢é£å¥æ°åç¸é»ä¸¤é¡¹ä½ä¸ºè¾å ¥ä¼ä½¿æ¬§å éå¾·ç®æ³è¾¾å°æåå¤æåº¦ï¼å ·ä½åè§ [ç»´åº - ææ¢ ](https://en.wikipedia.org/wiki/Gabriel_Lam%C3%A9)ï¼ï¼

### ææ³¢é£å¥æ°åä¸å¢å¡æ¯æ°åçå ³ç³»

ä¸é¾åç°ï¼å ³äºå¢å¡æ¯æ°åä¸ææ³¢é£å¥æ°åçç­å¼ï¼ä¸ä¸è§å½æ°å ¬å¼å ·æå¾é«çç¸ä¼¼æ§ï¼æ¯å¦ï¼

ð¿ð+ð¹ðâ52=(1+â52)ðLn+Fn52=(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸

cosâ¡ðð¥+ðsinâ¡ðð¥=(cosâ¡ð¥+ðsinâ¡ð¥)ðcosâ¡nx+isinâ¡nx=(cosâ¡x+isinâ¡x)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¾åï¼ä»¥å

ð¿ð2â5ð¹ð2=â4Ln2â5Fn2=â4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸

cos2â¡ð¥+sin2â¡ð¥=1cos2â¡x+sin2â¡x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¾åï¼å æ­¤ï¼å¢å¡æ¯æ°åä¸ä½å¼¦å½æ°å¾åï¼èææ³¢é£å¥æ°åä¸æ­£å¼¦å½æ°å¾åï¼æ¯å¦ï¼æ ¹æ®

(1+â52)ð(1+â52)ð=(1+â52)ð+ð(1+52)m(1+52)n=(1+52)m+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥å¾å°ä¸¤ä¸æ ä¹åçç­å¼ï¼

2ð¿ð+ð=5ð¹ðð¹ð+ð¿ðð¿ð2Lm+n=5FmFn+LmLn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2ð¹ð+ð=ð¹ðð¿ð+ð¿ðð¹ð2Fm+n=FmLn+LmFn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯æ¨è®ºå°±æäºåä¸æ çç­å¼ï¼

ð¿2ð=ð¿ð2â2(â1)ðL2n=Ln2â2(â1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¹2ð=ð¹ðð¿ðF2n=FnLn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¹æ¯ä¸ç§å¿«éåå¢ä¸æ çåæ³ï¼åæ ·å°ï¼ä¹å¯ä»¥ä»¿ç §ä¸è§å½æ°çå ¬å¼ï¼æ¯å¦å¥å¶æ§ãåå·®åç§¯ãç§¯ååå·®ãåè§ãä¸è½ä»£æ¢ç­ç­ï¼æ¨çåºæ´å¤æå ³å¢å¡æ¯æ°åä¸ææ³¢é£å¥æ°åçç¸åºç­å¼ï¼

## ææ³¢é£å¥ç¼ç 

æä»¬å¯ä»¥å©ç¨ææ³¢é£å¥æ°åä¸ºæ­£æ´æ°ç¼ç ï¼æ ¹æ® [é½è¯å¤å¤«å®ç](https://zh.wikipedia.org/wiki/%E9%BD%8A%E8%82%AF%E5%A4%9A%E5%A4%AB%E5%AE%9A%E7%90%86)ï¼ä»»ä½èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¢«å¯ä¸å°è¡¨ç¤ºæä¸äºææ³¢é£å¥æ°çåï¼

ð=ð¹ð1+ð¹ð2+â¦+ð¹ððN=Fk1+Fk2+â¦+Fkr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¹¶ä¸ ð1 â¥ð2 +2,Â ð2 â¥ð3 +2,Â â¦,Â ðð â¥2k1â¥k2+2,Â k2â¥k3+2,Â â¦,Â krâ¥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ä¸è½ä½¿ç¨ä¸¤ä¸ªç¸é»çææ³¢é£å¥æ°ï¼

äºæ¯æä»¬å¯ä»¥ç¨ ð0ð1ð2â¦ðð 1d0d1d2â¦ds1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¼ç è¡¨ç¤ºä¸ä¸ªæ­£æ´æ°ï¼å ¶ä¸­ ðð =1di=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè¡¨ç¤º ð¹ð+2Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¢«ä½¿ç¨ï¼ç¼ç æ«ä½æä»¬å¼ºå¶ç»å®å ä¸ä¸ª 1ï¼è¿æ ·ä¼åºç°ä¸¤ä¸ªç¸é»ç 1ï¼ï¼è¡¨ç¤ºè¿ä¸ä¸²ç¼ç ç»æï¼ä¸¾å ä¸ªä¾å­ï¼

1=1=ð¹2=(11)ð¹2=2=ð¹3=(011)ð¹6=5+1=ð¹5+ð¹2=(10011)ð¹8=8=ð¹6=(000011)ð¹9=8+1=ð¹6+ð¹2=(100011)ð¹19=13+5+1=ð¹7+ð¹5+ð¹2=(1001011)ð¹1=1=F2=(11)F2=2=F3=(011)F6=5+1=F5+F2=(10011)F8=8=F6=(000011)F9=8+1=F6+F2=(100011)F19=13+5+1=F7+F5+F2=(1001011)F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç» ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¼ç çè¿ç¨å¯ä»¥ä½¿ç¨è´ªå¿ç®æ³è§£å³ï¼

  1. ä»å¤§å°å°æä¸¾ææ³¢é£å¥æ° ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´å° ð¹ð â¤ðFiâ¤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ç¼ç ç ð â2iâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½ç½®ä¸æ¾ä¸ä¸ª 1ï¼ç¼ç ä»å·¦å°å³ä»¥ 0 ä¸ºèµ·ç¹ï¼ï¼
  3. å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­£ï¼åå°æ­¥éª¤ 1ï¼
  4. æåå¨ç¼ç æ«ä½æ·»å ä¸ä¸ª 1ï¼è¡¨ç¤ºç¼ç çç»æä½ç½®ï¼

è§£ç è¿ç¨åçï¼å å ææ«ä½ç 1ï¼å¯¹äºç¼ç ä¸º 1 çä½ç½® ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¼ç ä»å·¦å°å³ä»¥ 0 ä¸ºèµ·ç¹ï¼ï¼ç´¯å ä¸ä¸ª ð¹ð+2Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°ç­æ¡ï¼æåçç­æ¡å°±æ¯åæ°å­ï¼

## æ¨¡æä¹ä¸å¨ææ§

å¯¹äºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸çææ³¢é£å¥æ°åï¼å¯ä»¥å®¹æå°ä½¿ç¨æ½å±åçè¯æï¼è¯¥æ°åæ¯æå¨ææ§çï¼ç±äºææ³¢é£å¥æ°æ¯ä¸é¡¹çè®¡ç®é½ä¾èµäºåä¸¤é¡¹çåå¼ï¼æä»¥éè¦ç¨ç¸é»ææ³¢é£å¥æ°ç»æçæ°å¯¹æè¿°æ°åå½ä¸æå¤çç¶æï¼èèæ¨¡æä¹ä¸å ð2 +1m2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªææ³¢é£å¥æ°å¯¹ï¼

(ð¹0,Â ð¹1),Â (ð¹1,Â ð¹2),Â â¦,Â (ð¹ð2,Â ð¹ð2+1)(F0,Â F1),Â (F1,Â F2),Â â¦,Â (Fm2,Â Fm2+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå©ä½ç³»å¤§å°ä¸º ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æå³çè³å¤åªå¯è½æ ð2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§äºä¸ç¸åçæ°å¯¹ï¼å æ­¤ï¼å¨å ð2 +1m2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°å¯¹ä¸­å¿ æä¸¤ä¸ªç¸åçæ°å¯¹ï¼äºæ¯ä»è¿ä¸¤ä¸ªæ°å¯¹å¯ä»¥å¾åçæç¸åçææ³¢é£å¥æ°åï¼é£ä¹ï¼ææ³¢é£å¥æ°åå°±æ¯å¨ææ§çï¼ä¸ï¼æå°æ­£ï¼å¨æä¸ä¼è¶ è¿ ð2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### Pisano å¨æ

æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ææ³¢é£å¥æ°åçæå°æ­£å¨æè¢«ç§°ä¸º **Pisano å¨æ** ï¼Pisano periodï¼ç®è¨è¯ºå¨æï¼[OEIS A001175](http://oeis.org/A001175)ï¼ï¼æ¬æä¸­ç¨ ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Pisano å¨æï¼

è¿ä¸è§å¯å¯ä»¥ç¨äºè®¡ç®ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ææ³¢é£å¥æ°æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éå¸¸å¤§ï¼å°±éè¦è®¡ç®ææ³¢é£å¥æ°æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¨æï¼å½ç¶ï¼åªéè¦è®¡ç®å¨æï¼ä¸ä¸å®æ¯æå°æ­£å¨æï¼

ä¸ºæ­¤ï¼æå¦ä¸ç»è®ºï¼

  1. å¯¹äºäºç´ çæ¨¡æ° ð1,ð2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð1ð2) =lcmâ¡(ð(ð1),ð(ð2))Ï(m1m2)=lcmâ¡(Ï(m1),Ï(m2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å¯¹äºç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ­£æ´æ° ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ðð) â£ððâ1ð(ð)Ï(pe)â£peâ1Ï(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. å¯¹äº ð =2ðÂ (ð âð+)m=2eÂ (eâN+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) =3 â 2ðâ1Ï(m)=3â 2eâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. å¯¹äº ð =5ðÂ (ð âð+)m=5eÂ (eâN+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) =4 â 5ðÏ(m)=4â 5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  5. æåï¼å¯¹äºç´ æ° ð â¡ Â±1(mod10)pâ¡Â±1(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) â£(ð â1)Ï(p)â£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºç´ æ° ð â¡ Â±3(mod10)pâ¡Â±3(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ð) â£2(ð +1)Ï(p)â£2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç»¼åè¿äºæ å½¢ï¼å¯ä»¥è¯´æï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Pisano å¨æä¸ä¼è¶ è¿ 6ð6m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç­å·å½ä¸ä» å½ ð =2 Ã5ðÂ (ð âð+)m=2Ã5eÂ (eâN+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶åå¾ï¼

å©ç¨ä¸è¿°ç»è®ºï¼å¯ä»¥åºäºç´ å æ°åè§£ç®æ³ï¼å¾å°å¦ä¸å¿«éè®¡ç® Pisano å¨æçæ¹æ³ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // Get a period of Fibonacci sequence mod m. // Not necessarily be the exact Pisano period. uint32_t calc_cycle_from_mod ( uint32_t m ) { uint32_t res = 1 ; for ( auto pe : factorize ( m )) { auto p = pe . first ; auto e = pe . second ; uint64_t cur = pow ( p , e \- 1 ); if ( p == 2 ) { cur *= 3 ; } else if ( p == 5 ) { cur *= 20 ; } else if ( p % 5 == 1 || p % 5 == 4 ) { cur *= p \- 1 ; } else { cur *= 2 * ( p \+ 1 ); } res = lcm ( res , cur ); } return res ; } ```   
---|---  
  
è¿æ ·å¾å°çå¨æå¯è½åªæ¯ Pisano å¨æçä¸ä¸ªåæ°ï¼è¦å¾å°ç²¾ç¡®ç Pisano å¨æï¼å¯ä»¥è¿ä¸æ­¥èå¯è¯¥å¨æçå æ°ï¼æè ï¼å¯ä»¥ç´æ¥éè¿ [BSGS ç®æ³](../../number-theory/discrete-logarithm/#å¤§æ­¥å°æ­¥ç®æ³) ä»¥ ð(âð)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦è®¡ç®ï¼

### è¯æ

æåï¼æ¬æç®è¦è¯æä¸è¿°å ³äº Pisano å¨æçç»è®ºï¼å¼å¾è¯´æçæ¯ï¼å©ç¨ä¸æè¯´æçæ¹æ³ï¼ç±»ä¼¼çç»è®ºå¯ä»¥æ¨å¹¿å°ä¸è¬çäºé¶å¸¸ç³»æ°çº¿æ§é½æ¬¡éæ¨æ°åï¼å°½ç®¡å ·ä½çå¸¸æ°ææå·®å¼ï¼è¿äºæ°åæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Pisano å¨æé½æ¯ ð(ð)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

ç¬¬ä¸ä¸ªè§å¯æ¯ï¼å©ç¨ [ä¸­å½å©ä½å®ç](../../number-theory/crt/)ï¼å¯ä»¥å°è®¨è®ºéå¶å¨ç´ æ°å¹æ¨¡çæ å½¢ï¼è®¾ ð1,ð2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸¤ä¸ªäºç´ çæ¨¡æ°ï¼ææ³¢é£å¥æ°åå¨æ¨¡ ð1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çå¨ææ¯ ð(ð1)Ï(m1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶åæ°ï¼å¨æ¨¡ ð2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çå¨ææ¯ ð(ð2)Ï(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶åæ°ï¼æä»¥å®å¨æ¨¡ ð1ð2m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çæå°æ­£å¨æåæ°ä¸º ð(ð1)Ï(m1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð(ð2)Ï(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å ¬åæ°ï¼è¿å°±æ¯åæçç»è®º 1ï¼

å¦ä¸ä¸ªè§å¯æ¯ï¼æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ç Pisano å¨æï¼å ¶å®æ¯æå°çæ­£æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾

ð´ð=(1110)ðâ¡ð¼(modð).Ak=(1110)kâ¡I(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¹å°±æ¯è¯´ï¼å®å ¶å®æ¯ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸1ç [é¶](../../algebra/group-theory/#é¶)ï¼

å¯¹äºç´ æ°å¹æ¨¡ ð =ððm=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å¯ä»¥éè¿ç»å ¸çåå¹è®ºè¯èç³»å°ç¸åºçç´ æ°æ¨¡çæ å½¢ï¼è®¾ ð =ð(ðð)k=Ï(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å­å¨äºé¶æ¹éµ ÎÎ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾

ð´ð=ððÎ+ð¼Ak=peÎ+I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç«ï¼æ èï¼ç± [äºé¡¹å¼å®ç](../combination/#äºé¡¹å¼å®ç) å¯ç¥

ð´ðð=(ððÎ+ð¼)ð=ð¼+ðâð=1(ðð)(ððÎ)ðâ¡ð¼(modðð+1).Akp=(peÎ+I)p=I+âi=1p(pi)(peÎ)iâ¡I(modpe+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ç± [é¶çæ§è´¨](../../number-theory/primitive-root/#å¹çå¾ªç¯ç»æ)ï¼æ ð(ðð+1) â£ðð =ðð(ðð)Ï(pe+1)â£kp=pÏ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½çº³å¯ç¥ï¼ð(ðð) â£ððâ1ð(ð)Ï(pe)â£peâ1Ï(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯æç«ï¼

å¯¹äºç´ æ°æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ¬æè®¨è®ºä¸¤ç§è¯ææ¹å¼ï¼

å©ç¨éé¡¹å ¬å¼å©ç¨æ©å

ä¸ç§æ¯å©ç¨ææ³¢é£å¥æ°åçéé¡¹å ¬å¼ï¼

ð¹ð=1â5(1+â52)ðâ1â5(1ââ52)ð.Fn=15(1+52)nâ15(1â52)n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°å®ç¨äºé¡¹å¼å®çå±å¼ï¼å¹¶æ¶å»æ ¹å¼é¡¹ï¼

ð¹ð=12ðâ1â(ðâ1)/2ââð=0(ð2ð+1)5ð.Fn=12nâ1âi=0â(nâ1)/2â(n2i+1)5i.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äº ð =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸è¡¨è¾¾å¼æ æ³ç´æ¥åæ¨¡ï¼ä½å¯ä»¥éªè¯å¯¹åºç Pisano å¨æä¸º ð(2) =3Ï(2)=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äº ð =5p=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð¹ð â¡ð â 3ðâ1(modð)Fnâ¡nâ 3nâ1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥ç´æ¥éªè¯å¯¹åºç Pisano å¨æä¸º ð(5) =20Ï(5)=20![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºå©ä½çå¥ç´ æ¨¡æ°ï¼å¯ä»¥åä¸ºä¸¤ç§æ å½¢ï¼

  * å¦æ ð â¡1,4(mod5)pâ¡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

ð¹ðâ¡12ðâ1(ðð)5(ðâ1)/2â¡1(modð),ð¹ð+1â¡12ð((ð+11)+(ð+1ð)5(ðâ1)/2)â¡1(modð).Fpâ¡12pâ1(pp)5(pâ1)/2â¡1(modp),Fp+1â¡12p((p+11)+(p+1p)5(pâ1)/2)â¡1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åç®è¿ç¨ä¸­ï¼å©ç¨äºå¦ä¸ç»è®ºï¼ç± [Lucas å®ç](../../number-theory/lucas/)ï¼å¯¹äº 0 <ð <ð0<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ (ðð) â¡0(modð)(pk)â¡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯¹äº 1 <ð <ð1<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ (ð+1ð) â¡0(modð)(p+1k)â¡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± [Fermat å°å®ç](../../number-theory/fermat/#è´¹é©¬å°å®ç)ï¼æ 2ðâ1 â¡5ðâ1 â¡1(modð)2pâ1â¡5pâ1â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äº ð â¡1,4(mod5)pâ¡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡å©ä½ï¼å©ç¨ [äºæ¬¡äºåå¾](../../number-theory/quad-residue/#äºæ¬¡äºåå¾)ï¼ä¹æ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡å©ä½ï¼æ è 5(ðâ1)/2 â¡1(modð)5(pâ1)/2â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼æ (ð¹ð,ð¹ð+1) â¡(ð¹1,ð¹2)(modð)(Fp,Fp+1)â¡(F1,F2)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ (ð â1)(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå¨æï¼æä»¥ï¼ð(ð) â£(ð â1)Ï(p)â£(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * å¦æ ð â¡2,3(mod5)pâ¡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ

ð¹2ðâ¡122ðâ1(2ðð)5(ðâ1)/2â¡â1(modð),ð¹2ð+1â¡122ð((2ð+11)+(2ð+1ð)5(ðâ1)/2+(2ð+12ð+1)5ð)â¡â1(modð).F2pâ¡122pâ1(2pp)5(pâ1)/2â¡â1(modp),F2p+1â¡122p((2p+11)+(2p+1p)5(pâ1)/2+(2p+12p+1)5p)â¡â1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åç®è¿ç¨ä¸­ï¼å©ç¨äºå¦ä¸ç»è®ºï¼ç± Lucas å®çï¼å¯¹äº 0 <ð <ð0<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð <ð <2ðp<k<2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ (ðð) â¡0(modð)(pk)â¡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥å (2ðð) â¡2(modð)(2pp)â¡2(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯¹äº 1 <ð <ð1<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð +1 <ð <2ðp+1<k<2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ (ðð) â¡0(modð)(pk)â¡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥å (2ð+1ð) â¡2(modð)(2p+1p)â¡2(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç± Fermat å°å®çï¼æ 2ðâ1 â¡5ðâ1 â¡1(modð)2pâ1â¡5pâ1â¡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äº ð â¡2,3(mod5)pâ¡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡éå©ä½ï¼å©ç¨äºæ¬¡äºåå¾ï¼ä¹æ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡éå©ä½ï¼æ è 5(ðâ1)/2 â¡ â1(modð)5(pâ1)/2â¡â1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼æ (ð¹2ð,ð¹2ð+1) â¡(ð¹â2,ð¹â1)(modð)(F2p,F2p+1)â¡(Fâ2,Fâ1)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ 2(ð +1)2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªå¨æï¼æä»¥ï¼ð(ð) â£2(ð +1)Ï(p)â£2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿å°±å®æäºè¯æï¼è¿ä¸æ¹æ³çå±éæ§å¨äºå®é«åº¦ä¾èµäºææ³¢é£å¥æ°åçéé¡¹å ¬å¼ï¼æä»¥è¾é¾ç´æ¥æ¨å¹¿å°ä¸è¬çæ å½¢ï¼

å¦ä¸ç§è¯ææ¹å¼åæ¯è¯å¾ç´æ¥è®¡ç®ç©éµ ð´ =(1110)A=(1110)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶ï¼å®ç [ç¹å¾å¤é¡¹å¼](../../linear-algebra/char-poly/) æ¯ ð(ð¥) =ð¥2 âð¥ â1f(x)=x2âxâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹åºçå¤å«å¼ä¸º Î =5Î=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºæ¨¡ ð =5p=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ Î â¡0(mod5)Îâ¡0(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¸¤ä¸ªç¸åç¹å¾å¼ ð =3Î»=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ä¸è½å¯¹è§åï¼éè¦åç¬è®¡ç®ï¼å¯¹äºæ¨¡ ð â¡1,4(mod5)pâ¡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºæ¬¡äºåå¾å¯ç¥ï¼å¤å«å¼ Î =5Î=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡å©ä½ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨å ð ðFp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æä¸¤ä¸ªç¸å¼ç¹å¾å¼ ð1 â ð2Î»1â Î»2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶å°±æ¯ lcmâ¡(ordâ¡(ð1),ordâ¡(ð2))lcmâ¡(ordâ¡(Î»1),ordâ¡(Î»2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ ç¶æ´é¤ |ð Ãð| =ð â1|FpÃ|=pâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºæ¨¡ ð â¡2,3(mod5)pâ¡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äºæ¬¡äºåå¾å¯ç¥ï¼å¤å«å¼ Î =5Î=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºæ¬¡éå©ä½ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨å ð ðFp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ²¡æç¹å¾å¼ï¼èåªæå¨ [æ©å](../../algebra/field-theory/#åçæ©å¼) ð ð[â5]Fp[5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ææä¸¤ä¸ªç¸å¼ç¹å¾å¼ ð1 â ð2Î»1â Î»2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº Frobenius èªåæ ð¥ â¦ð¥ðxâ¦xp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°ä¸¤æ ¹äº¤æ¢ï¼æ ð2 =ðð1Î»2=Î»1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ è ðð+11 =ðð+12 =ð1ð2 = â1Î»1p+1=Î»2p+1=Î»1Î»2=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äº¦å³ ð2(ð+1)1 =ð2(ð+1)2 =1Î»12(p+1)=Î»22(p+1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¶å°±æ¯ lcmâ¡(ordâ¡(ð1),ordâ¡(ð2))lcmâ¡(ordâ¡(Î»1),ordâ¡(Î»2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¿ ç¶æ´é¤ 2(ð +1)2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±å¾å°äºä¸åç§æ¹æ³ä¸è´çç»è®ºï¼

ç»¼ä¸ï¼å¯¹äºä¸åçæ å½¢ï¼ç¸åºå°æï¼

  * ð(2ð) =32 â 2ð,Â 14ð(5ð) =5ðÏ(2e)=32â 2e,Â 14Ï(5e)=5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å½ ð â¡ Â±1(mod10)pâ¡Â±1(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ð(ðð) â£(ð â1)ððâ1Ï(pe)â£(pâ1)peâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ð(ðð) â¤ððÏ(pe)â¤pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å½ ð â¡ Â±3(mod10)pâ¡Â±3(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼14ð(ðð) â£ð+12ððâ114Ï(pe)â£p+12peâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ 14ð(ðð) â¤ðð14Ï(pe)â¤pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æä»¥ï¼å©ç¨ç»è®º 1ï¼å¯¹äºä¸è¬çæ¨¡æ° ð =âðððððm=âipiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð(ð)=lcmâ¡{ð(ðððð):ððâð}â¤lcmâ¡{ð(ðððð):ðð=2Â orÂ ððâ¡Â±1Â (modâ¡10)}â 4â lcmâ¡{ð(ðððð)/4:ðð=5Â orÂ ððâ¡Â±3Â (modâ¡10)}â¤â{ð(ðððð):ðð=2Â orÂ ððâ¡Â±1Â (modâ¡10)}â 4â â{ð(ðððð)/4:ðð=5Â orÂ ððâ¡Â±3Â (modâ¡10)}â¤32â â{ðððð:ðð=2Â orÂ ððâ¡Â±1Â (modâ¡10)}â 4â â{ðððð:ðð=5Â orÂ ððâ¡Â±3Â (modâ¡10)}=6ð.Ï(m)=lcmâ¡{Ï(piei):piâP}â¤lcmâ¡{Ï(piei):pi=2Â orÂ piâ¡Â±1Â (modâ¡10)}â 4â lcmâ¡{Ï(piei)/4:pi=5Â orÂ piâ¡Â±3Â (modâ¡10)}â¤â{Ï(piei):pi=2Â orÂ piâ¡Â±1Â (modâ¡10)}â 4â â{Ï(piei)/4:pi=5Â orÂ piâ¡Â±3Â (modâ¡10)}â¤32â â{piei:pi=2Â orÂ piâ¡Â±1Â (modâ¡10)}â 4â â{piei:pi=5Â orÂ piâ¡Â±3Â (modâ¡10)}=6m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±è¯´æäºææ³¢é£å¥æ°åæ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Pisano å¨ææ»æ¯ä¸è¶ è¿ 6ð6m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ç­å·å½ä¸ä» å½å¨ ð =2 â 5ðm=2â 5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤åå¾ï¼

## ä¹ é¢

  * [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
  * [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
  * [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
  * [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
  * [æ´è°· P4000 ææ³¢é£å¥æ°å](https://www.luogu.com.cn/problem/P4000)

## åèæç®ä¸æ³¨é

  * [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
  * [Zeckendorf's theorem - Wikipedia](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
  * [Pisano period - Wikipedia](https://en.wikipedia.org/wiki/Pisano_period)

**æ¬é¡µé¢ä¸»è¦è¯èªåæ[Ð§Ð¸ÑÐ»Ð° Ð¤Ð¸Ð±Ð¾Ð½Ð°ÑÑÐ¸](http://e-maxx.ru/algo/fibonacci_numbers) ä¸å ¶è±æç¿»è¯ç [Fibonacci Numbers](https://cp-algorithms.com/algebra/fibonacci-numbers.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼å å®¹ææ¹å¨ï¼**

* * *

  1. ä¸¥æ ¼æ¥è¯´ï¼å®æ¯ç©éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ä¸è¬çº¿æ§ç¾¤ ðºð¿2(ðð)GL2(Zm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çé¶ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/2/1 11:46:32ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/fibonacci.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/fibonacci.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Great-designer](https://github.com/Great-designer), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [jifbt](https://github.com/jifbt), [Chrogeek](https://github.com/Chrogeek), [Enter-tainer](https://github.com/Enter-tainer), [EntropyIncreaser](https://github.com/EntropyIncreaser), [FFjet](https://github.com/FFjet), [gsjz](https://github.com/gsjz), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [Junyan721113](https://github.com/Junyan721113), [ouuan](https://github.com/ouuan), [untitledunrevised](https://github.com/untitledunrevised), [Xeonacid](https://github.com/Xeonacid)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
