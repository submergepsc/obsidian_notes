# Java 实例 - 获取数组长度

- Source: https://www.runoob.com/java/arrays-upperbound.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


本文我们将为大家介绍如何使用数组的属性 length 来获取数组的长度。


以下实例中我们定义了二维数组，并获取数组的长度：


## Main.java 文件



```java
public class Main {
   public static void main(String args[]) {
      String[][] data = new String[2][5];
      System.out.println("第一维数组长度: " + data.length);
      System.out.println("第二维数组长度: " + data[0].length);
   }
}
```


以上代码运行输出结果为：


```
第一维数组长度: 2
第二维数组长度: 5
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组添加元素](https://www.runoob.com/arrays-insert.html)
			[Java 实例 – 数组反转](https://www.runoob.com/arrays-reverse.html) **