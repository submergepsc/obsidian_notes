# Java 实例 - Socket 实现多线程服务器程序

- Source: https://www.runoob.com/java/net-multisoc.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


在 Java 中，实现一个多线程服务器程序可以通过使用 `ServerSocket` 来监听客户端连接，每当有新的客户端连接时，启动一个新的线程来处理该连接。下面是一个示例代码，展示了如何使用 Java Socket 实现一个多线程服务器程序。


### 服务器端代码


首先，我们创建一个服务器端程序，它会监听指定的端口，并为每个客户端连接启动一个新的线程来处理通信。


## MultiThreadedServer.java 文件



```java
import java.io.*;
import java.net.*;

public class MultiThreadedServer {
    public static void main(String[] args) {
        int port = 12345; // 定义服务器端口
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("服务器已启动，等待客户端连接...");

            while (true) {
                Socket clientSocket = serverSocket.accept(); // 接受客户端连接
                System.out.println("客户端已连接: " + clientSocket.getInetAddress().getHostAddress());

                // 为每个客户端连接启动一个新的线程
                ClientHandler clientHandler = new ClientHandler(clientSocket);
                new Thread(clientHandler).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class ClientHandler implements Runnable {
    private Socket clientSocket;

    public ClientHandler(Socket socket) {
        this.clientSocket = socket;
    }

    @Override
    public void run() {
        try (
            InputStream input = clientSocket.getInputStream();
            OutputStream output = clientSocket.getOutputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            PrintWriter writer = new PrintWriter(output, true)
        ) {
            String clientMessage;
            while ((clientMessage = reader.readLine()) != null) {
                System.out.println("收到客户端消息: " + clientMessage);
                writer.println("服务器回应: " + clientMessage); // 发送回应消息给客户端
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```


### 客户端代码

客户端代码用于连接服务器并发送消息。可以创建多个客户端来测试服务器的多线程处理能力。


## Client.java 文件代码：


```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 12345; // 服务器端口

        try (Socket socket = new Socket(serverAddress, port)) {
            System.out.println("已连接到服务器");

            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);
            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));

            String userInput;
            while ((userInput = consoleReader.readLine()) != null) {
                writer.println(userInput);
                String serverResponse = reader.readLine();
                System.out.println("服务器回应: " + serverResponse);
            }
        } catch (UnknownHostException e) {
            System.err.println("不明主机: " + serverAddress);
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("无法获取 I/O 连接到: " + serverAddress);
            e.printStackTrace();
        }
    }
}
```



### 运行步骤


- **运行服务器端**： - 编译并运行 `MultiThreadedServer` 类。 - 服务器将启动并监听指定端口上的客户端连接。
- **运行客户端**： - 编译并运行多个 `Client` 类实例，模拟多个客户端连接到服务器。 - 在客户端控制台中输入消息，客户端会将消息发送到服务器，服务器将回应相同的消息。


### 解释


- **`ServerSocket`**: 服务器端用来监听客户端连接的套接字。
- **`Socket`**: 客户端和服务器之间的通信通道。
- **`ClientHandler`**: 处理每个客户端连接的线程类。
- **`BufferedReader` 和 `PrintWriter`**: 用于读取和写入数据流。


这种实现方式确保了服务器能够同时处理多个客户端连接，而不会因为一个客户端的长时间操作而阻塞其他客户端的请求。


### 编译代码

打开终端或命令提示符，切换到存上述 Java 文件的目录，然后编译代码：


```
javac MultiThreadedServer.java Client.java
```


在编译完成后，首先运行服务器程序，服务器将启动并开始监听端口 12345。


```
java MultiThreadedServer
```


你会看到服务器输出：


```
服务器已启动，等待客户端连接...
```


打开另一个终端或命令提示符窗口，运行客户端程序。你可以运行多个客户端实例来测试多线程处理。


```
java Client
```


你会看到客户端输出：


```
已连接到服务器
```


然后，你可以在客户端控制台中输入消息，例如：


```
Hello Server
```


服务器会回应：


```
服务器回应: Hello Server
```


服务器端的输出会显示：


```
客户端已连接: 127.0.0.1
收到客户端消息: Hello Server
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 查看主机指定文件的最后修改时间](https://www.runoob.com/net-filetime.html)
			[Java 实例 – 获取远程文件大小](https://www.runoob.com/net-serverfile.html) **













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