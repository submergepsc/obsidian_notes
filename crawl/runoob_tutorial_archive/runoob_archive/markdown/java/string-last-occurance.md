# Java 实例 - 查找字符串最后一次出现的位置

- Source: https://www.runoob.com/java/string-last-occurance.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)

以下实例中我们通过字符串函数 strOrig.lastIndexOf(Stringname) 来查找子字符串 Stringname 在 strOrig 出现的位置：


实例代码如下：


## SearchlastString.java 文件



```java
public class SearchlastString {
   public static void main(String[] args) {
      String strOrig = "Hello world ,Hello Runoob";
      int lastIndex = strOrig.lastIndexOf("Runoob");
      if(lastIndex == - 1){
         System.out.println("没有找到字符串 Runoob");
      }else{
         System.out.println("Runoob 字符串最后出现的位置： "+ lastIndex);
      }
   }
}
```


以上代码实例输出结果为：


```
Runoob 字符串最后出现的位置： 19
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例](https://www.runoob.com/java-examples.html)
			[Java 实例 – 删除字符串中的一个字符](https://www.runoob.com/string-removing-char.html) **