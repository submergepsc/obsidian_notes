# å¾ªç¯ - OI Wiki

- Source: https://oi-wiki.org/lang/loop/

# å¾ªç¯

ææ¶ï¼æä»¬éè¦åä¸ä»¶äºå¾å¤éï¼ä¸ºäºä¸åè¿å¤éå¤çä»£ç ï¼æä»¬éè¦å¾ªç¯ï¼

ææ¶ï¼å¾ªç¯çæ¬¡æ°ä¸æ¯ä¸ä¸ªå¸¸éï¼é£ä¹æä»¬æ æ³å°ä»£ç éå¤å¤éï¼å¿ é¡»ä½¿ç¨å¾ªç¯ï¼

## for è¯­å¥

ä»¥ä¸æ¯ for è¯­å¥çç»æï¼

```text 1 2 3 ``` |  ```text for ( åå§å ; å¤æ­æ¡ä»¶ ; æ´æ° ) { å¾ªç¯ä½ ; } ```   
---|---  
  
æ§è¡é¡ºåºï¼

![](./images/for-loop.svg)

e.g. è¯»å ¥ n ä¸ªæ°ï¼

```text 1 2 3 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) { cin >> a [ i ]; } ```   
---|---  
  
for è¯­å¥çä¸ä¸ªé¨åä¸­ï¼ä»»ä½ä¸ä¸ªé¨åé½å¯ä»¥çç¥ï¼å ¶ä¸­ï¼è¥çç¥äºå¤æ­æ¡ä»¶ï¼ç¸å½äºå¤æ­æ¡ä»¶æ°¸è¿ä¸ºçï¼

## while è¯­å¥

ä»¥ä¸æ¯ while è¯­å¥çç»æï¼

```text 1 2 3 ``` |  ```text while ( å¤æ­æ¡ä»¶ ) { å¾ªç¯ä½ ; } ```   
---|---  
  
æ§è¡é¡ºåºï¼

![](./images/while-loop.svg)

