# Memcached stats 命令

- Source: https://www.runoob.com/memcached/memcached-stats.html

Memcached stats 命令用于返回统计信息例如 PID(进程号)、版本号、连接数等。


### 语法：


stats 命令的基本语法格式如下：


```
stats
```


### 实例


在以下实例中，我们使用了 stats 命令来输出 Memcached 服务信息。


```
stats
STAT pid 1162
STAT uptime 5022
STAT time 1415208270
STAT version 1.4.14
STAT libevent 2.0.19-stable
STAT pointer_size 64
STAT rusage_user 0.096006
STAT rusage_system 0.152009
STAT curr_connections 5
STAT total_connections 6
STAT connection_structures 6
STAT reserved_fds 20
STAT cmd_get 6
STAT cmd_set 4
STAT cmd_flush 0
STAT cmd_touch 0
STAT get_hits 4
STAT get_misses 2
STAT delete_misses 1
STAT delete_hits 1
STAT incr_misses 2
STAT incr_hits 1
STAT decr_misses 0
STAT decr_hits 1
STAT cas_misses 0
STAT cas_hits 0
STAT cas_badval 0
STAT touch_hits 0
STAT touch_misses 0
STAT auth_cmds 0
STAT auth_errors 0
STAT bytes_read 262
STAT bytes_written 313
STAT limit_maxbytes 67108864
STAT accepting_conns 1
STAT listen_disabled_num 0
STAT threads 4
STAT conn_yields 0
STAT hash_power_level 16
STAT hash_bytes 524288
STAT hash_is_expanding 0
STAT expired_unfetched 1
STAT evicted_unfetched 0
STAT bytes 142
STAT curr_items 2
STAT total_items 6
STAT evictions 0
STAT reclaimed 1
END
```


这里显示了很多状态信息，下边详细解释每个状态项：


- **pid**： memcache服务器进程ID
- **uptime**：服务器已运行秒数
- **time**：服务器当前Unix时间戳
- **version**：memcache版本
- **pointer_size**：操作系统指针大小
- **rusage_user**：进程累计用户时间
- **rusage_system**：进程累计系统时间
- **curr_connections**：当前连接数量
- **total_connections**：Memcached运行以来连接总数
- **connection_structures**：Memcached分配的连接结构数量
- **cmd_get**：get命令请求次数
- **cmd_set**：set命令请求次数
- **cmd_flush**：flush命令请求次数
- **get_hits**：get命令命中次数
- **get_misses**：get命令未命中次数
- **delete_misses**：delete命令未命中次数
- **delete_hits**：delete命令命中次数
- **incr_misses**：incr命令未命中次数
- **incr_hits**：incr命令命中次数
- **decr_misses**：decr命令未命中次数
- **decr_hits**：decr命令命中次数
- **cas_misses**：cas命令未命中次数
- **cas_hits**：cas命令命中次数
- **cas_badval**：使用擦拭次数
- **auth_cmds**：认证命令处理的次数
- **auth_errors**：认证失败数目
- **bytes_read**：读取总字节数
- **bytes_written**：发送总字节数
- **limit_maxbytes**：分配的内存总大小（字节）
- **accepting_conns**：服务器是否达到过最大连接（0/1）
- **listen_disabled_num**：失效的监听数
- **threads**：当前线程数
- **conn_yields**：连接操作主动放弃数目
- **bytes**：当前存储占用的字节数
- **curr_items**：当前存储的数据总数
- **total_items**：启动以来存储的数据总数
- **evictions**：LRU释放的对象数目
- **reclaimed**：已过期的数据条目来存储新数据的数目









	  AI 思考中...





			** [Memcached incr 与 decr 命令](https://www.runoob.com/memcached-incr-decr.html)
			[Memcached stats items 命令](https://www.runoob.com/memcached-stats-items.html) **













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