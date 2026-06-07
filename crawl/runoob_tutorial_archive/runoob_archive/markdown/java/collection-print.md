# Java 实例 - 集合输出

- Source: https://www.runoob.com/java/collection-print.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 Java Util 类的 tMap.keySet(),tMap.values() 和 tMap.firstKey() 方法将集合元素输出：


## Main.java 文件



```java
import java.util.*;

public class Main{
   public static void main(String[] args) {
      System.out.println("TreeMap 实例！\n");
      TreeMap tMap = new TreeMap();
      tMap.put(1, "Sunday");
      tMap.put(2, "Monday");
      tMap.put(3, "Tuesday");
      tMap.put(4, "Wednesday");
      tMap.put(5, "Thursday");
      tMap.put(6, "Friday");
      tMap.put(7, "Saturday");
      System.out.println("TreeMap 键："
      + tMap.keySet());
      System.out.println("TreeMap 值："
      + tMap.values());
      System.out.println("键为 5 的值为: " + tMap.get(5)+ "\n");
      System.out.println("第一个键: " + tMap.firstKey()
      + " Value: "
      + tMap.get(tMap.firstKey()) + "\n");
      System.out.println("最后一个键: " + tMap.lastKey()
      + " Value: "+ tMap.get(tMap.lastKey()) + "\n");
      System.out.println("移除第一个数据: "
      + tMap.remove(tMap.firstKey()));
      System.out.println("现在 TreeMap 键为: "
      + tMap.keySet());
      System.out.println("现在 TreeMap 包含: "
      + tMap.values() + "\n");
      System.out.println("移除最后一个数据: "
      + tMap.remove(tMap.lastKey()));
      System.out.println("现在 TreeMap 键为: "
      + tMap.keySet());
      System.out.println("现在 TreeMap 包含: "
      + tMap.values());
   }
}
```


以上代码运行输出结果为：


```
TreeMap 实例！

TreeMap 键：[1, 2, 3, 4, 5, 6, 7]
TreeMap 值：[Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
键为 5 的值为: Thursday

第一个键: 1 Value: Sunday

最后一个键: 7 Value: Saturday

移除第一个数据: Sunday
现在 TreeMap 键为: [2, 3, 4, 5, 6, 7]
现在 TreeMap 包含: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]

移除最后一个数据: Saturday
现在 TreeMap 键为: [2, 3, 4, 5, 6]
现在 TreeMap 包含: [Monday, Tuesday, Wednesday, Thursday, Friday]
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 集合转数组](https://www.runoob.com/collection-conversion.html)
			[Java 实例 – 只读集合](https://www.runoob.com/collection-readonly.html) **