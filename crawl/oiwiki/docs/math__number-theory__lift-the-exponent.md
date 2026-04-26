# åå¹å¼ç - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/lift-the-exponent/

# åå¹å¼ç

## å å®¹

åå¹ï¼Lift the Exponentï¼LTEï¼å¼çæ¯åç­æ°è®ºä¸­æ¯è¾å¸¸ç¨çä¸ä¸ªå®çï¼

å®ä¹ ðð(ð)Î½p(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ ååè§£ä¸­ç´ å å­ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡ï¼å³ ðð(ð)Î½p(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³ ððð(ð) â£ðpÎ½p(n)â£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ððð(ð)+1 â¤ðpÎ½p(n)+1â¤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

ç±äºåå¹å¼çå å®¹è¾é¿ï¼æä»¬å°å ¶åä¸ºä¸é¨åä»ç»ï¼

ä»¥ä¸å å®¹è®¾ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºç´ æ°ï¼ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ»¡è¶³ ð â¤ð¥pâ¤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â¤ð¦pâ¤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ­£æ´æ°ï¼

### ç¬¬ä¸é¨å

å¯¹ææçç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ»¡è¶³ (ð,ð) =1(n,p)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  1. è¥ ð â£ð¥ âð¦pâ£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åï¼

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)Î½p(xnâyn)=Î½p(xây)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. è¥ ð â£ð¥ +ð¦pâ£x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯¹å¥æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼

ðð(ð¥ð+ð¦ð)=ðð(ð¥+ð¦)Î½p(xn+yn)=Î½p(x+y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æ

è¥ ð â£ð¥ âð¦pâ£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åä¸é¾åç° ð â£ð¥ âð¦ âº ð¥ â¡ð¦(modð)pâ£xâyâºxâ¡y(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¾ç¶æï¼

ðâ1âð=0ð¥ðð¦ðâ1âðâ¡ðð¥ðâ1â¢0(modð)âi=0nâ1xiynâ1âiâ¡nxnâ1â¢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿èç± ð¥ð âð¦ð =(ð¥ âð¦)âðâ1ð=0ð¥ðð¦ðâ1âðxnâyn=(xây)âi=0nâ1xiynâ1âi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥å½é¢å¾è¯ï¼

å¯¹ ð â£ð¥ +ð¦pâ£x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµè¯ææ¹æ³ç±»ä¼¼ï¼

### ç¬¬äºé¨å

è¥ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¥ç´ æ°ï¼

  1. è¥ ð â£ð¥ âð¦pâ£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åï¼

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)+ðð(ð)Î½p(xnâyn)=Î½p(xây)+Î½p(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. è¥ ð â£ð¥ +ð¦pâ£x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå¯¹å¥æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼

ðð(ð¥ð+ð¦ð)=ðð(ð¥+ð¦)+ðð(ð)Î½p(xn+yn)=Î½p(x+y)+Î½p(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æ

è¥ ð â£ð¥ âð¦pâ£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¤ ð¦ =ð¥ +ððy=x+kp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬åªéè¯æ ð â£ðpâ£n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµï¼

  * è¥ ð =ðn=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç±äºé¡¹å¼å®çï¼

ðâ1âð=0ð¥ðâ1âðð¦ð=ðâ1âð=0ð¥ðâ1âððâð=0(ðð)ð¥ð(ðð)ðâðâ¡ðð¥ðâ1(modð2)âi=0pâ1xpâ1âiyi=âi=0pâ1xpâ1âiâj=0i(ij)xj(kp)iâjâ¡pxpâ1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»è

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)+1Î½p(xnâyn)=Î½p(xây)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * è¥ ð =ððn=pa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åç±æ°å­¦å½çº³æ³å¯å¾

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)+ðÎ½p(xnâyn)=Î½p(xây)+a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤å½é¢å¾è¯ï¼

å¯¹ ð â£ð¥ +ð¦pâ£x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ åµè¯ææ¹æ³ç±»ä¼¼ï¼

### ç¬¬ä¸é¨å

è¥ ð =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð â£ð¥ âð¦pâ£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  1. å¯¹å¥æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼ä¸ç¬¬ä¸é¨åç 1 ç¸åï¼ï¼

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)Î½p(xnâyn)=Î½p(xây)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. å¯¹å¶æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æï¼

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)+ðð(ð¥+ð¦)+ðð(ð)â1Î½p(xnâyn)=Î½p(xây)+Î½p(x+y)+Î½p(n)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦å¤å¯¹ä¸è¿°ç ð¥,ð¦,ðx,y,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬æï¼

è¥ 4 â£ð¥ âð¦4â£xây![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åï¼

  * ð2(ð¥ +ð¦) =1Î½2(x+y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ð2(ð¥ðâð¦ð) =ð2(ð¥ âð¦) +ð2(ð)Î½2(xnâyn)=Î½2(xây)+Î½2(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æ

æä»¬åªéè¯æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°çæ åµï¼ç±äºæ­¤æ¶ ð â¤(ð2)pâ¤(p2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ æä»¬ä¸è½ç¨ç¬¬äºé¨åçæ¹æ³è¯æï¼

ä»¤ ð =2ððn=2ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ ð =ðð(ð)a=Î½p(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼2 â¤ð2â¤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»è

ðð(ð¥ðâð¦ð)=ðð(ð¥2ðâð¦2ð)=ðð((ð¥âð¦)(ð¥+ð¦)ðâ1âð=1(ð¥2ð+ð¦2ð))Î½p(xnâyn)=Î½p(x2aây2a)=Î½p((xây)(x+y)âi=1aâ1(x2i+y2i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ³¨æå° 2 â£ð¥ âð¦ â¹ 4 â£ð¥2 âð¦22â£xâyâ¹4â£x2ây2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»è (âð â¥1),Â Â ð¥2ð +ð¦2ð â¡2(mod4)(âiâ¥1),Â Â x2i+y2iâ¡2(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿èä¸å¼å¯åä¸ºï¼

ðð(ð¥ðâð¦ð)=ðð(ð¥âð¦)+ðð(ð¥+ð¦)+ðð(ð)â1Î½p(xnâyn)=Î½p(xây)+Î½p(x+y)+Î½p(n)â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤å½é¢å¾è¯ï¼

## åèèµæ

  1. [Lifting-the-exponent lemma - Wikipedia](https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/lift-the-exponent.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/lift-the-exponent.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Xeonacid](https://github.com/Xeonacid)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
