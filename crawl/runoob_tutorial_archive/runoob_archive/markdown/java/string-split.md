# Java 实例 - 字符串分割

- Source: https://www.runoob.com/java/string-split.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例使用了 split(string) 方法通过指定分隔符将字符串分割为数组：


## JavaStringSplitEmp.java 文件



```java
public class JavaStringSplitEmp {
   public static void main(String args[]){

      String str = "www-runoob-com";
      String[] temp;
      String delimeter = "-";  // 指定分割字符
      temp = str.split(delimeter); // 分割字符串
      // 普通 for 循环
      for(int i =0; i < temp.length ; i++){
         System.out.println(temp[i]);
         System.out.println("");
      }

      System.out.println("------java for each循环输出的方法-----");
      String str1 = "www.runoob.com";
      String[] temp1;
      String delimeter1 = "\\.";  // 指定分割字符， . 号需要转义
      temp1 = str1.split(delimeter1); // 分割字符串
      for(String x :  temp1){
         System.out.println(x);
         System.out.println("");
      }
   }
}
```


以上代码实例输出结果为：


```
www

runoob

com

------java for each循环输出的方法-----
www

runoob

com
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 字符串查找](https://www.runoob.com/string-search.html)
			[Java 实例 – 字符串小写转大写](https://www.runoob.com/string-uppercase.html) **