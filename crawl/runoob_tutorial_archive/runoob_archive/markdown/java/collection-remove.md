# Java 实例 - 删除集合中指定元素

- Source: https://www.runoob.com/java/collection-remove.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 Collection 类的 collection.remove() 方法来删除集合中的指定的元素：


## Main.java 文件



```java
import java.util.*;

public class Main {
   public static void main(String [] args) {
      System.out.println( "集合实例!\n" );
      int size;
      HashSet collection = new HashSet ();
      String str1 = "Yellow", str2 = "White", str3 =
      "Green", str4 = "Blue";
      Iterator iterator;
      collection.add(str1);
      collection.add(str2);
      collection.add(str3);
      collection.add(str4);
      System.out.print("集合数据: ");
      iterator = collection.iterator();
      while (iterator.hasNext()){
         System.out.print(iterator.next() + " ");
      }
      System.out.println();
      collection.remove(str2);
      System.out.println("删除之后 [" + str2 + "]\n");
      System.out.print("现在集合的数据是: ");
      iterator = collection.iterator();
      while (iterator.hasNext()){
         System.out.print(iterator.next() + " ");
      }
      System.out.println();
      size = collection.size();
      System.out.println("集合大小: " + size + "\n");
   }
}
```


以上代码运行输出结果为：


```
集合实例!

集合数据: White Yellow Blue Green
删除之后 [White]

现在集合的数据是: Yellow Blue Green
集合大小: 3
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 只读集合](https://www.runoob.com/collection-readonly.html)
			[Java 实例 – 集合反转](https://www.runoob.com/collection-reverse.html) **













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