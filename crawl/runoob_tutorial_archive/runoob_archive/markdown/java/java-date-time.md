# Java 日期时间

- Source: https://www.runoob.com/java/java-date-time.html

Java 提供了多套日期时间 API，以下是主要类别的对比和常用方法总结：


| 类别 | 主要类 | 线程安全 | 可变性 | Java 版本 | 特点 |
| --- | --- | --- | --- | --- | --- |
| 传统日期 | Date, Calendar，GregorianCalendar | 否 | 可变 | 1.0+ | 设计缺陷多，不推荐使用 |
| 新日期时间 | LocalDate, LocalTime, LocalDateTime, ZonedDateTime, ChronoUnit | 是 | 不可变 | 8+ | 设计良好，推荐使用 |
| 时间戳 | Instant | 是 | 不可变 | 8+ | 机器时间，精确到纳秒 |
| 格式化 | DateTimeFormatter | 是 | 不可变 | 8+ | 线程安全的格式化类 |

---

## LocalDate/DateTimeFormatter

LocalDate/DateTimeFormatter 是 Java 8 引入的日期类，LocalDate 用于表示不带时间的日期（年-月-日），DateTimeFormatter 用于格式化和解析日期时间对象。


## 实例


```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class RunoobTest {
    public static void main(String[] args) {
        // 获取当前日期
        LocalDate today = LocalDate.now();
        System.out.println("当前日期: " + today);

        // 创建特定日期
        LocalDate nationalDay = LocalDate.of(2025, 10, 1);
        System.out.println("国庆节: " + nationalDay);

        // 日期加减
        LocalDate tomorrow = today.plusDays(1);
        LocalDate nextMonth = today.plusMonths(1);
        LocalDate lastYear = today.minusYears(1);

        System.out.println("明天: " + tomorrow);
        System.out.println("下个月: " + nextMonth);
        System.out.println("去年今天: " + lastYear);
    }
}
```


以上实例输出结果为：


```
当前日期: 2025-05-01
国庆节: 2025-10-01
明天: 2025-05-02
下个月: 2025-06-01
去年今天: 2024-05-01
```


- **新项目优先使用 java.time 包** (Java 8+)
- **避免使用老旧的 Date 和 Calendar 类**
- **明确区分使用时区**： - 不需要时区：LocalDate/LocalTime/LocalDateTime - 需要时区：ZonedDateTime
- **格式化时考虑线程安全**：使用 DateTimeFormatter 而非 SimpleDateFormat
- **数据库交互**： - JDBC 4.2+ 直接支持 java.time 类型 - 旧版本可转换为 java.sql.Date/Timestamp


** 1. LocalDate (日期)**


## 实例


```java
LocalDate today = LocalDate.now();
LocalDate date = LocalDate.of(2023, Month.JUNE, 15);
int year = date.getYear();  // 2023
Month month = date.getMonth();  // JUNE
int day = date.getDayOfMonth();  // 15
LocalDate nextWeek = today.plusWeeks(1);
boolean isLeap = date.isLeapYear();  // 是否闰年
```


**2. LocalTime (时间)**


## 实例


```java
LocalTime now = LocalTime.now();
LocalTime time = LocalTime.of(14, 30, 45);  // 14:30:45
int hour = time.getHour();  // 14
int minute = time.getMinute();  // 30
LocalTime nextHour = time.plusHours(1);
```


**3. LocalDateTime (日期时间)**


## 实例


```java
LocalDateTime ldt = LocalDateTime.now();
LocalDateTime dt = LocalDateTime.of(2023, 6, 15, 14, 30);
LocalDateTime nextMonth = dt.plusMonths(1);
```


**4. ZonedDateTime (带时区日期时间)**


## 实例


```java
ZonedDateTime zdt = ZonedDateTime.now(ZoneId.of("Asia/Shanghai"));
ZonedDateTime nyTime = zdt.withZoneSameInstant(ZoneId.of("America/New_York"));
ZoneId zone = zdt.getZone();  // 获取时区
```


