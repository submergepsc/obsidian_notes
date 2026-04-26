# å²ç¹åæ¡¥ - OI Wiki

- Source: https://oi-wiki.org/graph/cut/

# å²ç¹åæ¡¥

ç¸å ³é è¯»ï¼[åè¿éåé](../bcc/)

å²ç¹åæ¡¥æ´ä¸¥è°¨çå®ä¹åè§ [å¾è®ºç¸å ³æ¦å¿µ](../concept/)ï¼

## å²ç¹

> å¯¹äºä¸ä¸ªæ åå¾ï¼å¦ææä¸ä¸ªç¹å é¤åè¿ä¸ªå¾çæå¤§è¿éåéæ°å¢å äºï¼é£ä¹è¿ä¸ªç¹å°±æ¯è¿ä¸ªå¾çå²ç¹ï¼åç§°å²é¡¶ï¼ï¼

### è¿ç¨

å¦ææä»¬å°è¯å é¤æ¯ä¸ªç¹ï¼å¹¶ä¸å¤æ­è¿ä¸ªå¾çè¿éæ§ï¼é£ä¹å¤æåº¦ä¼ç¹å«çé«ï¼æä»¥è¦ä»ç»ä¸ä¸ªå¸¸ç¨çç®æ³ï¼Tarjanï¼

é¦å ï¼æä»¬ä¸ä¸ä¸ªå¾ï¼

![](./images/cut1.svg)

å¾å®¹æççåºå²ç¹æ¯ 2ï¼èä¸è¿ä¸ªå¾ä» æè¿ä¸ä¸ªå²ç¹ï¼

é¦å ï¼æä»¬æç § DFS åºç»ä»æä¸æ¶é´æ³ï¼è®¿é®çé¡ºåºï¼ï¼

![](./images/cut2.svg)

è¿äºä¿¡æ¯è¢«æä»¬ä¿å­å¨ä¸ä¸ªå«å `dfn` çæ°ç»ä¸­ï¼

è¿éè¦å¦å¤ä¸ä¸ªæ°ç» `low`ï¼ç¨å®æ¥å­å¨ä¸ç»è¿å ¶ç¶äº²è½å°è¾¾çæå°çæ¶é´æ³ï¼

ä¾å¦ `low[2]` æ¯ 1ï¼`low[5]` å `low[6]` æ¯ 3ï¼

ç¶åæä»¬å¼å§ DFSï¼æä»¬å¤æ­æä¸ªç¹æ¯å¦æ¯å²ç¹çæ ¹æ®æ¯ï¼å¯¹äºæä¸ªé¡¶ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå­å¨è³å°ä¸ä¸ªé¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¿å­ï¼ï¼ä½¿å¾ ððð¤ð£ â¥ðððð¢lowvâ¥dfnu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ä¸è½åå°ç¥å ï¼é£ä¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¹ä¸ºå²ç¹ï¼

æ­¤æ ¹æ®æç¬ä¸éç¨äºæç´¢çèµ·å§ç¹ï¼å ¶éè¦ç¹æ®èèï¼è¥è¯¥ç¹ä¸æ¯å²ç¹ï¼åå ¶ä»è·¯å¾äº¦è½å°è¾¾å ¨é¨ç»ç¹ï¼å æ­¤ä»èµ·å§ç¹åªãåä¸æäºä¸æ¬¡ãï¼å³å¨æç´¢æ å ä» æä¸ä¸ªå­ç»ç¹ï¼å¦æå¨æç´¢æ å æä¸¤ä¸ªåä»¥ä¸çå¿å­ï¼é£ä¹ä»ä¸å®æ¯å²ç¹äºï¼è®¾æ³ä¸å¾ä» 2 å¼å§æç´¢ï¼æç´¢æ å åºæä¸¤ä¸ªå­ç»ç¹ï¼3 æ 4 å 5 æ 6ï¼ï¼å¦æåªæä¸ä¸ªå¿å­ï¼é£ä¹æå®å æï¼ä¸ä¼æä»»ä½çå½±åï¼æ¯å¦ä¸é¢è¿ä¸ªå¾ï¼æ­¤å¤å½¢æäºä¸ä¸ªç¯ï¼

![](./images/cut3.svg)

