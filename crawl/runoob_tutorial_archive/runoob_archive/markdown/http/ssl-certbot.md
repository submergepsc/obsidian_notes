# SSL 免费证书申请 - Certbot

- Source: https://www.runoob.com/http/ssl-certbot.html

我们知道使用 SSL（安全套接层）证书对于网站和在线服务来说非常重要，SSL 证书通过加密用户和服务器之间的通信，保护数据不被窃听或篡改。

本章节我们将介绍使用 Certbot 工具申请免费的 SSL 证书。


## 什么是 Certbot？

Certbot 是一个开源的自动化工具，用于获取和续订由 Let's Encrypt 提供的免费 SSL/TLS 证书。

Let's Encrypt 是一个由互联网安全研究小组（ISRG）运营的证书颁发机构（CA），它提供了一个自动化的流程来生成和更新证书，使得网站管理员可以轻松地为他们的站点启用 HTTPS 加密。


**Certbot 的主要特点包括：**


- **自动化**：它可以自动验证域名所有权，并申请证书。
- **免费**：它使用的是 Let's Encrypt 提供的免费证书。
- **兼容性**：支持多种 web 服务器，如 Apache、Nginx 等。
- **易用性**：提供了命令行界面，使得安装和使用变得简单。
- **续订**：自动处理证书的续订，确保网站的 HTTPS 连接始终保持有效。


Let's Encrypt 颁发的证书有效期为 90 天，Certbot 会自动配置证书的续期任务，确保证书不会过期。


---

## Certbot 安装


### 1. 在 Ubuntu/Debian 系统上安装 Certbot


**使用 APT 安装：**


```
sudo apt update
sudo apt install certbot
```


安装完成后，Certbot 就可以用了。


**安装 Snap 版本：**

Snap 是 Certbot 官方推荐的安装方式，尤其是针对长期支持的 Ubuntu 版本。


```
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot  # 这一步是为了确保 certbot 命令能全局使用
```


### 2. 在 CentOS/RHEL 系统上安装 Certbot


安装 EPEL 仓库（适用于 CentOS 7 及以下）：


```
sudo yum install epel-release
```


```
sudo yum install certbot
```


### 3. 在 macOS 上安装 Certbot

macOS 上可以使用 Homebrew 安装 Certbot：


```
brew install certbot
```


更多内容我们可以在 Certbot 网站 [https://certbot.eff.org/](https://certbot.eff.org/) 查看各个系统平台的安装方法：


![](https://www.runoob.com/wp-content/uploads/2024/09/Certbot-1.png)


安装完成后，使用以下命令查看 certbot 安装的版本：


```
certbot --version
```


---


## 证书申请与续签

安装好certbot 后就可以使用以下命令来申请证书了，注意 *.runoob.com 为你自己的域名，需要修改：


```
certbot certonly  -d *.runoob.com --manual --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory
```


执行以上命令后，填写信息：


```
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): [email protected]. # 这里输入你的邮箱

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.4-April-3-2024.pdf. You must agree in
order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y    # 输入 Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y       # 输入 Y

Account registered.
Requesting a certificate for *.runoob.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name:

xxxxxxx.runoob.com. # 这里需要设置域名解析，需要到域名后台填写信息，参考下图

with the following value:

aIwqY00CZtziVwr-xxxxxxxxxxxxxx  # 这里是域名解析的内容，参考下图

Before continuing, verify the TXT record has been deployed. Depending on the DNS
provider, this may take some time, from a few seconds to multiple minutes. You can
check if it has finished deploying with aid of online tools, such as the Google
Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.runoob.com.
Look for one or more bolded line(s) below the line ';ANSWER'. It should show the
value(s) you've just added.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue  # 参考下图设置完域名解析后，按回车就可以生成了，记住一定要先解析设置完成后再回车，然后生成的证书信息如下：

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/runoob.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/runoob.com/privkey.pem
This certificate expires on 2024-12-21.
These files will be updated when the certificate renews.

NEXT STEPS:
- This certificate will not be renewed automatically. Autorenewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```


设置域名解析用于验证证书：

![](https://www.runoob.com/wp-content/uploads/2024/09/certbot-2.png)


Let's Encrypt 颁发的证书有效期为 90 天，可以使用以下命令进行续签证书:


```
certbot certonly --force-renewal --manual -d '*.runoob.com' \
--preferred-challenges dns \
--server https://acme-v02.api.letsencrypt.org/directory
```


执行以上续签命令后，就会让我们更新下 DNS 解析记录：


```
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for *.jysahre.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name:

_acme-challenge.jysahre.com.

with the following value:

ckxo1wGXbP1CtNQ3ZRfvHxxxxxx          # 这里会显示你要更改的 DNS 解析记录值，设置好就可以完成更新了

Before continuing, verify the TXT record has been deployed. Depending on the DNS
provider, this may take some time, from a few seconds to multiple minutes. You can
check if it has finished deploying with aid of online tools, such as the Google
Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.jysahre.com.
Look for one or more bolded line(s) below the line ';ANSWER'. It should show the
value(s) you've just added.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```









	  AI 思考中...





			** [HTTP2](http2-tutorial.html)














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