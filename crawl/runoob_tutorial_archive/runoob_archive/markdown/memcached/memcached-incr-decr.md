# Memcached incr 与 decr 命令

- Source: https://www.runoob.com/memcached/memcached-incr-decr.html

Memcached incr 与 decr 命令用于对已存在的 key(键) 的数字值进行自增或自减操作。


incr 与 decr 命令操作的数据必须是十进制的32位无符号整数。


如果 key 不存在返回 **NOT_FOUND**，如果键的值不为数字，则返回 **CLIENT_ERROR**，其他错误返回 **ERROR**。


---

## incr 命令


### 语法：


incr 命令的基本语法格式如下：


```
incr key increment_value
```


参数说明如下：


- **key：**键值 key-value 结构中的 key，用于查找缓存值。
- **increment_value**： 增加的数值。


### 实例


在以下实例中，我们使用 visitors 作为 key，初始值为 10，之后进行加 5 操作。


```
set visitors 0 900 2
10
STORED
get visitors
VALUE visitors 0 2
10
END
incr visitors 5
15
get visitors
VALUE visitors 0 2
15
END
```


### 输出


输出信息说明：


- **NOT_FOUND**：key 不存在。
- **CLIENT_ERROR**：自增值不是对象。
- **ERROR**其他错误，如语法错误等。


---

## decr 命令


decr 命令的基本语法格式如下：


```
decr key decrement_value
```


参数说明如下：


- **key：**键值 key-value 结构中的 key，用于查找缓存值。
- **decrement_value**： 减少的数值。


### 实例


```
set visitors 0 900 2
10
STORED
get visitors
VALUE visitors 0 2
10
END
decr visitors 5
5
get visitors
VALUE visitors 0 1
5
END
```


在以下实例中，我们使用 visitors 作为 key，初始值为 10，之后进行减 5 操作。 ### 输出 输出信息说明：


- **NOT_FOUND**：key 不存在。
- **CLIENT_ERROR**：自增值不是对象。
- **ERROR**其他错误，如语法错误等。









	  AI 思考中...





			** [Memcached delete 命令](https://www.runoob.com/memcached-delete-key.html)
			[Memcached stats 命令](https://www.runoob.com/memcached-stats.html) **













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