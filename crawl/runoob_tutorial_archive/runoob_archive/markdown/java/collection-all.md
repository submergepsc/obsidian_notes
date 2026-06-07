# Java 实例 - 集合中添加不同类型元素

- Source: https://www.runoob.com/java/collection-all.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了在集合类中添加不同类型的元素：


## Main.java 文件



```java
import java.util.Map;
import java.util.Set;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;

public class Main {
   public static void main(String[] args) {
      List lnkLst = new LinkedList();
      lnkLst.add("element1");
      lnkLst.add("element2");
      lnkLst.add("element3");
      lnkLst.add("element4");
      displayAll(lnkLst);
      List aryLst = new ArrayList();
      aryLst.add("x");
      aryLst.add("y");
      aryLst.add("z");
      aryLst.add("w");
      displayAll(aryLst);
      Set hashSet = new HashSet();
      hashSet.add("set1");
      hashSet.add("set2");
      hashSet.add("set3");
      hashSet.add("set4");
      displayAll(hashSet);
      SortedSet treeSet = new TreeSet();
      treeSet.add("1");
      treeSet.add("2");
      treeSet.add("3");
      treeSet.add("4");
      displayAll(treeSet);
      LinkedHashSet lnkHashset = new LinkedHashSet();
      lnkHashset.add("one");
      lnkHashset.add("two");
      lnkHashset.add("three");
      lnkHashset.add("four");
      displayAll(lnkHashset);
      Map map1 = new HashMap();
      map1.put("key1", "J");
      map1.put("key2", "K");
      map1.put("key3", "L");
      map1.put("key4", "M");
      displayAll(map1.keySet());
      displayAll(map1.values());
      SortedMap map2 = new TreeMap();
      map2.put("key1", "JJ");
      map2.put("key2", "KK");
      map2.put("key3", "LL");
      map2.put("key4", "MM");
      displayAll(map2.keySet());
      displayAll(map2.values());
      LinkedHashMap map3 = new LinkedHashMap();
      map3.put("key1", "JJJ");
      map3.put("key2", "KKK");
      map3.put("key3", "LLL");
      map3.put("key4", "MMM");
      displayAll(map3.keySet());
      displayAll(map3.values());
   }
   static void displayAll(Collection col) {
      Iterator itr = col.iterator();
      while (itr.hasNext()) {
         String str = (String) itr.next();
         System.out.print(str + " ");
      }
      System.out.println();
   }
}
```


以上代码运行输出结果为：


```
element1 element2 element3 element4
x y z w
set3 set2 set4 set1
1 2 3 4
one two three four
key1 key2 key3 key4
J K L M
key1 key2 key3 key4
JJ KK LL MM
key1 key2 key3 key4
JJJ KKK LLL MMM
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – HashMap遍历](https://www.runoob.com/collection-iterate.html)
			[Java 实例 – 使用 Enumeration 遍历 HashTable](https://www.runoob.com/collection-enumeration.html) **













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