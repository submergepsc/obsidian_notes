# DFSï¼å¾è®ºï¼ - OI Wiki

- Source: https://oi-wiki.org/graph/dfs/

# DFSï¼å¾è®ºï¼

## å¼å ¥

DFS å ¨ç§°æ¯ [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)ï¼ä¸­æåæ¯æ·±åº¦ä¼å æç´¢ï¼æ¯ä¸ç§ç¨äºéåææç´¢æ æå¾çç®æ³ï¼æè°æ·±åº¦ä¼å ï¼å°±æ¯è¯´æ¯æ¬¡é½å°è¯åæ´æ·±çèç¹èµ°ï¼

è¯¥ç®æ³è®²è§£æ¶å¸¸å¸¸ä¸ BFS å¹¶åï¼ä½ä¸¤è é¤äºé½è½éåå¾çè¿éåä»¥å¤ï¼ç¨éå®å ¨ä¸åï¼å¾å°æè½æ··ç¨ä¸¤ç§ç®æ³çæ åµï¼

DFS å¸¸å¸¸ç¨æ¥æä»£ç¨éå½å½æ°å®ç°çæç´¢ï¼ä½å®é ä¸ä¸¤è å¹¶ä¸ä¸æ ·ï¼æå ³è¯¥ç±»æç´¢ææ³è¯·åé [DFSï¼æç´¢ï¼](../../search/dfs/).

## è¿ç¨

DFS ææ¾èçç¹å¾å¨äºå ¶ **éå½è°ç¨èªèº«** ï¼åæ¶ä¸ BFS ç±»ä¼¼ï¼DFS ä¼å¯¹å ¶è®¿é®è¿çç¹æä¸è®¿é®æ è®°ï¼å¨éåå¾æ¶è·³è¿å·²æè¿æ è®°çç¹ï¼ä»¥ç¡®ä¿ **æ¯ä¸ªç¹ä» è®¿é®ä¸æ¬¡** ï¼ç¬¦åä»¥ä¸ä¸¤æ¡è§åçå½æ°ï¼ä¾¿æ¯å¹¿ä¹ä¸ç DFSï¼

å ·ä½å°è¯´ï¼DFS å¤§è´ç»æå¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 ``` |  ```text DFS(v) // v å¯ä»¥æ¯å¾ä¸­çä¸ä¸ªé¡¶ç¹ï¼ä¹å¯ä»¥æ¯æ½è±¡çæ¦å¿µï¼å¦ dp ç¶æç­ï¼ å¨ v ä¸æè®¿é®æ è®° for u in v çç¸é»èç¹ if u æ²¡ææè¿è®¿é®æ è®° then DFS(u) end end end ```   
---|---  
  
ä»¥ä¸ä»£ç åªå å«äº DFS å¿ éçä¸»è¦ç»æï¼å®é ç DFS ä¼å¨ä»¥ä¸ä»£ç åºç¡ä¸å å ¥ä¸äºä»£ç ï¼å©ç¨ DFS æ§è´¨è¿è¡å ¶ä»æä½ï¼

## æ§è´¨

è¯¥ç®æ³éå¸¸çæ¶é´å¤æåº¦ä¸º ð(ð +ð)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç©ºé´å¤æåº¦ä¸º ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç¹æ°ï¼ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºè¾¹æ°ï¼æ³¨æç©ºé´å¤æåº¦å å«äºæ ç©ºé´ï¼æ ç©ºé´çç©ºé´å¤æåº¦æ¯ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼å¨å¹³å ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåä¸æ¡è¾¹çæ¡ä»¶ä¸æè½è¾¾å°æ­¤æ¶é´å¤æåº¦ï¼ä¾å¦ç¨ååææé»æ¥è¡¨å­å¨å¾ï¼å¦æç¨é»æ¥ç©éµåä¸ä¸å®è½è¾¾å°æ­¤å¤æåº¦ï¼

