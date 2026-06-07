# Java 实例 – 打印矩形

- Source: https://www.runoob.com/java/java-print-rect.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


输出矩形。


## 实例



```java
public class Rect {
    public static void main(String[] args) {
         //外层循环 每次输出一行*
        for (int i = 1; i <= 5; i++) {
            System.out.print("*");
            //内层循环 每次输出一个*
            for (int j = 1; j <= 5; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```


输出结果：


```
******
******
******
******
******
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 九九乘法表](https://www.runoob.com/java-print-multiplicationtable.html)
			[Java 实例 – 打印平行四边形](https://www.runoob.com/java-print-parallelogram.html) **