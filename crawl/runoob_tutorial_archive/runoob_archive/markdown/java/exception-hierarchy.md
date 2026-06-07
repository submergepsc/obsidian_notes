# Java 实例 - 多个异常处理（多个catch）

- Source: https://www.runoob.com/java/exception-hierarchy.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


对异常的处理：


1，声明异常时，建议声明更为具体的异常，这样可以处理的更具体


2,对方声明几个异常，就对应几个catch块， 如果多个catch块中的异常出现继承关系，父类异常catch块放在最下面


以下实例演示了如何处理多异常：


## ExceptionDemo.java 文件



```java
class Demo
{
    int div(int a,int b) throws ArithmeticException,ArrayIndexOutOfBoundsException//在功能上通过throws的关键字声明该功能可能出现问题
    {
        int []arr = new int [a];

        System.out.println(arr[4]);//制造的第一处异常

        return a/b;//制造的第二处异常
    }
}

class ExceptionDemo
{
    public static void main(String[]args) //throws Exception
    {
        Demo d = new Demo();

        try
            {
                int x = d.div(4,0);//程序运行截图中的三组示例 分别对应此处的三行代码
                //int x = d.div(5,0);
                //int x = d.div(4,1);
                System.out.println("x="+x);
        }
        catch (ArithmeticException e)
        {
            System.out.println(e.toString());
        }
        catch (ArrayIndexOutOfBoundsException e)
        {
            System.out.println(e.toString());
        }
        catch (Exception e)//父类 写在此处是为了捕捉其他没预料到的异常 只能写在子类异常的代码后面
                            //不过一般情况下是不写的
        {
            System.out.println(e.toString());
        }

        System.out.println("Over");
    }

}
```


以上代码运行输出结果为：


```
java.lang.ArrayIndexOutOfBoundsException: 4
Over
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – Finally的用法](https://www.runoob.com/exception-finally.html)
			[Java 实例 – 异常处理方法](https://www.runoob.com/exception-method.html) **













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