> å¤æ³¨ï¼ç®åå¤§é¨åç®æ³ç«èµï¼å æ¬ NOIPãå¤§é¨åçéä»¥å CCF ä¸¾åçåé¡¹èµäºï¼é½æ¯æ **æ éæ ç©ºé´** ï¼å³ï¼æ ç©ºé´ä¸åç¬éå¶ï¼ä½æ»å å­ç©ºé´ä»ç¶åé¢é¢éå¶ï¼ä½å¤§é¨åæä½ç³»ç»ä¼å¯¹æ ç©ºé´åé¢å¤çéå¶ï¼å æ­¤å¨æ¬å°è°è¯æ¶éè¦ä¸äºæ¹å¼æ¥åæ¶æ ç©ºé´éå¶ï¼
> 
>   * å¨ Windows ä¸ï¼éå¸¸çæ¹æ³æ¯å¨ **ç¼è¯éé¡¹** ä¸­å å ¥ `-Wl,--stack=1000000000`ï¼è¡¨ç¤ºå°æ ç©ºé´éå¶è®¾ç½®ä¸º 1000000000 å­èï¼
>   * å¨ Linux ä¸ï¼éå¸¸çæ¹æ³æ¯å¨è¿è¡ç¨åºå **å¨ç»ç«¯å** æ§è¡ `ulimit -s unlimited`ï¼è¡¨ç¤ºæ ç©ºé´æ éï¼æ¯ä¸ªç»ç«¯åªéæ§è¡ä¸æ¬¡ï¼å¯¹ä¹åæ¯æ¬¡ç¨åºè¿è¡é½ææï¼
> 

## å®ç°

### æ å®ç°

DFS å¯ä»¥ä½¿ç¨ [æ ï¼Stackï¼](../../ds/stack/) ä¸ºéåä¸­èç¹çæå­å®¹å¨æ¥å®ç°ï¼è¿ä¸ç¨ [éåï¼Queueï¼](../../ds/queue/) å®ç°ç BFS å½¢æé«åº¦å¯¹åºï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text vector < vector < int >> adj ; // é»æ¥è¡¨ vector < bool > vis ; // è®°å½èç¹æ¯å¦å·²ç»éå void dfs ( int s ) { stack < int > st ; st . push ( s ); vis [ s ] = true ; while ( ! st . empty ()) { int u = st . top (); st . pop (); for ( int v : adj [ u ]) { if ( ! vis [ v ]) { vis [ v ] = true ; // ç¡®ä¿æ éæ²¡æéå¤å ç´ st . push ( v ); } } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # adj : List[List[int]] é»æ¥è¡¨ # vis : List[bool] è®°å½èç¹æ¯å¦å·²ç»éå def dfs ( s : int ) -> None : stack = [ s ] # ç¨åè¡¨æ¥æ¨¡ææ ï¼æèµ·ç¹å å ¥æ ä¸­ vis [ s ] = True # èµ·ç¹è¢«éå while stack : # å½æ éç©ºæ¶ç»§ç»­æ§è¡ u = ( stack . pop () ) # æ¿åå¹¶ä¸¢å¼ææåä¸ä¸ªå ç´ ï¼æ é¡¶çå ç´ ï¼ï¼å¯ä»¥çè§£ä¸ºèµ°å°uè¿ä¸ªå ç´ for v in adj [ u ]: # å¯¹äºä¸uç¸é»çæ¯ä¸ªå ç´ v if not vis [ v ]: # å¦ævå¨æ­¤åæ²¡æèµ°è¿ vis [ v ] = True # ç¡®ä¿æ éæ²¡æéå¤å ç´ stack . append ( v ) # ævå å ¥æ ä¸­ ```   
---|---  
  
### éå½å®ç°

å½æ°å¨éå½è°ç¨æ¶çæ±å¼å¦åå¯¹æ çæ·»å åå é¤å ç´ çé¡ºåºï¼æ å½æ°è°ç¨æå æ®çèæå°åè¢«ç§°ä¸ºå½æ°è°ç¨æ ï¼Call Stackï¼ï¼DFS å¯ç¨éå½çæ¹å¼å®ç°ï¼

