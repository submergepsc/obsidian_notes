# çå©åé·å·ç§¯ - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/dirichlet/

# çå©å é·å·ç§¯

æ¬æä»ç» Dirichlet å·ç§¯å Dirichlet çæå½æ°ï¼

## Dirichlet å·ç§¯

æ°è®ºå½æ° ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð(ð)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **Dirichlet å·ç§¯** ï¼Dirichlet convolutionï¼ï¼è®°ä½ ð âðfâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä¹ä¸ºæ°è®ºå½æ°

(ðâð)(ð)=âðâ£ðð(ð)ð(ðð)=âðâ=ðð(ð)ð(â).(fâg)(n)=âkâ£nf(k)g(nk)=âkâ=nf(k)g(â).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Dirichlet å·ç§¯æ¯æ°è®ºå½æ°çéè¦è¿ç®ï¼æ°è®ºå½æ°çè®¸å¤æ§è´¨é½æ¯éè¿è¿ä¸ªè¿ç®ææåºæ¥çï¼

ä¾å­

  1. åä½å½æ° ðÎµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯è«æ¯ä¹æ¯å½æ° ðÎ¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¸¸æ°å½æ° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Dirichlet å·ç§¯ï¼

ð=ðâ1âºð(ð)=âðâ£ðð(ð).Îµ=Î¼â1âºÎµ(n)=âdâ£nÎ¼(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. é¤æ°ä¸ªæ°å½æ° ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸¸æ°å½æ° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå®èªèº«ç Dirichlet å·ç§¯ï¼

ð=1â1âºð(ð)=âðâ£ð1.Ï=1â1âºÏ(n)=âdâ£n1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. é¤æ°åå½æ° ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æç­å½æ° idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¸¸æ°å½æ° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Dirichlet å·ç§¯ï¼

ð=idâ1âºð(ð)=âðâ£ðð.Ï=idâ1âºÏ(n)=âdâ£nd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. æ¬§æå½æ° ðÏ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æç­å½æ° idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè«æ¯ä¹æ¯å½æ° ðÎ¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Dirichlet å·ç§¯ï¼

ð=idâðâºð(ð)=âðâ£ððâ ð(ðð).Ï=idâÎ¼âºÏ(n)=âdâ£ndâ Î¼(nd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

[è«æ¯ä¹æ¯åæ¼](../mobius/) å°±æ¯å©ç¨ ð =ð â1Îµ=Î¼â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹æ°è®ºå½æ°æç­å¼è¿è¡åå½¢ï¼

### æ§è´¨

Dirichlet å·ç§¯å ·æä¸ç³»åä»£æ°æ§è´¨ï¼

å®ç

è®¾ ð,ð,âf,g,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯æ°è®ºå½æ°ï¼é£ä¹ï¼æï¼

  1. **äº¤æ¢å¾** ï¼ð âð =ð âðfâg=gâf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. **ç»åå¾** ï¼(ð âð) ââ =ð â(ð ââ)(fâg)âh=fâ(gâh)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  3. **åé å¾** ï¼(ð +ð) ââ =ð ââ +ð ââ(f+g)âh=fâh+gâh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  4. **åä½å ** ï¼ð âð =ð âð =ðfâÎµ=Îµâf=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ð(ð) =[ð =1]Îµ(n)=[n=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å·ç§¯åä½å ï¼[ â ][â ]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Iverson æ¬å·ï¼
  5. **éå ** ï¼å½ä¸ä» å½ ð(1) â 0f(1)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å­å¨ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð âð =ð âð =ðfâg=gâf=Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç **Dirichlet éå ** ï¼Dirichlet inverseï¼ï¼å¯ä»¥è®°ä½ ðâ1fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èä¸ï¼éå  ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ»¡è¶³éæ¨å ¬å¼

ð(ð)=ð(ð)ââðâ=ð,Â ðâ 1ð(ð)ð(â)ð(1).g(n)=Îµ(n)ââkâ=n,Â kâ 1f(k)g(â)f(1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¯æ

ä¸ºéªè¯äº¤æ¢å¾ï¼ç´æ¥è®¡ç®å¯ç¥

(ðâð)(ð)=âðâ=ðð(ð)ð(â)=(ðâð)(ð).(fâg)(n)=âkâ=nf(k)g(â)=(gâf)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ºéªè¯ç»åå¾ï¼ç´æ¥è®¡ç®å¯ç¥

((ðâð)ââ)(ð)=âðâð=ðð(ð)ð(â)â(ð)=(ðâ(ðââ))(ð).((fâg)âh)(n)=âkâm=nf(k)g(â)h(m)=(fâ(gâh))(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ºéªè¯åé å¾ï¼ç´æ¥è®¡ç®å¯ç¥

((ð+ð)ââ)(ð)=âðâ=ð(ð(ð)+ð(ð))â(â)=âðâ=ðð(ð)â(â)+âðâ=ðð(ð)â(â)=(ðââ+ðââ)(ð).((f+g)âh)(n)=âkâ=n(f(k)+g(k))h(â)=âkâ=nf(k)h(â)+âkâ=ng(k)h(â)=(fâh+gâh)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ºéªè¯ ð(ð)Îµ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯åä½å ï¼ç´æ¥è®¡ç®å¯ç¥

(ðâð)(ð)=âðâ=ðð(ð)ð(â)=ð(ð).(fâÎµ)(n)=âkâ=nf(k)Îµ(â)=f(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç¬¬äºä¸ªç­å·æ¯å ä¸º ð(â)Îµ(â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä» å¨ â =1â=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å³ ð =ðk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶åå¾éé¶å¼ï¼

æåï¼éè¦è¯æ ðâ1fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼å½ä¸ä» å½ ð(1) â 0f(1)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹äºä»»æ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾å­å¨ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð âð =ðfâg=Îµ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æå³ç

(ðâð)(ð)=âðâ=ðð(ð)ð(â)=ð(ð).(fâg)(n)=âkâ=nf(k)g(â)=Îµ(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿å®é ä¸ç»åºäºä¸ç³»åå ³äº ð(ð)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¼çæ¹ç¨ç»ï¼ä»ä¸­å¯ä»¥ç´æ¥æ±åº ð(ð)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç¹å«å°ï¼å½ ð =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç­å¼åä¸º ð(1)ð(1) =1f(1)g(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¥ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼è³å°è¦æ± ð(1) â 0f(1)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èåªè¦ ð(1) â 0f(1)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥ç´æ¥è§£åº

ð(ð)=ð(ð)ââðâ=ð,Â ðâ 1ð(ð)ð(â)ð(1).g(n)=Îµ(n)ââkâ=n,Â kâ 1f(k)g(â)f(1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®å¯ä»¥ç¨äºéå½è®¡ç® ð(ð)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåå¼ï¼å æ­¤ï¼éå  ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼å½ä¸ä» å½ ð(1) â 0f(1)â 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç¨æ½è±¡ä»£æ°çè¯­è¨è¯´ï¼è¿äºä»£æ°æ§è´¨è¯´æï¼å ¨ä½æ°è®ºå½æ°å¨ï¼éç¹ï¼å æ³è¿ç®å Dirichlet å·ç§¯è¿ç®ä¸ææ [äº¤æ¢ç¯](../../algebra/basic/#ç¯)ï¼ä¸å®çå ¨ä½å¯éå å°±æ¯é£äºå¨ ð =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤åéé¶å¼çå½æ°ï¼è¿ä¸ªç¯ç§°ä¸º **Dirichlet ç¯** ï¼Dirichlet ringï¼ï¼

ç§¯æ§å½æ°æ¯ä¸ç±»ç¹æ®çæ°è®ºå½æ°ï¼å®å¯¹äº Dirichlet å·ç§¯å Dirichlet éé½æ¯å°é­çï¼

å®ç

è®¾ ð,ðf,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼é£ä¹ï¼ð âðfâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹æ¯ç§¯æ§å½æ°ï¼èä¸ï¼éå  ðâ1fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®å­å¨ï¼å®ä¹æ¯ç§¯æ§å½æ°ï¼

è¯æ

å¯¹äºç¬¬ä¸ç¹ï¼è®¾ â =ð âðh=fâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç´æ¥éªè¯å¯ç¥ï¼å¯¹äº ð1 âð2n1ân2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ

â(ð1)â(ð2)=(âð1â1=ð1ð(ð1)ð(â1))(âð2â2=ð2ð(ð2)ð(â2))=âð1â1=ð1,Â ð2â2=ð2ð(ð1)ð(ð2)ð(â1)ð(â2)=âðâ=ð1ð2ð(ð)ð(â)=â(ð1ð2).h(n1)h(n2)=(âk1â1=n1f(k1)g(â1))(âk2â2=n2f(k2)g(â2))=âk1â1=n1,Â k2â2=n2f(k1)f(k2)g(â1)g(â2)=âkâ=n1n2f(k)g(â)=h(n1n2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ç¬¬ä¸ä¸ªç­å·æ¹åæ±åé¡ºåºçé»è¾æ¯ï¼å½ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éå ð1ð2n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå æ°æ¶ï¼ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å å­å¯ä»¥æ ¹æ®å®æ¯ ð1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ¯ ð2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ å å­åä¸ºä¸¤ç±»ï¼å°ä¸¤ç±»ä¸­çç´ å å­ï¼è®¡éå¤ï¼åå«ä¹èµ·æ¥å¾å° ð1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬å°åå«éå ð1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå æ°ï¼åè¿æ¥ï¼æ ¹æ® ð1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå æ° ð1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ»æ¯å¯ä»¥å¾å° ð1ð2n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå æ° ð =ð1ð2k=k1k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äºç¬¬äºç¹ï¼è®¾ ð =ðâ1g=fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èèåºç¨æ°å­¦å½çº³æ³ï¼é¦å ï¼ð(1) =1/ð(1) =1g(1)=1/f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ­¤æ¶ï¼éå çéå½å ¬å¼å¯ä»¥åä½

ð(ð)=ð(ð)ââðâ=ð,Â ðâ 1ð(ð)ð(â).g(n)=Îµ(n)ââkâ=n,Â kâ 1f(k)g(â).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å¯¹äº ð1 âð2n1ân2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ ð1ð2 >1n1n2>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ

ð(ð1ð2)=ââðâ=ð1ð2,Â ðâ 1ð(ð)ð(â)=ââð1â1=ð1,Â ð2â2=ð2,Â ð1ð2â 1ð(ð1)ð(ð2)ð(â1)ð(â2)=ð(1)ð(1)ð(ð1)ð(ð2)ââð1â1=ð1,Â ð2â2=ð2ð(ð1)ð(ð2)ð(â1)ð(â2)=ð(ð1)ð(ð2)â(âð1â1=ð1ð(ð1)ð(â1))(âð2â2=ð2ð(ð2)ð(â2))=ð(ð1)ð(ð2)âð(ð1)ð(ð2)=ð(ð1)ð(ð2).g(n1n2)=ââkâ=n1n2,Â kâ 1f(k)g(â)=ââk1â1=n1,Â k2â2=n2,Â k1k2â 1f(k1)f(k2)g(â1)g(â2)=f(1)f(1)g(n1)g(n2)ââk1â1=n1,Â k2â2=n2f(k1)f(k2)g(â1)g(â2)=g(n1)g(n2)â(âk1â1=n1f(k1)g(â1))(âk2â2=n2f(k2)g(â2))=g(n1)g(n2)âÎµ(n1)Îµ(n2)=g(n1)g(n2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ç¬¬äºä¸ªç­å·ç¨å°äºå½çº³åè®¾ï¼å³å¯¹äº â1â2 <ð1ð2â1â2<n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ â1 ââ2â1ââ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¡ä»¶ ð(â1â2) =ð(â1)ð(â2)g(â1â2)=g(â1)g(â2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼

ç¨æ½è±¡ä»£æ°çè¯­è¨è¯´ï¼å ¨ä½ç§¯æ§å½æ°å¨ Dirichlet å·ç§¯è¿ç®ä¸ææ Dirichlet ç¯ä¹æ³ç¾¤ç [å­ç¾¤](../../algebra/group-theory/#å­ç¾¤)ï¼

æ´ä¸ºç¹æ®çæ¯å®å ¨ç§¯æ§å½æ°ï¼

å®ç

è®¾ ð¼Î±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼ð,ðf,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ°è®ºå½æ°ï¼é£ä¹ï¼æï¼

  1. åé å¾ï¼(ð¼ð) â(ð¼ð) =ð¼ â (ð âð)(Î±f)â(Î±g)=Î±â (fâg)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. éå ï¼(ð¼ð)â1 =ð¼ðâ1(Î±f)â1=Î±fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦ ðâ1fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å­å¨ï¼
  3. ç§¯æ§å½æ° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼å½ä¸ä» å½ ðâ1 =ððfâ1=Î¼f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ï¼ðÎ¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ [è«æ¯ä¹æ¯å½æ°](../mobius/#è«æ¯ä¹æ¯å½æ°)ï¼

è¯æ

å¯¹äºç¬¬ä¸æ¡ï¼ç´æ¥éªè¯å¯ç¥

((ð¼ð)â(ð¼ð))(ð)=âðâ=ð(ð¼ð)(ð)(ð¼ð)(â)=âðâ=ðð¼(ð)ð(ð)ð¼(â)ð(â)=âðâ=ðð¼(ð)ð(ð)ð(â)=ð¼(ð)(ðâð)(ð).((Î±f)â(Î±g))(n)=âkâ=n(Î±f)(k)(Î±g)(â)=âkâ=nÎ±(k)f(k)Î±(â)g(â)=âkâ=nÎ±(n)f(k)g(â)=Î±(n)(fâg)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ç¬¬ä¸ä¸ªç­å·ç¨å°äºå®å ¨ç§¯æ§å½æ°çæ§è´¨ï¼ð¼(ð) =ð¼(ð)ð¼(â)Î±(n)=Î±(k)Î±(â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹ææ ð =ðân=kâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æç«ï¼

å¯¹äºç¬¬äºæ¡ï¼å©ç¨ç¬¬ä¸æ¡å°±æ

(ð¼ð)â(ð¼ðâ1)=ð¼(ðâðâ1)=ð¼ð=ð.(Î±f)â(Î±fâ1)=Î±(fâfâ1)=Î±Îµ=Îµ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼æåä¸ä¸ªç­å·åªå©ç¨äº ð¼(1) =1Î±(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±éå å®ä¹ï¼(ð¼ð)â1 =ð¼ðâ1(Î±f)â1=Î±fâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯¹äºç¬¬ä¸æ¡ï¼å©ç¨ç¬¬äºæ¡å 1â1 =ð1â1=Î¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ç¥ï¼å¦æ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼é£ä¹

ðâ1=(1ð)â1=1â1â ð=ðð.fâ1=(1f)â1=1â1â f=Î¼f.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸¸æ°å½æ°ï¼åè¿æ¥ï¼å¦æ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ä¸ ðâ1 =ððfâ1=Î¼f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹åªéè¦è¯æå¯¹äºææç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é½æ ð(ðð) =ð(ð)ðf(pe)=f(p)e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æç«ï¼å°±è½è¯æ ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼ä¸ºæ­¤ï¼å¯¹ ð âð+eâN+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åºç¨æ°å­¦å½çº³æ³ï¼å½çº³èµ·ç¹ ð =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤å½é¢æ¾ç¶æç«ï¼å¯¹äºä»»æ ð >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºç¨éå éæ¨å ¬å¼ï¼é½æ

ðâ1(ðð)=âðâð=1ð(ðð)ðâ1(ððâð)=âðâð=1ð(ðð)ð(ððâð)ð(ððâð)=âð(ðð)ð(1)ð(1)âð(ððâ1)ð(ð)ð(ð)=âð(ðð)+ð(ð)ð.fâ1(pe)=ââi=1ef(pi)fâ1(peâi)=ââi=1ef(pi)Î¼(peâi)f(peâi)=âf(pe)f(1)Î¼(1)âf(peâ1)Î¼(p)f(p)=âf(pe)+f(p)e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼æåä¸ä¸ªç­å·ç¨å°äºå½çº³åè®¾ ð(ððâ1) =ð(ð)ðâ1f(peâ1)=f(p)eâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åºç¨ ðâ1 =ððfâ1=Î¼f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±å¾å°

ðâ1(ðð)=ð(ðð)ð(ðð)=0.fâ1(pe)=Î¼(pe)f(pe)=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥åå¼ï¼å°±å¾å°

ð(ðð)=ð(ð)ð.f(pe)=f(p)e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä»¥ï¼å½çº³æ­¥éª¤æç«ï¼åå½é¢å¾è¯ï¼

ç¨æ½è±¡ä»£æ°çè¯­è¨è¯´ï¼å¦æ ð¼Î±![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼æ å° ð â¦ð¼ðfâ¦Î±f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ Dirichlet ç¯ç [èªåæ](../../algebra/ring-theory/#çæ³)ï¼

## Dirichlet çæå½æ°

ä¸ Dirichlet å·ç§¯ç´§å¯ç¸å ³çæ¯ Dirichlet çæå½æ°ï¼

æ°è®ºå½æ° ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ââä¹å°±æ¯æ°å {ð(ð)}{f(n)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ââå¯¹åºç **Dirichlet çæå½æ°** ï¼Dirichlet series generating functionï¼DGFï¼å®ä¹ä¸ºå½¢å¼ Dirichlet çº§æ°ï¼formal Dirichlet seriesï¼ï¼

ð¹(ð )=ââð=1ð(ð)ðð .F(s)=ân=1âf(n)ns.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çº§æ°ä¸­ç ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å½¢å¼åå ï¼å¸¸è§ç Dirichlet çæå½æ°ä¸­ï¼ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å¾å¯ä»¥çä½æ¯å¤åéï¼è¿èè®¨è®º Dirichlet çº§æ°çè§£ææ§è´¨ï¼ä½è¿è¶ åºäºç®æ³ç«èµçèå´ï¼

Dirichlet çæå½æ°çä¹ç§¯å¯¹åºçç¸åºçæ°è®ºå½æ°ç Dirichlet å·ç§¯ï¼

å®ç

å¯¹äºæ°è®ºå½æ° ð,ðf,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå ¶ Dirichlet çæå½æ° ð¹,ðºF,G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®ä»¬ç Dirichlet å·ç§¯ ð âðfâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççæå½æ°ç­äº ð¹ â ðºFâ G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¯æ

ç´æ¥éªè¯ï¼

ð¹(ð )ðº(ð )=(ââð=1ð(ð)ðð )(âââ=1ð(â)âð )=ââð=1âââ=1ð(ð)ð(â)(ðâ)ð =ââð=1âðâ=ðð(ð)ð(â)ðð =ââð=1(ðâð)(ð)ðð .F(s)G(s)=(âk=1âf(k)ks)(ââ=1âg(â)âs)=âk=1âââ=1âf(k)g(â)(kâ)s=ân=1ââkâ=nf(k)g(â)ns=ân=1â(fâg)(n)ns.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å©ç¨ Dirichlet å·ç§¯å Dirichlet çæå½æ°ä¹ç§¯ä¹é´çå¯¹åºå ³ç³»ï¼å¯ä»¥ä» Dirichlet çæå½æ°çè§åº¦çè§£ Dirichlet å·ç§¯çæ§è´¨ï¼ç±äºå½¢å¼ Dirichlet çº§æ°çä¹æ³è¿ç®æ»¡è¶³äº¤æ¢å¾ãç»åå¾ãå¯¹å æ³çåé å¾ï¼æ°è®ºå½æ°ç Dirichlet å·ç§¯è¿ç®æ»¡è¶³åæ ·çä»£æ°æ§è´¨ï¼

### Euler ä¹ç§¯

ç§¯æ§å½æ°çç¹æ®æ§åæ ·åæ å¨ Dirichlet çæå½æ°ä¸ï¼ç±äºæ´æ°æ [å¯ä¸åè§£å®ç](../basic/#ç®æ¯åºæ¬å®ç)ï¼ç§¯æ§å½æ° ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ççæå½æ° ð¹(ð )F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯åæå¦ä¸å½¢å¼ï¼

ð¹(ð )=ââð=1ð(ð)ðð =ââð=1âðâðð(ðð)ððð =âðâðââð=0ð(ðð)ððð =âðâð(1+ð(ð)ðð +ð(ð2)ð2ð +ð(ð3)ð3ð +â¯).F(s)=ân=1âf(n)ns=ân=1ââpâPf(pe)pes=âpâPâe=0âf(pe)pes=âpâP(1+f(p)ps+f(p2)p2s+f(p3)p3s+â¯).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿æå³çï¼ð¹(ð )F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯ä»¥åè§£ä¸ºè¥å¹² ð¹ð(ð )Fp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¹ç§¯ï¼ä¸æ¯ä¸ª ð¹ð(ð )Fp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¯¹åºçæ°è®ºå½æ°é½åªå¨ ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡å¤å¯è½åéé¶å¼ï¼è¿ä¸æ ç©·ä¹ç§¯ä¹ç§°ä¸º **Euler ä¹ç§¯** ï¼Euler productï¼ï¼å¦æ ð¹(ð )F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðº(ð )G(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½è½åè§£æç±»ä¼¼çå½¢å¼ï¼é£ä¹å®ä»¬çä¹ç§¯åæ ·å¦æ­¤ï¼å°è¿ä¸è§å¯å¯¹åºå°æ°è®ºå½æ°ä¸ï¼å°±æ¯ç§¯æ§å½æ°ç Dirichlet å·ç§¯ä»ç¶æ¯ç§¯æ§å½æ°ï¼

è¿ä¸æ­¥å°ï¼å¦æ ð(ð)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿æ¯å®å ¨ç§¯æ§å½æ°ï¼é£ä¹ ð(ðð) =ð(ð)ðf(pe)=f(p)e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸å¼å¯ä»¥ç»§ç»­ç®åï¼

ð¹(ð )=âðâðââð=0ð(ð)ðððð =âðâð(1âð(ð)ðð )â1.F(s)=âpâPâe=0âf(p)epes=âpâP(1âf(p)ps)â1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸ç§¯æ§å½æ°ä¸åï¼å®å ¨ç§¯æ§å½æ°ç Dirichlet çæå½æ°çå½¢å¼å¨ä¹æ³è¿ç®ä¸å¹¶ä¸å ·æå°é­æ§ï¼å æ­¤ï¼å®å ¨ç§¯æ§å½æ°ç Dirichlet å·ç§¯å Dirichlet éé½æªå¿ æ¯å®å ¨ç§¯æ§å½æ°ï¼ä½ä¸å®æ¯ç§¯æ§å½æ°ï¼

ä¾å­

  1. åä½å½æ° ð(ð)Îµ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯å ³äºä¸å®å  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¸¸å¼å½æ°

ð¸(ð )=ââð=1ð(ð)ðð =1.E(s)=ân=1âÎµ(n)ns=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. å¸¸æ°å½æ° 1(ð)1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯ Riemann å½æ°

ð¼(ð )=ââð=11ðð =âðâð11âðâð =ð(ð ).I(s)=ân=1â1ns=âpâP11âpâs=Î¶(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. è«æ¯ä¹æ¯å½æ° ð(ð)Î¼(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å¸¸æ°å½æ°ç Dirichlet éï¼å®ç Dirichlet çæå½æ°æ¯ ð(ð )Î¶(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåæ°ï¼

ð(ð )=ââð=1ð(ð)ðð =âðâð(1âðâð )=1ð(ð ).M(s)=ân=1âÎ¼(n)ns=âpâP(1âpâs)=1Î¶(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. å¹å½æ° idðâ¡(ð) =ððidkâ¡(n)=nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°ï¼ç¹å«å°ï¼å½ ð =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å®å°±æ¯å¸¸æ°å½æ°ï¼å½ ð =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼å®å°±æ¯æç­å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯

ð¼ð(ð )=ââð=1ðððð =âðâð11âððâð =ð(ð âð).Ik(s)=ân=1ânkns=âpâP11âpkâs=Î¶(sâk).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  5. æ¬§æå½æ° ð(ð)Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯

Î¦(ð )=âðâð(1+ðâ1ðð +ð(ðâ1)ð2ð +ð2(ðâ1)ð3ð +â¯)=âðâð(11âð1âð â1ðð 11âð1âð )=âðâð1âðâð 1âð1âð =ð(ð â1)ð(ð ).Î¦(s)=âpâP(1+pâ1ps+p(pâ1)p2s+p2(pâ1)p3s+â¯)=âpâP(11âp1âsâ1ps11âp1âs)=âpâP1âpâs1âp1âs=Î¶(sâ1)Î¶(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»åå¹å½æ°ç Dirichlet å½æ°è¡¨è¾¾å¼ï¼å°±å¾å° id =ð â1id=Ïâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  6. çº¦æ°å½æ° ðð(ð) =âðâ£ðððÏk(n)=âdâ£ndk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯

Î£ð(ð )=âðâð(1+1+ðððð +1+ðð+ð2ðð2ð +1+ðð+ð2ð+ð3ðð3ð +â¯)=âðâð11âðð((1âðð)+1âð2ððð +1âð3ðð2ð +1âð4ðð3ð+â¯)=âðâð11âðð(11âðâð âðð1âððâð )=âðâð1(1âðâð )(1âððâð )=ð(ð âð)ð(ð ).Î£k(s)=âpâP(1+1+pkps+1+pk+p2kp2s+1+pk+p2k+p3kp3s+â¯)=âpâP11âpk((1âpk)+1âp2kps+1âp3kp2s+1âp4kp3k+â¯)=âpâP11âpk(11âpâsâpk1âpkâs)=âpâP1(1âpâs)(1âpkâs)=Î¶(sâk)Î¶(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç»åå¹å½æ°ç Dirichlet è¡¨è¾¾å¼ï¼å°±å¾å° ðð =idð â1Ïk=idkâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿æ­£æ¯ ððÏk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå®ä¹å¼ï¼

  7. æ å¹³æ¹å å­æ°çæç¤ºå½æ° ð¢(ð) =|ð(ð)|u(n)=|Î¼(n)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°æ¯

ð(ð )=âðâð(1+ðâð )=âðâð1âðâ2ð 1âðâð =ð(ð )ð(2ð ).U(s)=âpâP(1+pâs)=âpâP1âpâ2s1âpâs=Î¶(s)Î¶(2s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### åºç¨

Dirichlet çæå½æ°å¯ä»¥ç¨äºå°ç§¯æ§å½æ°è¡¨ç¤ºä¸º Dirichlet å·ç§¯ï¼

ä¾å¦å¨ææç­çè¿ç¨ä¸­ï¼è¦è®¡ç®ç§¯æ§å½æ° ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåç¼åï¼éè¦æ¾å°å¦ä¸ä¸ªç§¯æ§å½æ° ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½¿å¾ ð âðfâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½å¯ä»¥å¿«éæ±åç¼åï¼å¯ä»¥å©ç¨ Dirichlet çæå½æ°æ¨å¯¼è¿ä¸è¿ç¨ï¼

ä»¥ææç­ä¸èçä¾é¢ [Luogu P3768 ç®åçæ°å­¦é¢](../du/#é®é¢äº) ä¸ºä¾ï¼éè¦å¯¹ ð(ð) =ð2ð(ð)f(n)=n2Ï(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æé æ»¡è¶³ä¸è¿°æ¡ä»¶çæ°è®ºå½æ° ð(ð)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç±äº ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼å®ç Dirichlet çæå½æ°ä¸º

ð¹(ð )=âðâð(1+ââð=1ð3ðâ1(ðâ1)ððð )=âðâð1âð2âð 1âð3âð =ð(ð â3)ð(ð â2).F(s)=âpâP(1+âk=1âp3kâ1(pâ1)pks)=âpâP1âp2âs1âp3âs=Î¶(sâ3)Î¶(sâ2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹æ¯å¹å½æ°ç Dirichlet çæå½æ°å¯ç¥ï¼åªè¦å ð =id2g=id2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æ ð âð =id3fâg=id3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¤è é½æ¯å¯ä»¥å¿«éè®¡ç®åç¼åçï¼

## Dirichlet å·ç§¯çè®¡ç®

æ¬èè®¨è®º Dirichlet å·ç§¯çè®¡ç®é®é¢ï¼å³ç»å®åºå {ð(ð)}ðð=1{f(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å {ð(ð)}ðð=1{g(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ±è§£ Dirichlet å·ç§¯ â =ð âðh=fâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çåè¥å¹²é¡¹ {â(ð)}ðð=1{h(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çé®é¢ï¼æ ¹æ®æ¶åå°çå½æ°æ§è´¨ï¼ç®æ³çå¤æåº¦ä¹ç¥æä¸åï¼

### ä¸è¬æ å½¢

å¦æ ð,ð,âf,g,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ²¡æç¹æ®æ§è´¨ï¼é£ä¹ Dirichlet å·ç§¯çè®¡ç®åªè½å©ç¨å ¶å®ä¹ï¼

â(ð)=âðâ=ðð(ð)ð(â).h(n)=âkâ=nf(k)g(â).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æä¸¾ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°è´¡ç® ð(ð)ð(â)f(k)g(â)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç´¯å å° â(ðâ)h(kâ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å³å¯ï¼æä¸¾å¤æåº¦ä¸º

ð(ðâð=1ðð)=ð(ðlogâ¡ð).O(âk=1nnk)=O(nlogâ¡n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text // Compute the Dirichlet convolution h = f * g. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( n \+ 1 ); for ( int k = 1 ; k <= n ; ++ k ) { for ( int d = 1 ; k * d <= n ; ++ d ) { h [ k * d ] += f [ k ] * g [ d ]; } } return h ; } ```   
---|---  
  
### ä¸ç§¯æ§å½æ°å·ç§¯çæ å½¢

å¦æ ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°ï¼é£ä¹å¯ä»¥å©ç¨ Euler ä¹ç§¯å é Dirichlet å·ç§¯çè®¡ç®ï¼è®¡ç® âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¸å½äºè®¡ç®å®ç Dirichlet çæå½æ° ð»H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­åé¡¹çç³»æ°ï¼ç±äº

ð»(ð )=ð¹(ð )ðº(ð )=ð¹(ð )âðâððºð(ð ).H(s)=F(s)G(s)=F(s)âpâPGp(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å ¶ä¸­ï¼ðºð(ð )Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ ðº(ð )G(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç Euler ä¹ç§¯åè§£ä¸­çå å¼ï¼å®åªå å« ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¹æ¬¡å¤çç³»æ°ï¼

ðºð(ð )=âððâ¤ðð(ðð)ððð =1+ð(ð)ðð +ð(ð2)ð2ð +â¯.Gp(s)=âpkâ¤nf(pk)pks=1+f(p)ps+f(p2)p2s+â¯.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹ï¼ä» ð¹(ð )F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼éåææä¸è¶ è¿ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç´ æ° ðp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ðºð(ð )Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) éä¸ä¹ä¸å»ï¼åæ ·å¯ä»¥å¾å°æç»ç»æ ð»(ð )H(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ðºð(ð )Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸å»æ¶ï¼ç´æ¥åºç¨ä¸è¬æ å½¢ä¸­çæ´åæä¸¾ç®æ³å³å¯ï¼æ»æä¸¾æ¬¡æ°

âðâð,Â ðâ¤ðââð=1âðððââ¤âðâð,Â ðâ¤ðððâ1â¤âðâð,Â ðâ¤ð2ððâð(ðlogâ¡logâ¡ð).âpâP,Â pâ¤nâk=1âânpkââ¤âpâP,Â pâ¤nnpâ1â¤âpâP,Â pâ¤n2npâO(nlogâ¡logâ¡n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æåä¸æ­¥å¤æåº¦çä¼°è®¡ä¸ [Eratosthenes ç­æ³](../sieve/#åæææ¯ç¹å°¼ç­æ³) å¤æåº¦çè¯æä¸è´ï¼æä»¥ï¼æ¬ç®æ³çæ¶é´å¤æåº¦ä¸º ð(ðlogâ¡logâ¡ð)O(nlogâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // Compute the Dirichlet convolution h = f * g. // Assume that g is multiplicative. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( f ); std :: vector < bool > vis ( n \+ 1 ); for ( int i = 2 ; i <= n ; ++ i ) { if ( vis [ i ]) continue ; // Reverse the order for in-place computation. for ( int k = n / i * i ; k ; k -= i ) { vis [ k ] = true ; int d = k ; while ( true ) { d /= i ; h [ k ] += h [ d ] * g [ k / d ]; if ( d % i ) break ; } } } return h ; } ```   
---|---  
  
ç¹å«å°ï¼å½ç§¯æ§å½æ° ðg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯å®å ¨ç§¯æ§å½æ°æå ¶ Dirichlet éæ¶ï¼ä¾å¦å½ ð =1g=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ ð =ðg=Î¼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼é£ä¹ç®æ³å¯ä»¥è¿ä¸æ­¥ç®åï¼æ­¤æ¶ï¼Dirichlet å·ç§¯ â =ð âðh=fâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çè®¡ç®å¯ä»¥éç¨å¸¸æ°æ´å°ç [Dirichlet åç¼å/å·®å](../mobius/#dirichlet-åç¼å) ç®æ³ï¼ä½æ¯ç®æ³æ¶é´å¤æåº¦ä»ä¸º ð(ðlogâ¡logâ¡ð)O(nlogâ¡logâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### ç»æä¸ºç§¯æ§å½æ°çæ å½¢

æåï¼èè âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ç§¯æ§å½æ°çæ å½¢ï¼ç¹å«å°ï¼å½ ð,ðf,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ç§¯æ§å½æ°æ¶ï¼â =ð âðh=fâg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±æ¯ç§¯æ§å½æ°ï¼è¦è®¡ç® âh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªéè¦ç¡®å®å®å¨ç´ æ°å¹å¤çåå¼ï¼å°±å¯ä»¥éè¿ [çº¿æ§ç­](../sieve/#çº¿æ§ç­æ³) å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å è®¡ç®ï¼èå¯¹äºç´ æ°å¹ ððpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çåå¼ â(ðð)h(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç´æ¥æ´åè®¡ç®å³å¯ï¼

â(ðð)=ðâð=0ð(ðð)ð(ððâð).h(pe)=âi=0ef(pi)g(peâi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿äºæ´åè®¡ç®éè¦çæä¸¾æ¬¡æ°ä¸º

âðâð,Â ðâ¤ðâlogðâ¡ðââð=1(ð+1)â¤âðâð,Â ðâ¤âðâlogðâ¡ðâ2+âðâð,Â âð<ðâ¤ð1â¤âð(log2â¡ð)2+ðâð(ð).âpâP,Â pâ¤nâe=1âlogpâ¡nâ(e+1)â¤âpâP,Â pâ¤nâlogpâ¡nâ2+âpâP,Â n<pâ¤n1â¤n(log2â¡n)2+nâO(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å æ­¤ï¼è¿ä¸ç®æ³çæ»æ¶é´å¤æåº¦ä¸º ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

åèå®ç°å¦ä¸ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text // Compute the Dirichlet convolution h = f * g. // Assume that h is multiplicative. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( n \+ 1 ), primes , rem ( n \+ 1 ), lpf ( n \+ 1 ); std :: vector < bool > vis ( n \+ 1 ); h [ 1 ] = 1 ; for ( int x = 2 ; x <= n ; ++ x ) { if ( ! vis [ x ]) { primes . push_back ( x ); rem [ x ] = 1 ; lpf [ x ] = x ; } for ( int p : primes ) { if ( x * p > n ) break ; vis [ x * p ] = true ; rem [ x * p ] = x % p ? x : rem [ x ]; lpf [ x * p ] = p ; if ( x % p == 0 ) break ; } if ( rem [ x ] == 1 ) { // prime powers. for ( int k = x ; k ; k /= lpf [ x ]) { h [ x ] += f [ k ] * g [ x / k ]; } } else { // other cases. h [ x ] = h [ rem [ x ]] * h [ x / rem [ x ]]; } } return h ; } ```   
---|---  
  
## åèèµæä¸æ³¨é

  * [Dirichlet convolution - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_convolution)
  * [Dirichlet series - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_series)
  * [Euler product - Wikipedia](https://en.wikipedia.org/wiki/Euler_product)
  * [Dirichlet ç©ã¨ãæ°è«é¢æ°ã®ç´¯ç©å by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/3/25 15:00:02ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/dirichlet.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/dirichlet.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [danielqfmai](https://github.com/danielqfmai), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [Nanarikom](https://github.com/Nanarikom), [ouuan](https://github.com/ouuan), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