**5. Instant (时间戳)**


## 实例


```java
Instant now = Instant.now();  // 获取当前时间戳
Instant later = now.plusSeconds(60);  // 60秒后
long epochMilli = now.toEpochMilli();  // 获取毫秒时间戳
```


---


## Date 类


java.util 包提供了 Date 类来封装当前的日期和时间。 Date 类提供两个构造函数来实例化 Date 对象。

第一个构造函数使用当前日期和时间来初始化对象。


```java
Date( )
```


第二个构造函数接收一个参数，该参数是从 1970 年 1 月 1 日起的毫秒数。


```java
Date(long millisec)
```


Date 对象创建以后，可以调用下面的方法。


| 序号 | 方法和描述 |
| --- | --- |
| 1 | boolean after(Date date) 若当调用此方法的Date对象在指定日期之后返回true,否则返回false。 |
| 2 | boolean before(Date date) 若当调用此方法的Date对象在指定日期之前返回true,否则返回false。 |
| 3 | Object clone( ) 返回此对象的副本。 |
| 4 | int compareTo(Date date) 比较当调用此方法的Date对象和指定日期。两者相等时候返回0。调用对象在指定日期之前则返回负数。调用对象在指定日期之后则返回正数。 |
| 5 | int compareTo(Object obj) 若obj是Date类型则操作等同于compareTo(Date) 。否则它抛出ClassCastException。 |
| 6 | boolean equals(Object date) 当调用此方法的Date对象和指定日期相等时候返回true,否则返回false。 |
| 7 | long getTime( ) 返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 Date 对象表示的毫秒数。 |
| 8 | int hashCode( ) 返回此对象的哈希码值。 |
| 9 | void setTime(long time) 用自1970年1月1日00:00:00 GMT以后time毫秒数设置时间和日期。 |
| 10 | String toString( ) 把此 Date 对象转换为以下形式的 String： dow mon dd hh:mm:ss zzz yyyy 其中： dow 是一周中的某一天 (Sun, Mon, Tue, Wed, Thu, Fri, Sat)。 |


---


## 获取当前日期时间


Java中获取当前日期和时间很简单，使用 Date 对象的 toString() 方法来打印当前日期和时间，如下所示：


## 实例



```java
import java.util.Date;

public class DateDemo {
   public static void main(String[] args) {
       // 初始化 Date 对象
       Date date = new Date();

       // 使用 toString() 函数显示日期时间
       System.out.println(date.toString());
   }
}
```


