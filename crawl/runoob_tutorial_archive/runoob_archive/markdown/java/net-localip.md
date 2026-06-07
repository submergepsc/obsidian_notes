# Java 实例 - 获取本机ip地址及主机名

- Source: https://www.runoob.com/java/net-localip.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


在 Java 中，可以使用标准的网络库来获取本机的 IP 地址和主机名。


以下实例演示了如何使用 InetAddress 类的 getLocalHost 和 getLocalAddress() 方法获取本机主机名及 ip 地址：


## Main.java 文件



```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class NetworkInfo {
    public static void main(String[] args) {
        try {
            // 获取本地主机对象
            InetAddress localHost = InetAddress.getLocalHost();

            // 获取主机名
            String hostName = localHost.getHostName();
            System.out.println("主机名: " + hostName);

            // 获取IP地址
            String hostAddress = localHost.getHostAddress();
            System.out.println("IP地址: " + hostAddress);
        } catch (UnknownHostException e) {
            System.err.println("无法获取本机IP地址及主机名: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```


### 说明


- `InetAddress.getLocalHost()`：获取表示本地主机的`InetAddress`对象。
- `getHostName()`：获取本地主机的主机名。
- `getHostAddress()`：获取本地主机的IP地址。

### 异常处理

- `UnknownHostException`：当无法确定本地主机名或IP地址时抛出。


以上代码运行输出结果为：


```
主机名: your-hostname
IP地址: 192.168.1.2
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 网页抓取](https://www.runoob.com/net-webpage.html)
			[Java 实例 – 查看端口是否已使用](https://www.runoob.com/net-port.html) **













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