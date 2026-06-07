# Java 实例 - 数组填充

- Source: https://www.runoob.com/java/arrays-fill.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例我们通过 Java Util 类的 Arrays.fill(arrayname,value) 方法和Arrays.fill(arrayname ,starting index ,ending index ,value) 方法向数组中填充元素：


## Main.java 文件



```java
import java.util.*;

public class FillTest {
    public static void main(String args[]) {
        int array[] = new int[6];
        Arrays.fill(array, 100);
        for (int i=0, n=array.length; i < n; i++) {
            System.out.println(array[i]);
        }
        System.out.println();
        Arrays.fill(array, 3, 6, 50);
        for (int i=0, n=array.length; i< n; i++) {
            System.out.println(array[i]);
        }
    }
}
```


以上代码运行输出结果为：


```
100
100
100
100
100
100

100
100
100
50
50
50
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组合并](https://www.runoob.com/arrays_merge.html)
			[Java 实例 – 数组扩容](https://www.runoob.com/arrays-extension.html) **