ä»¥ [é»æ¥è¡¨ï¼Adjacency Listï¼](../save/#é»æ¥è¡¨) ä½ä¸ºå¾çå­å¨æ¹å¼ï¼

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text vector < vector < int >> adj ; // é»æ¥è¡¨ vector < bool > vis ; // è®°å½èç¹æ¯å¦å·²ç»éå void dfs ( const int u ) { vis [ u ] = true ; for ( int v : adj [ u ]) if ( ! vis [ v ]) dfs ( v ) } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text # adj : List[List[int]] é»æ¥è¡¨ # vis : List[bool] è®°å½èç¹æ¯å¦å·²ç»éå def dfs ( u : int ) -> None : vis [ u ] = True for v in adj [ u ]: if not vis [ v ]: dfs ( v ) ```   
---|---  
  
ä»¥ [é¾å¼ååæ](../save/#é¾å¼ååæ) ä¸ºä¾ï¼

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text void dfs ( int u ) { vis [ u ] = 1 ; for ( int i = head [ u ]; i ; i = e [ i ]. x ) { if ( ! vis [ e [ i ]. t ]) { dfs ( v ); } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text public void dfs ( int u ) { vis [ u ] = true ; for ( int i = head [ u ] ; i != 0 ; i = e [ i ] . x ) { if ( ! vis [ e [ i ] . t ] ) { dfs ( v ); } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def dfs ( u ): vis [ u ] = True i = head [ u ] while i : if vis [ e [ i ] . t ] == False : dfs ( v ) i = e [ i ] . x ```   
---|---  
  
### DFS åºå

DFS åºåæ¯æ DFS è°ç¨è¿ç¨ä¸­è®¿é®çèç¹ç¼å·çåºåï¼

æä»¬åç°ï¼æ¯ä¸ªå­æ é½å¯¹åº DFS åºåä¸­çè¿ç»­ä¸æ®µï¼ä¸æ®µåºé´ï¼ï¼

### æ¬å·åºå

DFS è¿å ¥æä¸ªèç¹çæ¶åè®°å½ä¸ä¸ªå·¦æ¬å· `(`ï¼éåºæä¸ªèç¹çæ¶åè®°å½ä¸ä¸ªå³æ¬å· `)`ï¼

æ¯ä¸ªèç¹ä¼åºç°ä¸¤æ¬¡ï¼ç¸é»ä¸¤ä¸ªèç¹çæ·±åº¦ç¸å·® 1ï¼

### ä¸è¬å¾ä¸ DFS

å¯¹äºéè¿éå¾ï¼åªè½è®¿é®å°èµ·ç¹æå¨çè¿éåéï¼

å¯¹äºè¿éå¾ï¼DFS åºåéå¸¸ä¸å¯ä¸ï¼

æ³¨ï¼æ ç DFS åºåä¹æ¯ä¸å¯ä¸çï¼

å¨ DFS è¿ç¨ä¸­ï¼éè¿è®°å½æ¯ä¸ªèç¹ä»åªä¸ªç¹è®¿é®èæ¥ï¼å¯ä»¥å»ºç«ä¸ä¸ªæ ç»æï¼ç§°ä¸º DFS æ ï¼DFS æ æ¯åå¾çä¸ä¸ªçææ ï¼

[DFS æ ](../scc/#dfs-çææ) æå¾å¤æ§è´¨ï¼æ¯å¦å¯ä»¥ç¨æ¥æ± [å¼ºè¿éåé](../scc/)ï¼

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/dfs.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/graph/dfs.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [Craneplayz](https://github.com/Craneplayz), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [shenshuaijie](https://github.com/shenshuaijie), [sshwy](https://github.com/sshwy), [vincent-163](https://github.com/vincent-163), [Acfboy](https://github.com/Acfboy), [billchenchina](https://github.com/billchenchina), [ChungZH](https://github.com/ChungZH), [greyqz](https://github.com/greyqz), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [LLLgoyour](https://github.com/LLLgoyour), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [qq1010903229](https://github.com/qq1010903229), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [yjl9903](https://github.com/yjl9903), [zychen20](https://github.com/zychen20)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
