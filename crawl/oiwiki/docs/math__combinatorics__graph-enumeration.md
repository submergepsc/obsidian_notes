# å¾è®ºè®¡æ° - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/graph-enumeration/

# å¾è®ºè®¡æ°

å¨ç»åæ°å­¦ä¸­ï¼å¾è®ºè®¡æ°ï¼Graph Enumerationï¼æ¯ç ç©¶æ»¡è¶³ç¹å®æ§è´¨çå¾çè®¡æ°é®é¢çåæ¯ï¼[çæå½æ°](../../poly/intro/)ã[æ³¢å©äºè®¡æ°å®ç](../polya/) ä¸ [ç¬¦å·åæ¹æ³](../../poly/symbolic-method/#%E9%9B%86%E5%90%88%E7%9A%84-cycle-%E6%9E%84%E9%80%A0) å [OEIS](https://oeis.org/) æ¯è§£å³è¿ç±»é®é¢æ¶æéè¦çæ°å­¦å·¥å ·ï¼å¾è®ºè®¡æ°å¯åä¸ºææ å·åæ æ å·ä¸¤å¤§ç±»é®é¢ï¼å¤§å¤æ°æ åµä¸1ææ å·çæ¬çé®é¢é½æ¯å ¶å¯¹åºçæ æ å·é®é¢æ´å ç®åï¼å æ­¤æä»¬å°å èå¯ææ å·é®é¢çè®¡æ°ï¼

## ææ å·æ 

å³ Cayley å ¬å¼ï¼åè§ [PrÃ¼fer åºå](../../../graph/prufer/) ä¸æï¼æä»¬ä¹å¯ä»¥ä½¿ç¨ [Kirchhoff ç©éµæ å®ç](../../../graph/matrix-tree/) æ [çæå½æ°](../../poly/intro/#çæå½æ°) å [ææ ¼ææ¥å®ç](https://codeforces.com/blog/entry/104184) å¾å°è¿ä¸ç»æï¼

### ä¹ é¢

  * [Hihocoder 1047. Random Tree](https://vjudge.net/problem/HihoCoder-1047)

## ææ å·è¿éå¾

### ä¾é¢ãPOJ 1737ãConnected Graph

ä¾é¢ [ãPOJ 1737ãConnected Graph](http://poj.org/problem?id=1737)

é¢ç®å¤§æï¼æ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹çææ å·è¿éå¾çæ¹æ¡æ°ï¼ð â¤50nâ¤50![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

è¿ç±»é®é¢ææ©åºç°äºæ¥¼æä¸»çç·äººå «é¢ç³»åä¸­ï¼æä»¬è®¾ ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹ææ å·å¾çæ¹æ¡æ°ï¼ððcn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¾ æ±åºåï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç¹çå¾è³å¤æ (ð2)(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¡è¾¹ï¼æ¯æ¡è¾¹æ ¹æ®å ¶åºç°ä¸å¦æä¸¤ç§ç¶æï¼æ¯ç§ç¶æä¹é´ç¬ç«ï¼å èæ ðð =2(ð2)gn=2(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬åºå®å ¶ä¸­ä¸ä¸ªèç¹ï¼æä¸¾å ¶æå¨è¿éåçå¤§å°ï¼é£ä¹è¿éè¦ä»å©ä¸ç ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªèç¹ä¸­éæ© ð â1iâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªèç¹ç»æä¸ä¸ªè¿éåï¼è¿éåä¹å¤çèç¹å¯ä»¥ä»»æè¿è¾¹ï¼å èæå¦ä¸éæ¨å ³ç³»ï¼

ðâð=1(ðâ1ðâ1)ððððâð=ðððð=ððâðâ1âð=1(ðâ1ðâ1)ððððâðâi=1n(nâ1iâ1)cignâi=gncn=gnââi=1nâ1(nâ1iâ1)cignâi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç§»é¡¹å¾å° ððcn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåç ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éæ¨å ¬å¼ï¼å¯ä»¥éè¿æ­¤é¢ï¼

### ä¾é¢ãéè®­éä½ä¸ 2013ãåå¸è§å

ä¾é¢ [ãéè®­éä½ä¸ 2013ãåå¸è§å](https://www.luogu.com.cn/problem/P4841)

é¢ç®å¤§æï¼æ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹çææ å·è¿éå¾çæ¹æ¡æ°ï¼ð â¤130000nâ¤130000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

å¯¹äºæ°æ®èå´æ´å¤§çåºåé®é¢ï¼å¾å¾æä»¬éè¦æé è¿äºåºåççæå½æ°ï¼ä»¥ä½¿ç¨é«æçå¤é¡¹å¼ç®æ³ï¼

#### æ¹æ³ä¸ï¼åæ²» FFT

ä¸è¿°çéæ¨å¼å¯ä»¥çä½ä¸ç§èªå·ç§¯å½¢å¼ï¼å èå¯ä»¥ä½¿ç¨åæ²» FFT è¿è¡è®¡ç®ï¼å¤æåº¦ ð(ðlog2â¡ð)O(nlog2â¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### æ¹æ³äºï¼å¤é¡¹å¼æ±é

æä»¬å°ä¸è¿°éæ¨å¼ä¸­çç»åæ°å±å¼ï¼å¹¶è¿è¡åå½¢ï¼

ðâð=1(ðâ1ðâ1)ððððâð=ðððâð=1ðð(ðâ1)!ððâð(ðâð)!=ðð(ðâ1)!âi=1n(nâ1iâ1)cignâi=gnâi=1nci(iâ1)!gnâi(nâi)!=gn(nâ1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æé å¤é¡¹å¼ï¼

ð¶(ð¥)=âð=1ðð(ðâ1)!ð¥ððº(ð¥)=âð=0ððð!ð¥ðð»(ð¥)=âð=1ðð(ðâ1)!ð¥ðC(x)=ân=1cn(nâ1)!xnG(x)=ân=0gnn!xnH(x)=ân=1gn(nâ1)!xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£æ¢è¿ä¸å¼å¾å° ð¶ðº =ð»CG=H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿ç¨ [å¤é¡¹å¼æ±é](../../poly/elementary-func/#%E5%A4%9A%E9%A1%B9%E5%BC%8F%E6%B1%82%E9%80%86) ååå·ç§¯è§£åº ð¶(ð¥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

#### æ¹æ³ä¸ï¼å¤é¡¹å¼ exp

å¦ä¸ç§åæ³æ¯ä½¿ç¨ [EGF ä¸­å¤é¡¹å¼ exp çç»åæä¹](../../poly/egf/#egf-%E4%B8%AD%E5%A4%9A%E9%A1%B9%E5%BC%8F-exp-%E7%9A%84%E7%BB%84%E5%90%88%E6%84%8F%E4%B9%89)ï¼æä»¬è®¾ææ å·è¿éå¾åç®åå¾åºåç EGF åå«ä¸º ð¶(ð¥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðº(ð¥)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å®ä»¬å°æä¸åå ³ç³»ï¼

expâ¡(ð¶(ð¥))=ðº(ð¥)ð¶(ð¥)=lnâ¡(ðº(ð¥))expâ¡(C(x))=G(x)C(x)=lnâ¡(G(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½¿ç¨ [å¤é¡¹å¼ ln](../../poly/elementary-func/#å¤é¡¹å¼å¯¹æ°å½æ°--ææ°å½æ°) è§£åº ð¶(ð¥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

## ææ å·æ¬§æå¾ãäºåå¾

### ä¾é¢ãSPOJ KPGRAPHSãCounting Graphs

ä¾é¢ [ãSPOJ KPGRAPHSãCounting Graphs](http://www.spoj.com/problems/KPGRAPHS/)

é¢ç®å¤§æï¼æ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹çåå«æ»¡è¶³ä¸åæ§è´¨çææ å·å¾çæ¹æ¡æ°ï¼ð â¤1000nâ¤1000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

  * è¿éå¾ [A001187](https://oeis.org/A001187)ï¼
  * æ¬§æå¾ [A033678](https://oeis.org/A033678)ï¼
  * äºåå¾ [A047864](https://oeis.org/A047864)ï¼

æ¬é¢éå¶ä»£ç é¿åº¦ï¼å èæ æ³ç´æ¥ä½¿ç¨å¤é¡¹å¼æ¨¡æ¿ï¼ä½çæå½æ°ä¾ç¶å¯ä»¥å¸®å©æä»¬è¿è¡åæï¼

è¿éå¾é®é¢å¨ä¹åçä¾é¢ä¸­å·²è¢«è§£å³ï¼èèæ¬§æå¾ï¼æ³¨æå°ä¸è¿°å¯¹è¿éå¾è®¡æ°çå ç§æ¹æ³ï¼åå¯ä»¥å¨æ»¡è¶³ä»»ææ§è´¨çææ å·è¿éå¾è¿è¡æ¨å¹¿ï¼ä¾å¦æä»¬å¯ä»¥å°è¿éå¾éæ¨å ¬å¼ä¸­ç ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»ä»»æå¾æ¿æ¢ææ»¡è¶³é¡¶ç¹åº¦æ°åä¸ºå¶æ°çå¾ï¼æ­¤æ¶å¾å°ç ððcn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ä¸ºæ¬§æå¾ï¼

æä»¬å° POJ 1737 çéæ¨è¿ç¨å°è£ æè¿éåå½æ°ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text void ln ( Int C [], Int G []) { for ( int i = 1 ; i <= n ; ++ i ) { C [ i ] = G [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) C [ i ] -= binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } ```   
---|---  
  
åä¸¤é®å³å¯è½»æ¾è§£å³ï¼

```text 1 2 3 4 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i ][ 2 ]); ln ( C , G ); for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i \- 1 ][ 2 ]); ln ( E , G ); ```   
---|---  
  
æ³¨æå°è¿éçè¿éåéæ¨è¿ç¨å ¶å®ç­ä»·äºå¯¹å ¶ EGF æ±å¤é¡¹å¼ lnï¼åçæä»¬ä¹å¯ä»¥ååºéè¿éåå½æ°ï¼å®ç­ä»·äºå¯¹å ¶ EGF æ±å¤é¡¹å¼ expï¼

```text 1 2 3 4 5 6 7 ``` |  ```text void exp ( Int G [], Int C []) { for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = C [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) G [ i ] += binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } ```   
---|---  
  
ä¸é¢è®¨è®ºææ å·äºåå¾è®¡æ°ï¼

æä»¬è®¾ ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º n ä¸ªç»ç¹çäºåå¾æ¹æ¡æ°ï¼ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç»ç¹å¯¹ç»ç¹è¿è¡ 2 æè²ï¼æ»¡è¶³ç¸åé¢è²çç»ç¹ä¹é´ä¸å­å¨è¾¹çå¾çæ¹æ¡æ°ï¼æä¸¾å ¶ä¸­ä¸ç§é¢è²èç¹çæ°éï¼æ2ï¼

ðð=ðâð=0(ðð)2ð(ðâð)gn=âi=0n(ni)2i(nâi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¥ä¸æ¥æä»¬ç¨ä¸¤ç§ä¸åçæ¹æ³å»ºç« ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çå ³ç³»ï¼

#### æ¹æ³ä¸ï¼ç®ä¸¤æ¬¡

æä»¬è®¾ ðð,ðcn,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºæ k ä¸ªè¿éåéçäºåå¾æ¹æ¡æ°ï¼é£ä¹ä¸é¾å¾å°å¦ä¸å ³ç³»ï¼

ðð=ðâð=1ðð,ððð=ðâð=1ðð,ð2ðbn=âi=1ncn,ign=âi=1ncn,i2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¯è¾ä¸¤ç§ ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼å±å¼å¾ï¼

ðâð=0(ðð)2ð(ðâð)=ðâð=1ðð,ð2ððð,ð=âð=0ðâ1(ðâ1ðâ1)ðð,1ððâð,ðâ1âi=0n(ni)2i(nâi)=âi=1ncn,i2icn,i=âi=0nâ1(nâ1iâ1)cn,1cnâi,kâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸é¾å¾å° ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨å ³ç³»ï¼å¤æåº¦ ð(ð3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ­¥ä½¿ç¨å®¹æ¥åçï¼å¯ä»¥ä¼åå° ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿æ¬é¢ï¼

#### æ¹æ³äºï¼è¿éåéæ¨

æ¹æ³äºåæ¹æ³ä¸åä½¿ç¨è¿éäºåå¾ ð1ðb1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) [A001832](https://oeis.org/A001832) æ¥å»ºç« ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çæ¡¥æ¢ï¼

æ³¨æå°å¯¹äºæ¯ä¸ªè¿éäºåå¾ï¼æä»¬æ°å¥½æä¸¤ç§ä¸åçæè²æ¹æ³ï¼å¯¹åºå°ä¸¤ç»ä¸åçè¿é 2 æè²å¾ï¼ å èå¯¹ ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡è¿éåï¼å¾å°çåºåæ°å¥½æ¯ ð1ðb1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸¤åï¼è ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç± ð1ðb1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡éè¿éåå¾å°ï¼

å æ­¤ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = 0 ; for ( int j = 0 ; j < i \+ 1 ; ++ j ) G [ i ] += binom [ i ][ j ] * pow ( 2 , j * ( i \- j )); } ln ( B1 , G ); for ( int i = 1 ; i <= n ; ++ i ) B1 [ i ] /= 2 ; exp ( B , B1 ); ```   
---|---  
  
ä¸¤ç§éæ¨çè¿ç¨å¤æåº¦åä¸º ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥éè¿æ¬é¢ï¼

#### æ¹æ³ä¸ï¼å¤é¡¹å¼ exp

æä»¬æ³¨æå°ä¹å¯ä»¥ä½¿ç¨ EGF çè§£ä¸é¢çéæ¨è¿ç¨ï¼

è®¾ ðº(ð¥)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ððgn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç EGFï¼ðµ1(ð¥)B1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð1ðb1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç EGFï¼ðµ(ð¥)B(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ððbn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç EGFï¼åºç¨åæ³äºçæ¹æ³ï¼æä»¬æï¼

ðº(ð¥)=expâ¡(2ðµ1(ð¥))ðµ(ð¥)=expâ¡(ðµ1(ð¥))=expâ¡(lnâ¡ðº(ð¥)2)=âðºG(x)=expâ¡(2B1(x))B(x)=expâ¡(B1(x))=expâ¡(lnâ¡G(x)2)=G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬å¯ä»¥å¯¹ç­å¼ä¸¤è¾¹åå«è¿è¡æ±å¯¼å¹¶æ¯è¾ä¸¤è¾¹ç³»æ°ï¼ä»¥å¾å°æäºç¼ç çéæ¨å ¬å¼ï¼éè¿æ­¤é¢ï¼ æ³¨æå°åæ³äºä¸åæ³ä¸æ¬è´¨ç¸åï¼ä¸ä¸è¬æ åµä¸åæ³ä¸å¯ä»¥å¾å°æ´ä¼çæ¶é´å¤æåº¦ï¼

ðµ2ð=ðº2ðµððµâ²ð=ðºâ²Bn2=G2BnBnâ²=Gâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 ``` |  ```text #include <iostream> using namespace std ; using LL = long long ; constexpr int MOD = int ( 1e9 ) \+ 7 ; // <<= '2. Number Theory .,//{ namespace NT { void INC ( int & a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; } int sum ( int a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; return a ; } void DEC ( int & a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; } int dff ( int a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; return a ; } void MUL ( int & a , int b ) { a = ( LL ) a * b % MOD ; } int pdt ( int a , int b ) { return ( LL ) a * b % MOD ; } int _I ( int b ) { int a = MOD , x1 = 0 , x2 = 1 , q ; while ( 1 ) { q = a / b , a %= b ; if ( ! a ) return x2 ; DEC ( x1 , pdt ( q , x2 )); q = b / a , b %= a ; if ( ! b ) return x1 ; DEC ( x2 , pdt ( q , x1 )); } } void DIV ( int & a , int b ) { MUL ( a , _I ( b )); } int qtt ( int a , int b ) { return pdt ( a , _I ( b )); } int pow ( int a , LL b ) { int c ( 1 ); while ( b ) { if ( b & 1 ) MUL ( c , a ); MUL ( a , a ), b >>= 1 ; } return c ; } template < class T > T pow ( T a , LL b ) { T c ( 1 ); while ( b ) { if ( b & 1 ) c *= a ; a *= a , b >>= 1 ; } return c ; } template < class T > T pow ( T a , int b ) { return pow ( a , ( LL ) b ); } struct Int { int val ; operator int () const { return val ; } Int ( int _val = 0 ) : val ( _val ) { val %= MOD ; if ( val < 0 ) val += MOD ; } Int ( LL _val ) : val ( _val ) { _val %= MOD ; if ( _val < 0 ) _val += MOD ; val = _val ; } Int & operator += ( const int & rhs ) { INC ( val , rhs ); return * this ; } Int operator \+ ( const int & rhs ) const { return sum ( val , rhs ); } Int & operator -= ( const int & rhs ) { DEC ( val , rhs ); return * this ; } Int operator \- ( const int & rhs ) const { return dff ( val , rhs ); } Int & operator *= ( const int & rhs ) { MUL ( val , rhs ); return * this ; } Int operator * ( const int & rhs ) const { return pdt ( val , rhs ); } Int & operator /= ( const int & rhs ) { DIV ( val , rhs ); return * this ; } Int operator / ( const int & rhs ) const { return qtt ( val , rhs ); } Int operator \- () const { return MOD \- * this ; } }; } // namespace NT using namespace NT ; constexpr int N = int ( 1e3 ) \+ 9 ; Int binom [ N ][ N ], C [ N ], E [ N ], B [ N ], B1 [ N ], G [ N ]; int n ; void ln ( Int C [], Int G []) { for ( int i = 1 ; i <= n ; ++ i ) { C [ i ] = G [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) C [ i ] -= binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } void exp ( Int G [], Int C []) { for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = C [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) G [ i ] += binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); n = 1000 ; for ( int i = 0 ; i < n \+ 1 ; ++ i ) { binom [ i ][ 0 ] = 1 ; for ( int j = 0 ; j < i ; ++ j ) binom [ i ][ j \+ 1 ] = binom [ i \- 1 ][ j ] \+ binom [ i \- 1 ][ j \+ 1 ]; } for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i ][ 2 ]); ln ( C , G ); for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i \- 1 ][ 2 ]); ln ( E , G ); for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = 0 ; for ( int j = 0 ; j < i \+ 1 ; ++ j ) G [ i ] += binom [ i ][ j ] * pow ( 2 , j * ( i \- j )); } ln ( B1 , G ); for ( int i = 1 ; i <= n ; ++ i ) B1 [ i ] /= 2 ; exp ( B , B1 ); int T ; cin >> T ; while ( T \-- ) { cin >> n ; cout << "Connected: " << C [ n ] << '\n' << "Eulerian: " << E [ n ] << '\n' << "Bipartite: " << B [ n ] << " \n\n " ; } } ```   
---|---  
  
### ä¹ é¢

  * [UOJ Goodbye Jihai D. æ°å¹´çè¿½éæ](https://uoj.ac/contest/50/problem/498)
  * [BZOJ 3864. å¤§æååå¤åæ ](https://hydro.ac/p/bzoj-P3864)
  * [BZOJ 2863. æ¤æçå é¦](https://hydro.ac/p/bzoj-P2863)
  * [Luogu P6295. ææ å· DAG è®¡æ°](https://www.luogu.com.cn/problem/P6295)
  * [LOJ 6569. ä»äººæè®¡æ°](https://loj.ac/p/6569)
  * [LOJ 6570. æ¯æ¯è«è®¡æ°](https://loj.ac/p/6570)
  * [Luogu P5434. ææ å·èæ¼ è®¡æ°](https://www.luogu.com.cn/problem/P5434)
  * [Luogu P3343. [ZJOI2015] å°éåçå¹»æ³ä¹¡](https://www.luogu.com.cn/problem/P3343)
  * [HDU 5279. YJC plays Minecraft](https://acm.hdu.edu.cn/showproblem.php?pid=5279)
  * [Luogu P7364. ææ å·äºåå¾è®¡æ°](https://www.luogu.com.cn/problem/P7364)
  * [Luogu P5827. ç¹åè¿éå¾è®¡æ°](https://www.luogu.com.cn/problem/P5827)
  * [Luogu P5827. è¾¹åè¿éå¾è®¡æ°](https://www.luogu.com.cn/problem/P5828)
  * [Luogu P6596. How Many of Them](https://www.luogu.com.cn/problem/P6596)
  * [Luogu U152448. ææ å·å¼ºè¿éå¾è®¡æ°](https://www.luogu.com.cn/problem/U152448)
  * [Project Euler 434. Rigid graphs](https://projecteuler.net/problem=434)

## Riddell's Formula

ä¸è¿°å ³äº EGF ç exp çç¨æ³ï¼ææ¶åè¢«ç§°ä½ Riddell's formula for labeled graphsï¼çæå½æ°ç [æ¬§æåæ¢](../../poly/symbolic-method/#%E9%9B%86%E5%90%88%E7%9A%84-multiset-%E6%9E%84%E9%80%A0)ï¼ææ¶ä¹è¢«ç§°ä¸º Riddell's formula for unlabeled graphsï¼åè ææ©åºç°å¨æ¬§æå¯¹åææ°çç ç©¶ä¸­ï¼é¤äºè§£å³å¾è®ºè®¡æ°é®é¢ä¹å¤ï¼ä¹å¨å®å ¨èå é®é¢ä¸­åºç°ï¼

å¯¹äºç»å®åºå ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯¹åºç OGF ð´(ð¥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹ ð´(ð¥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬§æåæ¢ä¸ºï¼

E(ð´(ð¥))=âð(1âð¥ð)âðð=expâ¡(âðð´(ð¥ð)ð)E(A(x))=âi(1âxi)âai=expâ¡(âiA(xi)i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ E(ð´(ð¥))E(A(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåé¡¹ç³»æ°ä¸º ððbi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹è¾ å©æ°ç» ðð =âð|ððððci=âd|ndad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæéæ¨å ¬å¼

ððð=ðð+ðâ1âð=1ððððâðnbn=cn+âi=1nâ1cibnâi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## æ æ å·æ 

### ä¾é¢ãSPOJ PT07DãLet us count 1 2 3

ä¾é¢ [ãSPOJ PT07DãLet us count 1 2 3](https://www.spoj.com/problems/PT07D/)

é¢ç®å¤§æï¼æ±æ n ä¸ªç»ç¹çåå«æ»¡è¶³ä¸åæ§è´¨çæ çæ¹æ¡æ°ï¼

  * ææ å·ææ ¹æ  [A000169](https://oeis.org/A000169)ï¼
  * ææ å·æ æ ¹æ  [A000272](https://oeis.org/A000272)ï¼
  * æ æ å·ææ ¹æ  [A000081](https://oeis.org/A000081)ï¼
  * æ æ å·æ æ ¹æ  [A000055](https://oeis.org/A000055)ï¼

#### ææ ¹æ 

ææ å·æ åµä»¥å¨åæä¸­è§£å³ï¼ä¸é¢èå¯æ æ å·ææ ¹æ ï¼è®¾å ¶ OGF ä¸º ð¹(ð¥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºç¨æ¬§æåæ¢ï¼å¯å¾ï¼

ð¹(ð¥)=ð¥E(ð¹(ð¥))F(x)=xE(F(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ååºç³»æ°å³å¯ï¼

#### æ æ ¹æ 

èèå®¹æ¥ï¼æä»¬ç¨ææ ¹æ çæ¹æ¡ä¸­åå»æ ¹ä¸æ¯éå¿çæ¹æ¡ï¼å¹¶å¯¹ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¥å¶æ§è¿è¡è®¨è®ºï¼

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°æ¶ï¼

å¿ ç¶å­å¨ä¸æ£µå­æ å¤§å° â¥âð2ââ¥ân2â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä¸¾è¿æ£µå­æ çå¤§å°æï¼

ðð=ððâðâ1âð=âð2âððððâðgn=fnââi=ân2ânâ1fifnâi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¶æ°æ¶ï¼

æ³¨æå°å½æä¸¤ä¸ªéå¿çæ åµæ¶ï¼ä¸é¢çè¿ç¨åªä¼åå»ä¸æ¬¡ï¼å æ­¤è¿éè¦åå»

ðð=ððâðâ1âð=âð2âððððâðâ(ðð22)gn=fnââi=ân2ânâ1fifnâiâ(fn22)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ä¾é¢ãLuogu P5900ãæ æ å·æ æ ¹æ è®¡æ°

ä¾é¢ [ãLuogu P5900ãæ æ å·æ æ ¹æ è®¡æ°](https://www.luogu.com.cn/problem/P5900)

é¢ç®å¤§æï¼æ±æ n ä¸ªç»ç¹çæ æ å·æ æ ¹æ çæ¹æ¡æ°ï¼ð â¤200000nâ¤200000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

å¯¹äºæ°æ®èå´æ´å¤§çæ åµï¼åæ³åçï¼æ¬§æåæ¢åä½¿ç¨å¤é¡¹å¼æ¨¡æ¿å³å¯ï¼

## æ æ å·ç®åå¾

### ä¾é¢ãSGU 282. IsomorphismãIsomorphism

ä¾é¢ [ãSGU 282. IsomorphismãIsomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)

é¢ç®å¤§æï¼æ±æ n ä¸ªç»ç¹çæ æ å·å®å ¨å¾çè¾¹è¿è¡ m æè²çæ¹æ¡æ°ï¼

æ³¨æå°å½ m = 2 æ¶ï¼ææ±å¯¹è±¡å°±æ¯æ æ å·ç®åå¾ [A000088](https://oeis.org/A000088)ï¼èå¯æ³¢å©äºè®¡æ°å®çï¼

1|ðº|âðâðºðð(ð)1|G|âgâGmc(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¬é¢ä¸­ç½®æ¢ç¾¤ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºé¡¶ç¹ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶å¯¹ç§°ç¾¤çæçè¾¹éç½®æ¢ç¾¤ï¼ä½æ´ååæ³çæä¸¾éä¸º ð(ð!)O(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ æ³éè¿æ­¤é¢ï¼

èèæ ¹æ®æç §ç½®æ¢çå¾ªç¯ç»æè¿è¡åç±»ï¼æ¯ç§å¾ªç¯ç»æå¯¹åºä¸ç§æ°çåæï¼æä»¬ç¨ dfs() çæåæï¼é£ä¹é®é¢å³è½¬åä¸ºæ±æ¯ä¸ç§åæ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¯¹åºçç½®æ¢æ°ç® ð¤(ð)w(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¯ä¸ç±»ç½®æ¢ä¸­çå¾ªç¯ä¸ªæ° ð(ð)c(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç­æ¡ä¸º

1|ðº|âðâðð¤(ð)ðð(ð)1|G|âpâPw(p)mc(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èè ð¤(ð)w(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ä¸ªåæå¯¹åºä¸ä¸ªå¾ªç¯æåï¼åæ¶åä¸ç§å¤§å°çåæä¹é´çé¡ºåºæ å ³ï¼å èæä»¬æï¼

ð¤(ð)=ð!âð(ðð)âð(ðð!)w(p)=n!âi(pi)âi(qi!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿é ððqi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå¤§å°ä¸º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæå¨ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­åºç°çæ¬¡æ°ï¼

èè ð(ð)c(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå½±åçç¹éçå¾ªç¯å³ä¸º |ð||p|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½é¢ç®èå¯çæ¯è¾¹æè²ï¼æä»¥è¿éè¦èå¯ç¹ç½®æ¢æçæçè¾¹ç½®æ¢ï¼

å¦æä¸æ¡è¾¹å ³èçé¡¶ç¹å¤å¨åä¸ä¸ªå¾ªç¯å ï¼è®¾è¯¥å¾ªç¯å¤§å°ä¸º ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹è¾¹æçæçå¾ªç¯æ°æ°å¥½ä¸º âðð2ââpi2â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦æä¸æ¡è¾¹å ³èçé¡¶ç¹å¤å¨ä¸¤ä¸ªä¸åçå¾ªç¯ä¸­ï¼è®¾åå«ä¸º ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),ððpj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ªå¾ªç¯èçé¿åº¦åä¸º lcmâ¡(ðð,ðð)lcmâ¡(pi,pj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å èè¾¹æçæçå¾ªç¯æ°æ°å¥½ä¸º ððððlcmâ¡(ðð,ðð) =gcd(ðð,ðð)pipjlcmâ¡(pi,pj)=gcd(pi,pj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 ``` |  ```text #include <iostream> #include <vector> using namespace std ; using LL = long long ; int MOD = int ( 1e9 ) \+ 7 ; namespace NT { void INC ( int & a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; } int sum ( int a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; return a ; } void DEC ( int & a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; } int dff ( int a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; return a ; } void MUL ( int & a , int b ) { a = ( LL ) a * b % MOD ; } int pdt ( int a , int b ) { return ( LL ) a * b % MOD ; } int _I ( int b ) { int a = MOD , x1 = 0 , x2 = 1 , q ; while ( 1 ) { q = a / b , a %= b ; if ( ! a ) return x2 ; DEC ( x1 , pdt ( q , x2 )); q = b / a , b %= a ; if ( ! b ) return x1 ; DEC ( x2 , pdt ( q , x1 )); } } void DIV ( int & a , int b ) { MUL ( a , _I ( b )); } int qtt ( int a , int b ) { return pdt ( a , _I ( b )); } int pow ( int a , LL b ) { int c ( 1 ); while ( b ) { if ( b & 1 ) MUL ( c , a ); MUL ( a , a ), b >>= 1 ; } return c ; } template < class T > T pow ( T a , LL b ) { T c ( 1 ); while ( b ) { if ( b & 1 ) c *= a ; a *= a , b >>= 1 ; } return c ; } template < class T > T pow ( T a , int b ) { return pow ( a , ( LL ) b ); } struct Int { int val ; operator int () const { return val ; } Int ( int _val = 0 ) : val ( _val ) { val %= MOD ; if ( val < 0 ) val += MOD ; } Int ( LL _val ) : val ( _val ) { _val %= MOD ; if ( _val < 0 ) _val += MOD ; val = _val ; } Int & operator += ( const int & rhs ) { INC ( val , rhs ); return * this ; } Int operator \+ ( const int & rhs ) const { return sum ( val , rhs ); } Int & operator -= ( const int & rhs ) { DEC ( val , rhs ); return * this ; } Int operator \- ( const int & rhs ) const { return dff ( val , rhs ); } Int & operator *= ( const int & rhs ) { MUL ( val , rhs ); return * this ; } Int operator * ( const int & rhs ) const { return pdt ( val , rhs ); } Int & operator /= ( const int & rhs ) { DIV ( val , rhs ); return * this ; } Int operator / ( const int & rhs ) const { return qtt ( val , rhs ); } Int operator \- () const { return MOD \- * this ; } }; } // namespace NT using namespace NT ; constexpr int N = int ( 5e1 ) \+ 9 ; Int Fact [ N ]; vector < vector < int >> Partition ; vector < int > cur ; int n , m ; void gen ( int n = :: n , int s = 1 ) { if ( ! n ) { Partition . push_back ( cur ); } else if ( n >= s ) { cur . push_back ( s ); gen ( n \- s , s ); cur . pop_back (); gen ( n , s \+ 1 ); } } Int w ( const vector < int > P ) { Int z = Fact [ n ]; int c = 0 , l = P . front (); for ( auto p : P ) { z /= p ; if ( p != l ) { z /= Fact [ c ]; l = p ; c = 1 ; } else { ++ c ; } } z /= Fact [ c ]; return z ; } int gcd ( int x , int y ) { return y ? gcd ( y , x % y ) : x ; } int c ( const vector < int > P ) { int z = 0 ; for ( int i = 0 ; i < P . size (); ++ i ) { z += P [ i ] / 2 ; for ( int j = 0 ; j < i ; ++ j ) z += gcd ( P [ i ], P [ j ]); } return z ; } int main () { cin >> n >> m >> MOD ; Fact [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) Fact [ i ] = Fact [ i \- 1 ] * i ; gen (); Int res = 0 ; for ( auto P : Partition ) { res += w ( P ) * pow ( m , c ( P )); } res /= Fact [ n ]; cout << res << endl ; } ```   
---|---  
  
## ä¹ é¢

  * [CodeForces 438 E. The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)
  * [Luogu P5448. [THUPC2018] å¥½å¾è®¡æ°](https://www.luogu.com.cn/problem/P5448)
  * [Luogu P5818. [JSOI2011] ååå¼æä½è®¡æ°](https://www.luogu.com.cn/problem/P5818)
  * [Luogu P6597. ç¯çè®¡æ°](https://www.luogu.com.cn/problem/P6597)
  * [Luogu P6598. ç·çè®¡æ°](https://www.luogu.com.cn/problem/P6598)
  * [Luogu P4128. [SHOI2006] æè²å¾](https://www.luogu.com.cn/problem/P4128)
  * [Luogu P4727. [HNOI2009] å¾çåæè®¡æ°](https://www.luogu.com.cn/problem/P4727)
  * [AtCoder Beginner Contest 222 H. Binary Tree](https://atcoder.jp/contests/abc222/tasks/abc222_h)
  * [AtCoder Beginner Contest 284 Ex. Count Unlabeled Graphs](https://atcoder.jp/contests/abc284/tasks/abc284_h)
  * [Luogu P4708. ç»ç»](https://www.luogu.com.cn/problem/P4708)
  * [Luogu P7592. æ°æ ï¼2021 CoE-II Eï¼](https://www.luogu.com.cn/problem/P7592)
  * [Luogu P5206. [WC2019] æ°æ ](https://www.luogu.com.cn/problem/P5206)

## åèèµæä¸æ³¨é

  1. [WC2015, é¡¾æ±æ´²è¥åäº¤æµèµæ Graphical Enumeration](https://github.com/lychees/ACM-Training/blob/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2015/%E9%A1%BE%E6%98%B1%E6%B4%B2%E8%90%A5%E5%91%98%E4%BA%A4%E6%B5%81%E8%B5%84%E6%96%99%20Graphical%20Enumeration.pdf)
  2. [WC2019, çæå½æ°ï¼å¤é¡¹å¼ç®æ³ä¸å¾çè®¡æ°](https://github.com/lychees/ACM-Training/tree/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2019/d4)
  3. [Counting labeled graphs - Algorithms for Competitive Programming](https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html)
  4. [Graphical Enumeration Paperback, Frank Harary, Edgar M. Palmer](https://github.com/lychees/ACM-Training/blob/master/Note/Book/)
  5. [The encyclopedia of integer sequences, N. J. A. Sloane, Simon Plouffe](https://github.com/lychees/ACM-Training/blob/master/Note/Book/The%20encyclopedia%20of%20integer%20sequences%20\\\\\(N.%20J.A.%20Sloane%2C%20Simon%20Plouffe\\\\\).pdf)
  6. [Combinatorial Problems and Exercises, LÃ¡szlÃ³ LovÃ¡sz](https://github.com/lychees/ACM-Training/blob/master/Note/Book/Combinatorial%20Problems%20and%20Exercises_L%C3%A1szl%C3%B3%20Lov%C3%A1sz.pdf)
  7. [Graph Theory and Additive Combinatorics](https://yufeizhao.com/gtacbook/)

* * *

  1. ä¹è®¸æ æ å·äºåæ æ¯ä¸ä¸ªåä¾ï¼å¨ç»æç®åçæ åµä¸ï¼å¯¹åºçç½®æ¢ç¾¤æ¯æç­ç¾¤ï¼Identity Groupï¼ï¼æ­¤æ¶ææ å·çæ¬å¯ä»¥ç´æ¥éè¿ä¹ä»¥ ð!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°ï¼Â â©

  2. [ç²å ç blog](https://www.luogu.com.cn/blog/PinkRabbit/solution-sp4420) åè¯æä»¬ï¼è¿ä¸ªåºåä¹å¯ä»¥ä½¿ç¨ [Chirp Z-Transform](../../poly/czt/) ä¼åï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/graph-enumeration.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/graph-enumeration.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [lychees](https://github.com/lychees), [c-forrest](https://github.com/c-forrest), [ComeIntoCalm](https://github.com/ComeIntoCalm), [GoodCoder666](https://github.com/GoodCoder666), [HeRaNO](https://github.com/HeRaNO), [megakite](https://github.com/megakite), [Molmin](https://github.com/Molmin)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
