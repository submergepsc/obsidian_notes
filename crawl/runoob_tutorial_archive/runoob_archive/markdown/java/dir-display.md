# Java 实例 - 遍历指定目录下的所有目录

- Source: https://www.runoob.com/java/dir-display.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 File 类的 list 方法来遍历指定目录下的所有目录：


## Main.java 文件



```java
import java.io.*;

class Main {
   public static void main(String[] args) {
      File dir = new File("F:");
      File[] files = dir.listFiles();
      FileFilter fileFilter = new FileFilter() {
         public boolean accept(File file) {
            return file.isDirectory();
         }
      };
      files = dir.listFiles(fileFilter);
      System.out.println(files.length);
      if (files.length == 0) {
         System.out.println("目录不存在或它不是一个目录");
      }
      else {
         for (int i=0; i< files.length; i++) {
            File filename = files[i];
            System.out.println(filename.toString());
         }
      }
   }
}
```


以上代码运行输出结果为：


```
14
F:\C Drive Data Old HDD
F:\Desktop1
F:\harsh
F:\hharsh final
F:\hhhh
F:\mov
F:\msdownld.tmp
F:\New Folder
F:\ravi
F:\ravi3
F:\RECYCLER
F:\System Volume Information
F:\temp
F:\work
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 遍历指定目录下的所有文件](https://www.runoob.com/dir-sub.html)
			[Java 实例 – Finally的用法](https://www.runoob.com/exception-finally.html) **