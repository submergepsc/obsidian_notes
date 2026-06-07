# Java 实例 - List 循环移动元素

- Source: https://www.runoob.com/java/collection-rotate.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 Collections 类的 rotate() 来循环移动元素，方法第二个参数指定了移动的起始位置：


## Main.java 文件



```java
import java.util.*;

public class Main {
   public static void main(String[] args) {
      List list = Arrays.asList("one Two three Four five six".split(" "));
      System.out.println("List :"+list);
      Collections.rotate(list, 3);
      System.out.println("rotate: " + list);
   }
}
```


以上代码运行输出结果为：


```
List :[one, Two, three, Four, five, six]
rotate: [Four, five, six, one, Two, three]
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – List 元素替换](https://www.runoob.com/collection-replace.html)
			[Java 实例 – 获取指定主机的IP地址](https://www.runoob.com/net-address.html) **