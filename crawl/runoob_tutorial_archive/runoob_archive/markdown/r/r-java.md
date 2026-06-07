# Java 中操作 R

- Source: https://www.runoob.com/r/r-java.html

首先，在 R 中安装软件包 "Rserve" 。


如果你使用的是 RGui 可视化界面，在菜单栏的 程序包 - 安装程序包 里可以完成这个步骤。如果你使用的是纯粹的 R Console，可以使用以下命令：


```
install.packages("Rserve", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


当 Reserve 安装完成之后，在 R 的根目录下会有一个 library 目录，在其中找到 Rserve/java 目录，然后会发现目录下有两个文件：REngine.jar 和 Rserve.jar。


这两个文件就是 Java 中的 R 接口库。


**注意：**Java 不能做到脱离 R 系统独立使用 R 的功能！


### 第一步 启动 Reserve


进入 R，输入以下代码已启动 Rserve：


```
library("Rserve")
Rserve()
```


如果启动成功，R 会输出 Rserve 的路径。


### 第二步 编写 Java 程序


首先导入刚才的两个 jar 库。

导入之后，我们认识一个关键的类：RConnection, 这个类可以用于连接到 Rserve。

我们现在在 Java 中利用 R 完成一个逆矩阵运算：


![](https://www.runoob.com/wp-content/uploads/2020/07/JAOMiRYeuLwZq0Yw__thumbnail.png)


## 实例


```r
import org.rosuda.REngine.Rserve.*;

public class Main {

    public static void main(String[] args) {
        RConnection rcon = null;
        try {
            // 建立与 Rserve 的连接
            rcon = new RConnection("127.0.0.1");

            // eval() 函数用于令 R 执行 R 语句
            // 此处制造了一个 m1 矩阵
            rcon.eval("m1 = matrix(c(1, 2, 3, 4), 2, 2, byrow=TRUE)");

            // solve() 函数在 R 中求 m1 矩阵的逆矩阵
            // 并将结果返回，asDoubleMatrix 函数可以将数据转换成
            // Java 中的 double 二维数组以表示矩阵
            double[][] m1 = rcon.eval("solve(m1)").asDoubleMatrix();

            // 输出矩阵的内容
            for (int i = 0; i < m1.length; i++) {
                for (int j = 0; j < m1[0].length; j++)
                    System.out.print(m1[i][j] + "\t");
                System.out.println();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (rcon != null) rcon.close();
        }
    }
}
```


执行结果：


```
-1.9999999999999998    1.0
1.4999999999999998    -0.49999999999999994
```


很显然，结果是正确的，但毕竟是浮点数，所以打印出来可能有些不好看，不影响对数据的使用。








	  AI 思考中...





			** [R 绘图 – 散点图](https://www.runoob.com/r-scatterplots-charts.html)
			[R 数据重塑](https://www.runoob.com/r-data-reshaping.html) **













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

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





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