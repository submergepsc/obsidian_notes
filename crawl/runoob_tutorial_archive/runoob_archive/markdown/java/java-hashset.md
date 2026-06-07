# Java HashSet

- Source: https://www.runoob.com/java/java-hashset.html

[![Java 集合框架](https://www.runoob.com/images/up.gif) Java 集合框架](https://www.runoob.com/java-collections.html)


HashSet 基于 HashMap 来实现的，是一个不允许有重复元素的集合。

HashSet 允许有 null 值。


HashSet 是无序的，即不会记录插入的顺序。

HashSet 不是线程安全的， 如果多个线程尝试同时修改 HashSet，则最终结果是不确定的。 您必须在多线程访问时显式同步对 HashSet 的并发访问。

HashSet 实现了 Set 接口。


![](https://www.runoob.com/wp-content/uploads/2020/07/java-hashset-hierarchy.png)


HashSet 中的元素实际上是对象，一些常见的基本类型可以使用它的包装类。

基本类型对应的包装类表如下：


| 基本类型 | 引用类型 |
| --- | --- |
| boolean | Boolean |
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| char | Character |


HashSet 类位于 java.util 包中，使用前需要引入它，语法格式如下：


```
import java.util.HashSet; // 引入 HashSet 类
```


以下实例我们创建一个 HashSet 对象 sites，用于保存字符串元素：


```
HashSet<String> sites = new HashSet<String>();
```


### 添加元素

HashSet 类提供了很多有用的方法，添加元素可以使用 add() 方法:


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");  // 重复的元素不会被添加
        System.out.println(sites);
    }
}
```


执行以上代码，输出结果如下：


```
[Google, Runoob, Zhihu, Taobao]
```


在上面的实例中，Runoob 被添加了两次，它在集合中也只会出现一次，因为集合中的每个元素都必须是唯一的。

### 判断元素是否存在


我们可以使用 contains() 方法来判断元素是否存在于集合当中:


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");  // 重复的元素不会被添加
        System.out.println(sites.contains("Taobao"));
    }
}
```


执行以上代码，输出结果如下：



```
true
```


### 删除元素


我们可以使用 remove() 方法来删除集合中的元素:


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");     // 重复的元素不会被添加
        sites.remove("Taobao");  // 删除元素，删除成功返回 true，否则为 false
        System.out.println(sites);
    }
}
```


执行以上代码，输出结果如下：


```
[Google, Runoob, Zhihu]
```


删除集合中所有元素可以使用 clear 方法：


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");     // 重复的元素不会被添加
        sites.clear();
        System.out.println(sites);
    }
}
```


执行以上代码，输出结果如下：


```
[]
```


### 计算大小


如果要计算 HashSet 中的元素数量可以使用 size() 方法：


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");     // 重复的元素不会被添加
        System.out.println(sites.size());
    }
}
```


执行以上代码，输出结果如下：


```
4
```


### 迭代 HashSet


可以使用 for-each 来迭代 HashSet 中的元素。


## 实例


```java
// 引入 HashSet 类
import java.util.HashSet;

public class RunoobTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Runoob");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Runoob");     // 重复的元素不会被添加
        for (String i : sites) {
            System.out.println(i);
        }
    }
}
```


执行以上代码，输出结果如下：


```
Google
Runoob
Zhihu
Taobao
```


---


## HashSet 常用方法


| 方法 | 返回值 | 说明 | 示例 |
| --- | --- | --- | --- |
| add(E e) | boolean | 添加元素到集合，成功返回 true，重复元素返回 false。 | set.add("Java"); |
| remove(Object o) | boolean | 删除指定元素，成功返回 true，元素不存在返回 false。 | set.remove("Python"); |
| contains(Object o) | boolean | 检查集合是否包含指定元素。 | if (set.contains("Java")) { ... } |
| size() | int | 返回集合中的元素数量。 | int count = set.size(); |
| isEmpty() | boolean | 判断集合是否为空。 | if (set.isEmpty()) { ... } |
| clear() | void | 清空集合中的所有元素。 | set.clear(); |
| iterator() | Iterator | 返回集合的迭代器，用于遍历元素。 | for (String s : set) { ... } |
| toArray() | Object[] | 将集合转换为数组。 | Object[] arr = set.toArray(); |
| toArray(T[] a) | T[] | 将集合转换为指定类型的数组。 | String[] arr = set.toArray(new String[0]); |
| addAll(Collection c) | boolean | 添加另一个集合的所有元素（并集操作）。 | set.addAll(Arrays.asList("A", "B")); |
| retainAll(Collection c) | boolean | 仅保留与指定集合共有的元素（交集操作）。 | set.retainAll(otherSet); |
| removeAll(Collection c) | boolean | 删除与指定集合共有的元素（差集操作）。 | set.removeAll(otherSet); |


更多 API 方法可以查看：[https://www.runoob.com/manual/jdk11api/java.base/java/util/HashSet.html](https://www.runoob.com/../manual/jdk11api/java.base/java/util/HashSet.html)


[![Java 集合框架](https://www.runoob.com/images/up.gif) Java 集合框架](https://www.runoob.com/java-collections.html)








	  AI 思考中...





			** [Java HashMap](https://www.runoob.com/java-hashmap.html)
			[Java Iterator（迭代器）](https://www.runoob.com/java-iterator.html) **













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