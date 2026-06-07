# Java 实例 – 打印菱形

- Source: https://www.runoob.com/java/java-print-diamond.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


输出指定行数的菱形。


## 实例



```java
public class Diamond {
    public static void main(String[] args) {
        print(8); // 输出 8 行的菱形
    }

    public static void print(int size) {
        if (size % 2 == 0) {
            size++; // 计算菱形大小
        }
        for (int i = 0; i < size / 2 + 1; i++) {
            for (int j = size / 2 + 1; j > i + 1; j--) {
                System.out.print(" "); // 输出左上角位置的空白
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*"); // 输出菱形上半部边缘
            }
            System.out.println(); // 换行
        }
        for (int i = size / 2 + 1; i < size; i++) {
            for (int j = 0; j < i - size / 2; j++) {
                System.out.print(" "); // 输出菱形左下角空白
            }
            for (int j = 0; j < 2 * size - 1 - 2 * i; j++) {
                System.out.print("*"); // 输出菱形下半部边缘
            }
            System.out.println(); // 换行
        }
    }
}
```


输出结果：


```
*
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java MySQL 连接](https://www.runoob.com/java-mysql-connect.html)
			[Java 实例 – 九九乘法表](https://www.runoob.com/java-print-multiplicationtable.html) **