# å  - OI Wiki

- Source: https://oi-wiki.org/lang/pb-ds/pq/

# å 

## `__gnu_pbds::priority_queue`

éï¼[å®æ¹ææ¡£å°åââå¤æåº¦åå¸¸æ°æµè¯](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/pq_performance_tests.html#std_mod1)

```text 1 2 3 ``` |  ```text #include <ext/pb_ds/priority_queue.hpp> using namespace __gnu_pbds ; __gnu_pbds :: priority_queue < T , Compare , Tag , Allocator > ```   
---|---  
  
## æ¨¡æ¿å½¢å

  * `T`: å¨å­çå ç´ ç±»å
  * `Compare`: æä¾ä¸¥æ ¼çå¼±åºæ¯è¾ç±»å
  * `Tag`: æ¯ `__gnu_pbds` æä¾çä¸åçäºç§å ï¼Tag åæ°é»è®¤æ¯ `pairing_heap_tag` äºç§åå«æ¯ï¼
    * `pairing_heap_tag`ï¼é å¯¹å  å®æ¹ææ¡£è®¤ä¸ºå¨éåçå ç´ ï¼å¦èªå®ä¹ç»æä½/`std::string`/`pair`ï¼ä¸­ï¼é å¯¹å è¡¨ç°æå¥½
    * `binary_heap_tag`ï¼äºåå  å®æ¹ææ¡£è®¤ä¸ºå¨åçå ç´ ä¸­äºåå è¡¨ç°æå¥½ï¼ä¸è¿ç¬è æµè¯çè¡¨ç°å¹¶æ²¡æé£ä¹å¥½
    * `binomial_heap_tag`ï¼äºé¡¹å  äºé¡¹å å¨åå¹¶æä½çè¡¨ç°è¦ä¼äºäºåå ï¼ä½æ¯å ¶åå é¡¶å ç´ æä½çå¤æåº¦æ¯äºåå é«
    * `rc_binomial_heap_tag`ï¼åä½è®¡æ°äºé¡¹å 
    * `thin_heap_tag`ï¼é¤äºåå¹¶çå¤æåº¦é½å Fibonacci å ä¸æ ·çä¸ä¸ª tag
  * `Allocator`ï¼ç©ºé´é ç½®å¨ï¼ç±äº OI ä¸­å¾å°åºç°ï¼æ è¿éä¸åè®²è§£

ç±äºæ¬ç¯æç« åªæ¯æä¾ç»å­¦ä¹ ç®æ³ç«èµçåå­¦ä»¬ï¼æ å¯¹äºååä¸ª tag åªä¼ç®åçä»ç»å¤æåº¦ï¼ç¬¬ä¸ä¸ªä¼ä»ç»æåå½æ°åä½¿ç¨æ¹æ³ï¼

ç»ä½è æ¬æº Core i5 @3.1 GHz On macOS æµè¯å çåºç¡æä½ï¼ç»å GNU å®æ¹çå¤æåº¦æµè¯ï¼Dijkstra æµè¯ï¼é½è¡¨æï¼ è³å°å¯¹äº OIer æ¥è®²ï¼é¤äºé å¯¹å çå ¶ä»åä¸ª tag é½æ¯é¸¡èï¼è¦ä¹æ²¡ç¨ï¼è¦ä¹å¸¸æ°å¤§å°ä¸å¦ `std` çï¼ä¸æå¯è½é æ MLEï¼æ è¿éåªæ¨èç¨é»è®¤çé å¯¹å ï¼åæ ·ï¼é å¯¹å ä¹ä¼äº `algorithm` åºä¸­ç `make_heap()`ï¼

## æé æ¹å¼

è¦æ³¨æå½åç©ºé´å ä¸ºå `std` çç±»åç§°éå¤ï¼

```text 1 2 3 4 5 6 ``` |  ```text // __gnu_pbds::priority_queue<int>; // __gnu_pbds::priority_queue<int, greater<int>>; // __gnu_pbds::priority_queue<int, greater<int>, pairing_heap_tag>; __gnu_pbds :: priority_queue < int >:: point_iterator id ; // ç¹ç±»åè¿­ä»£å¨ // å¨ modify å push çæ¶åé½ä¼è¿åä¸ä¸ª point_iteratorï¼ä¸æä¼è¯¦ç»çè®²ä½¿ç¨æ¹æ³ id = q . push ( 1 ); ```   
---|---  
  
## æåå½æ°

  * `push()`: åå ä¸­åå ¥ä¸ä¸ªå ç´ ï¼è¿åè¯¥å ç´ ä½ç½®çè¿­ä»£å¨ï¼
  * `pop()`: å°å é¡¶å ç´ å¼¹åºï¼
  * `top()`: è¿åå é¡¶å ç´ ï¼
  * `size()` è¿åå ç´ ä¸ªæ°ï¼
  * `empty()` è¿åæ¯å¦éç©ºï¼
  * `modify(point_iterator, const key)`: æè¿­ä»£å¨ä½ç½®ç `key` ä¿®æ¹ä¸ºä¼ å ¥ç `key`ï¼å¹¶å¯¹åºå±å¨å­ç»æè¿è¡æåºï¼
  * `erase(point_iterator)`: æè¿­ä»£å¨ä½ç½®çé®å¼ä»å ä¸­æ¦é¤ï¼
  * `join(__gnu_pbds::priority_queue &other)`: æ `other` åå¹¶å° `*this` å¹¶æ `other` æ¸ ç©ºï¼

ä½¿ç¨ç tag å³å®äºæ¯ä¸ªæä½çæ¶é´å¤æåº¦ï¼

| push| pop| modify| erase| Join  
---|---|---|---|---|---  
`pairing_heap_tag`| ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`binary_heap_tag`| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`binomial_heap_tag`| æå Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`rc_binomial_heap_tag`| ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`thin_heap_tag`| ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| æå Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) åæ Î(logâ¡(ð))Î(logâ¡(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| Î(ð)Î(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
## ç¤ºä¾

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` |  ```text #include <algorithm> #include <cstdio> #include <ext/pb_ds/priority_queue.hpp> #include <iostream> using namespace __gnu_pbds ; // ç±äºé¢åOIer, æ¬æä»¥å¸¸ç¨å  : pairing_heap_tagä½ä¸ºèä¾ // ä¸ºäºæ´å¥½çé è¯»ä½éªï¼å®ä¹å®å¦ä¸ ï¼ using pair_heap = __gnu_pbds :: priority_queue < int > ; pair_heap q1 ; // å¤§æ ¹å , é å¯¹å  pair_heap q2 ; pair_heap :: point_iterator id ; // ä¸ä¸ªè¿­ä»£å¨ int main () { id = q1 . push ( 1 ); // å ä¸­å ç´ ï¼ [1]; for ( int i = 2 ; i <= 5 ; i ++ ) q1 . push ( i ); // å ä¸­å ç´ : [1, 2, 3, 4, 5]; std :: cout << q1 . top () << std :: endl ; // è¾åºç»æ : 5; q1 . pop (); // å ä¸­å ç´ : [1, 2, 3, 4]; id = q1 . push ( 10 ); // å ä¸­å ç´ : [1, 2, 3, 4, 10]; q1 . modify ( id , 1 ); // å ä¸­å ç´ : [1, 1, 2, 3, 4]; std :: cout << q1 . top () << std :: endl ; // è¾åºç»æ : 4; q1 . pop (); // å ä¸­å ç´ : [1, 1, 2, 3]; id = q1 . push ( 7 ); // å ä¸­å ç´ : [1, 1, 2, 3, 7]; q1 . erase ( id ); // å ä¸­å ç´ : [1, 1, 2, 3]; q2 . push ( 1 ), q2 . push ( 3 ), q2 . push ( 5 ); // q1ä¸­å ç´ : [1, 1, 2, 3], q2ä¸­å ç´ : [1, 3, 5]; q2 . join ( q1 ); // q1ä¸­æ å ç´ ï¼q2ä¸­å ç´ ï¼[1, 1, 1, 2, 3, 3, 5]; } ```   
---|---  
  
## __gnu_pbds è¿­ä»£å¨çå¤±æä¿è¯ï¼invalidation_guaranteeï¼

å¨ä¸è¿°ç¤ºä¾ä»¥åä¸äºå®è·µä¸­ï¼å¦ä½¿ç¨æ¬ç« ç pb-ds å æ¥ç¼ååæºæç­è·¯ç­ç®æ³ï¼ï¼å¸¸å¸¸éè¦ä¿å­å¹¶ä½¿ç¨å çè¿­ä»£å¨ï¼å¦ `__gnu_pbds::priority_queue<int>::point_iterator` ç­ï¼ï¼

å¯æ¯ä¾å¦å¯¹äº `__gnu_pbds::priority_queue` ä¸­ä¸åç Tag åæ°ï¼å ¶åºå±å®ç°å¹¶ä¸ç¸åï¼è¿­ä»£å¨çå¤±ææ¡ä»¶ä¹ä¸ä¸æ ·ï¼æ ¹æ®__gnu_pbds åºçè®¾è®¡ï¼ä»¥ä¸ä¸ç§ç±ä¸è³ä¸æ´¾ççæ åµï¼

  1. åºæ¬å¤±æä¿è¯ï¼basic_invalidation_guaranteeï¼ï¼å³ä¸ä¿®æ¹å®¹å¨æ¶ï¼ç¹ç±»åè¿­ä»£å¨ï¼point_iteratorï¼ãæéåå¼ç¨ï¼key/valueï¼**ä¿æ** ææï¼

  2. ç¹å¤±æä¿è¯ï¼point_invalidation_guaranteeï¼ï¼å³ **ä¿®æ¹** å®¹å¨åï¼ç¹ç±»åè¿­ä»£å¨ï¼point_iteratorï¼ãæéåå¼ç¨ï¼key/valueï¼åªè¦å¯¹åºå¨å®¹å¨ä¸­æ²¡è¢«å é¤ **ä¿æ** ææï¼

  3. èå´å¤±æä¿è¯ï¼range_invalidation_guaranteeï¼ï¼å³ **ä¿®æ¹** å®¹å¨åï¼é¤ï¼2ï¼çç¹æ§ä»¥å¤ï¼ä»»ä½èå´ç±»åçè¿­ä»£å¨ï¼å æ¬ `begin()` å `end()` çè¿åå¼ï¼æ¯æ­£ç¡®çï¼å ·æèå´å¤±æä¿è¯ç Tag æ `rb_tree_tag` å éç¨äº `__gnu_pbds::tree` ç `splay_tree_tag`ï¼ä»¥å éç¨äº `__gnu_pbds::trie` ç `pat_trie_tag`ï¼

ä»è¿è¡ä¸è¿°ä»£ç ä¸­çåºï¼é¤äº `binary_heap_tag` ä¸º `basic_invalidation_guarantee` å¨ä¿®æ¹åè¿­ä»£å¨ä¼å¤±æï¼å ¶ä½çåä¸º `point_invalidation_guarantee` å¯ä»¥å®ç°ä¿®æ¹åç¹ç±»åè¿­ä»£å¨ (point_iterator) ä¸å¤±æçéæ±ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text #include <iostream> using namespace std ; #include <ext/pb_ds/assoc_container.hpp> #include <ext/pb_ds/priority_queue.hpp> using namespace __gnu_pbds ; #include <cxxabi.h> template < typename T > void print_invalidation_guarantee () { using gute = __gnu_pbds :: container_traits < T >:: invalidation_guarantee ; cout << abi :: __cxa_demangle ( typeid ( gute ). name (), 0 , 0 , 0 ) << endl ; } int main () { using pairing = __gnu_pbds :: priority_queue < int , greater < int > , pairing_heap_tag > ; using binary = __gnu_pbds :: priority_queue < int , greater < int > , binary_heap_tag > ; using binomial = __gnu_pbds :: priority_queue < int , greater < int > , binomial_heap_tag > ; using rc_binomial = __gnu_pbds :: priority_queue < int , greater < int > , rc_binomial_heap_tag > ; using thin = __gnu_pbds :: priority_queue < int , greater < int > , thin_heap_tag > ; print_invalidation_guarantee < pairing > (); print_invalidation_guarantee < binary > (); print_invalidation_guarantee < binomial > (); print_invalidation_guarantee < rc_binomial > (); print_invalidation_guarantee < thin > (); return 0 ; } ```   
---|---  
  
* * *

> __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/pb-ds/pq.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/pb-ds/pq.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [Early0v0](https://github.com/Early0v0), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [GoodCoder666](https://github.com/GoodCoder666), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [opsiff](https://github.com/opsiff), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [abc1763613206](https://github.com/abc1763613206), [alphagocc](https://github.com/alphagocc), [Chrogeek](https://github.com/Chrogeek), [CoderOJ](https://github.com/CoderOJ), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [i-Yirannn](https://github.com/i-Yirannn), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [Planet6174](https://github.com/Planet6174), [r-value](https://github.com/r-value), [SukkaW](https://github.com/SukkaW), [WAAutoMaton](https://github.com/WAAutoMaton)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
