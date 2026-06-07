# PHP FTP 函数

- Source: https://www.runoob.com/php/php-ref-ftp.html

---


## PHP FTP 简介


FTP 函数通过文件传输协议 (FTP) 提供对文件服务器的客户端访问。


FTP 函数用于打开、登录以及关闭连接，同时用于上传、下载、重命名、删除及获取文件服务器上的文件信息。不是所有的 FTP 函数对每个服务器都起作用或返回相同的结果。自 PHP 3 起，FTP 函数可用。


这些函数用于对 FTP 服务器进行细致的访问。如果您仅仅需要对 FTP 服务器进行读写操作，建议使用 Filesystem 函数中的 ftp:// wrapper。


---


## 安装


PHP 的 Windows 版本内置了对 FTP 扩展的支持。无需加载任何附加扩展库即可使用 FTP 函数。


然而，如果您运行的是 PHP 的 Linux 版本，在编译 PHP 的时候请添加 *--enable-ftp * 选项（PHP4 或以上版本）或者 *--with-ftp* 选项（PHP3 版本）。


---


## PHP FTP 函数


**PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| ftp_alloc() | 为要上传到 FTP 服务器的文件分配空间。 | 5 |
| ftp_cdup() | 把当前目录改变为 FTP 服务器上的父目录。 | 3 |
| ftp_chdir() | 改变 FTP 服务器上的当前目录。 | 3 |
| ftp_chmod() | 通过 FTP 设置文件上的权限。 | 5 |
| ftp_close() | 关闭 FTP 连接。 | 4 |
| ftp_connect() | 打开 FTP 连接。 | 3 |
| ftp_delete() | 删除 FTP 服务器上的一个文件。 | 3 |
| ftp_exec() | 在 FTP 服务器上执行一个程序/命令。 | 4 |
| ftp_fget() | 从 FTP 服务器上下载一个文件并保存到本地一个已经打开的文件中。 | 3 |
| ftp_fput() | 上传一个已经打开的文件，并在 FTP 服务器上把它保存为一个文件。 | 3 |
| ftp_get_option() | 返回 FTP 连接的各种运行时选项。 | 4 |
| ftp_get() | 从 FTP 服务器上下载文件。 | 3 |
| ftp_login() | 登录 FTP 服务器。 | 3 |
| ftp_mdtm() | 返回指定文件的最后修改时间。 | 3 |
| ftp_mkdir() | 在 FTP 服务器上创建一个新目录。 | 3 |
| ftp_nb_continue() | 连续获取/发送文件。（无阻塞） | 4 |
| ftp_nb_fget() | 从 FTP 服务器上下载一个文件并保存到本地一个已经打开的文件中。（无阻塞） | 4 |
| ftp_nb_fput() | 上传一个已经打开的文件，并在 FTP 服务器上把它保存为一个文件。（无阻塞） | 4 |
| ftp_nb_get() | 从 FTP 服务器上下载文件。（无阻塞） | 4 |
| ftp_nb_put() | 把文件上传到 FTP 服务器上。（无阻塞） | 4 |
| ftp_nlist() | 返回 FTP 服务器上指定目录的文件列表。 | 3 |
| ftp_pasv() | 把被动模式设置为打开或关闭。 | 3 |
| ftp_put() | 把文件上传到 FTP 服务器上。 | 3 |
| ftp_pwd() | 返回当前目录名称。 | 3 |
| ftp_quit() | ftp_close() 的别名。 | 3 |
| ftp_raw() | 向 FTP 服务器发送一个 raw 命令。 | 5 |
| ftp_rawlist() | 返回指定目录中文件的详细列表。 | 3 |
| ftp_rename() | 重命名 FTP 服务器上的文件或目录。 | 3 |
| ftp_rmdir() | 删除 FTP 服务器上的一个目录。 | 3 |
| ftp_set_option() | 设置 FTP 连接的各种运行时选项。 | 4 |
| ftp_site() | 向服务器发送 SITE 命令。 | 3 |
| ftp_size() | 返回指定文件的大小。 | 3 |
| ftp_ssl_connect() | 打开一个安全的 SSL-FTP 连接。 | 4 |
| ftp_systype() | 返回 FTP 服务器的系统类型标识符。 | 3 |

**
---


## PHP FTP 常量


PHP**：指示支持该常量的最早的 PHP 版本。


| 常量 | 描述 | PHP |
| --- | --- | --- |
| FTP_ASCII |  | 3 |
| FTP_TEXT |  | 3 |
| FTP_BINARY |  | 3 |
| FTP_IMAGE |  | 3 |
| FTP_TIMEOUT_SEC |  | 3 |
| FTP_AUTOSEEK |  | 4 |
| FTP_AUTORESUME | 为 GET 和 PUT 请求自动决定恢复和开始的位置 | 4 |
| FTP_FAILED | 异步传输失败 | 4 |
| FTP_FINISHED | 异步传输成功 | 4 |
| FTP_MOREDATA | 异步传输是活动状态的 | 4 |








	  AI 思考中...





			** [PHP Filter 函数](https://www.runoob.com/php-ref-filter.html)
			[PHP HTTP 函数](https://www.runoob.com/php-ref-http.html) **













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