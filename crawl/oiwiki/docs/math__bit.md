# ä½æä½ - OI Wiki

- Source: https://oi-wiki.org/math/bit/

# ä½æä½

ä½æä½æçæ¯å¯¹æ´æ°äºè¿å¶è¡¨ç¤ºçä¸å åäºå æä½ï¼åä¸º **ä½è¿ç®** å **ç§»ä½** ä¸¤ç±»ï¼ä½æä½æ¯ CPU ä¸­æåºç¡çä¸ç±»è¿ç®ï¼å ¶éåº¦å¾å¾æ¯ç¸å½å¿«çï¼

## æ´æ°ä¸ä½åºå

å¦è¯·åé ï¼[æ´æ°ç±»å](../../lang/var/#æ´æ°ç±»å)ã[è¡¥æ°æ³](../numeral-sys/base/#è¡¥æ°æ³)

æä»¬å°åªç± `0` æ `1` ææçé¿åº¦åºå®çåºåç§°ä¸ºä½åºåï¼æå·¦è¾¹çä½ç§°ä¸ºæé«ä½ï¼æå³è¾¹çä½ç§°ä¸ºæä½ä½ï¼

è®¡ç®æºä¸­ç¨ä½åºåè¡¨ç¤ºä¸å®èå´å çæ´æ°ï¼é¿åº¦ä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½åºååªæ 2ð2N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§ï¼æä»¥åªè½å 2ð2N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ´æ°å»ºç«ä¸ä¸å¯¹åºå ³ç³»ï¼è¿ç§ä¸ä¸å¯¹åºå ³ç³»å¯ä»¥åä¸ºä¸¤ç±»ï¼**æç¬¦å·** å **æ ç¬¦å·** ï¼æç¬¦å·æçæ¯å¯¹åºçæ´æ°æè´æ°ï¼æ ç¬¦å·æçæ¯å¯¹åºçæ´æ°å ¨é¨ä¸ºéè´æ°ï¼

  * å¯¹äºæ ç¬¦å·çå¯¹åºå ³ç³»ï¼æä»¬å¯ä»¥ç´æ¥å°æ´æ°çäºè¿å¶è¡¨ç¤ºä½ä¸ºä½åºåï¼é¿åº¦ä¸è¶³å°±å¨é«ä½è¡¥ `0`ï¼

å¨æ ç¬¦å·çå¯¹åºå ³ç³»ä¸ï¼é¿åº¦ä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½åºåå¯ä»¥è¡¨ç¤º [0,2ð â1][0,2Nâ1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å çæ´æ°ï¼

  * å¯¹äºæç¬¦å·çå¯¹åºå ³ç³»ï¼æä»¬æä¸¤ç§è¡¨ç¤ºè§åï¼**åç ** ï¼ones' complementï¼å **è¡¥ç ** ï¼two's complementï¼ï¼

å¯¹äºéè´æ´æ°æ¥è¯´ï¼å ¶è¡¨ç¤ºè§ååæ ç¬¦å·çè§åä¸è´ï¼å¯¹äºè´æ´æ°æ¥è¯´ï¼æä»¬å°å ¶ç¸åæ°å¯¹åºçä½åºå **æä½åå** ï¼å³å° `0` åä¸º `1`ï¼å° `1` åä¸º `0`ï¼åçç»æç§°ä¸ºåç ï¼å°åç ææ ç¬¦å·çå¯¹åºå ³ç³»è½¬ä¸ºæ´æ°ï¼ç¶åå ä¸ï¼æåææ ç¬¦å·çå¯¹åºå ³ç³»è½¬ä¸ºä½åºåï¼è¶ åºåä½åºåé¿åº¦çé¨åèå¼ï¼å¾å°çæ°åºåç§°ä¸ºè¡¥ç ï¼

å¨åç çå¯¹åºå ³ç³»ä¸ï¼é¿åº¦ä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½åºåå¯ä»¥è¡¨ç¤º [ â2ðâ1 +1,2ðâ1 â1][â2Nâ1+1,2Nâ1â1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å çæ´æ°ï¼

å¨è¡¥ç çå¯¹åºå ³ç³»ä¸ï¼é¿åº¦ä¸º ðN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½åºåå¯ä»¥è¡¨ç¤º [ â2ðâ1,2ðâ1 â1][â2Nâ1,2Nâ1â1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å çæ´æ°ï¼

ä»¥ 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çä½åºåä¸ºä¾ï¼

ä½åºå| æ ç¬¦å·æ´æ°| æç¬¦å·æ´æ°ï¼åç ï¼| æç¬¦å·æ´æ°ï¼è¡¥ç ï¼  
---|---|---|---  
`000`| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`001`| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`010`| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`011`| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`100`| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â3â3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â4â4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`101`| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â2â2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â3â3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`110`| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â2â2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`111`| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â0â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
å¯ä»¥çå°åç çæå¤§é®é¢æ¯ä¼åºç° â0â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ä¸ªå®é ä¸ä¸å­å¨çãè´æ°ãï¼æä»¥ä¸è¬æ åµä¸æä»¬åªç¨è¡¥ç ï¼ç±äºè¡¨ç¤ºæç¬¦å·æ´æ°æ¶ï¼å ¶æ­£è´å·ä» ç±ä½åºåçæé«ä½å³å®ï¼æä»¥æä»¬å°è¿ä¸ä½ç§°ä¸º **ç¬¦å·ä½** ï¼

å°ä½åºåè½¬ä¸ºæ´æ°ä¹æ¯å®¹æåå°çï¼å¯¹éè´æ°æ¥è¯´ä¸éè¦ç¹å«æä½ï¼å¯¹åç æ¥è¯´ååå³å¯å¾å°å¯¹åºçç¸åæ°ï¼å¯¹è¡¥ç æ¥è¯´ååå ä¸å³å¯å¾å°å¯¹åºçç¸åæ°ï¼

## ä½è¿ç®

ä½è¿ç®æçæ¯å¯¹ä½åºåéä½åºç¨æäº [å¸å°å½æ°](../boolean-algebra/#å¸å°å½æ°) çè¿ç®ï¼å½¢å¼åå°è¯´ï¼å¯¹å¸å°å½æ° ð :ðð âðf:BkâB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½è¿ç®å³ä¸ºå½¢å¦

ð¹:(ðð)ðâðð((ð1,1,â¦,ðð,1),â¦,(ð1,ð,â¦,ðð,ð))â¦(ð(ð1,1,â¦,ð1,ð),â¦,ð(ðð,1,â¦,ðð,ð))F:(Bm)kâBm((p1,1,â¦,pm,1),â¦,(p1,k,â¦,pm,k))â¦(f(p1,1,â¦,p1,k),â¦,f(pm,1,â¦,pm,k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

çå½æ°ï¼å ¶ä¸­ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä½åºåçé¿åº¦ï¼åæ ·çï¼æä»¬ä¸è¬åªç ç©¶ä¸å åäºå çä½è¿ç®ï¼å¦æ ç¹æ®è¯´æï¼ä¸æçä½è¿ç®ä» éäºä¸å åäºå çæ åµï¼

ä¸è¬æ¥è¯´ï¼æä»¬æ **æä½åå** ã**æä½ä¸** ã**æä½æ** ã**æä½å¼æ** è§ä½åºæ¬çä½è¿ç®ï¼å ¶ä½çä½è¿ç®åå¯ä»¥éè¿è¿äºè¿ç®ç»åå¾å°ï¼

ä½è¿ç®| æ°å­¦ç¬¦å·è¡¨ç¤º| å¯¹åºçå¸å°å½æ°| C++ è¿ç®ç¬¦| è§£é  
---|---|---|---|---  
æä½åå| NOTNOT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Â¬Â¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `~`| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
æä½ä¸| ANDAND![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â§â§![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `&`| åªæä¸¤ä¸ªå¯¹åºä½é½ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶æä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
æä½æ| OROR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â¨â¨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `|`| åªè¦ä¸¤ä¸ªå¯¹åºä½ä¸­æä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶å°±ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
æä½å¼æ| ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ãXORXOR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `^`| åªæä¸¤ä¸ªå¯¹åºä½ä¸åæ¶æä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
Warning

æ³¨æåºåä½è¿ç®ä¸å¸å°å½æ°ï¼

ä¾å¦ï¼

  * NOTâ¡01010111 =10101000NOTâ¡01010111=10101000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * 01010011ANDâ¡00110010 =0001001001010011ANDâ¡00110010=00010010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * 01010011ORâ¡00110010 =0111001101010011ORâ¡00110010=01110011![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * 01010011XORâ¡00110010 =0110000101010011XORâ¡00110010=01100001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ç±äºä¸è¿°åç§ä½è¿ç®å¨è¿ç®æ¶ï¼åä¸ªä½çè¿ç®ç¬ç«ï¼æä»¥è¿åç§ä½è¿ç®è½ç´æ¥ç»§æ¿å ¶å¯¹åºå¸å°å½æ°çæ§è´¨ï¼

ä¸ºæ¹ä¾¿èµ·è§ï¼å¨ä½åºåé¿åº¦å·²ç¥æ¶ï¼æä»¬ä¹å¯ä»¥ç´æ¥å¯¹æ´æ°åä½è¿ç®ï¼ä¾å¦ï¼

NOTâ¡5=â6,NOTâ¡(â5)=4,5ANDâ¡6=4,5ORâ¡6=7,5XORâ¡6=3.NOTâ¡5=â6,NOTâ¡(â5)=4,5ANDâ¡6=4,5ORâ¡6=7,5XORâ¡6=3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åè®¾ ð¥,ð¦ â¥0x,yâ¥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬ä¹å¯ä»¥å°ä½è¿ç®ç¨æ±åçæ¹å¼è¡¨ç¤ºï¼

NOTâ¡ð¥=âlog2â¡ð¥ââð=02ð((âð¥2ðâmod2+1)mod2)=âlog2â¡ð¥ââð=0(2âlog2â¡ð¥â+1â1âð¥)ð¥ANDâ¡ð¦=âlog2â¡max{ð¥,ð¦}ââð=02ð(âð¥2ðâmod2)(âð¦2ðâmod2)ð¥ORâ¡ð¦=âlog2â¡max{ð¥,ð¦}ââð=02ð((âð¥2ðâmod2)+(âð¦2ðâmod2)â(âð¥2ðâmod2)(âð¦2ðâmod2))ð¥XORâ¡ð¦=âlog2â¡max{ð¥,ð¦}ââð=02ð(((âð¥2ðâmod2)+(âð¦2ðâmod2))mod2)=âlog2â¡max{ð¥,ð¦}ââð=02ð((âð¥2ðâ+âð¦2ðâ)mod2)NOTâ¡x=ân=0âlog2â¡xâ2n((âx2nâmod2+1)mod2)=ân=0âlog2â¡xâ(2âlog2â¡xâ+1â1âx)xANDâ¡y=ân=0âlog2â¡max{x,y}â2n(âx2nâmod2)(ây2nâmod2)xORâ¡y=ân=0âlog2â¡max{x,y}â2n((âx2nâmod2)+(ây2nâmod2)â(âx2nâmod2)(ây2nâmod2))xXORâ¡y=ân=0âlog2â¡max{x,y}â2n(((âx2nâmod2)+(ây2nâmod2))mod2)=ân=0âlog2â¡max{x,y}â2n((âx2nâ+ây2nâ)mod2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¨ä¸å¼èµ·æ­§ä¹çæ åµä¸ï¼ä¸æä¸­çç¥ãæä½ãï¼

## ç§»ä½

å¦è¯·åé ï¼[C++ ä½æä½ç¬¦](../../lang/op/#ä½æä½ç¬¦)ï¼

ç§»ä½ä¸ºä¸ç±»å°ä½åºåãæä½åå·¦æåå³ç§»å¨ãçäºå è¿ç®ï¼ç¬¬ä¸ä¸ªåæ°ä¸ºä½åºåï¼ç¬¬äºä¸ªåæ°ä¸è¬ä¸ºéè´æ´æ°ï¼åå·¦ç§»å¨ç§°ä¸º **å·¦ç§»** ï¼åå³ç§»å¨ç§°ä¸º **å³ç§»** ï¼æ ¹æ®å¯¹ç§»å¨åçç©ºä½å¡«å æ¹å¼ï¼å¯å°ç§»ä½æä½åä¸º **ç®æ¯ç§»ä½** ã**é»è¾ç§»ä½** ã**å¾ªç¯ç§»ä½** ï¼å ¶ä¸­

  * é»è¾ç§»ä½ç¨ 0 å¡«å ç©ºä½ï¼
  * ç®æ¯å³ç§»ç¨ç¬¦å·ä½å¡«å ç©ºä½ï¼ç®æ¯å·¦ç§»åé»è¾å·¦ç§»ç¸åï¼
  * å¾ªç¯ç§»ä½ç¨æº¢åºä½å¡«å ç©ºä½ï¼

ä¾å¦å¯¹ 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½çä½åºå `10 01 01 10`ï¼

æä½| ç»æ  
---|---  
ç®æ¯å·¦ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `01 01 10 00`  
ç®æ¯å³ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `11 10 01 01`  
é»è¾å·¦ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `01 01 10 00`  
é»è¾å³ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `00 10 01 01`  
å¾ªç¯å·¦ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `01 01 10 10`  
å¾ªç¯å³ç§» 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½| `10 10 01 01`  
  
å¨ C++ ä¸­ï¼æä»¬ç¨ `a << b` è¡¨ç¤ºå·¦ç§»ï¼`a >> b` è¡¨ç¤ºå³ç§»ï¼å ·ä½éç¨ä½ç§ç§»ä½è§ååè§ [C++ ä½æä½ç¬¦](../../lang/op/#ä½æä½ç¬¦)ï¼

æä»¬å¯ä»¥ç¨å¦ä¸ä»£ç å®ç°å¾ªç¯ç§»ä½ï¼

å®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // From <https://stackoverflow.com/a/776523/224132> #include <climits> #include <cstdint> uint32_t rotl32 ( uint32_t value , unsigned int count ) { const unsigned int mask = CHAR_BIT * sizeof ( value ) \- 1 ; count &= mask ; return ( value << count ) | ( value >> ( \- count & mask )); } uint32_t rotr32 ( uint32_t value , unsigned int count ) { const unsigned int mask = CHAR_BIT * sizeof ( value ) \- 1 ; count &= mask ; return ( value >> count ) | ( value << ( \- count & mask )); } ```   
---|---  
  
## ä½æä½çåºç¨

ä½æä½ä¸è¬æä¸ç§ä½ç¨ï¼

  1. é«æå°è¿è¡æäºè¿ç®ï¼ä»£æ¿å ¶å®ä½æçæ¹å¼ï¼åè§ [ç¼è¯ä¼å #å¼ºåº¦åå](../../lang/optimizations/#å¼ºåº¦åå-strength-reduction)ï¼
  2. [è¡¨ç¤ºéå](../binary-set/)ï¼å¸¸ç¨äº [ç¶å DP](../../dp/state/)ï¼ï¼
  3. é¢ç®æ¬æ¥å°±è¦æ±è¿è¡ä½æä½ï¼

éè¦æ³¨æçæ¯ï¼ç¨ä½æä½ä»£æ¿å ¶å®è¿ç®æ¹å¼å¨å¾å¤æ¶åå¹¶ä¸è½å¸¦æ¥å¤ªå¤§çä¼åï¼åèä¼ä½¿ä»£ç åå¾å¤æï¼ä½¿ç¨æ¶éè¦æé ï¼

### æå ³ 2 çå¹çåºç¨

ç±äºä½æä½éå¯¹çæ¯äºè¿å¶è¡¨ç¤ºï¼å æ­¤å¯ä»¥æ¨å¹¿åºè®¸å¤ä¸ 2 çæ´æ°æ¬¡å¹æå ³çåºç¨ï¼

å°ä¸ä¸ªæ°ä¹ï¼é¤ï¼2 çéè´æ´æ°æ¬¡å¹ï¼

C++Python

```text 1 2 3 4 5 6 7 ``` |  ```text int mulPowerOfTwo ( int n , int m ) { // è®¡ç® n*(2^m) return n << m ; } int divPowerOfTwo ( int n , int m ) { // è®¡ç® n/(2^m) return n >> m ; } ```   
---|---  
  
```text 1 2 3 4 5 6 ``` |  ```text def mulPowerOfTwo ( n , m ): # è®¡ç® n*(2^m) return n << m def divPowerOfTwo ( n , m ): # è®¡ç® n/(2^m) return n >> m ```   
---|---  
  
Warning

æä»¬å¹³å¸¸åçé¤æ³æ¯å 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ´ï¼èè¿éçå³ç§»æ¯åä¸åæ´ï¼æ³¨æè¿éçåºå«ï¼ï¼å³å½æ°å¤§äºç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ä¸¤ç§æ¹æ³ç­ä»·ï¼å½æ°å°äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ä¼æåºå«ï¼å¦ï¼`-1 / 2` çå¼ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è `-1 >> 1` çå¼ä¸º â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

### åç»å¯¹å¼

å¨æäºæºå¨ä¸ï¼æçæ¯ `n > 0 ? n : -n` é«ï¼

C++Python

```text 1 2 3 4 5 6 7 ``` |  ```text int Abs ( int n ) { return ( n ^ ( n >> 31 )) \- ( n >> 31 ); /* n>>31 åå¾ n çç¬¦å·ï¼è¥ n ä¸ºæ­£æ°ï¼n>>31 ç­äº 0ï¼è¥ n ä¸ºè´æ°ï¼n>>31 ç­äº -1 è¥ n ä¸ºæ­£æ° n^0=n, æ°ä¸åï¼è¥ n ä¸ºè´æ°æ n^(-1) éè¦è®¡ç® n å -1 çè¡¥ç ï¼ç¶åè¿è¡å¼æè¿ç®ï¼ ç»æ n åå·å¹¶ä¸ä¸º n çç»å¯¹å¼å 1ï¼ååå» -1 å°±æ¯ç»å¯¹å¼ */ } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def Abs ( n ): return ( n ^ ( n >> 31 )) \- ( n >> 31 ) """ n>>31 åå¾ n çç¬¦å·ï¼è¥ n ä¸ºæ­£æ°ï¼n>>31 ç­äº 0ï¼è¥ n ä¸ºè´æ°ï¼n>>31 ç­äº -1 è¥ n ä¸ºæ­£æ° n^0=n, æ°ä¸åï¼è¥ n ä¸ºè´æ°æ n^(-1) éè¦è®¡ç® n å -1 çè¡¥ç ï¼ç¶åè¿è¡å¼æè¿ç®ï¼ ç»æ n åå·å¹¶ä¸ä¸º n çç»å¯¹å¼å 1ï¼ååå» -1 å°±æ¯ç»å¯¹å¼ """ ```   
---|---  
  
### åä¸¤ä¸ªæ°çæå¤§/æå°å¼

å¨æäºæºå¨ä¸ï¼æçæ¯ `a > b ? a : b` é«ï¼

C++Python

```text 1 2 3 4 ``` |  ```text // å¦æ a >= b, (a - b) >> 31 ä¸º 0ï¼å¦åä¸º -1 int max ( int a , int b ) { return ( b & (( a \- b ) >> 31 )) | ( a & ( ~ ( a \- b ) >> 31 )); } int min ( int a , int b ) { return ( a & (( a \- b ) >> 31 )) | ( b & ( ~ ( a \- b ) >> 31 )); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # å¦æ a >= b, (a - b) >> 31 ä¸º 0ï¼å¦åä¸º -1 def max ( a , b ): return b & (( a \- b ) >> 31 ) | a & ( ~ ( a \- b ) >> 31 ) def min ( a , b ): return a & (( a \- b ) >> 31 ) | b & ( ~ ( a \- b ) >> 31 ) ```   
---|---  
  
### å¤æ­ä¸¤éé¶æ°ç¬¦å·æ¯å¦ç¸å

C++Python

```text 1 2 3 ``` |  ```text bool isSameSign ( int x , int y ) { // æ 0 çæ åµä¾å¤ return ( x ^ y ) >= 0 ; } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # æ 0 çæ åµä¾å¤ def isSameSign ( x , y ): return ( x ^ y ) >= 0 ```   
---|---  
  
### äº¤æ¢ä¸¤ä¸ªæ°

è¯¥æ¹æ³å ·æå±éæ§

è¿ç§æ¹å¼åªè½ç¨æ¥äº¤æ¢ä¸¤ä¸ªæ´æ°ï¼ä½¿ç¨èå´æéï¼

å¯¹äºä¸è¬æ åµä¸çäº¤æ¢æä½ï¼æ¨èç´æ¥è°ç¨ `algorithm` åºä¸­ç `std::swap` å½æ°ï¼

```text 1 ``` |  ```text void swap ( int & a , int & b ) { a ^= b ^= a ^= b ; } ```   
---|---  
  
### æä½ä¸ä¸ªæ°çäºè¿å¶ä½

è·åä¸ä¸ªæ°äºè¿å¶çæä¸ä½ï¼

C++Python

```text 1 2 ``` |  ```text // è·å a çç¬¬ b ä½ï¼æä½ä½ç¼å·ä¸º 0 int getBit ( int a , int b ) { return ( a >> b ) & 1 ; } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # è·å a çç¬¬ b ä½ï¼æä½ä½ç¼å·ä¸º 0 def getBit ( a , b ): return ( a >> b ) & 1 ```   
---|---  
  
å°ä¸ä¸ªæ°äºè¿å¶çæä¸ä½è®¾ç½®ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 ``` |  ```text // å° a çç¬¬ b ä½è®¾ç½®ä¸º 0 ï¼æä½ä½ç¼å·ä¸º 0 int unsetBit ( int a , int b ) { return a & ~ ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # å° a çç¬¬ b ä½è®¾ç½®ä¸º 0 ï¼æä½ä½ç¼å·ä¸º 0 def unsetBit ( a , b ): return a & ~ ( 1 << b ) ```   
---|---  
  
å°ä¸ä¸ªæ°äºè¿å¶çæä¸ä½è®¾ç½®ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

C++Python

```text 1 2 ``` |  ```text // å° a çç¬¬ b ä½è®¾ç½®ä¸º 1 ï¼æä½ä½ç¼å·ä¸º 0 int setBit ( int a , int b ) { return a | ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # å° a çç¬¬ b ä½è®¾ç½®ä¸º 1 ï¼æä½ä½ç¼å·ä¸º 0 def setBit ( a , b ): return a | ( 1 << b ) ```   
---|---  
  
å°ä¸ä¸ªæ°äºè¿å¶çæä¸ä½ååï¼

C++Python

```text 1 2 ``` |  ```text // å° a çç¬¬ b ä½åå ï¼æä½ä½ç¼å·ä¸º 0 int flapBit ( int a , int b ) { return a ^ ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # å° a çç¬¬ b ä½åå ï¼æä½ä½ç¼å·ä¸º 0 def flapBit ( a , b ): return a ^ ( 1 << b ) ```   
---|---  
  
è¿äºæä½ç¸å½äºå°ä¸ä¸ª 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ´ååéå½ä½ä¸ä¸ªé¿åº¦ä¸º 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¸å°æ°ç»ï¼

## æ±ææé

æ±ææéæ¯ä¸ä¸²ç¬¦å·ä¸­ä¸åäºï¼å®ä¹å¨å ¶æä½¿ç¨çå­ç¬¦éä¸çï¼é¶ç¬¦å·ï¼zero-symbolï¼çä¸ªæ°ï¼å¯¹äºä¸ä¸ªäºè¿å¶æ°ï¼å®çæ±ææéå°±ç­äºå® 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼å³ `popcount`ï¼ï¼

æ±ä¸ä¸ªæ°çæ±ææéå¯ä»¥å¾ªç¯æ±è§£ï¼æä»¬ä¸æ­å°å»æè¿ä¸ªæ°å¨äºè¿å¶ä¸çæåä¸ä½ï¼å³å³ç§» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ï¼ç»´æ¤ä¸ä¸ªç­æ¡åéï¼å¨é¤çè¿ç¨ä¸­æ ¹æ®æä½ä½æ¯å¦ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ´æ°ç­æ¡ï¼

ä»£ç å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // æ± x çæ±ææé int popcount ( int x ) { int cnt = 0 ; while ( x ) { cnt += x & 1 ; x >>= 1 ; } return cnt ; } ```   
---|---  
  
æ±ä¸ä¸ªæ°çæ±ææéè¿å¯ä»¥ä½¿ç¨ `lowbit` æä½ï¼æä»¬å°è¿ä¸ªæ°ä¸æ­å°åå»å®ç `lowbit`1ï¼ç´å°è¿ä¸ªæ°åä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä»£ç å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // æ± x çæ±ææé int popcount ( int x ) { int cnt = 0 ; while ( x ) { cnt ++ ; x -= x & \- x ; } return cnt ; } ```   
---|---  
  
### æé æ±ææééå¢çæå

å¨ [ç¶å DP](../../dp/state/) ä¸­ï¼æç § popcount éå¢çé¡ºåºæä¸¾ææ¶å¯ä»¥é¿å éå¤æä¸¾ç¶æï¼è¿æ¯æé æ±ææééå¢çæåçä¸å¤§ä½ç¨ï¼

ä¸é¢æä»¬æ¥å ·ä½æ¢ç©¶å¦ä½å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æé æ±ææééå¢çæåï¼

æä»¬ç¥éï¼ä¸ä¸ªæ±ææéä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå°çæ´æ°ä¸º 2ð â12nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åªè¦å¯ä»¥å¨å¸¸æ°æ¶é´æé åºä¸ä¸ªæ´æ°æ±ææéç¸ç­çåç»§ï¼æä»¬å°±å¯ä»¥éè¿æä¸¾æ±ææéï¼ä» 2ð â12nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ä¸æ­å¯»æ¾ä¸ä¸ä¸ªæ°çæ¹å¼ï¼å¨ ð(ð)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å æé åº 0 â¼ð0â¼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¦åè¦æ±çæåï¼

èæ¾åºä¸ä¸ªæ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ±ææéç¸ç­çåç»§æè¿æ ·çæè·¯ï¼ä»¥ (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¾ï¼

  * æ (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³è¾¹ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå·¦ç§»å¨ï¼å¦æä¸è½ç§»å¨ï¼ç§»å¨å®å·¦è¾¹ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥æ­¤ç±»æ¨ï¼å¾å° (11010)2(11010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

  * æå¾å°ç (11010)2(11010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æåç§»å¨ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå çä½ç½®ä¸ç´å°æä½ä½çææ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½ç§»å°æå³è¾¹ï¼è¿éæåç§»å¨ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ¥å¨ç¬¬ä¸ä½ï¼æä»¥æåä¸ä½ 010010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¦åæ 001001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¾å° (11001)2(11001)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

è¿ä¸ªè¿ç¨å¯ä»¥ç¨ä½æä½ä¼åï¼

```text 1 2 ``` |  ```text int t = x \+ ( x & \- x ); x = t | (((( t & \- t ) / ( x & \- x )) >> 1 ) \- 1 ); ```   
---|---  
  
  * ç¬¬ä¸ä¸ªæ­¥éª¤ä¸­ï¼æä»¬ææ° ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ä¸å®ç `lowbit`ï¼å¨äºè¿å¶è¡¨ç¤ºä¸ï¼å°±ç¸å½äºæ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³è¾¹çè¿ç»­ä¸æ®µ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¢æå®å·¦è¾¹çä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¦åææå°çäºè¿å¶æ° (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å®å¨å ä¸å®ç `lowbit` åæ¯ (11000)2(11000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¿å ¶å®å¾å°äºæä»¬ç­æ¡çååé¨åï¼
  * æä»¬æ¥ä¸æ¥è¦æç­æ¡åé¢ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¥é½ï¼ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `lowbit` æ¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³è¾¹è¿ç»­ä¸æ®µ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå·¦è¾¹ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§»å¨åçä½ç½®ï¼è ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `lowbit` åæ¯ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³è¾¹è¿ç»­ä¸æ®µ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æå³è¾¹çä½ç½®ï¼è¿æ¯ä»¥ (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºä¾ï¼ð¡ =(11000)2t=(11000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼lowbitâ¡(ð¡) =(01000)2lowbitâ¡(t)=(01000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼lowbitâ¡(ð¥) =(00010)2lowbitâ¡(x)=(00010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * æ¥ä¸æ¥çé¤æ³æä½æ¯è¿ç§ä½æä½ä¸­æé¾çè§£çé¨åï¼ä½ä¹æ¯æå ³é®çé¨åï¼æä»¬è®¾ **åæ°** æå³è¾¹è¿ç»­ä¸æ®µ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æé«ä½ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ç¬¬ ðr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ä¸ï¼ä½æ°ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼ï¼æä½ä½ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¨ç¬¬ ðl![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼ð¡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `lowbit` ç­äº `1 << (r+1)`ï¼ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `lowbit` ç­äº `1 << l`ï¼`(((t&-t)/(x&-x))>>1)` å¾å°çï¼å°±æ¯ `(1<<(r+1))/(1<<l)/2 = (1<<r)/(1<<l) = 1<<(r-l)`ï¼å¨äºè¿å¶è¡¨ç¤ºä¸å°±æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åé¢è·ä¸ ð âðrâl![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªé¶ï¼é¶çä¸ªæ°æ­£å¥½ç­äºè¿ç»­ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°åå» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸¾æä»¬åæçæ°ä¸ºä¾ï¼lowbit(t)/2lowbit(x) =(00100)2(00010)2 =(00010)2lowbit(t)/2lowbit(x)=(00100)2(00010)2=(00010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æè¿ä¸ªæ°åå» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¾å°çå°±æ¯æä»¬è¦è¡¥å ¨çä½ä½ï¼æä¸åæ¥çæ°å°±å¯ä»¥å¾å°ç­æ¡ï¼

æä»¥æä¸¾ 0 â¼ð0â¼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ææ±ææééå¢çæåçå®æ´ä»£ç ä¸ºï¼

```text 1 2 3 4 5 6 ``` |  ```text for ( int i = 0 ; ( 1 << i ) \- 1 <= n ; i ++ ) { for ( int x = ( 1 << i ) \- 1 , t ; x <= n ; t = x \+ ( x & \- x ), x = x ? ( t | (((( t & \- t ) / ( x & \- x )) >> 1 ) \- 1 )) : ( n \+ 1 )) { // åä¸éè¦å®æçæä½ } } ```   
---|---  
  
å ¶ä¸­è¦æ³¨æ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¹å¤ï¼å ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ²¡æç¸åæ±ææéçåç»§ï¼

## C++ ä¸­çç¸å ³ç±»ä¸å½æ°

### GCC å å»ºå½æ°

GCC ä¸­è¿æä¸äºç¨äºä½æä½çå å»ºå½æ°ï¼

  * `int __builtin_ffs(int x)`ï¼è¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶æ«å°¾æåä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä½ç½®ï¼ä½ç½®çç¼å·ä» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§ï¼æä½ä½ç¼å·ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ï¼å½ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶è¿å 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * `int __builtin_clz(unsigned int x)`ï¼è¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶çåå¯¼ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼å½ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç»ææªå®ä¹ï¼
  * `int __builtin_ctz(unsigned int x)`ï¼è¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶æ«å°¾è¿ç»­ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼å½ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ç»ææªå®ä¹ï¼
  * `int __builtin_clrsb(int x)`ï¼å½ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç¬¦å·ä½ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶è¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶çåå¯¼ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°åä¸ï¼å¦åè¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶çåå¯¼ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°åä¸ï¼
  * `int __builtin_popcount(unsigned int x)`ï¼è¿å ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶ä¸­ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼
  * `int __builtin_parity(unsigned int x)`ï¼å¤æ­ ð¥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶ä¸­ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°çå¥å¶æ§ï¼

è¿äºå½æ°é½å¯ä»¥å¨å½æ°åæ«å°¾æ·»å `l` æ `ll`ï¼å¦ `__builtin_popcountll`ï¼æ¥ä½¿åæ°ç±»ååä¸º (`unsigned`)`long` æ (`unsigned`)`long long`ï¼è¿åå¼ä»ç¶æ¯ `int` ç±»åï¼ï¼ ä¾å¦ï¼æä»¬ææ¶åå¸ææ±åºä¸ä¸ªæ°ä»¥äºä¸ºåºçå¯¹æ°ï¼å¦æä¸èè `0` çç¹æ®æ åµï¼å°±ç¸å½äºè¿ä¸ªæ°äºè¿å¶çä½æ° `-1`ï¼èä¸ä¸ª `N` ä½æ´æ° `n` çäºè¿å¶è¡¨ç¤ºçä½æ°å¯ä»¥ä½¿ç¨ `N - __builtin_clz(n)` è¡¨ç¤ºï¼å æ­¤ `N - 1 - __builtin_clz(n)` å°±å¯ä»¥æ±åº `n` ä»¥äºä¸ºåºçå¯¹æ°ï¼

ç±äºè¿äºå½æ°æ¯å å»ºå½æ°ï¼ç»è¿äºç¼è¯å¨çé«åº¦ä¼åï¼è¿è¡éåº¦ååå¿«ï¼æäºçè³åªéè¦ä¸æ¡æä»¤ï¼ï¼

### æ´å¤ä½æ°

å¦æéè¦æä½çä½åºåéå¸¸é¿ï¼å¯ä»¥ä½¿ç¨ [`std::bitset`](../../lang/csl/bitset/)ï¼

## é¢ç®æ¨è

  * [Luogu P1225 é»ç½æ£æ¸¸æ](https://www.luogu.com.cn/problem/P1225)

## åèèµæä¸æ³¨é

  1. [ä½è¿ç®æå·§](https://graphics.stanford.edu/~seander/bithacks.html)
  2. [Bit Operation Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html)
  3. [Bitwise operation - Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

* * *

  1. ä¸ä¸ªæ°äºè¿å¶è¡¨ç¤ºä»ä½å¾é«çç¬¬ä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿ååé¢çé¶ï¼å¦ (1010)2(1010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç `lowbit` æ¯ (0010)2(0010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è¯¦è§ [æ ç¶æ°ç»](../../ds/fenwick/)ï¼Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/30 14:50:40ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/bit.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/bit.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [greyqz](https://github.com/greyqz), [Link-cute](https://github.com/Link-cute), [cjsoft](https://github.com/cjsoft), [Marcythm](https://github.com/Marcythm), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [lihaoyu1234](https://github.com/lihaoyu1234), [akakw1](https://github.com/akakw1), [Anguei](https://github.com/Anguei), [aofall](https://github.com/aofall), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Dian-Jiao](https://github.com/Dian-Jiao), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [flylai](https://github.com/flylai), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [Henry-ZHR](https://github.com/Henry-ZHR), [hhc0001](https://github.com/hhc0001), [hjsjhn](https://github.com/hjsjhn), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [Menci](https://github.com/Menci), [MingqiHuang](mailto:hmq011212@163.com), [orzAtalod](https://github.com/orzAtalod), [PlanariaIce](https://github.com/PlanariaIce), [sakuragi1111](https://github.com/sakuragi1111), [sbofgayschool](https://github.com/sbofgayschool), [shawlleyw](https://github.com/shawlleyw), [Shen-Linwood](https://github.com/Shen-Linwood), [skippre](https://github.com/skippre), [sshwy](https://github.com/sshwy), [stevenlele](https://github.com/stevenlele), [TOMWT-qwq](https://github.com/TOMWT-qwq), [Voileexperiments](https://github.com/Voileexperiments), [Xeonacid](https://github.com/Xeonacid), [xinchengo](https://github.com/xinchengo), [ylxmf2005](https://github.com/ylxmf2005), [zhilu-tang](https://github.com/zhilu-tang), [ZnPdCo](https://github.com/ZnPdCo), [zryi2003](https://github.com/zryi2003)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
