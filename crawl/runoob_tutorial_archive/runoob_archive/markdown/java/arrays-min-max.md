# Java 实例 - 数组获取最大和最小值

- Source: https://www.runoob.com/java/arrays-min-max.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过 Collections 类的 Collections.max() 和 Collections.min() 方法来查找数组中的最大和最小值：


## Main.java 文件



```java
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        Integer[] numbers = { 8, 2, 7, 1, 4, 9, 5};
        int min = (int) Collections.min(Arrays.asList(numbers));
        int max = (int) Collections.max(Arrays.asList(numbers));
        System.out.println("最小值: " + min);
        System.out.println("最大值: " + max);
    }
}
```


以上代码运行输出结果为：


```
最小值: 1
最大值: 9
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组输出](https://www.runoob.com/arrays-output.html)
			[Java 实例 – 数组合并](https://www.runoob.com/arrays_merge.html) **