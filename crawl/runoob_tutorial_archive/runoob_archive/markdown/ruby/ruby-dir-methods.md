# Ruby Dir 类和方法

- Source: https://www.runoob.com/ruby/ruby-dir-methods.html

**Dir** 是一个表示用于给出操作系统中目录中的文件名的目录流。Dir 类也拥有与目录相关的操作，比如通配符文件名匹配、改变工作目录等。


## 类方法


| 序号 | 方法 & 描述 |
| --- | --- |
| 1 | Dir[pat] Dir::glob( pat)返回一个数组，包含与指定的通配符模式 pat 匹配的文件名： * - 匹配包含 null 字符串的任意字符串 ** - 递归地匹配任意字符串 ? - 匹配任意单个字符 [...] - 匹配封闭字符中的任意一个 {a,b...} - 匹配字符串中的任意一个 Dir["foo.*"] # 匹配 "foo.c"、 "foo.rb" 等等 Dir["foo.?"] # 匹配 "foo.c"、 "foo.h" 等等 |
| 2 | Dir::chdir( path)改变当前目录。 |
| 3 | Dir::chroot( path)改变根目录（只允许超级用户）。并不是在所有的平台上都可用。 |
| 4 | Dir::delete( path)删除 path 指定的目录。目录必须是空的。 |
| 5 | Dir::entries( path)返回一个数组，包含目录 path 中的文件名。 |
| 6 | Dir::foreach( path) {\| f\| ...}为 path 指定的目录中的每个文件执行一次块。 |
| 7 | Dir::getwd Dir::pwd返回当前目录。 |
| 8 | Dir::mkdir( path[, mode=0777])创建 path 指定的目录。权限模式可被 File::umask 的值修改，在 Win32 的平台上会被忽略。 |
| 9 | Dir::new( path) Dir::open( path) Dir::open( path) {\| dir\| ...}返回 path 的新目录对象。如果 open 给出一个块，则新目录对象会传到该块，块会在终止前关闭目录对象。 |
| 10 | Dir::pwd参见 Dir::getwd。 |
| 11 | Dir::rmdir( path) Dir::unlink( path) Dir::delete( path)删除 path 指定的目录。目录必须是空的。 |


## 实例方法


假设 **d** 是 **Dir** 类的一个实例：


| 序号 | 方法 & 描述 |
| --- | --- |
| 1 | d.close关闭目录流。 |
| 2 | d.each {\| f\| ...}为 d 中的每一个条目执行一次块。 |
| 3 | d.pos d.tell返回 d 中的当前位置。 |
| 4 | d.pos= offset设置目录流中的位置。 |
| 5 | d.pos= pos d.seek(pos)移动到 d 中的某个位置。pos 必须是一个由 d.pos 返回的值或 0。 |
| 6 | d.read返回 d 的下一个条目。 |
| 7 | d.rewind移动 d 中的位置到第一个条目。 |
| 8 | d.seek(po s)参见 d.pos=pos。 |
| 9 | d.tell参见 d.pos。 |








	  AI 思考中...





			** [Ruby File 类和方法](https://www.runoob.com/ruby-file-methods.html)
			[Ruby 异常](https://www.runoob.com/ruby-exceptions.html) **













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