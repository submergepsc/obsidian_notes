# åææ° - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/partition/

# åææ°

åæï¼å°èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæééæ­£æ´æ°åçè¡¨ç¤ºï¼

ð=ð1+ð2+â¦+ððð1â¥ð2â¥â¦â¥ððâ¥1n=r1+r2+â¦+rkr1â¥r2â¥â¦â¥rkâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¼ä¸­æ¯ä¸ªæ­£æ´æ°ç§°ä¸ºä¸ä¸ªé¨åï¼

åææ°ï¼ððpn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåææ¹æ³æ°ï¼

èª 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§çåææ°ï¼

n| 0| 1| 2| 3| 4| 5| 6| 7| 8  
---|---|---|---|---|---|---|---|---|---  
ððpn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1| 1| 2| 3| 5| 7| 11| 15| 22  
  
## k é¨åææ°

å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åææ°æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¨åçåæï¼ç§°ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ°ï¼è®°ä½ ð(ð,ð)p(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¾ç¶ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ° ð(ð,ð)p(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¶ä¹æ¯ä¸é¢æ¹ç¨çè§£æ°ï¼

ðâð=ð¦1+ð¦2+â¦+ð¦ðð¦1â¥ð¦2â¥â¦â¥ð¦ðâ¥0nâk=y1+y2+â¦+yky1â¥y2â¥â¦â¥ykâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æè¿ä¸ªæ¹ç¨éé¢æ°æ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¨åé 0ï¼åæ°æ ð(ð âð,ð)p(nâk,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªè§£ï¼å æ­¤æåå¼ï¼

ð(ð,ð)=ðâð=0ð(ðâð,ð)p(n,k)=âj=0kp(nâk,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¸é»ä¸¤ä¸ªåå¼ä½å·®ï¼å¾ï¼

ð(ð,ð)=ð(ðâ1,ðâ1)+ð(ðâð,ð)p(n,k)=p(nâ1,kâ1)+p(nâk,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æååºè¡¨æ ¼ï¼æ¯ä¸ªæ ¼éçæ°ï¼ç­äºå·¦ä¸æ¹çæ°ï¼å ä¸è¯¥æ ¼åä¸æ¹æ°ï¼æå¨åæ°ä¸ªæ ¼å­ä¸­çæ°ï¼

k| 0| 1| 2| 3| 4| 5| 6| 7| 8  
---|---|---|---|---|---|---|---|---|---  
ð(0,ð)p(0,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1| 0| 0| 0| 0| 0| 0| 0| 0  
ð(1,ð)p(1,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 0| 0| 0| 0| 0| 0| 0  
ð(2,ð)p(2,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 1| 0| 0| 0| 0| 0| 0  
ð(3,ð)p(3,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 1| 1| 0| 0| 0| 0| 0  
ð(4,ð)p(4,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 2| 1| 1| 0| 0| 0| 0  
ð(5,ð)p(5,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 2| 2| 1| 1| 0| 0| 0  
ð(6,ð)p(6,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 3| 3| 2| 1| 1| 0| 0  
ð(7,ð)p(7,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 3| 4| 3| 2| 1| 1| 0  
ð(8,ð)p(8,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 4| 5| 5| 3| 2| 1| 1  
  
### ä¾é¢

è®¡ç® k é¨åææ°

è®¡ç® ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ° ð(ð,ð)p(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤ç»è¾å ¥ï¼å ¶ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸º 1000010000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸º 10001000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ 10000071000007![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼

è§å¯è¡¨æ ¼ä¸éæ¨å¼ï¼æåæ´æ°å¯¹äºå­å¨æ´æå©ï¼ä¸é¾ååºç¨åºï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text #include <cstdio> #include <cstring> int p [ 10005 ][ 1005 ]; /*å°èªç¶æ°nåæä¸ºkä¸ªé¨åçæ¹æ³æ°*/ int main () { int n , k ; while ( ~ scanf ( "%d%d" , & n , & k )) { memset ( p , 0 , sizeof ( p )); p [ 0 ][ 0 ] = 1 ; int i ; for ( i = 1 ; i <= n ; ++ i ) { int j ; for ( j = 1 ; j <= k ; ++ j ) { if ( i \- j >= 0 ) /*p[i-j][j]ææé¨åå¤§äº1*/ { p [ i ][ j ] = ( p [ i \- j ][ j ] \+ p [ i \- 1 ][ j \- 1 ]) % 1000007 ; /*p[i-1][j-1]è³å°æä¸ä¸ªé¨åä¸º1ï¼*/ } } } printf ( "%d \n " , p [ n ][ k ]); } } ```   
---|---  
  
### çæå½æ°

ç±ç­æ¯æ°åæ±åå ¬å¼ï¼æï¼

11âð¥ð=1+ð¥ð+ð¥2ð+ð¥3ð+â¦11âxk=1+xk+x2k+x3k+â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1+ð1ð¥+ð2ð¥2+ð3ð¥3+â¦=11âð¥11âð¥211âð¥3â¦1+p1x+p2x2+p3x3+â¦=11âx11âx211âx3â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ°ï¼çæå½æ°ç¨å¾®å¤æï¼å ·ä½ååºå¦ä¸ï¼

ââð,ð=0ð(ð,ð)ð¥ðð¦ð=11âð¥ð¦11âð¥2ð¦11âð¥3ð¦â¦ân,k=0âp(n,k)xnyk=11âxy11âx2y11âx3yâ¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### Ferrers å¾

Ferrers å¾ï¼å°åæçæ¯ä¸ªé¨åç¨ç¹ç»æçè¡è¡¨ç¤ºï¼æ¯è¡ç¹çä¸ªæ°ä¸ºè¿ä¸ªé¨åçå¤§å°ï¼

æ ¹æ®åæçå®ä¹ï¼Ferrers å¾ä¸­ä¸åçè¡æç §éåçæ¬¡åºææ¾ï¼æé¿è¡å¨æä¸é¢ï¼

ä¾å¦ï¼åæ 12 =5 +4 +2 +112=5+4+2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Ferrers å¾ï¼

![](./images/ferrers.jpg)

å°ä¸ä¸ª Ferrers å¾æ²¿çå¯¹è§çº¿ç¿»è½¬ï¼å¾å°çæ° Ferrers å¾ç§°ä¸ºåå¾çå ±è½­ï¼æ°åæç§°ä¸ºååæçå ±è½­ï¼æ¾ç¶ï¼å ±è½­æ¯å¯¹ç§°çå ³ç³»ï¼

ä¾å¦ä¸è¿°åæ 12 =5 +4 +2 +112=5+4+2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ±è½­æ¯åæ 12 =4 +3 +2 +2 +112=4+3+2+2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æå¤§ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åææ°ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§é¨åä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæä¸ªæ°ï¼

æ ¹æ®å ±è½­çå®ä¹ï¼ææ¾ç¶ç»è®ºï¼

æå¤§ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åææ°ä¸ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ°ç¸åï¼åä¸º ð(ð,ð)p(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## äºå¼åææ°

äºå¼åææ°ï¼ðððpdn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåé¨åäºä¸ç¸åçåææ¹æ³æ°ï¼ï¼Differentï¼

n| 0| 1| 2| 3| 4| 5| 6| 7| 8  
---|---|---|---|---|---|---|---|---|---  
ðððpdn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1| 1| 1| 2| 2| 3| 4| 5| 6  
  
åæ ·å°ï¼å®ä¹äºå¼ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ° ðð(ð,ð)pd(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¡¨ç¤ºæå¤§æåº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¨åçäºå¼åæï¼æ¯è¿ä¸ªæ¹ç¨çè§£æ°ï¼

ð=ð1+ð2+â¦+ððð1>ð2>â¦>ððâ¥1n=r1+r2+â¦+rkr1>r2>â¦>rkâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®å ¨åä¸ï¼ä¹æ¯è¿ä¸ªæ¹ç¨çè§£æ°ï¼

ðâð=ð¦1+ð¦2+â¦+ð¦ðð¦1>ð¦2>â¦>ð¦ðâ¥0nâk=y1+y2+â¦+yky1>y2>â¦>ykâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éä¸ä¸é¢ä¸åçæ¯ï¼ç±äºäºå¼ï¼æ°æ¹ç¨ä¸­è³å¤åªæä¸ä¸ªé¨åä¸ºé¶ï¼æä¸åçç»è®ºï¼æ°æ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¨åé 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ°æ ðð(ð âð,ð)pd(nâk,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªè§£ï¼è¿é ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð â1kâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ç´æ¥å¾å°éæ¨ï¼

ðð(ð,ð)=ðð(ðâð,ðâ1)+ðð(ðâð,ð)pd(n,k)=pd(nâk,kâ1)+pd(nâk,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ ·åç»åæ°ä¸æ ·ååºè¡¨æ ¼ï¼æ¯ä¸ªæ ¼éçæ°ï¼ç­äºè¯¥æ ¼åä¸åä¸æ°ï¼æå¨åæ°ä¸ªæ ¼å­ä¸­çæ°ï¼å ä¸è¯¥æ ¼åä¸æ¹æ°ï¼æå¨åæ°ä¸ªæ ¼å­ä¸­çæ°ï¼

k| 0| 1| 2| 3| 4| 5| 6| 7| 8  
---|---|---|---|---|---|---|---|---|---  
ðð(0,ð)pd(0,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1| 0| 0| 0| 0| 0| 0| 0| 0  
ðð(1,ð)pd(1,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 0| 0| 0| 0| 0| 0| 0  
ðð(2,ð)pd(2,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 0| 0| 0| 0| 0| 0| 0  
ðð(3,ð)pd(3,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 1| 0| 0| 0| 0| 0| 0  
ðð(4,ð)pd(4,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 1| 0| 0| 0| 0| 0| 0  
ðð(5,ð)pd(5,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 2| 0| 0| 0| 0| 0| 0  
ðð(6,ð)pd(6,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 2| 1| 0| 0| 0| 0| 0  
ðð(7,ð)pd(7,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 3| 1| 0| 0| 0| 0| 0  
ðð(8,ð)pd(8,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 0| 1| 3| 2| 0| 0| 0| 0| 0  
  
### ä¾é¢

è®¡ç®äºå¼åææ°

è®¡ç®äºå¼åææ° ðððpdn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤ç»è¾å ¥ï¼å ¶ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸º 5000050000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ 10000071000007![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼

è§å¯è¡¨æ ¼ä¸éæ¨å¼ï¼æåæ´æ°å¯¹äºå­å¨æ´æå©ï¼ä»£ç ä¸­å°åä¸ä½ç¼©åäºç©ºé´ï¼ä» ä¿çç¸é»ä¸¤é¡¹ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text #include <cstdio> #include <cstring> int pd [ 50005 ][ 2 ]; /*å°èªç¶æ°nåæä¸ºkä¸ªé¨åçäºå¼æ¹æ³æ°*/ int main () { int n ; while ( ~ scanf ( "%d" , & n )) { memset ( pd , 0 , sizeof ( pd )); pd [ 0 ][ 0 ] = 1 ; int ans = 0 ; int j ; for ( j = 1 ; j < 350 ; ++ j ) { int i ; for ( i = 0 ; i < 350 ; ++ i ) { pd [ i ][ j & 1 ] = 0 ; /*pd[i][j]åªä¸pd[][j]åpd[][j-1]æå ³*/ } for ( i = 0 ; i <= n ; ++ i ) { if ( i \- j >= 0 ) /*pd[i-j][j]ææé¨åå¤§äº1*/ { pd [ i ][ j & 1 ] = ( pd [ i \- j ][ j & 1 ] \+ pd [ i \- j ][( j \- 1 ) & 1 ]) % 1000007 ; /*pd[i-j][j-1]è³å°æä¸ä¸ªé¨åä¸º1ï¼*/ } } ans = ( ans \+ pd [ n ][ j & 1 ]) % 1000007 ; } printf ( "%d \n " , ans ); } } ```   
---|---  
  
### å¥åææ°

å¥åææ°ï¼ðððpon![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåé¨åé½æ¯å¥æ°çåææ¹æ³æ°ï¼ï¼Oddï¼

æä¸ä¸ªæ¾ç¶çç­å¼ï¼

ââð=1(1+ð¥ð)=ââð=1(1âð¥2ð)ââð=1(1âð¥ð)=ââð=111âð¥2ðâ1âi=1â(1+xi)=âi=1â(1âx2i)âi=1â(1âxi)=âi=1â11âx2iâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æå·¦è¾¹æ¯äºå¼åææ°ççæå½æ°ï¼æå³è¾¹æ¯å¥åææ°ççæå½æ°ï¼ä¸¤è å¯¹åºç³»æ°ç¸åï¼å æ­¤ï¼å¥åææ°åäºå¼åææ°ç¸åï¼

ððð=ðððpon=pdn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä½æ¾ç¶ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨å¥åææ°åäºå¼ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨åææ°ä¸æ¯ä¸ä¸ªæ¦å¿µï¼è¿éå°±ä¸ååºäºï¼

åå¼å ¥ä¸¤ä¸ªæ¦å¿µï¼

äºå¼å¶åææ°ï¼ððððpden![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¨åæ°ä¸ºå¶æ°çäºå¼åææ¹æ³æ°ï¼ï¼Evenï¼

äºå¼å¥åææ°ï¼ððððpdon![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èªç¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¨åæ°ä¸ºå¥æ°çäºå¼åææ¹æ³æ°ï¼ï¼Oddï¼

å æ­¤æï¼

ððð=ðððð+ððððpdn=pden+pdon![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ ·ä¹æç¸åºç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¨æ¦å¿µï¼ç±äºè¿äºå¤æï¼ä¸åååºï¼

## äºè¾¹å½¢æ°å®ç

åç¬è§å¯åææ°ççæå½æ°çåæ¯é¨åï¼

ââð=1(1âð¥ð)âi=1â(1âxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°è¿é¨åå±å¼ï¼å¯ä»¥æ³å°äºå¼åæï¼ä¸äºå¼åææåºçé¨åæ°å¥å¶æ§æå ³ï¼

å ·ä½å°ï¼äºå¼å¶é¨åæå¨å±å¼å¼ä¸­è¢«æ­£åè®¡æ°ï¼äºå¼å¥é¨åæå¨å±å¼å¼ä¸­è¢«è´åè®¡æ°ï¼å æ­¤å±å¼å¼ä¸­åé¡¹ç³»æ°ä¸ºä¸¤æ¹æ³æ°ä¹å·®ï¼å³ï¼

ââð=0(ððððâðððð)ð¥ð=ââð=1(1âð¥ð)âi=0â(pdenâpdon)xn=âi=1â(1âxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¥ä¸æ¥è¯´æï¼å¤æ°æ åµä¸ï¼ä¸è¿°ä¸¤æ¹æ³æ°ç¸ç­ï¼å¨å±å¼å¼ä¸­ç³»æ°ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä» å¨å°æ°ä½ç½®ï¼ä¸¤æ¹æ³æ°ç¸å·® 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿éå¯ä»¥åå©æé å¯¹åºçåæ³ï¼

ç»åºæ¯ä¸ªäºå¼åæç Ferrers å¾ï¼æåä¸è¡ç§°ä¸ºè¿ä¸ªå¾çåºï¼åºä¸ç¹çä¸ªæ°è®°ä¸º ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Bottomï¼ï¼è¿æ¥æä¸é¢ä¸è¡çæåä¸ä¸ªç¹ä¸å¾ä¸­æç¹çæé¿ 4545![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åº¦è§çº¿æ®µï¼ç§°ä¸ºè¿ä¸ªå¾çå¡ï¼å¡ä¸ç¹çä¸ªæ°è®°ä¸º ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Slideï¼ï¼

![](./images/bottom_slide.jpg)

è¦æ³å¨äºå¼å¶é¨åæä¸äºå¼å¥é¨åæä¹é´æé å¯¹åºï¼å°±è¦å®ä¹åæ¢ï¼å¨ä¿è¯äºå¼æ¡ä»¶ä¸åçåæä¸ï¼ä½¿å¾è¡æ°æ¹å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åæ¢ Aï¼å½ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°äºç­äº ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶åï¼å°±å°åºç§»å°å³è¾¹ï¼æä¸ºä¸ä¸ªæ°å¡ï¼

åæ¢ Bï¼å½ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤§äº ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶åï¼å°±å°å¡ç§»å°ä¸è¾¹ï¼æä¸ºä¸ä¸ªæ°åºï¼

è¿ä¸¤ä¸ªåæ¢å¯¹äºå¤§å¤æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä»»æäºå¼åæï¼æ°æä¸ä¸ªåæ¢å¯ä»¥è¿è¡ï¼å°±å¨äºå¼å¶é¨åæä¸äºå¼å¥é¨åæä¹é´æé äºä¸ä¸ªä¸ä¸å¯¹åºï¼å·²ç»æé äºä¸ä¸å¯¹åºçä¸¤é¨ååæä¸ªæ°ç¸ç­ï¼å æ­¤è¿æ¶å±å¼å¼ä¸­ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ç³»æ°ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä½æ¯å¯¹äºæäº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶å­å¨æ°ä¸ä¸ªäºå¼åææ æ³è¿è¡ä¸è¿°åæ¢ï¼

  * æ åµä¸ï¼ð =ð b=s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åºä¸å¡æä¸ä¸ªå ¬å ±ç¹æ¶ï¼åæ¢ A ä¸è½è¿è¡ï¼æ­¤æ¶

ð=ð +(ð +1)+â¦+(ð +ð â1)=ð (3ð â1)2n=s+(s+1)+â¦+(s+sâ1)=s(3sâ1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å±å¼å¼çç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ä¸åæé¨åæ°çå¥å¶æ§æå ³ï¼ä¸º ( â1)ð ð¥ð(â1)sxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * æ åµäºï¼ð =ð  +1b=s+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åºä¸å¡æä¸ä¸ªå ¬å ±ç¹æ¶ï¼åæ¢ B ä¸è½è¿è¡ï¼æ­¤æ¶

ð=(ð +1)+(ð +2)+â¦+(ð +ð )=ð (3ð +1)2n=(s+1)+(s+2)+â¦+(s+s)=s(3s+1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å±å¼å¼çç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ä¸º ( â1)ð ð¥ð(â1)sxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¨ âð âs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢ä¸å¼ç ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å° ð =ð (3ð â1)2n=s(3sâ1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè´æ´æ°ï¼å±å¼å¼çç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ä»ä¸º ( â1)ð ð¥ð(â1)sxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼

ç±äºä¸¤ç§æ åµä¸ä¼å¨åä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¶åºç°ï¼æä»¬å¯ä»¥æä¸¤ä¸ªæ¡ä»¶åèµ·æ¥ï¼å¾å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¦æ»¡è¶³çæ¡ä»¶æ¯

âðââ¤,ð=ð(3ðâ1)2âkâZ,n=k(3kâ1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è³æ­¤ï¼æä»¬å°±è¯æäºï¼

(1âð¥)(1âð¥2)(1âð¥3)â¦=+ââð=ââ(â1)ðð¥ð(3ðâ1)2=â¦+ð¥26âð¥15+ð¥7âð¥2+1âð¥+ð¥5âð¥12+ð¥22ââ¦(1âx)(1âx2)(1âx3)â¦=âk=ââ+â(â1)kxk(3kâ1)2=â¦+x26âx15+x7âx2+1âx+x5âx12+x22ââ¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¿ä¸ä¸ï¼è¿ä¸ªå¼å­æ¯åææ°ççæå½æ°çåæ°ï¼å æ­¤å ¶ä¸åææ°ççæå½æ°ç¸ä¹çç»ææ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´çå¹¶å¯¹æ¯ä¸¤è¾¹åé¡¹ç³»æ°ï¼å°±å¾å°åææ°æ°åçéæ¨å¼ï¼

(1+ð1ð¥+ð2ð¥2+ð3ð¥3+â¦)(1âð¥âð¥2+ð¥5+ð¥7âð¥12âð¥15+ð¥22+ð¥26ââ¦)=1(1+p1x+p2x2+p3x3+â¦)(1âxâx2+x5+x7âx12âx15+x22+x26ââ¦)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ðð=ððâ1+ððâ2âððâ5âððâ7+â¦pn=pnâ1+pnâ2âpnâ5âpnâ7+â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªéæ¨å¼ææ éé¡¹ï¼ä½æ¯å¦æè§å®è´æ°çåææ°æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåææ°å·²ç»å®ä¹ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼é£ä¹å°±ç®åä¸ºäºæéé¡¹ï¼

### ä¾é¢

è®¡ç®åææ°

è®¡ç®åææ° ððpn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¤ç»è¾å ¥ï¼å ¶ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çä¸º 5000050000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹ 10000071000007![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼

éç¨äºè¾¹å½¢æ°å®ççæ¹æ³ï¼æä»£ç ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text #include <cstdio> long long a [ 100010 ]; long long p [ 50005 ]; int main () { p [ 0 ] = 1 ; p [ 1 ] = 1 ; p [ 2 ] = 2 ; int i ; for ( i = 1 ; i < 50005 ; i ++ ) /*éæ¨å¼ç³»æ°1,2,5,7,12,15,22,26...i*(3*i-1)/2,i*(3*i+1)/2*/ { a [ 2 * i ] = i * ( i * 3 \- 1 ) / 2 ; /*äºè¾¹å½¢æ°ä¸º1,5,12,22...i*(3*i-1)/2*/ a [ 2 * i \+ 1 ] = i * ( i * 3 \+ 1 ) / 2 ; } for ( i = 3 ; i < 50005 ; i ++ ) /*p[n]=p[n-1]+p[n-2]-p[n-5]-p[n-7]+p[12]+p[15]-...+p[n-i*[3i-1]/2]+p[n-i*[3i+1]/2]*/ { p [ i ] = 0 ; int j ; for ( j = 2 ; a [ j ] <= i ; j ++ ) /*æå¯è½ä¸ºè´æ°,å¼ä¸­å 1000007*/ { if ( j & 2 ) { p [ i ] = ( p [ i ] \+ p [ i \- a [ j ]] \+ 1000007 ) % 1000007 ; } else { p [ i ] = ( p [ i ] \- p [ i \- a [ j ]] \+ 1000007 ) % 1000007 ; } } } int n ; while ( ~ scanf ( "%d" , & n )) { printf ( "%lld \n " , p [ n ]); } } ```   
---|---  
  
* * *

> __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/partition.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/partition.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [2008verser](https://github.com/2008verser), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [ksyx](https://github.com/ksyx), [myeeye](https://github.com/myeeye), [Xeonacid](https://github.com/Xeonacid), [YOYO-UIAT](https://github.com/YOYO-UIAT)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
