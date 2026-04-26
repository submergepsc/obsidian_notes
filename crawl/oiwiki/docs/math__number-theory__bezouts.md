# è£´èå®ç & ä¸æ¬¡ä¸å®æ¹ç¨ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/bezouts/

# è£´èå®ç & ä¸æ¬¡ä¸å®æ¹ç¨

è£´èå®çæ­ç¤ºäºæå¤§å ¬çº¦æ°ä¸æ´æ°çº¿æ§ç»åä¹é´çæ·±å»èç³»ï¼æ¯æ°è®ºä¸­æåºç¡ä¹æéè¦çç»è®ºä¹ä¸ï¼åºäºæ­¤ï¼æ¬æè¿ä¸æ­¥è®¨è®ºäºä¸æ¬¡ä¸å®æ¹ç¨çæ±è§£æ¹æ³ï¼

## è£´èå®ç

**è£´èå®ç** ï¼BÃ©zout's lemmaï¼ï¼ä¹è¯ä½è´ç¥å®çï¼æç§°ä½è´ç¥ç­å¼ï¼BÃ©zout's identityï¼ï¼ç»åºäºä¸ä¸ªæ´æ°è½å¤è¡¨ç¤ºä¸ºä¸¤ä¸ªæ´æ°çæ´ç³»æ°çº¿æ§ç»åçå åå¿ è¦æ¡ä»¶ï¼

è£´èå®ç

