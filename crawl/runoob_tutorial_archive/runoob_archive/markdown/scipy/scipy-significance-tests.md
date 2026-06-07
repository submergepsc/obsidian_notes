# Scipy 显著性检验

- Source: https://www.runoob.com/scipy/scipy-significance-tests.html

显著性检验（significance test）就是事先对总体（随机变量）的参数或总体分布形式做出一个假设，然后利用样本信息来判断这个假设（备择假设）是否合理，即判断总体的真实情况与原假设是否有显著性差异。或者说，显著性检验要判断样本与我们对总体所做的假设之间的差异是纯属机会变异，还是由我们所做的假设与总体真实情况之间不一致所引起的。 显著性检验是针对我们对总体所做的假设做检验，其原理就是"小概率事件实际不可能性原理"来接受或否定假设。


显著性检验即用于实验处理组与对照组或两种不同处理的效应之间是否有差异，以及这种差异是否显著的方法。


SciPy 提供了 scipy.stats 的模块来执行Scipy 显著性检验的功能。


### 统计假设


统计假设是关于一个或多个随机变量的未知分布的假设。随机变量的分布形式已知，而仅涉及分布中的一个或几个未知参数的统计假设，称为参数假设。检验统计假设的过程称为假设检验，判别参数假设的检验称为参数检验。


### 零假设


零假设（null hypothesis），统计学术语，又称原假设，指进行统计检验时预先建立的假设。 零假设成立时，有关统计量应服从已知的某种概率分布。

当统计量的计算值落入否定域时，可知发生了小概率事件，应否定原假设。


常把一个要检验的假设记作 H0，称为原假设（或零假设） (null hypothesis) ，与 H0 对立的假设记作 H1，称为备择假设(alternative hypothesis) 。


- 在原假设为真时，决定放弃原假设，称为第一类错误，其出现的概率通常记作 **α**；
- 在原假设不真时，决定不放弃原假设，称为第二类错误，其出现的概率通常记作 **β**
- α+β 不一定等于 1。


通常只限定犯第一类错误的最大概率 **α**， 不考虑犯第二类错误的概率 **β**。这样的假设 检验又称为显著性检验，概率 **α** 称为显著性水平。

最常用的 **α** 值为 0.01、0.05、0.10 等。一般情况下，根据研究的问题，如果放弃真假设损失大，为减少这类错误，**α** 取值小些 ，反之，**α** 取值大些。


### 备择假设


备择假设(alternative hypothesis)是统计学的基本概念之一，其包含关于总体分布的一切使原假设不成立的命题。备择假设亦称对立假设、备选假设。


备择假设可以替代零假设。


例如我们对于学生的评估，我们将采取：


```
“学生比平均水平差” -—  作为零假设

“学生优于平均水平” —— 作为替代假设。
```


### 单边检验


单边检验(one-sided test)亦称单尾检验，又称单侧检验，在假设检验中，用检验统计量的密度曲线和二轴所围成面积中的单侧尾部面积来构造临界区域进行检验的方法称为单边检验。


当我们的假设仅测试值的一侧时，它被称为"单尾测试"。


例子：


对于零假设：


```
“均值等于 k”
```


我们可以有替代假设：


```
“平均值小于 k”
或
“平均值大于 k”
```


### 双边检验

边检验(two-sided test)，亦称双尾检验、双侧检验.在假设检验中，用检验统计量的密度曲线和x轴所围成的面积的左右两边的尾部面积来构造临界区域进行检验的方法。


当我们的假设测试值的两边时。


例子：


对于零假设：


```
“均值等于 k”
```


我们可以有替代假设：


```
“均值不等于k”
```


在这种情况下，均值小于或大于 k，两边都要检查。


### 阿尔法值

阿尔法值是显著性水平。


显著性水平是估计总体参数落在某一区间内，可能犯错误的概率，用 **α** 表示。


数据必须有多接近极端才能拒绝零假设。


通常取为 0.01、0.05 或 0.1。


### P 值


P 值表明数据实际接近极端的程度。


比较 P 值和阿尔法值(alpha)来确定统计显著性水平。


如果 p 值







	  AI 思考中...





			** [SciPy 插值](https://www.runoob.com/scipy-interpolation.html)














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