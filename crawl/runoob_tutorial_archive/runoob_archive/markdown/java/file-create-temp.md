# Java 实例 - 创建临时文件

- Source: https://www.runoob.com/java/file-create-temp.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了使用 File 类的 createTempFile(String prefix, String suffix); 方法在默认临时目录来创建临时文件，参数 prefix 为前缀，suffix 为后缀：


## Main.java 文件



```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        File temp = File.createTempFile("testrunoobtmp", ".txt");
        System.out.println("文件路径: "+temp.getAbsolutePath());
        temp.deleteOnExit();
        BufferedWriter out = new BufferedWriter(new FileWriter(temp));
        out.write("aString");
        System.out.println("临时文件已创建:");
        out.close();
    }
}
```


也可以使用 **createTempFile(String prefix, String suffix, File directory)** 中的 directory 参数来指定临时文件的目录：


## Main.java 文件



```java
import java.io.File;

public class Main {

   public static void main(String[] args) {
      File f = null;

      try {

         // 创建临时文件
         f = File.createTempFile("tmp", ".txt", new File("C:/"));

         // 输出绝对路径
         System.out.println("File path: "+f.getAbsolutePath());

         // 终止后删除临时文件
         f.deleteOnExit();

         // 创建临时文件
         f = File.createTempFile("tmp", null, new File("D:/"));

         // 输出绝对路径
         System.out.print("File path: "+f.getAbsolutePath());

         // 终止后删除临时文件
         f.deleteOnExit();

      } catch(Exception e) {

         // 如果有错误输出内容
         e.printStackTrace();
      }
   }
}
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 修改文件最后的修改日期](https://www.runoob.com/file-date-modify.html)
			[Java 实例 – 向文件中追加数据](https://www.runoob.com/file-append.html) **













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