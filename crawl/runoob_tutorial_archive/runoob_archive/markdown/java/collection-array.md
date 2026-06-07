# Java 实例 - 数组转集合

- Source: https://www.runoob.com/java/collection-array.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了使用 Java Util 类的 Arrays.asList(name) 方法将数组转换为集合：


## ArrayToCollection.java 文件



```java
import java.util.*;
import java.io.*;

public class ArrayToCollection{
   public static void main(String args[])
   throws IOException{
      int n = 5;         // 5 个元素
      String[] name = new String[n];
      for(int i = 0; i < n; i++){
         name[i] = String.valueOf(i);
      }
      List<String> list = Arrays.asList(name);
      System.out.println();
      for(String li: list){
         String str = li;
         System.out.print(str + " ");
      }
   }
}
```


以上代码运行输出结果为：


```
0 1 2 3 4
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 删除链表中的元素](https://www.runoob.com/data-replace.html)
			[Java 实例 – 集合比较](https://www.runoob.com/collection-compare.html) **