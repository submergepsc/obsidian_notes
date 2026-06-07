# Java 实例 - 集合遍历

- Source: https://www.runoob.com/java/collection-iterator.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何遍历从Collection接口延伸出的List、Set和以键值对形式作存储的Map类型的集合，以下我们分别使用了普通for，增强型的 for ，iterator 等方式来遍历集合：


### List与Set类型集合的遍历


## Main.java 文件



```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class Main {

   public static void main(String[] args) {
      // List集合的遍历
      listTest();
      // Set集合的遍历
      setTest();
   }

   private static void setTest() {
      Set<String> set = new HashSet<String>();
      set.add("JAVA");
      set.add("C");
      set.add("C++");
      // 重复数据添加失败
      set.add("JAVA");
      set.add("JAVASCRIPT");

      // 使用iterator遍历set集合
      Iterator<String> it = set.iterator();
      while (it.hasNext()) {
         String value = it.next();
         System.out.println(value);
      }

      // 使用增强for循环遍历set集合
      for(String s: set){
         System.out.println(s);
      }
   }

   // 遍历list集合
   private static void listTest() {
      List<String> list = new ArrayList<String>();
      list.add("菜");
      list.add("鸟");
      list.add("教");
      list.add("程");
      list.add("www.runoob.com");

      // 使用iterator遍历
      Iterator<String> it = list.iterator();
      while (it.hasNext()) {
         String value = it.next();
         System.out.println(value);
      }

      // 使用传统for循环进行遍历
      for (int i = 0, size = list.size(); i < size; i++) {
         String value = list.get(i);
         System.out.println(value);
      }

      // 使用增强for循环进行遍历
      for (String value : list) {
         System.out.println(value);
      }
   }
}
```


以上代码运行输出结果为：


```
菜
鸟
教
程
www.runoob.com
菜
鸟
教
程
www.runoob.com
菜
鸟
教
程
www.runoob.com
JAVA
JAVASCRIPT
C++
C
JAVA
JAVASCRIPT
C++
C
```


### 关于Map类型集合的遍历


以下实例我们使用了 HashMap 的 keySet()与entrySet()方法来遍历集合：


```
/*
 author by runoob.com
 Main.java
 */

import java.util.Map;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.Map.Entry;

//增强For循环
public class Main {

   public static void main(String[] args) {
      // 创建一个HashMap对象,并加入了一些键值对。
      Map<String, String> maps = new HashMap<String, String>();
      maps.put("1", "PHP");
      maps.put("2", "Java");
      maps.put("3", "C");
      maps.put("4", "C++");
      maps.put("5", "HTML");

      // 传统的遍历map集合的方法1; keySet()
      //traditionalMethod1(maps);
      // 传统的遍历map集合的方法2; entrySet()
      //traditionalMethod2(maps);
      // 使用增强For循环来遍历map集合方法1; keySet()
      //strongForMethod1(maps);
      // 使用增强For循环来遍历map集合方法2; entrySet()
      strongForMethod2(maps);
   }

   private static void strongForMethod2(Map<String, String> maps) {
      Set<Entry<String, String>> set = maps.entrySet();
      for (Entry<String, String> entry : set) {
         String key = entry.getKey();
         String value = entry.getValue();
         System.out.println(key + " : " + value);
      }
   }

   private static void strongForMethod1(Map<String, String> maps) {
      Set<String> set = maps.keySet();
      for (String s : set) {
         String key = s;
         String value = maps.get(s);
         System.out.println(key + " : " + value);
      }
   }

   // 使用entrySet()方法，获取maps集合中的每一个键值对，
   private static void traditionalMethod2(Map<String, String> maps) {
      Set<Map.Entry<String, String>> sets = maps.entrySet();
      // 取得迭代器遍历出对应的值。
      Iterator<Entry<String, String>> it = sets.iterator();
      while (it.hasNext()) {
         Map.Entry<String, String> entry = (Entry<String, String>) it.next();
         String key = entry.getKey();
         String value = entry.getValue();
         System.out.println(key + " : " + value);
      }
   }

   // 使用keySet()方法，获取maps集合中的所有键，遍历键取得所对应的值。
   private static void traditionalMethod1(Map<String, String> maps) {
      Set<String> sets = maps.keySet();
      // 取得迭代器遍历出对应的值
      Iterator<String> it = sets.iterator();
      while (it.hasNext()) {
         String key = it.next();
         String value = maps.get(key);
         System.out.println(key + " : " + value);
      }
   }
}
```


以上代码运行输出结果为：


```
1 : PHP
2 : Java
3 : C
4 : C++
5 : HTML
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 集合反转](https://www.runoob.com/collection-reverse.html)
			[Java 实例 – 集合打乱顺序](https://www.runoob.com/collection-shuffle.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **