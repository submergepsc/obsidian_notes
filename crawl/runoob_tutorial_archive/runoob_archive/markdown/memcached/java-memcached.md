# Java 连接 Memcached 服务

- Source: https://www.runoob.com/memcached/java-memcached.html

使用 Java 程序连接 Memcached，需要在你的 classpath 中添加 Memcached jar 包。


本站 jar 包下载地址：[spymemcached-2.10.3.jar](https://www.runoob.com/try/download/spymemcached-2.10.3.jar)。


Google Code jar 包下载地址：[spymemcached-2.10.3.jar](https://code.google.com/p/spymemcached/downloads/list)（需要科学上网）。



以下程序假定 Memcached 服务的主机为 127.0.0.1，端口为 11211。


### 连接实例


Java 连接 Memcached


## MemcachedJava.java 文件：


```memcached
import net.spy.memcached.MemcachedClient;
import java.net.*;

public class MemcachedJava {
   public static void main(String[] args) {
      try{
         // 本地连接 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex){
         System.out.println( ex.getMessage() );
      }
   }
}
```


该程序中我们使用 InetSocketAddress 连接 IP 为 127.0.0.1 端口 为 11211 的 memcached 服务。


执行以上代码，如果连接成功会输出以下信息：


```
Connection to server successful.
```


### set 操作实例


以下使用 java.util.concurrent.Future 来存储数据


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{
         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 存储数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 查看存储状态
         System.out.println("set status:" + fo.get());

         // 输出值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex){
         System.out.println( ex.getMessage() );
      }
   }
}
```


执行程序，输出结果为：


```
Connection to server successful.
set status:true
runoob value in cache - Free Education
```


### add 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 打印状态
         System.out.println("set status:" + fo.get());

         // 输出
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 添加
         fo = mcc.add("runoob", 900, "memcached");

         // 打印状态
         System.out.println("add status:" + fo.get());

         // 添加新key
         fo = mcc.add("runoob", 900, "All Free Compilers");

         // 打印状态
         System.out.println("add status:" + fo.get());

         // 输出
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex){
         System.out.println(ex.getMessage());
      }
   }
}
```


### replace 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try {
         //连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加第一个 key=》value 对
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 输出执行 add 方法后的状态
         System.out.println("add status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 添加新的 key
         fo = mcc.replace("runoob", 900, "Largest Tutorials' Library");

         // 输出执行 set 方法后的状态
         System.out.println("replace status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex){
         System.out.println( ex.getMessage() );
      }
   }
}
```


### append 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 对存在的key进行数据添加操作
         fo = mcc.append("runoob", 900, " for All");

         // 输出执行 set 方法后的状态
         System.out.println("append status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      ]
   }
}
```


### prepend 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Education for All");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 对存在的key进行数据添加操作
         fo = mcc.prepend("runoob", 900, "Free ");

         // 输出执行 set 方法后的状态
         System.out.println("prepend status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```


### CAS 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.CASValue;
import net.spy.memcached.CASResponse;
import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 使用 get 方法获取数据
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 通过 gets 方法获取 CAS token（令牌）
         CASValue casValue = mcc.gets("runoob");

         // 输出 CAS token（令牌） 值
         System.out.println("CAS token - " + casValue);

         // 尝试使用cas方法来更新数据
         CASResponse casresp = mcc.cas("runoob", casValue.getCas(), 900, "Largest Tutorials-Library");

         // 输出 CAS 响应信息
         System.out.println("CAS Response - " + casresp);

         // 输出值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```


### get 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 使用 get 方法获取数据
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```


### gets 操作实例、CAS


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.CASValue;
import net.spy.memcached.CASResponse;
import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "Free Education");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 从缓存中获取键为 runoob 的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 通过 gets 方法获取 CAS token（令牌）
         CASValue casValue = mcc.gets("runoob");

         // 输出 CAS token（令牌） 值
         System.out.println("CAS value in cache - " + casValue);

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```


### delete 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数据
         Future fo = mcc.set("runoob", 900, "World's largest online tutorials library");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 对存在的key进行数据添加操作
        fo = mcc.delete("runoob");

         // 输出执行 delete 方法后的状态
         System.out.println("delete status:" + fo.get());

         // 获取键对应的值
         System.out.println("runoob value in cache - " + mcc.get("runoob"));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```


### Incr/Decr 操作实例


## MemcachedJava.java 文件：


```memcached
import java.net.InetSocketAddress;
import java.util.concurrent.Future;

import net.spy.memcached.MemcachedClient;

public class MemcachedJava {
   public static void main(String[] args) {

      try{

         // 连接本地的 Memcached 服务
         MemcachedClient mcc = new MemcachedClient(new InetSocketAddress("127.0.0.1", 11211));
         System.out.println("Connection to server successful.");

         // 添加数字值
         Future fo = mcc.set("number", 900, "1000");

         // 输出执行 set 方法后的状态
         System.out.println("set status:" + fo.get());

         // 获取键对应的值
         System.out.println("value in cache - " + mcc.get("number"));

         // 自增并输出
         System.out.println("value in cache after increment - " + mcc.incr("number", 111));

         // 自减并输出
         System.out.println("value in cache after decrement - " + mcc.decr("number", 112));

         // 关闭连接
         mcc.shutdown();

      }catch(Exception ex) {
         System.out.println(ex.getMessage());
      }
   }
}
```










	  AI 思考中...





			** [Memcached flush_all 命令](https://www.runoob.com/memcached-clear-data.html)
			[Windows 下安装 Memcached](https://www.runoob.com/window-install-memcached.html) **













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