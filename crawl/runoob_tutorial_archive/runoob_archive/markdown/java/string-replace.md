# Java 实例 - 字符串替换

- Source: https://www.runoob.com/java/string-replace.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


如何使用java替换字符串中的字符呢？


以下实例中我们使用 java String 类的 replace 方法来替换字符串中的字符：


## StringReplaceEmp.java 文件



```java
public class StringReplaceEmp{
   public static void main(String args[]){
      String str="Hello World";
      System.out.println( str.replace( 'H','W' ) );
      System.out.println( str.replaceFirst("He", "Wa") );
      System.out.println( str.replaceAll("He", "Ha") );
   }
}
```


以上代码实例输出结果为：


```
Wello World
Wallo World
Hallo World
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 删除字符串中的一个字符](https://www.runoob.com/string-removing-char.html)
			[Java 实例 – 字符串反转](https://www.runoob.com/string-reverse.html) **