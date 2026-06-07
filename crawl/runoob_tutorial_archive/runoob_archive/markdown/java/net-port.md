# Java 实例 - 查看端口是否已使用

- Source: https://www.runoob.com/java/net-port.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何检测端口是否已经使用：


## 实例


```java
import java.net.*;
import java.io.*;

public class Main {
   public static void main(String[] args) {
      Socket Skt;
      String host = "localhost";
      if (args.length > 0) {
         host = args[0];
      }
      for (int i = 0; i < 1024; i++) {
         try {
            System.out.println("查看 "+ i);
            Skt = new Socket(host, i);
            System.out.println("端口 " + i + " 已被使用");
         }
         catch (UnknownHostException e) {
            System.out.println("Exception occured"+ e);
            break;
         }
         catch (IOException e) {
         }
      }
   }
}
```


以上代码运行输出结果为：


```
……
查看 17
查看 18
查看 19
查看 20
查看 21
端口 21 已被使用
查看 22
查看 23
查看 24
……
```


也可以指定主机的端口：


## Main.java 文件



```java
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.SocketTimeoutException;

public class Main {

    public static void main(String[] args) {
        // 检测本地 80 端口
        log(isSocketAliveUitlitybyCrunchify("localhost", 80));

        // 检测本地 8080 端口
        log(isSocketAliveUitlitybyCrunchify("localhost", 8080));

        // 检测本地 8081 端口
        log(isSocketAliveUitlitybyCrunchify("localhost", 8081));

        // 检测 runoob.com 的 80 端口
        log(isSocketAliveUitlitybyCrunchify("runoob.com", 80));

         // 检测 runoob.com 的 443 端口
        log(isSocketAliveUitlitybyCrunchify("runoob.com", 443));

        // 检测 runoob.com 的 81 端口
        log(isSocketAliveUitlitybyCrunchify("runoob.com", 81));
    }

    /**
     * 判断主机端口
     *
     * @param hostName
     * @param port
     * @return boolean - true/false
     */
    public static boolean isSocketAliveUitlitybyCrunchify(String hostName, int port) {
        boolean isAlive = false;

        // 创建一个套接字
        SocketAddress socketAddress = new InetSocketAddress(hostName, port);
        Socket socket = new Socket();

        // 超时设置，单位毫秒
        int timeout = 2000;

        log("hostName: " + hostName + ", port: " + port);
        try {
            socket.connect(socketAddress, timeout);
            socket.close();
            isAlive = true;

        } catch (SocketTimeoutException exception) {
            System.out.println("SocketTimeoutException " + hostName + ":" + port + ". " + exception.getMessage());
        } catch (IOException exception) {
            System.out.println(
                    "IOException - Unable to connect to " + hostName + ":" + port + ". " + exception.getMessage());
        }
        return isAlive;
    }

    private static void log(String string) {
        System.out.println(string);
    }

    private static void log(boolean isAlive) {
        System.out.println("是否真正在使用: " + isAlive + "\n");
    }

}
```


以上代码运行输出结果为：


```
hostName: localhost, port: 80
IOException - Unable to connect to localhost:80. Connection refused
是否真正在使用: true

hostName: localhost, port: 8080
IOException - Unable to connect to localhost:8080. Connection refused
是否真正在使用: false

hostName: localhost, port: 8081
IOException - Unable to connect to localhost:8081. Connection refused
是否真正在使用: false

hostName: runoob.com, port: 80
是否真正在使用: true

hostName: runoob.com, port: 443
是否真正在使用: true

hostName: runoob.com, port: 81
SocketTimeoutException runoob.com:81. connect timed out
是否真正在使用: false
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 获取本机ip地址及主机名](https://www.runoob.com/net-localip.html)
			[Java 实例 – 查看线程是否存活](https://www.runoob.com/thread-alive.html) **













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

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





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