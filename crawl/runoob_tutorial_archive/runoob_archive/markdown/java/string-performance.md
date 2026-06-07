# Java 实例 - 字符串性能比较测试

- Source: https://www.runoob.com/java/string-performance.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了通过两种方式创建字符串，并测试其性能：


## StringComparePerformance.java 文件



```java
public class StringComparePerformance{
   public static void main(String[] args){
      long startTime = System.currentTimeMillis();
      for(int i=0;i<50000;i++){
         String s1 = "hello";
         String s2 = "hello";
      }
      long endTime = System.currentTimeMillis();
      System.out.println("通过 String 关键词创建字符串"
      + " : "+ (endTime - startTime)
      + " 毫秒" );
      long startTime1 = System.currentTimeMillis();
      for(int i=0;i<50000;i++){
         String s3 = new String("hello");
         String s4 = new String("hello");
      }
      long endTime1 = System.currentTimeMillis();
      System.out.println("通过 String 对象创建字符串"
      + " : " + (endTime1 - startTime1)
      + " 毫秒");
   }
}
```


以上代码实例输出结果为：


```
通过 String 关键词创建字符串 : 6 毫秒
通过 String 对象创建字符串 : 14 毫秒
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 测试两个字符串区域是否相等](https://www.runoob.com/string-regionmatch.html)
			[Java 实例 – 字符串优化](https://www.runoob.com/string-optimization.html) **