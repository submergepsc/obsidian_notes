# æ¬§æå½æ° - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/euler-totient/

# æ¬§æå½æ°

## å®ä¹

æ¬§æå½æ°ï¼Euler's totient functionï¼ï¼å³ ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¡¨ç¤ºçæ¯å°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè´¨çæ°çä¸ªæ°ï¼

æ¯å¦è¯´ ð(1) =1Ï(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è´¨æ°çæ¶åï¼æ¾ç¶æ ð(ð) =ð â1Ï(n)=nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## æ§è´¨

  * æ¬§æå½æ°æ¯ [ç§¯æ§å½æ°](../basic/#ç§¯æ§å½æ°)ï¼

å³å¯¹ä»»ææ»¡è¶³ gcd(ð,ð) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð(ðð) =ð(ð)ð(ð)Ï(ab)=Ï(a)Ï(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¹å«å°ï¼å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥æ°æ¶ ð(2ð) =ð(ð)Ï(2n)=Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æåè§ [å©ä½ç³»çå¤å](../basic/#å©ä½ç³»çå¤å)ï¼

  * ð =âðâ£ðð(ð)n=âdâ£nÏ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

å©ç¨ [è«æ¯ä¹æ¯åæ¼](../mobius/) ç¸å ³ç¥è¯å¯ä»¥å¾åºï¼

ä¹å¯ä»¥è¿æ ·èèï¼å¦æ gcd(ð,ð) =ðgcd(k,n)=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ gcd(ðð,ðð) =1,(ð <ð)gcd(kd,nd)=1,(k<n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦ææä»¬è®¾ ð(ð¥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º gcd(ð,ð) =ð¥gcd(k,n)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°çä¸ªæ°ï¼é£ä¹ ð =âðð=1ð(ð)n=âi=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ ¹æ®ä¸é¢çè¯æï¼æä»¬åç°ï¼ð(ð¥) =ð(ðð¥)f(x)=Ï(nx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»è ð =âðâ£ðð(ðð)n=âdâ£nÏ(nd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ³¨æå°çº¦æ° ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððnd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ·æå¯¹ç§°æ§ï¼æä»¥ä¸å¼åä¸º ð =âðâ£ðð(ð)n=âdâ£nÏ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * è¥ ð =ððn=pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è´¨æ°ï¼é£ä¹ ð(ð) =ðð âððâ1Ï(n)=pkâpkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ ï¼æ ¹æ®å®ä¹å¯ç¥ï¼

  * ç±å¯ä¸åè§£å®çï¼è®¾ ð =âð ð=1ððððn=âi=1spiki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è´¨æ°ï¼æ ð(ð) =ð Ãâð ð=1ððâ1ððÏ(n)=nÃâi=1spiâ1pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ
    * å¼çï¼è®¾ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä»»æè´¨æ°ï¼é£ä¹ ð(ðð) =ððâ1 Ã(ð â1)Ï(pk)=pkâ1Ã(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æï¼æ¾ç¶å¯¹äºä» 1 å° ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæææ°ä¸­ï¼é¤äº ððâ1pkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ä»¥å¤å ¶å®æ°é½ä¸ ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼æ ð(ðð) =ðð âððâ1 =ððâ1 Ã(ð â1)Ï(pk)=pkâpkâ1=pkâ1Ã(pâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯æ¯ï¼

æ¥ä¸æ¥æä»¬è¯æ ð(ð) =ð Ãâð ð=1ððâ1ððÏ(n)=nÃâi=1spiâ1pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±å¯ä¸åè§£å®çä¸ ð(ð¥)Ï(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½æ°çç§¯æ§

ð(ð)=ð âð=1ð(ðððð)=ð âð=1(ððâ1)Ãððððâ1=ð âð=1ððððÃ(1â1ðð)=ðÂ ð âð=1(1â1ðð)â»Ï(n)=âi=1sÏ(piki)=âi=1s(piâ1)Ãpikiâ1=âi=1spikiÃ(1â1pi)=nÂ âi=1s(1â1pi)â»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * å¯¹ä»»æä¸å ¨ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ð,ðm,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð(ðð)ð(gcd(ð,ð)) =ð(ð)ð(ð)gcd(ð,ð)Ï(mn)Ï(gcd(m,n))=Ï(m)Ï(n)gcd(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯ç±ä¸ä¸æ¡ç´æ¥è®¡ç®å¾åºï¼

## å®ç°

å¦æåªè¦æ±ä¸ä¸ªæ°çæ¬§æå½æ°å¼ï¼é£ä¹ç´æ¥æ ¹æ®å®ä¹è´¨å æ°åè§£çåæ¶æ±å°±å¥½äºï¼è¿ä¸ªè¿ç¨å¯ä»¥ç¨ [Pollard Rho](../pollard-rho/) ç®æ³ä¼åï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text #include <cmath> int euler_phi ( int n ) { int ans = n ; for ( int i = 2 ; i * i <= n ; i ++ ) if ( n % i == 0 ) { ans = ans / i * ( i \- 1 ); while ( n % i == 0 ) n /= i ; } if ( n > 1 ) ans = ans / n * ( n \- 1 ); return ans ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text import math def euler_phi ( n ): ans = n for i in range ( 2 , math . isqrt ( n ) \+ 1 ): if n % i == 0 : ans = ans // i * ( i \- 1 ) while n % i == 0 : n = n // i if n > 1 : ans = ans // n * ( n \- 1 ) return ans ```   
---|---  
  
å¦ææ¯å¤ä¸ªæ°çæ¬§æå½æ°å¼ï¼å¯ä»¥å©ç¨åé¢ä¼æå°ççº¿æ§ç­æ³æ¥æ±å¾ï¼

è¯¦è§ï¼[ç­æ³æ±æ¬§æå½æ°](../sieve/#ç­æ³æ±æ¬§æå½æ°)

## åºç¨

æ¬§æå½æ°å¸¸å¸¸ç¨äºåç®ä¸åæå¤§å ¬çº¦æ°çåï¼å½å æäºæç« ç§°å®ä¸º **æ¬§æåæ¼**1ï¼

å¨ç»è®º

ð=âð|ðð(ð)n=âd|nÏ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸­ä»£å ¥ ð =gcd(ð,ð)n=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ

gcd(ð,ð)=âð|gcd(ð,ð)ð(ð)=âð[ð|ð][ð|ð]ð(ð),gcd(a,b)=âd|gcd(a,b)Ï(d)=âd[d|a][d|b]Ï(d),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ [ â ][â ]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º Iverson æ¬å·ï¼å¯¹ä¸å¼æ±åï¼å°±å¯ä»¥å¾å°

ðâð=1gcd(ð,ð)=âððâð=1[ð|ð][ð|ð]ð(ð)=âðâððâ[ð|ð]ð(ð)=âð|ðâððâð(ð).âi=1ngcd(i,n)=âdâi=1n[d|i][d|n]Ï(d)=âdândâ[d|n]Ï(d)=âd|nândâÏ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éå ³é®çè§å¯æ¯ âðð=1[ð|ð] =âððââi=1n[d|i]=ândâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å¨ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´è½å¤è¢« ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´é¤ç ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°æ¯ âððâândâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å©ç¨è¿ä¸ªå¼å­ï¼å°±å¯ä»¥éåçº¦æ°æ±åäºï¼éè¦å¤ç»æ¥è¯¢çæ¶åï¼å¯ä»¥é¢å¤çæ¬§æå½æ°çåç¼åï¼å©ç¨æ°è®ºååæ¥è¯¢ï¼

[GCD SUM](https://www.luogu.com.cn/problem/P2398)

ç»å® ð â¤100000nâ¤100000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±

ðâð=1ðâð=1gcd(ð,ð).âi=1nâj=1ngcd(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè·¯

ä»¿ç §ä¸æçæ¨å¯¼ï¼å¯ä»¥å¾åº

ðâð=1ðâð=1gcd(ð,ð)=ðâð=1âððâ2ð(ð).âi=1nâj=1ngcd(i,j)=âd=1nândâ2Ï(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤æ¶éè¦ä» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éåå° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±æ¬§æå½æ°ï¼ç¨çº¿æ§ç­åå°±å¯ä»¥ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°ç­æ¡ï¼

## æ¬§æå®ç

ä¸æ¬§æå½æ°ç´§å¯ç¸å ³çä¸ä¸ªå®çå°±æ¯æ¬§æå®çï¼å ¶æè¿°å¦ä¸ï¼

è¥ gcd(ð,ð) =1gcd(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ðð(ð) â¡1(modð)aÏ(m)â¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### æ©å±æ¬§æå®ç

å½ç¶ä¹ææ©å±æ¬§æå®çï¼ç¨äºå¤çä¸è¬ç ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

ððâ¡â§{ {â¨{ {â©ððmodð(ð),gcd(ð,ð)=1ðð,gcd(ð,ð)â 1,ð<ð(ð)ððmodð(ð)+ð(ð),gcd(ð,ð)â 1,ðâ¥ð(ð)(modð)abâ¡{abmodÏ(m),gcd(a,m)=1ab,gcd(a,m)â 1,b<Ï(m)abmodÏ(m)+Ï(m),gcd(a,m)â 1,bâ¥Ï(m)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æåä¹ é¢è¯¦è§ [æ¬§æå®ç](../fermat/)ï¼

## ä¹ é¢

  * [SPOJ ETF. Euler Totient Function](http://www.spoj.com/problems/ETF/)
  * [UVa 10179. Irreducible Basic Fractions](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
  * [UVa 10299. Relatives](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
  * [UVa 11327. Enumerating Rational Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
  * [TIMUS 1673. Admission to Exam](http://acm.timus.ru/problem.aspx?space=1&num=1673)
  * [Luogu P1390 å ¬çº¦æ°çå](https://www.luogu.com.cn/problem/P1390)
  * [Luogu P2155 [SDOI2008] æ²æå ¬ä¸»çå°æ](https://www.luogu.com.cn/problem/P2155)
  * [Luogu P2568 GCD](https://www.luogu.com.cn/problem/P2568)

## åèèµæä¸æ³¨é

* * *

  1. è¿ä¸è¯´æ³å¹¶æªè§äºå­¦æ¯æåæå½å¤çè®ºåä¸­ï¼å¨ä½¿ç¨è¯¥è¯´æ³æ¶åºå½æ³¨æï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/euler-totient.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/euler-totient.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [guodong2005](https://github.com/guodong2005), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [MegaOwIer](https://github.com/MegaOwIer), [StudyingFather](https://github.com/StudyingFather), [Chrogeek](https://github.com/Chrogeek), [mgt](mailto:i@margatroid.xyz), [shuzhouliu](https://github.com/shuzhouliu), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [frank-xjh](https://github.com/frank-xjh), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [henrytbtrue](https://github.com/henrytbtrue), [kZime](https://github.com/kZime), [lihaoyu1234](https://github.com/lihaoyu1234), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [nalemy](https://github.com/nalemy), [orzAtalod](https://github.com/orzAtalod), [ouuan](https://github.com/ouuan), [Persdre](https://github.com/Persdre), [segment-tree](https://github.com/segment-tree), [ShaoChenHeng](https://github.com/ShaoChenHeng), [Struggler-q](https://github.com/Struggler-q), [yuhuoji](https://github.com/yuhuoji), [ksyx](https://github.com/ksyx), [Pinghigh](https://github.com/Pinghigh), [shawlleyw](https://github.com/shawlleyw), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TrisolarisHD](https://github.com/TrisolarisHD)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
