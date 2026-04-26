# BerlekampâMassey ç®æ³ - OI Wiki

- Source: https://oi-wiki.org/math/berlekamp-massey/

# BerlekampâMassey ç®æ³

BerlekampâMassey ç®æ³æ¯ä¸ç§ç¨äºæ±æ°åçæç­éæ¨å¼çç®æ³ï¼ç»å®ä¸ä¸ªé¿ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ°åï¼å¦æå®çæç­éæ¨å¼çé¶æ°ä¸º ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å BerlekampâMassey ç®æ³è½å¤å¨ ð(ðð)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æ±åºæ°åçæ¯ä¸ªåç¼çæç­éæ¨å¼ï¼æåæ åµä¸ ð =ð(ð)m=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ç®æ³çæåå¤æåº¦ä¸º ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### å®ä¹

å®ä¹ä¸ä¸ªæ°å {ð0â¦ððâ1}{a0â¦anâ1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨å¼ä¸ºæ»¡è¶³ä¸å¼çåºå {ð0â¦ðð}{r0â¦rm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

âðð=0ððððâð =0,âð â¥ðâj=0mrjaiâj=0,âiâ¥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ ð0 =1r0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºè¯¥éæ¨å¼ç **é¶æ°** ï¼

æ°å {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼å³ä¸ºé¶æ°æå°çéæ¨å¼ï¼

### åæ³

ä¸ä¸é¢å®ä¹çç¨æä¸åï¼è¿éå®ä¹ä¸ä¸ªæ°çéæ¨ç³»æ° {ð0â¦ððâ1}{f0â¦fmâ1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»¡è¶³ï¼

ðð =âðâ1ð=0ððððâðâ1,âð â¥ðai=âj=0mâ1fjaiâjâ1,âiâ¥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®¹æçåº ðð = âðð+1fi=âri+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸é¶æ° ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¹åçå®ä¹æ¯ç¸åçï¼

æä»¬å¯ä»¥å¢éå°æ±éæ¨å¼ï¼æé¡ºåºèè {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¯ä¸ä½ï¼å¹¶å¨éæ¨ç»æåºç°éè¯¯æ¶å¯¹éæ¨ç³»æ° {ðð}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡è°æ´ï¼æ¹ä¾¿èµ·è§ï¼ä»¥ä¸å°å ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çæç­éæ¨å¼è®°ä¸º ð¹ð ={ðð,ð}Fi={fi,j}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

æ¾ç¶åå§æ¶æ ð¹0 ={}F0={}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾éæ¨ç³»æ° ð¹ðâ1Fiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹æ°å {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ð â1iâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹åæç«ï¼è¿æ¶å¯¹ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹å°±æä¸¤ç§æ åµï¼

  1. éæ¨ç³»æ°å¯¹ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æç«ï¼è¿æ¶ä¸éè¦è¿è¡ä»»ä½è°æ´ï¼ç´æ¥ä»¤ ð¹ð =ð¹ðâ1Fi=Fiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼
  2. éæ¨ç³»æ°å¯¹ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸æç«ï¼è¿æ¶éè¦å¯¹ ð¹ðâ1Fiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡è°æ´ï¼å¾å°æ°ç ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è®¾ Îð =ðð ââðð=0ððâ1,ðððâðâ1Îi=aiââj=0mfiâ1,jaiâjâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð¹ðâ1Fiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéæ¨ç»æçå·®å¼ï¼

å¦æè¿æ¯ç¬¬ä¸æ¬¡å¯¹éæ¨ç³»æ°è¿è¡ä¿®æ¹ï¼åè¯´æ ððai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åºåä¸­çç¬¬ä¸ä¸ªéé¶é¡¹ï¼è¿æ¶ç´æ¥ä»¤ ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼æ¾ç¶è¿æ¯ä¸ä¸ªåæ³çæç­éæ¨å¼ï¼

å¦åè®¾ä¸ä¸æ¬¡å¯¹éæ¨ç³»æ°è¿è¡ä¿®æ¹æ¶ï¼å·²èèç {ðð}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé¡¹æ°ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æå­å¨ä¸ä¸ªåºå ðº ={ð0â¦ððâ²â1}G={g0â¦gmâ²â1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»¡è¶³ï¼

âðâ²â1ð=0ððððâ²âðâ1 =0,âðâ² â[ðâ²,ð)âj=0mâ²â1gjaiâ²âjâ1=0,âiâ²â[mâ²,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¹¶ä¸ âðâ²â1ð=0ððððâðâ1 =Îðâj=0mâ²â1gjaiâjâ1=Îi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ä¸é¾åç°å° ð¹ðFk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä½åå«ç¸å ä¹åå³å¯å¾å°ä¸ä¸ªåæ³çéæ¨ç³»æ° ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

èèå¦ä½æé ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ç§å¯è¡çæé æ¹æ¡æ¯ä»¤

ðº ={0,0,â¦,0,ÎðÎð, âÎðÎðð¹ðâ1}G={0,0,â¦,0,ÎiÎk,âÎiÎkFkâ1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­åé¢ä¸å ±æ ð âð â1iâkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æåç âÎðÎðð¹ðâ1âÎiÎkFkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå° ð¹ðâ1Fkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é¡¹ä¹ä»¥ âÎðÎðâÎiÎk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¥å¨åºååé¢ï¼

ä¸é¾éªè¯æ­¤æ¶ âðâ²â1ð=0ððððâðâ1 =ÎðÎðÎð =Îðâj=0mâ²â1gjaiâjâ1=ÎkÎiÎk=Îi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤è¿æ ·æé åºçæ¯ä¸ä¸ªåæ³ç ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ð¹ðFi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èµå¼ä¸º ð¹ðFk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ðºG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éé¡¹ç¸å åçç»æå³å¯ï¼

å¦æè¦æ±çæ¯ç¬¦åæå¼å§å®ä¹çéæ¨å¼ {ðð}{ri}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå° {ðð}{fj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ¨é¨åç¸åæ°åå¨æå¼å§æå ¥ ð0 =1r0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

ä»ä¸è¿°ç®æ³æµç¨ä¸­å¯ä»¥çåºï¼å¦ææ°åçæç­éæ¨å¼çé¶æ°ä¸º ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç®æ³çå¤æåº¦ä¸º ð(ðð)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æåæ åµä¸ ð =ð(ð)m=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ç®æ³çæåå¤æåº¦ä¸º ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¨å®ç°ç®æ³æ¶ï¼ç±äºæ¯æ¬¡è°æ´éæ¨ç³»æ°æ¶é½åªéè¦ç¨å°ä¸æ¬¡è°æ´æ¶çéæ¨ç³»æ° ð¹ðFk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å¦æåªéè¦æ±æ´ä¸ªæ°åçæç­éæ¨å¼ï¼å¯ä»¥åªå­å¨å½åéæ¨ç³»æ°åä¸æ¬¡è°æ´æ¶çéæ¨ç³»æ°ï¼ç©ºé´å¤æåº¦ä¸º ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text vector < int > berlekamp_massey ( const vector < int > & a ) { vector < int > v , last ; // v is the answer, 0-based, p is the module int k = -1 , delta = 0 ; for ( int i = 0 ; i < ( int ) a . size (); i ++ ) { int tmp = 0 ; for ( int j = 0 ; j < ( int ) v . size (); j ++ ) tmp = ( tmp \+ ( long long ) a [ i \- j \- 1 ] * v [ j ]) % p ; if ( a [ i ] == tmp ) continue ; if ( k < 0 ) { k = i ; delta = ( a [ i ] \- tmp \+ p ) % p ; v = vector < int > ( i \+ 1 ); continue ; } vector < int > u = v ; int val = ( long long )( a [ i ] \- tmp \+ p ) * power ( delta , p \- 2 ) % p ; if ( v . size () < last . size () \+ i \- k ) v . resize ( last . size () \+ i \- k ); ( v [ i \- k \- 1 ] += val ) %= p ; for ( int j = 0 ; j < ( int ) last . size (); j ++ ) { v [ i \- k \+ j ] = ( v [ i \- k \+ j ] \- ( long long ) val * last [ j ]) % p ; if ( v [ i \- k \+ j ] < 0 ) v [ i \- k \+ j ] += p ; } if (( int ) u . size () \- i < ( int ) last . size () \- k ) { last = u ; k = i ; delta = a [ i ] \- tmp ; if ( delta < 0 ) delta += p ; } } for ( auto & x : v ) x = ( p \- x ) % p ; v . insert ( v . begin (), 1 ); return v ; // $\forall i, \sum_{j = 0} ^ m a_{i - j} v_j = 0$ } ```   
---|---  
  
æ´ç´ ç BerlekampâMassey ç®æ³æ±è§£çæ¯æéé¡¹æ°åçæç­éæ¨å¼ï¼å¦æå¾ æ±éæ¨å¼çåºåææ éé¡¹ï¼ä½å·²ç¥æç­éæ¨å¼çé¶æ°ä¸çï¼ååªéååºåºåçå 2ð2m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹å³å¯æ±åºæ´ä¸ªåºåçæç­éæ¨å¼ï¼ï¼è¯æç¥ï¼

### åºç¨

ç±äº BerlekampâMassey ç®æ³çæ°å¼ç¨³å®æ§æ¯è¾å·®ï¼å¨å¤çå®æ°é®é¢æ¶ä¸è¬å¾å°ä½¿ç¨ï¼ä¸ºäºåè¿°æ¹ä¾¿ï¼ä»¥ä¸ååå®å¨æä¸ªè´¨æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå©ä½ç³»ä¸è¿è¡è¿ç®ï¼

#### æ±åéåæç©éµåçæç­éæ¨å¼

å¦æè¦æ±åéå ððvi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼ï¼è®¾åéçç»´æ°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å¯ä»¥éæºä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´è¡åé ð®ðuT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®¡ç®æ éåºå {ðððð}{uTvi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼ï¼ç± SchwartzâZippel å¼çï¼äºè çæç­éæ¨å¼æè³å° 1 âðð1ânp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¦çç¸åï¼

æ±ç©éµå {ð´ð}{Ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼ä¹æ¯ç±»ä¼¼çï¼è®¾ç©éµçå¤§å°ä¸º ð ÃðnÃm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ååªééæºä¸ä¸ª 1 Ãð1Ãn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡åé ð®ðuT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ä¸ª ð Ã1mÃ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååé ðv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶è®¡ç®æ éåºå {ððð´ðð}{uTAiv}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼å³å¯ï¼ç± SchwartzâZippel å¼çå¯ä»¥ç±»ä¼¼å°å¾å°äºè ç¸åçæ¦çè³å°ä¸º 1 âð+ðð1ân+mp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### ä¼åç©éµå¿«éå¹

è®¾ ððfi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»´ååéï¼å¹¶ä¸è½¬ç§»æ»¡è¶³ ðð =ð´ððâ1fi=Afiâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯ä»¥åç° {ðð}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶ççº¿æ§éæ¨åéåï¼ï¼è¯æç¥ï¼

æä»¬å¯ä»¥ç´æ¥æ´åæ±åº ð0â¦ð2ðâ1f0â¦f2nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¶åç¨åé¢æå°çåæ³æ±åº {ðð}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼ï¼åè°ç¨ [å¸¸ç³»æ°é½æ¬¡çº¿æ§éæ¨](../poly/linear-recurrence/) å³å¯ï¼

å¦æè¦æ±çåéæ¯ ððfm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç®æ³çå¤æåº¦æ¯ ð(ð3 +ðlogâ¡ðlogâ¡ð)O(n3+nlogâ¡nlogâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦æ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªåªæ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéé¶é¡¹çç¨çç©éµï¼åå¤æåº¦å¯ä»¥éä¸º ð(ðð +ðlogâ¡ðlogâ¡ð)O(nk+nlogâ¡nlogâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½ç±äºç®æ³è³å°éè¦ ð(ðð)O(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´é¢å¤çï¼å æ­¤å¨ååä¸å¤§çæ åµä¸ä¹å¯ä»¥ä½¿ç¨ ð(ð2logâ¡ð)O(n2logâ¡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççº¿æ§éæ¨ç®æ³ï¼å¤æåº¦åæ ·æ¯å¯ä»¥æ¥åçï¼

#### æ±ç©éµçæå°å¤é¡¹å¼

æ¹éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å¤é¡¹å¼æ¯æ¬¡æ°æå°çå¹¶ä¸æ»¡è¶³ ð(ð´) =0f(A)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤é¡¹å¼ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å®é ä¸æå°å¤é¡¹å¼å°±æ¯ {ð´ð}{Ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°éæ¨å¼ï¼æä»¥ç´æ¥è°ç¨ BerlekampâMassey ç®æ³å°±å¯ä»¥äºï¼å¦æ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶æ¹éµï¼åæ¾ç¶æå°å¤é¡¹å¼çæ¬¡æ°ä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¶é¢å¨äºæ±åº ð´ðAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸ºå¦æç´æ¥æ¯æ¬¡åç©éµä¹æ³çè¯å¤æåº¦ä¼è¾¾å° ð(ð4)O(n4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½èèå°æ±ç©éµåçæç­éæ¨å¼æ¶å®é ä¸æ±çæ¯ {ððð´ðð}{uTAiv}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæç­éæ¨å¼ï¼å æ­¤æä»¬åªè¦æ±åº ð´ððAiv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±è¡äºï¼

åè®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéé¶é¡¹ï¼åå¤æåº¦ä¸º ð(ðð +ð2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### æ±ç¨çç©éµè¡åå¼

å¦æè½æ±åºæ¹éµ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¹å¾å¤é¡¹å¼ï¼åå¸¸æ°é¡¹ä¹ä¸ ( â1)ð(â1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯è¡åå¼ï¼ä½æ¯æå°å¤é¡¹å¼ä¸ä¸å®å°±æ¯ç¹å¾å¤é¡¹å¼ï¼

å®é ä¸å¦ææ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ä¸ä¸ªéæºå¯¹è§éµ ðµB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ð´ðµAB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å¤é¡¹å¼æè³å° 1 â2ð2âðð1â2n2ânp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¦çå°±æ¯ç¹å¾å¤é¡¹å¼ï¼æååé¤æ det ðµdetB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±è¡äºï¼

è®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¶æ¹éµï¼ä¸æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéé¶é¡¹ï¼åå¤æåº¦ä¸º ð(ðð +ð2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### æ±ç¨çç©éµçç§©

è®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª ð ÃðnÃm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç©éµï¼é¦å éæºä¸ä¸ª ð ÃðnÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹è§éµ ðP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ä¸ª ð ÃðmÃm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯¹è§éµ ðQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), ç¶åè®¡ç® ðð´ðð´ððQAPATQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°å¤é¡¹å¼å³å¯ï¼

å®é ä¸ä¸ç¨è°ç¨ç©éµä¹æ³ï¼å ä¸ºæ±æå°å¤é¡¹å¼æ¶è¦ç¨ ðð´ðð´ððQAPATQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸ä¸ªåéï¼æä»¥æä»¬ä¾æ¬¡æè¿å ä¸ªç©éµä¹å°åééå°±è¡äºï¼ç­æ¡å°±æ¯æå°å¤é¡¹å¼é¤æææ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­åå©ä¸çæ¬¡æ°ï¼

è®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéé¶é¡¹ï¼ä¸ ð â¤ðnâ¤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¤æåº¦ä¸º ð(ðð +ð2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### è§£ç¨çæ¹ç¨ç»

**é®é¢** ï¼å·²ç¥ ð´ð± =ðAx=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), å ¶ä¸­ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ª ð ÃðnÃn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **æ»¡ç§©** ç¨çç©éµï¼ðb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð±x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ 1 Ãð1Ãn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çååéï¼ð´,ðA,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å·²ç¥ï¼éè¦å¨ä½äº ððnÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤æåº¦å è§£åº ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**åæ³** ï¼æ¾ç¶ ð± =ð´â1ðx=Aâ1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦ææä»¬è½æ±åº {ð´ðð}{Aib}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(ð â¥0iâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) çæå°éæ¨å¼ {ð0â¦ððâ1}{r0â¦rmâ1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(ð â¤ðmâ¤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)), é£ä¹å°±æç»è®º

ð´â1ð = â1ððâ1âðâ2ð=0ð´ððððâ2âðAâ1b=â1rmâ1âi=0mâ2Aibrmâ2âi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ï¼è¯æç¥ï¼

å ä¸º ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç¨çç©éµï¼ç´æ¥æå®ä¹éæ¨åº ðâ¦ð´2ðâ1ðbâ¦A2nâ1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³å¯ï¼

åæ ·å°ï¼è®¾ ð´A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéé¶é¡¹ï¼åå¤æåº¦ä¸º ð(ðð +ð2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text vector < int > solve_sparse_equations ( const vector < tuple < int , int , int >> & A , const vector < int > & b ) { int n = ( int ) b . size (); // 0-based vector < vector < int >> f ({ b }); for ( int i = 1 ; i < 2 * n ; i ++ ) { vector < int > v ( n ); auto & u = f . back (); for ( auto [ x , y , z ] : A ) // [x, y, value] v [ x ] = ( v [ x ] \+ ( long long ) u [ y ] * z ) % p ; f . push_back ( v ); } vector < int > w ( n ); mt19937 gen ; for ( auto & x : w ) x = uniform_int_distribution < int > ( 1 , p \- 1 )( gen ); vector < int > a ( 2 * n ); for ( int i = 0 ; i < 2 * n ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) a [ i ] = ( a [ i ] \+ ( long long ) f [ i ][ j ] * w [ j ]) % p ; auto c = berlekamp_massey ( a ); int m = ( int ) c . size (); vector < int > ans ( n ); for ( int i = 0 ; i < m \- 1 ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) ans [ j ] = ( ans [ j ] \+ ( long long ) c [ m \- 2 \- i ] * f [ i ][ j ]) % p ; int inv = power ( p \- c [ m \- 1 ], p \- 2 ); for ( int i = 0 ; i < n ; i ++ ) ans [ i ] = ( long long ) ans [ i ] * inv % p ; return ans ; } ```   
---|---  
  
### ä¾é¢

  1. [LibreOJ #163. é«æ¯æ¶å  2](https://loj.ac/p/163)
  2. [ICPC2021 å°å Gym103443E. Composition with Large Red Plane, Yellow, Black, Gray, and Blue](https://codeforces.com/gym/103443/problem/E)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/berlekamp-massey.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/berlekamp-massey.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [antileaf](https://github.com/antileaf), [Enter-tainer](https://github.com/Enter-tainer), [AntiLeaf](https://github.com/AntiLeaf), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
