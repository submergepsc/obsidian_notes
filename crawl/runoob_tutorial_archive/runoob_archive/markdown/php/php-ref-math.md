# PHP 5 Math 函数

- Source: https://www.runoob.com/php/php-ref-math.html

---


## PHP Math 简介


Math 函数能处理 integer 和 float 范围内的值。


---


## 安装


PHP Math 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## PHP 5 Math 函数


| 函数 | 描述 |
| --- | --- |
| abs() | 返回一个数的绝对值。 |
| acos() | 返回一个数的反余弦。 |
| acosh() | 返回一个数的反双曲余弦。 |
| asin() | 返回一个数的反正弦。 |
| asinh() | 返回一个数的反双曲正弦。 |
| atan() | 返回一个数的反正切。 |
| atan2() | 返回两个变量 x 和 y 的反正切。 |
| atanh() | 返回一个数的反双曲正切。 |
| base_convert() | 在任意进制之间转换数字。 |
| bindec() | 把二进制数转换为十进制数。 |
| ceil() | 向上舍入为最接近的整数。 |
| cos() | 返回一个数的余弦。 |
| cosh() | 返回一个数的双曲余弦。 |
| decbin() | 把十进制数转换为二进制数。 |
| dechex() | 把十进制数转换为十六进制数。 |
| decoct() | 把十进制数转换为八进制数。 |
| deg2rad() | 将角度值转换为弧度值。 |
| exp() | 返回 Ex 的值。 |
| expm1() | 返回 Ex - 1 的值。 |
| floor() | 向下舍入为最接近的整数。 |
| fmod() | 返回 x/y 的浮点数余数。 |
| getrandmax() | 返回通过调用 rand() 函数显示的随机数的最大可能值。 |
| hexdec() | 把十六进制数转换为十进制数。 |
| hypot() | 计算直角三角形的斜边长度。 |
| is_finite() | 判断是否为有限值。 |
| is_infinite() | 判断是否为无限值。 |
| is_nan() | 判断是否为非数值。 |
| lcg_value() | 返回范围为 (0, 1) 的一个伪随机数。 |
| log() | 返回一个数的自然对数（以 E 为底）。 |
| log10() | 返回一个数的以 10 为底的对数。 |
| log1p() | 返回 log(1+number) |
| max() | 返回一个数组中的最大值，或者几个指定值中的最大值。 |
| min() | 返回一个数组中的最小值，或者几个指定值中的最小值。 |
| mt_getrandmax() | 返回通过调用 mt_rand() 函数显示的随机数的最大可能值。 |
| mt_rand() | 使用 Mersenne Twister 算法生成随机整数。 |
| mt_srand() | 播种 Mersenne Twister 随机数生成器。 |
| octdec() | 把八进制数转换为十进制数。 |
| pi() | 返回圆周率 PI 的值。 |
| pow() | 返回 x 的 y 次方。 |
| rad2deg() | 把弧度值转换为角度值。 |
| rand() | 返回随机整数。 |
| round() | 对浮点数进行四舍五入。 |
| sin() | 返回一个数的正弦。 |
| sinh() | 返回一个数的双曲正弦。 |
| sqrt() | 返回一个数的平方根。 |
| srand() | 播种随机数生成器。 |
| tan() | 返回一个数的正切。 |
| tanh() | 返回一个数的双曲正切。 |

**
---


## PHP 5 预定义的 Math 常量


| 常量 | 值 | 描述 | PHP 版本 |
| --- | --- | --- | --- |
| INF | INF | 无限 | PHP 4 |
| M_E | 2.7182818284590452354 | 返回 e | PHP 4 |
| M_EULER | 0.57721566490153286061 | 返回 Euler 常量 | PHP 4 |
| M_LNPI | 1.14472988584940017414 | 返回圆周率 PI 的自然对数：log_e(pi) | PHP 5.2 |
| M_LN2 | 0.69314718055994530942 | 返回 2 的自然对数：log_e 2 | PHP 4 |
| M_LN10 | 2.30258509299404568402 | 返回 10 的自然对数：log_e 10 | PHP 4 |
| M_LOG2E | 1.4426950408889634074 | 返回 E 的以 2 为底的对数：log_2 e | PHP 4 |
| M_LOG10E | 0.43429448190325182765 | 返回 E 的以 10 为底的对数：log_10 e | PHP 4 |
| M_PI | 3.14159265358979323846 | 返回 Pi | PHP 4 |
| M_PI_2 | 1.57079632679489661923 | 返回 Pi/2 | PHP 4 |
| M_PI_4 | 0.78539816339744830962 | 返回 Pi/4 | PHP 4 |
| M_1_PI | 0.31830988618379067154 | 返回 1/Pi | PHP 4 |
| M_2_PI | 0.63661977236758134308 | 返回 2/Pi | PHP 4 |
| M_SQRTPI | 1.77245385090551602729 | 返回圆周率 PI 的平方根：sqrt(pi) | PHP 5.2 |
| M_2_SQRTPI | 1.12837916709551257390 | 返回圆周率 PI 的 2/平方根：2/sqrt(pi) | PHP 4 |
| M_SQRT1_2 | 0.70710678118654752440 | 返回 1/2 的平方根：1/sqrt(2) | PHP 4 |
| M_SQRT2 | 1.41421356237309504880 | 返回 2 的平方根：sqrt(2) | PHP 4 |
| M_SQRT3 | 1.73205080756887729352 | 返回 3 的平方根：sqrt(3) | PHP 5.2 |
| NAN | NAN | 不是一个数字 | PHP 4 |
| PHP_ROUND_HALF_UP | 1 | 遇到 .5 的情况时向上舍入 | PHP 5.3 |
| PHP_ROUND_HALF_DOWN | 2 | 遇到 .5 的情况时向下舍入 | PHP 5.3 |
| PHP_ROUND_HALF_EVEN | 3 | 遇到 .5 的情况时取偶数舍入 | PHP 5.3 |
| PHP_ROUND_HALF_ODD | 4 | 遇到 .5 的情况时取奇数舍入 | PHP 5.3 |








	  AI 思考中...





			** [PHP Mail 函数](https://www.runoob.com/php-ref-mail.html)
			[PHP Misc. 函数](https://www.runoob.com/php-ref-misc.html) **













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