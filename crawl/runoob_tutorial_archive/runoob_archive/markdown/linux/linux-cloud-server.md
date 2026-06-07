# 云服务器

- Source: https://www.runoob.com/linux/linux-cloud-server.html

**云服务器(Elastic Compute Service, ECS)**是一种简单高效、安全可靠、处理能力可弹性伸缩的计算服务。


云服务器管理方式比物理服务器更简单高效，我们无需提前购买昂贵的硬件，即可迅速创建或删除云服务器，云服务器费用一般在几十到几百不等，可以根据我们的需求配置。



目前市场上的云服务器很多，这里主要介绍以下几家：


- 阿里云：阿里云年度促销的服务器折扣很大，[直达链接](https://www.aliyun.com/minisite/goods?userCode=i5mn5r7m)。
- 腾讯云：腾讯云目前活动多一些，性价比也高，[直达链接](https://curl.qcloud.com/tzANIP5i)。
- [京东云](https://3.cn/1TSF9-L5)：京东云的服务器折扣很大，[直达链接](https://3.cn/1TSF9-L5)。
- 更多云服务器参考：**** [https://www.jyshare.com/cloud-server/](https://www.jyshare.com/cloud-server/)**


    **

注意：**很多云服务器给新用户提供的优惠力度是最大，基本上都是 1～2 折，建议新注册的用户购买。



## 阿里云


阿里云新用户购买折扣比较大，云服务器2核2G 3M固定带宽原价 **1507.56/年**, **现低至 **99元/年**，另外可以按 **99元** 续费一年，也就是 **198元** 用两年点击下面图片查看详情。**


[![](https://www.runoob.com/wp-content/uploads/2019/11/618-aliiiii.png)](https://www.aliyun.com/minisite/goods?userCode=i5mn5r7m)



---


## 腾讯云


腾讯云秒杀活动已开始，以下几款性价比非常高，有几款是需要抢购的，大家看好时间基本能拿到。


- 2核2G4M云服务器 新老同享 99元/年，续费同价。


每个时间点都有不同的配置跟价格，具体信息，可以点击下面的图片（**[**https://url.cn/zpx9ruoW](https://curl.qcloud.com/tzANIP5i)**）。


[![](https://www.runoob.com/wp-content/uploads/2019/11/txy-618888.png)](https://curl.qcloud.com/tzANIP5i)





当然，你也可以直接到[购买页面（点我直达）](https://www.aliyun.com/product/ecs?userCode=i5mn5r7m)选择更多配置及其他地域的云服务器：


[![](https://www.runoob.com/wp-content/uploads/2019/11/4FBA14FA-1036-4DE5-8A18-41E4D56F3AD5.jpg)](https://www.aliyun.com/product/ecs?userCode=i5mn5r7m)


红框为无需备案地区：


![](https://www.runoob.com/wp-content/uploads/2019/11/892F38BC-32E8-471B-8D37-0E307AB02175.jpg)






---


## 华为云

新用户折扣力度还是很大，可以点击下列图片，查看详情：


[![](https://www.runoob.com/wp-content/uploads/2019/11/B159DBCA-6853-48E3-8831-301174850A2C.jpg)](https://activity.huaweicloud.com/cps/recommendstore.html?fromacct=f3797f3d-4da5-4a2f-9149-130ad807c940&utm_source=dGlhbnFpeGlu=&utm_medium=cps&utm_campaign=201905)


华为云可在优惠券专区领取优惠券来购买：[点我领取优惠券](https://activity.huaweicloud.com/cps/recommendstore.html?fromacct=f3797f3d-4da5-4a2f-9149-130ad807c940&utm_source=dGlhbnFpeGlu=&utm_medium=cps&utm_campaign=201905)。


![](https://www.runoob.com/wp-content/uploads/2019/11/86BFA3BD-6722-48DF-BF4B-9D7C2057BCB7.jpg)

    -->

---


## 腾讯云服务器使用


本章节以腾讯云服务器为例。


**1、首先点击下图购买（更多服务器的配置信息见下文）：**


[![](https://www.runoob.com/wp-content/uploads/2019/11/ED28C34B-0BF0-4AA3-A95F-2B348B983CEC.jpeg)](https://curl.qcloud.com/tzANIP5i)


**2、登陆腾讯云控制台，查看已购买的服务器：**


![](https://www.runoob.com/wp-content/uploads/2019/11/812CFA9E-41F6-4EA2-8044-9FBCAB9C0AAE.jpg)


**3、在使用腾讯云服务器前，我们需要先创建一个 SSH 密钥，点击左侧的 **SSH 密钥** （使用密钥登录比密码更安全）：**


![](https://www.runoob.com/wp-content/uploads/2019/11/018E95B9-756E-4B6C-A0A2-CED21B42F25A.jpg)


输入密钥名称，然后点击确定，就会自动生成一个密钥，密钥会自动下载到本地，请保存好下载的密钥，密钥文件名就是你输入的密钥名称。


**4、接着我们勾选已经创建的密钥，点击 **绑定/解绑实例** 按钮，弹窗中会出现我们的 ECS 服务器，将其绑定到这个密钥即可：**


![](https://www.runoob.com/wp-content/uploads/2019/11/963AF776-FE8C-4340-A426-870D962BDC93.jpg)


**5、返回实例列表，点击实例右侧的 **登录** 按钮，弹窗中点击立即登录，这是会弹出一个新的浏览器窗口，我们选择密钥登录，密钥文件就是在第三个步骤创建的：**



![](https://www.runoob.com/wp-content/uploads/2019/11/A23D733A-DA1B-42C9-91E8-12FB84A68400.jpg)


![](https://www.runoob.com/wp-content/uploads/2019/11/7603BDAC-3103-4379-B0BE-8E669E069AF4.jpg)


![](https://www.runoob.com/wp-content/uploads/2019/11/D1D8FA9C-4ECD-42A4-B24B-70520F854858.jpg)


当然你可以选择第三方客户端登录（如：SecureCRT），用户名为 ubuntu，其他系统估计略有不同，然后导入对应的 key 即可。










	  AI 思考中...





			** [Linux groupadd 命令](https://www.runoob.com/linux-comm-groupadd.html)
			[Linux gpasswd 命令](https://www.runoob.com/linux-comm-gpasswd.html) **













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