# Java 实例 - 删除数组元素

- Source: https://www.runoob.com/java/arrays-remove.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


Java 的数组是固定长度的，无法直接删除，我们可以通过创建一个新数组，把原始数组中要保留的元素放到新数组中即可：


## Main.java 文件



```java
import java.util.Arrays;

public class RunoobTest {

    public static void main(String[] args) {
        int[] oldarray = new int[] {3, 4, 5, 6, 7};// 原始数组
        int num = 2;   // 删除索引为 2 的元素，即删除第三个元素 5
        int[] newArray = new int[oldarray.length-1];// 新数组，长度为原始数组减去 1

        for(int i=0;i<newArray.length; i++) {
            // 判断元素是否越界
            if (num < 0 || num >= oldarray.length) {
                throw new RuntimeException("元素越界... ");
            }
            //
            if(i<num) {
                newArray[i] = oldarray[i];
            }
            else {
                newArray[i] = oldarray[i+1];
            }
        }
        // 打印输出数组内容
        System.out.println(Arrays.toString(oldarray));
        oldarray = newArray;
        System.out.println(Arrays.toString(oldarray));
    }
}
```


以上代码运行输出结果为：


```
[3, 4, 5, 6, 7]
[3, 4, 6, 7]
```


我们也可以使用 ArrayList 来实现这个功能，ArrayList 是动态数组，操作起来更加方便。


以下实例演示了如何使用 ArrayList 的 remove () 方法来删除数组列表的元素：


## Main.java 文件



```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args)  {
        ArrayList<String> objArray = new ArrayList<String>();
        objArray.clear();
        objArray.add(0,"第 0 个元素");
        objArray.add(1,"第 1 个元素");
        objArray.add(2,"第 2 个元素");
        System.out.println("数组删除元素前："+objArray);
        objArray.remove(1);
        objArray.remove("第 0 个元素");
        System.out.println("数组删除元素后："+objArray);
    }
}
```


以上代码运行输出结果为：


```
数组删除元素前：[第 0 个元素, 第 1 个元素, 第 2 个元素]
数组删除元素后：[第 2 个元素]
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 查找数组中的重复元素](https://www.runoob.com/arrays-compare.html)
			[Java 实例 – 数组差集](https://www.runoob.com/arrays-removeall.html) **













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