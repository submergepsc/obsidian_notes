# å¹³è¡¡æ  - OI Wiki

- Source: https://oi-wiki.org/lang/pb-ds/tree/

# å¹³è¡¡æ 

## `__gnu_pbds::tree`

éï¼[å®æ¹ææ¡£å°å](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/tree_based_containers.html)

```text 1 2 3 4 5 6 ``` |  ```text #include <ext/pb_ds/assoc_container.hpp> // å ä¸º tree å®ä¹å¨è¿é æä»¥éè¦å å«è¿ä¸ªå¤´æä»¶ #include <ext/pb_ds/tree_policy.hpp> using namespace __gnu_pbds ; __gnu_pbds :: tree < Key , Mapped , Cmp_Fn = std :: less < Key > , Tag = rb_tree_tag , Node_Update = null_tree_node_update , Allocator = std :: allocator < char >> ```   
---|---  
  
## æ¨¡æ¿å½¢å

  * `Key`: å¨å­çå ç´ ç±»åï¼å¦ææ³è¦å­å¨å¤ä¸ªç¸åç `Key` å ç´ ï¼åéè¦ä½¿ç¨ç±»ä¼¼äº `std::pair` å `struct` çæ¹æ³ï¼å¹¶é åä½¿ç¨ `lower_bound` å `upper_bound` æåå½æ°è¿è¡æ¥æ¾
  * `Mapped`: æ å°è§åï¼Mapped-Policyï¼ç±»åï¼å¦æè¦æç¤ºå ³èå®¹å¨æ¯ **éå** ï¼ç±»ä¼¼äºå­å¨å ç´ å¨ `std::set` ä¸­ï¼æ­¤å¤å¡«å ¥ `null_type`ï¼ä½çæ¬ `g++` æ­¤å¤ä¸º `null_mapped_type`ï¼å¦æè¦æç¤ºå ³èå®¹å¨æ¯ **å¸¦å¼çéå** ï¼ç±»ä¼¼äºå­å¨å ç´ å¨ `std::map` ä¸­ï¼æ­¤å¤å¡«å ¥ç±»ä¼¼äº `std::map<Key, Value>` ç `Value` ç±»å
  * `Cmp_Fn`: å ³é®å­æ¯è¾å½å­ï¼ä¾å¦ `std::less<Key>`
  * `Tag`: éæ©ä½¿ç¨ä½ç§åºå±æ°æ®ç»æç±»åï¼é»è®¤æ¯ `rb_tree_tag`ï¼`__gnu_pbds` æä¾ä¸åçä¸ç§å¹³è¡¡æ ï¼åå«æ¯ï¼
    * `rb_tree_tag`ï¼çº¢é»æ ï¼ä¸è¬ä½¿ç¨è¿ä¸ªï¼åä¸¤è çæ§è½ä¸è¬ä¸å¦çº¢é»æ 
    * `splay_tree_tag`ï¼splay æ 
    * `ov_tree_tag`ï¼æåºåéæ ï¼åªæ¯ä¸ä¸ªç± `vector` å®ç°çæåºç»æï¼ç±»ä¼¼äºæåºç `vector` æ¥å®ç°å¹³è¡¡æ ï¼æ§è½åå³äºæ°æ®æ³ä¸æ³å¡ä½ 
  * `Node_Update`ï¼ç¨äºæ´æ°èç¹çç­ç¥ï¼é»è®¤ä½¿ç¨ `null_node_update`ï¼è¥è¦ä½¿ç¨ `order_of_key` å `find_by_order` æ¹æ³ï¼éè¦ä½¿ç¨ `tree_order_statistics_node_update`
  * `Allocator`ï¼ç©ºé´åé å¨ç±»å

## æé æ¹å¼

```text 1 2 3 4 ``` |  ```text __gnu_pbds :: tree < std :: pair < int , int > , __gnu_pbds :: null_type , std :: less < std :: pair < int , int >> , __gnu_pbds :: rb_tree_tag , __gnu_pbds :: tree_order_statistics_node_update > trr ; ```   
---|---  
  
## æåå½æ°

  * `insert(x)`ï¼åæ ä¸­æå ¥ä¸ä¸ªå ç´ `x`ï¼è¿å `std::pair<point_iterator, bool>`ï¼å ¶ä¸­ç¬¬ä¸ä¸ªå ç´ ä»£è¡¨æå ¥ä½ç½®çè¿­ä»£å¨ï¼ç¬¬äºä¸ªå ç´ ä»£è¡¨æ¯å¦æå ¥æåï¼
  * `erase(x)`ï¼ä»æ ä¸­å é¤ä¸ä¸ªå ç´ /è¿­ä»£å¨ `x`ï¼å¦æ `x` æ¯è¿­ä»£å¨ï¼åè¿åæå `x` ä¸ä¸ä¸ªçè¿­ä»£å¨ï¼å¦æ `x` æ¯ `end()` åè¿å `end()`ï¼ï¼å¦æ `x` æ¯ `Key`ï¼åè¿åæ¯å¦å é¤æåï¼å¦æä¸å­å¨åå é¤å¤±è´¥ï¼ï¼
  * `order_of_key(x)`ï¼è¿åä¸¥æ ¼å°äº `x` çå ç´ ä¸ªæ°ï¼ä»¥ `Cmp_Fn` ä½ä¸ºæ¯è¾é»è¾ï¼ï¼å³ä» 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å¼å§çæåï¼
  * `find_by_order(x)`ï¼è¿å `Cmp_Fn` æ¯è¾çæåæå¯¹åºå ç´ çè¿­ä»£å¨ï¼
  * `lower_bound(x)`ï¼è¿åç¬¬ä¸ä¸ªä¸å°äº `x` çå ç´ æå¯¹åºçè¿­ä»£å¨ï¼ä»¥ `Cmp_Fn` ä½ä¸ºæ¯è¾é»è¾ï¼ï¼
  * `upper_bound(x)`ï¼è¿åç¬¬ä¸ä¸ªä¸¥æ ¼å¤§äº `x` çå ç´ æå¯¹åºçè¿­ä»£å¨ï¼ä»¥ `Cmp_Fn` ä½ä¸ºæ¯è¾é»è¾ï¼ï¼
  * `join(x)`ï¼å° `x` æ å¹¶å ¥å½åæ ï¼`x` æ è¢«æ¸ ç©ºï¼å¿ é¡»ç¡®ä¿ä¸¤æ ç **æ¯è¾å½æ°** å **å ç´ ç±»å** ç¸åï¼ï¼
  * `split(x,b)`ï¼ä»¥ `Cmp_Fn` æ¯è¾ï¼å°äºç­äº `x` çå±äºå½åæ ï¼å ¶ä½çå±äº `b` æ ï¼
  * `empty()`ï¼è¿åæ¯å¦ä¸ºç©ºï¼
  * `size()`ï¼è¿åå¤§å°ï¼

