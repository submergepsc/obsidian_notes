# äºè¿å¶éåæä½ - OI Wiki

- Source: https://oi-wiki.org/math/binary-set/

# äºè¿å¶éåæä½

åç½®ç¥è¯ï¼[ä½è¿ç®](../bit/#ä½è¿ç®)ã[æ´æ°ä¸ä½åºå](../bit/#æ´æ°ä¸ä½åºå)ï¼

ä¸ä¸ªæ°çäºè¿å¶è¡¨ç¤ºå¯ä»¥çä½æ¯ä¸ä¸ªéåï¼00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºä¸å¨éåä¸­ï¼11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤ºå¨éåä¸­ï¼ï¼æ¯å¦éå {1,3,4,8}{1,3,4,8}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥è¡¨ç¤ºæ (100011010)2(100011010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èå¯¹åºçä½è¿ç®ä¹å°±å¯ä»¥çä½æ¯å¯¹éåè¿è¡çæä½ï¼

æä½| éåè¡¨ç¤º| ä½è¿ç®è¡¨ç¤º  
---|---|---  
äº¤é| ð â©ðaâ©b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ðANDâ¡ðaANDâ¡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
å¹¶é| ð âªðaâªb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ðORâ¡ðaORâ¡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
è¡¥é| Â¯ðaÂ¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| NOTâ¡ðNOTâ¡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¨éä¸ºäºè¿å¶é½æ¯ 1ï¼  
å·®é| ð âðaâb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ðANDâ¡NOTâ¡ðaANDâ¡NOTâ¡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
å¯¹ç§°å·®| ðâ³ðaâ³b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ðXORâ¡ðaXORâ¡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
å¨è¿ä¸æ­¥ä»ç»éåçå­ééåæä½ä¹åï¼å çä½è¿ç®çæå ³åºç¨ä¾å­ï¼

### æ¨¡ 2 çå¹

ä¸ä¸ªæ°å¯¹ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°æ¬¡å¹åæ¨¡ï¼ç­ä»·äºåäºè¿å¶ä¸ä¸ä¸ªæ°çåè¥å¹²ä½ï¼ç­ä»·äºå ððð â1modâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¿è¡ä¸æä½ï¼

C++Python

```text 1 ``` |  ```text int modPowerOfTwo ( int x , int mod ) { return x & ( mod \- 1 ); } ```   
---|---  
  
```text 1 2 ``` |  ```text def modPowerOfTwo ( x , mod ): return x & ( mod \- 1 ) ```   
---|---  
  
äºæ¯å¯ä»¥ç¥éï¼22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°æ¬¡å¹å¯¹å®æ¬èº«åæ¨¡ï¼ç»æä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å¦æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¯ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°æ¬¡å¹ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æä½ç»æä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

äºå®ä¸ï¼å¯¹äºä¸ä¸ªæ­£æ´æ° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¼å° ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ç½®é¶ï¼å¹¶å°åç»­ä½æ°å ¨é¨ç½® 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð â1nâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸æä½ç­ä»·äºå æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæä½ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼

åæ­¤å¯ä»¥å¤æ­ä¸ä¸ªæ°æ¯ä¸æ¯ 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°æ¬¡å¹ï¼å½ä¸ä» å½ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çäºè¿å¶è¡¨ç¤ºåªæä¸ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸º 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéè´æ´æ°æ¬¡å¹ï¼

C++Python

```text 1 ``` |  ```text bool isPowerOfTwo ( int n ) { return n > 0 && ( n & ( n \- 1 )) == 0 ; } ```   
---|---  
  
```text 1 2 ``` |  ```text def isPowerOfTwo ( n ): return n > 0 and ( n & ( n \- 1 )) == 0 ```   
---|---  
  
### å­ééå

éåä¸ä¸ªäºè¿å¶æ°è¡¨ç¤ºçéåçå ¨é¨å­éï¼ç­ä»·äºæä¸¾äºè¿å¶æ°å¯¹åºæ©ç çææå­æ©ç ï¼

æ©ç æ¯ä¸ä¸²äºè¿å¶ç ï¼ç¨äºåæºç è¿è¡ä¸è¿ç®ï¼å¾å°å±è½æºç çè¥å¹²è¾å ¥ä½åçæ°æä½æ°ï¼

æ©ç å¯¹äºæºç å¯ä»¥èµ·å°é®ç½©çä½ç¨ï¼æ©ç ä¸­ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æå³çæºç çç¸åºä½å¾å°ä¿çï¼æ©ç ä¸­ç 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æå³çæºç çç¸åºä½è¿è¡ç½® 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æä½ï¼å°æ©ç çè¥å¹² 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½æ¹ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½å¯ä»¥å¾å°æ©ç çå­æ©ç ï¼æ©ç æ¬èº«ä¹æ¯èªå·±çå­æ©ç ï¼

ç»å®ä¸ä¸ªæ©ç  ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¸æææè¿­ä»£ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çææå­æ©ç  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯ä»¥èèåºäºä½è¿ç®æå·§çå®ç°ï¼

```text 1 2 3 4 5 6 ``` |  ```text // éåºéå m çéç©ºå­é int s = m ; while ( s > 0 ) { // s æ¯ m çä¸ä¸ªéç©ºå­é s = ( s \- 1 ) & m ; } ```   
---|---  
  
æè ä½¿ç¨æ´ç´§åç for è¯­å¥ï¼

```text 1 2 3 ``` |  ```text // éåºéå m çéç©ºå­é for ( int s = m ; s ; s = ( s \- 1 ) & m ) // s æ¯ m çä¸ä¸ªéç©ºå­é ```   
---|---  
  
è¿ä¸¤æ®µä»£ç é½ä¸ä¼å¤çç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­æ©ç ï¼è¦æ³å¤çç­äº 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­æ©ç å¯ä»¥ä½¿ç¨å ¶ä»åæ³ï¼ä¾å¦ï¼

```text 1 2 3 4 5 ``` |  ```text // éåºéå m çå­é for ( int s = m ;; s = ( s \- 1 ) & m ) { // s æ¯ m çä¸ä¸ªå­é if ( s == 0 ) break ; } ```   
---|---  
  
æ¥ä¸æ¥è¯æï¼ä¸é¢çä»£ç è®¿é®äºææ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­æ©ç ï¼æ²¡æéå¤ï¼å¹¶ä¸æéåºæåï¼

åè®¾æä¸ä¸ªå½åä½æ©ç  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¹¶ä¸æ³ç»§ç»­è®¿é®ä¸ä¸ä¸ªä½æ©ç ï¼å¨æ©ç  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­åå» 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ç­ä»·äºå é¤æ©ç  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æå³è¾¹çè®¾ç½®ä½ï¼å¹¶å°å ¶å³è¾¹çææä½åä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

ä¸ºäºä½¿ ð  â1sâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åä¸ºæ°çå­æ©ç ï¼éè¦å é¤æ©ç  ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­æªå å«çææé¢å¤ç 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼å¯ä»¥ä½¿ç¨ä½è¿ç® `(s - 1) & m` æ¥è¿è¡æ­¤ç§»é¤ï¼

è¿ä¸¤æ­¥æä½ç­ä»·äºåå²æ©ç  ð  â1sâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä»¥ç¡®å®ç®æ¯ä¸å¯ä»¥åå°çæå¤§å¼ï¼å³æéåºæåç ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åçä¸ä¸ä¸ªå­æ©ç ï¼

å æ­¤ï¼è¯¥ç®æ³æéåºçæè¯¥æ©ç çææå­æ©ç ï¼æ¯æ¬¡è¿­ä»£ä» æ§è¡ä¸¤ä¸ªæä½ï¼

ç¹æ®æ åµæ¯ ð  =0s=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨æ§è¡ ð  â1sâ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¹åå¾å° â1â1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ¶ä¸­ææä½é½ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¨ `(s - 1) & m` æä½ä¹åå°å¾å°æ°ç ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç­äº ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤ï¼å¦æå¾ªç¯ä¸ä»¥ ð  =0s=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ç»æï¼ç®æ³çå¾ªç¯å°æ æ³ç»æ­¢ï¼

ä½¿ç¨ popcount(ð)popcount(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) è¡¨ç¤º ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) äºè¿å¶ä¸­ 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çä¸ªæ°ï¼ç¨è¿ç§æ¹æ³å¯ä»¥å¨ ð(2popcount(ð))O(2popcount(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çæ¶é´å¤æåº¦å éåéå ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå­éï¼

### éåæææ©ç çå­æ©ç 

å¨ä½¿ç¨ç¶å DP çé®é¢ä¸­ï¼ææ¶ä¼å¸æå¯¹äºæ¯ä¸ªæ©ç ï¼éåæ©ç çææå­æ©ç ï¼

```text 1 2 3 4 ``` |  ```text for ( int m = 0 ; m < ( 1 << n ); ++ m ) // éåºéå m çéç©ºå­é for ( int s = m ; s ; s = ( s \- 1 ) & m ) // s æ¯ m çä¸ä¸ªéç©ºå­é ```   
---|---  
  
è¿æ ·åå¯ä»¥éåå¤§å°ä¸º ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çéåçæ¯ä¸ªå­éçå­éï¼

æ¥ä¸æ¥è¯æï¼è¯¥æä½çæ¶é´å¤æåº¦ä¸º ð(3ð)O(3n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ºæ©ç æ»å ±çä½æ°ï¼å³éåä¸­å ç´ çæ»æ°ï¼

èèç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼å³éåä¸­ç¬¬ ði![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå ç´ ï¼æä¸ç§æ åµï¼

  * å¨æ©ç  ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å æ­¤å¨å­æ©ç  ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å ç´ ä¸å¨å¤§å°å­éä¸­ï¼
  * å¨ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½å¨ ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­ä¸º 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å ç´ åªå¨å¤§å­éä¸­ï¼ä¸å¨å°å­éä¸­ï¼
  * å¨ ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ð s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸­åä¸º 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å³å ç´ åæ¶å¨å¤§å°å­éä¸­ï¼

æ»å ±æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä½ï¼å æ­¤æ 3ð3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¸åçç»åï¼

è¿æä¸ç§è¯ææ¹æ³æ¯ï¼

å¦ææ©ç  ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å ·æ ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ª 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹å®æ 2ð2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­æ©ç ï¼å¯¹äºç»å®ç ðk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å¯¹åºæ (ðð)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ©ç  ðm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼é£ä¹æææ©ç çæ»æ°ä¸ºï¼

ðâð=0(ðð)2ðâk=0n(nk)2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

ä¸é¢çåç­äºä½¿ç¨äºé¡¹å¼å®çå¯¹ (1 +2)ð(1+2)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çå±å¼ï¼å æ­¤æ 3ð3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªä¸åçç»åï¼

### åèèµæ

**æ¬é¡µé¢ä¸»è¦è¯èªåæ[ÐÐµÑÐµÐ±Ð¾Ñ Ð²ÑÐµÑ Ð¿Ð¾Ð´Ð¼Ð°ÑÐ¾Ðº Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¼Ð°ÑÐºÐ¸](http://e-maxx.ru/algo/all_submasks) ä¸å ¶è±æç¿»è¯ç [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html)ï¼å ¶ä¸­ä¿æççæåè®®ä¸º Public Domain + Leave a Linkï¼è±æççæåè®®ä¸º CC-BY-SA 4.0ï¼**

### ä¹ é¢

  * [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
  * [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
  * [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
  * [UVa 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
  * [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/27 12:26:08ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/binary-set.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/math/binary-set.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [aofall](https://github.com/aofall), [arielherself](https://github.com/arielherself), [c-forrest](https://github.com/c-forrest), [gavinliu266](https://github.com/gavinliu266), [Great-designer](https://github.com/Great-designer), [hhc0001](https://github.com/hhc0001), [jol888](https://github.com/jol888), [Menci](https://github.com/Menci), [shawlleyw](https://github.com/shawlleyw), [TOMWT-qwq](https://github.com/TOMWT-qwq), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
