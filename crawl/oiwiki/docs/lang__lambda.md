# Lambda è¡¨è¾¾å¼ - OI Wiki

- Source: https://oi-wiki.org/lang/lambda/

# Lambda è¡¨è¾¾å¼

**æ³¨æ** ï¼èèå°ç®æ³ç«èµçå®é æ åµï¼æ¬æå°ä¸ä¼å ¨é¢ç ç©¶è¯­æ³ï¼åªä¼è®²è¿°å¨ç®æ³ç«èµä¸­å¯è½ä¼åºç¨å°çé¨åï¼

æ¬æè¯­æ³åç § **C++11** æ åï¼å ¶ä»é«çæ¬çæ åè¯­æ³è§æ åµæåå¹¶ä¼ç¹å«æ æ³¨ï¼

## Lambda è¡¨è¾¾å¼

Lambda è¡¨è¾¾å¼å æ°å­¦ä¸­ç ðÎ»![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¼ç®å¾åï¼ç´æ¥å¯¹åºäºå ¶ä¸­ç lambda æ½è±¡ï¼ç¼è¯å¨å¨ç¼è¯æ¶ä¼æ ¹æ®è¯­æ³çæä¸ä¸ªå¿åç [**å½æ°å¯¹è±¡**](../new/#å½æ°å¯¹è±¡)ï¼ä»¥æè·çåéä½ä¸ºå ¶æåï¼åæ°åå½æ°ä½ç¨äºå®ç° `operator()` éè½½ï¼

å½æ°å¯¹è±¡ï¼Function Objectï¼

å½æ°å¯¹è±¡æ¯ä¸ç§ç±»å¯¹è±¡ï¼ä¸è¬éè¿éè½½ `operator()` å®ç°ï¼æä»¥è½åå½æ°ä¸æ ·è°ç¨ï¼ç¸è¾äºä½¿ç¨æ®éçå½æ°ï¼å½æ°å¯¹è±¡æå¾å¤ä¼ç¹ï¼ä¾å¦å¯ä»¥ä¿å­ç¶æï¼å¯ä»¥ä½ä¸ºåæ°ä¼ éç»å ¶ä»å½æ°ç­ï¼

ä»¥ä¸æ¯ lambda çä¸ç§è¯­æ³ï¼

```text 1 ``` |  ```text [capture] (parameters) mutable -> return-type {statement} ```   
---|---  
  
Lambda è¡¨è¾¾å¼æ¬èº«æ¯ä¸ä¸ªç±»ï¼å±å¼åå¦ä»¥ä¸å½¢å¼ï¼

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text class Lambda_1 { private: Lambda_1() : capture-list(init-value) { } public: return-type operator()(parameters) const { statement } private: mutable capture-list }; ```   
---|---  
  
ç©ºç capture å¯ä»¥éå¼è½¬æ¢ä¸ºå½æ°æéï¼ä¾å¦ï¼

```text 1 ``` |  ```text void ( * f )( int , int ) = []( int , int ) -> void {}; ```   
---|---  
  
ä¸é¢æä»¬åå«å¯¹è¯­æ³ä¸­çåé¨åè¿è¡ä»ç»ï¼

### statement å½æ°ä½

å½æ°ä½ä¸æ®éå½æ°å½æ°ä½ç±»ä¼¼ï¼é¤äºè½è®¿é®åæ°åå ¨å±åéç­ï¼è¿å¯è®¿é® æè· çåéï¼

### capture æè·å­å¥

lambda ä»¥ capture å­å¥å¼å¤´ï¼å®æå®åªäºåéè¢«æè·ï¼æè·åè¡¨å¯ä¸ºç©ºï¼ææå®æè·æ¹å¼ï¼æ `&` ç¬¦å·åç¼çåééè¿ [å¼ç¨](../reference/) è®¿é®ï¼æ²¡æè¯¥åç¼çåééè¿å¼è®¿é®ï¼

æä»¬ä¹å¯ä»¥ä½¿ç¨é»è®¤æè·æ¨¡å¼ï¼æè· Lambda ä¸­æåçææåéï¼`&` è¡¨ç¤ºæè·å°çææåéé½éè¿å¼ç¨è®¿é®ï¼`=` è¡¨ç¤ºæè·å°çææåéé½éè¿å¼è®¿é®ï¼

å¨é»è®¤æè·ä¹åï¼ä»ç¶å¯ä»¥ä¸ºç¹å®çåé **æ¾å¼** æå®æè·æ¨¡å¼ï¼

å¦æéè¦å¼ç¨è®¿é®å¤é¨åé `a`ï¼å¹¶éè¿å¼è®¿é®å¤é¨åé `b`ï¼é£ä¹ä»¥ä¸æè·å­å¥é½å¯ä»¥åå°ï¼

  * `[&a, b]`
  * `[b, &a]`
  * `[&, b]`
  * `[b, &]`
  * `[=, &a]`

åæ¶æè·åè¡¨ä¹å¯ä»¥ç¨äºå£°æåéï¼ç±»åç±åå§åå¨æ¨å¯¼ï¼ç±»ä¼¼äºä½¿ç¨ `auto` å£°æåéï¼

ä»¥ä¸æ¯ä¸äºå¸¸è§çä¾å­ï¼

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int a = 0 ; auto f0 = []() { return a * 9 ; }; // Error, æ æ³è®¿é® 'a' auto f1 = [ a ]() { return a * 9 ; }; // OK, 'a' è¢«å¼ãæè·ã auto f2 = [ & a ]() { return a ++ ; }; // OK, 'a' è¢«å¼ç¨ãæè·ã auto f3 = [ v = a \+ 1 ]() { return v \+ 1 ; }; // OK, ä½¿ç¨åå§åå¨å£°æåé vï¼ç±»åä¸ a ç¸å // æ³¨æï¼ä½¿ç¨å¼ç¨æè·æ¶ï¼è¯·ä¿è¯è¢«è°ç¨æ¶ a æ²¡æè¢«éæ¯ auto b = f2 (); // f2 ä»æè·åè¡¨éè·å¾ a çå¼ï¼æ ééè¿åæ°ä¼ å ¥ a ```   
---|---  
  
#### generalized capture å¸¦åå§åçæè·ï¼C++14ï¼

èª C++14 èµ·ï¼capture ä¸ä» å¯ä»¥ç¨æ¥æè·å¤é¨åéï¼è¿å¯ç¨äºå£°ææ°çåéå¹¶åå§åï¼ä¾å¦ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text auto f1 = [ val = 520 ]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º intï¼åå§å¼ä¸º 520ï¼è¿åå¼ç±»å int auto f2 = [ val = 520L L ]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º long longï¼åå§å¼ä¸º 520ï¼è¿åå¼ç±»å long long auto f3 = [ val = "520" ]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º const char*ï¼åå§å¼ä¸º "520"ï¼è¿åå¼ç±»å const char* auto f4 = [ val = "520" s ]() { return val ; }; // OK, C++14 èµ·ï¼éè¦ using namespace std; æ using namespace std::literals; // å®ä¹ val ç±»åä¸º std::stringï¼åå§å¼ä¸º std::string("520")ï¼è¿åå¼ç±»å // std::string auto f5 = [ val = std :: string ( "520" )]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º std::stringï¼åå§å¼ä¸º std::string("520")ï¼è¿åå¼ç±»å // std::string auto f6 = [ val = std :: vector < int > ( 3 , 6 )]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º std::vector<int>ï¼å¤§å°ä¸º 3ï¼å ç´ å¡«å 6ï¼è¿åå¼ç±»å // std::vector<int> auto f7 = [ val = 520 ]() -> int { return val ; }; // OK, å®ä¹ val ç±»åä¸º intï¼åå§å¼ä¸º 520ï¼è¿åå¼ç±»å int auto f8 = [ val = 520 ]() -> long long { return val ; }; // OK, å®ä¹ val ç±»åä¸º intï¼åå§å¼ä¸º 520ï¼è¿åå¼ç±»å long long ```   
---|---  
  
å®ä¹æ°çåéä¸å¯ä»¥çç¥åå§å¼ï¼åéçç±»åç±åå§å¼çç±»åå³å®ï¼ç¸å½äºï¼

```text 1 ``` |  ```text auto val = init-value; ```   
---|---  
  
ä»¥ä¸æ¯éè¯¯çåæ³ï¼

```text 1 2 ``` |  ```text auto f = [ val ]() { return val ; }; // Error: 'val' was not declared in this // scope, identifier "val" is undefined ```   
---|---  
  
åå§åå¼ä¹å¯ä»¥æ¯å¤é¨åéï¼ä¾å¦ï¼

```text 1 2 3 ``` |  ```text int value = 520 ; auto f = [ val = value ]() { return val ; }; std :: cout << f (); // Output: 520 ```   
---|---  
  
`val` ä¹å¯ä»¥æ¯ä¸ä¸ªå¼ç¨ç±»åï¼å¯ä»¥å¼ç¨ä¸ä¸ªå¤é¨åéï¼éè¿è¿ç§æ¹å¼å¯ä»¥ä¸ºéè¿å¼ç¨æè·çå¤é¨åéåä¸ªå«åï¼ä¾å¦ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int value = 520 ; auto f = [ & val = value ]() { return val ; }; // OK, å®ä¹ val ç±»åä¸º int&ï¼è¿åå¼ç±»å intï¼ç¸å½äº int& val = value; std :: cout << f () << '\n' ; // Output: 520 value = 1314 ; std :: cout << f () << '\n' ; // Output: 1314 ```   
---|---  
  
æè·å¤é¨åéåå®ä¹æ°åéå¯ä»¥åæ¶ä½¿ç¨ï¼

å¦æä½ æ³å¨ Lambda è¡¨è¾¾å¼å ä¿®æ¹ capture ä¸­å®ä¹çæ°åéï¼éè¦ä½¿ç¨ `mutable` å ³é®å­ï¼å¦ææ¯å¼ç¨åä¸éè¦ï¼ä¾å¦ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text int value = 520 ; { auto f = [ val = value ]() mutable -> int { return val = 1314 ; }; // éè¦ mutable auto val_f = f (); std :: cout << value << ' ' << val_f << std :: endl ; // Output: 520 1314 } { auto f = [ & val = value ]() -> int { return val = 1314 ; }; // ä¸éè¦ mutable auto val_f = f (); std :: cout << value << ' ' << val_f << std :: endl ; // Output: 1314 1314 } ```   
---|---  
  
è¯¦è§ mutable å¯åè§èï¼

å¨ capture ä¸­å®ä¹çåéççå½å¨æè·é Lambda è¡¨è¾¾å¼çæ¥æ¶æ¹ï¼å¨ä»¥ä¸å ä¸ªç¤ºä¾ä¸­ä¸ºåé ðf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼å ä¸º Lambda æ¬èº«å ¶å®æ¯ä¸ä¸ªç±»ï¼capture ä¸­çææå å®¹é½æ¯è¿ä¸ªç±»ç `private` æååéï¼ä¾å¦ï¼

```text 1 2 3 4 5 6 7 ``` |  ```text int main () { auto f = [ val = 0 ]() mutable -> int { return ++ val ; }; // val è¢«æé ååå§å std :: cout << f () << '\n' ; // Output: 1 std :: cout << f () << '\n' ; // Output: 2 std :: cout << f () << '\n' ; // Output: 3 } // val è·é f è¢«éæ¯ ```   
---|---  
  
### parameters åæ°åè¡¨

å¤§å¤æ°æ åµä¸ç±»ä¼¼äºå½æ°çåæ°åè¡¨ï¼ä¾å¦ï¼

```text 1 2 3 ``` |  ```text int x [] = { 5 , 1 , 7 , 6 , 1 , 4 , 2 }; std :: sort ( x , x \+ 7 , []( int a , int b ) { return ( a > b ); }); for ( auto i : x ) std :: cout << i << " " ; ```   
---|---  
  
è¿å°æå°åº `x` æ°ç»ä»å¤§å°å°æåºåçç»æï¼

ç±äº **parameters åæ°åè¡¨** æ¯å¯éçï¼å¦æä¸å°åæ°ä¼ éç» lambdaï¼å¹¶ä¸å ¶å£°æä¸å å« mutableï¼ä¸æ²¡æåç½®è¿åå¼ç±»åï¼åå¯ä»¥çç¥ç©ºæ¬å·ï¼

ä½¿ç¨ `auto` å£°æçåæ°

**C++14** åï¼è¥åæ°ä½¿ç¨ `auto` å£°æç±»åï¼é£ä¹ä¼æé ä¸ä¸ª æ³å Lambda è¡¨è¾¾å¼ï¼

#### æ¾å¼å¯¹è±¡å½¢åï¼C++23ï¼

**C++23** èµ·ï¼[æ¾å¼å¯¹è±¡å½¢å](https://zh.cppreference.com/w/cpp/language/function#.E5.BD.A2.E5.8F.82.E5.88.97.E8.A1.A8) å¯ä»¥å¨ lambda çåæ°ä¸­ä½¿ç¨ï¼

```text 1 2 3 4 5 ``` |  ```text auto nth_fibonacci = []( this auto self , unsigned n ) -> unsigned { return n < 2 ? n : self ( n \- 1 ) \+ self ( n \- 2 ); }; cout << nth_fibonacci ( 10u ); ```   
---|---  
  
### mutable å¯åè§è

ä½¿å¾å½æ°ä½å¯ä»¥ä¿®æ¹éè¿å¼æè·çåéï¼

```text 1 2 3 4 5 6 ``` |  ```text int a = 0 ; auto by_value = [ a ]() mutable { ++ a ; }; auto by_ref = [ & a ] { ++ a ; }; by_value (); by_ref (); ```   
---|---  
  
å¨æ§è¡å® `by_value()` åï¼`by_value` çæè·æå `a` ä¸º 1ï¼ä½å¤é¨çåé `a` ä¾ç¶ä¸º 0ï¼ èå¨æ§è¡å® `by_ref()` åï¼å¤é¨ `a` çå¼åä¸º 1ï¼

### return-type è¿åç±»å

ç¨äºæå® lambda è¡¨è¾¾å¼çè¿åç±»åï¼å¦æçç¥ï¼åè¿åç±»åå°è¢«èªå¨æ¨æ­ï¼è¡ä¸ºä¸ç¨ `auto` å£°æè¿åå¼çå½æ°ä¸è´ï¼ï¼

å¤ä¸ª `return` è¯­å¥ä¸æ¨å¯¼ç±»åä¸ä¸è´æ¶ï¼å°äº§çç¼è¯éè¯¯ï¼

```text 1 2 3 4 5 6 7 8 ``` |  ```text auto lam = []( int a , int b ) -> int { return 0 ; }; auto x1 = []( int i ) { return i ; }; auto x2 = []( bool condition ) { if ( condition ) return 1 ; return 1.0 ; }; // Error, æ¨å¯¼ç±»åä¸ä¸è´ ```   
---|---  
  
### æ³å Lambdaï¼C++14ï¼

ä½¿ç¨ `auto` ä½ä¸ºåæ°ç±»åï¼å¯ä»¥æé æ³å lambdaï¼

```text 1 ``` |  ```text auto add = []( auto a , auto b ) { return a \+ b ; }; ```   
---|---  
  
å¨ [cpp insights](https://cppinsights.io) ä¸­å¯ä»¥è§å¯å°ç¼è¯å¨çæç `lambda` ç±»å®ä¹ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text class add_lambda { public : template < class T , class U > auto operator ()( T a , U b ) const { return a \+ b ; } }; add_lambda add {}; ```   
---|---  
  
`add` ä¸¤ä¸ªåæ°å£°æåä½¿ç¨äº `auto`ï¼å¯¹åºä¸º `add_lambda` ç±»ç `operator()` å½æ°æ¨¡æ¿çä¸¤ä¸ªæ¨¡æ¿åæ° `T` å `U`ï¼

### Lambda ä¸­çéå½

å æ¥çä¸ä¸ªç¼è¯å¤±è´¥çä¾å­ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text int n = 10 ; auto dfs = [ & ]( int i ) -> void { if ( i == n ) return ; else dfs ( i \+ 1 ); // Error: a variable declared with an auto type specifier // cannot appear in its own initializer }; ```   
---|---  
  
æä»¬è¿éå°è¯å¨æè·åè¡¨ä¸­æè· ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä½æ¯æä¸ä¸ªé®é¢ï¼ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç±»åä¸º `auto`ï¼è¦ç­å¾ ç­å·å³è¾¹çç±»åæ¨å¯¼å®æåæä¼æ¨å¯¼åº ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç±»åï¼è Lambda è¦æè· ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) å°±å¿ é¡»è¦ç¡®å® ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç±»ååæè½åå»ºå®çå¼ç¨åéï¼å¥½ï¼è¿ä¼é·å ¥äºä¸ä¸ªå¥å¨è¿ç¨ï¼

æä¹è§£å³è¿ä¸ªé®é¢å¢ï¼

  1. æ¾å¼æå® ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç±»åï¼å¯ä»¥ä½¿ç¨ `std::function` æ¿ä»£ï¼

ä¿®æ¹å¦ä¸ä»£ç ä¸ºï¼

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int n = 10 ; std :: function < void ( int ) > dfs = [ & ]( int i ) -> void { if ( i == n ) return ; else dfs ( i \+ 1 ); // OK }; dfs ( 1 ); ```   
---|---  
  
ä¸å»ºè®®ä½¿ç¨ [`std::function`](../new/#stdfunction) å®ç°çéå½

`std::function` çç±»åæ¦é¤éå¸¸éè¦åé é¢å¤å å­ï¼åæ¶é´æ¥è°ç¨å¸¦æ¥çå¯»åæä½ä¼è¿ä¸æ­¥éä½æ§è½ï¼

å¨ [Benchmark](https://quick-bench.com/q/U5qf_dHHKsSyVU83jmt0p_U541c) æµè¯ä¸­ï¼ä½¿ç¨ Clang 17 ç¼è¯å¨ï¼libc++ ä½ä¸ºæ ååºï¼`std::function` å®ç°æ¯ lambda å®ç°çéå½æ ¢äºçº¦ 2.5 åï¼

æµè¯ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` |  ```text #include <algorithm> #include <functional> #include <numeric> #include <random> using namespace std ; const auto & nums = [] { random_device rd ; mt19937 gen { rd ()}; array < unsigned , 32 > arr {}; std :: iota ( arr . begin (), arr . end (), 0u ); ranges :: shuffle ( arr , gen ); return arr ; }(); static void std_function_fib ( benchmark :: State & state ) { std :: function < int ( int ) > fib ; fib = [ & ]( int n ) { return n <= 2 ? 1 : fib ( n \- 1 ) \+ fib ( n \- 2 ); }; unsigned i = 0 ; for ( auto _ : state ) { auto res = fib ( nums [ i ]); benchmark :: DoNotOptimize ( res ); ++ i ; if ( i == nums . size ()) i = 0 ; } } BENCHMARK ( std_function_fib ); static void template_lambda_fib ( benchmark :: State & state ) { auto n_fibonacci = []( const auto & self , int n ) -> int { return n <= 2 ? 1 : self ( self , n \- 1 ) \+ self ( self , n \- 2 ); }; unsigned i = 0 ; for ( auto _ : state ) { auto res = n_fibonacci ( n_fibonacci , nums [ i ]); benchmark :: DoNotOptimize ( res ); ++ i ; if ( i == nums . size ()) i = 0 ; } } BENCHMARK ( template_lambda_fib ); ```   
---|---  
  
     1. ä¸éè¿æè·çæ¹å¼è·å ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼èæ¯éè¿å½æ°ä¼ åçæ¹å¼ï¼
ä¿®æ¹å¦ä¸ä»£ç ä¸ºï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text int n = 10 ; // åæ°åè¡¨ä¸­æåæ°ç±»åä¸º autoï¼åè¿ä¸ª Lambda ç±»ä¸­ç operator() // å½æ°å°è¢«å®ä¹ä¸ºæ¨¡æ¿å½æ°ï¼æ¨¡æ¿å½æ°å¯ä»¥å¨ç¨åè¢«è°ç¨æ¶åè¿è¡å®ä¾å auto dfs = [ & ]( auto & self , int i ) -> void // [&] åªä¼æè·ç¨å°çåéï¼æä»¥ä¸ä¼æè· auto dfs { if ( i == n ) return ; else self ( self , i \+ 1 ); // OK }; dfs ( dfs , 1 ); ```   
---|---  
  
`auto self`ã`auto& self` å `auto&& self` çåºå«ï¼

`auto& self` å `auto&& self` çè®ºä¸é½åªä¼ä½¿ç¨ 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªå­èï¼æéçå¤§å°ï¼ç¨ä½ä¼ åï¼ä¸ä¼åçå ¶ä»çæ·è´ï¼å ·ä½è¦çç¼è¯å¨å¯¹ Lambda çå®ç°æ¹å¼åå¯¹åºçä¼åï¼ èä½¿ç¨ `auto self` ä¼åçå¯¹è±¡æ·è´ï¼æ·è´çå¤§å°åå³äºæè·åè¡¨ä¸­çå ç´ ï¼å ä¸ºå®ä»¬é½æ¯è¿ä¸ª Lambda ç±»ä¸­çç§ææååéï¼

     1. å¯ä»¥éè¿æå¨å±å¼ Lambda ç±»ï¼æä½¿ç¨ç±»ä¼¼åæ³ï¼è¿æ ·å¯ä»¥ç´æ¥å£°æ ððð dfs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) çç±»åï¼
ä¿®æ¹å¦ä¸ä»£ç ä¸ºï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text int n = 10 ; class Lambda_1 { public : auto operator ()( int i ) const -> void { if ( i == n ) return ; else ( * this )( i \+ 1 ); // OK } explicit Lambda_1 ( int & __n ) : n ( __n ) {} private : int & n ; } dfs ( n ); dfs ( 1 ); ```   
---|---  
  
     1. å¦æ lambda æ²¡ææè·ä»»ä½åéï¼æä»¬ä¹å¯ä»¥å©ç¨å½æ°æéï¼

å¦æ lambda æ²¡ææè·ä»»ä½åéï¼é£ä¹å®å¯ä»¥éå¼è½¬æ¢ä¸ºå½æ°æéï¼åæ¶ lambda æ­¤æ¶ä¹å¯ä»¥å£°æä¸º `static`ï¼å½æ°æéç±»åä¹å¯ä»¥å£°æä¸º `static`ï¼å¦æ­¤ä¾èµï¼lambda å¯ä»¥ä¸éè¦æè·å°±è½è®¿é®å½æ°æéï¼ä»èå®ç°éå½ï¼

ç¤ºä¾

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text static unsigned ( * fptr )( unsigned ); static const auto lambda = []( const unsigned a ) { return a < 2 ? a : ( * fptr )( a \- 2 ) \+ ( * fptr )( a \- 1 ); }; static auto init = [] { fptr = \+ lambda ; // Or // fptr = static_cast<unsigned (*)(unsigned)>(lambda); return 0 ; }(); cout << lambda ( 10 ); ```   
---|---  
  

### Lambda è¡¨è¾¾å¼çåºç¨

#### ä½ä¸ºæ ååºç®æ³ç Predicateï¼è°è¯ï¼

ä»å¤§å°å°æåºï¼

```text 1 2 ``` |  ```text std :: vector < int > v = { 1 , 2 , 3 , 4 , 5 }; std :: sort ( v . begin (), v . end (), []( int a , int b ) { return a > b ; }); ```   
---|---  
  
ä½¿ç¨ [std::find_if](https://zh.cppreference.com/w/cpp/algorithm/find) æ¥æ¾ç¬¬ä¸ä¸ªå¤§äº 3 çå ç´ ï¼

```text 1 2 ``` |  ```text std :: vector < int > v = { 1 , 2 , 3 , 4 , 5 }; auto it = std :: find_if ( v . begin (), v . end (), []( int a ) { return a > 3 ; }); ```   
---|---  
  
#### æ§å¶ä¸­é´åéççå½å¨æ

å¨ç®æ³ç«èµä¸­ï¼æä»¬ä¼éå°è¿æ ·çåºæ¯ï¼ä¸ä¸ªåéçåå§åéè¦ä½¿ç¨ä¹åå£°æçåéï¼å ¶åå§åè¿ç¨åçæå ç¨ç©ºé´è¾å¤§çä¸­é´åéï¼

æä»¬å¸æè½å°½å¿«ææè¿äºä¸­é´åéï¼ä»¥éä½å å­æ¶èï¼æ­¤æ¶ï¼æä»¬å¯ä»¥ä½¿ç¨ lambda æ¥æ§å¶è¿äºä¸­é´åéççå½å¨æï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text void solution ( const vector < int >& input ) { int b = [ & ] { vector < int > large_objects ( input . size ()); int c = 0 ; for ( int i = 0 ; i < large_objects . size (); ++ i ) large_objects [ i ] = i \+ input [ i ]; for ( int i = 0 ; i < input . size (); ++ i ) c += large_objects [ input [ i ]]; return c ; }(); // ... } ```   
---|---  
  
ç¸è¾äºä½¿ç¨åä½ç¨åï¼lambda å¯ä»¥å è®¸æä»¬ä½¿ç¨è¿åå¼ï¼ä½¿å¾ä»£ç æ´å ç®æ´ï¼ç¸è¾äºå½æ°ï¼æä»¬ä¸éè¦é¢å¤èµ·ååå£°æè¢«æè·çåç§åæ°ï¼ä½¿å¾ä»£ç æ´å ç´§åï¼

## åèæç®

  * [cppreference-lambda](https://en.cppreference.com/w/cpp/language/lambda)
  * [Stackoverflow: Overhead with std::function](https://stackoverflow.com/a/33881130/11120338)

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/2/26 03:56:39ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/lambda.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/lambda.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [c0nstexpr](https://github.com/c0nstexpr), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [CoderOJ](https://github.com/CoderOJ), [Great-designer](https://github.com/Great-designer), [hly1204](https://github.com/hly1204), [huanhuanonly](https://github.com/huanhuanonly), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [ZnPdCo](https://github.com/ZnPdCo), [zyzzyh](https://github.com/zyzzyh)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
