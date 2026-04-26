# ä¸­å½å©ä½å®ç - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/crt/

# ä¸­å½å©ä½å®ç

## å¼å ¥

> ãç©ä¸ç¥æ°ãé®é¢ï¼æç©ä¸ç¥å ¶æ°ï¼ä¸ä¸æ°ä¹å©äºï¼äºäºæ°ä¹å©ä¸ï¼ä¸ä¸æ°ä¹å©äºï¼é®ç©å ä½ï¼

å³æ±æ»¡è¶³ä»¥ä¸æ¡ä»¶çæ´æ°ï¼é¤ä»¥ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¤ä»¥ 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¤ä»¥ 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯¥é®é¢ææ©è§äºãå­å­ç®ç»ãä¸­ï¼å¹¶æè¯¥é®é¢çå ·ä½è§£æ³ï¼å®ææ°å­¦å®¶ç§¦ä¹é¶äº 1247 å¹´ãæ°ä¹¦ä¹ç« ãå·ä¸ãäºãå¤§è¡ç±»ãå¯¹ãç©ä¸ç¥æ°ãé®é¢ååºäºå®æ´ç³»ç»çè§£ç­ï¼ä¸é¢å ·ä½é®é¢çè§£ç­å£è¯ç±æææ°å­¦å®¶ç¨å¤§ä½å¨ãç®æ³ç»å®ãä¸­ç»åºï¼

> ä¸äººåè¡ä¸åå¸ï¼äºæ æ¢ è±å»¿ä¸æ¯ï¼ä¸å­å¢åæ­£åæï¼é¤ç¾é¶äºä¾¿å¾ç¥ï¼

