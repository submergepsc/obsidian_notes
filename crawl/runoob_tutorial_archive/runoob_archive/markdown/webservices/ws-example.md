# Web Service 实例

- Source: https://www.runoob.com/webservices/ws-example.html

---


任何应用程序都可拥有 Web Service 组件。


Web Service 的创建与编程语言的种类无关。


本章节我们将为大家介绍使用 PHP 的 SOAP 扩展来创建 Web Service。


SOAP有两种操作方式，NO-WSDL 与 WSDL。


- **NO-WSDL模式：**使用参数来传递要使用的信息。
- **WSDL模式：** 使用WSDL文件名作为参数，并从WSDL中提取服务所需的信息。


---


## 一个实例：PHP Web Service


在开始实例前，我们需要确定PHP是否安装了 SOAP 扩展。查看 phpinfo，出现以下信息表明已经安装了 SOAP 扩展：


![](https://www.runoob.com/wp-content/uploads/2013/09/phpinfo-soap.png)


在这个例子中，我们会使用 PHP SOAP 来创建一个简单的 Web Service。


服务端 **Server.php** 文件代码如下：


```
<?php
// SiteInfo 类用于处理请求
Class SiteInfo
{
    /**
     *    返回网站名称
     *    @return string
     *
     */
    public function getName(){
        return "菜鸟教程";
    }

    public function getUrl(){
        return "www.runoob.com";
    }
}

// 创建 SoapServer 对象
$s = new SoapServer(null,array("location"=>"http://localhost/soap/Server.php","uri"=>"Server.php"));

// 导出 SiteInfo 类中的全部函数
$s->setClass("SiteInfo");
// 处理一个SOAP请求，调用必要的功能，并发送回一个响应。
$s->handle();
?>
```


客户端 **Client.php** 文件代码如下：


```
<?php
try{
  // non-wsdl方式调用web service
  // 创建 SoapClient 对象
  $soap = new SoapClient(null,array('location'=>"http://localhost/soap/Server.php",'uri'=>'Server.php'));
  // 调用函数
  $result1 = $soap->getName();
  $result2 = $soap->__soapCall("getUrl",array());
  echo $result1."<br/>";
  echo $result2;
} catch(SoapFault $e){
  echo $e->getMessage();
}catch(Exception $e){
  echo $e->getMessage();
}
```


这时我们访问 http://localhost/soap/Client.php，输出结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2013/09/266876C0-6DF8-479C-AE5F-25ED1277F1B9.jpg)









	  AI 思考中...





			** [Web Services 平台元素](https://www.runoob.com/ws-platform.html)
			[Web Services 总结](https://www.runoob.com/ws-summary.html) **













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