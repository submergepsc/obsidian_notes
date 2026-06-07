# Java 实例 - ServerSocket 和 Socket 通信实例

- Source: https://www.runoob.com/java/net-serversocket-socket.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何实现客户端发送消息到服务器，服务器接收到消息并读取输出，然后写出到客户端客户端接收到输出。


### 1、建立服务器端


- 服务器建立通信ServerSocket
- 服务器建立Socket接收客户端连接
- 建立IO输入流读取客户端发送的数据
- 建立IO输出流向客户端发送数据消息


服务器端代码:


## Server.java 文件



```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
   public static void main(String[] args) {
      try {
         ServerSocket ss = new ServerSocket(8888);
         System.out.println("启动服务器....");
         Socket s = ss.accept();
         System.out.println("客户端:"+s.getInetAddress().getLocalHost()+"已连接到服务器");

         BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
         //读取客户端发送来的消息
         String mess = br.readLine();
         System.out.println("客户端："+mess);
         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
         bw.write(mess+"\n");
         bw.flush();
      } catch (IOException e) {
         e.printStackTrace();
      }
   }
}
```


以上代码运行输出结果为：


```
启动服务器....
```


### 2、建立客户端


- 创建Socket通信，设置通信服务器的IP和Port
- 建立IO输出流向服务器发送数据消息
- 建立IO输入流读取服务器发送来的数据消息


客户端代码:


## Client.java 文件



```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
   public static void main(String[] args) {
      try {
         Socket s = new Socket("127.0.0.1",8888);

         //构建IO
         InputStream is = s.getInputStream();
         OutputStream os = s.getOutputStream();

         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(os));
         //向服务器端发送一条消息
         bw.write("测试客户端和服务器通信，服务器接收到消息返回到客户端\n");
         bw.flush();

         //读取服务器返回的消息
         BufferedReader br = new BufferedReader(new InputStreamReader(is));
         String mess = br.readLine();
         System.out.println("服务器："+mess);
      } catch (UnknownHostException e) {
         e.printStackTrace();
      } catch (IOException e) {
         e.printStackTrace();
      }
   }
}
```


以上代码运行输出结果为：


```
服务器：测试客户端和服务器通信，服务器接收到消息返回到客户端
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 获取远程文件大小](https://www.runoob.com/net-serverfile.html)
			[Java 实例 – 解析 URL](https://www.runoob.com/net-url.html) **













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