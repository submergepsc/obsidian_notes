# Java 实例 - 数组输出

- Source: https://www.runoob.com/java/arrays-output.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过循环输出数组：


## Welcome.java 文件



```java
public class Welcome {
    public static void main(String[] args){
        String[] runoobs = new String[3];
        runoobs[0] = "菜鸟教程";
        runoobs[1] = "菜鸟工具";
        runoobs[2] = "菜鸟笔记";
        for (int i = 0; i < runoobs.length; i++){
            System.out.println(runoobs[i]);
        }
    }
}
```


以上代码运行输出结果为：


```
菜鸟教程
菜鸟工具
菜鸟笔记
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组反转](https://www.runoob.com/arrays-reverse.html)
			[Java 实例 – 数组获取最大和最小值](https://www.runoob.com/arrays-min-max.html) **