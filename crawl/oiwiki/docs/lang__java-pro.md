# Java è¿é¶ - OI Wiki

- Source: https://oi-wiki.org/lang/java-pro/

# Java è¿é¶

æ³¨æ

ä»¥ä¸å å®¹ååºäº Java JDK 8 çæ¬ç¼åï¼ä¸æé¤å¨æ´é«çæ¬ä¸­æé¨åæ¹å¨çå¯è½æ§ï¼

## æ´é«éçè¾å ¥è¾åº

`Scanner` å `System.out.print` å¨æå¼å§ä¼å·¥ä½å¾å¾å¥½ï¼ä½æ¯å¨å¤çæ´å¤§çè¾å ¥çæ¶åä¼éä½æçï¼å æ­¤æä»¬ä¼éè¦ä½¿ç¨ä¸äºæ¹æ³æ¥æé« IO éåº¦ï¼

### ä½¿ç¨ Kattio + StringTokenizer ä½ä¸ºè¾å ¥

æå¸¸ç¨çæ¹æ³ä¹ä¸æ¯ä½¿ç¨æ¥èª Kattis ç [Kattio.java](https://github.com/Kattis/kattio/blob/master/Kattio.java) æ¥æé« IO æçï¼1è¿ä¸ªæ¹æ³ä¼å° `StringTokenizer` ä¸ `PrintWriter` å è£ å¨ä¸ä¸ªç±»ä¸­æ¹ä¾¿ä½¿ç¨ï¼èå¨å ·ä½è¿è¡è§£é¢çæ¶åï¼åå¦èµä¼/ç»ç»æ¹å è®¸ï¼å¯ä»¥ç´æ¥ä½¿ç¨è¿ä¸ªæ¨¡æ¿ï¼

ä¸æ¹å³ä¸ºåºå å«å¨ä»£ç ä¸­ç IO æ¨¡æ¿ï¼ç±äº Kattis çå Kattio å å«ä¸äºå¹¶ä¸å¸¸ç¨çåè½ï¼ä¸æ¹çæ¨¡æ¿ç»è¿äºä¸äºè°æ´ï¼å Kattio ä½¿ç¨ MIT ä½ä¸ºåè®®ï¼ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text class Kattio extends PrintWriter { private BufferedReader r ; private StringTokenizer st ; // æ å IO public Kattio () { this ( System . in , System . out ); } public Kattio ( InputStream i , OutputStream o ) { super ( o ); r = new BufferedReader ( new InputStreamReader ( i )); } // æä»¶ IO public Kattio ( String intput , String output ) throws IOException { super ( output ); r = new BufferedReader ( new FileReader ( intput )); } // å¨æ²¡æå ¶ä»è¾å ¥æ¶è¿å null public String next () { try { while ( st == null || ! st . hasMoreTokens ()) st = new StringTokenizer ( r . readLine ()); return st . nextToken (); } catch ( Exception e ) {} return null ; } public int nextInt () { return Integer . parseInt ( next ()); } public double nextDouble () { return Double . parseDouble ( next ()); } public long nextLong () { return Long . parseLong ( next ()); } } ```   
---|---  
  
èä¸æ¹ä»£ç ç®åå±ç¤ºäº Kattio çä½¿ç¨ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text class Test { public static void main ( String [] args ) { Kattio io = new Kattio (); // å­ç¬¦ä¸²è¾å ¥ String str = io . next (); // int è¾å ¥ int num = io . nextInt (); // è¾åº io . println ( "Result" ); // è¯·ç¡®ä¿å ³é­ IO æµä»¥ç¡®ä¿è¾åºè¢«æ­£ç¡®åå ¥ io . close (); } } ```   
---|---  
  
### ä½¿ç¨ StreamTokenizer ä½ä¸ºè¾å ¥

å¨æäºæ åµä½¿ç¨ `StringTokenizer` ä¼å¯¼è´ MLEï¼Memory Limit Exceededï¼è¶ è¿å å­ä¸éï¼ï¼æ­¤æ¶æä»¬éè¦ä½¿ç¨ `StreamTokenizer` ä½ä¸ºè¾å ¥ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text import java.io.* ; public class Main { // IO ä»£ç  public static StreamTokenizer in = new StreamTokenizer ( new BufferedReader ( new InputStreamReader ( System . in ), 32768 )); public static PrintWriter out = new PrintWriter ( new OutputStreamWriter ( System . out )); public static double nextDouble () throws IOException { in . nextToken (); return in . nval ; } public static float nextFloat () throws IOException { in . nextToken (); return ( float ) in . nval ; } public static int nextInt () throws IOException { in . nextToken (); return ( int ) in . nval ; } public static String next () throws IOException { in . nextToken (); return in . sval ; } public static long nextLong () throws Exception { in . nextToken (); return ( long ) in . nval ;} // ä½¿ç¨ç¤ºä¾ public static void main ( String [] args ) throws Exception { int n = nextInt (); out . println ( n ); out . close (); } } ```   
---|---  
  
### Kattio + StringTokenizer çæ¹æ³ä¸ StreamTokenizer çæ¹æ³ä¹é´çåæä¸å¯¹æ¯

  1. `StreamTokenizer` ç¸è¾äº `StringTokenizer` ä½¿ç¨çå å­è¾å°ï¼å½ Java æ ç¨ MLE æ¶å¯ä»¥å°è¯ä½¿ç¨ `StreamTokenizer`ï¼ä½æ¯ `StreamTokenizer` ä¼ä¸¢å¤±ç²¾åº¦ï¼è¯»å ¥é¨åæ°æ®æ¶ä¼åºç°é®é¢ï¼
     * `StreamTokenizer` æºç å­å¨ `Type`ï¼è¯¥ `Type` æ ¹æ®è¾å ¥å å®¹æ¥å³å®ç±»åï¼å¦æè¾å ¥ç±»ä¼¼äº `123oi` ä»¥ **æ°å­å¼å¤´** çå­ç¬¦ä¸²ï¼ä»ä¼å¼ºå¶è®¤ä¸ºçç±»åæ¯ `double` ç±»åï¼å æ­¤å¨è¯»å ¥ä¸­ä»¥ `double` ç±»åå»è¯» `String` ç±»åä¾¿ä¼æåºå¼å¸¸ï¼
     * `StreamTokenizer` å¨è¯»å ¥ `1e14` ä»¥ä¸å¤§å°çæ°å­ä¼ä¸¢å¤±ç²¾åº¦ï¼
  2. å¨ä½¿ç¨ `PrintWriter` æ åµä¸ï¼éæ³¨æå¨ç¨åºç»ææå `close()` å ³é­è¾åºæµæå¨éè¦è¾åºçæ¶åä½¿ç¨ `flush()` æ¸ é¤ç¼å²åºï¼å¦åå å®¹å°ä¸ä¼è¢«åå ¥å°æ§å¶å°/æä»¶ä¸­ï¼
  3. `Kattio` æ¯ç»§æ¿èª `PrintWriter` ç±»ï¼èªèº«å¯¹è±¡å ·æäº `PrintWriter` çåè½ï¼å æ­¤å¯ä»¥ç´æ¥è°ç¨ `PrintWriter` ç±»çå½æ°è¾åºï¼åæ¶å° `StringTokenizer` ä½ä¸ºäºèªèº«çæååéæ¥ä¿®æ¹ï¼èç¬¬äºç§ `Main` æ¯åæ¶å° `StreamTokenizer` ä¸ `PrintWriter` ä½ä¸ºäºèªèº«çæååéï¼å æ­¤å¨ä½¿ç¨ä¸æäºè®¸å·®è·ï¼

ç»¼ä¸æè¿°ï¼å¨å¤§é¨åæ åµä¸ï¼`StringTokenizer` çä½¿ç¨å¤å¢è¦ä¼è¶äº `StreamTokenizer`ï¼å¨æç«¯ MLE çæ åµä¸å¯ä»¥å°è¯ `StreamTokenizer`ï¼åæ¶ `int` èå´ä»¥ä¸çæ°æ® `StreamTokenizer` å¤çæ¯æ è½ä¸ºåçï¼

## BigInteger ä¸æ°è®º

`BigInteger` æ¯ Java æä¾çé«ç²¾åº¦è®¡ç®ç±»ï¼å¯ä»¥å¾æ¹ä¾¿å°è§£å³é«ç²¾åº¦é®é¢ï¼

### åå§å

`BigInteger` å¸¸ç¨åå»ºæ¹å¼æå¦ä¸äºç§ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text import java.io.PrintWriter ; import java.math.BigInteger ; class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { BigInteger a = new BigInteger ( "12345678910" ); // å°å­ç¬¦ä¸²ä»¥åè¿å¶çå½¢å¼åå»º BigInteger å¯¹è±¡ out . println ( a ); // a çå¼ä¸º 12345678910Â BigInteger b = new BigInteger ( "1E" , 16 ); // å°å­ç¬¦ä¸²ä»¥æå®è¿å¶çå½¢å¼åå»º BigInteger å¯¹è±¡ out . println ( b ); // b çå¼ä¸º 30Â out . close (); } } ```   
---|---  
  
### åºæ¬è¿ç®

ä»¥ä¸åç¨ `this` ä»£æ¿å½å `BigIntger`:

å½æ°å| åè½  
---|---  
`abs()`| è¿å `this` çç»å¯¹å¼  
`negate()`| è¿å `this` çç¸åæ°  
`add(BigInteger val)`| è¿å `this` å `val` çå  
`subtract(BigInteger val)`| è¿å `this` å `val` çå·®  
`multiply(BigInteger val)`| è¿å `this` å `val` çç§¯  
`divide(BigInteger val)`| è¿å `this` å `val` çå  
`remainder(BigInteger val)`| è¿å `this` é¤ä»¥ `val` çä½æ°  
`mod(BigInteger val)`| è¿å `this` å¯¹ `val` åæ¨¡çå¼  
`pow(int val)`| è¿å `this` ç `val` æ¬¡æ¹  
`and(BigInteger val)`| è¿å `this` å `val` çæä½ä¸  
`or(BigInteger val)`| è¿å `this` å `val` çæä½æ  
`not()`| è¿å `this` çæä½åå  
`xor(BigInteger val)`| è¿å `this` å `val` çæä½å¼æ  
`shiftLeft(int n)`| è¿å `this` å·¦ç§» `n` ä½  
`shiftRight(int n)`| è¿å `this` å³ç§» `n` ä½  
`max(BigInteger val)`| è¿å `this` ä¸ `val` çè¾å¤§å¼  
`min(BigInteger val)`| è¿å `this` ä¸ `val` çè¾å°å¼  
`bitCount()`| è¿å `this` çäºè¿å¶ä¸­ä¸å æ¬ç¬¦å·ä½ç `1` çä¸ªæ°  
`bitLength()`| è¿å `this` çäºè¿å¶ä¸­ä¸å æ¬ç¬¦å·ä½çé¿åº¦  
`getLowestSetBit()`| è¿å `this` çäºè¿å¶ä¸­æå³è¾¹çä½ç½®  
`compareTo(BigInteger val)`| æ¯è¾ `this` å `val` å¼å¤§å°  
`toString()`| è¿å `this` çåè¿å¶å­ç¬¦ä¸²è¡¨ç¤ºå½¢å¼  
`toString(int radix)`| è¿å `this` ç `raidx` è¿å¶å­ç¬¦ä¸²è¡¨ç¤ºå½¢å¼  
  
ä½¿ç¨æ¡ä¾å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 ``` |  ```text import java.io.PrintWriter ; import java.math.BigInteger ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static BigInteger a , b ; static void abs () { out . println ( "abs:" ); a = new BigInteger ( "-123" ); out . println ( a . abs ()); // è¾åº 123Â a = new BigInteger ( "123" ); out . println ( a . abs ()); // è¾åº 123Â } static void negate () { out . println ( "negate:" ); a = new BigInteger ( "-123" ); out . println ( a . negate ()); // è¾åº 123Â a = new BigInteger ( "123" ); out . println ( a . negate ()); // è¾åº -123Â } static void add () { out . println ( "add:" ); a = new BigInteger ( "123" ); b = new BigInteger ( "123" ); out . println ( a . add ( b )); // è¾åº 246Â } static void subtract () { out . println ( "subtract:" ); a = new BigInteger ( "123" ); b = new BigInteger ( "123" ); out . println ( a . subtract ( b )); // è¾åº 0Â } static void multiply () { out . println ( "multiply:" ); a = new BigInteger ( "12" ); b = new BigInteger ( "12" ); out . println ( a . multiply ( b )); // è¾åº 144Â } static void divide () { out . println ( "divide:" ); a = new BigInteger ( "12" ); b = new BigInteger ( "11" ); out . println ( a . divide ( b )); // è¾åº 1Â } static void remainder () { out . println ( "remainder:" ); a = new BigInteger ( "12" ); b = new BigInteger ( "10" ); out . println ( a . remainder ( b )); // è¾åº 2Â a = new BigInteger ( "-12" ); b = new BigInteger ( "10" ); out . println ( a . remainder ( b )); // è¾åº -2Â } static void mod () { out . println ( "mod:" ); a = new BigInteger ( "12" ); b = new BigInteger ( "10" ); out . println ( a . mod ( b )); // è¾åº 2Â a = new BigInteger ( "-12" ); b = new BigInteger ( "10" ); out . println ( a . mod ( b )); // è¾åº 8Â } static void pow () { out . println ( "pow:" ); a = new BigInteger ( "2" ); out . println ( a . pow ( 10 )); // è¾åº 1024Â } static void and () { out . println ( "and:" ); a = new BigInteger ( "3" ); // 11Â b = new BigInteger ( "5" ); // 101Â out . println ( a . and ( b )); // è¾åº 1Â } static void or () { out . println ( "or:" ); a = new BigInteger ( "2" ); // 10Â b = new BigInteger ( "5" ); // 101Â out . println ( a . or ( b )); // è¾åº 7Â } static void not () { out . println ( "not:" ); a = new BigInteger ( "2147483647" ); // 01111111 11111111 11111111 11111111Â out . println ( a . not ()); // è¾åº -2147483648 äºè¿å¶ä¸ºï¼10000000 00000000 00000000 00000000Â } static void xor () { out . println ( "xor:" ); a = new BigInteger ( "6" ); // 110Â b = new BigInteger ( "5" ); // 101Â out . println ( a . xor ( b )); // 011 è¾åº 3Â } static void shiftLeft () { out . println ( "shiftLeft:" ); a = new BigInteger ( "1" ); out . println ( a . shiftLeft ( 10 )); // è¾åº 1024Â } static void shiftRight () { out . println ( "shiftRight:" ); a = new BigInteger ( "1024" ); out . println ( a . shiftRight ( 8 )); // è¾åº 4Â } static void max () { out . println ( "max:" ); a = new BigInteger ( "6" ); b = new BigInteger ( "5" ); out . println ( a . max ( b )); // è¾åº 6Â } static void min () { out . println ( "min:" ); a = new BigInteger ( "6" ); b = new BigInteger ( "5" ); out . println ( a . min ( b )); // è¾åº 5Â } static void bitCount () { out . println ( "bitCount:" ); a = new BigInteger ( "6" ); // 110Â out . println ( a . bitCount ()); // è¾åº 2Â } static void bitLength () { out . println ( "bitLength:" ); a = new BigInteger ( "6" ); // 110Â out . println ( a . bitLength ()); // è¾åº 3Â } static void getLowestSetBit () { out . println ( "getLowestSetBit:" ); a = new BigInteger ( "8" ); // 1000Â out . println ( a . getLowestSetBit ()); // è¾åº 3Â } static void compareTo () { out . println ( "compareTo:" ); a = new BigInteger ( "8" ); b = new BigInteger ( "9" ); out . println ( a . compareTo ( b )); // è¾åº -1Â a = new BigInteger ( "8" ); b = new BigInteger ( "8" ); out . println ( a . compareTo ( b )); // è¾åº 0Â a = new BigInteger ( "8" ); b = new BigInteger ( "7" ); out . println ( a . compareTo ( b )); // è¾åº 1Â } static void toStringTest () { out . println ( "toString:" ); a = new BigInteger ( "15" ); out . println ( a . toString ()); // è¾åº 15Â out . println ( a . toString ( 16 )); // è¾åº fÂ } public static void main ( String [] args ) { abs (); negate (); add (); subtract (); multiply (); divide (); remainder (); mod (); pow (); and (); or (); not (); xor (); shiftLeft (); shiftRight (); max (); min (); bitCount (); bitLength (); getLowestSetBit (); compareTo (); toStringTest (); out . close (); } } ```   
---|---  
  
### æ°å­¦è¿ç®

ä»¥ä¸åç¨ `this` ä»£æ¿å½å `BigIntger`:

å½æ°å| åè½  
---|---  
`gcd(BigInteger val)`| è¿å `this` çç»å¯¹å¼ä¸ `val` çç»å¯¹å¼çæå¤§å ¬çº¦æ°  
`isProbablePrime(int val)`| è¿åä¸ä¸ªè¡¨ç¤º `this` æ¯å¦æ¯ç´ æ°çå¸å°å¼  
`nextProbablePrime()`| è¿åç¬¬ä¸ä¸ªå¤§äº `this` çç´ æ°  
`modPow(BigInteger b, BigInteger p)`| è¿å `this` ç `b` æ¬¡æ¹æ¨¡ `p` çå¼  
`modInverse(BigInteger p)`| è¿å `this` å¨æ¨¡ `p` æä¹ä¸çä¹æ³éå   
  
ä½¿ç¨æ¡ä¾å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` |  ```text import java.io.PrintWriter ; import java.math.BigInteger ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static BigInteger a , b , p ; static void gcd () { // æå¤§å ¬çº¦æ°Â a = new BigInteger ( "120032414321432144212100" ); b = new BigInteger ( "240231431243123412432140" ); out . println ( String . format ( "gcd(%s,%s)=%s" , a . toString (), b . toString (), a . gcd ( b ). toString ())); // gcd(120032414321432144212100,240231431243123412432140)=20Â } static void isPrime () { // åºäºç±³åç½å®¾å¤å®è¯¥æ°æ¯å¦æ¯ç´ æ°ï¼åæ°è¶å¤§åç¡®æ§è¶é«ï¼å¤æåº¦è¶é«ï¼åç¡®æ§ä¸º (1-1/(val*2))Â a = new BigInteger ( "1200324143214321442127" ); out . println ( "a:" \+ a . toString ()); out . println ( a . isProbablePrime ( 10 ) ? "a is prime" : "a is not prime" ); // a is not primeÂ } static void nextPrime () { // æ¾åºè¯¥æ°çä¸ä¸ä¸ªç´ æ°Â a = new BigInteger ( "1200324143214321442127" ); out . println ( "a:" \+ a . toString ()); out . println ( String . format ( "a nextPrime is %s" , a . nextProbablePrime (). toString ())); // a nextPrime is 1200324143214321442199Â } static void modPow () { // å¿«éå¹ï¼æ¯æ­£å¸¸çæ¬è¦å¿«ï¼å é¨ææ°å­¦ä¼åÂ a = new BigInteger ( "2" ); b = new BigInteger ( "10" ); p = new BigInteger ( "1000" ); out . println ( String . format ( "a:%s b:%s p:%s" , a , b , p )); out . println ( String . format ( "a^b mod p:%s" , a . modPow ( b , p ). toString ())); // 24Â } static void modInverse () { // éå Â a = new BigInteger ( "10" ); b = new BigInteger ( "3" ); out . println ( a . modInverse ( b )); // a ^ (p-2) mod p = 1Â } public static void main ( String [] args ) { gcd (); isPrime (); nextPrime (); modPow (); modInverse (); out . close (); } } ```   
---|---  
  
å ³äºç±³åç½å®¾ç¸å ³ç¥è¯å¯ä»¥æ¥é [MillerâRabin ç´ æ§æµè¯](../../math/number-theory/prime/#millerrabin-ç´)ï¼

## åºæ¬æ°æ®ç±»åä¸å è£ æ°æ®ç±»å

### ç®ä»

ç±äºåºæ¬ç±»åæ²¡æé¢åå¯¹è±¡çç¹å¾ï¼ä¸ºäºä»ä»¬åå å°é¢åå¯¹è±¡çå¼åä¸­ï¼Java ä¸ºå «ä¸ªåºæ¬ç±»åæä¾äºå¯¹åºçå è£ ç±»ï¼åå«æ¯ `Byte`ã`Double`ã`Float`ã`Integer`ã`Long`ã`Short`ã`Character` å `Boolean`ï¼ä¸¤è ä¹é´çå¯¹åºå ³ç³»å¦ä¸ï¼

åºæ¬æ°æ®ç±»å| å è£ æ°æ®ç±»å  
---|---  
`byte`| `Byte`  
`short`| `Short`  
`boolean`| `Boolean`  
`char`| `Character`  
`int`| `Integer`  
`long`| `Long`  
`float`| `Float`  
`double`| `Double`  
  
### åºå«

æ­¤å¤ä»¥ `int` ä¸ `Integer` ä¸¾ä¾ï¼

  1. `Integer` æ¯ `int` çå è£ ç±»ï¼`int` åæ¯ Java çä¸ç§åºæ¬ç±»åæ°æ®ï¼
  2. `Integer` ç±»åå®ä¾åæè½ä½¿ç¨ï¼è `int` ç±»åä¸éè¦ï¼
  3. `Integer` å®é å¯¹åºçå¼ç¨ï¼å½ `new` ä¸ä¸ª `Integer` æ¶ï¼å®é ä¸çæäºä¸ä¸ªå¯¹è±¡ï¼è `int` åæ¯ç´æ¥å­å¨æ°æ®ï¼
  4. `Integer` çé»è®¤å¼æ¯ `null`ï¼å¯æ¥å `null` å `int` ç±»åçæ°æ®ï¼`int` é»è®¤å¼æ¯ 0ï¼ä¸è½æ¥å `null` ç±»åçæ°æ®ï¼
  5. `Integer` å¤å®äºä¸ªåéæ¯å¦ç¸åä½¿ç¨ `==` å¯è½ä¼å¯¼è´ä¸æ­£ç¡®çç»æï¼åªè½ä½¿ç¨ `equals()`ï¼è `int` å¯ä»¥ç´æ¥ä½¿ç¨ `==`ï¼

### è£ ç®±ä¸æç®±

æ­¤å¤ä»¥ `int` ä¸ `Integer` ä¸¾ä¾ï¼

`Integer` çæ¬è´¨æ¯å¯¹è±¡ï¼`int` æ¯åºæ¬ç±»åï¼ä¸¤ä¸ªç±»åä¹é´æ¯ä¸è½ç´æ¥èµå¼çï¼éè¦è½¬æ¢æ¶ï¼åºå°åºç¡ç±»åè½¬æ¢ä¸ºå è£ ç±»åï¼è¿ç§åæ³ç§°ä¸ºè£ ç®±ï¼åè¿æ¥åç§°ä¸ºæç®±ï¼

```text 1 2 3 4 5 6 ``` |  ```text // åºæ¬ç±»å int value1 = 1 ; // è£ ç®±è½¬æ¢ä¸ºå è£ ç±»å Integer integer = Integer . valueOf ( value1 ); // æç®±è½¬æ¢ä¸ºåºæ¬ç±»å int value2 = integer . intValue (); ```   
---|---  
  
Java 5 å¼å ¥äºèªå¨è£ ç®±æç®±æºå¶ï¼

```text 1 2 ``` |  ```text Integer integer = 1 ; int value = integer ; ```   
---|---  
  
æ³¨æ

è½ç¶ JDK å¢å äºèªå¨è£ ç®±æç®±çæºå¶ï¼ä½å¨å£°æåéæ¶è¯·éæ©åéçç±»åï¼å ä¸ºå è£ ç±»å `Integer` å¯ä»¥æ¥å `null`ï¼èåºæ¬ç±»å `int` ä¸è½æ¥å `null`ï¼å æ­¤ï¼å¯¹ä½¿ç¨ `null` å¼çå è£ ç±»åè¿è¡æç®±æä½æ¶ï¼ä¼æåºå¼å¸¸ï¼å¦ä¸ä»£ç å±ç¤ºäºè¿ä¸è¡ä¸ºï¼

```text 1 2 3 4 5 ``` |  ```text Integer integer = Integer . valueOf ( null ); integer . intValue (); // æåº java.lang.NumberFormatException å¼å¸¸ Integer integer = null ; integer . intValue (); // æåº java.lang.NullPointerException å¼å¸¸ ```   
---|---  
  
## ç»§æ¿

åºäºå·²æçè®¾è®¡åé æ°çè®¾è®¡ï¼å°±æ¯é¢åå¯¹è±¡ç¨åºè®¾è®¡ä¸­çç»§æ¿ï¼å¨ç»§æ¿ä¸­ï¼æ°çç±»ä¸æ¯å­ç©ºäº§ççï¼èæ¯åºäºä¸ä¸ªå·²ç»å­å¨çç±»èå®ä¹åºæ¥çï¼éè¿ç»§æ¿ï¼æ°çç±»èªå¨è·å¾äºåºç¡ç±»ä¸­ææçæåï¼å æ¬æååéåæ¹æ³ï¼å æ¬åç§è®¿é®å±æ§çæåï¼æ è®ºæ¯ `public` è¿æ¯ `private`ï¼æ¾ç¶ï¼éè¿ç»§æ¿æ¥å®ä¹æ°çç±»ï¼è¿æ¯ä»å¤´å¼å§åä¸ä¸ªæ°çç±»è¦ç®åå¿«æ·åæ¹ä¾¿ï¼ç»§æ¿æ¯æ¯æä»£ç éç¨çéè¦ææ®µä¹ä¸ï¼

å¨ Java ä¸­ï¼ç»§æ¿çå ³é®å­ä¸º `extends`ï¼ä¸ Java åªæ¯æåç»§æ¿ï¼ä½å¯ä»¥å®ç°å¤æ¥å£ï¼

å¨ Java ä¸­ï¼ææç±»é½æ¯ `Object` ç±»çå­ç±»ï¼

å­ç±»ç»§æ¿ç¶ç±»ï¼ææçç¶ç±»çæåï¼å æ¬åéåæ¹æ³ï¼é½æä¸ºäºå­ç±»çæåï¼é¤äºæé æ¹æ³ï¼æé æ¹æ³æ¯ç¶ç±»æç¬æçï¼å ä¸ºå®ä»¬çåå­å°±æ¯ç±»çåå­ï¼æä»¥ç¶ç±»çæé æ¹æ³å¨å­ç±»ä¸­ä¸å­å¨ï¼é¤æ­¤ä¹å¤ï¼å­ç±»ç»§æ¿å¾å°äºç¶ç±»ææçæåï¼

æ¯ä¸ªæåæä¸åçè®¿é®å±æ§ï¼å­ç±»ç»§æ¿å¾å°äºç¶ç±»ææçæåï¼ä½æ¯ä¸åçè®¿é®å±æ§ä½¿å¾å­ç±»å¨ä½¿ç¨è¿äºæåæ¶ææä¸åï¼æäºç¶ç±»çæåç´æ¥æä¸ºå­ç±»çå¯¹å¤ççé¢ï¼æäºåè¢«æ·±æ·±å°éèèµ·æ¥ï¼å³ä½¿å­ç±»èªå·±ä¹ä¸è½ç´æ¥è®¿é®ï¼

ä¸è¡¨ååºäºä¸åè®¿é®å±æ§çç¶ç±»æåå¨å­ç±»ä¸­çè®¿é®å±æ§ï¼

ç¶ç±»æåè®¿é®å±æ§| å¨ç¶ç±»ä¸­çå«ä¹| å¨å­ç±»ä¸­çå«ä¹  
---|---|---  
`public`| å¯¹ææç±»å¼æ¾| å¯¹ææç±»å¼æ¾  
`protected`| åªæå å å ¶å®ç±»ãèªå·±åå­ç±»å¯ä»¥è®¿é®| åªæå å å ¶å®ç±»ãèªå·±åå­ç±»å¯ä»¥è®¿é®  
ç¼ºçï¼`default`ï¼| åªæå å å ¶å®ç±»å¯ä»¥è®¿é®| å¦æå­ç±»ä¸ç¶ç±»å¨åä¸ä¸ªå å ï¼åªæå å å ¶å®ç±»å¯ä»¥è®¿é®ï¼å¦åç¸å½äº `private`ï¼ä¸è½è®¿é®  
`private`| åªæèªå·±å¯ä»¥è®¿é®| ä¸è½è®¿é®  
  
## å¤æ

å¨ Java ä¸­å½æä¸ä¸ªå¯¹è±¡èµå¼ç»ä¸ä¸ªåéæ¶ï¼å¯¹è±¡çç±»åå¿ é¡»ä¸åéçç±»åç¸å¹é ï¼ä½ç±äº Java æç»§æ¿çæ¦å¿µï¼ä¾¿å¯éæ°å®ä¹ä¸º **ä¸ä¸ªåéå¯ä»¥ä¿å­å ¶æå£°æçç±»åæè¯¥ç±»åçä»»ä½å­ç±»å** ï¼

å¦æä¸ä¸ªç±»åå®ç°äºæ¥å£ï¼ä¹å¯ä»¥ç§°ä¹ä¸ºè¯¥æ¥å£çå­ç±»åï¼

Java ä¸­ä¿å­å¯¹è±¡ç±»åçåéæ¯å¤æåéï¼ãå¤æãè¿ä¸ªæ¯è¯­ï¼å­é¢æææ¯è®¸å¤å½¢æï¼æ¯æä¸ä¸ªåéå¯ä»¥ä¿å­ä¸åç±»åï¼å³å ¶å£°æçç±»åæä»»ä½å­ç±»åï¼çå¯¹è±¡ï¼

å¤æåéï¼

  1. Java çå¯¹è±¡åéæ¯å¤æçï¼å®ä»¬è½ä¿å­ä¸æ­¢ä¸ç§ç±»åçå¯¹è±¡ï¼
  2. å®ä»¬å¯ä»¥ä¿å­çæ¯å£°æç±»åçå¯¹è±¡ï¼æå£°æç±»åå­ç±»çå¯¹è±¡ï¼
  3. å½æå­ç±»çå¯¹è±¡èµç»ç¶ç±»çåéçæ¶åï¼å°±åçäºåä¸è½¬åï¼

## æ³å

æ³åæå¨ç±»å®ä¹æ¶ä¸è®¾ç½®ç±»ä¸­çå±æ§ææ¹æ³åæ°çå ·ä½ç±»åï¼èæ¯å¨ä½¿ç¨ï¼æåå»ºå¯¹è±¡ï¼æ¶åè¿è¡ç±»åçå®ä¹ï¼æ³åæ¬è´¨æ¯åæ°åç±»åï¼å³ææä½çæ°æ®ç±»åè¢«æå®ä¸ºä¸ä¸ªåæ°ï¼

æ³åæä¾äºç¼è¯æ¶ç±»åå®å ¨æ£æµçæºå¶ï¼è¯¥æºå¶å è®¸ç¼è¯æ¶æ£æµéæ³ç±»åï¼

## æ¥å£

### ç®ä»

æ¥å£ï¼Interfaceï¼å¨ Java ä¸­æ¯ä¸ä¸ªæ½è±¡ç±»åï¼æ¯æ½è±¡æ¹æ³çéåï¼éå¸¸ä»¥ `interface` æ¥å£°æï¼ä¸ä¸ªç±»éè¿å®ç°æ¥å£çæ¹å¼ï¼ä»èæ¥ç»§æ¿æ¥å£çæ½è±¡æ¹æ³ï¼

æ¥å£å¹¶ä¸æ¯ç±»ï¼ç¼åæ¥å£çæ¹å¼åç±»å¾ç¸ä¼¼ï¼ä½æ¯å®ä»¬å±äºä¸åçæ¦å¿µï¼ç±»æè¿°å¯¹è±¡çå±æ§åæ¹æ³ï¼æ¥å£åå å«ç±»è¦å®ç°çæ¹æ³ï¼

é¤éå®ç°æ¥å£çç±»æ¯æ½è±¡ç±»ï¼å¦åè¯¥ç±»è¦å®ä¹æ¥å£ä¸­çæææ¹æ³ï¼

æ¥å£æ æ³è¢«å®ä¾åï¼ä½æ¯å¯ä»¥è¢«å®ç°ï¼ä¸ä¸ªå®ç°æ¥å£çç±»ï¼å¿ é¡»å®ç°æ¥å£å ææè¿°çæææ¹æ³ï¼å¦åå°±å¿ é¡»å£°æä¸ºæ½è±¡ç±»ï¼å¦å¤ï¼å¨ Java ä¸­ï¼æ¥å£ç±»åå¯ç¨æ¥å£°æä¸ä¸ªåéï¼ä»ä»¬å¯ä»¥æä¸ºä¸ä¸ªç©ºæéï¼ææ¯è¢«ç»å®å¨ä¸ä¸ªä»¥æ­¤æ¥å£å®ç°çå¯¹è±¡ï¼

### ä¸ç±»çåºå«

  1. æ¥å£ä¸è½ç¨äºå®ä¾åå¯¹è±¡ï¼
  2. æ¥å£æ²¡ææé æ¹æ³ï¼
  3. æ¥å£ä¸­ææçæ¹æ³å¿ é¡»æ¯æ½è±¡æ¹æ³ï¼Java 8 ä¹åæ¥å£ä¸­å¯ä»¥ä½¿ç¨ `default` å ³é®å­ä¿®é¥°çéæ½è±¡æ¹æ³ï¼
  4. æ¥å£ä¸è½å å«æååéï¼é¤äº static å final åéï¼
  5. æ¥å£ä¸æ¯è¢«ç±»ç»§æ¿äºï¼èæ¯è¦è¢«ç±»å®ç°ï¼
  6. æ¥å£æ¯æå¤ç»§æ¿ï¼ç±»ä¸æ¯æå¤ç»§æ¿ï¼

### å£°æ

```text 1 2 3 4 ``` |  ```text [ å¯è§åº¦ ] interface æ¥å£åç§° [ extends å ¶ä»çæ¥å£å ] { // å£°æåé // æ½è±¡æ¹æ³ } ```   
---|---  
  
### å®ç°

```text 1 ``` |  ```text ... implements æ¥å£åç§° [ , å ¶ä»æ¥å£åç§° , å ¶ä»æ¥å£åç§° ..., ... ] ... ```   
---|---  
  
## Lambda è¡¨è¾¾å¼

### ç®ä»

lambda è¡¨è¾¾å¼ä¹å¯ç§°ä¸ºé­å ï¼æ¯ Java 8 çæéè¦çæ°ç¹æ§ï¼

lambda è¡¨è¾¾å¼å è®¸æå½æ°ä½ä¸ºä¸ä¸ªæ¹æ³çåæ°ï¼å½æ°ä½ä¸ºåæ°ä¼ éè¿æ¹æ³ä¸­ï¼ï¼

ä½¿ç¨ lambda è¡¨è¾¾å¼å¯ä»¥ä½¿ä»£ç åçæ´å ç®æ´ç´§åï¼

### è¯­æ³

  * å¯éç±»åå£°æï¼ä¸éè¦å£°æåæ°ç±»åï¼ç¼è¯å¨å¯ä»¥ç»ä¸è¯å«åæ°å¼ï¼
  * å¯éçåæ°åæ¬å·ï¼ä¸ä¸ªåæ°æ éå®ä¹åæ¬å·ï¼ä½å¤ä¸ªåæ°éè¦å®ä¹åæ¬å·ï¼
  * å¯éçå¤§æ¬å·ï¼å¦æä¸»ä½å å«äºä¸ä¸ªè¯­å¥ï¼å°±ä¸éè¦ä½¿ç¨å¤§æ¬å·ï¼
  * å¯éçè¿åå ³é®å­ï¼å¦æä¸»ä½åªæä¸ä¸ªè¡¨è¾¾å¼è¿åå¼åç¼è¯å¨ä¼èªå¨è¿åå¼ï¼å¤§æ¬å·éè¦æå®è¡¨è¾¾å¼è¿åäºä¸ä¸ªæ°å¼ï¼

lambda è¡¨è¾¾å¼å£°ææ¹å¼å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text // 1. ä¸éè¦åæ°ï¼è¿åå¼ä¸º 5 () -> 5 // 2. æ¥æ¶ä¸ä¸ªåæ°ï¼æ°å­ç±»åï¼ï¼è¿åå ¶ 2 åçå¼ x -> 2 * x // 3. æ¥å 2 ä¸ªåæ°ï¼æ°å­ï¼å¹¶è¿åä»ä»¬çå·®å¼ ( x , y ) -> x â y // 4. æ¥æ¶ 2 ä¸ª int ç±»åæ´æ°å¹¶è¿åä»ä»¬çå ( int x , int y ) -> x \+ y // 5. æ¥åä¸ä¸ª String å¯¹è±¡å¹¶å¨æ§å¶å°æå°ï¼ä¸è¿åä»»ä½å¼ï¼çèµ·æ¥åæ¯è¿å voidï¼ ( String s ) -> System . out . print ( s ) ```   
---|---  
  
ä»¥å­ç¬¦ä¸²æ°ç»æé¿åº¦æåºçèªå®ä¹æ¯è¾å¨ä¸ºä¾ï¼lambda è¡¨è¾¾å¼å¯ä»¥æå¦ä¸å½¢å¼åºç¨ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text import java.util.Arrays ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { String [] plants = { "Mercury" , "venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune" }; Arrays . sort ( plants , ( String first , String second ) -> ( first . length () \- second . length ())); for ( String word : plants ) { out . print ( word \+ " " ); } out . close (); } } ```   
---|---  
  
ä¹å¯ä»¥ç±»ä¼¼ä¸é¢çä¾å­å¨ lambda è¡¨è¾¾å¼ä¸­ä½¿ç¨å¤æ¡è¯­å¥ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text import java.io.PrintWriter ; import java.util.Arrays ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { String [] plants = { "Mercury" , "venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune" }; Arrays . sort ( plants , ( first , second ) -> { // å½¢åä¸åç±»åï¼å¯ä»¥ä»ä¸ä¸æå¤æ­åº int result = first . length () \- second . length (); return result ; }); for ( String word : plants ) { out . print ( word \+ " " ); } out . close (); } } ```   
---|---  
  
å ¶ä¸­ï¼`->` æ¯ä¸ä¸ªæ¨å¯¼ç¬¦å·ï¼è¡¨ç¤ºåé¢çæ¬å·æ¥æ¶å°åæ°ï¼æ¨å¯¼åé¢çè¿åå¼ï¼å ¶å®å°±æ¯ä¼ éäºæ¹æ³ï¼ï¼

### å½æ°å¼æ¥å£

  1. æ¯ä¸ä¸ªæ¥å£ï¼ç¬¦å Java æ¥å£å®ä¹ï¼
  2. åªå å«ä¸ä¸ªæ½è±¡æ¹æ³çæ¥å£ï¼
  3. å ä¸ºåªæä¸ä¸ªæªå®ç°çæ¹æ³ï¼æä»¥ lambda è¡¨è¾¾å¼å¯ä»¥èªå¨å¡«ä¸å»ï¼

å½æ°å¼æ¥å£ä½¿ç¨æ¹å¼å¦ä¸ï¼

è¾åºé¿åº¦ä¸º 2 çåæ°çå­ç¬¦ä¸²

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text import java.io.PrintWriter ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { String [] plants = { "Mercury" , "venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune" }; Test test = s -> { // lambda è¡¨è¾¾å¼ä½ä¸ºå½æ°å¼æ¥å£çå®ä¾ if ( s . length () % 2 == 0 ) { return true ; } return false ; }; for ( String word : plants ) { if ( test . check ( word )) { out . print ( word \+ " " ); } } out . close (); } } interface Test { public boolean check ( String s ); } ```   
---|---  
  
å®ç°å åä¹é¤ååè¿ç®

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text import java.io.PrintWriter ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static double calc ( double a , double b , Calculator util ) { return util . operation ( a , b ); } public static void main ( String [] args ) { Calculator util [] = new Calculator [ 4 ] ; // å®ä¹å½æ°å¼æ¥å£æ°ç» util [ 0 ] = ( a , b ) -> a \+ b ; util [ 1 ] = ( a , b ) -> a \- b ; util [ 2 ] = ( a , b ) -> a * b ; util [ 3 ] = ( a , b ) -> a / b ; double a = 20 , b = 15 ; for ( Calculator c : util ) { System . out . println ( calc ( a , b , c )); } out . close (); } } interface Calculator { public double operation ( double a , double b ); } ```   
---|---  
  
## Collection

`Collection` æ¯ Java ä¸­çæ¥å£ï¼è¢«å¤ä¸ªæ³åå®¹å¨æ¥å£æå®ç°ï¼å¨è¿éï¼`Collection` æ¯æä»£å­æ¾å¯¹è±¡ç±»åçæ°æ®ç»æï¼

Java ä¸­ç `Collection` å ç´ ç±»åå®ä¹æ¶å¿ é¡»ä¸ºå¯¹è±¡ï¼ä¸è½ä¸ºåºæ¬æ°æ®ç±»åï¼

ä»¥ä¸å å®¹ç¨æ³ååºäº Java éå¤æçæ§è´¨ï¼åæ¯ä»¥å®ç°æ¥å£çå½¢å¼åºç°ï¼

å¸¸ç¨çæ¥å£å æ¬ `List`ã`Queue`ã`Set` å `Map`ï¼

### å®¹å¨å®ä¹

å½å®ä¹æ³åå®¹å¨ç±»æ¶ï¼éè¦å¨å®ä¹æ¶æå®æ°æ®ç±»åï¼å¦æä¸æå®æ°æ®ç±»åï¼èå½æ `Object` ç±»åéææ·»å æ°æ®ï¼å¨ Java 8 ä¸­è½è½ç¼è¯éè¿ï¼ä½ä¼æå¾å¤è­¦åé£é©ï¼

ä¾å¦ï¼å¦ä¸å®ä¹æ¹å¼æ¯å®å ¨çï¼å®¹å¨ä¸­åªæ¥å `Integer` ç±»åï¼

```text 1 ``` |  ```text List < Integer > list1 = new LinkedList <> (); ```   
---|---  
  
èå¦ä¸å®ä¹æ¹å¼ä¼åºç°è­¦åï¼

```text 1 2 3 4 5 6 ``` |  ```text List list = new ArrayList <> (); list . add ( 1 ); list . add ( true ); list . add ( 1.01 ); list . add ( 1L ); list . add ( "I am String" ); ```   
---|---  
  
å æ­¤ï¼å¦ææ²¡æç¹æ®éæ±çè¯ä¸æ¨èç¬¬ 2 ç§è¡ä¸ºï¼ç¼è¯å¨æ æ³å¸®å¿æ£æ¥å­å ¥çæ°æ®æ¯å¦å®å ¨ï¼`list.get(index)` åå¼æ¶æ æ³æç¡®æ°æ®çç±»åï¼åå°çæ°æ®ç±»åé½ä¸º `Object`ï¼ï¼éè¦æå¨è½¬ååæ¥çç±»åï¼ç¨æä¸æ å¯è½åºç°è¯¯è½¬åå¼å¸¸ï¼

å¦ææ¯æç¡®äºç±»åå¦ `List<Integer>`ï¼æ­¤æ¶ç¼è¯å¨ä¼æ£æ¥æ¾å ¥çæ°æ®ç±»åï¼åªè½æ¾å ¥æ´æ°çæ°æ®ï¼å£°æéååéæ¶åªè½ä½¿ç¨å è£ ç±»å `List<Integer>` æè èªå®ä¹ç `Class`ï¼èä¸è½æ¯åºæ¬ç±»åå¦ `List<int>`ï¼

### List

#### ArrayList

`ArrayList` æ¯æ¯æå¯ä»¥æ ¹æ®éæ±å¨æçé¿çæ°ç»ï¼åå§é¿åº¦é»è®¤ä¸º 10ï¼å¦æè¶ åºå½åé¿åº¦ä¾¿æ©å®¹ 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

##### åå§å

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text import java.io.PrintWriter ; import java.util.ArrayList ; import java.util.List ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { List < Integer > list1 = new ArrayList <> (); // åå»ºä¸ä¸ªåå­ä¸º list1 çå¯èªå¢æ°ç»ï¼åå§é¿åº¦ä¸ºé»è®¤å¼ï¼10ï¼ List < Integer > list2 = new ArrayList <> ( 30 ); // åå»ºä¸ä¸ªåå­ä¸ºlist2çå¯èªå¢æ°ç»ï¼åå§é¿åº¦ä¸º 30 List < Integer > list3 = new ArrayList <> ( list2 ); // åå»ºä¸ä¸ªåå­ä¸º list3 çå¯èªå¢æ°ç»ï¼ä½¿ç¨ list2 éçå ç´ å size ä½ä¸ºèªå·±çåå§å¼ } } ```   
---|---  
  
#### LinkedList

`LinkedList` æ¯åé¾è¡¨ï¼

##### åå§å

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text import java.io.PrintWriter ; import java.util.LinkedList ; import java.util.List ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); public static void main ( String [] args ) { List < Integer > list1 = new LinkedList <> (); // åå»ºä¸ä¸ªåå­ä¸º list1 çåé¾è¡¨Â List < Integer > list2 = new LinkedList <> ( list1 ); // åå»ºä¸ä¸ªåå­ä¸º list2 çåé¾è¡¨ï¼å° list1 å ææå ç´ å å ¥è¿æ¥Â } } ```   
---|---  
  
#### å¸¸ç¨æ¹æ³

ä»¥ä¸åç¨ `this` ä»£æ¿å½å `List<Integer>`ï¼

å½æ°å| åè½  
---|---  
`size()`| è¿å `this` çé¿åº¦  
`add(Integer val)`| å¨ `this` å°¾é¨æå ¥ `val` å ç´   
`add(int idx, Integer e)`| å¨ `this` ç `idx` ä½ç½®æå ¥ `e` å ç´   
`get(int idx)`| è¿å `this` ä¸­ç¬¬ `idx` ä½ç½®çå¼ï¼è¥è¶çåæåºå¼å¸¸  
`set(int idx, Integer e)`| ä¿®æ¹ `this` ä¸­ç¬¬ `idx` ä½ç½®çå¼ä¸º `e`  
  
ä½¿ç¨æ¡ä¾ååºå«å¯¹æ¯ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text import java.io.PrintWriter ; import java.util.ArrayList ; import java.util.LinkedList ; import java.util.List ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static List < Integer > array = new ArrayList <> (); static List < Integer > linked = new LinkedList <> (); static void add () { array . add ( 1 ); // æ¶é´å¤æåº¦ä¸º O(1)Â linked . add ( 1 ); // æ¶é´å¤æåº¦ä¸º O(1)Â } static void get () { array . get ( 10 ); // æ¶é´å¤æåº¦ä¸º O(1)Â linked . get ( 10 ); // æ¶é´å¤æåº¦ä¸º O(11)Â } static void addIdx () { array . add ( 0 , 2 ); // æåæ åµä¸æ¶é´å¤æåº¦ä¸º O(n) linked . add ( 0 , 2 ); // æåæ åµä¸æ¶é´å¤æåº¦ä¸º O(n) } static void size () { array . size (); // æ¶é´å¤æåº¦ä¸º O(1) linked . size (); // æ¶é´å¤æåº¦ä¸º O(1) } static void set () { // è¯¥æ¹æ³è¿åå¼ä¸ºåæ¬è¯¥ä½ç½®å ç´ çå¼ array . set ( 0 , 1 ); // æ¶é´å¤æåº¦ä¸º O(1) linked . set ( 0 , 1 ); // æåæ¶é´å¤æåº¦ä¸º O(n) } } ```   
---|---  
  
#### éå

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` |  ```text import java.io.PrintWriter ; import java.util.ArrayList ; import java.util.Iterator ; import java.util.LinkedList ; import java.util.List ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static List < Integer > array = new ArrayList <> (); static List < Integer > linked = new LinkedList <> (); static void function1 () { // æ´ç´ éå for ( int i = 0 ; i < array . size (); i ++ ) { out . println ( array . get ( i )); // éåèªå¢æ°ç»ï¼å¤æåº¦ä¸º O(n) } for ( int i = 0 ; i < linked . size (); i ++ ) { out . println ( linked . get ( i )); // éååé¾è¡¨ï¼å¤æåº¦ä¸º O(n^2)ï¼å ä¸º LinkedList ç get(i) å¤æåº¦æ¯ O(i) } } static void function2 () { // å¢å¼º for å¾ªç¯éåÂ for ( int e : array ) { out . println ( e ); } for ( int e : linked ) { out . println ( e ); // å¤æåº¦åä¸º O(n)Â } } static void function3 () { // è¿­ä»£å¨éåÂ Iterator < Integer > iterator1 = array . iterator (); Iterator < Integer > iterator2 = linked . iterator (); while ( iterator1 . hasNext ()) { out . println ( iterator1 . next ()); } while ( iterator2 . hasNext ()) { out . println ( iterator2 . next ()); } // å¤æåº¦åä¸º O(n)Â } } ```   
---|---  
  
æ³¨æ

ä¸è¦å¨ `for` æ `foreach` éå `List` çè¿ç¨ä¸­å é¤å ¶ä¸­çå ç´ ï¼å¦åä¼æåºå¼å¸¸ï¼

åå ä¹å¾ç®åï¼`list.size()` æ¹åäºï¼ä½å¨å¾ªç¯ä¸­å·²å¾ªç¯çæ¬¡æ°å´æ¯æ²¡æéä¹ååï¼åæ¥é¢è®¡å¨ä¸ä¸ä¸ª `index` çæ°æ®å ä¸ºå é¤çæä½åæäºå½å `index` çæ°æ®ï¼è¿è¡ä¸ä¸ä¸ªå¾ªç¯æ¶æä½çä¼åä¸ºåæ¥é¢è®¡å¨ä¸ä¸ä¸ª `index` çæ°æ®ï¼æç»ä¼å¯¼è´æä½çæ°æ®ä¸ç¬¦åé¢æï¼

### Queue

#### LinkedList

å¯ä»¥ä½¿ç¨ `LinkedList` å®ç°æ®ééåï¼åºå±æ¯é¾è¡¨æ¨¡æéåï¼

##### åå§å

```text 1 ``` |  ```text Queue < Integer > q = new LinkedList <> (); ```   
---|---  
  
`LinkedList` åºå±å®ç°äº `List` æ¥å£ä¸ `Deque` æ¥å£ï¼è `Deque` æ¥å£ç»§æ¿èª `Queue` æ¥å£ï¼æä»¥ `LinkedList` å¯ä»¥åæ¶å®ç° `List` ä¸ `Queue`ï¼

#### ArrayDeque

å¯ä»¥ä½¿ç¨ `ArrayDeque` å®ç°æ®ééåï¼åºå±æ¯æ°ç»æ¨¡æéåï¼

##### åå§å

```text 1 ``` |  ```text Queue < Integer > q = new ArrayDeque <> (); ```   
---|---  
  
`ArrayDeque` åºå±å®ç°äº `Deque` æ¥å£ï¼è `Deque` æ¥å£ç»§æ¿èª `Queue` æ¥å£ï¼æä»¥ `ArrayDeque` å¯ä»¥å®ç° `Queue`ï¼

#### LinkedList ä¸ ArrayDeque å¨å®ç° Queue æ¥å£ä¸çåºå«

  1. æ°æ®ç»æï¼å¨æ°æ®ç»æä¸ï¼`ArrayDeque` å `LinkedList` é½å®ç°äº Java Deque åç«¯éåæ¥å£ï¼ä½ `ArrayDeque` æ²¡æå®ç°äº Java List åè¡¨æ¥å£ï¼æä»¥ä¸å ·å¤æ ¹æ®ç´¢å¼ä½ç½®æä½çè¡ä¸ºï¼
  2. çº¿ç¨å®å ¨ï¼`ArrayDeque` å `LinkedList` é½ä¸èèçº¿ç¨åæ­¥ï¼ä¸ä¿è¯çº¿ç¨å®å ¨ï¼
  3. åºå±å®ç°ï¼å¨åºå±å®ç°ä¸ï¼`ArrayDeque` æ¯åºäºå¨ææ°ç»çï¼è `LinkedList` æ¯åºäºååé¾è¡¨çï¼
  4. å¨éåéåº¦ä¸ï¼`ArrayDeque` æ¯ä¸åè¿ç»­å å­ç©ºé´ï¼åºäºå±é¨æ§åçè½å¤æ´å¥½å°å½ä¸­ CPU ç¼å­è¡ï¼è `LinkedList` æ¯ç¦»æ£çå å­ç©ºé´å¯¹ç¼å­è¡ä¸åå¥½ï¼
  5. å¨æä½éåº¦ä¸ï¼`ArrayDeque` å `LinkedList` çæ åéåè¡ä¸ºé½æ¯ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å¤æåº¦ï¼`ArrayDeque` çå ¥æ åå ¥éæå¯è½ä¼è§¦åæ©å®¹ï¼ä½ä»åæåæä¸çä¾ç¶æ¯ ð(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) æ¶é´å¤æåº¦ï¼
  6. é¢å¤å å­æ¶èä¸ï¼`ArrayDeque` å¨æ°ç»çå¤´æéåå°¾æéå¤é¨æé²ç½®ç©ºé´ï¼è `LinkedList` å¨èç¹ä¸å¢å äºåé©±ååç»§æéï¼

#### PriorityQueue

`PriorityQueue` æ¯ä¼å éåï¼é»è®¤æ¯å°æ ¹å ï¼

##### åå§å

```text 1 2 ``` |  ```text Queue < Integer > q1 = new PriorityQueue <> (); // å°æ ¹å  Queue < Integer > q2 = new PriorityQueue <> (( x , y ) -> { return y \- x ;}); // å¤§æ ¹å  ```   
---|---  
  
#### å¸¸ç¨æ¹æ³

ä¸è¡¨ä¸­éåå®ä¹ä¸º `Queue<Integer>`ï¼

å½æ°å| åè½  
---|---  
`size()`| è¿åå½åéåé¿åº¦  
`add(Integer val)`| å° `val` æå ¥éåï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼å°æåºå¼å¸¸  
`offer(Integer val)`| å° `val` æå ¥éåï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼åæå ¥å¤±è´¥ï¼ä½ä¸ä¼æåºå¼å¸¸  
`isEmpty()`| å¤æ­éåæ¯å¦ä¸ºç©ºï¼ä¸ºç©ºåè¿å `true`  
`peek()`| è¿åéå¤´å ç´ ï¼è¥éåä¸ºç©ºè¿å `null`  
`poll()`| è¿åå¹¶å é¤éå¤´å ç´ ï¼è¥éåä¸ºç©ºè¿å `null`  
  
ä½¿ç¨æ¡ä¾ååºå«å¯¹æ¯ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text import java.io.PrintWriter ; import java.util.LinkedList ; import java.util.PriorityQueue ; import java.util.Queue ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Queue < Integer > q1 = new LinkedList <> (); static Queue < Integer > q2 = new PriorityQueue <> (); static void add () { // add å offer åè½ä¸æ²¡æå·®è·ï¼åºå«æ¯æ¯å¦ä¼æåºå¼å¸¸Â q1 . add ( 1 ); // æ¶é´å¤æåº¦ä¸º O(1)Â q2 . add ( 1 ); // æ¶é´å¤æåº¦ä¸º O(logn)Â } static void isEmpty () { q1 . isEmpty (); // æ¶é´å¤æåº¦ä¸º O(1)Â q2 . isEmpty (); // ç©ºé´å¤æåº¦ä¸º O(1)Â } static void size () { q1 . size (); // æ¶é´å¤æåº¦ä¸º O(1)Â q2 . size (); // è¿å q2 çé¿åº¦Â } static void peek () { q1 . peek (); // æ¶é´å¤æåº¦ä¸º O(1)Â q2 . peek (); // æ¶é´å¤æåº¦ä¸º O(logn)Â } static void poll () { q1 . poll (); // æ¶é´å¤æåº¦ä¸º O(1)Â q2 . poll (); // æ¶é´å¤æåº¦ä¸º O(logn)Â } } ```   
---|---  
  
#### éå

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text import java.io.PrintWriter ; import java.util.LinkedList ; import java.util.PriorityQueue ; import java.util.Queue ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Queue < Integer > q1 = new LinkedList <> (); static Queue < Integer > q2 = new PriorityQueue <> (); static void test () { while ( ! q1 . isEmpty ()) { // å¤æåº¦ä¸º O(n)Â out . println ( q1 . poll ()); } while ( ! q2 . isEmpty ()) { // å¤æåº¦ä¸º O(nlogn)Â out . println ( q2 . poll ()); } } } ```   
---|---  
  
### Deque

`Deque` æ¯ `Java` ä¸­çåç«¯éåï¼æä»¬éå¸¸ç¨å ¶è¿è¡éåçæä½ä»¥åæ çæä½ï¼

#### ä¸»è¦å½æ°

ä¸è¡¨ä¸­éåå®ä¹ä¸º `Deque<Integer>`ï¼

å½æ°å| åè½  
---|---  
`addFirst(Integer val)`| å° `val` æå ¥éå¤´ï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼å°æåºå¼å¸¸  
`offerFirst(Integer val)`| å° `val` æå ¥éå¤´ï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼åæå ¥å¤±è´¥ï¼ä½ä¸ä¼æåºå¼å¸¸  
`removeFirst()`| è¿åå¹¶å é¤éå¤´å ç´ ï¼å¦æéåä¸ºç©ºï¼å°æåºå¼å¸¸  
`pollFirst()`| è¿åå¹¶å é¤éå¤´å ç´ ï¼å¦æéåä¸ºç©ºï¼åè¿å `null`  
`peekFirst()`| è¿åéå¤´å ç´ ï¼å¦æéåä¸ºç©ºï¼åè¿å `null`  
`push(Integer val)`| å° `val` æå ¥éå¤´ï¼ç­æäº `addFirst`  
`pop()`| è¿åå¹¶å é¤éå¤´å ç´ ï¼ç­æäº `removeFirst`  
`remove()`| å é¤éå¤´å ç´ ï¼ç­æäº `removeFirst`  
`poll()`| å é¤éå¤´å ç´ ï¼ç­æäº `pollFirst`  
`addLast(Integer val)`| å° `val` æå ¥éå°¾ï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼å°æåºå¼å¸¸  
`offerLast(Integer val)`| å° `val` æå ¥éå°¾ï¼å¦ææå ¥æ¶è¿åäºéåçå®¹ééå¶ï¼åæå ¥å¤±è´¥ï¼ä½ä¸ä¼æåºå¼å¸¸  
`removeLast()`| è¿åå¹¶å é¤éå°¾å ç´ ï¼å¦æéåä¸ºç©ºï¼å°æåºå¼å¸¸  
`pollLast()`| è¿åå¹¶å é¤éå°¾å ç´ ï¼å¦æéåä¸ºç©ºï¼åè¿å `null`  
`peekLast()`| è¿åéå°¾å ç´ ï¼å¦æéåä¸ºç©ºï¼åè¿å `null`  
`add(Integer val)`| å° `val` æå ¥éå°¾ï¼ç­æäº `addLast`  
`offer(Integer val)`| å° `val` æå ¥éå°¾ï¼ç­æäº `offerLast`  
  
#### æ çæä½

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text import java.util.ArrayDeque ; import java.util.Deque ; public class Main { static Deque < Integer > stack = new ArrayDeque <> (); static int [] a = { 1 , 2 , 3 , 4 , 5 }; public static void main ( String [] args ) { for ( int v : a ) { stack . push ( v ); } while ( ! stack . isEmpty ()) { //è¾åº 5 4 3 2 1 System . out . println ( stack . pop ()); } } } ```   
---|---  
  
#### åç«¯éåçæä½

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text import java.util.ArrayDeque ; import java.util.Deque ; public class Main { static Deque < Integer > deque = new ArrayDeque <> (); static void insert () { deque . addFirst ( 1 ); deque . addFirst ( 2 ); deque . addLast ( 3 ); deque . addLast ( 4 ); } public static void main ( String [] args ) { insert (); while ( ! deque . isEmpty ()) { //è¾åº 2 1 3 4 System . out . println ( deque . poll ()); } insert (); while ( ! deque . isEmpty ()) { //è¾åº 4 3 1 2 System . out . println ( deque . pollLast ()); } } } ```   
---|---  
  
### Set

`Set` æ¯ä¿æå®¹å¨ä¸­çå ç´ ä¸éå¤çä¸ç§æ°æ®ç»æï¼

#### HashSet

éæºä½ç½®æå ¥ç `Set`ï¼

##### åå§å

```text 1 ``` |  ```text Set < Integer > s1 = new HashSet <> (); ```   
---|---  
  
#### LinkedHashSet

ä¿ææå ¥é¡ºåºç `Set`ï¼

##### åå§å

```text 1 ``` |  ```text Set < Integer > s2 = new LinkedHashSet <> (); ```   
---|---  
  
#### TreeSet

ä¿æå®¹å¨ä¸­å ç´ æåºç `Set`ï¼é»è®¤ä¸ºååºï¼

##### åå§å

```text 1 2 ``` |  ```text Set < Integer > s3 = new TreeSet <> (); Set < Integer > s4 = new TreeSet <> (( x , y ) -> { return y \- x ;}); // éåºÂ ```   
---|---  
  
##### TreeSet çæ´å¤ä½¿ç¨

è¿äºæ¹æ³æ¯ `TreeSet` æ°åå»ºå¹¶å®ç°çï¼æä»¬æ æ³ä½¿ç¨ `Set` æ¥å£è°ç¨ä»¥ä¸æ¹æ³ï¼å æ­¤æä»¬åå»ºæ¹å¼å¦ä¸ï¼

```text 1 2 ``` |  ```text TreeSet < Integer > s3 = new TreeSet <> (); TreeSet < Integer > s4 = new TreeSet <> (( x , y ) -> { return y \- x ;}); // éåº ```   
---|---  
  
ä¸è¡¨ä¸­åç¨ `this` ä»£æ¿å½å `TreeSet<Integer>`ï¼

å½æ°å| åè½  
---|---  
`first()`| è¿å `this` ä¸­ç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`last()`| è¿å `this` ä¸­æåä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`floor(Integer val)`| è¿å `this` ä¸­å°äºç­äº `val` çç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`ceiling(Integer val)`| è¿å `this` ä¸­å¤§äºç­äº `val` çç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`higher(Integer val)`| è¿å `this` ä¸­å¤§äº `val` çç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`lower(Integer val)`| è¿å `this` ä¸­å°äº `val` çç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`pollFirst()`| è¿åå¹¶å é¤ `this` ä¸­ç¬¬ä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
`pollLast()`| è¿åå¹¶å é¤ `this` ä¸­æåä¸ä¸ªå ç´ ï¼æ åè¿å `null`  
  
ä»£ç ç¤ºä¾ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text import java.util.TreeSet ; public class Main { static int [] a = { 4 , 7 , 1 , 2 , 3 , 6 }; public static void main ( String [] args ) { TreeSet < Integer > set = new TreeSet <> (); for ( int v : a ) { set . add ( v ); } Integer a2 = set . first (); System . out . println ( a2 ); //è¿å 1 Integer a3 = set . last (); System . out . println ( a3 ); //è¿å 7 Integer a4 = set . floor ( 5 ); System . out . println ( a4 ); //è¿å 4 Integer a5 = set . ceiling ( 6 ); System . out . println ( a5 ); //è¿å 6 Integer a6 = set . higher ( 7 ); System . out . println ( a6 ); //è¿å null Integer a7 = set . lower ( 2 ); System . out . println ( a7 ); //è¿å 1 Integer a8 = set . pollFirst (); System . out . println ( a8 ); //è¿å 1 Integer a9 = set . pollLast (); System . out . println ( a9 ); //è¿å 7 } } ```   
---|---  
  
#### Set å¸¸ç¨æ¹æ³

å½æ°å| åè½  
---|---  
`size()`| è¿åå½åéåçå¤§å°  
`add(Integer val)`| å° `val` æå ¥éå  
`contains(Integer val)`| å¤æ­éåä¸­æ¯å¦æå ç´ `val`  
`addAll(Collection e)`| å°å®¹å¨ `e` éçææå ç´ æ·»å è¿å½åéå  
`retainAll(Collection e)`| å é¤å½åéåä¸­æªåºç°å¨å®¹å¨ `e` ä¸­çå ç´ ï¼å³æ±å½åéåä¸ `e` çäº¤é  
`removeAll(Collection e)`| å é¤å½åéåä¸­åºç°å¨å®¹å¨ `e` ä¸­çå ç´ ï¼å³æ±å½åéåä¸ `e` çå·®é  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text import java.io.PrintWriter ; import java.util.HashSet ; import java.util.LinkedHashSet ; import java.util.Set ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Set < Integer > s1 = new HashSet <> (); static Set < Integer > s2 = new LinkedHashSet <> (); static void add () { s1 . add ( 1 ); } static void contains () { // å¤æ­ set ä¸­æ¯å¦æå ç´ å¼ä¸º 2ï¼æåè¿å trueï¼å¦åè¿å falseÂ s1 . contains ( 2 ); } static void test1 () { // s1 ä¸ s2 çå¹¶éÂ Set < Integer > res = new HashSet <> (); res . addAll ( s1 ); res . addAll ( s2 ); } static void test2 () { // s1 ä¸ s2 çäº¤éÂ Set < Integer > res = new HashSet <> (); res . addAll ( s1 ); res . retainAll ( s2 ); } static void test3 () { // å·®éï¼s1 - s2Â Set < Integer > res = new HashSet <> (); res . addAll ( s1 ); res . removeAll ( s2 ); } } ```   
---|---  
  
#### éå

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text import java.io.PrintWriter ; import java.util.HashSet ; import java.util.LinkedHashSet ; import java.util.Set ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Set < Integer > s1 = new HashSet <> (); static Set < Integer > s2 = new LinkedHashSet <> (); static void test () { for ( int key : s1 ) { out . println ( key ); } out . close (); } } ```   
---|---  
  
### Map

`Map` æ¯ç»´æ¤é®å¼å¯¹ `<Key, Value>` çä¸ç§æ°æ®ç»æï¼å ¶ä¸­ `Key` å¯ä¸ï¼

#### HashMap

éæºä½ç½®æå ¥ç `Map`ï¼

##### åå§å

```text 1 ``` |  ```text Map < Integer , Integer > map1 = new HashMap <> (); ```   
---|---  
  
#### LinkedHashMap

ä¿ææå ¥é¡ºåºç `Map`ï¼

##### åå§å

```text 1 ``` |  ```text Map < Integer , Integer > map2 = new LinkedHashMap <> (); ```   
---|---  
  
#### TreeMap

ä¿æ `key` æåºç `Map`ï¼é»è®¤ååºï¼

##### åå§å

```text 1 2 ``` |  ```text Map < Integer , Integer > map3 = new TreeMap <> (); Map < Integer , Integer > map4 = new TreeMap <> (( x , y ) -> { return y \- x ;}); // éåº ```   
---|---  
  
#### å¸¸ç¨æ¹æ³

ä»¥ä¸åç¨ `this` ä»£æ¿å½å `Map<Integer, Integer>`ï¼

å½æ°å| åè½  
---|---  
`put(Integer key, Integer value)`| å° `<key, value>` æå ¥ `this`  
`size()`| è¿å `this` çå¤§å°  
`containsKey(Integer key)`| å¤æ­ `this` ä¸­æ¯å¦æå­å¨æä¸ªå ç´ çé®ä¸º `key`  
`get(Integer key)`| è¿å `this` ä¸­é®ä¸º `key` çå ç´ å¯¹åºçå¼  
`keySet()`| å° `this` ä¸­ææå ç´ çé®ä½ä¸ºéåè¿å  
  
ä½¿ç¨æ¡ä¾ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text import java.io.PrintWriter ; import java.util.HashMap ; import java.util.LinkedHashMap ; import java.util.Map ; import java.util.TreeMap ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Map < Integer , Integer > map1 = new HashMap <> (); static Map < Integer , Integer > map2 = new LinkedHashMap <> (); static Map < Integer , Integer > map3 = new TreeMap <> (); static Map < Integer , Integer > map4 = new TreeMap <> (( x , y ) -> { return y \- x ;}); static void put (){ // å° key ä¸º 1ãvalue ä¸º 1 çå ç´ è¿å map1 . put ( 1 , 1 ); } static void get (){ // å° key ä¸º 1 ç value è¿å map1 . get ( 1 ); } static void containsKey (){ // å¤æ­æ¯å¦æ key ä¸º 1 çé®å¼å¯¹ map1 . containsKey ( 1 ); } static void KeySet (){ map1 . keySet (); } } ```   
---|---  
  
#### éå

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text import java.io.PrintWriter ; import java.util.HashMap ; import java.util.Map ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static Map < Integer , Integer > map1 = new HashMap <> (); static void print () { for ( int key : map1 . keySet ()) { out . println ( key \+ " " \+ map1 . get ( key )); } } } ```   
---|---  
  
å½ç¶ï¼é®å¼çç±»åä¹å¯ä»¥æ´æ¹ï¼ä¾å¦ `Map` ä¹å¯ä»¥å®ä¹ä¸ºï¼

```text 1 ``` |  ```text Map < String , Set < Integer >> map = new HashMap <> (); ```   
---|---  
  
## Arrays

`Arrays` æ¯ `java.util` ä¸­å¯¹æ°ç»æä½çä¸ä¸ªå·¥å ·ç±»ï¼æ¹æ³åä¸ºéææ¹æ³ï¼å¯ä½¿ç¨ç±»åç´æ¥è°ç¨ï¼

### Arrays.sort()

`Arrays.sort()` æ¯å¯¹æ°ç»è¿è¡çæåºçæ¹æ³ï¼ä¸»è¦éè½½æ¹æ³å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` |  ```text import java.util.Arrays ; import java.util.Comparator ; public class Main { static int [] a = new int [ 10 ] ; static Integer [] b = new Integer [ 10 ] ; static int firstIdx , lastIdx ; public static void main ( String [] args ) { Arrays . sort ( a ); // 1Â Arrays . sort ( a , firstIdx , lastIdx ); // 2Â Arrays . sort ( b , new Comparator < Integer > () { // 3Â @Override public int compare ( Integer o1 , Integer o2 ) { return o2 \- o1 ; } }); Arrays . sort ( b , firstIdx , lastIdx , new Comparator < Integer > () { // 4Â @Override public int compare ( Integer o1 , Integer o2 ) { return o2 \- o1 ; } }); // ç±äº Java 8 åæ Lambda è¡¨è¾¾å¼ï¼ç¬¬ä¸ä¸ªéè½½åç¬¬åä¸ªéè½½äº¦å¯åä¸ºÂ Arrays . sort ( b , ( x , y ) -> { // 5Â return y \- x ; }); Arrays . sort ( b , ( x , y ) -> { // 6Â return y \- x ; }); } } ```   
---|---  
  
åºå·æå¯¹åºçéè½½æ¹æ³å«ä¹ï¼

  1. å¯¹æ°ç» `a` è¿è¡æåºï¼é»è®¤ååºï¼
  2. å¯¹æ°ç» `a` çæå®ä½ç½®è¿è¡æåºï¼é»è®¤ååºï¼æåºåºé´ä¸ºå·¦é­å³å¼ `[firstIdx, lastIdx)`ï¼
  3. å¯¹æ°ç» `a` ä»¥èªå®ä¹çå½¢å¼æåºï¼ç¬¬äºä¸ªåæ° `-` ç¬¬ä¸ä¸ªåæ°ä¸ºéåºï¼ç¬¬ä¸ä¸ªåæ° `-` ç¬¬äºä¸ªåæ°ä¸ºååºï¼å½èªå®ä¹æåºæ¯è¾å¨æ¶ï¼æ°ç»å ç´ ç±»åå¿ é¡»ä¸ºå¯¹è±¡ç±»åï¼
  4. å¯¹æ°ç» `a` çæå®ä½ç½®è¿è¡èªå®ä¹æåºï¼æåºåºé´ä¸ºå·¦é­å³å¼ `[firstIdx, lastIdx)`ï¼å½èªå®ä¹æåºæ¯è¾å¨æ¶ï¼æ°ç»å ç´ ç±»åå¿ é¡»ä¸ºå¯¹è±¡ç±»åï¼
  5. å 3 åçï¼ç¨ Lambda è¡¨è¾¾å¼ä¼åäºä»£ç é¿åº¦ï¼
  6. å 4 åçï¼ç¨ Lambda è¡¨è¾¾å¼ä¼åäºä»£ç é¿åº¦ï¼

`Arrays.sort()` åºå±å½æ°

  1. å½ `Arrays.sort` çåæ°æ°ç»å ç´ ç±»åä¸ºåºæ¬æ°æ®ç±»åï¼`byte`ã`short`ã`char`ã`int`ã`long`ã`double`ã`float`ï¼æ¶ï¼é»è®¤ä¸º `DualPivotQuicksort`ï¼åè½´å¿«æï¼ï¼å¤æåº¦æåå¯ä»¥è¾¾å° ð(ð2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼
  2. å½ `Arrays.sort` çåæ°æ°ç»å ç´ ç±»åä¸ºéåºæ¬æ°æ®ç±»åæ¶ï¼åé»è®¤ä¸º `legacyMergeSort` å `TimSort`ï¼å½å¹¶æåºï¼ï¼å¤æåº¦ä¸º ð(ðlogâ¡ð)O(nlogâ¡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼

å¯ä»¥éè¿å¦ä¸ä»£ç éªè¯ï¼

[Codeforces 1646B - Quality vs Quantity](https://codeforces.com/problemset/problem/1646/B)

æ ðn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ä¸ªæ´æ°ï¼ä½ éè¦å°å ¶åä¸ºä¸¤ç»ï¼æ¯å¦è½å­å¨æä¸ç»çé¿åº¦å°äºå¦ä¸ç»ï¼åæ¶åå¤§äºå®ï¼

ä¾é¢ä»£ç 

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 ``` |  ```text import java.io.BufferedReader ; import java.io.IOException ; import java.io.InputStreamReader ; import java.io.PrintWriter ; import java.util.Arrays ; import java.util.StringTokenizer ; public class Main { static class FastReader { StringTokenizer st ; BufferedReader br ; public FastReader () { br = new BufferedReader ( new InputStreamReader ( System . in )); } String next () { while ( st == null || ! st . hasMoreElements ()) { try { st = new StringTokenizer ( br . readLine ()); } catch ( IOException e ) { e . printStackTrace (); } } return st . nextToken (); } int nextInt () { return Integer . parseInt ( next ()); } long nextLong () { return Long . parseLong ( next ()); } double nextDouble () { return Double . parseDouble ( next ()); } String nextLine () { String str = "" ; try { str = br . readLine (); } catch ( IOException e ) { e . printStackTrace (); } return str ; } } static PrintWriter out = new PrintWriter ( System . out ); static FastReader in = new FastReader (); static void solve () { int n = in . nextInt (); // æ­¤å¤æ°ç»ç±»åç± Integer ä¿®æ¹ä¸º int ä¼å¯¼è´ TLE Integer [] a = new Integer [ n \+ 10 ] ; for ( int i = 1 ; i <= n ; i ++ ) { a [ i ] = in . nextInt (); } Arrays . sort ( a , 1 , n \+ 1 ); long left = a [ 1 ] ; long right = 0 ; int x = n ; for ( int i = 2 ; i < x ; i ++ , x \-- ) { left = left \+ a [ i ] ; right = right \+ a [ x ] ; if ( right > left ) { out . println ( "YES" ); return ; } } out . println ( "NO" ); } public static void main ( String [] args ) { int t = in . nextInt (); while ( t \-- > 0 ) { solve (); } out . close (); } } ```   
---|---  
  
### Arrays.binarySearch()

`Arrays.binarySearch()` æ¯å¯¹æ°ç»è¿ç»­åºé´è¿è¡äºåæç´¢çæ¹æ³ï¼åææ¯æ°ç»å¿ é¡»æåºï¼æ¶é´å¤æåº¦ä¸º ð(logð)O(logn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ï¼ä¸»è¦éè½½æ¹æ³å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text import java.util.Arrays ; public class Main { static int [] a = new int [ 10 ] ; static Integer [] b = new Integer [ 10 ] ; static int firstIdx , lastIdx ; static int key ; public static void main ( String [] args ) { Arrays . binarySearch ( a , key ); // 1Â Arrays . binarySearch ( a , firstIdx , lastIdx , key ); // 2Â } } ```   
---|---  
  
æºç å¦ä¸ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text private static int binarySearch0 ( int [] a , int fromIndex , int toIndex , int key ) { int low = fromIndex ; int high = toIndex \- 1 ; while ( low <= high ) { int mid = ( low \+ high ) >>> 1 ; int midVal = a [ mid ] ; if ( midVal < key ) low = mid \+ 1 ; else if ( midVal > key ) high = mid \- 1 ; else return mid ; // key found } return \- ( low \+ 1 ); // key not found. } ```   
---|---  
  
åºå·æå¯¹åºçéè½½æ¹æ³å«ä¹ï¼

  1. ä»æ°ç» a ä¸­äºåæ¥æ¾æ¯å¦å­å¨ `key`ï¼å¦æå­å¨ï¼ä¾¿è¿åå ¶ä¸æ ï¼è¥ä¸å­å¨ï¼åè¿åä¸ä¸ªè´æ°ï¼
  2. ä»æ°ç» a ä¸­äºåæ¥æ¾æ¯å¦å­å¨ `key`ï¼å¦æå­å¨ï¼ä¾¿è¿åå ¶ä¸æ ï¼æç´¢åºé´ä¸ºå·¦é­å³å¼ `[firstIdx,lastIdx)`ï¼è¥ä¸å­å¨ï¼åè¿åä¸ä¸ªè´æ°ï¼

### Arrays.fill()

`Arrays.fill()` æ¹æ³å°æ°ç»ä¸­è¿ç»­ä½ç½®çå ç´ èµå¼ä¸ºç»ä¸å ç´ ï¼å ¶æ¥åçåæ°ä¸ºæ°ç»ã`fromIndex`ã`toIndex` åéè¦å¡«å çæ°ï¼æ¹æ³æ§è¡åï¼æ°ç»å·¦é­å³å¼åºé´ `[firstIdx,lastIdx)` å çææå ç´ çå¼åä¸ºéè¦å¡«å çæ°ï¼

## Collections

`Collections` æ¯ `java.util` ä¸­å¯¹éåæä½çä¸ä¸ªå·¥å ·ç±»ï¼æ¹æ³åä¸ºéææ¹æ³ï¼å¯ä½¿ç¨ç±»åç´æ¥è°ç¨ï¼

### Collections.sort()

`Collections.sort()` åºå±åçä¸ºå°å ¶ä¸­ææå ç´ è½¬åä¸ºæ°ç»è°ç¨ `Arrays.sort()`ï¼å®ææåºååèµå¼ç»åæ¬çéåï¼åå ä¸º Java ä¸­ `Collection` çå ç´ ç±»ååä¸ºå¯¹è±¡ç±»åï¼æä»¥å§ç»æ¯å½å¹¶æåºå»å¤çï¼

è¯¥æ¹æ³æ æ³å¯¹éåæå®åºé´æåºï¼

åºå±æºç ï¼

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text default void sort ( Comparator <? super E > c ) { Object [] a = this . toArray (); Arrays . sort ( a , ( Comparator ) c ); ListIterator < E > i = this . listIterator (); for ( Object e : a ) { i . next (); i . set (( E ) e ); } } ```   
---|---  
  
### Collections.binarySearch()

`Collections.binarySearch()` æ¯å¯¹éåä¸­æå®åºé´è¿è¡äºåæç´¢ï¼åè½ä¸ `Arrays.binarySearch()` ç¸åï¼

```text 1 ``` |  ```text Collections . binarySearch ( list , key ); ```   
---|---  
  
è¯¥æ¹æ³æ æ³å¯¹æå®åºé´è¿è¡æç´¢ï¼

### Collections.swap()

`Collections.swap()` çåè½æ¯äº¤æ¢éåä¸­æå®äºä¸ªä½ç½®çå ç´ ï¼

```text 1 ``` |  ```text Collections . swap ( list , i , j ); ```   
---|---  
  
## å ¶ä»

### æ°å¼æ¯è¾é®é¢

å¨ Java ä¸­ï¼å¦æåçº¯æ¯æ°å¼ç±»åï¼`-0.0 = 0.0`ï¼è¥æ¯å¯¹è±¡ç±»åï¼å `-0.0 != 0.0`ï¼å¦æå°è¯ç¨ `Set` ç»è®¡æçæ°éæ¶ï¼è¿ä¸ªé®é¢å°±ä¼å¸¦æ¥éº»ç¦ï¼æä¾çè§£å³æ¹å¼æ¯å¨ææçæçå å ¥ `Set` åå°å¼å¢å `0.0`ï¼

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text import java.io.PrintWriter ; public class Main { static PrintWriter out = new PrintWriter ( System . out ); static void A () { Double a = 0.0 ; Double b = \- 0.0 ; out . println ( a . equals ( b )); // falseÂ } static void B () { Double a = 0.0 ; Double b = \- 0.0 \+ 0.0 ; out . println ( a . equals ( b )); // trueÂ } static void C () { double a = 0.0 ; double b = \- 0.0 ; out . println ( a == b ); // trueÂ } public static void main ( String [] args ) { A (); B (); C (); out . close (); } } ```   
---|---  
  
## åèèµæ

* * *

  1. [Input & Output - USACO Guide](https://usaco.guide/general/input-output?lang=java#method-3---io-template)Â â©

* * *

>  __æ¬é¡µé¢æè¿æ´æ°ï¼ 2026/1/7 08:56:54ï¼[æ´æ°åå²](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/java-pro.md)  
>  __åç°éè¯¯ï¼æ³ä¸èµ·å®åï¼[å¨ GitHub ä¸ç¼è¾æ­¤é¡µï¼](https://oi-wiki.org/edit-landing/?ref=/lang/java-pro.md "edit.link.title")  
>  __æ¬é¡µé¢è´¡ç®è ï¼[Tiphereth-A](https://github.com/Tiphereth-A), [1804040636](https://github.com/1804040636), [aofall](https://github.com/aofall), [HeRaNO](https://github.com/HeRaNO), [shuzhouliu](https://github.com/shuzhouliu), [yusancky](https://github.com/yusancky), [c-forrest](https://github.com/c-forrest), [caopengrun](https://github.com/caopengrun), [CCXXXI](https://github.com/CCXXXI), [ImpleLee](https://github.com/ImpleLee), [megakite](https://github.com/megakite), [optimize-2](https://github.com/optimize-2), [Qubik65536](https://github.com/Qubik65536), [untitledunrevised](https://github.com/untitledunrevised), [ZnPdCo](https://github.com/ZnPdCo)  
>  __æ¬é¡µé¢çå ¨é¨å å®¹å¨**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) å [SATA](https://github.com/zTrix/sata-license)** åè®®ä¹æ¡æ¬¾ä¸æä¾ï¼éå æ¡æ¬¾äº¦å¯è½åºç¨