è®¾ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸å ¨ä¸ºé¶çæ´æ°ï¼é£ä¹ï¼å¯¹äºä»»ææ´æ° ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ gcd(ð,ð) â£ðð¥ +ðð¦gcd(a,b)â£ax+by![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼èä¸ï¼å­å¨æ´æ° ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ðð¥ +ðð¦ =gcd(ð,ð)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

è¯æ

è®° ð =gcd(ð,ð)d=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ð â£ð,ðdâ£a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼å­å¨æ´æ° ð¢,ð£u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð =ðð¢,Â ð =ðð£a=du,Â b=dv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼å æ­¤ï¼æ»æ

ðð¥+ðð¦=ð(ð¢ð¥+ð£ð¦).ax+by=d(ux+vy).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±è¯´æ ð â£ðð¥ +ðð¦dâ£ax+by![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åè¿æ¥ï¼éè¦è¯´æå­å¨ ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ç­å¼æç«ï¼å¦æ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¦¨è®¾ ð =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å®ä»¬çæå¤§å ¬çº¦æ°ä¸º ð =ðd=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¾ç¶æ (ð¥,ð¦) =(1,0)(x,y)=(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ç­å¼æç«ï¼æ¥ä¸æ¥ï¼èè ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ä¸ºé¶çæ å½¢ï¼ç±äº gcd(ð,ð) =gcd( âð,ð) =gcd(ð, âð)gcd(a,b)=gcd(âa,b)=gcd(a,âb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ä¸å¦¨è®¾ ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ­£æ°ï¼

èèè¾è½¬ç¸é¤æ³çè¿ç¨ï¼æ

ð=ð1ð+ð1,0â¤ð1<ð,ð=ð2ð1+ð2,0â¤ð2<ð1,ð1=ð3ð2+ð3,0â¤ð3<ð2,â¯ððâ3=ððâ1ððâ2+ððâ1,0â¤ððâ1<ððâ2,ððâ2=ððððâ1+ðð,0â¤ðð<ððâ1,ððâ1=ðð+1ðð.a=q1b+r1,0â¤r1<b,b=q2r1+r2,0â¤r2<r1,r1=q3r2+r3,0â¤r3<r2,â¯rnâ3=qnâ1rnâ2+rnâ1,0â¤rnâ1<rnâ2,rnâ2=qnrnâ1+rn,0â¤rn<rnâ1,rnâ1=qn+1rn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äºæå¤§å ¬çº¦æ°æ¯ ðd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æåä¸æ­¥è¾è½¬ç¸é¤æ¶ï¼ä¸å®æ ðð =ðrn=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ï¼åæ°ç¬¬äºä¸ªç­å¼å¯ä»¥åä½

ð=ðð=ððâ2âððððâ1.d=rn=rnâ2âqnrnâ1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»åæ°ç¬¬ä¸ä¸ªç­å¼ä¸­è§£åº

ððâ1=ððâ3âððâ1ððâ2rnâ1=rnâ3âqnâ1rnâ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åä»£å ¥ä¸å¼ï¼å°±å¯ä»¥æ¶å» ððâ1rnâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ð=ððâ2âðð(ððâ3âððâ1ððâ2)=(1+ððððâ1)ððâ2âððððâ3.d=rnâ2âqn(rnâ3âqnâ1rnâ2)=(1+qnqnâ1)rnâ2âqnrnâ3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±»ä¼¼å°ï¼å¯ä»¥éæ­¥å°æ¶å»ææ ððâ2,ððâ3,â¯,ð2,ð1rnâ2,rnâ3,â¯,r2,r1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æç»å¾å°

ð=ð¥ð+ð¦ð.d=xa+yb.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å°±è¯æäºå­å¨ ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð¥ +ðð¦ =ðax+by=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼ç±åæåæå¯ç¥ï¼è¿ä¹è¯æäºåå½é¢ï¼

æ­¤å¤ï¼å ³äºå­å¨æ§çè¯ææ¯æé æ§çï¼å®åæ¶ç»åºäºè¯¥ç³»æ°çä¸ç§è®¡ç®æ¹æ³ï¼è¿ä¸è®¡ç®æ¹æ³å°±æ¯ [æ©å±æ¬§å éå¾ç®æ³](../gcd/#æ©å±æ¬§å)ï¼

èèè£´èå®çå¨ gcd(ð,ð) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çç¹æ®æ å½¢ï¼å¯ä»¥å¾å°å¦ä¸æ¨è®ºï¼

æ¨è®º

æ´æ° ð,ða,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å½ä¸ä» å½å­å¨æ´æ° ð¥,ð¦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ ðð¥ +ðð¦ =1ax+by=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

### å¤ä¸ªæ´æ°çæ å½¢

è£´èå®çå¯ä»¥æ¨å¹¿å°å¤ä¸ªæ´æ°çæ å½¢ï¼

å®ç

è®¾ ð1,ð2,â¯,ðða1,a2,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸å ¨ä¸ºé¶çæ´æ°ï¼é£ä¹ï¼å¯¹äºä»»ææ´æ° ð¥1,ð¥2,â¯,ð¥ðx1,x2,â¯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ gcd(ð1,ð2,â¯,ðð) â£ð1ð¥1 +ð2ð¥2 +â¯ +ððð¥ðgcd(a1,a2,â¯,an)â£a1x1+a2x2+â¯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼èä¸ï¼å­å¨æ´æ° ð¥1,ð¥2,â¯,ð¥ðx1,x2,â¯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ gcd(ð1,ð2,â¯,ðð) =ð1ð¥1 +ð2ð¥2 +â¯ +ððð¥ðgcd(a1,a2,â¯,an)=a1x1+a2x2+â¯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

è¯æ

å©ç¨ gcd(ð1,ð2,â¯,ðð) =gcd(gcd(ð1,ð2,â¯,ððâ1),ðð)gcd(a1,a2,â¯,an)=gcd(gcd(a1,a2,â¯,anâ1),an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸ç¹ï¼å¯¹ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡å½çº³å³å¯ï¼

### ä¾é¢

[Codeforces 510 D. Fox And Jumping](https://codeforces.com/problemset/problem/510/D)

ç»åº ð â¤300nâ¤300![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼ å¡çï¼åå«æ ððli![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ððci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ä¸æ¡æ éé¿ççº¸å¸¦ä¸ï¼ä½ å¯ä»¥éæ©è± ððci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé±æ¥è´­ä¹°å¡ç ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»æ­¤ä»¥åå¯ä»¥åå·¦æåå³è·³ ððli![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªåä½ä»»ææ¬¡ï¼é®ä½ è³å°è±å¤å°å é±æè½å¤è·³å°çº¸å¸¦ä¸å ¨é¨ä½ç½®ï¼è¥ä¸è¡ï¼è¾åº â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è§£ç­

åæè¯¥é®é¢ï¼åç°æ³è¦è·³å°æ¯ä¸ä¸ªæ ¼å­ä¸ï¼å¿ é¡»ä½¿å¾æéæ° ðð1,â¯,ðððli1,â¯,lik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éè¿æ°æ¬¡ç¸å æç¸åå¾åºçç»å¯¹å¼ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼å­å¨æ´æ° ð¥1,â¯,ð¥ðx1,â¯,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ðð1ð¥1 +â¯ +ðððð¥ð =1li1x1+â¯+likxk=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±å¤ä¸ªæ´æ°çè£´èå®çï¼è¿ç¸å½äºä»æ°ç» ð1,â¯,ððl1,â¯,ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­éæ©è¥å¹²ä¸ªæ°ï¼æ»¡è¶³å®ä»¬çæå¤§å ¬çº¦æ°ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¶è¦æ±ä»£ä»·åæå°ï¼

**è§£æ³ 1** ï¼å°æå°ä»£ä»·åçä½æ¯æç­è·¯å¾é®é¢ï¼å¯ä»¥ç¨ Dijkstra ç®æ³æ±è§£ï¼å¾çé¡¶ç¹å¤å­å¨äºå½åçæå¤§å ¬çº¦æ°çåå¼ï¼å¾çèµ·ç¹æ¯ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¦å°è¾¾çç®æ ç¹æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯èµ°ä¸æ­¥ï¼å°±ä»å½åé¡¶ç¹ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºåï¼æ²¿çé¿åº¦ä¸º ððci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¾¹èµ°å°é¡¶ç¹ gcd(ð¥,ðð)gcd(x,li)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿ä¸ç®æ³çæ¶é´å¤æåº¦ä¸º ð(ð2logâ¡ð)O(n2logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**è§£æ³ 2** ï¼ä»æ°ç» ð1,â¯,ððl1,â¯,ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éæ©è¥å¹²ä¸ªæ°ï¼æ»¡è¶³å®ä»¬çæå¤§å ¬å æ°ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ä»£ä»·åæå°ï¼ç±æ­¤å¯ä»¥æ³å° 0-1 èå é®é¢ï¼

è®¾ ðð,ðfi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºèèå ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°ä¸æå¤§å ¬å æ°ä¸º ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°ä»£ä»·ï¼åæè½¬ç§»æ¹ç¨ï¼

ðð,ð=mingcd(ð,ðð)=ðððâ1,ð+ðð.fi,j=mingcd(k,li)=jfiâ1,k+ci.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

DP åæç»çæ»ä»£ä»·å³ä¸º ðð,1fn,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¦åä¸è¬ç 0-1 èå é®é¢ï¼å¯ä»¥ç¨æ»å¨æ°ç»ä¼åï¼å»æç¬¬ä¸ç»´ï¼èè¿é 300 ä¸ªæ°å¯ä»¥ç»æçæå¤§å ¬çº¦æ° ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¾ç¨ççï¼å¯ä»¥ç¨åå¸è¡¨å¨å­ï¼

å®é ä¸ï¼è¿éè§£æ³ 1 å»ºåºçå¾ä¾¿æ¯è§£æ³ 2 ä¸­å¨æè§åçç¶æè½¬ç§»å¾ï¼è§£æ³ 2 ç¸å½äºç¨å¨æè§åæ±æåæ ç¯å¾çæç­è·¯ï¼å æ­¤è§£æ³ 1 åè§£æ³ 2 æ¯ç­ä»·çï¼ä½è§£æ³ 2 æ éå¨å­å ¨å¾ï¼åæ¶ DP çæ¶é´å¤æåº¦ä¸º ð(ð +ð)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¸æ¯ Dijkstra ç®æ³æ´ä½ï¼å æ­¤è§£æ³ 2 å¨æ¶é´åç©ºé´ä¸æ´ä¼ï¼

## ä¸æ¬¡ä¸å®æ¹ç¨

**ä¸æ¬¡ä¸å®æ¹ç¨** ï¼linear Diophantine equationï¼æ¯å½¢å¦

ð1ð¥1+ð2ð¥2+â¯+ððð¥ð=ða1x1+a2x2+â¯+anxn=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çä¸å®æ¹ç¨ï¼å ¶ä¸­ï¼ð1,ð2,â¯,ðða1,a2,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ´æ°ï¼æ¬èçç®æ æ¯å¯»æ¾å®çå ¨ä½æ´æ°è§£ï¼

### ä¸¤ä¸ªåéçæ å½¢

é¦å èèäºå ä¸æ¬¡ä¸å®æ¹ç¨ï¼

ð1ð¥1+ð2ð¥2=ð.a1x1+a2x2=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è£´èå®çæåºï¼è¯¥æ¹ç¨æè§£ï¼å½ä¸ä» å½

ð=gcd(ð1,ð2)â£ð.d=gcd(a1,a2)â£b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¥ä¸æ¥ï¼åè®¾è¿ä¸æ¡ä»¶æç«ï¼å©ç¨æ©å±æ¬§å éå¾ç®æ³å¯ä»¥æ±åºæ¹ç¨ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç»æ´æ°è§£ (ð¥â1,ð¥â2)(x1â,x2â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±æ­¤ï¼å¯ä»¥å¾å°åæ¹ç¨çä¸ç»ç¹è§£

(ð¥â1,ð¥â2)=(ððð¥â1,ððð¥â2).(x1â,x2â)=(bdx1â,bdx2â).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¦å¾å°å ¨é¨è§£ï¼å¯ä»¥èèå°åæ¹ç¨ä¸æç­å¼ ð1ð¥â1 +ð2ð¥â2 =ða1x1â+a2x2â=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸åï¼å°±æ

ð1(ð¥1âð¥â1)+ð2(ð¥2âð¥â2)=0.a1(x1âx1â)+a2(x2âx2â)=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ä¸ä¸ªå ³äº (ð¥1 âð¥â1,ð¥2 âð¥â2)(x1âx1â,x2âx2â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé½æ¬¡ä¸æ¬¡ä¸å®æ¹ç¨ï¼å®æéè§£

(ð¥1âð¥â1,ð¥2âð¥â2)=(ð¡ð2ð,âð¡ð1ð).(ð¡âð)(x1âx1â,x2âx2â)=(ta2d,âta1d).(tâZ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼åæ¹ç¨çéè§£å°±æ¯

(ð¥1,ð¥2)=(ð¥â1+ð¡ð2ð,ð¥â2âð¡ð1ð).(ð¡âð)(x1,x2)=(x1â+ta2d,x2ââta1d).(tâZ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ç´çº¿ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ä¸ç³»åç­é´éåå¸çæ´ç¹ï¼

### å¤ä¸ªåéçæ å½¢

è§£å³äºäºå çæ å½¢ï¼å¤å çæ å½¢ä¹å°±å®¹æè§£å³äºï¼å¯¹äº ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸æ¬¡ä¸å®æ¹ç¨

ð1ð¥1+ð2ð¥2+â¯+ððð¥ð=ð,(ð>3)a1x1+a2x2+â¯+anxn=b,(n>3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±è£´èå®çå¯ç¥ï¼æ¹ç¨æè§£å½ä¸ä» å½

gcd(ð1,ð2,â¯,ðð)â£ð.gcd(a1,a2,â¯,an)â£b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åäºå çæ å½¢ç±»ä¼¼ï¼å¤å ä¸æ¬¡ä¸å®æ¹ç¨çéè§£åæ ·å¯ä»¥åä½

(ð¥â1,ð¥â2,â¯,ð¥âð)+ðâ1âð=1ð¡ð(ð¥(ð)1,ð¥(ð)2,â¯,ð¥(ð)ð)(x1â,x2â,â¯,xnâ)+âk=1nâ1tk(x1(k),x2(k),â¯,xn(k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½¢å¼ï¼å ¶ä¸­ï¼ð¥âxâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¸ä¸ªç¹è§£ï¼ð¥(ð)x(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºç¸åºçé½æ¬¡æ¹ç¨ç (ð â1)(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªè§£ï¼

è¦æ±åºéè§£çå ·ä½å½¢å¼ï¼å¯ä»¥éè¿å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ¹ç¨è½¬åä¸º (ð â1)(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æ¹ç¨æ¥å®æï¼ä¸å¦¨è®¾ ð1 =gcd(ð1,ð2)d1=gcd(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ ¹æ®è£´èå®çï¼ð1ð¥1 +ð2ð¥2a1x1+a2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå ¨ä½æ°ä¸º ð1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææåæ°ï¼å æ­¤ï¼å¯ä»¥é¦å æ±è§£ (ð â1)(nâ1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸æ¬¡ä¸å®æ¹ç¨ï¼

ð1ð¦1+ð3ð¥3+ð4ð¥4+â¯+ððð¥ð=ð.d1y1+a3x3+a4x4+â¯+anxn=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾å¾å°çå®çéè§£ä¸º

ð¦1=ð¦â1+ðâ1âð=2ð¡ðð¦(ð)1,ð¥ð=ð¥âð+ðâ1âð=2ð¡ðð¥(ð)ð,ð=3,â¯,ð.y1=y1â+âk=2nâ1tky1(k),xi=xiâ+âk=2nâ1tkxi(k),i=3,â¯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ð1ð¥1 +ð2ð¥2 =ð1a1x1+a2x2=d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ç»ç¹è§£ä¸º (ð¥â1,ð¥â2)(x1â,x2â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼æ ¹æ®åä¸èçè®¨è®ºå¯ç¥ï¼å ³äº ð¥1,ð¥2x1,x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºå ä¸æ¬¡ä¸å®æ¹ç¨ ð1ð¥1 +ð2ð¥2 =ð1ð¦1a1x1+a2x2=d1y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè§£å°±æ¯

ð¥1=ð¥â1ð¦1+ð¡1ð2ð1,Â ð¥2=ð¥â2ð¦1âð¡1ð1ð1.x1=x1ây1+t1a2d1,Â x2=x2ây1ât1a1d1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥ ð¦1y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼å°±å¾å°åæ¹ç¨çéè§£

ð¥1=ð¥â1ð¦â1+ð¡1ð2ð1+ðâ1âð=2ð¡ðð¥â1ð¦(ð)1,ð¥2=ð¥â2ð¦â1âð¡1ð1ð1+ðâ1âð=2ð¡ðð¥â2ð¦(ð)1,ð¥ð=ð¥âð+ðâ1âð=2ð¡ðð¥(ð)ð,ð=3,â¯,ð.x1=x1ây1â+t1a2d1+âk=2nâ1tkx1ây1(k),x2=x2ây1âât1a1d1+âk=2nâ1tkx2ây1(k),xi=xiâ+âk=2nâ1tkxi(k),i=3,â¯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Frobenius ç¡¬å¸é®é¢

è£´èå®çç»åºäºä¸ä¸ªæ´æ°å¯ä»¥ç±è¥å¹²ä¸ªæ´æ°çº¿æ§è¡¨åºçå åå¿ è¦æ¡ä»¶ï¼ä¸æ­¤ç´§å¯ç¸å ³çæ¯ **Frobenius ç¡¬å¸é®é¢** ï¼Frobenius coin problemï¼ï¼

  * å¦æç¡¬å¸å ±æ ð1,ð2,â¯,ðða1,a2,â¯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­è¥å¹²ç§æ´æ°é¢å¼ï¼ä¸ gcd(ð1,ð2,â¯,ðð) =1gcd(a1,a2,â¯,an)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ä¸è½å¤ç±è¿äºç¡¬å¸ç»æçæå¤§æ´æ°æ¯å¤å°ï¼

åæ ·æ¯å¨èå¯æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»ä¹æ¶åå¯ä»¥è¡¨ç¤ºä¸º ð1ð¥1 +ð2ð¥2 +â¯ +ððð¥ða1x1+a2x2+â¯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå½¢å¼ï¼è£´èå®çä¸­ ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥æ¯ä»»ææ´æ°ï¼è Frobenius ç¡¬å¸é®é¢ä¸­ ð¥ðxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åªè½æ¯èªç¶æ°ï¼

åªæä¸ç§ç¡¬å¸çæ å½¢æ¯å¹³å¡çï¼å ä¸ºåªè½æ ð1 =1a1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ææèªç¶æ°é½å¯ä»¥ç±å®è¡¨ç¤ºï¼è ð >2n>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢åå¤ªè¿å¤æï¼æä»¥ï¼æ¬èä» è®¨è®º ð =2n=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ å½¢ï¼

### Sylvester å®ç

å¨ 1882 å¹´ï¼Sylvester å®å ¨è§£å³äº ð =2n=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ç Frobenius ç¡¬å¸é®é¢ï¼

å®çï¼Sylvesterï¼

å¯¹äºäºç´ çæ­£æ´æ° ð1,ð2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸è½å¤åä½ ð1ð¥1 +ð2ð¥2Â (ð¥1,ð¥2 âð)a1x1+a2x2Â (x1,x2âN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå¤§æ´æ°æ¯ ð¶ =ð1ð2 âð1 âð2C=a1a2âa1âa2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ï¼å¯¹äºææ ð âðkâZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æä¸åªæä¸ä¸ªå¯ä»¥åä½è¯¥å½¢å¼ï¼

ä¸ºè¡¨è¿°æ¹ä¾¿ï¼ç§°å¯ä»¥åä½ ð1ð¥1 +ð2ð¥2Â (ð¥1,ð¥2 âð)a1x1+a2x2Â (x1,x2âN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å½¢å¼çæ´æ°ä¸º **å¯è¡¨ç¤ºç** ï¼

è¯æä¸

ç±äº ð1,ð2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼å¯¹äºä»»ææ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¹ç¨ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æè§£ï¼ä¸éè§£ä¸º

(ð¥1,ð¥2)=(ð¥â1+ð¡ð2,ð¥â2âð¡ð1).(ð¡âð)(x1,x2)=(x1â+ta2,x2ââta1).(tâZ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º ð¥â2x2â![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¸¦ä½é¤æ³å¾å°çåï¼é£ä¹ï¼ä½æ° ð¥2 =ð¥â2 âð¡ð1x2=x2ââta1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1 â1a1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼èå¯æ­¤æ¶å¾å°çä¸ç»è§£ (ð¥1,ð¥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º ð¥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®è½å¤åå°çæå°éè´æ´æ°å¼ï¼æä»¥ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è¡¨ç¤ºå½ä¸ä» å½ ð¥1 â¥0x1â¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

**ç¬¬ä¸æ­¥** ï¼è¯æå¤§äº ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°é½æ¯å¯è¡¨ç¤ºçï¼

å½ ð >ð¶k>C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼æ

ð1ð¥1=ðâð2ð¥2>ð¶âð2(ð1â1)=âð1.a1x1=kâa2x2>Câa2(a1â1)=âa1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼ð¥1 > â1x1>â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¹å°±æ¯è¯´ï¼ð¥1 â¥0x1â¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿è¯´æï¼(ð¥1,ð¥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ç»èªç¶æ°è§£ï¼æ­¤æ¶ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åä½ææ±å½¢å¼ï¼

**ç¬¬äºæ­¥** ï¼è¯æ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡¨ç¤ºï¼è¿èï¼ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æå¤§çä¸å¯è¡¨ç¤ºçæ´æ°ï¼ä¸ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¹¶éé½å¯è¡¨ç¤ºçï¼

åè¯æ³ï¼åè®¾ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¡¨ç¤ºï¼å³å­å¨ ð¥1,ð¥2 âðx1,x2âN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð1ð¥1 +ð2ð¥2 =ð¶a1x1+a2x2=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼ä»£å ¥ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨è¾¾å¼ï¼å¯ç¥

ð1ð2=ð1(ð¥1+1)+ð2(ð¥2+1).a1a2=a1(x1+1)+a2(x2+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼ð2 â£(ð¥1 +1)a2â£(x1+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð1 â£(ð¥2 +1)a1â£(x2+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå ä¸º ð¥1 +1,ð¥2 +1x1+1,x2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ­£æ°ï¼æä»¥ï¼æ

ð1ð2â¥ð1ð2+ð2ð1=2ð1ð2.a1a2â¥a1a2+a2a1=2a1a2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çç¾ï¼è¿å°±è¯´æ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡¨ç¤ºï¼ç»åç¬¬ä¸æ­¥ï¼å®ä¹å°±æ¯ä¸å¯è¡¨ç¤ºçæå¤§æ´æ°ï¼

å¦æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥è¡¨ç¤ºï¼é£ä¹ï¼å° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨ç¤ºä¸­çç³»æ°ç¸å å°±å¾å° ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè¡¨ç¤ºä¸­çç³»æ°ï¼è¿ä¸ ð¶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡¨ç¤ºçç¾ï¼æ è ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è³å¤åªæä¸ä¸ªå¯ä»¥è¡¨ç¤ºï¼

**ç¬¬ä¸æ­¥** ï¼è¯æå¦æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡¨ç¤ºï¼é£ä¹ ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æ¯å¯è¡¨ç¤ºçï¼

è®¾ (ð¥1,ð¥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åææè®¾çæ¹ç¨ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ´æ°è§£ï¼é£ä¹ï¼åæå·²ç»è¯´æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯è¡¨ç¤ºï¼å°±ç­ä»·äº ð¥1 <0x1<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼æ

ð¶âð=ð1ð2âð1âð2âð1ð¥1âð2ð¥2=ð1(â1âð¥1)+ð2(ð1â1âð¥2).Câk=a1a2âa1âa2âa1x1âa2x2=a1(â1âx1)+a2(a1â1âx2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼â1 âð¥1â1âx1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð1 â1 âð¥2a1â1âx2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯éè´æ´æ°ï¼æä»¥ï¼ð¶ âðCâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¡¨ç¤ºï¼

è¯æäº

æ­¤å¤ä» è¯æ ð¶ =ð1ð2 âð1 âð2C=a1a2âa1âa2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æå¤§çä¸å¯è¡¨ç¤ºçèªç¶æ°ï¼å ¶ä½é¨åçè¯æç±»ä¼¼è¯æä¸ï¼

èèæ¨¡ ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä¹ä¸ï¼æ¯ä¸ªå©ä½ç³»ä¸­æå°çå¯è¡¨ç¤ºçèªç¶æ°ï¼å ä¸ºåä¸ä¸ªå©ä½ç³»ä¸­çä¸åèªç¶æ°å¯ä»¥éè¿å åè¥å¹²ä¸ª ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç¸è½¬åï¼æä»¥ï¼å¨è®¨è®ºæå°å¯è¡¨ç¤ºæ°æ¶ï¼åªéè¦èèå å ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¯è½æ§å°±å¯ä»¥äºï¼ç±äº ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºç´ ï¼æä»¥ï¼æ¯ä¸ªå©ä½ç³»ä¸­æå°çå¯è¡¨ç¤ºçèªç¶æ°æ°å¥½å°±æ¯ ð1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°

0,Â ð1,Â 2ð1,Â â¯,Â (ð2â1)ð1.0,Â a1,Â 2a1,Â â¯,Â (a2â1)a1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼æå¤§çä¸å¯è¡¨ç¤ºæ°ä¸º

max0â¤ð<ð2ðð1âð2=(ð2â1)ð1âð2=ð¶.max0â¤i<a2ia1âa2=(a2â1)a1âa2=C.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### å ä½æä¹

å°æ¹ç¨ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½æ¯ä¸æ¡ç´çº¿ï¼é£ä¹ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯è¡¨ç¤ºï¼å½ä¸ä» å½è¿æ¡ç´çº¿å¨ç¬¬ä¸è±¡éï¼å æ¬åæ è½´ï¼å éè¿ä¸ä¸ªæ´ç¹ï¼å½ ð <ððk<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼è¿æ¡ç´çº¿å¨ç¬¬ä¸è±¡éè³å¤åªè½éè¿ä¸ä¸ªæ´ç¹ï¼å æ­¤ï¼å¯¹äº 0 â¤ð <ðð0â¤k<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ´æ° ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥è¡¨ç¤ºï¼å½ä¸ä» å½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ç¬¬ä¸è±¡ééè¿æ°å¥½ä¸ä¸ªæ´ç¹ï¼

å æ­¤ï¼å°äºç­äº ð <ððk<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å¯ä»¥è¡¨ç¤ºçèªç¶æ°çæ°éï¼æ°å¥½ç­äºç¬¬ä¸è±¡éå ç´çº¿ ð1ð¥1 +ð2ð¥2 =ða1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸çæ´ç¹ä¸ªæ°ï¼å å«è¾¹çä¸çç¹ï¼ï¼è¿ä¸æ°éå°±ç­äº

âð/ð1ââð=0âðâðð1ð2â.âi=0âk/a1ââkâia1a2â.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æ¯ç»å ¸çç´çº¿ä¸æ´ç¹é®é¢ï¼å¯ä»¥ç¨ [ç±»æ¬§å éå¾ç®æ³](../euclidean/#ç±»æ¬§å) å¨ ð(logâ¡min{ð1,ð2,ð})O(logâ¡min{a1,a2,k})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´æ±è§£ï¼

### ä¹ é¢

  * [Luogu P3951 NOIP2017 æé«ç» å°å¯ççæ/èæ¡¥æ¯ 2013 ç ä¹°ä¸å°çæ°ç®](https://www.luogu.com.cn/problem/P3951)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/bezouts.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/bezouts.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Xeonacid](https://github.com/Xeonacid), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [greyqz](https://github.com/greyqz), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [ylxmf2005](https://github.com/ylxmf2005), [buggg-hfc](https://github.com/buggg-hfc), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [monkeysui](https://github.com/monkeysui), [ShizuhaAki](https://github.com/ShizuhaAki), [StudyingFather](https://github.com/StudyingFather), [Sunlight-zero](https://github.com/Sunlight-zero), [TianKong-y](https://github.com/TianKong-y)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
