# 斯特林数 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/stirling/

# 斯特林数

## 第二类斯特林数（Stirling Number）

为什么先介绍第二类斯特林数

虽然被称作「第二类」，第二类斯特林数却在斯特林的相关著作和具体数学中被首先描述，同时也比第一类斯特林数常用得多．

**第二类斯特林数** （斯特林子集数）{𝑛𝑘}{nk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也可记做 𝑆(𝑛,𝑘)S(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的元素，划分为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不区分的非空子集的方案数．

### 递推式

{𝑛𝑘}={𝑛−1𝑘−1}+𝑘{𝑛−1𝑘}{nk}={n−1k−1}+k{n−1k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

边界是 {𝑛0} =[𝑛 =0]{n0}=[n=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑用组合意义来证明．

我们插入一个新元素时，有两种方案：

  * 将新元素单独放入一个子集，有 {𝑛−1𝑘−1}{n−1k−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案；
  * 将新元素放入一个现有的非空子集，有 𝑘{𝑛−1𝑘}k{n−1k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案．

根据加法原理，将两式相加即可得到递推式．

### 通项公式

{𝑛𝑚}=𝑚∑𝑖=0(−1)𝑚−𝑖𝑖𝑛𝑖!(𝑚−𝑖)!{nm}=∑i=0m(−1)m−iini!(m−i)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用容斥原理证明该公式．设将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的元素，划分到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的集合（允许空集）的方案数为 𝐺𝑖Gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的元素，划分到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的非空集合（不允许空集）的方案数为 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显然

𝐺𝑖=𝑖𝑛𝐺𝑖=𝑖∑𝑗=0(𝑖𝑗)𝐹𝑗Gi=inGi=∑j=0i(ij)Fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据二项式反演

𝐹𝑖=𝑖∑𝑗=0(−1)𝑖−𝑗(𝑖𝑗)𝐺𝑗=𝑖∑𝑗=0(−1)𝑖−𝑗(𝑖𝑗)𝑗𝑛=𝑖∑𝑗=0𝑖!(−1)𝑖−𝑗𝑗𝑛𝑗!(𝑖−𝑗)!Fi=∑j=0i(−1)i−j(ij)Gj=∑j=0i(−1)i−j(ij)jn=∑j=0ii!(−1)i−jjnj!(i−j)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 {𝑛𝑖}{ni}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的关系．第二类斯特林数要求集合之间互不区分，因此 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 正好就是 {𝑛𝑖}{ni}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑖!i!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍．于是

{𝑛𝑚}=𝐹𝑚𝑚!=𝑚∑𝑖=0(−1)𝑚−𝑖𝑖𝑛𝑖!(𝑚−𝑖)!{nm}=Fmm!=∑i=0m(−1)m−iini!(m−i)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 同一行第二类斯特林数的计算

「同一行」的第二类斯特林数指的是，有着不同的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相同的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一系列 {𝑛𝑖}{ni}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求出同一行的所有第二类斯特林数，就是对 𝑖 =0..𝑛i=0..n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出了将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素划分为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非空集的方案数．

根据上面给出的通项公式，卷积计算即可．该做法的时间复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面的代码使用了名为 `poly` 的多项式类，仅供参考．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 ``` |  ```text #ifndef _FEISTDLIB_POLY_ #define _FEISTDLIB_POLY_ /* * This file is part of the fstdlib project. * Version: Build v0.0.2 * You can check for details at https://github.com/FNatsuka/fstdlib */ #include <algorithm> #include <cmath> #include <cstdio> #include <vector> namespace fstdlib { using ll = long long ; int mod = 998244353 , grt = 3 ; class poly { private : std :: vector < int > data ; void out ( void ) { for ( int i = 0 ; i < ( int ) data . size (); ++ i ) printf ( "%d " , data [ i ]); puts ( "" ); } public : poly ( std :: size_t len = std :: size_t ( 0 )) { data = std :: vector < int > ( len ); } poly ( const std :: vector < int > & b ) { data = b ; } poly ( const poly & b ) { data = b . data ; } void resize ( std :: size_t len , int val = 0 ) { data . resize ( len , val ); } std :: size_t size ( void ) const { return data . size (); } void clear ( void ) { data . clear (); } #if __cplusplus >= 201103L void shrink_to_fit ( void ) { data . shrink_to_fit (); } #endif int & operator []( std :: size_t b ) { return data [ b ]; } const int & operator []( std :: size_t b ) const { return data [ b ]; } poly operator * ( const poly & h ) const ; poly operator *= ( const poly & h ); poly operator * ( const int & h ) const ; poly operator *= ( const int & h ); poly operator \+ ( const poly & h ) const ; poly operator += ( const poly & h ); poly operator \- ( const poly & h ) const ; poly operator -= ( const poly & h ); poly operator << ( const std :: size_t & b ) const ; poly operator <<= ( const std :: size_t & b ); poly operator >> ( const std :: size_t & b ) const ; poly operator >>= ( const std :: size_t & b ); poly operator / ( const int & h ) const ; poly operator /= ( const int & h ); poly operator == ( const poly & h ) const ; poly operator != ( const poly & h ) const ; poly operator \+ ( const int & h ) const ; poly operator += ( const int & h ); poly inv ( void ) const ; poly inv ( const int & h ) const ; friend poly sqrt ( const poly & h ); friend poly log ( const poly & h ); friend poly exp ( const poly & h ); }; int qpow ( int a , int b , int p = mod ) { int res = 1 ; while ( b ) { if ( b & 1 ) res = ( ll ) res * a % p ; a = ( ll ) a * a % p , b >>= 1 ; } return res ; } std :: vector < int > rev ; void dft_for_module ( std :: vector < int > & f , int n , int b ) { static std :: vector < int > w ; w . resize ( n ); for ( int i = 0 ; i < n ; ++ i ) if ( i < rev [ i ]) std :: swap ( f [ i ], f [ rev [ i ]]); for ( int i = 2 ; i <= n ; i <<= 1 ) { w [ 0 ] = 1 , w [ 1 ] = qpow ( grt , ( mod \- 1 ) / i ); if ( b == -1 ) w [ 1 ] = qpow ( w [ 1 ], mod \- 2 ); for ( int j = 2 ; j < i / 2 ; ++ j ) w [ j ] = ( ll ) w [ j \- 1 ] * w [ 1 ] % mod ; for ( int j = 0 ; j < n ; j += i ) for ( int k = 0 ; k < i / 2 ; ++ k ) { int p = f [ j \+ k ], q = ( ll ) f [ j \+ k \+ i / 2 ] * w [ k ] % mod ; f [ j \+ k ] = ( p \+ q ) % mod , f [ j \+ k \+ i / 2 ] = ( p \- q \+ mod ) % mod ; } } } poly poly :: operator * ( const poly & h ) const { int N = 1 ; while ( N < ( int )( size () \+ h . size () \- 1 )) N <<= 1 ; std :: vector < int > f ( this -> data ), g ( h . data ); f . resize ( N ), g . resize ( N ); rev . resize ( N ); for ( int i = 0 ; i < N ; ++ i ) rev [ i ] = ( rev [ i >> 1 ] >> 1 ) | ( i & 1 ? N >> 1 : 0 ); dft_for_module ( f , N , 1 ), dft_for_module ( g , N , 1 ); for ( int i = 0 ; i < N ; ++ i ) f [ i ] = ( ll ) f [ i ] * g [ i ] % mod ; dft_for_module ( f , N , -1 ), f . resize ( size () \+ h . size () \- 1 ); for ( int i = 0 , inv = qpow ( N , mod \- 2 ); i < ( int ) f . size (); ++ i ) f [ i ] = ( ll ) f [ i ] * inv % mod ; return f ; } poly poly :: operator *= ( const poly & h ) { return * this = * this * h ; } poly poly :: operator * ( const int & h ) const { std :: vector < int > f ( this -> data ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = ( ll ) f [ i ] * h % mod ; return f ; } poly poly :: operator *= ( const int & h ) { for ( int i = 0 ; i < ( int ) size (); ++ i ) data [ i ] = ( ll ) data [ i ] * h % mod ; return * this ; } poly poly :: operator \+ ( const poly & h ) const { std :: vector < int > f ( this -> data ); if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \+ h [ i ]) % mod ; return f ; } poly poly :: operator += ( const poly & h ) { std :: vector < int > & f = this -> data ; if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \+ h [ i ]) % mod ; return f ; } poly poly :: operator \- ( const poly & h ) const { std :: vector < int > f ( this -> data ); if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \- h [ i ] \+ mod ) % mod ; return f ; } poly poly :: operator -= ( const poly & h ) { std :: vector < int > & f = this -> data ; if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \- h [ i ] \+ mod ) % mod ; return f ; } poly poly :: operator << ( const std :: size_t & b ) const { std :: vector < int > f ( size () \+ b ); for ( int i = 0 ; i < ( int ) size (); ++ i ) f [ i \+ b ] = data [ i ]; return f ; } poly poly :: operator <<= ( const std :: size_t & b ) { return * this = ( * this ) << b ; } poly poly :: operator >> ( const std :: size_t & b ) const { std :: vector < int > f ( size () \- b ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = data [ i \+ b ]; return f ; } poly poly :: operator >>= ( const std :: size_t & b ) { return * this = ( * this ) >> b ; } poly poly :: operator / ( const int & h ) const { std :: vector < int > f ( this -> data ); int inv = qpow ( h , mod \- 2 ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = ( ll ) f [ i ] * inv % mod ; return f ; } poly poly :: operator /= ( const int & h ) { int inv = qpow ( h , mod \- 2 ); for ( int i = 0 ; i < ( int ) data . size (); ++ i ) data [ i ] = ( ll ) data [ i ] * inv % mod ; return * this ; } poly poly :: inv ( void ) const { int N = 1 ; while ( N < ( int )( size () \+ size () \- 1 )) N <<= 1 ; std :: vector < int > f ( N ), g ( N ), d ( this -> data ); d . resize ( N ), f [ 0 ] = qpow ( d [ 0 ], mod \- 2 ); for ( int w = 2 ; w < N ; w <<= 1 ) { for ( int i = 0 ; i < w ; ++ i ) g [ i ] = d [ i ]; rev . resize ( w << 1 ); for ( int i = 0 ; i < w * 2 ; ++ i ) rev [ i ] = ( rev [ i >> 1 ] >> 1 ) | ( i & 1 ? w : 0 ); dft_for_module ( f , w << 1 , 1 ), dft_for_module ( g , w << 1 , 1 ); for ( int i = 0 ; i < w * 2 ; ++ i ) f [ i ] = ( ll ) f [ i ] * ( 2 \+ mod \- ( ll ) f [ i ] * g [ i ] % mod ) % mod ; dft_for_module ( f , w << 1 , -1 ); for ( int i = 0 , inv = qpow ( w << 1 , mod \- 2 ); i < w ; ++ i ) f [ i ] = ( ll ) f [ i ] * inv % mod ; for ( int i = w ; i < w * 2 ; ++ i ) f [ i ] = 0 ; } f . resize ( size ()); return f ; } poly poly :: operator == ( const poly & h ) const { if ( size () != h . size ()) return 0 ; for ( int i = 0 ; i < ( int ) size (); ++ i ) if ( data [ i ] != h [ i ]) return 0 ; return 1 ; } poly poly :: operator != ( const poly & h ) const { if ( size () != h . size ()) return 1 ; for ( int i = 0 ; i < ( int ) size (); ++ i ) if ( data [ i ] != h [ i ]) return 1 ; return 0 ; } poly poly :: operator \+ ( const int & h ) const { poly f ( this -> data ); f [ 0 ] = ( f [ 0 ] \+ h ) % mod ; return f ; } poly poly :: operator += ( const int & h ) { return * this = ( * this ) \+ h ; } poly poly :: inv ( const int & h ) const { poly f ( * this ); f . resize ( h ); return f . inv (); } int modsqrt ( int h , int p = mod ) { return 1 ; } poly sqrt ( const poly & h ) { int N = 1 ; while ( N < ( int )( h . size () \+ h . size () \- 1 )) N <<= 1 ; poly f ( N ), g ( N ), d ( h ); d . resize ( N ), f [ 0 ] = modsqrt ( d [ 0 ]); for ( int w = 2 ; w < N ; w <<= 1 ) { g . resize ( w ); for ( int i = 0 ; i < w ; ++ i ) g [ i ] = d [ i ]; f = ( f \+ f . inv ( w ) * g ) / 2 ; f . resize ( w ); } f . resize ( h . size ()); return f ; } poly log ( const poly & h ) { poly f ( h ); for ( int i = 1 ; i < ( int ) f . size (); ++ i ) f [ i \- 1 ] = ( ll ) f [ i ] * i % mod ; f [ f . size () \- 1 ] = 0 , f = f * h . inv (), f . resize ( h . size ()); for ( int i = ( int ) f . size () \- 1 ; i > 0 ; \-- i ) f [ i ] = ( ll ) f [ i \- 1 ] * qpow ( i , mod \- 2 ) % mod ; f [ 0 ] = 0 ; return f ; } poly exp ( const poly & h ) { int N = 1 ; while ( N < ( int )( h . size () \+ h . size () \- 1 )) N <<= 1 ; poly f ( N ), g ( N ), d ( h ); f [ 0 ] = 1 , d . resize ( N ); for ( int w = 2 ; w < N ; w <<= 1 ) { f . resize ( w ), g . resize ( w ); for ( int i = 0 ; i < w ; ++ i ) g [ i ] = d [ i ]; f = f * ( g \+ 1 \- log ( f )); f . resize ( w ); } f . resize ( h . size ()); return f ; } struct comp { long double x , y ; comp ( long double _x = 0 , long double _y = 0 ) : x ( _x ), y ( _y ) {} comp operator * ( const comp & b ) const { return comp ( x * b . x \- y * b . y , x * b . y \+ y * b . x ); } comp operator \+ ( const comp & b ) const { return comp ( x \+ b . x , y \+ b . y ); } comp operator \- ( const comp & b ) const { return comp ( x \- b . x , y \- b . y ); } comp conj ( void ) { return comp ( x , \- y ); } }; const int EPS = 1e-9 ; template < typename FLOAT_T > FLOAT_T fabs ( const FLOAT_T & x ) { return x > 0 ? x : \- x ; } template < typename FLOAT_T > FLOAT_T sin ( const FLOAT_T & x , const long double & EPS = fstdlib :: EPS ) { FLOAT_T res = 0 , delt = x ; int d = 0 ; while ( fabs ( delt ) > EPS ) { res += delt , ++ d ; delt *= \- x * x / (( 2 * d ) * ( 2 * d \+ 1 )); } return res ; } template < typename FLOAT_T > FLOAT_T cos ( const FLOAT_T & x , const long double & EPS = fstdlib :: EPS ) { FLOAT_T res = 0 , delt = 1 ; int d = 0 ; while ( fabs ( delt ) > EPS ) { res += delt , ++ d ; delt *= \- x * x / (( 2 * d ) * ( 2 * d \- 1 )); } return res ; } const long double PI = std :: acos (( long double )( -1 )); void dft_for_complex ( std :: vector < comp > & f , int n , int b ) { static std :: vector < comp > w ; w . resize ( n ); for ( int i = 0 ; i < n ; ++ i ) if ( i < rev [ i ]) std :: swap ( f [ i ], f [ rev [ i ]]); for ( int i = 2 ; i <= n ; i <<= 1 ) { w [ 0 ] = comp ( 1 , 0 ), w [ 1 ] = comp ( cos ( 2 * PI / i ), b * sin ( 2 * PI / i )); for ( int j = 2 ; j < i / 2 ; ++ j ) w [ j ] = w [ j \- 1 ] * w [ 1 ]; for ( int j = 0 ; j < n ; j += i ) for ( int k = 0 ; k < i / 2 ; ++ k ) { comp p = f [ j \+ k ], q = f [ j \+ k \+ i / 2 ] * w [ k ]; f [ j \+ k ] = p \+ q , f [ j \+ k \+ i / 2 ] = p \- q ; } } } class arbitrary_module_poly { private : std :: vector < int > data ; int construct_element ( int D , ll x , ll y , ll z ) const { x %= mod , y %= mod , z %= mod ; return (( ll ) D * D * x % mod \+ ( ll ) D * y % mod \+ z ) % mod ; } public : int mod ; arbitrary_module_poly ( std :: size_t len = std :: size_t ( 0 ), int module_value = 1e9 \+ 7 ) { mod = module_value ; data = std :: vector < int > ( len ); } arbitrary_module_poly ( const std :: vector < int > & b , int module_value = 1e9 \+ 7 ) { mod = module_value ; data = b ; } arbitrary_module_poly ( const arbitrary_module_poly & b ) { mod = b . mod ; data = b . data ; } void resize ( std :: size_t len , const int & val = 0 ) { data . resize ( len , val ); } std :: size_t size ( void ) const { return data . size (); } void clear ( void ) { data . clear (); } #if __cplusplus >= 201103L void shrink_to_fit ( void ) { data . shrink_to_fit (); } #endif int & operator []( std :: size_t b ) { return data [ b ]; } const int & operator []( std :: size_t b ) const { return data [ b ]; } arbitrary_module_poly operator * ( const arbitrary_module_poly & h ) const ; arbitrary_module_poly operator *= ( const arbitrary_module_poly & h ); arbitrary_module_poly operator * ( const int & h ) const ; arbitrary_module_poly operator *= ( const int & h ); arbitrary_module_poly operator \+ ( const arbitrary_module_poly & h ) const ; arbitrary_module_poly operator += ( const arbitrary_module_poly & h ); arbitrary_module_poly operator \- ( const arbitrary_module_poly & h ) const ; arbitrary_module_poly operator -= ( const arbitrary_module_poly & h ); arbitrary_module_poly operator << ( const std :: size_t & b ) const ; arbitrary_module_poly operator <<= ( const std :: size_t & b ); arbitrary_module_poly operator >> ( const std :: size_t & b ) const ; arbitrary_module_poly operator >>= ( const std :: size_t & b ); arbitrary_module_poly operator / ( const int & h ) const ; arbitrary_module_poly operator /= ( const int & h ); arbitrary_module_poly operator == ( const arbitrary_module_poly & h ) const ; arbitrary_module_poly operator != ( const arbitrary_module_poly & h ) const ; arbitrary_module_poly inv ( void ) const ; arbitrary_module_poly inv ( const int & h ) const ; friend arbitrary_module_poly sqrt ( const arbitrary_module_poly & h ); friend arbitrary_module_poly log ( const arbitrary_module_poly & h ); }; arbitrary_module_poly arbitrary_module_poly :: operator * ( const arbitrary_module_poly & h ) const { int N = 1 ; while ( N < ( int )( size () \+ h . size () \- 1 )) N <<= 1 ; std :: vector < comp > f ( N ), g ( N ), p ( N ), q ( N ); const int D = std :: sqrt ( mod ); for ( int i = 0 ; i < ( int ) size (); ++ i ) f [ i ]. x = data [ i ] / D , f [ i ]. y = data [ i ] % D ; for ( int i = 0 ; i < ( int ) h . size (); ++ i ) g [ i ]. x = h [ i ] / D , g [ i ]. y = h [ i ] % D ; rev . resize ( N ); for ( int i = 0 ; i < N ; ++ i ) rev [ i ] = ( rev [ i >> 1 ] >> 1 ) | ( i & 1 ? N >> 1 : 0 ); dft_for_complex ( f , N , 1 ), dft_for_complex ( g , N , 1 ); for ( int i = 0 ; i < N ; ++ i ) { p [ i ] = ( f [ i ] \+ f [( N \- i ) % N ]. conj ()) * comp ( 0.50 , 0 ) * g [ i ]; q [ i ] = ( f [ i ] \- f [( N \- i ) % N ]. conj ()) * comp ( 0 , -0.5 ) * g [ i ]; } dft_for_complex ( p , N , -1 ), dft_for_complex ( q , N , -1 ); std :: vector < int > r ( size () \+ h . size () \- 1 ); for ( int i = 0 ; i < ( int ) r . size (); ++ i ) r [ i ] = construct_element ( D , p [ i ]. x / N \+ 0.5 , ( p [ i ]. y \+ q [ i ]. x ) / N \+ 0.5 , q [ i ]. y / N \+ 0.5 ); return arbitrary_module_poly ( r , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator *= ( const arbitrary_module_poly & h ) { return * this = * this * h ; } arbitrary_module_poly arbitrary_module_poly :: operator * ( const int & h ) const { std :: vector < int > f ( this -> data ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = ( ll ) f [ i ] * h % mod ; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator *= ( const int & h ) { for ( int i = 0 ; i < ( int ) size (); ++ i ) data [ i ] = ( ll ) data [ i ] * h % mod ; return * this ; } arbitrary_module_poly arbitrary_module_poly :: operator \+ ( const arbitrary_module_poly & h ) const { std :: vector < int > f ( this -> data ); if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \+ h [ i ]) % mod ; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator += ( const arbitrary_module_poly & h ) { if ( size () < h . size ()) resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) data [ i ] = ( data [ i ] \+ h [ i ]) % mod ; return * this ; } arbitrary_module_poly arbitrary_module_poly :: operator \- ( const arbitrary_module_poly & h ) const { std :: vector < int > f ( this -> data ); if ( f . size () < h . size ()) f . resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) f [ i ] = ( f [ i ] \+ mod \- h [ i ]) % mod ; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator -= ( const arbitrary_module_poly & h ) { if ( size () < h . size ()) resize ( h . size ()); for ( int i = 0 ; i < ( int ) h . size (); ++ i ) data [ i ] = ( data [ i ] \+ mod \- h [ i ]) % mod ; return * this ; } arbitrary_module_poly arbitrary_module_poly :: operator << ( const std :: size_t & b ) const { std :: vector < int > f ( size () \+ b ); for ( int i = 0 ; i < ( int ) size (); ++ i ) f [ i \+ b ] = data [ i ]; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator <<= ( const std :: size_t & b ) { return * this = ( * this ) << b ; } arbitrary_module_poly arbitrary_module_poly :: operator >> ( const std :: size_t & b ) const { std :: vector < int > f ( size () \- b ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = data [ i \+ b ]; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator >>= ( const std :: size_t & b ) { return * this = ( * this ) >> b ; } arbitrary_module_poly arbitrary_module_poly :: inv ( void ) const { int N = 1 ; while ( N < ( int )( size () \+ size () \- 1 )) N <<= 1 ; arbitrary_module_poly f ( 1 , mod ), g ( N , mod ), h ( * this ), f2 ( 1 , mod ); f [ 0 ] = qpow ( data [ 0 ], mod \- 2 , mod ), h . resize ( N ), f2 [ 0 ] = 2 ; for ( int w = 2 ; w < N ; w <<= 1 ) { g . resize ( w ); for ( int i = 0 ; i < w ; ++ i ) g [ i ] = h [ i ]; f = f * ( f * g \- f2 ) * ( mod \- 1 ); f . resize ( w ); } f . resize ( size ()); return f ; } arbitrary_module_poly arbitrary_module_poly :: inv ( const int & h ) const { arbitrary_module_poly f ( * this ); f . resize ( h ); return f . inv (); } arbitrary_module_poly arbitrary_module_poly :: operator / ( const int & h ) const { int inv = qpow ( h , mod \- 2 , mod ); std :: vector < int > f ( this -> data ); for ( int i = 0 ; i < ( int ) f . size (); ++ i ) f [ i ] = ( ll ) f [ i ] * inv % mod ; return arbitrary_module_poly ( f , mod ); } arbitrary_module_poly arbitrary_module_poly :: operator /= ( const int & h ) { int inv = qpow ( h , mod \- 2 , mod ); for ( int i = 0 ; i < ( int ) size (); ++ i ) data [ i ] = ( ll ) data [ i ] * inv % mod ; return * this ; } arbitrary_module_poly arbitrary_module_poly :: operator == ( const arbitrary_module_poly & h ) const { if ( size () != h . size () || mod != h . mod ) return 0 ; for ( int i = 0 ; i < ( int ) size (); ++ i ) if ( data [ i ] != h [ i ]) return 0 ; return 1 ; } arbitrary_module_poly arbitrary_module_poly :: operator != ( const arbitrary_module_poly & h ) const { if ( size () != h . size () || mod != h . mod ) return 1 ; for ( int i = 0 ; i < ( int ) size (); ++ i ) if ( data [ i ] != h [ i ]) return 1 ; return 0 ; } arbitrary_module_poly sqrt ( const arbitrary_module_poly & h ) { int N = 1 ; while ( N < ( int )( h . size () \+ h . size () \- 1 )) N <<= 1 ; arbitrary_module_poly f ( 1 , mod ), g ( N , mod ), d ( h ); f [ 0 ] = modsqrt ( h [ 0 ], mod ), d . resize ( N ); for ( int w = 2 ; w < N ; w <<= 1 ) { g . resize ( w ); for ( int i = 0 ; i < w ; ++ i ) g [ i ] = d [ i ]; f = ( f \+ f . inv ( w ) * g ) / 2 ; f . resize ( w ); } f . resize ( h . size ()); return f ; } arbitrary_module_poly log ( const arbitrary_module_poly & h ) { arbitrary_module_poly f ( h ); for ( int i = 1 ; i < ( int ) f . size (); ++ i ) f [ i \- 1 ] = ( ll ) f [ i ] * i % f . mod ; f [ f . size () \- 1 ] = 0 , f = f * h . inv (), f . resize ( h . size ()); for ( int i = ( int ) f . size () \- 1 ; i > 0 ; \-- i ) f [ i ] = ( ll ) f [ i \- 1 ] * qpow ( i , f . mod \- 2 , f . mod ) % f . mod ; f [ 0 ] = 0 ; return f ; } using m_poly = arbitrary_module_poly ; } // namespace fstdlib #endif ```   
---|---  
  
实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text int main () { scanf ( "%d" , & n ); fact [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) fact [ i ] = ( ll ) fact [ i \- 1 ] * i % mod ; exgcd ( fact [ n ], mod , ifact [ n ], ifact [ 0 ]), ifact [ n ] = ( ifact [ n ] % mod \+ mod ) % mod ; for ( int i = n \- 1 ; i >= 0 ; \-- i ) ifact [ i ] = ( ll ) ifact [ i \+ 1 ] * ( i \+ 1 ) % mod ; poly f ( n \+ 1 ), g ( n \+ 1 ); for ( int i = 0 ; i <= n ; ++ i ) g [ i ] = ( i & 1 ? mod \- 1l l : 1l l ) * ifact [ i ] % mod , f [ i ] = ( ll ) qpow ( i , n ) * ifact [ i ] % mod ; f *= g , f . resize ( n \+ 1 ); for ( int i = 0 ; i <= n ; ++ i ) printf ( "%d " , f [ i ]); return 0 ; } ```   
---|---  
  
### 同一列第二类斯特林数的计算

「同一列」的第二类斯特林数指的是，有着不同的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相同的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一系列 {𝑖𝑘}{ik}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求出同一列的所有第二类斯特林数，就是对 𝑖 =0..𝑛i=0..n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出了将 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素划分为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非空集的方案数．

利用指数型生成函数计算．

一个盒子装 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品且盒子非空的方案数是 [𝑖 >0][i>0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们可以写出它的指数型生成函数为 𝐹(𝑥) =+∞∑𝑖=1𝑥𝑖𝑖! =e𝑥 −1F(x)=∑i=1+∞xii!=ex−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．经过之前的学习，我们明白 𝐹𝑘(𝑥)Fk(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有标号物品放到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有标号盒子里的指数型生成函数，那么除掉 𝑘!k!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有标号物品放到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个无标号盒子里的指数型生成函数．

{𝑖𝑘} =[𝑥𝑖𝑖!]𝐹𝑘(𝑥)𝑘!{ik}=[xii!]Fk(x)k!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算多项式幂即可．

另外，exp⁡𝐹(𝑥) =+∞∑𝑖=0𝐹𝑖(𝑥)𝑖!exp⁡F(x)=∑i=0+∞Fi(x)i!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有标号物品放到任意多个无标号盒子里的指数型生成函数（EXP 通过每项除以一个 𝑖!i!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 去掉了盒子的标号）．这其实就是贝尔数的生成函数．

这里涉及到很多「有标号」「无标号」的内容，注意辨析．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int main () { scanf ( "%d%d" , & n , & k ); poly f ( n \+ 1 ); fact [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) fact [ i ] = ( ll ) fact [ i \- 1 ] * i % mod ; for ( int i = 1 ; i <= n ; ++ i ) f [ i ] = qpow ( fact [ i ], mod \- 2 ); f = exp ( log ( f >> 1 ) * k ) << k , f . resize ( n \+ 1 ); int inv = qpow ( fact [ k ], mod \- 2 ); for ( int i = 0 ; i <= n ; ++ i ) printf ( "%lld " , ( ll ) f [ i ] * fact [ i ] % mod * inv % mod ); return 0 ; } ```   
---|---  
  
## 第一类斯特林数（Stirling Number）

**第一类斯特林数** （斯特林轮换数）[𝑛𝑘][nk]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也可记做 𝑠(𝑛,𝑘)s(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不同的元素，划分为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不区分的非空轮换的方案数．

一个轮换就是一个首尾相接的环形排列．我们可以写出一个轮换 [𝐴,𝐵,𝐶,𝐷][A,B,C,D]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且我们认为 [𝐴,𝐵,𝐶,𝐷] =[𝐵,𝐶,𝐷,𝐴] =[𝐶,𝐷,𝐴,𝐵] =[𝐷,𝐴,𝐵,𝐶][A,B,C,D]=[B,C,D,A]=[C,D,A,B]=[D,A,B,C]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即，两个可以通过旋转而互相得到的轮换是等价的．注意，我们不认为两个可以通过翻转而相互得到的轮换等价，即 [𝐴,𝐵,𝐶,𝐷] ≠[𝐷,𝐶,𝐵,𝐴][A,B,C,D]≠[D,C,B,A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 递推式

[𝑛𝑘]=[𝑛−1𝑘−1]+(𝑛−1)[𝑛−1𝑘][nk]=[n−1k−1]+(n−1)[n−1k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

边界是 [𝑛0] =[𝑛 =0][n0]=[n=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

该递推式的证明可以考虑其组合意义．

我们插入一个新元素时，有两种方案：

  * 将该新元素置于一个单独的轮换中，共有 [𝑛−1𝑘−1][n−1k−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案；
  * 将该元素插入到任何一个现有的轮换中，共有 (𝑛 −1)[𝑛−1𝑘](n−1)[n−1k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案．

根据加法原理，将两式相加即可得到递推式．

### 通项公式

第一类斯特林数没有实用的通项公式．

### 同一行第一类斯特林数的计算

类似第二类斯特林数，我们构造同行第一类斯特林数的生成函数，即

𝐹𝑛(𝑥) =𝑛∑𝑖=0[𝑛𝑖]𝑥𝑖Fn(x)=∑i=0n[ni]xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据递推公式，不难写出

𝐹𝑛(𝑥) =(𝑛 −1)𝐹𝑛−1(𝑥) +𝑥𝐹𝑛−1(𝑥)Fn(x)=(n−1)Fn−1(x)+xFn−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是

𝐹𝑛(𝑥) =𝑛−1∏𝑖=0(𝑥 +𝑖) =(𝑥+𝑛−1)!(𝑥−1)!Fn(x)=∏i=0n−1(x+i)=(x+n−1)!(x−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这其实是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次上升阶乘幂，记做 𝑥――𝑛xn―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这个东西自然是可以暴力分治乘 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出的，但用上升幂相关做法可以 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出，详情见 [多项式平移 | 连续点值平移](../../poly/shift/#同一行第一类无符号-stirling-数)．

### 同一列第一类斯特林数的计算

仿照第二类斯特林数的计算，我们可以用指数型生成函数解决该问题．注意，由于递推公式和行有关，我们不能利用递推公式计算同列的第一类斯特林数．

显然，单个轮换的指数型生成函数为

𝐹(𝑥) =𝑛∑𝑖=1(𝑖−1)!𝑥𝑖𝑖! =𝑛∑𝑖=1𝑥𝑖𝑖F(x)=∑i=1n(i−1)!xii!=∑i=1nxii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂就是 [𝑖𝑘][ik]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数型生成函数，𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算即可．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text int main () { scanf ( "%d%d" , & n , & k ); fact [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) fact [ i ] = ( ll ) fact [ i \- 1 ] * i % mod ; ifact [ n ] = qpow ( fact [ n ], mod \- 2 ); for ( int i = n \- 1 ; i >= 0 ; \-- i ) ifact [ i ] = ( ll ) ifact [ i \+ 1 ] * ( i \+ 1 ) % mod ; poly f ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) f [ i ] = ( ll ) fact [ i \- 1 ] * ifact [ i ] % mod ; f = exp ( log ( f >> 1 ) * k ) << k , f . resize ( n \+ 1 ); for ( int i = 0 ; i <= n ; ++ i ) printf ( "%lld " , ( ll ) f [ i ] * fact [ i ] % mod * ifact [ k ] % mod ); return 0 ; } ```   
---|---  
  
## 应用

### 上升幂与普通幂的相互转化

我们记上升阶乘幂 𝑥――𝑛 =∏𝑛−1𝑘=0(𝑥 +𝑘)xn―=∏k=0n−1(x+k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则可以利用下面的恒等式将上升幂转化为普通幂：

𝑥――𝑛=∑𝑘[𝑛𝑘]𝑥𝑘xn―=∑k[nk]xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果将普通幂转化为上升幂，则有下面的恒等式：

𝑥𝑛=∑𝑘{𝑛𝑘}(−1)𝑛−𝑘𝑥――𝑘xn=∑k{nk}(−1)n−kxk―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 下降幂与普通幂的相互转化

我们记下降阶乘幂 𝑥𝑛―― =𝑥!(𝑥−𝑛)! =∏𝑛−1𝑘=0(𝑥 −𝑘)xn―=x!(x−n)!=∏k=0n−1(x−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则可以利用下面的恒等式将普通幂转化为下降幂：

𝑥𝑛=∑𝑘{𝑛𝑘}𝑥𝑘――xn=∑k{nk}xk―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果将下降幂转化为普通幂，则有下面的恒等式：

𝑥𝑛――=∑𝑘[𝑛𝑘](−1)𝑛−𝑘𝑥𝑘xn―=∑k[nk](−1)n−kxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 多项式下降阶乘幂表示与多项式点值表示的关系

在这里，多项式的下降阶乘幂表示就是用

𝑓(𝑥)=𝑛∑𝑖=0𝑏𝑖𝑥𝑖――f(x)=∑i=0nbixi―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的形式表示一个多项式，而点值表示就是用 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点

(𝑖,𝑎𝑖),𝑖=0..𝑛(i,ai),i=0..n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

来表示一个多项式．

显然，下降阶乘幂 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和点值 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间满足这样的关系：

𝑎𝑘=𝑛∑𝑖=0𝑏𝑖𝑘𝑖――ak=∑i=0nbiki―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即

𝑎𝑘=𝑛∑𝑖=0𝑏𝑖𝑘!(𝑘−𝑖)!𝑎𝑘𝑘!=𝑘∑𝑖=0𝑏𝑖1(𝑘−𝑖)!ak=∑i=0nbik!(k−i)!akk!=∑i=0kbi1(k−i)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一个卷积形式的式子，我们可以在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内完成点值和下降阶乘幂的互相转化．

## 习题

  * [HDU3625 Examining the Rooms](https://acm.hdu.edu.cn/showproblem.php?pid=3625)
  * [UOJ540 联合省选 2020 组合数问题](https://uoj.ac/problem/540)
  * [UOJ269 清华集训 2016 如何优雅地求和](https://uoj.ac/problem/269)

## 参考资料与注释

  1. [Stirling Number of the First Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheFirstKind.html)
  2. [Stirling Number of the Second Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/stirling.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/stirling.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [Fei Natsuka](mailto:fei-natsuka@outlook.com), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [caijianhong](https://github.com/caijianhong), [CCXXXI](https://github.com/CCXXXI), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [isdanni](https://github.com/isdanni), [Konano](https://github.com/Konano), [LLLMMKK](https://github.com/LLLMMKK), [Menci](https://github.com/Menci), [purple-vine](https://github.com/purple-vine), [shuzhouliu](https://github.com/shuzhouliu), [YanagiOrigami](https://github.com/YanagiOrigami)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
