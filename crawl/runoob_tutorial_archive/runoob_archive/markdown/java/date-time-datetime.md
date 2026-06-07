# Java 实例 - 获取当前时间

- Source: https://www.runoob.com/java/date-time-datetime.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 Date 类及 SimpleDateFormat 类的 format(date) 方法来输出当前时间：


## Main.java 文件



```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class Main{
    public static void main(String[] args){

        SimpleDateFormat sdf = new SimpleDateFormat();// 格式化时间
        sdf.applyPattern("yyyy-MM-dd HH:mm:ss a");// a为am/pm的标记
        Date date = new Date();// 获取当前时间
        System.out.println("现在时间：" + sdf.format(date)); // 输出已经格式化的现在时间（24小时制）
    }
}
```


以上代码运行输出结果为：


```
现在时间：2015-03-27 21:27:28 下午
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 格式化时间（SimpleDateFormat）](https://www.runoob.com/date-time-am-pm.html)
			[Java 实例 – 获取年份、月份等](https://www.runoob.com/date-year-month.html) **