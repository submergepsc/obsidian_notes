# éä½æå - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/derangement/

# éä½æå

## éä½æå

### å®ä¹

éä½æåï¼derangementï¼æ¯æ²¡æä»»ä½å ç´ åºç°å¨å ¶æåºä½ç½®çæåï¼å³ï¼å¯¹äº 1 â¼ð1â¼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ææ»¡è¶³ ðð â ðPiâ i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç§° ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéä½æåï¼

ä¾å¦ï¼ä¸å éä½æåæ {2,3,1}{2,3,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å {3,1,2}{3,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå éä½æåæ {2,1,4,3}{2,1,4,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{2,3,4,1}{2,3,4,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{2,4,1,3}{2,4,1,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{3,1,4,2}{3,1,4,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{3,4,1,2}{3,4,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{3,4,2,1}{3,4,2,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{4,1,2,3}{4,1,2,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ã{4,3,1,2}{4,3,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å {4,3,2,1}{4,3,2,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼éä½æåæ¯æ²¡æä¸å¨ç¹çæåï¼å³æ²¡æé¿åº¦ä¸º 1 çå¾ªç¯ï¼

### å®¹æ¥åççè®¡ç®

å ¨é ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸º 1 â¼ð1â¼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæåï¼|ð| =ð!|U|=n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ððSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å ¶ä¸­æ»¡è¶³ ðð â ðPiâ i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæåï¼è¿ç¨è¡¥éå [å®¹æ¥åç](../inclusion-exclusion-principle/) çç¥è¯ï¼é®é¢åææ±ï¼

â£ðâð=1ððâ£=|ð|ââ£ðâð=1ââððâ£=ð!âðâð=1(â1)ðâ1âðð<ðð+1â£ðâð=1âââðððâ£|âi=1nSi|=|U|â|âi=1nSiâ|=n!ââk=1n(â1)kâ1âai<ai+1|âi=1kSaiâ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­æ±åçå«ä¹æ¯ 1,2,â¯,ð1,2,â¯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å ð1,ð2,â¯,ðða1,a2,â¯,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ»¡è¶³ ðð <ðð+1ai<ai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯

â£ðâð=1âââðððâ£|âi=1kSaiâ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¡¨ç¤ºæ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ° ð1,ð2,â¯,ðða1,a2,â¯,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ ððð =ððPai=ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå©ä¸ ð âðnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°çä½ç½®ä»»æçæåæ°ï¼å æ­¤ï¼

â£ðâð=1âââðððâ£=(ðâð)!|âi=1kSaiâ|=(nâk)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°çéæ©æ åµå ± (ðð)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§ï¼å¯¹å ¶æ±åæï¼

ðâð=1(â1)ðâ1âðð<ðð+1â£ðâð=1âââðððâ£=ðâð=1(â1)ðâ1(ðð)(ðâð)!=ðâð=1(â1)ðâ1ð!ð!=ð!ðâð=1(â1)ðâ1ð!âk=1n(â1)kâ1âai<ai+1|âi=1kSaiâ|=âk=1n(â1)kâ1(nk)(nâk)!=âk=1n(â1)kâ1n!k!=n!âk=1n(â1)kâ1k!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ çéä½æåæ°ä¸ºï¼

ð·ð=ð!âð!ðâð=1(â1)ðâ1ð!=ð!ðâð=0(â1)ðð!Dn=n!ân!âk=1n(â1)kâ1k!=n!âk=0n(â1)kk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éä½æåæ°åçåå é¡¹ä¸º 0,1,2,9,44,2650,1,2,9,44,265![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼[OEIS A000166](http://oeis.org/A000166)ï¼ï¼

### éæ¨çè®¡ç®

æéä½æåé®é¢å ·ä½åï¼èèè¿æ ·ä¸ä¸ªé®é¢ï¼

ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°ä¸åçä¿¡ï¼ç¼å·åå«æ¯ 1,2,3,4,51,2,3,4,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç°å¨è¦æè¿äºå°ä¿¡æ¾å¨ç¼å· 1,2,3,4,51,2,3,4,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¿¡å°ä¸­ï¼è¦æ±ä¿¡å°çç¼å·ä¸ä¿¡çç¼å·ä¸ä¸æ ·ï¼é®æå¤å°ç§ä¸åçæ¾ç½®æ¹æ³ï¼

åè®¾èèå°ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°ï¼åå§æ¶ææ¶æç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°ä¿¡æ¾å¨ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°ä¸­ï¼ç¶åèèä¸¤ç§æ åµçéæ¨ï¼

  * åé¢ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°å ¨é¨è£ éï¼
  * åé¢ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°æä¸ä¸ªæ²¡æè£ éå ¶ä½å ¨é¨è£ éï¼

å¯¹äºç¬¬ä¸ç§æ åµï¼åé¢ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°å ¨é¨è£ éï¼å ä¸ºåé¢ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå·²ç»å ¨é¨è£ éäºï¼æä»¥ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°åªéè¦ä¸åé¢ä»»ä¸ä¸ä¸ªä½ç½®äº¤æ¢å³å¯ï¼æ»å ±æ ð·ðâ1 Ã(ð â1)Dnâ1Ã(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§æ åµï¼

å¯¹äºç¬¬äºç§æ åµï¼åé¢ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°æä¸ä¸ªæ²¡æè£ éå ¶ä½å ¨é¨è£ éï¼èèè¿ç§æ åµçç®çå¨äºï¼è¥ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¿¡å°ä¸­å¦ææä¸ä¸ªæ²¡è£ éï¼é£ä¹æé£ä¸ªæ²¡è£ éçä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äº¤æ¢ï¼å³å¯å¾å°ä¸ä¸ªå ¨éä½æåæ åµï¼

å ¶ä»æ åµï¼ä¸å¯è½éè¿ä¸æ¬¡æä½æ¥æå®åæä¸ä¸ªé¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæï¼

äºæ¯å¯å¾ï¼éä½æåæ°æ»¡è¶³éæ¨å ³ç³»ï¼

ð·ð=(ðâ1)(ð·ðâ1+ð·ðâ2)Dn=(nâ1)(Dnâ1+Dnâ2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éä¹ç»åºå¦ä¸ä¸ªéæ¨å ³ç³»ï¼

ð·ð=ðð·ðâ1+(â1)ðDn=nDnâ1+(â1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å ¶ä»å ³ç³»

éä½æåæ°æä¸ä¸ªç®åçåæ´è¡¨è¾¾å¼ï¼å¢é¿éåº¦ä¸é¶ä¹ä» ç¸å·®å¸¸æ°ï¼

ð·ð=âð!e+12âDn=ân!e+12â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

éçå ç´ æ°éçå¢å ï¼å½¢æéä½æåçæ¦ç P æ¥è¿ï¼

ð=limðââð·ðð!=1eP=limnââDnn!=1e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/3/25 06:20:21ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/derangement.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/derangement.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [amlhdsan](https://github.com/amlhdsan), [BeiChenStanly](https://github.com/BeiChenStanly), [Enter-tainer](https://github.com/Enter-tainer), [untitledunrevised](https://github.com/untitledunrevised), [xzdeyg](https://github.com/xzdeyg)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
