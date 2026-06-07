# Java 实例 - 向文件中追加数据

- Source: https://www.runoob.com/java/file-append.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了使用 filewriter 方法向文件中追加数据：


## Main.java 文件



```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter("filename"));
            out.write("aString1\n");
            out.close();
            out = new BufferedWriter(new FileWriter("filename",true));
            out.write("aString2");
            out.close();
            BufferedReader in = new BufferedReader(new FileReader("filename"));
            String str;
            while ((str = in.readLine()) != null) {
                System.out.println(str);
            }
            in.close();
        }
            catch (IOException e) {
            System.out.println("exception occoured"+ e);
        }
    }
}
```


以上代码运行输出结果为：


```
aString1
aString2
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 创建临时文件](https://www.runoob.com/file-create-temp.html)
			[Java 实例 – 将文件内容复制到另一个文件](https://www.runoob.com/file-copy.html) **