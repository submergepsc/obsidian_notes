# ä¼¯åªå©æ° - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/bernoulli/

# ä¼¯åªå©æ°

ä¼¯åªå©æ° ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ä¸ä¸ªä¸æ°è®ºæå¯åå ³èçæçæ°åºåï¼åå é¡¹è¢«åç°çä¼¯åªå©æ°åå«ä¸ºï¼

ðµ0 =1,ðµ1 = â12,ðµ2 =16,ðµ3 =0,ðµ4 = â130,â¦B0=1,B1=â12,B2=16,B3=0,B4=â130,â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## ç­å¹æ±å

ä¼¯åªå©æ°æ¯ç±é åå¸Â·ä¼¯åªå©çåå­å½åçï¼ä»å¨ç ç©¶ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¬¡å¹åçå ¬å¼æ¶åç°äºå¥å¦çå ³ç³»ï¼æä»¬è®°

ðð(ð)=ðâ1âð=0ðð=0ð+1ð+â¯+(ðâ1)ðSm(n)=âk=0nâ1km=0m+1m+â¯+(nâ1)m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¼¯åªå©è§å¯äºå¦ä¸ä¸åå ¬å¼ï¼å¾ç»åºä¸ç§æ¨¡å¼ï¼

ð0(ð)=ðð1(ð)=12ð2â12ðð2(ð)=13ð3â12ð2+16ðð3(ð)=14ð4â12ð3+14ð2ð4(ð)=15ð5â12ð4+13ð3â130ðS0(n)=nS1(n)=12n2â12nS2(n)=13n3â12n2+16nS3(n)=14n4â12n3+14n2S4(n)=15n5â12n4+13n3â130n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯ä»¥åç°ï¼å¨ ðð(ð)Sm(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ ðð+1nm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ»æ¯ 1ð+11m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ððnm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ»æ¯ â12â12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ððâ1nmâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ»æ¯ ð12m12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ððâ3nmâ3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ¯ âð(ðâ1)(ðâ2)720âm(mâ1)(mâ2)720![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ððâ4nmâ4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ»æ¯é¶ç­ï¼

è ððâðnmâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç³»æ°æ»æ¯æä¸ªå¸¸æ°ä¹ä»¥ ððââmkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ððââmkâ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºä¸éé¶ä¹å¹ï¼å³ ð!(ðâð)!m!(mâk)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

## éæ¨å ¬å¼

ðð(ð)=1ð+1(ðµ0ðð+1+(ð+11)ðµ1ðð+â¯+(ð+1ð)ðµðð)=1ð+1ðâð=0(ð+1ð)ðµððð+1âðSm(n)=1m+1(B0nm+1+(m+11)B1nm+â¯+(m+1m)Bmn)=1m+1âk=0m(m+1k)Bknm+1âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¼¯åªå©æ°ç±éå«çéæ¨å ³ç³»å®ä¹ï¼

ðâð=0(ð+1ð)ðµð=0,(ð>0)ðµ0=1âj=0m(m+1j)Bj=0,(m>0)B0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¾å¦ï¼(20)ðµ0 +(21)ðµ1 =0(20)B0+(21)B1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åå ä¸ªå¼æ¾ç¶æ¯

ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â¦â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
---|---|---|---|---|---|---|---|---|---|---  
ðµðBn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â12â12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â130â130![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 142142![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â130â130![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| â¦â¦![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
### è¯æ

#### å©ç¨å½çº³æ³è¯æ

è¿ä¸ªè¯ææ¹æ³æ¥èª Concrete Mathematics 6.5 BERNOULLI NUMBERï¼

è¿ç¨äºé¡¹å¼ç³»æ°çæç­åæ¢åå½çº³æ³è¿è¡è¯æï¼

ðð+1(ð)+ðð+1=ðâ1âð=0(ð+1)ð+1=ðâ1âð=0ð+1âð=0(ð+1ð)ðð=ð+1âð=0(ð+1ð)ðð(ð)Sm+1(n)+nm+1=âk=0nâ1(k+1)m+1=âk=0nâ1âj=0m+1(m+1j)kj=âj=0m+1(m+1j)Sj(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»¤ Ëðð(ð) =1ð+1âðð=0(ð+1ð)ðµððð+1âðS^m(n)=1m+1âk=0m(m+1k)Bknm+1âk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æä»¬å¸æè¯æ ðð(ð) =Ëðð(ð)Sm(n)=S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åè®¾å¯¹ ð â[0,ð)jâ[0,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ ðð(ð) =Ëðð(ð)Sj(n)=S^j(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å°åå¼ä¸­ä¸¤è¾¹é½åå» ðð+1(ð)Sm+1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åå¯ä»¥å¾å°ï¼

ðð+1(ð)+ðð+1=ð+1âð=0(ð+1ð)ðð(ð)ðð+1=ðâð=0(ð+1ð)ðð(ð)=ðâ1âð=0(ð+1ð)Ëðð(ð)+(ð+1ð)ðð(ð)Sm+1(n)+nm+1=âj=0m+1(m+1j)Sj(n)nm+1=âj=0m(m+1j)Sj(n)=âj=0mâ1(m+1j)S^j(n)+(m+1m)Sm(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°è¯å¨å¼å­çå³è¾¹å ä¸ (ð+1ð)Ëðð(ð) â(ð+1ð)Ëðð(ð)(m+1m)S^m(n)â(m+1m)S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åè¿è¡åç®ï¼å¯ä»¥å¾å°ï¼

ðð+1=ðâð=0(ð+1ð)Ëðð(ð)+(ð+1)(ðð(ð)âËðð(ð))nm+1=âj=0m(m+1j)S^j(n)+(m+1)(Sm(n)âS^m(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸å¦¨è®¾ Î =ðð(ð) âËðð(ð)Î=Sm(n)âS^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸å° Ëðð(ð)S^j(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å±å¼ï¼é£ä¹æ

ðð+1=ðâð=0(ð+1ð)Ëðð(ð)+(ð+1)Î=ðâð=0(ð+1ð)1ð+1ðâð=0(ð+1ð)ðµððð+1âð+(ð+1)Înm+1=âj=0m(m+1j)S^j(n)+(m+1)Î=âj=0m(m+1j)1j+1âk=0j(j+1k)Bknj+1âk+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°ç¬¬äºä¸ª ââ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­çæ±åé¡ºåºæ¹ä¸ºéåï¼åå°ç»åæ°çåæ³æç­åæ¢å¯ä»¥å¾å°ï¼

ðð+1=ðâð=0(ð+1ð)1ð+1ðâð=0(ð+1ðâð)ðµðâððð+1+(ð+1)Î=ðâð=0(ð+1ð)1ð+1ðâð=0(ð+1ð+1)ðµðâððð+1+(ð+1)Î=ðâð=0(ð+1ð)1ð+1ðâð=0ð+1ð+1(ðð)ðµðâððð+1+(ð+1)Î=ðâð=0(ð+1ð)ðâð=0(ðð)ðµðâðð+1ðð+1+(ð+1)Înm+1=âj=0m(m+1j)1j+1âk=0j(j+1jâk)Bjâknk+1+(m+1)Î=âj=0m(m+1j)1j+1âk=0j(j+1k+1)Bjâknk+1+(m+1)Î=âj=0m(m+1j)1j+1âk=0jj+1k+1(jk)Bjâknk+1+(m+1)Î=âj=0m(m+1j)âk=0j(jk)Bjâkk+1nk+1+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹ä¸¤ä¸ªæ±åç¬¦å·è¿è¡äº¤æ¢ï¼å¯ä»¥å¾å°ï¼

ðð+1=ðâð=0ðð+1ð+1ðâð=ð(ð+1ð)(ðð)ðµðâð+(ð+1)Înm+1=âk=0mnk+1k+1âj=km(m+1j)(jk)Bjâk+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å¯¹ (ð+1ð)(ðð)(m+1j)(jk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡æç­åæ¢ï¼

(ð+1ð)(ðð)ï¼(ð+1ð)(ðâð+1ðâð)(m+1j)(jk)ï¼(m+1k)(mâk+1jâk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

é£ä¹å¼å­å°±åæäºï¼

ðð+1=ðâð=0ðð+1ð+1ðâð=ð(ð+1ð)(ðâð+1ðâð)ðµðâð+(ð+1)Î=ðâð=0ðð+1ð+1(ð+1ð)ðâð=ð(ðâð+1ðâð)ðµðâð+(ð+1)Înm+1=âk=0mnk+1k+1âj=km(m+1k)(mâk+1jâk)Bjâk+(m+1)Î=âk=0mnk+1k+1(m+1k)âj=km(mâk+1jâk)Bjâk+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

å°ææç ð âðjâk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç¨ ðj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä»£æ¿ï¼é£ä¹å°±å¯ä»¥å¾å°ï¼

ðð+1=ðâð=0ðð+1ð+1(ð+1ð)ðâðâð=0(ðâð+1ð)ðµð+(ð+1)Înm+1=âk=0mnk+1k+1(m+1k)âj=0mâk(mâk+1j)Bj+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

èèæä»¬åé¢æå°è¿çéå½å ³ç³»

ðâð=0(ð+1ð)ðµð=0,(ð>0)ðµ0=1ðâð=0(ð+1ð)ðµð=[ð=0]âj=0m(m+1j)Bj=0,(m>0)B0=1âj=0m(m+1j)Bj=[m=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥åå¯ä»¥å¾å°ï¼

ðð+1=ðâð=0ðð+1ð+1(ð+1ð)[ðâð=0]+(ð+1)Î=ðâð=0ðð+1ð+1(ð+1ð)+(ð+1)Î=ðð+1ð+1(ð+1ð)+(ð+1)Î=ðð+1+(ð+1)Înm+1=âk=0mnk+1k+1(m+1k)[mâk=0]+(m+1)Î=âk=0mnk+1k+1(m+1k)+(m+1)Î=nm+1m+1(m+1m)+(m+1)Î=nm+1+(m+1)Î![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

äºæ¯ Î =0Î=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸æ ðð(ð) =Ëðð(ð)Sm(n)=S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

#### å©ç¨ææ°çæå½æ°è¯æ

å¯¹éæ¨å¼ âðð=0(ð+1ð)ðµð =[ð =0]âj=0m(m+1j)Bj=[m=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸¤è¾¹é½å ä¸ ðµð+1Bm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å¾å°ï¼

ð+1âð=0(ð+1ð)ðµð=[ð=0]+ðµð+1ðâð=0(ðð)ðµð=[ð=1]+ðµððâð=0ðµðð!â 1(ðâð)!=[ð=1]+ðµðð!âj=0m+1(m+1j)Bj=[m=0]+Bm+1âj=0m(mj)Bj=[m=1]+Bmâj=0mBjj!â 1(mâj)!=[m=1]+Bmm!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ðµ(ð§) =âðâ¥0ðµðð!ð§ðB(z)=âiâ¥0Bii!zi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼æ³¨æå°å·¦è¾¹ä¸ºå·ç§¯å½¢å¼ï¼æ ï¼

ðµ(ð§)eð§=ð§+ðµ(ð§)ðµ(ð§)=ð§eð§â1B(z)ez=z+B(z)B(z)=zezâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è®¾ ð¹ð(ð§) =âðâ¥0ðð(ð)ð!ð§ðFn(z)=âmâ¥0Sm(n)m!zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼åï¼

ð¹ð(ð§)=âðâ¥0ðð(ð)ð!ð§ð=âðâ¥0ðâ1âð=0ððð§ðð!Fn(z)=âmâ¥0Sm(n)m!zm=âmâ¥0âi=0nâ1imzmm!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

è°æ¢æ±åé¡ºåºï¼

ð¹ð(ð§)=ðâ1âð=0âðâ¥0ððð§ðð!=ðâ1âð=0eðð§=eðð§â1eð§â1=ð§eð§â1â eðð§â1ð§Fn(z)=âi=0nâ1âmâ¥0imzmm!=âi=0nâ1eiz=enzâ1ezâ1=zezâ1â enzâ1z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä»£å ¥ ðµ(ð§) =ð§eð§â1B(z)=zezâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ð¹ð(ð§)=ðµ(ð§)â eðð§â1ð§=(âðâ¥0ðµðð!)(âðâ¥1ððð§ðâ1ð!)=(âðâ¥0ðµðð!)(âðâ¥0ðð+1ð§ð(ð+1)!)Fn(z)=B(z)â enzâ1z=(âiâ¥0Bii!)(âiâ¥1niziâ1i!)=(âiâ¥0Bii!)(âiâ¥0ni+1zi(i+1)!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ç±äº ð¹ð(ð§) =âðâ¥0ðð(ð)ð!ð§ðFn(z)=âmâ¥0Sm(n)m!zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³ ðð(ð) =ð![ð§ð]ð¹ð(ð§)Sm(n)=m![zm]Fn(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ðÃð(ð)=ð![ð§ð]ð¹ð(ð§)=ð!ðâð=0ðµÃðð!â ððâð+1(ðâð+1)!=1ð+1ðâð=0(ð+1ð)ðµðððâð+1SÃm(n)=m![zm]Fn(z)=m!âi=0mBÃii!â nmâi+1(mâi+1)!=1m+1âi=0m(m+1i)Binmâi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

æ å¾è¯ï¼

åèå®ç°

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` |  ```text using ll = long long ; constexpr int MAXN = 10000 ; constexpr int mod = 1e9 \+ 7 ; ll B [ MAXN ]; // ä¼¯åªå©æ° ll C [ MAXN ][ MAXN ]; // ç»åæ° ll inv [ MAXN ]; // éå ï¼è®¡ç®ä¼¯åªå©æ°ï¼ void init () { // é¢å¤çç»åæ° for ( int i = 0 ; i < MAXN ; i ++ ) { C [ i ][ 0 ] = C [ i ][ i ] = 1 ; for ( int k = 1 ; k < i ; k ++ ) { C [ i ][ k ] = ( C [ i \- 1 ][ k ] % mod \+ C [ i \- 1 ][ k \- 1 ] % mod ) % mod ; } } // é¢å¤çéå  inv [ 1 ] = 1 ; for ( int i = 2 ; i < MAXN ; i ++ ) { inv [ i ] = ( mod \- mod / i ) * inv [ mod % i ] % mod ; } // é¢å¤çä¼¯åªå©æ° B [ 0 ] = 1 ; for ( int i = 1 ; i < MAXN ; i ++ ) { ll ans = 0 ; if ( i == MAXN \- 1 ) break ; for ( int k = 0 ; k < i ; k ++ ) { ans += C [ i \+ 1 ][ k ] * B [ k ]; ans %= mod ; } ans = ( ans * ( \- inv [ i \+ 1 ]) % mod \+ mod ) % mod ; B [ i ] = ans ; } } ```   
---|---  
  
* * *

> __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/bernoulli.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/bernoulli.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [ShaoChenHeng](https://github.com/ShaoChenHeng), [Aquistcev](https://github.com/Aquistcev), [c-forrest](https://github.com/c-forrest), [Great-designer](https://github.com/Great-designer), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [OkazakiYumemi](https://github.com/OkazakiYumemi), [Xeonacid](https://github.com/Xeonacid)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
