# Java 实例 - 连接字符串

- Source: https://www.runoob.com/java/string-concatenation.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了通过 "+" 操作符和StringBuffer.append() 方法来连接字符串，并比较其性能：


## StringConcatenate.java 文件



```java
public class StringConcatenate {
    public static void main(String[] args){
        long startTime = System.currentTimeMillis();
        for(int i=0;i<5000;i++){
            String result = "This is"
            + "testing the"
            + "difference"+ "between"
            + "String"+ "and"+ "StringBuffer";
        }
        long endTime = System.currentTimeMillis();
        System.out.println("字符串连接"
        + " - 使用 + 操作符 : "
        + (endTime - startTime)+ " ms");
        long startTime1 = System.currentTimeMillis();
        for(int i=0;i<5000;i++){
            StringBuffer result = new StringBuffer();
            result.append("This is");
            result.append("testing the");
            result.append("difference");
            result.append("between");
            result.append("String");
            result.append("and");
            result.append("StringBuffer");
        }
        long endTime1 = System.currentTimeMillis();
        System.out.println("字符串连接"
        + " - 使用 StringBuffer : "
        + (endTime1 - startTime1)+ " ms");
    }
}
```


以上代码实例输出结果为：


```
字符串连接 - 使用 + 操作符 : 0 ms
字符串连接 - 使用 StringBuffer : 6 ms
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 字符串格式化](https://www.runoob.com/string-format.html)
			[Java 实例 – 数组排序及元素查找](https://www.runoob.com/arrays-search.html) **