e.g. éªè¯ 3x+1 çæ³ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text while ( x > 1 ) { if ( x % 2 == 1 ) { x = 3 * x \+ 1 ; } else { x = x / 2 ; } } ```   
---|---  
  
## do...while è¯­å¥

ä»¥ä¸æ¯ do...while è¯­å¥çç»æï¼

```text 1 2 3 ``` |  ```text do { å¾ªç¯ä½ ; } while ( å¤æ­æ¡ä»¶ ); ```   
---|---  
  
æ§è¡é¡ºåºï¼

![](./images/do-while-loop.svg)

ä¸ while è¯­å¥çåºå«å¨äºï¼do...while è¯­å¥æ¯å æ§è¡å¾ªç¯ä½åè¿è¡å¤æ­çï¼

e.g. æä¸¾æåï¼

```text 1 2 3 ``` |  ```text do { // do someting... } while ( next_permutation ( a \+ 1 , a \+ n \+ 1 )); ```   
---|---  
  
## ä¸ç§è¯­å¥çèç³»

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text // for è¯­å¥ for ( statement1 ; statement2 ; statement3 ) { statement4 ; } // while è¯­å¥ statement1 ; while ( statement2 ) { statement4 ; statement3 ; } ```   
---|---  
  
å¨ statement4 ä¸­æ²¡æ `continue` è¯­å¥ï¼è§ä¸æï¼çæ¶åæ¯ç­ä»·çï¼ä½æ¯ä¸é¢ä¸ç§æ¹æ³å¾å°ç¨å°ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text // while è¯­å¥ statement1 ; while ( statement2 ) { statement1 ; } // do...while è¯­å¥ do { statement1 ; } while ( statement2 ); ```   
---|---  
  
å¨ statement1 ä¸­æ²¡æ `continue` è¯­å¥çæ¶åè¿ä¸¤ç§æ¹å¼ä¹ä¹æ¯ç­ä»·çï¼

```text 1 2 3 4 5 6 7 ``` |  ```text while ( 1 ) { // do something... } for (;;) { // do something... } ```   
---|---  
  
è¿ä¸¤ç§æ¹å¼é½æ¯æ°¸è¿å¾ªç¯ä¸å»ï¼ï¼å¯ä»¥ä½¿ç¨ `break`ï¼è§ä¸æï¼éåºï¼ï¼

å¯ä»¥çåºï¼ä¸ç§è¯­å¥å¯ä»¥å½¼æ­¤ä»£æ¿ï¼ä½ä¸è¬æ¥è¯´ï¼è¯­å¥çéç¨éµå®ä»¥ä¸ååï¼

  1. å¾ªç¯è¿ç¨ä¸­æä¸ªåºå®çå¢å æ­¥éª¤ï¼æå¸¸è§çæ¯æä¸¾ï¼æ¶ï¼ä½¿ç¨ for è¯­å¥ï¼
  2. åªç¡®å®å¾ªç¯çç»æ­¢æ¡ä»¶æ¶ï¼ä½¿ç¨ while è¯­å¥ï¼
  3. ä½¿ç¨ while è¯­å¥æ¶ï¼è¥è¦å æ§è¡å¾ªç¯ä½åè¿è¡å¤æ­ï¼ä½¿ç¨ do...while è¯­å¥ï¼ä¸è¬å¾å°ç¨å°ï¼å¸¸ç¨åºæ¯æ¯ç¨æ·è¾å ¥ï¼

## break ä¸ continue è¯­å¥

break è¯­å¥çä½ç¨æ¯éåºå¾ªç¯ï¼

continue è¯­å¥çä½ç¨æ¯è·³è¿å¾ªç¯ä½çä½ä¸é¨åï¼ä¸é¢ä»¥ continue è¯­å¥å¨ do...while è¯­å¥ä¸­çä½¿ç¨ä¸ºä¾ï¼

```text 1 2 3 4 5 6 ``` |  ```text do { // do something... continue ; // ç­ä»·äº goto END; // do something... END :; } while ( statement ); ```   
---|---  
  
break ä¸ continue è¯­å¥åå¯å¨ä¸ç§å¾ªç¯è¯­å¥çå¾ªç¯ä½ä¸­ä½¿ç¨ï¼

ä¸è¬æ¥è¯´ï¼break ä¸ continue è¯­å¥ç¨äºè®©ä»£ç çé»è¾æ´å æ¸ æ°ï¼ä¾å¦ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // é»è¾è¾ä¸ºä¸æ¸ æ°ï¼å¤§æ¬å·å±æ¬¡å¤æ for ( int i = 1 ; i <= n ; ++ i ) { if ( i != x ) { for ( int j = 1 ; j <= n ; ++ j ) { if ( j != x ) { // do something... } } } } // é»è¾æ´å æ¸ æ°ï¼å¤§æ¬å·å±æ¬¡ç®åæäº for ( int i = 1 ; i <= n ; ++ i ) { if ( i == x ) continue ; for ( int j = 1 ; j <= n ; ++ j ) { if ( j == x ) continue ; // do something... } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text // for è¯­å¥å¤æ­æ¡ä»¶å¤æï¼æ²¡æä½ç°ãæä¸¾ãçæ¬è´¨ for ( int i = l ; i <= r && i % 10 != 0 ; ++ i ) { // do something... } // for è¯­å¥ç¨äºæä¸¾ï¼break ç¨äºãå°ä½æ¶ä¸ºæ­¢ã for ( int i = l ; i <= r ; ++ i ) { if ( i % 10 == 0 ) break ; // do something... } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // è¯­å¥éå¤ï¼é¡ºåºä¸èªç¶ statement1 ; while ( statement3 ) { statement2 ; statement1 ; } // æ²¡æéå¤è¯­å¥ï¼é¡ºåºèªç¶ while ( 1 ) { statement1 ; if ( ! statement3 ) break ; statement2 ; } ```   
---|---  
  
* * *

> __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/loop.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/loop.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [orzAtalod](https://github.com/orzAtalod), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [mcendu](https://github.com/mcendu), [Tiphereth-A](https://github.com/Tiphereth-A), [tLLWtG](https://github.com/tLLWtG)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
