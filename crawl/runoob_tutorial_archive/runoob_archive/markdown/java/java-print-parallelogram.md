# Java 实例 – 打印平行四边形

- Source: https://www.runoob.com/java/java-print-parallelogram.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


输出平行四边形。


## 实例



```java
public class Parallelogram {
    public static void main(String[] args) {
         //外层循环 每次打出一个*
        for (int i = 1; i <=5; i++) {
            //填充空格
            for (int j = 1; j <= 5 - i; j++) {
                System.out.print(" ");
            }
            //内层循环 每次打印一个*
            for (int k = 1; k <= 5; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```


输出结果：


```
*****
   *****
  *****
 *****
*****
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 打印矩形](https://www.runoob.com/java-print-rect.html)
			[Java 实例 – 打印倒立的三角形](https://www.runoob.com/java-print-invertedtriangle.html) **