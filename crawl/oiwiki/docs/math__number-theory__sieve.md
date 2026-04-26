# ç­æ³ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/sieve/

# ç­æ³

## ç´ æ°ç­æ³

### å¼å ¥

å¦ææä»¬æ³è¦ç¥éå°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå¤å°ä¸ªç´ æ°å¢ï¼

ä¸ä¸ªèªç¶çæ³æ³æ¯å¯¹äºå°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ªæ°è¿è¡ä¸æ¬¡è´¨æ°æ£éªï¼è¿ç§æ´åçåæ³æ¾ç¶ä¸è½è¾¾å°æä¼å¤æåº¦ï¼

### åæææ¯ç¹å°¼ç­æ³

#### è¿ç¨

èèè¿æ ·ä¸ä»¶äºæ ï¼å¯¹äºä»»æä¸ä¸ªå¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å®ç ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå°±æ¯åæ°ï¼ð¥ >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å©ç¨è¿ä¸ªç»è®ºï¼æä»¬å¯ä»¥é¿å å¾å¤æ¬¡ä¸å¿ è¦çæ£æµï¼

å¦ææä»¬ä»å°å°å¤§èèæ¯ä¸ªæ°ï¼ç¶ååæ¶æå½åè¿ä¸ªæ°çææï¼æ¯èªå·±å¤§çï¼åæ°è®°ä¸ºåæ°ï¼é£ä¹è¿è¡ç»æçæ¶åæ²¡æè¢«æ è®°çæ°å°±æ¯ç´ æ°äºï¼

#### å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text vector < int > prime ; bool is_prime [ N ]; void Eratosthenes ( int n ) { is_prime [ 0 ] = is_prime [ 1 ] = false ; for ( int i = 2 ; i <= n ; ++ i ) is_prime [ i ] = true ; for ( int i = 2 ; i <= n ; ++ i ) { if ( is_prime [ i ]) { prime . push_back ( i ); if (( long long ) i * i > n ) continue ; for ( int j = i * i ; j <= n ; j += i ) // å ä¸ºä» 2 å° i - 1 çåæ°æä»¬ä¹åç­è¿äºï¼è¿éç´æ¥ä» i // çåæ°å¼å§ï¼æé«äºè¿è¡éåº¦ is_prime [ j ] = false ; // æ¯ i çåæ°çåä¸æ¯ç´ æ° } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text prime = [] is_prime = [ False ] * N def Eratosthenes ( n ): is_prime [ 0 ] = is_prime [ 1 ] = False for i in range ( 2 , n \+ 1 ): is_prime [ i ] = True for i in range ( 2 , n \+ 1 ): if is_prime [ i ]: prime . append ( i ) if i * i > n : continue for j in range ( i * i , n \+ 1 , i ): is_prime [ j ] = False ```   
---|---  
  