æä»¬å¨è®¿é® 1 çå¿å­æ¶åï¼åè®¾å  DFS å°äº 2ï¼ç¶åæ è®°ç¨è¿ï¼ç¶åéå½å¾ä¸ï¼æ¥å°äº 4ï¼4 åæ¥å°äº 3ï¼å½éå½åæº¯çæ¶åï¼ä¼åç° 3 å·²ç»è¢«è®¿é®è¿äºï¼æä»¥ä¸æ¯å²ç¹ï¼

æ´æ° `low` çä¼ªä»£ç å¦ä¸ï¼

1ð¢ðÂ ð£Â is a son ofÂ ð¢2lowð¢=min(lowð¢,lowð£)3ðð¥ð¬ð4lowð¢=min(lowð¢,dfnð£)1ifÂ vÂ is a son ofÂ u2lowu=min(lowu,lowv)3else4lowu=min(lowu,dfnv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### ä¾é¢

[æ´è°· P3388ãæ¨¡æ¿ãå²ç¹ï¼å²é¡¶ï¼](https://www.luogu.com.cn/problem/P3388)

ä¾é¢ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 ``` |  ```text /* æ´è°· P3388 ãæ¨¡æ¿ãå²ç¹ï¼å²é¡¶ï¼ */ #include <iostream> #include <vector> using namespace std ; int n , m ; // nï¼ç¹æ° mï¼è¾¹æ° int dfn [ 100001 ], low [ 100001 ], idx , res ; // dfnï¼è®°å½æ¯ä¸ªç¹çæ¶é´æ³ // lowï¼è½ä¸ç»è¿ç¶äº²å°è¾¾æå°çç¼å·ï¼idxï¼æ¶é´æ³ï¼resï¼ç­æ¡æ°é bool vis [ 100001 ], flag [ 100001 ]; // flag: ç­æ¡ visï¼æ è®°æ¯å¦éå¤ vector < int > edge [ 100001 ]; // å­å¾ç¨ç void Tarjan ( int u , int fa ) { // u å½åç¹çç¼å·ï¼fa èªå·±ç¸ç¸çç¼å· vis [ u ] = true ; // æ è®° low [ u ] = dfn [ u ] = ++ idx ; // æä¸æ¶é´æ³ int child = 0 ; // æ¯ä¸ä¸ªç¹å¿å­æ°é for ( const auto & v : edge [ u ]) { // è®¿é®è¿ä¸ªç¹çææé»å± ï¼C++11ï¼ if ( ! vis [ v ]) { child ++ ; // å¤äºä¸ä¸ªå¿å­ Tarjan ( v , u ); // ç»§ç»­ low [ u ] = min ( low [ u ], low [ v ]); // æ´æ°è½å°çæå°èç¹ç¼å· if ( fa != u && low [ v ] >= dfn [ u ] && ! flag [ u ]) { // ä¸»è¦ä»£ç  // å¦æä¸æ¯èªå·±ï¼ä¸ä¸éè¿ç¶äº²è¿åçæå°ç¹ç¬¦åå²ç¹çè¦æ±ï¼å¹¶ä¸æ²¡æè¢«æ è®°è¿ // è¦æ±å³ä¸ºï¼å äºç¶äº²è¿ä¸ä¸å»äºï¼å³ä¸ºæå¤è¿å°ç¶äº² flag [ u ] = true ; res ++ ; // è®°å½ç­æ¡ } } else if ( v != fa ) { // å¦æè¿ä¸ªç¹ä¸æ¯èªå·±çç¶äº²ï¼æ´æ°è½å°çæå°èç¹ç¼å· low [ u ] = min ( low [ u ], dfn [ v ]); } } // ä¸»è¦ä»£ç ï¼èªå·±çè¯éè¦ 2 ä¸ªå¿å­æå¯ä»¥ if ( fa == u && child >= 2 && ! flag [ u ]) { flag [ u ] = true ; res ++ ; // è®°å½ç­æ¡ } } int main () { cin >> n >> m ; // è¯»å ¥æ°æ® for ( int i = 1 ; i <= m ; i ++ ) { // æ³¨æç¹æ¯ä» 1 å¼å§ç int x , y ; cin >> x >> y ; edge [ x ]. push_back ( y ); edge [ y ]. push_back ( x ); } // ä½¿ç¨ vector å­å¾ for ( int i = 1 ; i <= n ; i ++ ) // å ä¸º Tarjan å¾ä¸ä¸å®è¿é if ( ! vis [ i ]) { idx = 0 ; // æ¶é´æ³åå§ä¸º 0 Tarjan ( i , i ); // ä»ç¬¬ i ä¸ªç¹å¼å§ï¼ç¶äº²ä¸ºèªå·± } cout << res << endl ; for ( int i = 1 ; i <= n ; i ++ ) if ( flag [ i ]) cout << i << " " ; // è¾åºç»æ return 0 ; } ```   
---|---  
  
## å²è¾¹ï¼æ éè¾¹æ¶ï¼

åå²ç¹å·®ä¸å¤ï¼å«åæ¡¥ï¼

> å¯¹äºä¸ä¸ªæ åå¾ï¼å¦æå æä¸æ¡è¾¹åå¾ä¸­çè¿éåéæ°å¢å äºï¼åç§°è¿æ¡è¾¹ä¸ºæ¡¥æè å²è¾¹ï¼ä¸¥è°¨æ¥è¯´ï¼å°±æ¯ï¼åè®¾æè¿éå¾ ðº ={ð,ð¸}G={V,E}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å ¶ä¸­ä¸æ¡è¾¹ï¼å³ ð âð¸eâE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å¦æ ðº âðGâe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸è¿éçï¼åè¾¹ ðe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æ¡å²è¾¹ï¼æ¡¥ï¼ï¼

æ¯å¦è¯´ï¼ä¸å¾ä¸­ï¼

![å²è¾¹ç¤ºä¾å¾](./images/bridge1.svg)

çº¢è²çè¾¹å°±æ¯å²è¾¹ï¼

### è¿ç¨

åå²ç¹å·®ä¸å¤ï¼åªè¦æ¹ä¸å¤ï¼ððð¤ð£ >ðððð¢lowv>dfnu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¯ä»¥äºï¼èä¸ä¸éè¦èèæ ¹èç¹çé®é¢ï¼

å²è¾¹æ¯åæ¯ä¸æ¯æ ¹èç¹æ²¡å ³ç³»çï¼åæ¥æä»¬æ±å²ç¹çæ¶åæ¯æç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸å¯è½ä¸ç»è¿ç¶èç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºåå°ç¥å èç¹ï¼å æ¬ç¶èç¹ï¼ï¼æä»¥é¡¶ç¹ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å²ç¹ï¼å¦æ ððð¤ð£ =ðððð¢lowv=dfnu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºè¿å¯ä»¥åå°ç¶èç¹ï¼å¦æé¡¶ç¹ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è½åå°ç¥å ä¹æ²¡æå¦å¤ä¸æ¡åå°ç¶äº²çè·¯ï¼é£ä¹ ð¢ âð£uâv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ¡è¾¹å°±æ¯å²è¾¹ï¼

### å®ç°

ä¸é¢ä»£ç å®ç°äºå¯¹ **æ éè¾¹** çæ åå¾æ±å²è¾¹ï¼å ¶ä¸­ï¼å½ `isbridge[x]` ä¸ºçæ¶ï¼`(father[x],x)` ä¸ºä¸æ¡å²è¾¹ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text int low [ MAXN ], dfn [ MAXN ], idx ; bool isbridge [ MAXN ]; vector < int > G [ MAXN ]; int cnt_bridge ; int father [ MAXN ]; void tarjan ( int u , int fa ) { father [ u ] = fa ; low [ u ] = dfn [ u ] = ++ idx ; for ( const auto & v : G [ u ]) { if ( ! dfn [ v ]) { tarjan ( v , u ); low [ u ] = min ( low [ u ], low [ v ]); if ( low [ v ] > dfn [ u ]) { isbridge [ v ] = true ; ++ cnt_bridge ; } } else if ( v != fa ) { low [ u ] = min ( low [ u ], dfn [ v ]); } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text low = [ 0 ] * MAXN dfn = [ 0 ] * MAXN idx = 0 isbridge = [ False ] * MAXN G = [[ 0 for i in range ( MAXN )] for j in range ( MAXN )] cnt_bridge = 0 father = [ 0 ] * MAXN def tarjan ( u , fa ): father [ u ] = fa idx = idx \+ 1 low [ u ] = dfn [ u ] = idx for i in range ( 0 , len ( G [ u ])): v = G [ u ][ i ] if dfn [ v ] == False : tarjan ( v , u ) low [ u ] = min ( low [ u ], low [ v ]) if low [ v ] > dfn [ u ]: isbridge [ v ] = True cnt_bridge = cnt_bridge \+ 1 elif v != fa : low [ u ] = min ( low [ u ], dfn [ v ]) ```   
---|---  
  
## å²è¾¹ï¼æéè¾¹æ¶ï¼

ç¶èï¼ä¸è¿°æ éè¾¹æ¶çåæ³å¨æéè¾¹çæ åå¾ä¸æ¯æé®é¢çï¼

å ä¸ºä¸¤èç¹é´å¯è½ä¸æ­¢æä¸æ¡è¾¹ï¼æ­¤æ¶å®ä»¬é½ä¸ä¼æ¯æ¡¥ï¼

### è¿ç¨

ä¸ç§æè·¯æ¯å°åæ° `fa` æ¹ä¸ºååèµ°è¿çè¾¹çç¼å·ï¼æ¯æ¡è¾¹çç¼å·ä¸è´ï¼å³å¯ï¼å³å°ãä¸ç¨ç¶èç¹æ´æ°ãæ¹ä¸ºãä¸ç¨æ¥æ¶çè¾¹æ´æ°ãï¼

å¦ä¸ç§æ´ç®åçæè·¯æ¯è®¾ç«ä¸ä¸ªæ è®°å¤æ­æ¯å¦å·²æä¸æ¡è¾¹æµè¾¾ç¶èç¹ï¼æ è®°ååè®¿é®å°ç¶èç¹æ¶æ­£å¸¸æ´æ°ï¼

ä¸é¢ä»£ç å®ç°äºå¯¹å¯è½ **æéè¾¹** çæ åå¾æ±å²è¾¹ï¼

C++

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text int low [ MAXN ], dfn [ MAXN ], idx ; bool isbridge [ MAXN ]; vector < int > G [ MAXN ]; int cnt_bridge ; int father [ MAXN ]; void tarjan ( int u , int fa ) { bool flag = false ; father [ u ] = fa ; low [ u ] = dfn [ u ] = ++ idx ; for ( const auto & v : G [ u ]) { if ( ! dfn [ v ]) { tarjan ( v , u ); low [ u ] = min ( low [ u ], low [ v ]); if ( low [ v ] > dfn [ u ]) { isbridge [ v ] = true ; ++ cnt_bridge ; } } else { if ( v != fa || flag ) low [ u ] = min ( low [ u ], dfn [ v ]); else flag = true ; } } } ```   
---|---  
  
## ç»ä¹ 

  * [P3388ãæ¨¡æ¿ãå²ç¹ï¼å²é¡¶ï¼](https://www.luogu.com.cn/problem/P3388)
  * [POJ2117 Electricity](http://poj.org/problem?id=2117)
  * [HDU4738 Caocao's Bridges](https://acm.hdu.edu.cn/showproblem.php?pid=4738)
  * [HDU2460 Network](https://acm.hdu.edu.cn/showproblem.php?pid=2460)
  * [POJ1523 SPF](http://poj.org/problem?id=1523)

Tarjan ç®æ³è¿æè®¸å¤ç¨éï¼å¸¸ç¨çä¾å¦æ±å¼ºè¿éåéï¼ç¼©ç¹ï¼è¿ææ± 2-SAT çç¨éç­ï¼

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/cut.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/graph/cut.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [GavinZhengOI](https://github.com/GavinZhengOI), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [Planet6174](https://github.com/Planet6174), [Tiphereth-A](https://github.com/Tiphereth-A), [0xis-cn](https://github.com/0xis-cn), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [tder6](https://github.com/tder6), [weiyong1024](https://github.com/weiyong1024), [ylxmf2005](https://github.com/ylxmf2005), [c-forrest](https://github.com/c-forrest), [ChungZH](https://github.com/ChungZH), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Error-Eric](https://github.com/Error-Eric), [Gesrua](https://github.com/Gesrua), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [Peanut-Tang](https://github.com/Peanut-Tang), [Qiu-Quanzhi](https://github.com/Qiu-Quanzhi), [shawlleyw](https://github.com/shawlleyw), [SukkaW](https://github.com/SukkaW), [t123yh](https://github.com/t123yh), [Xeonacid](https://github.com/Xeonacid), [yiyangit](https://github.com/yiyangit), [yusancky](https://github.com/yusancky)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
