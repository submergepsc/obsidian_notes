# å¼ç¨ - OI Wiki

- Source: https://oi-wiki.org/lang/reference/

# å¼ç¨

> å£°æå ·ååéä¸ºå¼ç¨ï¼å³æ¢å­å¯¹è±¡æå½æ°çå«åï¼

å¼ç¨å¯ä»¥çææ¯ C++ å°è£ çéç©ºæéï¼å¯ä»¥ç¨æ¥ä¼ éå®ææåçå¯¹è±¡ï¼å¨å£°ææ¶å¿ é¡»æåå¯¹è±¡ï¼

å¼ç¨ä¸æ¯å¯¹è±¡ï¼å æ­¤ä¸å­å¨å¼ç¨çæ°ç»ãæ æ³è·åå¼ç¨çæéï¼ä¹ä¸å­å¨å¼ç¨çå¼ç¨ï¼

å¼ç¨ç±»åä¸å±äºå¯¹è±¡ç±»å

å¦ææ³è®©å¼ç¨è½å®æä¸è¬çå¤å¶ãèµå¼ç­æä½ï¼æ¯å¦ä½ä¸ºå®¹å¨å ç´ ï¼åéè¦ [`reference_wrapper`](https://zh.cppreference.com/w/cpp/utility/functional/reference_wrapper)ï¼éå¸¸ç»´æ¤ä¸ä¸ªéç©ºæéå®ç°ï¼

å¼ç¨ä¸»è¦åä¸ºä¸¤ç§ï¼å·¦å¼å¼ç¨åå³å¼å¼ç¨ï¼

å·¦å¼åå³å¼

å¯¹å·¦å¼åå³å¼çè®²è§£ï¼è¯·åè [å¼ç±»å«](../value-category/) é¡µé¢ï¼

## å·¦å¼å¼ç¨ T&

éå¸¸æä»¬ä¼æ¥è§¦å°çå¼ç¨ä¸ºå·¦å¼å¼ç¨ï¼å³ç»å®å°å·¦å¼çå¼ç¨ï¼åæ¶ `const` éå®çå·¦å¼å¼ç¨å¯ä»¥ç»å®å³å¼ï¼ä»¥ä¸æ¯æ¥èª [åèæå](https://zh.cppreference.com/w/cpp/language/reference) çä¸æ®µç¤ºä¾ä»£ç ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text #include <iostream> #include <string> int main () { std :: string s = "Ex" ; std :: string & r1 = s ; const std :: string & r2 = s ; r1 += "ample" ; // ä¿®æ¹ r1ï¼å³ä¿®æ¹äº s // r2 += "!"; // éè¯¯ï¼ä¸è½éè¿å° const çå¼ç¨ä¿®æ¹ std :: cout << r2 << '\n' ; // æå° r2ï¼è®¿é®äºsï¼è¾åº "Example" } ```   
---|---  
  
å·¦å¼å¼ç¨æå¸¸ç¨çå°æ¹æ¯å½æ°åæ°ï¼ç¨äºé¿å ä¸éè¦çæ·è´ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text #include <iostream> #include <string> // åæ°ä¸­ç s æ¯å¼ç¨ï¼å¨è°ç¨å½æ°æ¶ä¸ä¼åçæ·è´ char & char_number ( std :: string & s , std :: size_t n ) { s += s ; // 's' ä¸ main() ç 'str' // æ¯åä¸å¯¹è±¡ï¼æ­¤å¤è¿è¯´æå·¦å¼ä¹æ¯å¯ä»¥æ¾å¨ç­å·å³ä¾§ç return s . at ( n ); // string::at() è¿å char çå¼ç¨ } int main () { std :: string str = "Test" ; char_number ( str , 1 ) = 'a' ; // å½æ°è¿åæ¯å·¦å¼ï¼å¯è¢«èµå¼ std :: cout << str << '\n' ; // æ­¤å¤è¾åº "TastTest" } ```   
---|---  
  
## å³å¼å¼ç¨ T&&ï¼C++ 11ï¼

å³å¼å¼ç¨æ¯ç»å®å°å³å¼çå¼ç¨ï¼ç¨äºç§»å¨å¯¹è±¡ï¼ä¹å¯ä»¥ç¨äº **å»¶é¿ä¸´æ¶å¯¹è±¡çå­æ** ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text #include <iostream> #include <string> using namespace std ; int main () { string s1 = "Test" ; // string&& r1 = s1; // éè¯¯ï¼ä¸è½ç»å®å°å·¦å¼ï¼éè¦ std::move æè static_cast const string & r2 = s1 \+ s1 ; // å¯è¡ï¼å°å¸¸éçå·¦å¼å¼ç¨å»¶é¿çå­æ // r2 += "Test"; // éè¯¯ï¼ä¸è½éè¿å°å¸¸éçå¼ç¨ä¿®æ¹ cout << r2 << '\n' ; string && r3 = s1 \+ s1 ; // å¯è¡ï¼å³å¼å¼ç¨å»¶é¿çå­æ r3 += "Test" ; cout << r3 << '\n' ; const string & r4 = r3 ; // å³å¼å¼ç¨å¯ä»¥è½¬æ¢å° const éå®çå·¦å¼ cout << r4 << '\n' ; string & r5 = r3 ; // å³å¼å¼ç¨å¯ä»¥è½¬æ¢å°å·¦å¼ cout << r5 << '\n' ; } ```   
---|---  
  
## æ¬åå¼ç¨

å½å¼ç¨æä»£çå¯¹è±¡å·²ç»éæ¯ï¼å¼ç¨å°±ä¼åææ¬åå¼ç¨ï¼è®¿é®æ¬åå¼ç¨è¿æ¯ä¸ç§æªå®ä¹è¡ä¸ºï¼å¯è½ä¼å¯¼è´ç¨åºå´©æºï¼

ä»¥ä¸ä¸ºå¸¸è§çæ¬åå¼ç¨çä¾å­ï¼

  * å¼ç¨å±é¨åé

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text #include <iostream> int & foo () { int a = 1 ; return a ; } int main () { int & b = foo (); std :: cout << b << std :: endl ; // æªå®ä¹è¡ä¸º } ```   
---|---  
  
  * è§£åé å¯¼è´çæ¬åå¼ç¨

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text #include <iostream> int main () { int * ptr = new int ( 10 ); int & ref = * ptr ; delete ptr ; std :: cout << ref << std :: endl ; // æªå®ä¹è¡ä¸º } ```   
---|---  
  
  * å å­éåé å¯¼è´çæ¬åå¼ç¨

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text #include <iostream> int main () { std :: string str = "hello" ; const char & ref = str . front (); str . append ( "world" ); // å¯è½ä¼éæ°åé å å­ï¼å¯¼è´ ref æåçå å­è¢«éæ¾ std :: cout << ref << std :: endl ; // æªå®ä¹è¡ä¸º } ```   
---|---  
  
ç±»ä¼¼ `std::vector`ï¼`std::unordered_map` ç­å®¹å¨çæå ¥æä½ï¼åæå¯è½å¯¼è´å å­éæ°åé ï¼

ä½¿ç¨å¼ç¨æ¶ï¼åºæ¶å»å ³æ³¨å¼ç¨æåçå¯¹è±¡ççå½å¨æï¼é¿å é ææ¬åå¼ç¨ï¼

éå¸¸éææ£æ¥å·¥å ·åè¯å¥½çä»£ç ä¹ æ¯è½è®©æä»¬é¿å æ¬åå¼ç¨çé®é¢ï¼

## å¼ç¨ç¸å ³çä¼åæå·§

### æ¶é¤éè½»éå¯¹è±¡å ¥åçæ·è´å¼é

å¸¸è§ç **éè½»éå¯¹è±¡** æï¼

  * å®¹å¨ `vector`ï¼`array`ï¼`map` ç­
  * `string`
  * å ¶ä»å®ç°äºæç»§æ¿äºèªå®ä¹æ·è´æé ãç§»å¨æé ç­ç¹æ®å½æ°çç±»å

èå¯¹ **è½»éå¯¹è±¡** ä½¿ç¨å¼ç¨ä¸è½å¸¦æ¥ä»»ä½å¥½å¤ï¼å¼ç¨ç±»åä½ä¸ºåæ°çç©ºé´å ç¨å¤§å°ï¼çè³å¯è½ä¼æ¯ç±»åæ¬èº«è¿å¤§ï¼

è¿å¯è½ä¼å¸¦æ¥äºçæ§è½è´æ ï¼åæ¶å¯è½ä¼é»æ­¢ç¼è¯å¨ä¼åï¼

ä»¥ä¸å±äº **è½»éå¯¹è±¡**

  * åºæ¬ç±»å `int`ï¼`float` ç­
  * è¾å°ç [èåä½ç±»å](https://zh.cppreference.com/w/cpp/language/aggregate_initialization)
  * æ ååºå®¹å¨çè¿­ä»£å¨

### å°å·¦å¼è½¬æ¢ä¸ºå³å¼

ä½¿ç¨ `std::move` [è½¬ç§»](../value-category/#stdmove) å¯¹è±¡çæææï¼è¿éå¸¸è§äºå±é¨åéä¹é´ï¼æåæ°ä¸å±é¨åéä¹é´ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text #include <iostream> #include <string> #include <vector> using namespace std ; string world ( string str ) { return std :: move ( str ) += " world!" ; } int main () { // 1 cout << world ( "hello" ) << '\n' ; vector < string > vec0 ; // 2 { string && size = to_string ( vec0 . size ()); size += ", " \+ to_string ( size . size ()); vec0 . emplace_back ( std :: move ( size )); } cout << vec0 . front (); } ```   
---|---  
  
ä½ä¸æ¯æææ¶åé½éè¦è¿ä¹åï¼æ¯å¦ [å½æ°è¿åå¼ä¼å](../value-category/#å¸¸è§è¯¯åº)ï¼

### å³å¼å»¶é¿ä¸´æ¶éçå½æ

ä»è¯­ä¹ä¸ï¼ä¸´æ¶éå¯è½ä¼å¸¦æ¥çé¢å¤çå¤å¶æç§»å¨ï¼å°½ç®¡å¤æ°æ åµä¸ç¼è¯å¨è½éè¿ [å¤å¶æ¶é¤](../value-category/#å¤å¶æ¶é¤) è¿è¡ä¼åï¼ä½å¼ç¨è½å¼ºå¶ç¼è¯å¨ä¸è¿è¡è¿äºå¤ä½æä½ï¼é¿å ä¸ç¡®å®æ§ï¼

## åèå å®¹

  1. [C++ è¯­è¨ææ¡£ââå¼ç¨å£°æ](https://zh.cppreference.com/w/cpp/language/reference)
  2. [C++ è¯­è¨ææ¡£ââå¼ç±»å«](https://zh.cppreference.com/w/cpp/language/value_category)
  3. [Does const ref lvalue to non-const func return value specifically reduce copies?](https://stackoverflow.com/questions/38909228/does-const-ref-lvalue-to-non-const-func-return-value-specifically-reduce-copies)

* * *

> __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/reference.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/reference.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[cmpute](https://github.com/cmpute), [Ir1d](https://github.com/Ir1d), [CoderOJ](https://github.com/CoderOJ), [ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [c0nstexpr](https://github.com/c0nstexpr), [Duodenum87](https://github.com/Duodenum87), [Enter-tainer](https://github.com/Enter-tainer), [mgt](mailto:i@margatroid.xyz), [ouuan](https://github.com/ouuan)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
