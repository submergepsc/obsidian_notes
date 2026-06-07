# Redis 服务器

- Source: https://www.runoob.com/redis/redis-server.html

Redis 服务器命令主要是用于管理 redis 服务。


### 实例


以下实例演示了如何获取 redis 服务器的统计信息：


```
redis 127.0.0.1:6379> INFO

# Server
redis_version:2.8.13
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:c2238b38b1edb0e2
redis_mode:standalone
os:Linux 3.5.0-48-generic x86_64
arch_bits:64
multiplexing_api:epoll
gcc_version:4.7.2
process_id:3856
run_id:0e61abd297771de3fe812a3c21027732ac9f41fe
tcp_port:6379
uptime_in_seconds:11554
uptime_in_days:0
hz:10
lru_clock:16651447
config_file:

# Clients
connected_clients:1
client-longest_output_list:0
client-biggest_input_buf:0
blocked_clients:0

# Memory
used_memory:589016
used_memory_human:575.21K
used_memory_rss:2461696
used_memory_peak:667312
used_memory_peak_human:651.67K
used_memory_lua:33792
mem_fragmentation_ratio:4.18
mem_allocator:jemalloc-3.6.0

# Persistence
loading:0
rdb_changes_since_last_save:3
rdb_bgsave_in_progress:0
rdb_last_save_time:1409158561
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok

# Stats
total_connections_received:24
total_commands_processed:294
instantaneous_ops_per_sec:0
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
evicted_keys:0
keyspace_hits:41
keyspace_misses:82
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:264

# Replication
role:master
connected_slaves:0
master_repl_offset:0
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:10.49
used_cpu_user:4.96
used_cpu_sys_children:0.00
used_cpu_user_children:0.01

# Keyspace
db0:keys=94,expires=1,avg_ttl=41638810
db1:keys=1,expires=0,avg_ttl=0
db3:keys=1,expires=0,avg_ttl=0
```


---


## Redis 服务器命令


下表列出了 redis 服务器的相关命令:


| 序号 | 命令及描述 |
| --- | --- |
| 1 | BGREWRITEAOF 异步执行一个 AOF（AppendOnly File） 文件重写操作 |
| 2 | BGSAVE 在后台异步保存当前数据库的数据到磁盘 |
| 3 | CLIENT KILL [ip:port] [ID client-id] 关闭客户端连接 |
| 4 | CLIENT LIST 获取连接到服务器的客户端连接列表 |
| 5 | CLIENT GETNAME 获取连接的名称 |
| 6 | CLIENT PAUSE timeout 在指定时间内终止运行来自客户端的命令 |
| 7 | CLIENT SETNAME connection-name 设置当前连接的名称 |
| 8 | CLUSTER SLOTS 获取集群节点的映射数组 |
| 9 | COMMAND 获取 Redis 命令详情数组 |
| 10 | COMMAND COUNT 获取 Redis 命令总数 |
| 11 | COMMAND GETKEYS 获取给定命令的所有键 |
| 12 | TIME 返回当前服务器时间 |
| 13 | COMMAND INFO command-name [command-name ...] 获取指定 Redis 命令描述的数组 |
| 14 | CONFIG GET parameter 获取指定配置参数的值 |
| 15 | CONFIG REWRITE 对启动 Redis 服务器时所指定的 redis.conf 配置文件进行改写 |
| 16 | CONFIG SET parameter value 修改 redis 配置参数，无需重启 |
| 17 | CONFIG RESETSTAT 重置 INFO 命令中的某些统计数据 |
| 18 | DBSIZE 返回当前数据库的 key 的数量 |
| 19 | DEBUG OBJECT key 获取 key 的调试信息 |
| 20 | DEBUG SEGFAULT 让 Redis 服务崩溃 |
| 21 | FLUSHALL 删除所有数据库的所有key |
| 22 | FLUSHDB 删除当前数据库的所有key |
| 23 | INFO [section] 获取 Redis 服务器的各种信息和统计数值 |
| 24 | LASTSAVE 返回最近一次 Redis 成功将数据保存到磁盘上的时间，以 UNIX 时间戳格式表示 |
| 25 | MONITOR 实时打印出 Redis 服务器接收到的命令，调试用 |
| 26 | ROLE 返回主从实例所属的角色 |
| 27 | SAVE 同步保存数据到硬盘 |
| 28 | SHUTDOWN [NOSAVE] [SAVE] 异步保存数据到硬盘，并关闭服务器 |
| 29 | SLAVEOF host port 将当前服务器转变为指定服务器的从属服务器(slave server) |
| 30 | SLOWLOG subcommand [argument] 管理 redis 的慢日志 |
| 31 | SYNC 用于复制功能(replication)的内部命令 |








	  AI 思考中...





			** [Redis Select 命令](https://www.runoob.com/connection-select.html)
			[Redis Bgrewriteaof 命令](https://www.runoob.com/server-bgrewriteaof.html) **













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