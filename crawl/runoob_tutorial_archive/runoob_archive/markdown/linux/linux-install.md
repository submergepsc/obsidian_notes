# Linux 安装

- Source: https://www.runoob.com/linux/linux-install.html

本章节我们将为大家介绍 Linux 的安装，安装步骤比较繁琐，现在其实云服务器挺普遍的，价格也便宜，如果自己不想搭建，也可以配置一个，参考 [Linux 云服务器](https://www.runoob.com/linux-cloud-server.html)。


本章节以 centos6.4 为例。


centos 下载地址：


可以去官网下载最新版本：[https://www.centos.org/download/](https://www.centos.org/download/)


![](https://www.runoob.com/wp-content/uploads/2017/06/1497342019-2668-2a90-3944-9027-0352de39b1fe.jpg)


以下针对各个版本的ISO镜像文件，进行一一说明：


- **CentOS-7.0-x86_64-DVD-1503-01.iso **: 标准安装版，一般下载这个就可以了（推荐）
- **CentOS-7.0-x86_64-NetInstall-1503-01.iso **: 网络安装镜像（从网络安装或者救援系统）
- **CentOS-7.0-x86_64-Everything-1503-01.iso**: 对完整版安装盘的软件进行补充，集成所有软件。（包含centos7的一套完整的软件包，可以用来安装系统或者填充本地镜像）
- **CentOS-7.0-x86_64-GnomeLive-1503-01.iso**: GNOME桌面版
- **CentOS-7.0-x86_64-KdeLive-1503-01.iso**: KDE桌面版
- **CentOS-7.0-x86_64-livecd-1503-01.iso **: 光盘上运行的系统，类拟于winpe


**
注：**建议安装64位Linux系统。


旧版本下载地址：[https://wiki.centos.org/Download](https://wiki.centos.org/Download)


接下来你需要将下载的Linux系统刻录成光盘或U盘。


**注：**你也可以在Window上安装VMware虚拟机来安装Linux系统。


---


## Linux 安装步骤


1、首先，使用光驱或U盘或你下载的Linux ISO文件进行安装。


界面说明：


![image001](https://www.runoob.com/wp-content/uploads/2014/06/image001.png)


Install or upgrade an existing system 安装或升级现有的系统


install system with basic video driver 安装过程中采用基本的显卡驱动


Rescue installed system 进入系统修复模式


Boot from local drive 退出安装从硬盘启动


Memory test 内存检测


注：用联想E49安装时选择第一项安装时会出现屏幕显示异常的问题，后改用第二项安装时就没有出现问题


2、这时直接"skip"就可以了


![image002](https://www.runoob.com/wp-content/uploads/2014/06/image002.png)


3、出现引导界面，点击"next"


![image003](https://www.runoob.com/wp-content/uploads/2014/06/image003.png)


4、选中"English（English）"否则会有部分乱码问题


![image004](https://www.runoob.com/wp-content/uploads/2014/06/image004.png)


5、键盘布局选择"U.S.English"


![image005](https://www.runoob.com/wp-content/uploads/2014/06/image005.png)


6、选择"Basic Storage Devices"点击"Next"


![image006](https://www.runoob.com/wp-content/uploads/2014/06/image006.png)


7、询问是否忽略所有数据，新电脑安装系统选择"Yes,discard any data"


![image007](https://www.runoob.com/wp-content/uploads/2014/06/image007.png)


8、Hostname填写格式"英文名.姓"


![image008](https://www.runoob.com/wp-content/uploads/2014/06/image008.png)


9、网络设置安装图示顺序点击就可以了


![image009](https://www.runoob.com/wp-content/uploads/2014/06/image009.png)


10、时区可以在地图上点击，选择"shanghai"并取消System clock uses UTC前面的对勾


![image010](https://www.runoob.com/wp-content/uploads/2014/06/image010.png)


11、设置root的密码


![image011](https://www.runoob.com/wp-content/uploads/2014/06/image011.png)


12、硬盘分区，一定要按照图示点选


![image012](https://www.runoob.com/wp-content/uploads/2014/06/image012.png)


13、调整分区，必须要有/home这个分区，如果没有这个分区，安装部分软件会出现不能安装的问题


![image013](https://www.runoob.com/wp-content/uploads/2014/06/image013.png)


14、询问是否格式化分区


![image014](https://www.runoob.com/wp-content/uploads/2014/06/image014.png)


15、将更改写入到硬盘


![image015](https://www.runoob.com/wp-content/uploads/2014/06/image015.png)


16、引导程序安装位置


![image016](https://www.runoob.com/wp-content/uploads/2014/06/image016.png)


17、最重要的一步，也是本教程最关键的一步，也是其他教程没有提及的一步，按图示顺序点击


![image017](https://www.runoob.com/wp-content/uploads/2014/06/image017.png)


18、取消以下内容的所有选项


**Applications**


**Base System**


**Servers**


并对Desktops进行如下设置


即取消如下选项：


**Desktop Debugging and Performance Tools**


**Desktop Platform**


**Remote Desktop Clients**


**Input Methods****中仅保留ibus-pinyin-1.3.8-1.el6.x86_64,其他的全部取消**


![image018](https://www.runoob.com/wp-content/uploads/2014/06/image018.png)


![image019](https://www.runoob.com/wp-content/uploads/2014/06/image019.png)


19、选中Languages，并选中右侧的Chinese Support然后点击红色区域


![image020](https://www.runoob.com/wp-content/uploads/2014/06/image020.png)


20、调整完成后如下图所示


![image021](https://www.runoob.com/wp-content/uploads/2014/06/image021.png)


21、至此，一个最精简的桌面环境就设置完成了，


![image022](https://www.runoob.com/wp-content/uploads/2014/06/image022.png)


22、安装完成，重启


![image023](https://www.runoob.com/wp-content/uploads/2014/06/image023.png)


23、重启之后，的License Information


![image024](https://www.runoob.com/wp-content/uploads/2014/06/image024.png)


24、Create User


Username：填写您的英文名（不带.姓）


Full Name：填写您的英文名.姓（首字母大写）


![image025](https://www.runoob.com/wp-content/uploads/2014/06/image025.png)


25、"Date and Time" 选中 "Synchronize data and time over the network"


Finsh之后系统将重启


![image026](https://www.runoob.com/wp-content/uploads/2014/06/image026.png)


26、第一次登录，登录前不要做任何更改，这个很重要！！！登录之后紧接着退出


第二次登录，选择语言，在红色区域选择下拉小三角，选other，选中"汉语（中国）"


![image027](https://www.runoob.com/wp-content/uploads/2014/06/image027.png)


![image028](https://www.runoob.com/wp-content/uploads/2014/06/image028.png)


27、登录之后，请一定按照如下顺序点击！


至此，CentOS安装完成，如有其他问题，请随时与我联系！！


![image029](https://www.runoob.com/wp-content/uploads/2014/06/image029.png)


**

如果你使用的是 VMware，可以参考：[VMware 安装 Centos7](https://www.runoob.com/w3cnote/vmware-install-centos7.html) AI 思考中... ** [Linux 简介](https://www.runoob.com/linux-intro.html) [Linux 系统启动过程](https://www.runoob.com/linux-system-boot.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！



[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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