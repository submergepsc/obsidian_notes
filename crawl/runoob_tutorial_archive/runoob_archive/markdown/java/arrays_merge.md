# Java 实例 - 数组合并

- Source: https://www.runoob.com/java/arrays_merge.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过 List 类的 Arrays.toString () 方法和 List 类的 list.Addall(array1.asList(array2) 方法将两个数组合并为一个数组：


## Main.java 文件



```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String args[]) {
        String a[] = { "A", "E", "I" };
        String b[] = { "O", "U" };
        List list = new ArrayList(Arrays.asList(a));
        list.addAll(Arrays.asList(b));
        Object[] c = list.toArray();
        System.out.println(Arrays.toString(c));
    }
}
```


以上代码运行输出结果为：


```
[A, E, I, O, U]
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组获取最大和最小值](https://www.runoob.com/arrays-min-max.html)
			[Java 实例 – 数组填充](https://www.runoob.com/arrays-fill.html) **