2 Ã70 +3 Ã21 +2 Ã15 =233 =2 Ã105 +232Ã70+3Ã21+2Ã15=233=2Ã105+23![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ç­æ¡ä¸º 2323![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å®ä¹

ä¸­å½å©ä½å®ç (Chinese Remainder Theorem, CRT) å¯æ±è§£å¦ä¸å½¢å¼çä¸å çº¿æ§åä½æ¹ç¨ç»ï¼å ¶ä¸­ ð1,ð2,â¯,ððn1,n2,â¯,nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸¤ä¸¤äºè´¨ï¼ï¼

â§{ { {â¨{ { {â©ð¥â¡ð1(modð1)ð¥â¡ð2(modð2)â®ð¥â¡ðð(modðð){xâ¡a1(modn1)xâ¡a2(modn2)â®xâ¡ak(modnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸é¢çãç©ä¸ç¥æ°ãé®é¢å°±æ¯ä¸å çº¿æ§åä½æ¹ç¨ç»çä¸ä¸ªå®ä¾ï¼

## è¿ç¨

  1. è®¡ç®æææ¨¡æ°çç§¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å¯¹äºç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¹ç¨ï¼
     1. è®¡ç® ðð =ðððmi=nni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     2. è®¡ç® ððmi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ððni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ç [éå ](../inverse/) ðâ1ðmiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
     3. è®¡ç® ðð =ðððâ1ðci=mimiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼**ä¸è¦å¯¹ ððni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡**ï¼ï¼
  3. æ¹ç¨ç»å¨æ¨¡ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸çå¯ä¸è§£ä¸ºï¼ð¥ =âðð=1ðððð(modð)x=âi=1kaici(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text LL CRT ( int k , LL * a , LL * r ) { LL n = 1 , ans = 0 ; for ( int i = 1 ; i <= k ; i ++ ) n = n * r [ i ]; for ( int i = 1 ; i <= k ; i ++ ) { LL m = n / r [ i ], b , y ; exgcd ( m , r [ i ], b , y ); // b * m mod r[i] = 1 ans = ( ans \+ a [ i ] * m * b % n ) % n ; } return ( ans % n \+ n ) % n ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text def CRT ( k , a , r ): n = 1 ans = 0 for i in range ( 1 , k \+ 1 ): n = n * r [ i ] for i in range ( 1 , k \+ 1 ): m = n // r [ i ] b = y = 0 exgcd ( m , r [ i ], b , y ) # b * m mod r[i] = 1 ans = ( ans \+ a [ i ] * m * b % n ) % n return ( ans % n \+ n ) % n ```   
---|---  
  
## è¯æ

æä»¬éè¦è¯æä¸é¢ç®æ³è®¡ç®æå¾ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹äºä»»æ ð =1,2,â¯,ði=1,2,â¯,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ ð¥ â¡ðð(modðð)xâ¡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å½ ð â ðiâ j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ ðð â¡0(modðð)mjâ¡0(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ðð â¡ðð â¡0(modðð)cjâ¡mjâ¡0(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ðð â¡ðð â (ðâ1ðmodðð) â¡1(modðð)ciâ¡miâ (miâ1modni)â¡1(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥æä»¬æï¼

ð¥â¡ðâð=1ðððð(modðð)â¡ðððð(modðð)â¡ððâ ððâ (ðâ1ðmodðð)(modðð)â¡ðð(modðð)xâ¡âj=1kajcj(modni)â¡aici(modni)â¡aiâ miâ (miâ1modni)(modni)â¡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³å¯¹äºä»»æ ð =1,2,â¯,ði=1,2,â¯,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸é¢ç®æ³å¾å°ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯æ»¡è¶³ ð¥ â¡ðð(modðð)xâ¡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³è¯æäºè§£åä½æ¹ç¨ç»çç®æ³çæ­£ç¡®æ§ï¼

å ä¸ºæä»¬æ²¡æå¯¹è¾å ¥ç ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç¹æ®éå¶ï¼æä»¥ä»»ä½ä¸ç»è¾å ¥ {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯¹åºä¸ä¸ªè§£ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦å¤ï¼è¥ ð¥ â ð¦xâ y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ»å­å¨ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ððni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸åä½ï¼æ ç³»æ°åè¡¨ {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è§£ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´æ¯ä¸ä¸æ å°å ³ç³»ï¼æ¹ç¨ç»æ»æ¯æå¯ä¸è§£ï¼

## è§£é

ä¸é¢æ¼ç¤º CRT å¦ä½è§£ãç©ä¸ç¥æ°ãé®é¢ï¼

  1. ð =3 Ã5 Ã7 =105n=3Ã5Ã7=105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. ä¸äººåè¡ **ä¸å** å¸ï¼ð1 =3,ð1 =ð/ð1 =35,ðâ11 â¡2(mod3)n1=3,m1=n/n1=35,m1â1â¡2(mod3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð1 =35 Ã2 =70c1=35Ã2=70![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. äºæ æ¢ è± **å»¿ä¸** æ¯ï¼ð2 =5,ð2 =ð/ð2 =21,ðâ12 â¡1(mod5)n2=5,m2=n/n2=21,m2â1â¡1(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð2 =21 Ã1 =21c2=21Ã1=21![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. ä¸å­å¢åæ­£ **åæ** ï¼ð3 =7,ð3 =ð/ð3 =15,ðâ13 â¡1(mod7)n3=7,m3=n/n3=15,m3â1â¡1(mod7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð3 =15 Ã1 =15c3=15Ã1=15![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  5. æä»¥æ¹ç¨ç»çå¯ä¸è§£ä¸º ð¥ â¡2 Ã70 +3 Ã21 +2 Ã15 â¡233 â¡23(mod105)xâ¡2Ã70+3Ã21+2Ã15â¡233â¡23(mod105)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼é¤ **ç¾é¶äº** ä¾¿å¾ç¥ï¼

## Garner ç®æ³

CRT çå¦ä¸ä¸ªç¨éæ¯ç¨ä¸ç»æ¯è¾å°çè´¨æ°è¡¨ç¤ºä¸ä¸ªå¤§çæ´æ°ï¼

ä¾å¦ï¼è¥ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å¦ä¸çº¿æ§æ¹ç¨ç»ï¼ä¸ ð <âðð=1ðða<âi=1kpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè´¨æ°ï¼ï¼

â§{ { {â¨{ { {â©ðâ¡ð1(modð1)ðâ¡ð2(modð2)â®ðâ¡ðð(modðð){aâ¡a1(modp1)aâ¡a2(modp2)â®aâ¡ak(modpk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¬å¯ä»¥ç¨ä»¥ä¸å½¢å¼çå¼å­ï¼ç§°ä½ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ··ååºæ°è¡¨ç¤ºï¼è¡¨ç¤º ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ð=ð¥1+ð¥2ð1+ð¥3ð1ð2+â¦+ð¥ðð1â¦ððâ1a=x1+x2p1+x3p1p2+â¦+xkp1â¦pkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**Garner ç®æ³** å°ç¨æ¥è®¡ç®ç³»æ° ð¥1,â¦,ð¥ðx1,â¦,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»¤ ðððrij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ððpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ððpj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ç [é](../inverse/)ï¼

ððâ ðð,ðâ¡1(modðð)piâ ri,jâ¡1(modpj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»£å ¥æä»¬å¾å°çç¬¬ä¸ä¸ªæ¹ç¨ï¼

ð1â¡ð¥1(modð1)a1â¡x1(modp1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥ç¬¬äºä¸ªæ¹ç¨å¾åºï¼

ð2â¡ð¥1+ð¥2ð1(modð2)a2â¡x1+x2p1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¹ç¨ä¸¤è¾¹å ð¥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¤ ð1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¾

ð2âð¥1â¡ð¥2ð1(modð2)(ð2âð¥1)ð1,2â¡ð¥2(modð2)ð¥2â¡(ð2âð¥1)ð1,2(modð2)a2âx1â¡x2p1(modp2)(a2âx1)r1,2â¡x2(modp2)x2â¡(a2âx1)r1,2(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±»ä¼¼å°ï¼æä»¬å¯ä»¥å¾å°ï¼

ð¥ð=(â¦((ððâð¥1)ð1,ðâð¥2)ð2,ð)ââ¦)ððâ1,ðmodððxk=(â¦((akâx1)r1,kâx2)r2,k)ââ¦)rkâ1,kmodpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text for ( int i = 0 ; i < k ; ++ i ) { x [ i ] = a [ i ]; for ( int j = 0 ; j < i ; ++ j ) { x [ i ] = r [ j ][ i ] * ( x [ i ] \- x [ j ]); x [ i ] = x [ i ] % p [ i ]; if ( x [ i ] < 0 ) x [ i ] += p [ i ]; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text for i in range ( 0 , k ): x [ i ] = a [ i ] for j in range ( 0 , i ): x [ i ] = r [ j ][ i ] * ( x [ i ] \- x [ j ]) x [ i ] = x [ i ] % p [ i ] if x [ i ] < 0 : x [ i ] = x [ i ] \+ p [ i ] ```   
---|---  
  
è¯¥ç®æ³çæ¶é´å¤æåº¦ä¸º ð(ð2)O(k2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®é ä¸ Garner ç®æ³å¹¶ä¸è¦æ±æ¨¡æ°ä¸ºè´¨æ°ï¼åªè¦æ±æ¨¡æ°ä¸¤ä¸¤äºè´¨ï¼æä»¬æå¦ä¸ä¼ªä»£ç ï¼

ðð¡ð¢ð§ðð¬ð ððð¦ðð¢ð§ððð« ðð¥ð ð¨ð«ð¢ð­ð¡ð¦Â craâ¡(ð¯,ð¦):ðð§ð©ð®ð­:Â ð¦=(ð0,ð1,â¦,ððâ1),Â ððââ¤+â§gcd(ðð,ðð)=1Â for allÂ ðâ ð,ð¯=(ð£0,â¦,ð£ðâ1)Â whereÂ ð£ð=ð¥modðð.ðð®ð­ð©ð®ð­:Â ð¥modâðâ1ð=0ðð.1ðð¨ð«Â ðÂ fromÂ 1Â toÂ (ðâ1)Â ðð¨2ð¶ðâ(âðâ1ð=0ðð)â1modðð3ð¥âð£04ðð¨ð«Â ðÂ fromÂ 1Â toÂ (ðâ1)Â ðð¨5ð¢â(ð£ðâð¥)â ð¶ðmodðð6ð¥âð¥+ð¢âðâ1ð=0ðð7ð«ðð­ð®ð«ð§Â (ð¥)Chinese Remainder AlgorithmÂ craâ¡(v,m):Input:Â m=(m0,m1,â¦,mnâ1),Â miâZ+â§gcd(mi,mj)=1Â for allÂ iâ j,v=(v0,â¦,vnâ1)Â whereÂ vi=xmodmi.Output:Â xmodâi=0nâ1mi.1forÂ iÂ fromÂ 1Â toÂ (nâ1)Â do2Ciâ(âj=0iâ1mj)â1modmi3xâv04forÂ iÂ fromÂ 1Â toÂ (nâ1)Â do5uâ(viâx)â Cimodmi6xâx+uâj=0iâ1mj7returnÂ (x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥åç°å¨ç¬¬å ­è¡ä¸­çè®¡ç®è¿ç¨å¯¹åºä¸è¿°æ··ååºæ°çè¡¨ç¤ºï¼

## åºç¨

æäºè®¡æ°é®é¢ææ°è®ºé®é¢åºäºå é¿ä»£ç ãå¢å é¾åº¦ãæè æ¯ä¸äºå ¶ä»åå ï¼ç»åºçæ¨¡æ°ï¼**ä¸æ¯è´¨æ°** ï¼

ä½æ¯å¯¹å ¶è´¨å æ°åè§£ä¼åç°å®æ²¡æå¹³æ¹å å­ï¼ä¹å°±æ¯è¯¥æ¨¡æ°æ¯ç±ä¸äºä¸éå¤çè´¨æ°ç¸ä¹å¾å°ï¼

é£ä¹æä»¬å¯ä»¥åå«å¯¹è¿äºæ¨¡æ°è¿è¡è®¡ç®ï¼æåç¨ CRT åå¹¶ç­æ¡ï¼

ä¸é¢è¿éé¢å°±æ¯ä¸ä¸ªä¸éçä¾å­ï¼

[æ´è°· P2480 [SDOI2010] å¤ä»£çªæ](https://www.luogu.com.cn/problem/P2480)

ç»åº ðº,ðG,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼1 â¤ðº,ð â¤1091â¤G,nâ¤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼æ±ï¼

ðºâðâ£ð(ðð)mod999Â 911Â 659Gâkâ£n(nk)mod999Â 911Â 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é¦å ï¼å½ ðº =999Â 911Â 659G=999Â 911Â 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ææ±æ¾ç¶ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦åï¼æ ¹æ® [æ¬§æå®ç](../fermat/)ï¼å¯ç¥ææ±ä¸ºï¼

ðºâðâ£ð(ðð)mod999Â 911Â 658mod999Â 911Â 659Gâkâ£n(nk)mod999Â 911Â 658mod999Â 911Â 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç°å¨èèå¦ä½è®¡ç®ï¼

âðâ£ð(ðð)mod999Â 911Â 658âkâ£n(nk)mod999Â 911Â 658![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ä¸º 999Â 911Â 658999Â 911Â 658![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯è´¨æ°ï¼æ æ³ä¿è¯ âð¥ â[1,999Â 911Â 657]âxâ[1,999Â 911Â 657]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æéå å­å¨ï¼ä¸é¢è¿ä¸ªå¼å­æä»¬æ æ³ç´æ¥è®¡ç®ï¼

æ³¨æå° 999Â 911Â 658 =2 Ã3 Ã4679 Ã35617999Â 911Â 658=2Ã3Ã4679Ã35617![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­æ¯ä¸ªè´¨å å­çæé«æ¬¡æ°åä¸ºä¸ï¼æä»¬å¯ä»¥èèåå«æ±åº âðâ£ð(ðð)âkâ£n(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼46794679![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼3561735617![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿å ä¸ªè´¨æ°ä¸çç»æï¼æåç¨ä¸­å½å©ä½å®çæ¥åå¹¶ç­æ¡ï¼

ä¹å°±æ¯è¯´ï¼æä»¬å®é ä¸è¦æ±ä¸é¢ä¸ä¸ªçº¿æ§æ¹ç¨ç»çè§£ï¼

â§{ { {â¨{ { {â©ð¥â¡ð1(mod2)ð¥â¡ð2(mod3)ð¥â¡ð3(mod4679)ð¥â¡ð4(mod35617){xâ¡a1(mod2)xâ¡a2(mod3)xâ¡a3(mod4679)xâ¡a4(mod35617)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èè®¡ç®ä¸ä¸ªç»åæ°å¯¹è¾å°çè´¨æ°åæ¨¡åçç»æï¼å¯ä»¥å©ç¨ [å¢å¡æ¯å®ç](../lucas/)ï¼

## æ©å±ï¼æ¨¡æ°ä¸äºè´¨çæ åµ

### ä¸¤ä¸ªæ¹ç¨

è®¾ä¸¤ä¸ªæ¹ç¨åå«æ¯ ð¥ â¡ð1(modð1)xâ¡a1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãð¥ â¡ð2(modð2)xâ¡a2(modm2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å°å®ä»¬è½¬åä¸ºä¸å®æ¹ç¨ï¼ð¥ =ð1ð +ð1 =ð2ð +ð2x=m1p+a1=m2q+a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð,ðp,q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ´æ°ï¼åæ ð1ð âð2ð =ð2 âð1m1pâm2q=a2âa1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç± [è£´èå®ç](../bezouts/)ï¼å½ ð2 âð1a2âa1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è½è¢« gcd(ð1,ð2)gcd(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´é¤æ¶ï¼æ è§£ï¼

å ¶ä»æ åµä¸ï¼å¯ä»¥éè¿ [æ©å±æ¬§å éå¾ç®æ³](../gcd/) è§£åºæ¥ä¸ç»å¯è¡è§£ (ð,ð)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ååæ¥çä¸¤æ¹ç¨ç»æçæ¨¡æ¹ç¨ç»çè§£ä¸º ð¥ â¡ð(modð)xâ¡b(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð =ð1ð +ð1b=m1p+a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð =lcm(ð1,ð2)M=lcm(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å¤ä¸ªæ¹ç¨

ç¨ä¸é¢çæ¹æ³ä¸¤ä¸¤åå¹¶å³å¯ï¼

## ä¹ é¢

  * [ãæ¨¡æ¿ãä¸­å½å©ä½å®çï¼CRTï¼/æ¹å²å »çª](https://www.luogu.com.cn/problem/P1495)
  * [ãæ¨¡æ¿ãæ©å±ä¸­å½å©ä½å®ç](https://www.luogu.com.cn/problem/P4777)
  * [ãNOI2018ãå± é¾åå£«](https://uoj.ac/problem/396)
  * [ãTJOI2009ãçæ°å­](https://www.luogu.com.cn/problem/P3868)

**æ¬é¡µé¢é¨åå å®¹è¯èªåæ[ÐÐ¸ÑÐ°Ð¹ÑÐºÐ°Ñ ÑÐµÐ¾ÑÐµÐ¼Ð° Ð¾Ð± Ð¾ÑÑÐ°ÑÐºÐ°Ñ ](http://e-maxx.ru/algo/chinese_theorem) ä¸å ¶è±æç¿»è¯ç [Chinese Remainder Theorem](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/crt.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/crt.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [sshwy](https://github.com/sshwy), [Chrogeek](https://github.com/Chrogeek), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [383494](https://github.com/383494), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [kzoacn](https://github.com/kzoacn), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [stevebraveman](https://github.com/stevebraveman), [Suyun514](mailto:suyun514@qq.com), [Unnamed2964](https://github.com/Unnamed2964), [weiyong1024](https://github.com/weiyong1024), [ChungZH](https://github.com/ChungZH), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [hly1204](https://github.com/hly1204), [ImpleLee](https://github.com/ImpleLee), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [little-cindy](https://github.com/little-cindy), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [namasikanam](https://github.com/namasikanam), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [Phemon](mailto:i@phemon.me), [renbaoshuo](https://github.com/renbaoshuo), [shawlleyw](https://github.com/shawlleyw), [SukkaW](https://github.com/SukkaW), [xyf007](https://github.com/xyf007)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
