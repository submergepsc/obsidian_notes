# Entringer Number - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/entringer/

# Entringer Number

## æ©ç¹ææ ¼æ°

æ©ç¹ææ ¼æ°ï¼Entringer numberï¼[OEIS A008281](http://oeis.org/A008281)ï¼ð¸(ð,ð)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ»¡è¶³ä¸è¿°æ¡ä»¶ç 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ± ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°çç½®æ¢æ°ç®ï¼

  * é¦å ç´ æ¯ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  * é¦å ç´ çä¸ä¸ä¸ªå ç´ æ¯é¦å ç´ å°ï¼åä¸ä¸ä¸ªå ç´ æ¯åä¸ä¸ªå ç´ å¤§ï¼åä¸ä¸ä¸ªå ç´ æ¯åä¸ä¸ªå ç´ å°â¦â¦åé¢ç¸é»å ç´ çå¤§å°å ³ç³»åæ»¡è¶³è¿æ ·çè§åï¼

æ©ç¹ææ ¼æ°çåå¼æï¼

ð¸(0,0)=1E(0,0)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ð¸(ð,0)=0E(n,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æéæ¨å ³ç³»ï¼

ð¸(ð,ð)=ð¸(ð,ðâ1)+ð¸(ðâ1,ðâð)E(n,k)=E(n,kâ1)+E(nâ1,nâk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## SeidelâEntringerâArnold ä¸è§

æ©ç¹ææ ¼æ°çä¸ä¸ªéå½æåçæ°å­ä¸è§ï¼ç§°ä¸º SeidelâEntringerâArnold ä¸è§ï¼SeidelâEntringerâArnold triangleï¼[OEIS A008280](http://oeis.org/A008280)ï¼ï¼è¯¥ä¸è§æ¯æç §ãçèãé¡ºåºï¼ox-plowing orderï¼æåçæ©ç¹ææ ¼æ° ð¸(ð,ð)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ð¸(0,0)ð¸(1,0)âð¸(1,1)ð¸(2,2)âð¸(2,1)âð¸(2,0)ð¸(3,0)âð¸(3,1)âð¸(3,2)âð¸(3,3)ð¸(4,4)âð¸(4,3)âð¸(4,2)âð¸(4,1)âð¸(4,0)E(0,0)E(1,0)âE(1,1)E(2,2)âE(2,1)âE(2,0)E(3,0)âE(3,1)âE(3,2)âE(3,3)E(4,4)âE(4,3)âE(4,2)âE(4,1)âE(4,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³ï¼

10â11â1â00â1â2â25â5â4â2â010â11â1â00â1â2â25â5â4â2â0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æç §è¿ç§æ¹å¼æåçæ©ç¹ææ ¼æ°çä¼å¿æ¯ï¼ä¸å®çéæ¨å ³ç³» ð¸(ð,ð) =ð¸(ð,ð â1) +ð¸(ð â1,ð âð)E(n,k)=E(n,kâ1)+E(nâ1,nâk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸è´ï¼å¯ä»¥æ¹ä¾¿è®°å¿åçè§£ï¼

æ©ç¹ææ ¼æ°æä¸ä¸ªææ°åçæå½æ°ï¼

ââð=0ââð=0ð¸(ð+ð,12(ð+ð+(â1)ð+ð(ðâð)))ð¥ðð!ð¥ðð!=cosâ¡ð¥+sinâ¡ð¥cosâ¡(ð¥+ð¦)âm=0âân=0âE(m+n,12(m+n+(â1)m+n(nâm)))xmm!xnn!=cosâ¡x+sinâ¡xcosâ¡(x+y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿ä¸ªçæå½æ°çç³»æ°åå¸äºå®ä¸æ¯ä¸é¢ç SeidelâEntringerâArnold ä¸è§çç®åæä¼¸åå½¢ï¼

ð¸(0,0)ð¸(1,1)ð¸(2,0)ð¸(3,3)ð¸(4,0)ð¸(1,0)ð¸(2,1)ð¸(3,2)ð¸(4,1)ð¸(2,2)ð¸(3,1)ð¸(4,2)ð¸(3,0)ð¸(4,3)ð¸(4,4)E(0,0)E(1,1)E(2,0)E(3,3)E(4,0)E(1,0)E(2,1)E(3,2)E(4,1)E(2,2)E(3,1)E(4,2)E(3,0)E(4,3)E(4,4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å³ï¼

110200122114055110200122114055![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## zigzag ç½®æ¢

ä¸ä¸ª zigzag ç½®æ¢ï¼zigzag permutationï¼æ¯ä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæå ð1c1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ððci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½¿å¾ä»»æä¸ä¸ªå ç´ ððci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå¤§å°é½ä¸ä»äº ððâ1ciâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðð+1ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹é´ï¼

å¯¹äº zigzag ç½®æ¢çä¸ªæ° ððZn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼[OEIS A001250](http://oeis.org/A001250)ï¼ï¼ä» ð =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§æï¼

1,1,2,4,10,32,122,544,â¯1,1,2,4,10,32,122,544,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¾å¦ï¼åå ä¸ª ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäº¤æ¿ç½®æ¢æï¼

ð=1:{1}ð=2:{1,2},{2,1}ð=3:{1,3,2},{2,1,3},{2,3,1},{3,1,2}ð=4:{1,3,2,4},{1,4,2,3},{2,1,4,3},{2,3,1,4},{2,4,1,3},{3,1,4,2},{3,2,4,1},{3,4,1,2},{4,1,3,2},{4,2,3,1}n=1:{1}n=2:{1,2},{2,1}n=3:{1,3,2},{2,1,3},{2,3,1},{3,1,2}n=4:{1,3,2,4},{1,4,2,3},{2,1,4,3},{2,3,1,4},{2,4,1,3},{3,1,4,2},{3,2,4,1},{3,4,1,2},{4,1,3,2},{4,2,3,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## äº¤æ¿ç½®æ¢ä¸ zigzag æ°

ï¼æ³¨æåãéä½æåãè¿è¡æ¦å¿µä¸çåºåï¼ï¼

å¯¹äºå¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ¯ä¸ª zigzag ç½®æ¢ç¿»è½¬è¿æ¥ä»æ§ä¸º zigzag ç½®æ¢ï¼å¯ä»¥ä¸¤ä¸¤é å¯¹ï¼æä»¥å¿ ç¶ä¸ºå¶æ°ï¼

è¿éåç»åºä¸ç§é å¯¹çæ¹æ³ï¼å° zigzag ç½®æ¢åä¸ºäº¤æ¿ç½®æ¢ï¼alternating permutationï¼ååäº¤æ¿ç½®æ¢ï¼reverse alternating permutationï¼ï¼

äº¤æ¿ç½®æ¢çé¦å ç´ å¤§äºç¬¬äºä¸ªå ç´ ï¼å¤§å°å ³ç³»ä¸ºï¼

ð1>ð2<ð3>â¯c1>c2<c3>â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åäº¤æ¿ç½®æ¢çé¦å ç´ å°äºç¬¬äºä¸ªå ç´ ï¼å¤§å°å ³ç³»ä¸ºï¼

ð1<ð2>ð3<â¯c1<c2>c3<â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¦æå° 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç½®äºæ¢ï¼22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç½®äºæ¢ï¼ä»¥æ­¤ç±»æ¨ï¼å³å¯å°äº¤æ¿ç½®æ¢ä¸åäº¤æ¿ç½®æ¢ä¸¤ä¸ªéåäºæ¢ï¼å æ­¤ï¼äº¤æ¿ç½®æ¢ä¸åäº¤æ¿ç½®æ¢çä¸ªæ°ç¸ç­ï¼æ°å¥½ä¸º zigzag ç½®æ¢çä¸åï¼

å¯¹äºå¤§äº 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼è®°ï¼

ð´ð=ðð2An=Zn2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å®ä¹åå¼ï¼

ð´0=ð´1=1A0=A1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è¿éç ð´ðAn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸º zigzag æ°ï¼Euler zigzag numberï¼[OEIS A000111](http://oeis.org/A000111)ï¼ï¼ä» ð =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§æï¼

1,1,1,2,5,16,61,272,â¯1,1,1,2,5,16,61,272,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ¥ä¸æ¥è¯çæ±è§£ ð´ðAn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹ä¸­ï¼éå ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ°ææå­éï¼æ (ðð)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§éæ³ï¼

å¨è¿ä¸ª ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­éä¸­ï¼éåäº¤æ¿ç½®æ¢ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð´ðAk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§éæ³ï¼ç¨å ¨éåæè¿ä¸ª ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­éï¼å©ä½ç ð âðnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å å­éä¸­ï¼éåäº¤æ¿ç½®æ¢ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ð´ðâðAnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§éæ³ï¼

èè ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å æå ð¤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å° ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åç½®ä½ä¸ºå¼å¤´ï¼æ¥ä¸ ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åæ¥ä¸ ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹ï¼ð¤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸å®æ¯ zigzag ç½®æ¢ï¼å¹¶ä¸ä»»æä¸ä¸ª ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å  zigzag ç½®æ¢ï¼é½å¯ä»¥å¨ ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤æªæ­å¾å°å¯¹åºçåäº¤æ¿ç½®æ¢ ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸ä¸åç ð +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å  zigzag ç½®æ¢å¯¹åºç ð¢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð£v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸åï¼

å æ­¤æéæ¨å ³ç³»ï¼

2ð´ð+1=ðâð=0(ðð)ð´ðð´ðâð2An+1=âk=0n(nk)AkAnâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2(ð+1)ð´ð+1(ð+1)!=ðâð=0ð´ðð!ð´ðâð(ðâð)!2(n+1)An+1(n+1)!=âk=0nAkk!Anâk(nâk)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶å¹¶ä¸æ»¡è¶³è¿ä¸ªéæ¨å¼ï¼åå¼ ð´0A0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð´1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é½æ¯ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯è§ï¼è¿æ¯ä¸ä¸ªææ°åçæå½æ°çå·ç§¯ï¼åè®¾ ð´ðAn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææ°åçæå½æ°ä¸º ð¦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å°±æå¾®åæ¹ç¨ï¼

2dð¦dð¥=ð¦2+12dydx=y2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç­å¼å³é¢å 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ºäºå¤ç ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶çç¹æ®æ åµï¼è¯¥æ¹ç¨çéè§£ä¸ºï¼

ð¦=tanâ¡(12ð¥+ð¶)y=tanâ¡(12x+C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥ç¬¬ 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) é¡¹ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åï¼å¯ä»¥å¾å°ç¹è§£ï¼

ð¦=tanâ¡ð¥+secâ¡ð¥y=tanâ¡x+secâ¡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ­£åå½æ°æ¯å¥å½æ°ï¼æ­£å²å½æ°æ¯å¶å½æ°ï¼ä¸¤è ä¹åææ zigzag æ°ççæå½æ°ï¼

## æ©ç¹ææ ¼æ°ä¸ zigzag æ°çå ³ç³»

æ ¹æ®æ©ç¹ææ ¼æ°çå®ä¹ï¼æ©ç¹ææ ¼æ° ð¸(ð,ð)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯é¦å ç´ ä¸º ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäº¤æ¿ç½®æ¢ä¸ªæ°ï¼å æ­¤æ©ç¹ææ ¼æ°ä¸ zigzag æ°äºå®ä¸æå ³ç³»ï¼

ð´ð=ð¸(ð,ð)An=E(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å° ð´ðAn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç§°ä¸ºãzigzag æ°ãä¹æåå ï¼è®° ð¸ðEn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯æ¬§ææ°ï¼Euler numberï¼ï¼ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¼¯åªå©æ°ï¼

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¶æ°æ¶ï¼å¶æ°é¡¹ä¸æ ç zigzag æ°ä¹ç§°ãæ­£å²æ°ãððSn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè ãzig æ°ãï¼æå ³ç³»ï¼

ð´ð=(â1)ð/2ð¸ðAn=(â1)n/2En![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå é¡¹ä¸ºï¼[OEIS A000364](http://oeis.org/A000364)ï¼ï¼

1,1,5,61,1385,â¯1,1,5,61,1385,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºå¥æ°æ¶ï¼å¥æ°é¡¹ä¸æ ç zigzag æ°ä¹ç§°ãæ­£åæ°ãððTn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æè ãzag æ°ãï¼æå ³ç³»ï¼

ð´ð=(â1)(ðâ1)/22ð+1(2ð+1â1)ðµð+1ð+1An=(â1)(nâ1)/22n+1(2n+1â1)Bn+1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

åå é¡¹ä¸ºï¼[OEIS A000182](http://oeis.org/A000182)ï¼ï¼

1,2,16,272,7936,â¯1,2,16,272,7936,â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯å¯¹äºå¨ ð¥ =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¤çæ³°åå±å¼ï¼å¯ä»¥ç»åºæ­£å²æ°åæ­£åæ°ï¼

secâ¡ð¥=ð´0+ð´2ð¥22!+ð´4ð¥44!+â¯secâ¡x=A0+A2x22!+A4x44!+â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)tanâ¡ð¥=ð´1ð¥+ð´3ð¥33!+ð´5ð¥55!+â¯tanâ¡x=A1x+A3x33!+A5x55!+â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æè åå°ä¸èµ·ï¼

secâ¡ð¥+tanâ¡ð¥=ð´0+ð´1ð¥+ð´2ð¥22!+ð´3ð¥33!+ð´4ð¥44!+ð´5ð¥55!+â¯secâ¡x+tanâ¡x=A0+A1x+A2x22!+A3x33!+A4x44!+A5x55!+â¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ææ zigzag æ°ççæå½æ°ï¼

## åèèµæä¸é¾æ¥

  1. [Alternating permutation - Wikipedia](https://en.wikipedia.org/wiki/Alternating_permutation)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/entringer.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/entringer.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [jifbt](https://github.com/jifbt)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
