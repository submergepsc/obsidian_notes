# çº¿æ§åä½æ¹ç¨ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/linear-equation/

# çº¿æ§åä½æ¹ç¨

æ¬æè®¨è®ºçº¿æ§åä½æ¹ç¨çæ±è§£ï¼

## åºæ¬æ¦å¿µ

è®¾ ð,ð,ða,b,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ´æ°ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæªç¥æ°ï¼é£ä¹ï¼å½¢å¦

ðð¥â¡ð(modð)axâ¡b(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çæ¹ç¨ç§°ä¸º **çº¿æ§åä½æ¹ç¨** ï¼linear congruence equationï¼ï¼

æ±è§£çº¿æ§åä½æ¹ç¨ï¼éè¦æ¾å°åºé´ [0,ð â1][0,nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨é¨è§£ï¼å½ç¶ï¼å°å®ä»¬å å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä»»æåæ°ï¼ä¾ç¶æ¯æ¹ç¨çè§£ï¼å¨æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¹ä¸ï¼è¿äºå°±æ¯è¯¥æ¹ç¨çå ¨é¨è§£ï¼

æ¬ææ¥ä¸æ¥ä»ç»äºä¸¤ç§æ±è§£çº¿æ§åä½æ¹ç¨çæè·¯ï¼åå«å©ç¨äºéå åä¸å®æ¹ç¨ï¼å¯¹äºä¸è¬çæ å½¢ï¼éå åä¸å®æ¹ç¨çæ±è§£é½éè¦ç¨å° [æ©å±æ¬§å éå¾ç®æ³](../gcd/#æ©å±æ¬§å)ï¼å æ­¤ï¼è¿ä¸¤ç§æè·¯å ¶å®æ¯ä¸è´çï¼

## ç¨éå æ±è§£

é¦å ï¼èè ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ çæ å½¢ï¼å³ gcd(ð,ð) =1gcd(a,n)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼å¯ä»¥è®¡ç® ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [éå ](../inverse/) ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶å°æ¹ç¨ä¸¤è¾¹åä¹ä»¥ ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±å¾å°æ¹ç¨çå¯ä¸è§£ï¼

ð¥â¡ððâ1(modð).xâ¡baâ1(modn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç´§æ¥çï¼èè ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸äºç´ çæ å½¢ï¼å³ gcd(ð,ð) =ð >1gcd(a,n)=d>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼åæ¹ç¨ä¸ä¸å®æè§£ï¼ä¾å¦ï¼2ð¥ â¡1(mod4)2xâ¡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ²¡æè§£ï¼å æ­¤ï¼éè¦èèä¸¤ç§æ å½¢ï¼

  * å½ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è½æ´é¤ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ¹ç¨æ è§£ï¼å¯¹äºä»»æç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¹ç¨å·¦ä¾§ ðð¥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼ä½æ¯æ¹ç¨å³ä¾§ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å æ­¤ï¼å®ä»¬ä¸å¯è½ç¸å·® ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä¹ä¸å®æ¯ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼å æ­¤ï¼æ¹ç¨æ è§£ï¼

  * å½ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥æ´é¤ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å¯ä»¥å°æ¹ç¨çåæ° ð,ð,ða,b,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½åé¤ä»¥ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å°ä¸ä¸ªæ°çæ¹ç¨ï¼

ðâ²ð¥â¡ðâ²(modðâ²).aâ²xâ¡bâ²(modnâ²).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼gcd(ðâ²,ðâ²) =1gcd(aâ²,nâ²)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ðâ²aâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðâ²nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼è¿ç§æ å½¢å·²ç»å¨åæè§£å³ï¼æä»¥ï¼å¯ä»¥éè¿æ±è§£éå å¾å°æ¹ç¨çä¸ä¸ªè§£ ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

æ¾ç¶ï¼ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯åæ¹ç¨çä¸ä¸ªè§£ï¼ä½è¿å¹¶éåæ¹ç¨å¯ä¸çè§£ï¼ç±äºè½¬ååçæ¹ç¨çå ¨ä½è§£ä¸º

{ð¥â²+ððâ²:ðâð}.{xâ²+knâ²:kâZ}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿äºè§£ä¸­è½å¨åºé´ [0,ð â1][0,nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé£äºï¼å°±æ¯åæ¹ç¨å¨åºé´ [0,ð â1][0,nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çå ¨é¨è§£ï¼

ð¥â¡(ð¥â²+ððâ²)(modð),ð=0,1,â¯,ðâ1.xâ¡(xâ²+knâ²)(modn),k=0,1,â¯,dâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ»ç»è¿ä¸¤ç§æ å½¢ï¼çº¿æ§åä½æ¹ç¨ç **è§£çæ°é** ç­äº ð =gcd(ð,ð)d=gcd(a,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## ç¨ä¸å®æ¹ç¨æ±è§£

çº¿æ§åä½æ¹ç¨ç­ä»·äºå ³äº ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [äºå ä¸æ¬¡ä¸å®æ¹ç¨](../bezouts/#ä¸¤ä¸ªåéçæ)ï¼

ðð¥+ðð¦=ð.ax+ny=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨æå¼é¡µé¢çè®¨è®ºï¼æ¹ç¨æè§£å½ä¸ä» å½ gcd(ð,ð) â£ðgcd(a,n)â£b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸è¯¥æ¹ç¨çä¸ç»éè§£æ¯

ð¥=ð¥0+ð¡ðð,ð¦=ð¦0âð¡ðð,x=x0+tnd,y=y0âtad,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð =gcd(ð,ð)d=gcd(a,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®ä»¬çæå¤§å ¬çº¦æ°ï¼ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä»»ææ´æ°ï¼

è¿èï¼çº¿æ§åä½æ¹ç¨çéè§£å°±æ¯

ð¥â¡(ð¥0+ð¡ðð)(modð),ð¡âð.xâ¡(x0+tnd)(modn),tâZ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å° ð¥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ ð/ðn/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡å°±å¾å°åä½æ¹ç¨çæå°ï¼éè´ï¼æ´æ°è§£ï¼ä¹å°±æ¯ä¸æç ð¥â²xâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## åèå®ç°

æ¬èæä¾çåèå®ç°å¯ä»¥å¾å°åä½æ¹ç¨çæå°éè´æ´æ°è§£ï¼å¦æè§£ä¸å­å¨ï¼åè¾åº â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // Extended Euclidean Algorithm. // Finds integers x, y such that a*x + b*y = gcd(a, b), // and returns gcd(a, b). int ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; return a ; } else { int d = ex_gcd ( b , a % b , y , x ); y -= a / b * x ; return d ; } } // Solves the linear congruence equation: // a * x â¡ b (mod n), where n > 0\. // Returns the smallest non-negative solution x, // or -1 if there is no solution. int solve_linear_congruence_equation ( int a , int b , int n ) { int x , y ; int d = ex_gcd ( a , n , x , y ); if ( b % d ) return -1 ; n /= d ; return (( long long ) x * ( b / d ) % n \+ n ) % n ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text def ex_gcd ( a , b ): """ Extended Euclidean Algorithm. Finds integers x, y such that a*x + b*y = gcd(a, b), and returns (gcd, x, y). """ if b == 0 : return a , 1 , 0 d , x1 , y1 = ex_gcd ( b , a % b ) x = y1 y = x1 \- ( a // b ) * y1 return d , x , y def solve_linear_congruence_equation ( a , b , n ): """ Solves the linear congruence equation: a * x â¡ b (mod n), where n > 0\. Returns the smallest non-negative solution x, or -1 if there is no solution. """ d , x , y = ex_gcd ( a , n ) if b % d != 0 : return \- 1 n //= d return ( x * ( b // d ) % n \+ n ) % n ```   
---|---  
  
## ä¹ é¢

  * [ãNOIP2012ãåä½æ¹ç¨](https://loj.ac/problem/2605)

**æ¬é¡µé¢ä¸»è¦è¯èªåæ[ÐÐ¾Ð´ÑÐ»ÑÐ½Ð¾Ðµ Ð»Ð¸Ð½ÐµÐ¹Ð½Ð¾Ðµ ÑÑÐ°Ð²Ð½ÐµÐ½Ð¸Ðµ Ð¿ÐµÑÐ²Ð¾Ð³Ð¾ Ð¿Ð¾ÑÑÐ´ÐºÐ°](http://e-maxx.ru/algo/diofant_1_equation) ä¸å ¶è±æç¿»è¯ç [Linear Congruence Equation](https://cp-algorithms.com/algebra/linear_congruence_equation.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼å å®¹ææ¹å¨ï¼**

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/linear-equation.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/linear-equation.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [Great-designer](https://github.com/Great-designer), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [kZime](https://github.com/kZime), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [leoleoasd](https://github.com/leoleoasd), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [Persdre](https://github.com/Persdre), [Phemon](mailto:i@phemon.me), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [tsentau](https://github.com/tsentau)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