**
[运行实例 »](https://www.runoob.com/try/runcode.php?filename=date_demo&type=java)


以上实例编译运行结果如下:


```
Mon May 04 09:51:52 CDT 2013
```


---


## 日期比较


Java 使用以下三种方法来比较两个日期：


- 使用 getTime() 方法获取两个日期（自1970年1月1日经历的毫秒数值），然后比较这两个值。
- 使用方法 before()，after() 和 equals()。例如，一个月的 12 号比 18 号早，则 **new Date(99, 2, 12).before(new Date (99, 2, 18))** 返回true。
- 使用 compareTo() 方法，它是由 Comparable 接口定义的，Date 类实现了这个接口。


### 1. 使用 getTime() 方法比较


这种方法通过比较日期对象自 1970年1月1日（Unix纪元）以来的毫秒数。


## 实例


```java
import java.util.Date;

public class DateComparison {
    public static void main(String[] args) {
        Date date1 = new Date(121, 5, 15); // 2021年6月15日
        Date date2 = new Date(121, 5, 20); // 2021年6月20日

        // 比较毫秒数
        if (date1.getTime() < date2.getTime()) {
            System.out.println("date1 在 date2 之前");
        } else if (date1.getTime() > date2.getTime()) {
            System.out.println("date1 在 date2 之后");
        } else {
            System.out.println("两个日期相同");
        }
    }
}
```


输出：


```
date1 在 date2 之前
```


### 2. 使用 before(), after() 和 equals() 方法


这些方法是 Date 类自带的比较方法，语义更清晰。


## 实例


```java
import java.util.Date;

public class DateComparison {
    public static void main(String[] args) {
        Date date1 = new Date(121, 5, 15); // 2021年6月15日
        Date date2 = new Date(121, 5, 20); // 2021年6月20日

        // 使用 before() 方法
        System.out.println("date1 在 date2 之前吗？ " + date1.before(date2));

        // 使用 after() 方法
        System.out.println("date1 在 date2 之后吗？ " + date1.after(date2));

        // 使用 equals() 方法
        System.out.println("两个日期相同吗？ " + date1.equals(date2));
    }
}
```


输出：


```
date1 在 date2 之前吗？ true
date1 在 date2 之后吗？ false
两个日期相同吗？ false
```


### 3. 使用 compareTo() 方法

Date 类实现了 Comparable 接口，可以使用 compareTo() 方法进行比较。


## 实例


```java
import java.util.Date;

public class DateComparison {
    public static void main(String[] args) {
        Date date1 = new Date(121, 5, 15); // 2021年6月15日
        Date date2 = new Date(121, 5, 20); // 2021年6月20日

        int result = date1.compareTo(date2);

        if (result < 0) {
            System.out.println("date1 在 date2 之前");
        } else if (result > 0) {
            System.out.println("date1 在 date2 之后");
        } else {
            System.out.println("两个日期相同");
        }
    }
}
```


输出：


```
date1 在 date2 之前
```


---


## 使用 SimpleDateFormat 格式化日期


SimpleDateFormat 是一个以语言环境敏感的方式来格式化和分析日期的类。SimpleDateFormat 允许你选择任何用户自定义日期时间格式来运行。例如：


## 实例



```java
import  java.util.*;
import java.text.*;

public class DateDemo {
   public static void main(String[] args) {

      Date dNow = new Date( );
      SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");

      System.out.println("当前时间为: " + ft.format(dNow));
   }
}
```


[运行实例 »](https://www.runoob.com/try/runcode.php?filename=date_demo1&type=java)


```
SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
```


这一行代码确立了转换的格式，其中 yyyy 是完整的公元年，MM 是月份，dd 是日期，HH:mm:ss 是时、分、秒。

注意**:有的格式大写，有的格式小写，例如 MM 是月份，mm 是分；HH 是 24 小时制，而 hh 是 12 小时制。


以上实例编译运行结果如下:


```
当前时间为: 2018-09-06 10:16:34
```


---


## 日期和时间的格式化编码


时间模式字符串用来指定时间格式。在此模式中，所有的 ASCII 字母被保留为模式字母，定义如下：


| 字母 | 描述 | 示例 |
| --- | --- | --- |
| G | 纪元标记 | AD |
| y | 四位年份 | 2001 |
| M | 月份 | July or 07 |
| d | 一个月的日期 | 10 |
| h | A.M./P.M. (1~12)格式小时 | 12 |
| H | 一天中的小时 (0~23) | 22 |
| m | 分钟数 | 30 |
| s | 秒数 | 55 |
| S | 毫秒数 | 234 |
| E | 星期几 | Tuesday |
| D | 一年中的日子 | 360 |
| F | 一个月中第几周的周几 | 2 (second Wed. in July) |
| w | 一年中第几周 | 40 |
| W | 一个月中第几周 | 1 |
| a | A.M./P.M. 标记 | PM |
| k | 一天中的小时(1~24) | 24 |
| K | A.M./P.M. (0~11)格式小时 | 10 |
| z | 时区 | Eastern Standard Time |
| ' | 文字定界符 | Delimiter |
| " | 单引号 | ` |


---


## 使用printf格式化日期


printf 方法可以很轻松地格式化时间和日期。使用两个字母格式，它以 **%t** 开头并且以下面表格中的一个字母结尾。


- %tY：输出四位数的年份，例如：2023
- %ty：输出两位数的年份，例如：23
- %tm：输出两位数的月份，例如：02
- %tB：输出月份的全名，例如：February
- %tb：输出月份的缩写，例如：Feb
- %tA：输出星期的全名，例如：Wednesday
- %ta：输出星期的缩写，例如：Wed
- %td：输出两位数的日期，例如：24
- %te：输出一位或两位数的日期，例如：24 或 02
- %tH：输出24小时制的小时数，例如：23
- %tI：输出12小时制的小时数，例如：11
- %tM：输出分钟数，例如：45
- %tS：输出秒数，例如：30
- %tp：输出上午还是下午，例如：AM 或 PM
- %tZ：输出时区，例如：GMT+08:00


| 转换符 | 说明 | 示例 |
| --- | --- | --- |
| %tc | 包括全部日期和时间信息 | 星期六 十月 27 14:21:20 CST 2007 |
| %tF | "年-月-日"格式 | 2007-10-27 |
| %tD | "月/日/年"格式 | 10/27/07 |
| %tr | "HH:MM:SS PM"格式（12时制） | 02:25:51 下午 |
| %tT | "HH:MM:SS"格式（24时制） | 14:28:16 |
| %tR | "HH:MM"格式（24时制） | 14:28 |


更多 **printf** 解析可以参见：[Java 格式化输出 printf 例子](https://www.runoob.com/w3cnote/java-printf-formate-demo.html)


### 实例


## 实例


```java
import java.util.Date;
public class DateFormatExample {
   public static void main(String[] args) {
      Date date = new Date();
      System.out.printf("%tY-%tm-%td %tH:%tM:%tS %tZ", date, date, date, date, date, date, date);
   }
}
```


执行输出结果为：


```
2023-02-24 13:34:45 GMT+08:00
```


## 实例



```java
import java.util.Date;

public class DateDemo {

  public static void main(String[] args) {
     // 初始化 Date 对象
     Date date = new Date();

     //c的使用
    System.out.printf("全部日期和时间信息：%tc%n",date);
    //f的使用
    System.out.printf("年-月-日格式：%tF%n",date);
    //d的使用
    System.out.printf("月/日/年格式：%tD%n",date);
    //r的使用
    System.out.printf("HH:MM:SS PM格式（12时制）：%tr%n",date);
    //t的使用
    System.out.printf("HH:MM:SS格式（24时制）：%tT%n",date);
    //R的使用
    System.out.printf("HH:MM格式（24时制）：%tR",date);
  }
}
```


以上实例编译运行结果如下:


```
全部日期和时间信息：星期一 九月 10 10:43:36 CST 2012
年-月-日格式：2012-09-10
月/日/年格式：09/10/12
HH:MM:SS PM格式（12时制）：10:43:36 上午
HH:MM:SS格式（24时制）：10:43:36
HH:MM格式（24时制）：10:43
```


如果你需要重复提供日期，那么利用这种方式来格式化它的每一部分就有点复杂了。因此，可以利用一个格式化字符串指出要被格式化的参数的索引。


索引必须紧跟在 **%** 后面，而且必须以 **$** 结束。例如：


## 实例



```java
import java.util.Date;

public class DateDemo {

   public static void main(String[] args) {
       // 初始化 Date 对象
       Date date = new Date();

       // 使用toString()显示日期和时间
       System.out.printf("%1$s %2$tB %2$td, %2$tY",
                         "Due date:", date);
   }
}
```


**
[运行实例 »](https://www.runoob.com/try/runcode.php?filename=date_demo3&type=java)


以上实例编译运行结果如下:


```
Due date: February 09, 2014
```


或者，你可以使用







	  AI 思考中...





			** [Java 数组](https://www.runoob.com/java-array.html)
			[Java 正则表达式](https://www.runoob.com/java-regular-expressions.html) **