ä»¥ä¸ä¸º **Eratosthenes ç­æ³** ï¼åæææ¯ç¹å°¼ç­æ³ï¼ç®ç§°åæ°ç­æ³ï¼ï¼æ¶é´å¤æåº¦æ¯ ð(ðlogâ¡logâ¡ð)O(nlogâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

ç°å¨æä»¬å°±æ¥ççæ¨å¯¼è¿ç¨ï¼

å¦ææ¯ä¸æ¬¡å¯¹æ°ç»çæä½è±è´¹ 1 ä¸ªåä½æ¶é´ï¼åæ¶é´å¤æåº¦ä¸ºï¼

ð(ð(ð)âð=1ððð)=ð(ðð(ð)âð=11ðð)O(âk=1Ï(n)npk)=O(nâk=1Ï(n)1pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ððpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç¬¬ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°çç´ æ°ï¼ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º â¤ðâ¤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ°ä¸ªæ°ï¼âð(ð)ð=1âk=1Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç¬¬ä¸å± for å¾ªç¯ï¼å ¶ä¸­ç´¯å ä¸ç ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º `if (prime[i])` è¿å ¥ true åæ¯çæ¬¡æ°ï¼ðððnpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºç¬¬äºå± for å¾ªç¯çæ§è¡æ¬¡æ°ï¼

æ ¹æ® Mertens ç¬¬äºå®çï¼å­å¨å¸¸æ° ðµ1B1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ï¼

ð(ð)âð=11ðð=logâ¡logâ¡ð+ðµ1+ð(1logâ¡ð)âk=1Ï(n)1pk=logâ¡logâ¡n+B1+O(1logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ **Eratosthenes ç­æ³** çæ¶é´å¤æåº¦ä¸º ð(ðlogâ¡logâ¡ð)O(nlogâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¥ä¸æ¥æä»¬è¯æ Mertens ç¬¬äºå®ççå¼±åçæ¬ âðâ¤ð(ð)1/ðð =ð(logâ¡logâ¡ð)âkâ¤Ï(n)1/pk=O(logâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ ¹æ® ð(ð) =Î(ð/logâ¡ð)Ï(n)=Î(n/logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ç¥ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªç´ æ°çå¤§å°ä¸º Î(ðlogâ¡ð)Î(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼äºæ¯å°±æ

ð(ð)âð=11ðð=ð(ð(ð)âð=21ðlogâ¡ð)=ð(â«ð(ð)2dð¥ð¥logâ¡ð¥)=ð(logâ¡logâ¡ð(ð))=ð(logâ¡logâ¡ð)âk=1Ï(n)1pk=O(âk=2Ï(n)1klogâ¡k)=O(â«2Ï(n)dxxlogâ¡x)=O(logâ¡logâ¡Ï(n))=O(logâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ç¶ï¼ä¸é¢çåæ³æçä»ç¶ä¸å¤é«æï¼åºç¨ä¸é¢å ç§æ¹æ³å¯ä»¥ç¨å¾®æé«ç®æ³çæ§è¡æçï¼

#### ç­è³å¹³æ¹æ ¹

æ¾ç¶ï¼è¦æ¾å°ç´å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­¢çææç´ æ°ï¼ä» å¯¹ä¸è¶ è¿ âðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ°è¿è¡ç­éå°±è¶³å¤äºï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text vector < int > prime ; bool is_prime [ N ]; void Eratosthenes ( int n ) { is_prime [ 0 ] = is_prime [ 1 ] = false ; for ( int i = 2 ; i <= n ; ++ i ) is_prime [ i ] = true ; // i * i <= n è¯´æ i <= sqrt(n) for ( int i = 2 ; i * i <= n ; ++ i ) { if ( is_prime [ i ]) for ( int j = i * i ; j <= n ; j += i ) is_prime [ j ] = false ; } for ( int i = 2 ; i <= n ; ++ i ) if ( is_prime [ i ]) prime . push_back ( i ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text prime = [] is_prime = [ False ] * N def Eratosthenes ( n ): is_prime [ 0 ] = is_prime [ 1 ] = False for i in range ( 2 , n \+ 1 ): is_prime [ i ] = True # è®© i å¾ªç¯å° <= sqrt(n) for i in range ( 2 , isqrt ( n ) \+ 1 ): # `isqrt` æ¯ Python 3.8 æ°å¢çå½æ° if is_prime [ i ]: for j in range ( i * i , n \+ 1 , i ): is_prime [ j ] = False for i in range ( 2 , n \+ 1 ): if is_prime [ i ]: prime . append ( i ) ```   
---|---  
  
è¿ç§ä¼åä¸ä¼å½±åæ¸è¿æ¶é´å¤æåº¦ï¼å®é ä¸éå¤ä»¥ä¸è¯æï¼æä»¬å°å¾å° ðlnâ¡lnâ¡âð +ð(ð)nlnâ¡lnâ¡n+o(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å¯¹æ°çæ§è´¨ï¼å®ä»¬çæ¸è¿ç¸åï¼ä½æä½æ¬¡æ°ä¼ææ¾åå°ï¼

#### åªç­å¥æ°

å ä¸ºé¤ 2 ä»¥å¤çå¶æ°é½æ¯åæ°ï¼æä»¥æä»¬å¯ä»¥ç´æ¥è·³è¿å®ä»¬ï¼åªç¨å ³å¿å¥æ°å°±å¥½ï¼

é¦å ï¼è¿æ ·åè½è®©æä»¬å å­éæ±ååï¼å ¶æ¬¡ï¼æéçæä½å¤§çº¦ä¹ååï¼

#### åå°å å­çå ç¨

æä»¬æ³¨æå°ç­éæ¶åªéè¦ `bool` ç±»åçæ°ç»ï¼`bool` æ°ç»çä¸ä¸ªå ç´ ä¸è¬å ç¨ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­èï¼å³ 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¹ï¼ï¼ä½æ¯å­å¨ä¸ä¸ªå¸å°å¼åªéè¦ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ¯ç¹å°±è¶³å¤äºï¼

æä»¬å¯ä»¥ä½¿ç¨ [ä½æä½](../../bit/) çç¸å ³ç¥è¯ï¼å°æ¯ä¸ªå¸å°å¼åå°ä¸ä¸ªæ¯ç¹ä½ä¸­ï¼è¿æ ·æä»¬ä» éä½¿ç¨ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¹ï¼å³ ð8n8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­èï¼èé ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­èï¼å¯ä»¥æ¾èåå°å å­å ç¨ï¼è¿ç§æ¹å¼è¢«ç§°ä¸ºãä½çº§åç¼©ãï¼

å¼å¾ä¸æçæ¯ï¼å­å¨èªå¨æ§è¡ä½çº§åç¼©çæ°æ®ç»æï¼å¦ C++ ä¸­ç `vector<bool>` å `bitset<>`ï¼

å¦å¤ï¼`vector<bool>` å `bitset<>` å¯¹ç¨åºæå¸¸æ°ä¼åï¼æ¶é´å¤æåº¦ ð(ðlogâ¡logâ¡ð)O(nlogâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ç­å¨ä½¿ç¨ `bitset<>` æ `vector<bool>` ä¼ååï¼æ§è½çè³è¶ è¿æ¶é´å¤æåº¦ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¬§æç­ï¼

åè§ [bitset: ä¸åæ°ç­ç»å](../../../lang/csl/bitset/#ä¸åæ°ç­ç»å)ï¼

#### ååç­é

ç±ä¼åãç­è³å¹³æ¹æ ¹ãå¯ç¥ï¼ä¸éè¦ä¸ç´ä¿çæ´ä¸ª `is_prime[1...n]` æ°ç»ï¼ä¸ºäºè¿è¡ç­éï¼åªä¿çå° âðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ°å°±è¶³å¤äºï¼å³ `prime[1...sqrt(n)]`ï¼å¹¶å°æ´ä¸ªèå´åæåï¼æ¯ä¸ªååå«è¿è¡ç­éï¼è¿æ ·ï¼æä»¬å°±ä¸å¿ åæ¶å¨å å­ä¸­ä¿çå¤ä¸ªåï¼èä¸ CPU å¯ä»¥æ´å¥½å°å¤çç¼å­ï¼

è®¾ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªå¸¸æ°ï¼å®å³å®äºåçå¤§å°ï¼é£ä¹æä»¬å°±æäº âðð âânsâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªåï¼èå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(ð =0â¦âðð âk=0â¦ânsâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) å å«äºåºé´ [ðð ,ðð  +ð  â1][ks,ks+sâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çæ°å­ï¼æä»¬å¯ä»¥ä¾æ¬¡å¤çåï¼ä¹å°±æ¯è¯´ï¼å¯¹äºæ¯ä¸ªå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å°éåææè´¨æ°ï¼ä» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° âðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä½¿ç¨å®ä»¬è¿è¡ç­éï¼

å¼å¾æ³¨æçæ¯ï¼æä»¬å¨å¤çç¬¬ä¸ä¸ªæ°å­æ¶éè¦ç¨å¾®ä¿®æ¹ä¸ä¸ç­ç¥ï¼é¦å ï¼åºä¿ç [1,âð][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çææçè´¨æ°ï¼ç¬¬äºï¼æ°å­ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºè¯¥æ è®°ä¸ºéç´ æ°ï¼å¨å¤çæåä¸ä¸ªåæ¶ï¼ä¸åºè¯¥å¿è®°æåä¸ä¸ªæ°å­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶ä¸ä¸å®ä½äºåçæ«å°¾ï¼

ä»¥ä¸å®ç°ä½¿ç¨åç­éæ¥è®¡ç®å°äºç­äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè´¨æ°æ°éï¼

å®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text int count_primes ( int n ) { constexpr static int S = 10000 ; vector < int > primes ; int nsqrt = sqrt ( n ); vector < char > is_prime ( nsqrt \+ 1 , true ); for ( int i = 2 ; i <= nsqrt ; i ++ ) { if ( is_prime [ i ]) { primes . push_back ( i ); for ( int j = i * i ; j <= nsqrt ; j += i ) is_prime [ j ] = false ; } } int result = 0 ; vector < char > block ( S ); for ( int k = 0 ; k * S <= n ; k ++ ) { fill ( block . begin (), block . end (), true ); int start = k * S ; for ( int p : primes ) { int start_idx = ( start \+ p \- 1 ) / p ; int j = max ( start_idx , p ) * p \- start ; for (; j < S ; j += p ) block [ j ] = false ; } if ( k == 0 ) block [ 0 ] = block [ 1 ] = false ; for ( int i = 0 ; i < S && start \+ i <= n ; i ++ ) { if ( block [ i ]) result ++ ; } } return result ; } ```   
---|---  
  
ååç­æ³çæ¸è¿æ¶é´å¤æåº¦ä¸åæ°ç­æ³æ¯ä¸æ ·çï¼é¤éåéå¸¸å°ï¼ï¼ä½æ¯æéçå å­å°ç¼©å°ä¸º ð(âð +ð)O(n+S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸ææ´å¥½çç¼å­ç»æï¼ å¦ä¸æ¹é¢ï¼å¯¹äºæ¯ä¸å¯¹åååºé´ [1,âð][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çç´ æ°é½è¦è¿è¡é¤æ³ï¼èå¯¹äºè¾å°çåæ¥è¯´ï¼è¿ç§æ åµè¦ç³ç³å¾å¤ï¼ å æ­¤ï¼å¨éæ©å¸¸æ° ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶è¦ä¿æå¹³è¡¡ï¼

åå¤§å° ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å 104104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° 105105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼å¯ä»¥è·å¾æä½³çéåº¦ï¼

### çº¿æ§ç­æ³

åæ°ç­æ³ä»æä¼åç©ºé´ï¼å®ä¼å°ä¸ä¸ªåæ°éå¤å¤æ¬¡æ è®°ï¼ææ²¡æä»ä¹åæ³çææ æä¹çæ­¥éª¤å¢ï¼ç­æ¡æ¯è¯å®çï¼

å¦æè½è®©æ¯ä¸ªåæ°é½åªè¢«æ è®°ä¸æ¬¡ï¼é£ä¹æ¶é´å¤æåº¦å°±å¯ä»¥éå° ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºï¼

å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; void pre ( int n ) { for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { // i % pri_j == 0 // æ¢è¨ä¹ï¼i ä¹åè¢« pri_j ç­è¿äº // ç±äº pri éé¢è´¨æ°æ¯ä»å°å°å¤§çï¼æä»¥ i ä¹ä¸å ¶ä»çè´¨æ°çç»æä¸å®ä¼è¢« // pri_j çåæ°ç­æï¼å°±ä¸éè¦å¨è¿éå ç­ä¸æ¬¡ï¼æä»¥è¿éç´æ¥ break // æå°±å¥½äº break ; } } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text pri = [] not_prime = [ False ] * N def pre ( n ): for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : """ i % pri_j == 0 æ¢è¨ä¹ï¼i ä¹åè¢« pri_j ç­è¿äº ç±äº pri éé¢è´¨æ°æ¯ä»å°å°å¤§çï¼æä»¥ i ä¹ä¸å ¶ä»çè´¨æ°çç»æä¸å®ä¼è¢« pri_j çåæ°ç­æï¼å°±ä¸éè¦å¨è¿éå ç­ä¸æ¬¡ï¼æä»¥è¿éç´æ¥ break æå°±å¥½äº """ break ```   
---|---  
  
ä¸é¢çè¿ç§ **çº¿æ§ç­æ³** ä¹ç§°ä¸º **Euler ç­æ³** ï¼æ¬§æç­æ³ï¼ï¼

Note

æ³¨æå°ç­æ³æ±ç´ æ°çåæ¶ä¹å¾å°äºæ¯ä¸ªæ°çæå°è´¨å å­ï¼

## ç­æ³æ±æ¬§æå½æ°

æ³¨æå°å¨çº¿æ§ç­ä¸­ï¼æ¯ä¸ä¸ªåæ°é½æ¯è¢«æå°çè´¨å å­ç­æï¼æ¯å¦è®¾ ð1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°è´¨å å­ï¼ðâ² =ðð1nâ²=np1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹çº¿æ§ç­çè¿ç¨ä¸­ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿ ðâ² Ãð1nâ²Ãp1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­æï¼

è§å¯çº¿æ§ç­çè¿ç¨ï¼æä»¬è¿éè¦å¤çä¸¤ä¸ªé¨åï¼ä¸é¢å¯¹ ðâ²modð1nâ²modp1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ åµè®¨è®ºï¼

å¦æ ðâ²modð1 =0nâ²modp1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ ðâ²nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å«äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææè´¨å å­ï¼

ð(ð)=ðÃð âð=1ððâ1ðð=ð1Ãðâ²Ãð âð=1ððâ1ðð=ð1Ãð(ðâ²)Ï(n)=nÃâi=1spiâ1pi=p1Ãnâ²Ãâi=1spiâ1pi=p1ÃÏ(nâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£å¦æ ðâ²modð1 â 0nâ²modp1â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¢ï¼è¿æ¶ ðâ²nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯äºè´¨çï¼æ ¹æ®æ¬§æå½æ°æ§è´¨ï¼æä»¬æï¼

ð(ð)=ð(ð1)Ãð(ðâ²)=(ð1â1)Ãð(ðâ²)Ï(n)=Ï(p1)ÃÏ(nâ²)=(p1â1)ÃÏ(nâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int phi [ N ]; void pre ( int n ) { phi [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; i ++ ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); phi [ i ] = i \- 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { phi [ i * pri_j ] = phi [ i ] * pri_j ; break ; } phi [ i * pri_j ] = phi [ i ] * phi [ pri_j ]; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text pri = [] not_prime = [ False ] * N phi = [ 0 ] * N def pre ( n ): phi [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) phi [ i ] = i \- 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : phi [ i * pri_j ] = phi [ i ] * pri_j break phi [ i * pri_j ] = phi [ i ] * phi [ pri_j ] ```   
---|---  
  
## ç­æ³æ±è«æ¯ä¹æ¯å½æ°

### å®ä¹

æ ¹æ®è«æ¯ä¹æ¯å½æ°çå®ä¹ï¼è®¾ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªåæ°ï¼ð1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°è´¨å å­ï¼ðâ² =ðð1nâ²=np1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æï¼

ð(ð)=â§{ {â¨{ {â©0ðâ²modð1=0âð(ðâ²)otherwiseÎ¼(n)={0nâ²modp1=0âÎ¼(nâ²)otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¥ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è´¨æ°ï¼æ ð(ð) = â1Î¼(n)=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int mu [ N ]; void pre ( int n ) { mu [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { mu [ i ] = -1 ; pri . push_back ( i ); } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { mu [ i * pri_j ] = 0 ; break ; } mu [ i * pri_j ] = \- mu [ i ]; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text pri = [] not_prime = [ False ] * N mu = [ 0 ] * N def pre ( n ): mu [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) mu [ i ] = \- 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : mu [ i * pri_j ] = 0 break mu [ i * pri_j ] = \- mu [ i ] ```   
---|---  
  
## ç­æ³æ±çº¦æ°ä¸ªæ°

ç¨ ððdi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ä¸ªæ°ï¼ðð¢ððnumi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°è´¨å å­åºç°æ¬¡æ°ï¼

### çº¦æ°ä¸ªæ°å®ç

å®çï¼è¥ ð =âðð=1ððððn=âi=1mpici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð =âðð=1(ðð +1)di=âi=1m(ci+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æï¼æä»¬ç¥é ððððpici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°æ ð0ð,ð1ð,â¦,ððððpi0,pi1,â¦,pici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ± ðð +1ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªï¼æ ¹æ®ä¹æ³åçï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°ä¸ªæ°å°±æ¯ âðð=1(ðð +1)âi=1m(ci+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å®ç°

å ä¸º ððdi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼æä»¥å¯ä»¥ä½¿ç¨çº¿æ§ç­ï¼

å¨è¿éç®åä»ç»ä¸ä¸çº¿æ§ç­å®ç°åçï¼

  1. å½ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè´¨æ°æ¶ï¼ðð¢ðð â1,ðð â2numiâ1,diâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶è®¾ ð =âððâq=âipâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°è´¨å å­ï¼
  2. å½ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ðq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè´¨å å­æ¶ï¼ðð¢ðð âðð¢ðð +1,ðð âðððð¢ðð Ã(ðð¢ðð +1)numiânumq+1,diâdqnumiÃ(numi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. å½ ð,ðp,q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè´¨æ¶ï¼ðð¢ðð â1,ðð âðð Ã(ðð¢ðð +1)numiâ1,diâdqÃ(numi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int d [ N ], num [ N ]; void pre ( int n ) { d [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); d [ i ] = 2 ; num [ i ] = 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { num [ i * pri_j ] = num [ i ] \+ 1 ; d [ i * pri_j ] = d [ i ] / num [ i * pri_j ] * ( num [ i * pri_j ] \+ 1 ); break ; } num [ i * pri_j ] = 1 ; d [ i * pri_j ] = d [ i ] * 2 ; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text pri = [] not_prime = [ False ] * N d = [ 0 ] * N num = [ 0 ] * N def pre ( n ): d [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) d [ i ] = 2 num [ i ] = 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : num [ i * pri_j ] = num [ i ] \+ 1 d [ i * pri_j ] = d [ i ] // num [ i * pri_j ] * ( num [ i * pri_j ] \+ 1 ) break num [ i * pri_j ] = 1 d [ i * pri_j ] = d [ i ] * 2 ```   
---|---  
  
## ç­æ³æ±çº¦æ°å

ððfi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¦æ°åï¼ððgi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°è´¨å å­ç ð0 +ð1 +ð2 +â¦ððp0+p1+p2+â¦pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### å®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int g [ N ], f [ N ]; void pre ( int n ) { g [ 1 ] = f [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); g [ i ] = i \+ 1 ; f [ i ] = i \+ 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { g [ i * pri_j ] = g [ i ] * pri_j \+ 1 ; f [ i * pri_j ] = f [ i ] / g [ i ] * g [ i * pri_j ]; break ; } f [ i * pri_j ] = f [ i ] * f [ pri_j ]; g [ i * pri_j ] = 1 \+ pri_j ; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text pri = [] not_prime = [ False ] * N f = [ 0 ] * N g = [ 0 ] * N def pre ( n ): g [ 1 ] = f [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) g [ i ] = i \+ 1 f [ i ] = i \+ 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : g [ i * pri_j ] = g [ i ] * pri_j \+ 1 f [ i * pri_j ] = f [ i ] // g [ i ] * g [ i * pri_j ] break f [ i * pri_j ] = f [ i ] * f [ pri_j ] g [ i * pri_j ] = 1 \+ pri_j ```   
---|---  
  
## ä¸è¬çç§¯æ§å½æ°

åå¦ä¸ä¸ª [ç§¯æ§å½æ°](../basic/#ç§¯æ§å½æ°) ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ï¼å¯¹äºä»»æè´¨æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ­£æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å¨å ³äº ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ¬¡å¤é¡¹å¼æ¶é´å è®¡ç® ð(ðð)f(pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å¯ä»¥å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å ç­åº ð(1),ð(2),â¦,ð(ð)f(1),f(2),â¦,f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼

è®¾åæ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè´¨å å­åè§£æ¯ âðð=1ðð¼ððâi=1kpiÎ±i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð1 <ð2 <â¯ <ððp1<p2<â¯<pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè´¨æ°ï¼æä»¬å¨çº¿æ§ç­ä¸­è®°å½ ðð =ðð¼11gn=p1Î±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¦ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¢« ð¥ â ðxâ p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­æï¼ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è´¨æ°ï¼ï¼é£ä¹ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³å¦ä¸éæ¨å¼ï¼

ðð=â§{ {â¨{ {â©ðð¥â ðð¥modð=0ðotherwisegn={gxâ pxmodp=0potherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¦ ð =ððn=gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯´æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯æä¸ªè´¨æ°çæ¬¡å¹ï¼å¯ä»¥ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç® ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼ð(ð) =ð(ððð) â ð(ðð)f(n)=f(ngn)â f(gn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**æ¬èé¨åå å®¹è¯èªåæ[Ð ÐµÑÐµÑÐ¾ Ð­ÑÐ°ÑÐ¾ÑÑÐµÐ½Ð°](http://e-maxx.ru/algo/eratosthenes_sieve) ä¸å ¶è±æç¿»è¯ç [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/27 12:26:08ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/sieve.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/sieve.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [LJFYC007](https://github.com/LJFYC007), [Xeonacid](https://github.com/Xeonacid), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [mgt](mailto:i@margatroid.xyz), [shuzhouliu](https://github.com/shuzhouliu), [CCXXXI](https://github.com/CCXXXI), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [HeRaNO](https://github.com/HeRaNO), [MegaOwIer](https://github.com/MegaOwIer), [Peanut-Tang](https://github.com/Peanut-Tang), [YOYO-UIAT](https://github.com/YOYO-UIAT), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [Mr-Python-in-China](https://github.com/Mr-Python-in-China), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [TravorLZH](https://github.com/TravorLZH), [weilycoder](https://github.com/weilycoder), [weiyong1024](https://github.com/weiyong1024), [1804040636](https://github.com/1804040636), [383494](https://github.com/383494), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [cubeheadsun](https://github.com/cubeheadsun), [frank-xjh](https://github.com/frank-xjh), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hhc0001](https://github.com/hhc0001), [hqztrue](https://github.com/hqztrue), [ImpleLee](https://github.com/ImpleLee), [inkydragon](https://github.com/inkydragon), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [luojiny1](https://github.com/luojiny1), [Lutra-Fs](https://github.com/Lutra-Fs), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [opsiff](https://github.com/opsiff), [partychicken](https://github.com/partychicken), [PerfectPan](https://github.com/PerfectPan), [Persdre](https://github.com/Persdre), [shawlleyw](https://github.com/shawlleyw), [StableAgOH](https://github.com/StableAgOH), [Steaunk](https://github.com/Steaunk), [SukkaW](https://github.com/SukkaW), [sunruisjtu2020](https://github.com/sunruisjtu2020), [TianKong-y](https://github.com/TianKong-y), [TOMWT-qwq](https://github.com/TOMWT-qwq), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [untitledunrevised](https://github.com/untitledunrevised), [WAAutoMaton](https://github.com/WAAutoMaton), [WineChord](https://github.com/WineChord), [wkywkyQAQ](https://github.com/wkywkyQAQ), [wood3](https://github.com/wood3), [YanWQ-monad](https://github.com/YanWQ-monad), [Yisheng Gong](mailto:yisheng_gong@onmail.com), [zhouyuyang2002](https://github.com/zhouyuyang2002), [ZnPdCo](https://github.com/ZnPdCo), [ä»£å»ºæ](mailto:wood3s@foxmail.com)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
