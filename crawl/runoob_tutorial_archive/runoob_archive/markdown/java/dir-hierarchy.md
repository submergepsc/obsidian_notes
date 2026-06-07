# Java 实例 - 打印目录结构

- Source: https://www.runoob.com/java/dir-hierarchy.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了使用 File 类的 file.getName() 和 file.listFiles() 方法来打印目录结构：


## Main.java 文件



```java
import java.io.File;
import java.io.IOException;

public class FileUtil {
    public static void main(String[] a)throws IOException{
        showDir(1, new File("d:\\Java"));
    }
    static void showDir(int indent, File file) throws IOException {
        for (int i = 0; i < indent; i++)
            System.out.print('-');
        System.out.println(file.getName());
        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (int i = 0; i < files.length; i++)
                showDir(indent + 4, files[i]);
        }
    }
}
```


以上代码运行输出结果为：


```
-Java
-----codes
---------string.txt
---------array.txt
-----w3cschoolcc
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 判断文件是否隐藏](https://www.runoob.com/dir-hidden.html)
			[Java 实例 – 获取目录最后修改时间](https://www.runoob.com/dir-modification.html) **