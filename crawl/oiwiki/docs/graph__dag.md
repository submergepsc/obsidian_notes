# æåæ ç¯å¾ - OI Wiki

- Source: https://oi-wiki.org/graph/dag/

# æåæ ç¯å¾

## å®ä¹

è¾¹æåï¼æ ç¯ï¼

è±æåå« Directed Acyclic Graphï¼ç¼©åæ¯ DAGï¼

## æ§è´¨

  * è½ [æææåº](../topo/) çå¾ï¼ä¸å®æ¯æåæ ç¯å¾ï¼

å¦ææç¯ï¼é£ä¹ç¯ä¸çä»»æä¸¤ä¸ªèç¹å¨ä»»æåºåä¸­é½ä¸æ»¡è¶³æ¡ä»¶äºï¼

  * æåæ ç¯å¾ï¼ä¸å®è½æææåºï¼

ï¼å½çº³æ³ï¼åè®¾èç¹æ°ä¸è¶ è¿ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç æåæ ç¯å¾é½è½æææåºï¼é£ä¹å¯¹äºèç¹æ°ç­äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼èèæ§è¡æææåºç¬¬ä¸æ­¥ä¹åçæ å½¢å³å¯ï¼

## å¤å®

å¦ä½å¤å®ä¸ä¸ªå¾æ¯å¦æ¯æåæ ç¯å¾å¢ï¼

æ£éªå®æ¯å¦å¯ä»¥è¿è¡ [æææåº](../topo/) å³å¯ï¼

å½ç¶ä¹æå¦å¤çæ¹æ³ï¼å¯ä»¥å¯¹å¾è¿è¡ä¸é [DFS](../../search/dfs/)ï¼å¨å¾å°ç DFS æ ä¸ççææ²¡æè¿åç¥å çéæ è¾¹ï¼è¿ç¥è¾¹ï¼ï¼å¦ææçè¯ï¼é£å°±æç¯äºï¼

## åºç¨

### DP æ±æé¿ï¼ç­ï¼è·¯

å¨ä¸è¬å¾ä¸ï¼æ±åæºæé¿ï¼ç­ï¼è·¯å¾çæä¼æ¶é´å¤æåº¦ä¸º ð(ðð)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼[BellmanâFord ç®æ³](../shortest-path/#bellmanford-ç®æ³)ï¼éç¨äºæè´æå¾ï¼æ ð(ðlogâ¡ð)O(mlogâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼[Dijkstra ç®æ³](../shortest-path/#dijkstra-ç®æ³)ï¼éç¨äºæ è´æå¾ï¼ï¼

ä½å¨ DAG ä¸ï¼æä»¬å¯ä»¥ä½¿ç¨ DP æ±æé¿ï¼ç­ï¼è·¯ï¼ä½¿æ¶é´å¤æåº¦ä¼åå° ð(ð +ð)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶æè½¬ç§»æ¹ç¨ä¸º ððð ð£ =ððð(ððð ð£,ððð ð¢ +ð¤ð¢,ð£)disv=min(disv,disu+wu,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ððð ð£ =ððð¥(ððð ð£,ððð ð¢ +ð¤ð¢,ð£)disv=max(disv,disu+wu,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æææåºåï¼æç §ææåºéåæ¯ä¸ªèç¹ï¼ç¨å½åèç¹æ¥æ´æ°ä¹åçèç¹ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text struct edge { int v , w ; }; int n , m ; vector < edge > e [ MAXN ]; vector < int > L ; // å­å¨æææåºç»æ int max_dis [ MAXN ], min_dis [ MAXN ], in [ MAXN ]; // in å­å¨æ¯ä¸ªèç¹çå ¥åº¦ void toposort () { // æææåº queue < int > S ; memset ( in , 0 , sizeof ( in )); for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 0 ; j < e [ i ]. size (); j ++ ) { in [ e [ i ][ j ]. v ] ++ ; } } for ( int i = 1 ; i <= n ; i ++ ) if ( in [ i ] == 0 ) S . push ( i ); while ( ! S . empty ()) { int u = S . front (); S . pop (); L . push_back ( u ); for ( int i = 0 ; i < e [ u ]. size (); i ++ ) { if ( \-- in [ e [ u ][ i ]. v ] == 0 ) { S . push ( e [ u ][ i ]. v ); } } } } void dp ( int s ) { // ä»¥ s ä¸ºèµ·ç¹æ±åæºæé¿ï¼ç­ï¼è·¯ toposort (); // å è¿è¡æææåº memset ( min_dis , 0x3f , sizeof ( min_dis )); memset ( max_dis , 0 , sizeof ( max_dis )); min_dis [ s ] = 0 ; for ( int i = 0 ; i < L . size (); i ++ ) { int u = L [ i ]; for ( int j = 0 ; j < e [ u ]. size (); j ++ ) { min_dis [ e [ u ][ j ]. v ] = min ( min_dis [ e [ u ][ j ]. v ], min_dis [ u ] \+ e [ u ][ j ]. w ); max_dis [ e [ u ][ j ]. v ] = max ( max_dis [ e [ u ][ j ]. v ], max_dis [ u ] \+ e [ u ][ j ]. w ); } } } ```   
---|---  
  
åè§ï¼[DAG ä¸ç DP](../../dp/dag/)ï¼

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/dag.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/graph/dag.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [dong628](https://github.com/dong628), [HeRaNO](https://github.com/HeRaNO)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
