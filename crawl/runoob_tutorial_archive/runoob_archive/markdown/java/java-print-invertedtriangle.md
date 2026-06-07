# Java 实例 – 打印倒立的三角形

- Source: https://www.runoob.com/java/java-print-invertedtriangle.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


打印倒立的三角形。


## 实例



```java
public class InvertedTriangle {
    public static void main(String[] args) {
         //打印倒立的三角形
        for (int m = 1; m <= 4; m++) {
            //打印空格
            for (int n = 0; n <= m; n++) {
                System.out.print(" ");
            }
            //打印*
            for (int x = 1; x <= 7 -2 * (m - 1); x++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```


输出结果：


```
*******
   *****
    ***
     *
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 打印平行四边形](https://www.runoob.com/java-print-parallelogram.html)
			[Java 实例 – 字符串分隔(StringTokenizer)](https://www.runoob.com/java-stringtokenizer-example.html) **