æ³¨æ

`join(x)` å½æ°éè¦ä¿è¯å¹¶å ¥æ çé®çå¼åä¸è¢«å¹¶å ¥æ çé®çå¼å **ä¸ç¸äº¤** ï¼ä¹å°±æ¯è¯´å¹¶å ¥æ å ææå¼å¿ é¡»å ¨é¨å¤§äº/å°äºå½åæ å çææå¼ï¼ï¼å¦åä¼æåº `join_error` å¼å¸¸ï¼

å¦æè¦åå¹¶ä¸¤æ£µå¼åæäº¤éçæ ï¼éè¦å°ä¸æ£µæ çå ç´ ä¸ä¸æå ¥å°å¦ä¸æ£µæ ä¸­ï¼

## ç¤ºä¾

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text // Common Header Simple over C++11 #include <iostream> using namespace std ; using ll = long long ; using ull = unsigned long long ; using ld = long double ; using pii = pair < int , int > ; #include <ext/pb_ds/assoc_container.hpp> #include <ext/pb_ds/tree_policy.hpp> __gnu_pbds :: tree < pair < int , int > , __gnu_pbds :: null_type , less < pair < int , int >> , __gnu_pbds :: rb_tree_tag , __gnu_pbds :: tree_order_statistics_node_update > trr ; int main () { int cnt = 0 ; trr . insert ( make_pair ( 1 , cnt ++ )); trr . insert ( make_pair ( 5 , cnt ++ )); trr . insert ( make_pair ( 4 , cnt ++ )); trr . insert ( make_pair ( 3 , cnt ++ )); trr . insert ( make_pair ( 2 , cnt ++ )); // æ ä¸å ç´ {(1,0), (2,4), (3,3), (4,2), (5,1)} auto it = trr . lower_bound ( make_pair ( 2 , 0 )); trr . erase ( it ); // æ ä¸å ç´ {(1,0), (3,3), (4,2), (5,1)} // è¾åºæå 0 1 2 3 ä¸­çæå 1 çå ç´ ç first auto it2 = trr . find_by_order ( 1 ); cout << ( * it2 ). first << endl ; // è¾åºï¼3 // è¾åºå ¶æå int pos = trr . order_of_key ( * it2 ); cout << pos << endl ; // è¾åºï¼1 // æç § it2 åè£ trr decltype ( trr ) newtr ; trr . split ( * it2 , newtr ); for ( auto i = newtr . begin (); i != newtr . end (); ++ i ) { cout << ( * i ). first << ' ' ; // è¾åºï¼4 5 } cout << endl ; // å° newtr æ å¹¶å ¥ trr æ ï¼newtr æ è¢«æ¸ ç©ºï¼ trr . join ( newtr ); for ( auto i = trr . begin (); i != trr . end (); ++ i ) { cout << ( * i ). first << ' ' ; // è¾åºï¼1 3 4 5 } cout << endl ; cout << newtr . size () << endl ; // è¾åºï¼0 return 0 ; } ```   
---|---  
  
## åèèµæ

  * [Tree-Based Containers](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/tree_based_containers.html)
  * [`join` å½æ°å¨ GCC 14.1.0 ä¸­çå®ç°](https://gcc.gnu.org/onlinedocs/gcc-14.1.0/libstdc++/api/a18391_source.html#l00043)
  * [`erase` å½æ°å¨ GCC 14.1.0 ä¸­çå®ç°](https://gcc.gnu.org/onlinedocs/gcc-14.1.0/libstdc++/api/a18211_source.html#l00043)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/pb-ds/tree.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/pb-ds/tree.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[opsiff](https://github.com/opsiff), [Ir1d](https://github.com/Ir1d), [Xeonacid](https://github.com/Xeonacid), [Tiphereth-A](https://github.com/Tiphereth-A), [ksyx](https://github.com/ksyx), [c-forrest](https://github.com/c-forrest), [ChungZH](https://github.com/ChungZH), [HeRaNO](https://github.com/HeRaNO), [isdanni](https://github.com/isdanni), [Konano](https://github.com/Konano), [llleixx](https://github.com/llleixx), [sshwy](https://github.com/sshwy), [StableAgOH](https://github.com/StableAgOH), [zyzzyh](https://github.com/zyzzyh)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
