# æ¨¡éå - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/inverse/

# æ¨¡éå 

æ¬æä»ç»æ¨¡æä¹ä¸ä¹æ³è¿ç®çéå ï¼å¹¶è®¨è®ºå®çå¸¸è§æ±è§£æ¹æ³ï¼

## åºæ¬æ¦å¿µ

éé¶å®æ° ð âðaâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹æ³éå å°±æ¯å®çåæ° ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±»ä¼¼å°ï¼æ°è®ºä¸­ä¹å¯ä»¥å®ä¹ä¸ä¸ªæ´æ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸çéå  ðâ1modðaâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç®åå°è®°ä½ ðâ1aâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±æ¯ **æ¨¡éå ** ï¼modular multiplicative inverseï¼ï¼ä¹ç§°ä½ **æ°è®ºåæ°** ï¼

éå 

å¯¹äºéé¶æ´æ° ð,ða,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå­å¨ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð â¡1(modð)abâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±ç§° ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ç **éå ** ï¼inverseï¼ï¼

è¿ç¸å½äºè¯´ï¼ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯çº¿æ§åä½æ¹ç¨ ðð¥ â¡1(modð)axâ¡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ï¼æ ¹æ® [çº¿æ§åä½æ¹ç¨](../linear-equation/) çæ§è´¨å¯ç¥ï¼å½ä¸ä» å½ gcd(ð,ð) =1gcd(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ð,ða,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ æ¶ï¼éå  ðâ1modðaâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼ä¸å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä¹ä¸æ¯å¯ä¸çï¼

## åä¸ªéå çæ±æ³

å©ç¨æ©å±æ¬§å éå¾ç®æ³æå¿«éå¹æ³ï¼å¯ä»¥å¨ ð(logâ¡ð)O(logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±åºåä¸ªæ´æ°çéå ï¼

### æ©å±æ¬§å éå¾ç®æ³

æ±è§£éå ï¼å°±ç¸å½äºæ±è§£çº¿æ§åä½æ¹ç¨ï¼å æ­¤ï¼å¯ä»¥ä½¿ç¨ [æ©å±æ¬§å éå¾ç®æ³](../gcd/#æ©å±æ¬§å) å¨ ð(logâ¡min{ð,ð})O(logâ¡min{a,m})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±è§£éå ï¼åæ¶ï¼ç±äºéå å¯¹åºççº¿æ§æ¹ç¨æ¯è¾ç¹æ®ï¼å¯ä»¥éå½å°ç®åç¸åºçæ­¥éª¤ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text // Extended Euclidean algorithm. void ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; } else { ex_gcd ( b , a % b , y , x ); y -= a / b * x ; } } // Returns the modular inverse of a modulo m. // Assumes that gcd(a, m) = 1, so the inverse exists. int inverse ( int a , int m ) { int x , y ; ex_gcd ( a , m , x , y ); return ( x % m \+ m ) % m ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text # Extended Euclidean algorithm. def ex_gcd ( a , b ): if b == 0 : return 1 , 0 else : x1 , y1 = ex_gcd ( b , a % b ) x = y1 y = x1 \- ( a // b ) * y1 return x , y # Returns the modular inverse of a modulo m. # Assumes that gcd(a, m) = 1, so the inverse exists. def inverse ( a , m ): x , y = ex_gcd ( a , m ) return ( x % m \+ m ) % m ```   
---|---  
  
è¿ä¸ç®æ³éç¨äºææéå å­å¨çæ å½¢ï¼

### å¿«éå¹æ³

è¿ä¸æ¹æ³ä¸»è¦éç¨äºæ¨¡æ°æ¯ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶ï¼ç± [è´¹é©¬å°å®ç](../fermat/#è´¹é©¬å°å®ç) å¯ç¥å¯¹äºä»»æ ð âðaâp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ

ðâ ððâ2=ððâ1â¡1(modð).aâ apâ2=apâ1â¡1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®éå çå¯ä¸æ§å¯ç¥ï¼éå  ðâ1modðaâ1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ç­äº ððâ2modðapâ2modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å¯ä»¥ç´æ¥ä½¿ç¨ [å¿«éå¹](../../binary-exponentiation/) å¨ ð(logâ¡ð)O(logâ¡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text // Binary exponentiation. int pow ( int a , int b , int m ) { long long res = 1 , po = a ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * po % m ; po = po * po % m ; } return res ; } // Returns the modular inverse of a prime modulo p. int inverse ( int a , int p ) { return pow ( a , p \- 2 , p ); } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text # Returns the modular inverse of a prime modulo p. # Use built-in pow function. def inverse ( a , p ): return pow ( a , p \- 2 , p ) ```   
---|---  
  
å½ç¶ï¼çè®ºä¸ï¼è¿ä¸æ¹æ³å¯ä»¥å©ç¨ [æ¬§æå®ç](../fermat/#æ¬§æå®ç) æ¨å¹¿å°ä¸è¬çæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å³å©ç¨ ðð(ð)â1modðaÏ(m)â1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç®éå ï¼ä½æ¯ï¼åæ¬¡æ±è§£ [æ¬§æå½æ°](../euler-totient/) ð(ð)Ï(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸å®¹æï¼å æ­¤è¯¥ç®æ³å¨ä¸è¬æ åµä¸æçä¸é«ï¼

## å¤ä¸ªéå çæ±æ³

æäºåºæ¯ä¸ï¼éè¦å¿«éå¤çåºå¤ä¸ªæ´æ° ð1,ð2,â¯,ðða1,a2,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸çéå ï¼æ­¤æ¶ï¼éä¸ªæ±è§£éå ï¼æ»å ±éè¦ ð(ðlogâ¡ð)O(nlogâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´ï¼å®é ä¸ï¼å¦æå°å®ä»¬ç»ä¸å¤çï¼å°±å¯ä»¥å¨ ð(ð +logâ¡ð)O(n+logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å æ±åºæææ´æ°çéå ï¼

èèåºå {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåç¼ç§¯ï¼

ð0=1,Â ðð=ððððâ1,Â ð=1,2,â¯,ð.S0=1,Â Si=aiSiâ1,Â i=1,2,â¯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åªè¦æ¯ä¸ª ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å®ä»¬çä¹ç§¯ ððSn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å æ­¤ï¼å¯ä»¥éè¿åææè¿°ç®æ³æ±åº ðâ1ðmodðSnâ1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å ä¸ºä¹ç§¯çéå å°±æ¯éå çä¹ç§¯ï¼æä»¥ï¼ä» ðâ1ðSnâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼ååéååºåå°±è½æ±åºæ¯ä¸ª ððSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå ï¼

ðâ1ðâ1=ðððâ1ðmodð,Â ð=ð,ðâ1,â¯,1.Siâ1â1=aiSiâ1modm,Â i=n,nâ1,â¯,1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±æ­¤ï¼åä¸ª ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå å¯ä»¥éè¿ä¸å¼è®¡ç®ï¼

ðâ1ð=ððâ1ðâ1ðmodð,Â ð=1,2,â¯,ð.aiâ1=Siâ1Siâ1modm,Â i=1,2,â¯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åèå®ç°å¦ä¸ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text // Returns the modular inverses for each x in a modulo m. // Assume x mod m exists for each x in a. std :: vector < int > batch_inverse ( const std :: vector < int >& a , int m ) { int n = a . size (); std :: vector < int > prod ( n ); long long s = 1 ; for ( int i = 0 ; i < n ; ++ i ) { // prod[i] = product of a[0...i-1]; prod[0] = 1. prod [ i ] = s ; s = s * a [ i ] % m ; } // s = product of all elements in a. s = inverse ( s , m ); std :: vector < int > res ( n ); for ( int i = n \- 1 ; i >= 0 ; \-- i ) { res [ i ] = s * prod [ i ] % m ; s = s * a [ i ] % m ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # Returns the modular inverses for each x in a modulo m. # Assume x mod m exists for each x in a. def batch_inverse ( a , m ): n = len ( a ) prod = [ 0 ] * n s = 1 for i in range ( n ): # prod[i] = product of a[0...i-1]; prod[0] = 1. prod [ i ] = s s = s * a [ i ] % m # s = product of all elements in a. s = inverse ( s , m ) res = [ 0 ] * n for i in reversed ( range ( n )): res [ i ] = s * prod [ i ] % m s = s * a [ i ] % m return res ```   
---|---  
  
ç®æ³ä¸­ï¼åªæ±äºä¸æ¬¡åä¸ªå ç´ çéå ï¼å æ­¤æ»çæ¶é´å¤æåº¦æ¯ ð(ð +logâ¡ð)O(n+logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

## çº¿æ§æ¶é´é¢å¤çéå 

å¦æè¦é¢å¤çå ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ­£æ´æ°å¨ç´ æ°æ¨¡ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çéå ï¼è¿å¯ä»¥éè¿æ¬èå°è¦è®¨è®ºçéæ¨å ³ç³»å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®ï¼è¿ä¸æ¹æ³å¸¸ç¨äºç»åæ°è®¡ç®ä¸­å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ­£æ´æ°çé¶ä¹çåæ°çé¢å¤çï¼

å¯¹äº 1 <ð <ð1<i<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ´æ° ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯å¸¦ä½é¤æ³ï¼

ð=âððâð+(ðmodð).p=âpiâi+(pmodi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°è¯¥ç­å¼å¯¹ç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼å°±å¾å°

0â¡âððâð+(ðmodð)(modð).0â¡âpiâi+(pmodi)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°ç­å¼ä¸¤è¾¹åæ¶ä¹ä»¥ ðâ1(ðmodð)â1iâ1(pmodi)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¾å°

ðâ1â¡ââððâ(ðmodð)â1(modð).iâ1â¡ââpiâ(pmodi)â1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±æ¯ç¨äºçº¿æ§æ¶é´éæ¨æ±éå çå ¬å¼ï¼ç±äº ðmodð <ðpmodi<i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸å ¬å¼å°æ±è§£ ðâ1modðiâ1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé®é¢è½¬åä¸ºè§æ¨¡æ´å°çé®é¢ (ðmodð)â1modð(pmodi)â1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ä» 1â1modð =11â1modp=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼å¯¹æ¯ä¸ª ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡ºæ¬¡åºç¨è¯¥å ¬å¼ï¼å°±å¯ä»¥å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è·å¾å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ´æ°çéå ï¼

åèå®ç°å¦ä¸ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // Precomputes modular inverses of all integers from 1 to n modulo prime p. std :: vector < int > precompute_inverses ( int n , int p ) { std :: vector < int > res ( n \+ 1 ); res [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { res [ i ] = ( long long )( p \- p / i ) * res [ p % i ] % p ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # Precomputes modular inverses of all integers from 1 to n modulo prime p. def precompute_inverses ( n , p ): res = [ 0 ] * ( n \+ 1 ) res [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): res [ i ] = ( p \- p // i ) * res [ p % i ] % p return res ```   
---|---  
  
è¿ä¸ç®æ³åªéç¨äºæ¨¡æ°æ¯ç´ æ°çæ å½¢ï¼å¯¹äºæ¨¡æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯ç´ æ°çæ å½¢ï¼æ æ³ä¿è¯éæ¨å ¬å¼ä¸­å¾å°ç ðmodðmmodi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»ç¶ä¸ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å èéæ¨æéè¦ç (ðmodð)â1(mmodi)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½å¹¶ä¸å­å¨ï¼ä¸ä¸ªè¿æ ·çä¾å­æ¯ ð =8,ð =3m=8,i=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼ðmodð =2mmodi=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å­å¨æ¨¡ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå ï¼

å¦å¤ï¼å¾å°è¯¥éæ¨å ¬å¼åï¼ä¸ç§èªç¶çæ³æ³æ¯ç´æ¥éå½æ±è§£ä»»æä¸ä¸ªæ° ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå ï¼æ¯æ¬¡éå½æ¶ï¼é½å©ç¨éæ¨å ¬å¼å°å®è½¬åä¸ºæ´å°çä½æ° ðmodðpmoda![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå ï¼ç´å°ä½æ°åä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶åæ­¢ï¼ç®åå°ä¸æ¸ æ¥è¿æ ·åçå¤æåº¦1ï¼å æ­¤ï¼æ¨èä½¿ç¨åææè¿°çå¸¸è§æ¹æ³æ±è§£ï¼

## ä¹ é¢

  * [LOJ 110 ä¹æ³éå ](https://loj.ac/problem/110)
  * [LOJ 161 ä¹æ³éå  2](https://loj.ac/problem/161)
  * [LOJ 2605ãNOIP2012ãåä½æ¹ç¨](https://loj.ac/problem/2605)
  * [Luogu P2054ãAHOI2005ãæ´ç](https://www.luogu.com.cn/problem/P2054)
  * [LOJ 2034ãSDOI2016ãæåè®¡æ°](https://loj.ac/problem/2034)

## åèèµæä¸æ³¨é

  * [Modular multiplicative inverse - Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

* * *

  1. [riteme å¨ç¥ä¹ä¸çåç­](https://www.zhihu.com/question/59033693/answer/323292359) ä¸­æåºï¼è¿æ ·åçè®ºä¸å·²ç¥çå¤æåº¦çä¸çæ¯ ð(ð1/3+ð)O(p1/3+Îµ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¨å®é éæºæ°æ®ä¸­çè¡¨ç°æ¥è¿äº ð(logâ¡ð)O(logâ¡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/inverse.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/inverse.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [MegaOwIer](https://github.com/MegaOwIer), [PeterlitsZo](https://github.com/PeterlitsZo), [Tiphereth-A](https://github.com/Tiphereth-A), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [jifbt](https://github.com/jifbt), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [abc1763613206](https://github.com/abc1763613206), [buggg-hfc](https://github.com/buggg-hfc), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [hqztrue](https://github.com/hqztrue), [ImpleLee](https://github.com/ImpleLee), [JellyGoat](https://github.com/JellyGoat), [ksyx](https://github.com/ksyx), [lhhxxxxx](https://github.com/lhhxxxxx), [Menci](https://github.com/Menci), [MioChyan](https://github.com/MioChyan), [n-WN](https://github.com/n-WN), [Phemon](mailto:i@phemon.me), [shawlleyw](https://github.com/shawlleyw), [Siyuan](mailto:294873684@qq.com), [skr2005](https://github.com/skr2005), [thredreams](https://github.com/thredreams), [Tiooo111](https://github.com/Tiooo111), [WAAutoMaton](https://github.com/WAAutoMaton), [Zhaoyangzhen](https://github.com/Zhaoyangzhen)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
