# Java 实例 - 读取文件内容

- Source: https://www.runoob.com/java/file-read.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了使用 readLine() 方法来读取文件 test.log 内容，其中 test.log 文件内容为：


```
菜鸟教程
www.runoob.com
```


java 代码如下：


## Main.java 文件



```java
import java.io.*;

public class Main {
    public static void main(String[] args)  {
        try {
            BufferedReader in = new BufferedReader(new FileReader("test.log"));
            String str;
            while ((str = in.readLine()) != null) {
                System.out.println(str);
            }
            System.out.println(str);
        } catch (IOException e) {
        }
    }
}
```


以上代码运行输出结果为：


```
菜鸟教程
www.runoob.com
null
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 删除文件](https://www.runoob.com/file-delete.html)
			[Java 实例 – 文件写入](https://www.runoob.com/file-write.html) **