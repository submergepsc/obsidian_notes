# ç±»æ¬§å éå¾·ç®æ³ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/euclidean/

# ç±»æ¬§å éå¾·ç®æ³

## å¼å ¥

ç±»æ¬§å éå¾·ç®æ³æ¯æ´ªåæ¦å¨ 2016 å¹´å¬ä»¤è¥è¥åäº¤æµä¸­æåºçå å®¹ï¼å®å¸¸ç¨äºè§£å³å½¢å¦

âðð+ððââai+bcâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»æçæ°åï¼ä¸æ ä¸º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼çæ±åé®é¢ï¼å®çä¸»è¦æ³æ³æ¯ï¼å©ç¨åæ°èªèº«çéå½ç»æï¼å°é®é¢è½¬åä¸ºæ´å°è§æ¨¡çé®é¢ï¼éå½æ±è§£ï¼å ä¸ºåæ°çéå½ç»æå [æ¬§å éå¾ç®æ³](../gcd/#æ¬§å) å­å¨ç´æ¥ç [èç³»](../continued-fraction/#è¿åæ°è¡¨ç¤ºçæ±æ³)ï¼å æ­¤ï¼è¿ä¸æ±åæ¹æ³ä¹ç§°ä¸ºç±»æ¬§å éå¾ç®æ³ï¼

å ä¸º [è¿åæ°](../continued-fraction/) å [SternâBrocot æ ](../stern-brocot/) ç­æ¹æ³åæ ·å»ç»äºåæ°çéå½ç»æï¼æä»¥å©ç¨ç±»æ¬§å éå¾ç®æ³å¯ä»¥è§£å³çé®é¢ï¼éå¸¸ä¹å¯ä»¥ç¨è¿äºæ¹æ³è§£å³ï¼ä¸è¿äºæ¹æ³ç¸æ¯ï¼ç±»æ¬§å éå¾ç®æ³éå¸¸æ´å®¹æçè§£ï¼å®çå®ç°ä¹æ´ä¸ºç®æï¼

## ç±»æ¬§å éå¾ç®æ³

æç®åçä¾å­ï¼å°±æ¯æ±åé®é¢ï¼

ð(ð,ð,ð,ð)=ðâð=0âðð+ððâ,f(a,b,c,n)=âi=0nâai+bcâ,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð,ð,ð,ða,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ­£æ´æ°ï¼

### ä»£æ°è§£æ³

é¦å ï¼å° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ ðc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¨¡ï¼å¯ä»¥ç®åé®é¢ï¼å°é®é¢è½¬åä¸º 0 â¤ð,ð <ð0â¤a,b<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

ð(ð,ð,ð,ð)=ðâð=0âðð+ððâ=ðâð=0â(âððâð+(ðmodð))ð+(âððâð+(ðmodð))ðâ=ðâð=0(âððâð+âððâ+â(ðmodð)ð+(ðmodð)ðâ)=ð(ð+1)2âððâ+(ð+1)âððâ+ð(ðmodð,ðmodð,ð,ð).f(a,b,c,n)=âi=0nâai+bcâ=âi=0nâ(âacâc+(amodc))i+(âbcâc+(bmodc))câ=âi=0n(âacâi+âbcâ+â(amodc)i+(bmodc)câ)=n(n+1)2âacâ+(n+1)âbcâ+f(amodc,bmodc,c,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç°å¨ï¼èèè½¬ååçé®é¢ï¼ä»¤

ð=âðð+ððâ.m=âan+bcâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼åé®é¢å¯ä»¥åä½äºæ¬¡æ±åå¼ï¼

ðâð=0âðð+ððâ=ðâð=0ðâ1âð=0[ð<âðð+ððâ].âi=0nâai+bcâ=âi=0nâj=0mâ1[j<âai+bcâ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äº¤æ¢æ±åæ¬¡åºï¼è¿éè¦å¯¹äºæ¯ä¸ª ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è®¡ç®æ»¡è¶³æ¡ä»¶ç ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çèå´ï¼ä¸ºæ­¤ï¼å°æ¡ä»¶åå½¢ï¼

ð<âðð+ððâ=âðð+ð+1ðââ1âºð+1<âðð+ð+1ðââºð+1<ðð+ð+1ðâºðð+ðâðâ1ð<ðâºâðð+ðâðâ1ðâ<ð.j<âai+bcâ=âai+b+1cââ1âºj+1<âai+b+1cââºj+1<ai+b+1câºcj+câbâ1a<iâºâcj+câbâ1aâ<i.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå½¢è¿ç¨ä¸­å¤æ¬¡å©ç¨äº [åæ´å½æ°](../basic/#åæ´å½æ°) çæ§è´¨ï¼ä»£å ¥åå½¢åçæ¡ä»¶ï¼åå¼å¯ä»¥åä½ï¼

ð(ð,ð,ð,ð)=ðâ1âð=0ðâð=0[ð>âðð+ðâðâ1ðâ]=ðâ1âð=0(ðââðð+ðâðâ1ðâ)=ððâð(ð,ðâðâ1,ð,ðâ1).f(a,b,c,n)=âj=0mâ1âi=0n[i>âcj+câbâ1aâ]=âj=0mâ1(nââcj+câbâ1aâ)=nmâf(c,câbâ1,a,mâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤ (ðâ²,ðâ²,ðâ²,ðâ²) =(ð,ð âð â1,ð,ð â1)(aâ²,bâ²,câ²,nâ²)=(c,câbâ1,a,mâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±ååå°äºåé¢è®¨è®ºè¿ç ðâ² >ðâ²aâ²>câ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

å°è¿ä¸¤æ­¥è½¬åç»åå¨ä¸èµ·ï¼å¯ä»¥åç°å¨è¿ç¨ä¸­ï¼(ð,ð)(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ­å°åæ¨¡åäº¤æ¢ä½ç½®ï¼ç´å° ð =0a=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±ç±»ä¼¼äºå¯¹ (ð,ð)(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡è¾è½¬ç¸é¤ï¼è¿ä¹æ¯ç±»æ¬§å éå¾·ç®æ³çå¾åï¼å®çæ¶é´å¤æåº¦æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

å¨è®¡ç®è¿ç¨ä¸­ï¼å¯è½ä¼åºç° ð =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼æ­¤æ¶å å±éå½ä¼åºç° ð = â1n=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å¹¶ä¸å½±åæç»çç»æï¼ä½æ¯ï¼å¦æè¦æ±åºç° ð =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç´æ¥ç»æ­¢ç®æ³ï¼é£ä¹ç®æ³çæ¶é´å¤æåº¦å¯ä»¥æ¹è¯ä¸º ð(logâ¡min{ð,ð,ð})O(logâ¡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

å¯¹å¤æåº¦çè§£é

å©ç¨è¯¥ç®æ³åæ¬§å éå¾ç®æ³çç¸ä¼¼æ§ï¼å¾å®¹æè¯´æå®çæ¶é´å¤æåº¦æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼å æ­¤ï¼åªéè¦è¯´æï¼å¦æå¨ ð =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ç»æ­¢ç®æ³ï¼é£ä¹å®çæ¶é´å¤æåº¦ä¹æ¯ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

ä»¤ ð =â(ðð +ð)/ðâm=â(an+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®° ð =ððS=mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð =ð/ðk=m/n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬åå«ç¸å½äºå ä½ç´è§ï¼è§ä¸ä¸èï¼ä¸­ç¹éµå¾çé¢ç§¯åç´çº¿çæçï¼å¯¹äºå åå¤§ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¼¼æ ð âð/ðkâa/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

èå¯ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ç®æ³è¿ç¨ä¸­çååï¼ç¬¬ä¸æ­¥åæ¨¡æ¶ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¿æä¸åï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¼¼ç± ð/ða/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º (ðmodð)/ð(amodc)/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¸å½äºæçç± ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º ð ââðâkââkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹è¿ä¼¼åä¸ºåæ¥ç (ð ââðâ)(kââkâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼ç¬¬äºæ­¥äº¤æ¢æ¨ªçºµåæ æ¶ï¼ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¼¼ä¿æä¸åï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ååä¸ºå®çåæ°ï¼å æ­¤ï¼è¥è®¾ä¸¤æ­¥æä½åï¼äºå ç» (ð,ð)(k,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º (ðâ²,ðâ²)(kâ²,Sâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ ðâ² =(ð ââðâ)â1kâ²=(kââkâ)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðâ² =(ð ââðâ)ðSâ²=(kââkâ)S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å ä¸º 1 â¤âðâ²â â¤ðâ² <âðâ²â +11â¤âkâ²ââ¤kâ²<âkâ²â+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼éå½è®¡ç®ä¸¤è½®åï¼ä¹ç§¯ç¼©å°çåæ°æå°ä¸º

(ðâ²ââðâ²â)(ðââðâ)=1ââðâ²âðâ²<1ââðâ²ââðâ²â+1=1âðâ²â+1â¤12.(kâ²ââkâ²â)(kââkâ)=1ââkâ²âkâ²<1ââkâ²ââkâ²â+1=1âkâ²â+1â¤12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼è³å¤ ð(logâ¡ð)O(logâ¡S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½®ï¼ç®æ³å¿ ç¶ç»æ­¢ï¼å ä¸ºä»ç¬¬äºè½®å¼å§ï¼æ¯è½®å¼å§æ¶ç ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»æ¯ä¸è¶ è¿ä¸ä¸è½®åæ¨¡ç»æåç ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èåè å¤§è´ä¸º ðð2kn2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å è ð(logâ¡ð) âð(logâ¡ð)O(logâ¡S)âO(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å°±å¾å°äºä¸è¿°ç»è®ºï¼

æ¨¡æ¿é¢çåèå®ç°å¦ä¸ï¼

æ¨¡æ¿é¢å®ç°ï¼[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <iostream> long long solve ( long long a , long long b , long long c , long long n ) { long long n2 = n * ( n \+ 1 ) / 2 ; if ( a >= c || b >= c ) return solve ( a % c , b % c , c , n ) \+ ( a / c ) * n2 \+ ( b / c ) * ( n \+ 1 ); long long m = ( a * n \+ b ) / c ; if ( ! m ) return 0 ; return m * n \- solve ( c , c \- b \- 1 , a , m \- 1 ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> c >> a >> b ; std :: cout << solve ( a , b , c , n \- 1 ) << '\n' ; } return 0 ; } ```   
---|---  
  
### å ä½ç´è§

è¿ä¸ªç®æ³è¿å¯ä»¥ä»å ä½çè§åº¦çè§£ï¼ç±»æ¬§å éå¾ç®æ³å¯ä»¥è§£å³çé®é¢ä¸»è¦æ¯ç´çº¿ä¸æ´ç¹è®¡æ°é®é¢ï¼

å¦ä¸å¾æå·¦é¨åæç¤ºï¼è¯¥æ±åå¼ç¸å½äºæ±ç´çº¿

ð¦=ðð¥+ððy=ax+bc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸æ¹ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½´ä¸æ¹ï¼ä¸å æ¬ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è½´ï¼ï¼ä¸æ¨ªåæ ä½äº [0,ð][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´çæ ¼ç¹æ°ç®ï¼

![](./images/euclidean-1.svg)

é¦å ï¼ç§»é¤æçåæªè·ä¸­çæ´æ°é¨åï¼è¿ä¸æ­¥ç¸å½äºå°ä¸å¾ä¸­é´é¨åçèç¹æ°éåç¬è®¡ç®åºæ¥ï¼å½æçåæªè·é½æ¯æ´æ°æ¶ï¼èç¹ä¸å®ææä¸ä¸ªæ¢¯å½¢éµåï¼ä¹å°±æ¯è¯´ï¼ä¸åçºµåçæ ¼ç¹å½¢æç­å·®æ°åï¼å èè¿äºç¹çæ°éæ¯å®¹æè®¡ç®çï¼å°è¿äºç¹ç§»é¤åï¼å©ä½çæ ¼ç¹åä¸å¾æå³é¨åççº¢ç¹æ°éä¸è´ï¼é®é¢å°±è½¬åæäºæçåæªè·é½å°äºä¸çæ å½¢ï¼å ä¸ºæ¢¯å½¢çé«ä¸º ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸¤ä¸ªåºè¾¹é¿åº¦åå«ä¸º âð/ðââb/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (âð/ðâð +âð/ðâ)(âa/cân+âb/câ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å©ç¨æ¢¯å½¢é¢ç§¯å ¬å¼ï¼è¿ä¸æ­¥éª¤å¯ä»¥å½çº³ä¸ºç®å¼

ð(ð,ð,ð,ð)=ð(ðmodð,ðmodð,ð,ð)+12(ð+1)(âððâ+(âððâð+âððâ)).f(a,b,c,n)=f(amodc,bmodc,c,n)+12(n+1)(âbcâ+(âacân+âbcâ)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¶åï¼ç¿»è½¬æ¨ªçºµåæ è½´ï¼å¦ä¸å¾æå·¦é¨åæç¤ºï¼å¾ä¸­ççº¢ç¹åèç¹ææäºä¸ä¸ªæ¨ªåé¿åº¦ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãçºµåé¿åº¦ä¸º ð =â(ðð +ð)/ðâm=â(an+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©å½¢ç¹éµï¼è¦è®¡ç®çº¢ç¹çæ°éï¼åªéè¦è®¡ç®èç¹çæ°éï¼åç¨ç©å½¢ç¹éµçæ°éåå»èç¹çæ°éå³å¯ï¼ç¿»è½¬åï¼ä¸å¾å·¦åé¨åä¸­çèç¹ç¹éµå°±åæäºææ¡ç´çº¿ä¸ççº¢è²ç¹éµï¼èä¸ï¼ç¿»è½¬åï¼æçå¤§äºä¸ï¼å°±ååå°äºä¸æå·²ç»å¤çè¿çæ å½¢ï¼

![](./images/euclidean-2.svg)

å ³é®å¨äºå¦ä½è®¡ç®æ°ççº¢è²ç¹éµä¸æ¹çç´çº¿çæ¹ç¨ï¼å°ä¸å¾æå·¦é¨åçæ¨ªçºµåæ è½´ç¿»è½¬ï¼å°±å¾å°ä¸å¾ä¸­é´é¨åï¼ç¿»è½¬åççº¢è²ç¹éµä¸æ¹çç´çº¿ï¼ä¸­é´é¨åçå®çº¿ï¼ï¼å¹¶éå¯¹åºç¿»è½¬åçç´çº¿ï¼æå·¦é¨åçå®çº¿ï¼ï¼èæ¯ç¿»è½¬åçç´çº¿åå·¦ä¸å¹³ç§»ä¸ç¹ç¹çç»æï¼æå·¦é¨åçèçº¿ï¼ï¼è¿æ¯å ä¸ºï¼å¦æç´æ¥å°ç´çº¿ï¼æå·¦é¨åçå®çº¿ï¼ç¿»è½¬ï¼å°å¾å°ä¸­é´é¨åçèçº¿ï¼ä½æ¯æç §å®ä¹ï¼å®ä¸æ¹çæ ¼ç¹å æ¬æ°å¥½è½å¨ç´çº¿ä¸çæ ¼ç¹ï¼è¿å°±ä¼å¯¼è´ç´çº¿ä¸çæ ¼ç¹éå¤è®¡æ°ï¼ä¸ºäºé¿å è¿ä¸ç¹ï¼éè¦å°ç¿»è½¬ç´çº¿ ð¦ =(ðð¥ +ð)/ðy=(ax+b)/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¾å°çç´çº¿ ð¦ =(ðð¥ âð)/ðy=(cxâb)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸å¹³ç§»ä¸ç¹ç¹ï¼å¾å°ç´çº¿ ð¦ =(ðð¥ âð â1)/ðy=(cxâbâ1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ ·å®ä¸æ¹çç¹éµææ°ä¸ºç¿»è½¬åçèè²ç¹éµï¼

è¿æå¦ä¸å¤ç»èéè¦å¤çï¼ä¸å¾ä¸­é´é¨åçç´çº¿çæªè·æ¯è´æ°ï¼è¿æå³çè¿æ²¡æåå°ä¹åçåå§æ å½¢ï¼è¦è®©æªè·æ¢å¤ä¸ºéè´æ°ï¼åªéè¦å°ç´çº¿ï¼ä¸­é´é¨åçå®çº¿ï¼åå·¦å¹³ç§»ä¸ä¸ªåä½ï¼è¿æ ·åä¸ä¼æ¼æä»»ä½æ ¼ç¹ï¼å ä¸ºç¿»è½¬åçèè²ç¹éµä¸­æ²¡æçºµåæ ä¸ºé¶çç¹ï¼ç¿»è½¬åä¹å°±ä¸å­å¨æ¨ªåæ ä¸ºé¶çç¹ï¼æåï¼ç´çº¿æ¹ç¨å°±åä¸º ð¦ =(ðð¥ +ð âð â1)/ðy=(cx+câbâ1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶ï¼ç¹éµçæ¨ªåæ çä¸çä¹ä» ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæäº ð â1mâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ­¥éª¤å¯ä»¥å½çº³ä¸ºç®å¼

ð(ð,ð,ð,ð)=ððâð(ð,ðâðâ1,ð,ðâ1).f(a,b,c,n)=mnâf(c,câbâ1,a,mâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ç§éå½çç®æ³è¡å¾éï¼ä¸»è¦æä¸¤ä¸ªåå ï¼

  * ç¬¬ä¸ï¼ç´çº¿çæçä¸æ­å°å åå°æ°é¨ååååæ°ï¼è¿ç­ä»·äºè®¡ç®ç´çº¿æç ð =ð/ðk=a/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç [è¿åæ°å±å¼](../continued-fraction/#è¿åæ°è¡¨ç¤ºçæ±æ³)ï¼å ä¸ºæçåæ°çè¿åæ°å±å¼çé¿åº¦æ¯ ð(logâ¡min{ð,ð})O(logâ¡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼æä»¥è¿ä¸è¿ç¨ä¸å®å¨ ð(logâ¡min{ð,ð})O(logâ¡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­¥åç»æ­¢ï¼
  * ç¬¬äºï¼å ä¸ºæ¯æ¬¡ç¿»è½¬åæ è½´çæ¶åï¼ç´çº¿æçé½æ¯å°äºä¸çï¼å æ­¤ï¼ç´è§ä¸åºè¯¥æ ð <ðm<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ç»è¿è¿æ ·ä¸è½®è¿­ä»£åï¼æ¨ªåæ çèå´ä¸ç´æ¯å¨ç¼©å°çï¼åæçå¤æåº¦è®¡ç®ä¸­éè¿ä¸¥æ ¼çåæè¯´æï¼æ¯ä¸¤è½®è¿­ä»£åï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å¤ä¸ºåæ¥çä¸åï¼æ èè¿ä¸è¿ç¨ä¸å®å¨ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ­¥åç»æ­¢ï¼

è¿ä¹æ¯æçä¸ºæçæ°æ¶çç±»æ¬§å éå¾ç®æ³çå¤æåº¦æ¯ ð(logâ¡min{ð,ð,ð})O(logâ¡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå ï¼

å©ç¨ç±»ä¼¼çå ä½ç´è§ï¼å¯ä»¥å°ç±»æ¬§å éå¾ç®æ³æ¨å¹¿å°æçä¸ºæ çæ°çæ å½¢ï¼å ·ä½åæè¯·åèåæçä¾é¢ï¼

### ä¾é¢

[ãæ¨¡æ¿ãç±»æ¬§å éå¾ç®æ³](https://www.luogu.com.cn/problem/P5170)

å¤ç»è¯¢é®ï¼ç»å®æ­£æ´æ° ð,ð,ð,ða,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±

ð(ð,ð,ð,ð)=ðâð=0âðð+ððâ,ð(ð,ð,ð,ð)=ðâð=0ðâðð+ððâ,â(ð,ð,ð,ð)=ðâð=0âðð+ððâ2.f(a,b,c,n)=âi=0nâai+bcâ,g(a,b,c,n)=âi=0niâai+bcâ,h(a,b,c,n)=âi=0nâai+bcâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è§£ç­ä¸

ç±»ä¼¼äº ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¨å¯¼ï¼å¯ä»¥å¾å° ð,âg,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéå½è¡¨è¾¾å¼ï¼

é¦å ï¼å©ç¨åæ¨¡ï¼å°é®é¢è½¬åä¸º 0 â¤ð,ð <ð0â¤a,b<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

ð(ð,ð,ð,ð)=ð(ðmodð,ðmodð,ð,ð)+âððâð(ð+1)(2ð+1)6+âððâð(ð+1)2,â(ð,ð,ð,ð)=â(ðmodð,ðmodð,ð,ð)+2âððâð(ðmodð,ðmodð,ð,ð)+2âððâð(ðmodð,ðmodð,ð,ð)+âððâ2ð(ð+1)(2ð+1)6+âððâ2(ð+1)+âððââððâð(ð+1).g(a,b,c,n)=g(amodc,bmodc,c,n)+âacân(n+1)(2n+1)6+âbcân(n+1)2,h(a,b,c,n)=h(amodc,bmodc,c,n)+2âbcâf(amodc,bmodc,c,n)+2âacâg(amodc,bmodc,c,n)+âacâ2n(n+1)(2n+1)6+âbcâ2(n+1)+âacââbcân(n+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¶åï¼å©ç¨äº¤æ¢æ±åæ¬¡åºï¼å¯ä»¥è¿ä¸æ­¥è½¬åï¼åæ ·å°ï¼ä»¤

ð=âðð+ððâ.m=âan+bcâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼å¯¹äºåå¼ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð(ð,ð,ð,ð)=ðâð=0ðâðð+ððâ=ðâð=0ðâ1âð=0ð[ð<âðð+ððâ]=ðâ1âð=0ðâð=0ð[ð>âðð+ðâðâ1ðâ]=ðâ1âð=012(âðð+ðâðâ1ðâ+ð+1)(ðââðð+ðâðâ1ðâ)=12ðð(ð+1)â12ðâ1âð=0âðð+ðâðâ1ðââ12ðâ1âð=0âðð+ðâðâ1ðâ2=12ðð(ð+1)â12ð(ð,ðâðâ1,ð,ðâ1)â12â(ð,ðâðâ1,ð,ðâ1).g(a,b,c,n)=âi=0niâai+bcâ=âi=0nâj=0mâ1i[j<âai+bcâ]=âj=0mâ1âi=0ni[i>âcj+câbâ1aâ]=âj=0mâ112(âcj+câbâ1aâ+n+1)(nââcj+câbâ1aâ)=12mn(n+1)â12âj=0mâ1âcj+câbâ1aââ12âj=0mâ1âcj+câbâ1aâ2=12mn(n+1)â12f(c,câbâ1,a,mâ1)â12h(c,câbâ1,a,mâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºåå¼ âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

â(ð,ð,ð,ð)=ðâð=0âðð+ððâ2=ðâð=0ðâ1âð=0(2ð+1)[ð<âðð+ððâ]=ðâ1âð=0ðâð=0(2ð+1)[ð>âðð+ðâðâ1ðâ]=ðâ1âð=0(2ð+1)(ðââðð+ðâðâ1ðâ)=ðð2âðâ1âð=0âðð+ðâðâ1ðââ2ðâ1âð=0ðâðð+ðâðâ1ðâ=ðð2âð(ð,ðâðâ1,ð,ðâ1)â2ð(ð,ðâðâ1,ð,ðâ1).h(a,b,c,n)=âi=0nâai+bcâ2=âi=0nâj=0mâ1(2j+1)[j<âai+bcâ]=âj=0mâ1âi=0n(2j+1)[i>âcj+câbâ1aâ]=âj=0mâ1(2j+1)(nââcj+câbâ1aâ)=nm2ââj=0mâ1âcj+câbâ1aââ2âj=0mâ1jâcj+câbâ1aâ=nm2âf(c,câbâ1,a,mâ1)â2g(c,câbâ1,a,mâ1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»å ä½ç´è§çè§åº¦çï¼è¿äºéçº¿æ§çæ±åå¼ç¸å½äºç»åºåä¸­çæ¯ä¸ªç¹ (ð,ð)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½èµäºäºç¸åºçæé ð¤(ð,ð)w(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é¤äºè¿äºæéä¹å¤ï¼å ¶ä½é¨åçè®¡ç®è¿ç¨æ¯å®å ¨ä¸è´çï¼å¯¹äºæéçéæ©ï¼ä¸è¬å°ï¼æ

ðâð=0ððâðð+ððâð =ðâð=0ðâ1âð=0ðð((ð+1)ð âðð )[ð<âðð+ððâ].âi=0nirâai+bcâs=âi=0nâj=0mâ1ir((j+1)sâjs)[j<âai+bcâ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¬é¢çå¦ä¸ä¸ªç¹ç¹æ¯ï¼ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨éå½è®¡ç®æ¶ï¼ä¼ç¸äºäº¤éï¼å æ­¤ï¼éè¦å° (ð,ð,â)(f,g,h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ºä¸å ç»åæ¶éå½ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <iostream> struct Data { int f , g , h ; }; Data solve ( long long a , long long b , long long c , long long n ) { constexpr long long M = 998244353 ; constexpr long long i2 = ( M \+ 1 ) / 2 ; constexpr long long i6 = ( M \+ 1 ) / 6 ; long long n2 = ( n \+ 1 ) * n % M * i2 % M ; long long n3 = ( 2 * n \+ 1 ) * ( n \+ 1 ) % M * n % M * i6 % M ; Data res = { 0 , 0 , 0 }; if ( a >= c || b >= c ) { auto tmp = solve ( a % c , b % c , c , n ); long long aa = a / c , bb = b / c ; res . f = ( tmp . f \+ aa * n2 \+ bb * ( n \+ 1 )) % M ; res . g = ( tmp . g \+ aa * n3 \+ bb * n2 ) % M ; res . h = ( tmp . h \+ 2 * bb * tmp . f % M \+ 2 * aa * tmp . g % M \+ aa * aa % M * n3 % M \+ bb * bb % M * ( n \+ 1 ) % M \+ 2 * aa * bb % M * n2 % M ) % M ; return res ; } long long m = ( a * n \+ b ) / c ; if ( ! m ) return res ; auto tmp = solve ( c , c \- b \- 1 , a , m \- 1 ); res . f = ( m * n \- tmp . f \+ M ) % M ; res . g = ( m * n2 \+ ( M \- tmp . f ) * i2 \+ ( M \- tmp . h ) * i2 ) % M ; res . h = ( n * m % M * m \- tmp . f \- tmp . g * 2 \+ 3 * M ) % M ; return res ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n , a , b , c ; std :: cin >> n >> a >> b >> c ; auto res = solve ( a , b , c , n ); std :: cout << res . f << ' ' << res . h << ' ' << res . g << '\n' ; } return 0 ; } ```   
---|---  
  
[[æ¸ åéè®­ 2014] Sum](https://www.luogu.com.cn/problem/P5172)

å¤ç»è¯¢é®ï¼ç»å®æ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±

ðâð=1(â1)âðâðâ.âd=1n(â1)âdrâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è§£ç­ä¸

å¦æ ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨å¹³æ¹æ°ï¼é£ä¹å½ âðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°æ¶ï¼åå¼ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼åå¼ä¾æ® ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¥å¶æ§ä¸åï¼å¨ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´äº¤æ¿ååï¼ä¸é¢èè ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯å®å ¨å¹³æ¹æ°çæ å½¢ï¼

ä¸ºäºåºç¨ç±»æ¬§å éå¾ç®æ³ï¼é¦å å°æ±åå¼è½¬åä¸ºçæçå½¢å¼ï¼

ðâð=1(â1)âðâðâ=ðâð=1(1â2(âðâðâmod2))=ðâ2ðâð=1(âðâðââ2ââðâðâ2â)=ðâ2ðâð=1âðâðâ+4ðâð=1âðâð2â=ðâ2ð(ð,1,0,1)+4ð(ð,1,0,2)âd=1n(â1)âdrâ=âd=1n(1â2(âdrâmod2))=nâ2âd=1n(âdrââ2ââdrâ2â)=nâ2âd=1nâdrâ+4âd=1nâdr2â=nâ2f(n,1,0,1)+4f(n,1,0,2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­çå½æ° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ·æå½¢å¼

ð(ð,ð,ð,ð)=ðâð=1âðâð+ðððâ.f(a,b,c,n)=âi=1nâar+bciâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸æ­£æä¸­çç®æ³ä¸åçæ¯ï¼æ­¤å¤çæçä¸åæ¯æçæ°ï¼è®¾æç

ð=ðâð+ðð.k=ar+bc.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ ·åä¸ºä¸¤ç§æ å½¢è®¨è®ºï¼å¦æ ð â¥1kâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹

ð(ð,ð,ð,ð)=ðâð=1âððâ=ðâð=1â(ðââðâ)ðâ+âðâðâð=1ð=âðâð(ð+1)2+ð(ð,ðâðâðâ,ð,ð).f(a,b,c,n)=âi=1nâkiâ=âi=1nâ(kââkâ)iâ+âkââi=1ni=âkân(n+1)2+f(a,bâcâkâ,c,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é®é¢è½¬åä¸ºæçå°äºä¸çæ å½¢ï¼å¦æ ð <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹è®¾ ð =âððâm=ânkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð(ð,ð,ð,ð)=ðâð=1âððâ=ðâð=1ðâð=1[ðâ¤âððâ]=ðâð=1ðâð=1[ð>âðâ1ðâ]=ððâðâð=1ðâð=1[ðâ¤âðâ1ðâ].f(a,b,c,n)=âi=1nâkiâ=âi=1nâj=1m[jâ¤âkiâ]=âj=1mâi=1n[i>âkâ1jâ]=nmââj=1mâi=1n[iâ¤âkâ1jâ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­¤å¤çæ¨å¯¼ä¸­ï¼äº¤æ¢ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¡ä»¶æ¯æ­£æä¸­çæ å½¢æ´ä¸ºç®åï¼æ¯å ä¸ºç´çº¿ ð¦ =ðð¥y=kx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ²¡æé¤äºåç¹ä¹å¤çæ ¼ç¹ï¼å ³é®å¨äºäº¤æ¢åçæ±åå¼åæ ð(ð,ð,ð,ð)f(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼è¿ç¸å½äºè¦æ± ðâ²,ðâ²,ðâ²aâ²,bâ²,câ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³

ðâ1=ðâ²âð+ðâ²ðâ².kâ1=aâ²r+bâ²câ².![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å¹¶ä¸å°é¾ï¼åªéè¦å°åæ¯æçåï¼å°±è½å¾å°

ðâ1=ððâð+ð=ððâðâððð2ðâð2.kâ1=car+b=carâcba2râb2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼æ

ðâ²=ðð,Â ðâ²=âðð,Â ðâ²=ð2ðâð2.aâ²=ca,Â bâ²=âcb,Â câ²=a2râb2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æ

ð(ð,ð,ð,ð)=ððâð(ðð,âðð,ð2ðâð2,ð).f(a,b,c,n)=nmâf(ca,âcb,a2râb2,m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ºäºé¿å æ´æ°æº¢åºï¼éè¦æ¯æ¬¡é½å° ð,ð,ða,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¤ä»¥å®ä»¬çæå¤§å ¬çº¦æ°ï¼å ä¸ºè¿ä¸ªè®¡ç®è¿ç¨åè®¡ç® ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°çè¿ç¨å®å ¨ä¸è´ï¼æä»¥æ ¹æ® [è¿åæ°çè®º](../continued-fraction/#äºæ¬¡æ)ï¼åªè¦ä¿è¯ gcd(ð,ð,ð) =1gcd(a,b,c)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬å¨è®¡ç®è¿ç¨ä¸­å¿ ç¶å¨æ´åèå´å ï¼å¦å¤ï¼å°½ç®¡ (ð,ð,ð,ð)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¼æº¢åºï¼ä½æ¯å¨è¯¥é¢æ°æ®èå´ä¸ï¼ð(ð,ð,ð,ð)f(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è½ä¼è¶ è¿ 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´æ°çèå´ï¼èªç¶æº¢åºå³å¯ï¼æ éé¢å¤å¤çï¼æåç»æä¸å®å¨ [ âð,ð][ân,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼

å°½ç®¡æçä¸ä¼åä¸ºé¶ï¼ç®æ³çå¤æåº¦ä»ç¶æ¯ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼è¿ä¸ç¹ä»åæå ³äºç®æ³å¤æåº¦çè®ºè¯å®¹æçåºï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <cmath> #include <iostream> long long r ; long double sqrt_r ; long long gcd ( long long a , long long b ) { return b ? gcd ( b , a % b ) : a ; } unsigned long long f ( long long a , long long b , long long c , long long n ) { if ( ! n ) return 0 ; auto d = gcd ( a , gcd ( b , c )); a /= d ; b /= d ; c /= d ; unsigned long long k = ( a * sqrt_r \+ b ) / c ; if ( k ) { return n * ( n \+ 1 ) / 2 * k \+ f ( a , b \- c * k , c , n ); } else { unsigned long long m = n * ( a * sqrt_r \+ b ) / c ; return n * m \- f ( c * a , \- c * b , a * a * r \- b * b , m ); } } unsigned long long solve ( long long n , long long r ) { long long sqr = sqrt_r = sqrtl ( r ); if ( r == sqr * sqr ) return r % 2 ? ( n % 2 ? -1 : 0 ) : n ; return n \- 2 * f ( 1 , 0 , 1 , n ) \+ 4 * f ( 1 , 0 , 2 , n ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n >> r ; long long res = solve ( n , r ); std :: cout << res << '\n' ; } return 0 ; } ```   
---|---  
  
[Fraction](https://www.luogu.com.cn/problem/P5179)

ç»å®æ­£æ´æ° ð,ð,ð,ða,b,c,d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±æææ»¡è¶³ ð/ð <ð/ð <ð/ða/b<p/q<c/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç®åæ° ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­å ¸åºæå°çé£ä¸ªï¼

è§£ç­

è¿éé¢ç®ä¹æ¯ [SternâBrocot æ ](../stern-brocot/) çç»å ¸åºç¨ï¼ç¸å ³é¢è§£å¯ä»¥å¨ [æ­¤å¤](../continued-fraction/#è¿åæ°çæ) æ¾å°ï¼å ä¸ºå®åªä¾èµäºåæ°çéå½ç»æï¼æä»¥å®åæ ·å¯ä»¥å©ç¨ç±»ä¼¼æ¬§å éå¾ç®æ³çæ¹æ³æ±è§£ï¼æ èä¹å¯ä»¥è§ä½ç±»æ¬§å éå¾ç®æ³çä¸ä¸ªåºç¨ï¼

å¦æ ð/ða/b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð/ðc/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼ä¸å«ç«¯ç¹ï¼å­å¨è³å°ä¸ä¸ªèªç¶æ°ï¼å¯ä»¥ç´æ¥å (ð,ð) =(1,âð/ðâ +1)(q,p)=(1,âa/bâ+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åï¼å¿ ç¶æ

âððââ¤ðð<ðð<ððâ¤âððâ+1.âabââ¤ab<pq<cdâ¤âabâ+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»è¿ä¸ªä¸ç­å¼ä¸­å¯ä»¥çåºï¼ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°é¨åå¯ä»¥ç¡®å®ä¸º âð/ðââa/bâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´æ¥æ¶å»è¯¥æ´æ°é¨åï¼ç¶åæ´ä½ååæ°ï¼ç¨äºç¡®å®å®çå°æ°é¨åï¼è¿æ­£æ¯ç¡®å® ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°ç [åºæ¬æ¹æ³](../continued-fraction/#è¿åæ°è¡¨ç¤ºçæ±æ³)ï¼è¥æç»çç­æ¡æ¯ ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ç®æ³çæ¶é´å¤æåº¦ä¸º ð(logâ¡min{ð,ð})O(logâ¡min{p,q})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ­¤å¤ï¼æä¸ä¸ªç»èé®é¢ï¼å³ååæ°ä¹åå¾å°çå­å ¸åºæå°çåæ°ï¼æ¯å¦æ¯ååæ°ä¹åçå­å ¸åºæå°çåæ°ï¼æ¢å¥è¯è¯´ï¼æ»¡è¶³ ð/ð <ð/ð <ð/ða/b<p/q<c/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ° ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ï¼å­å ¸åº (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çï¼æ¯å¦ä¹æ¯å­å ¸åº (ð,ð)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çï¼åè®¾ä¸ç¶ï¼è®¾ ð/ðp/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å­å ¸åº (ð,ð)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çï¼ä½æ¯ ð/ð  â ð/ðr/sâ p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å­å ¸åº (ð,ð )(r,s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå°çï¼è¿å¿ ç¶æ ð <ðr<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð <ð q<s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯ï¼è¿è¯´æ

ðð<ðð <ðð<ðð<ðð.ab<rs<rq<pq<cd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ð/ðr/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ è®ºæç §åªä¸ªå­å ¸åºææ ·é½æ¯ä¸¥æ ¼æ´å°äºå½åè§£çï¼è¿ä¸æè®¾æ¡ä»¶çç¾ï¼å æ­¤ï¼ä¸è¿°ç®æ³æ¯æ­£ç¡®çï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text #include <iostream> void solve ( int a , int b , int & p , int & q , int c , int d ) { if (( a / b \+ 1 ) * d < c ) { p = a / b \+ 1 ; q = 1 ; } else { solve ( d , c \- d * ( a / b ), q , p , b , a % b ); p += q * ( a / b ); } } int main () { int a , b , c , d , p , q ; while ( std :: cin >> a >> b >> c >> d ) { solve ( a , b , p , q , c , d ); std :: cout << p << '/' << q << '\n' ; } return 0 ; } ```   
---|---  
  
## ä¸è½æ¬§å éå¾ç®æ³

ä¸ä¸èè®¨è®ºçç±»æ¬§å éå¾ç®æ³æ¨å¯¼éå¸¸è¾ä¸ºç¹çï¼èä¸è½å¤è§£å³çåå¼ä¸»è¦æ¯å¯ä»¥è½¬åä¸ºç´çº¿ä¸ï¼å¸¦æï¼æ´ç¹è®¡æ°é®é¢çåå¼ï¼æ¬èè®¨è®ºä¸ç§æ´ä¸ºä¸è¬çæ¹æ³ï¼å®è¿ä¸æ­¥æ½è±¡äºä¸è¿°è¿ç¨ï¼ä»èå¯ä»¥è§£å³æ´å¤çé®é¢ï¼å æ­¤ï¼è¿ä¸æ¹æ³ä¹ç§°ä¸ºä¸è½æ¬§å éå¾ç®æ³ï¼å®åæ ·å©ç¨äºåæ°çéå½ç»ææ±è§£é®é¢ï¼ä½æ¯ä¸ç±»æ¬§å éå¾ç®æ³çº¦åé®é¢çæè·¯ç¨æä¸åï¼

ä»ç¶èèæç»å ¸çæ±åé®é¢ï¼

ð(ð,ð,ð,ð)=ðâð=1âðð+ððâ,f(a,b,c,n)=âi=1nâai+bcâ,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð,ð,ð,ða,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ­£æ´æ°ï¼

### é®é¢è½¬å

è®¾åæ°ä¸º (ð,ð,ð,ð)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ®µä¸º

ð¦=ðð¥+ðð,Â 0<ð¥â¤ð.y=ax+bc,Â 0<xâ¤n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºè¿æ¡çº¿æ®µï¼å¯ä»¥æç §å¦ä¸æ¹æ³å®ä¹ä¸ä¸ªç± ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æçå­ç¬¦ä¸² ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹ç§°ä¸º **æä½åºå** ï¼

  * å­ç¬¦ä¸²æ°æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð =â(ðð +ð)/ðâm=â(an+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æï¼
  * ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éæ°ç­äº â(ðð +ð)/ðââ(ai+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð =1,â¯,ði=1,â¯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»å ä½ç´è§ä¸çï¼è¿å¤§è´ç¸å½äºä»åç¹å¼å§ï¼æ¯åå³ç©¿è¿ä¸æ¬¡ç«åçç½æ ¼çº¿ï¼å°±åä¸ä¸ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯åä¸ç©¿è¿ä¸æ¬¡æ¨ªåçç½æ ¼çº¿ï¼å°±åä¸ä¸ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ä¸å¾æç¤ºï¼

![](./images/euclidean-universal.svg)

å½ç¶ï¼è¿æ ·çå®ä¹è¿éè¦èéä¸ç³»åç¹æ®æ å½¢ï¼

  * ç»è¿æ´ç¹ï¼å³åæ¶ä¸ç©¿åå³ç©¿ï¼æ¶ï¼éè¦å å ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å­ç¬¦ä¸²å¼å§æ¶ï¼é¤äºå¨ (0,1](0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºé´å ä¸ç©¿ç½æ ¼çº¿çæ¬¡æ°å¤ï¼è¿éè¦æ ¼å¤è¡¥å âð/ðââb/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å­ç¬¦ä¸²ç»ææ¶ï¼ä¸è½ææ ¼å¤ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦æå¯¹äºå ä½ç´è§çæè¿°æä»»ä½ä¸ææ°çå°æ¹ï¼å¯ä»¥åèä¸è¿°ä»£æ°æ¹æ³çå®ä¹è¾ å©çè§£ï¼å ä½ç´è§çæè¿°ï¼æå©äºçè§£ä¸æçç®æ³è¿ç¨ï¼

ä¸è½æ¬§å éå¾ç®æ³çåºæ¬æè·¯ï¼å°±æ¯å°æä½åºåä¸­ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½è§ä½æä¸ª [å¹ºåç¾¤](../../algebra/basic/#ç¾¤) å çå ç´ ï¼å°æ´ä¸ªæä½åºåè§ä¸ºå¹ºåç¾¤å å ç´ çä¹ç§¯ï¼èé®é¢æç»çç­æ¡ä¸è¿ä¸ªä¹ç§¯æå ³ï¼

æ¯å¦ï¼æ¬é¢ä¸­ï¼å¯ä»¥å®ä¹ç¶æåé ð£ =(1,ð¦,âð¦)v=(1,y,ây)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¡¨ç¤ºèªåç¹å¼å§ï¼ç»åäºè¥å¹²æ¬¡ä¸ç©¿åå³ç©¿ç½æ ¼çº¿åï¼å½åçç¶æï¼å ¶ä¸­ï¼ç¬¬ä¸ä¸ªåéæ¯å¸¸æ°ï¼ç¬¬äºä¸ªåéæ¯çºµåæ  ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¬¬ä¸ä¸ªåéæ¯è¦æ±çåå¼ï¼èµ·å§æ¶ï¼æ ð£ =(1,0,0)v=(1,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯åä¸ç©¿è¿ä¸æ¬¡ç½æ ¼çº¿ï¼çºµåæ å°±ç´¯å ä¸ï¼å³ç¸å½äºå°ç¶æåéå³ä¹ä»¥ç©éµ

ð=ââ â ââ110010001ââ â ââ .U=(110010001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¯åå³ç©¿è¿ä¸æ¬¡ç½æ ¼çº¿ï¼åå¼å°±ç´¯å ä¸æ¬¡çºµåæ ï¼å³ç¸å½äºå°ç¶æåéå³ä¹ä»¥ç©éµ

ð =ââ â ââ100011001ââ â ââ .R=(100011001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼æç»çç¶æå°±æ¯ä¹ç§¯ (1,0,0)ð(1,0,0)S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè§£ä¸ºä¸è¿°ç©éµçä¹ç§¯ï¼ææ±çç­æ¡ï¼å°±æ¯æç»ç¶æçç¬¬ä¸ä¸ªåéï¼

é¤äºå°å¹ºåç¾¤ä¸­çå ç´ å®ä¹ä¸ºç©éµä»¥å¤ï¼è¿å¯ä»¥å°å®ä»¬å®ä¹ä¸ºä¸æ®µæä½åºåå¯¹äºæç»ç»æçè´¡ç®ï¼ç¶åå°æä½çä¹ç§¯å®ä¹ä¸ºä¸¤æ®µæä½åºåçè´¡ç®çåå¹¶ï¼

æ¬é¢ä¸­ï¼å¯ä»¥å®ä¹æ¯æ®µæä½åºåçè´¡ç®ä¸º (ð¥,ð¦,âð¦)(x,y,ây)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ºäºä¸¥è°¨å°è§£éè¿äºè®°å·ï¼å¯ä»¥å°è¿äºåéé½çä½æ¯æä½åºåçå½æ°ï¼ä¹å°±æ¯è¯´ï¼å¯¹äºæä½åºå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®çè´¡ç®å¯ä»¥åä½ (ð¥(ð),ð¦(ð),(âð¦)(ð))(x(S),y(S),(ây)(S))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð¥(ð)x(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¦(ð)y(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå«å¯¹åºçæä½åºå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éï¼ä¹å°±æ¯è¯¥çº¿æ®µå³ç©¿åä¸ç©¿ç½æ ¼çº¿çæ¬¡æ°ï¼æåä¸é¡¹ä¸­çæ±åç¬¦å·ï¼ä¸è¬å°ï¼æå¦ä¸å®ä¹ï¼å¯¹äºæä½åºåä¸çå½æ° ð(ð)f(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å®ä¹ (âð)(ð)(âf)(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æè®°ä½ âððâSf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ºä¸é¢çè¡¨è¾¾å¼ï¼

âðð:=â{ð(ð[1,ð]):ðð=ð }.âSf:=â{f(S[1,r]):Sr=R}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ððSr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çç¬¬ ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­ç¬¦ï¼ð[1,ð]S[1,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­å ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­ç¬¦ç»æçåç¼ï¼ä¹å°±æ¯è¯´ï¼è¿ä¸ªæ±åè®°å·ï¼å¯ä»¥çä½æ¯å¯¹äºæä½åºå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ææä»¥ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»å°¾çåç¼è¿è¡çæ±åï¼æ¯å¦è¯´ï¼æ

âð1=ð¥,Â âðð¥=12ð¥(ð¥+1).âS1=x,Â âSx=12x(x+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åæ¯å¦è¯´ï¼âð¦ây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯æä½åºåä¸­ï¼æ¯æ¬¡å³ç©¿ç½æ ¼çº¿æ¶ï¼ä¹åä¸ç©¿ç½æ ¼çº¿çæ¬¡æ°çç´¯å ï¼å¯¹äºæ´æ®µæä½åºåæ¥è¯´ï¼ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ææä»¥ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»å°¾çåç¼å¤çå¼ï¼å°±æ¯å¨ ð =1,â¯,ði=1,â¯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çææ â(ðð +ð)/ðââ(ai+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¼ï¼å æ­¤ï¼å¯¹äºæ´æ®µæä½åºåè®¡ç®ç âð¦ây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ¯æ¬é¢æç»è¦æ±çéï¼

åå§æ¶ï¼æ ð =(0,1,0)U=(0,1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð  =(1,0,0)R=(1,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ­¥ï¼å¯ä»¥å°ä¸¤ä¸ªå ç´ (ð¥1,ð¦1,ð 1)(x1,y1,s1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å (ð¥2,ð¦2,ð 2)(x2,y2,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹ç§¯å®ä¹ä¸º

(ð¥1,ð¦1,ð 1)â (ð¥2,ð¦2,ð 2)=(ð¥1+ð¥2,ð¦1+ð¦2,ð 1+ð 2+ð¥2ð¦1).(x1,y1,s1)â (x2,y2,s2)=(x1+x2,y1+y2,s1+s2+x2y1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼æåä¸é¡¹è´¡ç®åå¹¶çç»æå¯ä»¥éè¿å¦ä¸è®¡ç®å¾å°ï¼

âð1+ð2ð¦=âð1ð¦+âð2(ð¦+ð¦1)=âð1ð¦+âð2ð¦+ð¦1âð21=ð 1+ð 2+ð¥2ð¦1.âS1+S2y=âS1y+âS2(y+y1)=âS1y+âS2y+y1âS21=s1+s2+x2y1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®¹æéªè¯ï¼è¿ä¸ªä¹æ³è¿ç®æ»¡è¶³ç»åå¾ï¼ä¸å¹ºå ä¸º (0,0,0)(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥è¿äºå ç´ å¨è¯¥ä¹æ³è¿ç®ä¸ææå¹ºåç¾¤ï¼ææ±çç­æ¡ï¼å°±æ¯ä¹ç§¯çç¬¬ä¸ä¸ªåéï¼

è¿ä¸¤ç§æ¹æ³é½å¯ä»¥å¾å°æ­£ç¡®çç»æï¼ä½æ¯ï¼å ä¸ºä¿çäºè¾å¤çåä½ä¿¡æ¯ï¼ç©éµè¿ç®çå¸¸æ°è¾å¤§ï¼æä»¥ç¬¬äºç§æ¹æ³å¨å¤çå®é é®é¢æ¶æ´ä¸ºå®ç¨ï¼

### ç®æ³è¿ç¨

ä¸ç±»æ¬§å éå¾ç®æ³æ´ä½çº¦åä¸åï¼ä¸è½æ¬§å éå¾ç®æ³çº¦åé®é¢çææ®µæ¯å°è¿äºæä½åæ¹æ¬¡å°åå¹¶ï¼è®°å­ç¬¦ä¸²å¯¹åºçæä½çä¹ç§¯ä¸º

ð¹(ð,ð,ð,ð,ð,ð ).F(a,b,c,n,U,R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çº¦åè¿ç¨å ·ä½å¦ä¸ï¼

  * å½ ð â¥ðbâ¥c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æä½åºåçå¼å§æ âð/ðââb/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´æ¥è®¡ç®å®ä»¬çä¹ç§¯ï¼å¹¶å°è¿äº ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»æä½åºåä¸­ç§»é¤ï¼æ­¤æ¶ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éç­äº

âðð+ððâââððâ=âðð+(ðmodð)ðâ.âai+bcâââbcâ=âai+(bmodc)câ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼è¿ç¸å½äºå°çº¿æ®µåæ°ç± (ð,ð,ð,ð)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º (ð,ðmodð,ð,ð)(a,bmodc,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å¯¹äºè¿ç§æ å½¢ï¼æ

ð¹(ð,ð,ð,ð,ð,ð )=ðâð/ðâð¹(ð,ðmodð,ð,ð,ð,ð ).F(a,b,c,n,U,R)=Uâb/câF(a,bmodc,c,n,U,R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * å½ ð â¥ðaâ¥c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æä½åºåä¸­æ¯ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ¹é½è³å°æ âð/ðââa/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥å°å®ä»¬åå¹¶å° ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ï¼ä¹å°±æ¯è¯´ï¼å¯ä»¥ç¨ ðâð/ðâð Uâa/câR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿ä»£ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¹¶åçå­ç¬¦ä¸²ä¸­ï¼ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éç­äº

âðð+ððâââððâð=â(ðmodð)ð+ððâ.âai+bcâââacâi=â(amodc)i+bcâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼è¿ç¸å½äºå°çº¿æ®µåæ°ç± (ð,ð,ð,ð)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º (ðmodð,ð,ð,ð)(amodc,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å¯¹äºè¿ç§æ å½¢ï¼æ

ð¹(ð,ð,ð,ð,ð,ð )=ð¹(ðmodð,ð,ð,ð,ð,ðâð/ðâð ).F(a,b,c,n,U,R)=F(amodc,b,c,n,U,Uâa/câR).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * å¯¹äºå©ä¸çæ å½¢ï¼éè¦ç¿»è½¬æ¨ªçºµåæ ï¼è¿åºæ¬æ¯å¨äº¤æ¢ ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªæ¯ç¿»è½¬åçº¿æ®µçåæ°éè¦ä»ç»è®¡ç®ï¼ç»åæä½åºåçå®ä¹å¯ç¥ï¼éè¦ç¡®å®ç³»æ° (ðâ²,ðâ²,ðâ²,ðâ²)(aâ²,bâ²,câ²,nâ²)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾åæ¢åçæä½åºåä¸­ï¼ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éæ°ä¸º â(ðâ²ð +ðâ²)/ðâ²ââ(aâ²j+bâ²)/câ²â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ»å ±æ ðâ²nâ²![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ¹æ®å®ä¹å¯ç¥ï¼

ðâ²=âðð+ððâ=ð,nâ²=âan+bcâ=m,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éï¼å°±ç­äºæå¤§ç ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾

âðð+ððâ<ðâºðð+ðð<ðâºð<ððâððâºð<âððâððâ=âððâðâ1ðâ+1.âai+bcâ<jâºai+bc<jâºi<cjâbaâºi<âcjâbaâ=âcjâbâ1aâ+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ð =â(ðð âð â1)/ðâi=â(cjâbâ1)/aâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ¨å¯¼è¿ç¨ä¸åæç±»æ¬§å éå¾ç®æ³çæ¨å¯¼ç±»ä¼¼ï¼åæ ·å©ç¨äºä¸ä¸åæ´å½æ°çæ§è´¨ï¼

æä¸¤å¤ç»èéè¦å¤çï¼

    * æªè·é¡¹ â(ð +1)/ðâ(b+1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºè´æ°ï¼æ³¨æå°ï¼å¦æå°çº¿æ®µåå·¦å¹³ç§»ä¸ä¸ªåä½ï¼å°±å¯ä»¥è®©æªè·é¡¹æ¢å¤ä¸ºéè´æ°ï¼å ä¸ºæ»æ (ð âð â1)/ð â¥0(câbâ1)/aâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¯ä»¥å°äº¤æ¢åçç¬¬ä¸æ®µ ð â(ðâðâ1)/ðâðRâ(câbâ1)/aâU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æååºæ¥ï¼åªäº¤æ¢å©ä½æä½åºåä¸­ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
    * äº¤æ¢ ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åï¼ç»å°¾å­å¨å¤ä½ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼äº¤æ¢ ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åï¼éè¦é¦å å°æåä¸æ®µ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æååºæ¥ï¼åªäº¤æ¢å©ä½æä½åºåä¸­ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸æ®µ ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éä¸º ð ââ(ðð âð â1)/ðânââ(cmâbâ1)/aâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å»æå¤´å°¾è¥å¹²ä¸ªå­ç¬¦åï¼ç¬¬ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹ç ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éåä¸ºï¼

âð(ð+1)âðâ1ðâââðâðâ1ðâ=âðð+(ðâðâ1)modððâ.âc(j+1)âbâ1aâââcâbâ1aâ=âcj+(câbâ1)modaaâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå¿èµ·ï¼äº¤æ¢åçåºåä¸­ ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°éä¸º ð =â(ðð +ð)/ðâm=â(an+b)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸è¿°å·¦ç§»ä¸ä¸ªåä½çæä½ï¼è¦æ±ä¿è¯äº¤æ¢åè³å°å­å¨ä¸ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯ ð >0m>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å©ç¨è¿ä¸æ¡ä»¶ï¼å¯ä»¥åä¸ºä¸¤ç§æ å½¢ï¼

    * å¯¹äº ð >0m>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼å¤çäºä¸é¢çä¸¤ç¹åï¼äº¤æ¢å® ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½åºåå°±æ¯å¯¹åºçåæ°ä¸º (ð,(ð âð â1)modð,ð,ð â1)(c,(câbâ1)moda,a,mâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ®µçåæ³åºåï¼æä»¥ï¼æ

ð¹(ð,ð,ð,ð,ð,ð )=ð â(ðâðâ1)/ðâðð¹(ð,(ðâðâ1)modð,ð,ðâ1,ð ,ð)ð ðââ(ððâðâ1)/ðâ.F(a,b,c,n,U,R)=Râ(câbâ1)/aâUF(c,(câbâ1)moda,a,mâ1,R,U)Rnââ(cmâbâ1)/aâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
    * ç¹å«å°ï¼å¯¹äº ð =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼äº¤æ¢åçæä½åºåä¸­åªå å« ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ éäº¤æ¢ï¼å¯ä»¥ç´æ¥è¿åï¼

ð¹(ð,ð,ð,ð,ð,ð )=ð ð.F(a,b,c,n,U,R)=Rn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ç±»æ¬§å éå¾ç®æ³ä¸åï¼ä¸è½æ¬§å éå¾ç®æ³çè¿ä¸ç¹æ®æ å½¢éè¦åç¬å¤çï¼å¦åä¼å æ¶åè´å¹æ¬¡èæ æ³æ­£ç¡®è®¡ç®ï¼

å©ç¨è¿äºè®¨è®ºï¼å°±å¯ä»¥å°é®é¢éå½å°è§£å³ï¼

åè®¾å¹ºåç¾¤å å ç´ åæ¬¡ç¸ä¹çæ¶é´å¤æåº¦æ¯ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼é£ä¹ï¼å¦æè®¡ç®è¿ç¨ä¸­è¿äºå ç´ çå¹æ¬¡è®¡ç®é½ä½¿ç¨ [å¿«éå¹](../../binary-exponentiation/) è¿è¡ï¼æç»çç®æ³å¤æåº¦å°±æ¯ ð(logâ¡max{ð,ð} +logâ¡(ð/ð))O(logâ¡max{a,c}+logâ¡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç1ï¼

å¯¹å¤æåº¦çè§£é

å¯¹æ¯ï¼ç±»ï¼æ¬§å éå¾ç®æ³ï¼ä¸è½æ¬§å éå¾ç®æ³åªæ¯å¤äºæ±å¿«éå¹çæ­¥éª¤ï¼å ¶ä½çè®¡ç®è¿ç¨çå¤æåº¦åç±»æ¬§å éå¾ç®æ³ç¸ä»¿ï¼å·²ç»è¯´ææ¯ ð(logâ¡min{ð,ð,ð})O(logâ¡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼ç°å¨ï¼éè¦è®¡ç®è¿äºå¿«éå¹çæ»å¤æåº¦ï¼

é¤äºç¬¬ä¸è½®è¿­ä»£ï¼é½æ ð <ðb<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤è¿äºè¿­ä»£æ¯è½®é½æ¶åä¸æ¬¡å¿«éå¹çè®¡ç®ï¼æ»çå¤æåº¦æ¯ï¼

ð(logâ¡âððâ+logâ¡âðâð1â1ð1â+logâ¡(ðââððâð1â1ð1â)),O(logâ¡âacâ+logâ¡âcâb1â1a1â+logâ¡(nââcmâb1â1a1â)),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ð1 =ðmodða1=amodc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð1 =ðmodðb1=bmodc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð =â(ð1ð +ð1)/ðâm=â(a1n+b1)/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åé¢ä¸¤é¡¹ï¼åå«æä¼°è®¡ï¼

ðâð1â1ð1â¤ðð1,ðââððâð1â1ð1ââ¤ðâððâð1â1ð1+1â¤ðâð((ð1ð+ð1)/ðâ1)âð1â1ð1+1=ð+1ð1+1.câb1â1a1â¤ca1,nââcmâb1â1a1ââ¤nâcmâb1â1a1+1â¤nâc((a1n+b1)/câ1)âb1â1a1+1=c+1a1+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼è¿ä¸¤é¡¹çå¤æåº¦é½æ¯ ð(logâ¡(ð/ð1))O(logâ¡(c/a1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

æ¯ä¸è½®è¿­ä»£ä¸­ï¼çº¿æ®µçåæ°é½ç± (ð, â ,ð, â )(a,â ,c,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¢ä¸º (ð, â ,ðmodð, â )(c,â ,amodc,â )![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è¯¥è½®æ»çæ¶é´å¤æåº¦ä¸º

ð(logâ¡ðð+logâ¡ððmodð).O(logâ¡ac+logâ¡camodc).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹äºå ¨é¨éå½çè½®æ¬¡ï¼è¿äºé¡¹å¯ä»¥è£é¡¹ç¸æ¶ï¼å æ­¤ï¼æåæ»åå¤æåº¦å°±æ¯ ð(logâ¡ð +logâ¡ð) =ð(logâ¡max{ð,ð})O(logâ¡a+logâ¡c)=O(logâ¡max{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

æåï¼åå ä¸ç¬¬ä¸è½®è¿­ä»£ä¸­å¿«éå¹ ðâð/ðâUâb/câ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤æåº¦ ð(logâ¡(ð/ð))O(logâ¡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°æ»çå¤æåº¦ä¸º ð(logâ¡max{ð,ð} +logâ¡(ð/ð))O(logâ¡max{a,c}+logâ¡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸è½æ¬§å éå¾ç®æ³çæµç¨å¯ä»¥åæç»ä¸çæ¨¡æ¿ï¼å¤çå ·ä½é®é¢æ¶åªéè¦æ´æ¹æ¨¡æ¿ç±»å `T` çå®ç°å³å¯ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // Class T implements the monoid. // Assume that it provides a multiplication operator // and a default constructor returning the unity in the monoid. // Binary exponentiation. template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } // Universal Euclidean algorithm. template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } ```   
---|---  
  
å©ç¨ä¸è½æ¬§å éå¾ç®æ³å¯ä»¥å¾å°æ¨¡æ¿é¢çå®ç°å¦ä¸ï¼

æ¨¡æ¿é¢å®ç°ï¼[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 ``` |  ```text #include <array> #include <iostream> // Switch between matrix and info merging approaches. #define MATRIX 1 // Class T implements the monoid. // Assume that it provides a multiplication operator // and a default constructor returning the unity in the monoid. // Binary exponentiation. template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } // Universal Euclidean algorithm. template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } #if MATRIX template < size_t N > struct Matrix { std :: array < long long , N * N > mat ; auto loc ( size_t i , size_t j ) const { return mat [ i * N \+ j ]; } auto & loc ( size_t i , size_t j ) { return mat [ i * N \+ j ]; } Matrix () : mat {} { for ( size_t i = 0 ; i != N ; ++ i ) { loc ( i , i ) = 1 ; } } Matrix operator * ( const Matrix & rhs ) const { Matrix res ; res . mat . fill ( 0 ); for ( size_t i = 0 ; i != N ; ++ i ) { for ( size_t k = 0 ; k != N ; ++ k ) { for ( size_t j = 0 ; j != N ; ++ j ) { res . loc ( i , j ) += loc ( i , k ) * rhs . loc ( k , j ); } } } return res ; } }; long long solve ( int a , int b , int c , int n ) { if ( ! n ) return 0 ; Matrix < 3 > U , R ; U . loc ( 0 , 1 ) = R . loc ( 1 , 2 ) = 1 ; auto res = euclid ( a , b , c , n , U , R ); return res . loc ( 0 , 2 ); } #else struct Info { long long x , y , s ; Info () : x ( 0 ), y ( 0 ), s ( 0 ) {} Info operator * ( const Info & rhs ) const { Info res ; res . x = x \+ rhs . x ; res . y = y \+ rhs . y ; res . s = s \+ rhs . s \+ rhs . x * y ; return res ; } }; long long solve ( int a , int b , int c , int n ) { if ( ! n ) return 0 ; Info U , R ; U . y = 1 ; R . x = 1 ; auto res = euclid ( a , b , c , n , U , R ); return res . s ; } #endif int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> c >> a >> b ; std :: cout << solve ( a , b , c , n \- 1 ) << '\n' ; } return 0 ; } ```   
---|---  
  
### ä¾é¢

[ãæ¨¡æ¿ãç±»æ¬§å éå¾ç®æ³](https://www.luogu.com.cn/problem/P5170)

å¤ç»è¯¢é®ï¼ç»å®æ­£æ´æ° ð,ð,ð,ða,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±

ð(ð,ð,ð,ð)=ðâð=0âðð+ððâ,ð(ð,ð,ð,ð)=ðâð=0ðâðð+ððâ,â(ð,ð,ð,ð)=ðâð=0âðð+ððâ2.f(a,b,c,n)=âi=0nâai+bcâ,g(a,b,c,n)=âi=0niâai+bcâ,h(a,b,c,n)=âi=0nâai+bcâ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è§£ç­äº

ä¸ºäºåºç¨ä¸è½æ¬§å éå¾ç®æ³çæ¨¡æ¿ï¼é¦å å° ð =0i=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¡¹æåºæ¥ï¼åç¬èèï¼å¯¹äºå©ä¸çé¨åï¼å¯ä»¥çä½æ¯å¯¹åæ°ä¸º (ð,ð,ð,ð)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ®µåå«è®¡ç® âð¦,âð¥ð¦,âð¦2ây,âxy,ây2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ­£ææè¨ï¼æä¸¤ç§å°æä½åºåè½¬æ¢ä¸ºå¹ºåç¾¤å ç´ çæ¹å¼ï¼

**ç©éµè¿ç®** ï¼ç¶æåéå®ä¹ä¸º (1,ð¥,ð¦,ð¥ð¦,ð¦2,âð¦,âð¥ð¦,âð¦2)(1,x,y,xy,y2,ây,âxy,ây2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå§ç¶æä¸º (1,0,0,0,0,0,0,0)(1,0,0,0,0,0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¤ä¸ªæä½åå«ä¸º

ð=ââ â â â â â â â â â â â â â â â â â ââ1010100001010000001020000001000000001000000001000000001000000001ââ â â â â â â â â â â â â â â â â â ââ ,Â ð =ââ â â â â â â â â â â â â â â â â â ââ1100000001000000001101100001001000001001000001000000001000000001ââ â â â â â â â â â â â â â â â â â ââ .U=(1010100001010000001020000001000000001000000001000000001000000001),Â R=(1100000001000000001101100001001000001001000001000000001000000001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç»ç­æ¡ä¸ºåå§ç¶æå³ä¹è¿äºæä½ç©éµçä¹ç§¯å¾å°çåéæ«å°¾ä¸ä¸ªåéï¼

è¿ä¸ªåæ³çå¸¸æ°å·¨å¤§ï¼å¹¶ä¸è½éè¿æ¬é¢ï¼è¿éç»åºç»èä» ä» æ¯ä¸ºäºè¾ å©çè§£ï¼

**è´¡ç®åå¹¶** ï¼ä¸æ®µæä½åºåçè´¡ç®å®ä¹ä¸º (ð¥,ð¦,âð¦,âð¥ð¦,âð¦2)(x,y,ây,âxy,ây2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¤ä¸ªæä½åå«ä¸º

ð=(0,1,0,0,0),Â ð =(1,0,0,0,0).U=(0,1,0,0,0),Â R=(1,0,0,0,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è´¡ç®åå¹¶æ¶ï¼æ

âð1+ð2ð¦=âð1ð¦+âð2(ð¦+ð¦1)=âð1ð¦+âð2ð¦+ð¥2ð¦1,âð1+ð2ð¥ð¦=âð1ð¥ð¦+âð2(ð¥+ð¥1)(ð¦+ð¦1)=âð1ð¥ð¦+âð2ð¥ð¦+ð¥1âð2ð¦+ð¦1âð2ð¥+ð¥1ð¦1âð21=âð1ð¥ð¦+âð2ð¥ð¦+ð¥1âð2ð¦+12ð¥2(ð¥2+1)ð¦1+ð¥1ð¥2ð¦1,âð1+ð2ð¦2=âð1ð¦2+âð2(ð¦+ð¦1)2=âð1ð¦2+âð2ð¦2+2ð¦1âð2ð¦+ð¦21âð21=âð1ð¦2+âð2ð¦2+2ð¦1âð2ð¦+ð¥2ð¦21.âS1+S2y=âS1y+âS2(y+y1)=âS1y+âS2y+x2y1,âS1+S2xy=âS1xy+âS2(x+x1)(y+y1)=âS1xy+âS2xy+x1âS2y+y1âS2x+x1y1âS21=âS1xy+âS2xy+x1âS2y+12x2(x2+1)y1+x1x2y1,âS1+S2y2=âS1y2+âS2(y+y1)2=âS1y2+âS2y2+2y1âS2y+y12âS21=âS1y2+âS2y2+2y1âS2y+x2y12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿è¯´æï¼åºè¯¥å°æä½çä¹æ³å®ä¹ä¸º

(ð¥1,ð¦1,ð 1,ð¡1,ð¢1)â (ð¥2,ð¦2,ð 2,ð¡2,ð¢2)=(ð¥1+ð¥2,ð¦1+ð¦2,ð 1+ð 2+ð¥2ð¦1,ð¡1+ð¡2+ð¥1ð 2+(1/2)ð¥2(ð¥2+1)ð¦1+ð¥1ð¥2ð¦1,ð¢1+ð¢2+2ð¦1ð 2+ð¥2ð¦21).(x1,y1,s1,t1,u1)â (x2,y2,s2,t2,u2)=(x1+x2,y1+y2,s1+s2+x2y1,t1+t2+x1s2+(1/2)x2(x2+1)y1+x1x2y1,u1+u2+2y1s2+x2y12).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è½ç¶ç´æ¥éªè¯è¾ä¸ºç¹çï¼ä½æ¯ä¸è¿°å®ä¹çè´¡ç®åéå¨è¯¥ä¹æ³ä¸çç¡®ææå¹ºåç¾¤ï¼åä½å ä¸º (0,0,0,0,0)(0,0,0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äºä¸è¬çæ å½¢ï¼æ

âð1+ð2ð¥ðð¦ð =âð1ð¥ðð¦ð +âð2(ð¥+ð¥1)ð(ð¦+ð¦1)ð =âð1ð¥ðð¦ð +ðâð=0ð âð=0(ðð)(ð ð)ð¥ðâð1ð¦ð âð1âð2ð¥ðð¦ð.âS1+S2xrys=âS1xrys+âS2(x+x1)r(y+y1)s=âS1xrys+âi=0râj=0s(ri)(sj)x1râiy1sâjâS2xiyj.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åªè¦ç»´æ¤å¥½æææ´ä½å¹æ¬¡çè´¡ç®ï¼å°±å¯ä»¥è®¡ç®ä¸è¬æ å½¢çåå¼ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ``` |  ```text #include <iostream> template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } constexpr int M = 998244353 ; struct Info { long long x , y , s , t , u ; Info () : x ( 0 ), y ( 0 ), s ( 0 ), t ( 0 ), u ( 0 ) {} Info operator * ( const Info & rhs ) const { Info res ; res . x = ( x \+ rhs . x ) % M ; res . y = ( y \+ rhs . y ) % M ; res . s = ( s \+ rhs . s \+ rhs . x * y ) % M ; auto tmp = ( rhs . x * ( rhs . x \+ 1 ) / 2 \+ x * rhs . x ) % M ; res . t = ( t \+ rhs . t \+ x * rhs . s \+ tmp * y ) % M ; res . u = ( u \+ rhs . u \+ 2 * y * rhs . s \+ rhs . x * y % M * y ) % M ; return res ; } }; void solve ( int a , int b , int c , int n ) { Info U , R ; U . y = 1 ; R . x = 1 ; auto res = euclid ( a , b , c , n , U , R ); auto f = ( res . s \+ b / c ) % M ; auto g = res . t ; auto h = ( res . u \+ ( long long )( b / c ) * ( b / c )) % M ; std :: cout << f << ' ' << h << ' ' << g << '\n' ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> a >> b >> c ; solve ( a , b , c , n ); } return 0 ; } ```   
---|---  
  
[[æ¸ åéè®­ 2014] Sum](https://www.luogu.com.cn/problem/P5172)

å¤ç»è¯¢é®ï¼ç»å®æ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±

ðâð=1(â1)âðâðâ.âd=1n(â1)âdrâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)è§£ç­äº

é¦å ï¼åç¬å¤ç ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå®å ¨å¹³æ¹æ°çæ å½¢ï¼ä¸åæå®å ¨ä¸è´ï¼ä»ç¥ï¼æ­¤å¤ï¼ä» èè ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æ¯å®å ¨å¹³æ¹æ°çæ å½¢ï¼

æ¬é¢åºç¨ä¸è½æ¬§å éå¾ç®æ³çæ¹å¼æå¾å¤ï¼æ¯å¦è¯´ï¼å¯ä»¥ä¸ºæ¯ä¸ªæä½å®ä¹ä¸ä¸ªçº¿æ§åæ¢ï¼

ð(ð¥)=âð¥,Â ð (ð¥)=ð¥+1.U(x)=âx,Â R(x)=x+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä½çä¹æ³å®ä¹ä¸ºçº¿æ§åæ¢çå¤åï¼é£ä¹ï¼æç»çç­æ¡å°±æ¯æä½åºåå¯¹åºçåæ¢çå¤åå¾å°çå½æ°å¨ ð¥ =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çå¼ï¼

è¿å¯ä»¥ä¸ºæ¯æ®µæä½åºåå®ä¹å®çè´¡ç®ï¼è´¡ç®å¯ä»¥å®ä¹ä¸º (( â1)ð¦,â( â1)ð¦)((â1)y,â(â1)y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ä¸¤ä¸ªæä½åå«å

ð=(0,â1),Â ð =(1,1).U=(0,â1),Â R=(1,1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è´¡ç®çåå¹¶å®ä¹ä¸º

(ð¢1,ð£1)â (ð¢2,ð£2)=(ð¢1ð¢2,ð£1+ð¢1ð£2).(u1,v1)â (u2,v2)=(u1u2,v1+u1v2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®¹æéªè¯ï¼å¨è¯¥ä¹æ³ä¸ï¼æææä½ææäºå¹ºåç¾¤ï¼ä¸åä½å ä¸º (0,1)(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç»çç­æ¡å°±æ¯ææå ç´ ä¹ç§¯çç¬¬äºä¸ªåéï¼

è¿ä¸¤ç§æ¹æ³æ¯ä¸è´çï¼å ä¸ºå¦æå°çº¿æ§åæ¢åä½ ð(ð¥) =ð¢ +ð£ð¥f(x)=u+vx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹çº¿æ§åæ¢çå¤åå¯¹åºçç³»æ°çååï¼æ°æ°å°±æ¯ä¸è¿°æä½çä¹æ³ï¼ä¹å°±æ¯è¯´ï¼è¿ä¸¤ä¸ªå¹ºåç¾¤æ¯åæçï¼

æ¬é¢ä¸­ï¼çº¿æ®µçåæ°ä¸º (ð,ð)(k,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð âðkâR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºç´çº¿çæçï¼è®¾æä½åºåå¯¹åºçä¹ç§¯ä¸º ð¹(ð,ð,ð,ð )F(k,n,U,R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æå¦ä¸éå½ç®æ³ï¼

  * å¦æ ð â¥1kâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æä½åºåä¸­æ¯ä¸ª ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¹é½æè³å° âðââkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼æ

ð¹(ð,ð,ð,ð )=ð¹(ðââðâ,ð,ð,ðâðâð ).F(k,n,U,R)=F(kââkâ,n,U,UâkâR).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * å¦æ ð <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹äº¤æ¢æä½åºåä¸­ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶èå»æ«å°¾ç ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³äº¤æ¢åç ð R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼æä»¥ï¼æ

ð¹(ð,ð,ð,ð )=ð¹(ðâ1,ð,ð ,ð)ð ðââðâ1ðâ.F(k,n,U,R)=F(kâ1,m,R,U)Rnââkâ1mâ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç®æ³ä¸­ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿­ä»£è¿ç¨å ¶å®å°±æ¯å¨æ± âðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¿åæ°å±å¼ï¼ä¸ºæ­¤ï¼å¯ä»¥åºç¨ [PQa ç®æ³](../pell-equation/#pqa-ç®æ³)ï¼æ±è¿åæ°çè¿ç¨åä¸è½æ¬§å éå¾ç®æ³è¿­ä»£çè¿ç¨å¯ä»¥åæ¶è¿è¡ï¼

åç±»æ¬§å éå¾ç®æ³çæ å½¢ä¸è´ï¼ç®æ³çå¤æåº¦ä»ç¶æ¯ ð(logâ¡ð)O(logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } struct LinearTransform { int u , v ; LinearTransform () : u ( 0 ), v ( 1 ) {} LinearTransform operator * ( const LinearTransform & rhs ) const { LinearTransform res ; res . u = u \+ v * rhs . u ; res . v = v * rhs . v ; return res ; } int eval ( int x ) const { return u \+ v * x ; } }; int solve ( int n , int r ) { long double sqrt_r = sqrtl ( r ); int sqr = sqrt_r ; if ( r == sqr * sqr ) return sqr % 2 ? ( n % 2 ? -1 : 0 ) : n ; int P = 0 , Q = 1 , D = r , val = 0 ; LinearTransform U , R ; U . v = -1 ; R . u = 1 ; while ( n ) { int a = ( P \+ sqr ) / Q ; R = pow ( U , a ) * R ; int m = (( P \+ sqrt_r ) / Q \- a ) * n ; P = a * Q \- P ; Q = ( D \- P * P ) / Q ; int rem = n \- ( int )( m * ( P \+ sqrt_r ) / Q ); val = pow ( R , rem ). eval ( val ); std :: swap ( U , R ); n = m ; } return val ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n , r ; std :: cin >> n >> r ; std :: cout << solve ( n , r ) << '\n' ; } return 0 ; } ```   
---|---  
  
## ä¹ é¢

æ¨¡æ¿é¢ï¼

  * [Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
  * [Luogu P5170ãæ¨¡æ¿ãç±»æ¬§å éå¾ç®æ³](https://www.luogu.com.cn/problem/P5170)
  * [Luogu P5171 Earthquake](https://www.luogu.com.cn/problem/P5171)
  * [Luogu P5172 [æ¸ åéè®­ 2014] Sum](https://www.luogu.com.cn/problem/P5172)
  * [Luogu P4132 [BJOI2012] ç®ä¸åºçç­å¼](https://www.luogu.com.cn/problem/P4132)
  * [LOJ 138. ç±»æ¬§å éå¾ç®æ³](https://loj.ac/p/138)
  * [LOJ 6440. ä¸è½æ¬§å éå¾](https://loj.ac/p/6440)
  * [Luogu P5179 Fraction](https://www.luogu.com.cn/problem/P5179)
  * [Codeforces 1182 F. Maximum Sine](https://codeforces.com/problemset/problem/1182/F)

åºç¨é¢ï¼

  * [Luogu P4433 [COCI 2009/2010 #1] ALADIN](https://www.luogu.com.cn/problem/P4433)
  * [AtCoder Beginner Contest 372 G - Ax + By < C](https://atcoder.jp/contests/abc372/tasks/abc372_g)
  * [AtCoder Beginner Contest 313 G - Redistribution of Piles](https://atcoder.jp/contests/abc313/tasks/abc313_g)
  * [AtCoder Beginner Contest 283 Ex - Popcount Sum](https://atcoder.jp/contests/abc283/tasks/abc283_h)
  * [Codeforces 1098 E. Fedya the Potter](https://codeforces.com/problemset/problem/1098/E)
  * [Codeforces 868 G. El Toll Caves](https://codeforces.com/problemset/problem/868/G)

## åèèµæä¸æ³¨é

* * *

  1. éå¸¸èèçé®é¢ä¸­ï¼ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ä¸ ða![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¶ï¼ð(logâ¡(ð/ð))O(logâ¡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸é¡¹å¯ä»¥å¿½ç¥ï¼èä¸ï¼å¦æå¨è°ç¨ä¸è½æ¬§å éå¾ç®æ³åï¼é¦å è¿è¡äºä¸è½®ç±»æ¬§å éå¾ç®æ³çåæ¨¡ï¼æ¶é¤ ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½±åï¼è¿ä¸é¡¹çå¿«éå¹çå¤æåº¦æ¯å¯ä»¥è§é¿çï¼è¿å ¶å®æ¯å ä¸ºéå¸¸çé®é¢ä¸­ï¼ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå§å½¢å¼è¾ä¸ºç¹æ®ï¼å®çå¹æ¬¡æçæ´ç®åçå½¢å¼ï¼ä¸éè¦éè¿å¿«éå¹è®¡ç®ï¼æ¯å¦æ­£æçä¾å­ä¸­ï¼ðâð/ðâUâb/aâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç»æï¼å°±æ¯å° ðU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸å¨å¯¹è§çº¿ä¸çé£ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¿æ¢æ âð/ðââb/aâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èæ éç¨å¿«éå¹è®¡ç®ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/euclidean.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/euclidean.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Ir1d](https://github.com/Ir1d), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [FFjet](https://github.com/FFjet), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [qz-cqy](https://github.com/qz-cqy), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [alphagocc](https://github.com/alphagocc), [cxm1024](https://github.com/cxm1024), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [megakite](https://github.com/megakite), [Peanut-Tang](https://github.com/Peanut-Tang), [r-value](https://github.com/r-value), [SukkaW](https://github.com/SukkaW), [TonyYin0418](https://github.com/TonyYin0418)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
