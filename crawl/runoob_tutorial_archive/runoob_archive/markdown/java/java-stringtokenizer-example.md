# Java 实例 - 字符串分隔(StringTokenizer)

- Source: https://www.runoob.com/java/java-stringtokenizer-example.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


Java 中我们可以使用 StringTokennizer 设置不同分隔符来分隔字符串，默认的分隔符是：**空格、制表符（\t）、换行符(\n）、回车符（\r）**。


以下实例演示了 StringTokennizer 使用空格和等号来分隔字符串：


**更多 StringTokennizer 介绍可以查看：[Java StringTokenizer 类使用方法](https://www.runoob.com/w3cnote/java-stringtokenizer-intro.html)**


## JavaStringSplitEmp.java 文件



```java
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {

        String str = "This is String , split by StringTokenizer, created by runoob";
        StringTokenizer st = new StringTokenizer(str);

        System.out.println("----- 通过空格分隔 ------");
        while (st.hasMoreElements()) {
            System.out.println(st.nextElement());
        }

        System.out.println("----- 通过逗号分隔 ------");
        StringTokenizer st2 = new StringTokenizer(str, ",");

        while (st2.hasMoreElements()) {
            System.out.println(st2.nextElement());
        }
    }
}
```


输出结果：


```
----- 通过空格分隔 ------
This
is
String
,
split
by
StringTokenizer,
created
by
runoob
----- 通过逗号分隔 ------
This is String
 split by StringTokenizer
 created by runoob
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 打印倒立的三角形](https://www.runoob.com/java-print-invertedtriangle.html)
			[Java 9 新特性](https://www.runoob.com/java9-new-features.html) **