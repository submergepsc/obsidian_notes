# Ruby 命令行选项

- Source: https://www.runoob.com/ruby/ruby-command-line-options.html

Ruby 一般是从命令行运行，方式如下：


```
$ ruby [ options ] [.] [ programfile ] [ arguments ... ]
```


解释器可以通过下列选项被调用，来控制解释器的环境和行为。


| 选项 | 描述 |
| --- | --- |
| -a | 与 -n 或 -p 一起使用时，可以打开自动拆分模式(auto split mode)。请查看 -n 和 -p 选项。 |
| -c | 只检查语法，不执行程序。 |
| -C dir | 在执行前改变目录（等价于 -X）。 |
| -d | 启用调试模式（等价于 -debug）。 |
| -F pat | 指定 pat 作为默认的分离模式（$;）。 |
| -e prog | 指定 prog 作为程序在命令行中执行。可以指定多个 -e 选项，用来执行多个程序。 |
| -h | 显示命令行选项的一个概览。 |
| -i [ ext] | 把文件内容重写为程序输出。原始文件会被加上扩展名 ext 保存下来。如果未指定 ext，原始文件会被删除。 |
| -I dir | 添加 dir 作为加载库的目录。 |
| -K [ kcode] | 指定多字节字符集编码。e 或 E 对应 EUC（extended Unix code），s 或 S 对应 SJIS（Shift-JIS），u 或 U 对应 UTF-8，a、A、n 或 N 对应 ASCII。 |
| -l | 启用自动行尾处理。从输入行取消一个换行符，并向输出行追加一个换行符。 |
| -n | 把代码放置在一个输入循环中（就像在 while gets; ... end 中一样）。 |
| -0[ octal] | 设置默认的记录分隔符（$/）为八进制。如果未指定 octal 则默认为 \0。 |
| -p | 把代码放置在一个输入循环中。在每次迭代后输出变量 $_ 的值。 |
| -r lib | 使用 require 来加载 lib 作为执行前的库。 |
| -s | 解读程序名称和文件名参数之间的匹配模式 -xxx 的任何参数作为开关，并定义相应的变量。 |
| -T [level] | 设置安全级别，执行不纯度测试（如果未指定 level，则默认值为 1）。 |
| -v | 显示版本，并启用冗余模式。 |
| -w | 启用冗余模式。如果未指定程序文件，则从 STDIN 读取。 |
| -x [dir] | 删除 #!ruby 行之前的文本。如果指定了 dir，则把目录改变为 dir。 |
| -X dir | 在执行前改变目录（等价于 -C）。 |
| -y | 启用解析器调试模式。 |
| --copyright | 显示版权声明。 |
| --debug | 启用调试模式（等价于 -d）。 |
| --help | 显示命令行选项的一个概览（等价于 -h）。 |
| --version | 显示版本。 |
| --verbose | 启用冗余模式（等价于 -v）。设置 $VERBOSE 为 true。 |
| --yydebug | 启用解析器调试模式（等价于 -y）。 |


单字符的命令行选项可以组合使用。下面两行表达了同样的意思：


```
$ ruby -ne 'print if /Ruby/' /usr/share/bin


$ ruby -n -e 'print if /Ruby/' /usr/share/bin
```









	  AI 思考中...





			** [Ruby 安装 – Windows](https://www.runoob.com/ruby-installation-windows.html)
			[Ruby 环境变量](https://www.runoob.com/ruby-environment-variables.html) **













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