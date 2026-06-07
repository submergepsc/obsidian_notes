# Java 实例 - 如何执行指定class文件目录（classpath）

- Source: https://www.runoob.com/java/env-classpath.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


如果我们 Java 编译后的class文件不在当前目录，我们可以使用 -classpath 来指定class文件目录：


```
C:> java -classpath C:\java\DemoClasses HelloWorld
```


以上命令中我们使用了 -classpath 参数指定了 HelloWorld 的 class 文件所在目录。


如果class文件在jar文件中，则命令如下：


```
c:> java -classpath C:\java\myclasses.jar
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 如何执行编译过 Java 文件](https://www.runoob.com/env-run.html)
			[Java 实例 – 如何查看当前 Java 运行的版本?](https://www.runoob.com/env-version.html) **