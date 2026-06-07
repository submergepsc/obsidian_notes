# Java 实例 - 字符串比较

- Source: https://www.runoob.com/java/string-compare.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例中我们通过字符串函数 compareTo (string) ，compareToIgnoreCase(String) 及 compareTo(object string) 来比较两个字符串，并返回字符串中第一个字母ASCII的差值。


实例代码如下：


## StringCompareEmp.java 文件



```java
public class StringCompareEmp{
   public static void main(String args[]){
      String str = "Hello World";
      String anotherString = "hello world";
      Object objStr = str;

      System.out.println( str.compareTo(anotherString) );
      System.out.println( str.compareToIgnoreCase(anotherString) );  //忽略大小写
      System.out.println( str.compareTo(objStr.toString()));
   }
}
```


以上代码实例输出结果为：


```
-32
0
0
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 如何查看当前 Java 运行的版本?](https://www.runoob.com/env-version.html)
			[Java 实例](https://www.runoob.com/java-examples.html) **