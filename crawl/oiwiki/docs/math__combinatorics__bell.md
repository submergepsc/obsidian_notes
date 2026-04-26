# è´å°æ° - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/bell/

# è´å°æ°

è´å°æ° ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»¥åéå Â·å¦æ®å°Â·è´å°å½åï¼æ¯ç»åæ°å­¦ä¸­çä¸ç»æ´æ°æ°åï¼å¼é¦æ¯ï¼[OEIS A000110](https://oeis.org/A000110)ï¼ï¼

ðµ0=1,ðµ1=1,ðµ2=2,ðµ3=5,ðµ4=15,ðµ5=52,ðµ6=203,â¦B0=1,B1=1,B2=2,B3=5,B4=15,B5=52,B6=203,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åºæ°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåçååæ¹æ³çæ°ç®ï¼éå ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ä¸ªååæ¯å®ä¹ä¸º ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸¤ä¸¤ä¸ç¸äº¤çéç©ºå­éçæï¼å®ä»¬çå¹¶æ¯ ðS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¾å¦ ðµ3 =5B3=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸º 3 ä¸ªå ç´ çéå ð,ð,ða,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ 5 ç§ä¸åçååæ¹æ³ï¼

{{ð},{ð},{ð}}{{ð},{ð,ð}}{{ð},{ð,ð}}{{ð},{ð,ð}}{{ð,ð,ð}}{{a},{b},{c}}{{a},{b,c}}{{b},{a,c}}{{c},{a,b}}{{a,b,c}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ðµ0B0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ 1 å ä¸ºç©ºéæ­£å¥½æ 1 ç§ååæ¹æ³ï¼

## éæ¨å ¬å¼

è´å°æ°éåéæ¨å ¬å¼ï¼

ðµð+1=ðâð=0(ðð)ðµðBn+1=âk=0n(nk)Bk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æï¼

ðµð+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å«æ ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ éåçååä¸ªæ°ï¼è®¾ ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¸º {ð1,ð2,ð3,â¦,ðð}{b1,b2,b3,â¦,bn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðµð+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåä¸º {ð1,ð2,ð3,â¦,ðð,ðð+1}{b1,b2,b3,â¦,bn,bn+1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å¯ä»¥è®¤ä¸º ðµð+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¢æ·»äºä¸ä¸ª ðð+1bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) èäº§ççï¼èèå ç´ ðð+1bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * åå¦å®è¢«åç¬åå°ä¸ç±»ï¼é£ä¹è¿å©ä¸ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼è¿ç§æ åµä¸ååæ°ä¸º (ðð)ðµð(nn)Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7);

  * åå¦å®åæ 1 ä¸ªå ç´ åå°ä¸ç±»ï¼é£ä¹è¿å©ä¸ ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼è¿ç§æ åµä¸ååæ°ä¸º (ððâ1)ðµðâ1(nnâ1)Bnâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * åå¦å®åæ 2 ä¸ªå ç´ åå°ä¸ç±»ï¼é£ä¹è¿å©ä¸ ð â2nâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼è¿ç§æ åµä¸ååæ°ä¸º (ððâ2)ðµðâ2(nnâ2)Bnâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * â¦â¦

ä»¥æ­¤ç±»æ¨å°±å¾å°äºä¸é¢çå ¬å¼ï¼

æ¯ä¸ªè´å°æ°é½æ¯ç¸åºç [ç¬¬äºç±»æ¯ç¹ææ°](../stirling/#ç¬¬äºç±»æ¯ç¹ææ°stirling-number) çåï¼ å ä¸ºç¬¬äºç±»æ¯ç¹ææ°æ¯æåºæ°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåååä¸ºæ­£å¥½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªéç©ºéçæ¹æ³æ°ç®ï¼

ðµð=ðâð=0{ðð}Bn=âk=0n{nk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## è´å°ä¸è§å½¢

ç¨ä»¥ä¸æ¹æ³æé ä¸ä¸ªä¸è§ç©éµï¼å½¢å¼ç±»ä¼¼æ¨è¾ä¸è§å½¢ï¼ï¼

  * ð0,0 =1a0,0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å¯¹äº ð â¥1nâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡é¦é¡¹ç­äºä¸ä¸è¡çæ«é¡¹ï¼å³ ðð,0 =ððâ1,ðâ1an,0=anâ1,nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * å¯¹äº ð,ð â¥1m,nâ¥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¬¬ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡ç¬¬ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ç­äºå®å·¦è¾¹åå·¦ä¸è§ä¸¤ä¸ªæ°ä¹åï¼å³ ðð,ð =ðð,ðâ1 +ððâ1,ðâ1an,m=an,mâ1+anâ1,mâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

é¨åç»æå¦ä¸ï¼

11223557101515202737525267871141512032032553224095236748771122355710151520273752526787114151203203255322409523674877![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¯è¡çé¦é¡¹æ¯è´å°æ°ï¼å¯ä»¥å©ç¨è¿ä¸ªä¸è§å½¢æ¥éæ¨æ±åºè´å°æ°ï¼

åèå®ç°

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text constexpr int MAXN = 2000 \+ 5 ; int bell [ MAXN ][ MAXN ]; void f ( int n ) { bell [ 0 ][ 0 ] = 1 ; for ( int i = 1 ; i <= n ; i ++ ) { bell [ i ][ 0 ] = bell [ i \- 1 ][ i \- 1 ]; for ( int j = 1 ; j <= i ; j ++ ) bell [ i ][ j ] = bell [ i \- 1 ][ j \- 1 ] \+ bell [ i ][ j \- 1 ]; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text MAXN = 2000 \+ 5 bell = [[ 0 for i in range ( MAXN \+ 1 )] for j in range ( MAXN \+ 1 )] def f ( n ): bell [ 0 ][ 0 ] = 1 for i in range ( 1 , n \+ 1 ): bell [ i ][ 0 ] = bell [ i \- 1 ][ i \- 1 ] for j in range ( 1 , i \+ 1 ): bell [ i ][ j ] = bell [ i \- 1 ][ j \- 1 ] \+ bell [ i ][ j \- 1 ] ```   
---|---  
  
## ææ°çæå½æ°

èèè´å°æ°çææ°çæå½æ°åå ¶å¯¼å½æ°ï¼

Ëðµ(ð¥)=+ââð=0ðµðð!ð¥ð=1++ââð=0ðµð+1(ð+1)!ð¥ð+1Ëðµâ²(ð¥)=+ââð=0ðµð+1ð!ð¥ðB^(x)=ân=0+âBnn!xn=1+ân=0+âBn+1(n+1)!xn+1B^â²(x)=ân=0+âBn+1n!xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ ¹æ®è´å°æ°çéæ¨å ¬å¼å¯ä»¥å¾å°ï¼

ðµð+1ð!=ðâð=01(ðâð)!ðµðð!Bn+1n!=âk=0n1(nâk)!Bkk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸ä¸ªå·ç§¯çå¼å­ï¼å æ­¤æï¼

Ëðµâ²(ð¥)=eð¥Ëðµ(ð¥)B^â²(x)=exB^(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸ä¸ªå¾®åæ¹ç¨ï¼è§£å¾ï¼

Ëðµ(ð¥)=expâ¡(eð¥+ð¶)B^(x)=expâ¡(ex+C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æåå½ ð¥ =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ Ëðµ(ð¥) =1B^(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸¦å ¥åè§£å¾ ð¶ = â1C=â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å°è´å°æ°ææ°çæå½æ°çå°é­å½¢å¼ï¼

Ëðµ(ð¥)=expâ¡(eð¥â1)B^(x)=expâ¡(exâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é¢å¤çåº eð¥ â1exâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ååä¸æ¬¡ [å¤é¡¹å¼ exp](../../poly/elementary-func/#å¤é¡¹å¼å¯¹æ°å½æ°--ææ°å½æ°) å³å¯å¾åºè´å°æ°å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ï¼æ¶é´å¤æåº¦ç¶é¢å¨å¤é¡¹å¼ expï¼å¯åå° ð(ðlogâ¡ð)O(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦ï¼

## åèæç®

<https://en.wikipedia.org/wiki/Bell_number>

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/bell.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/bell.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [ksyx](https://github.com/ksyx), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [LDlornd](https://github.com/LDlornd), [Menci](https://github.com/Menci), [Running-Turtle1](https://github.com/Running-Turtle1), [ShaoChenHeng](https://github.com/ShaoChenHeng), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [untitledunrevised](https://github.com/untitledunrevised), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
