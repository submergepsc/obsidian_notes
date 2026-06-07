# QoderWork 教程

- Source: https://www.runoob.com/ai-agent/qoderwork.html

OpenClaw 虽然强大，其实还是有门槛的，要懂命令行，还得安装 node.js 等，各种配置，没技术还真不好整。

阿里出了一个桌面级 AI Agent -- QoderWork，这个就简单多了，下载后直接用，不需要懂命令行，软件内可以安装配置各种 skills。


我们只需要描述需求，QoderWork 就会自动拆解步骤、调用软件、执行并交付结果。


- **传统 AI 工具：**你问，它答，动手还得靠自己。
- **QoderWork：**你说需求，它交付结果。


  **


    **
      我们先点击访问
      [QoderWork 官网](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
      注册 QoderWork 账号
    **


      免费试用 Pro + 300 Credits




![](https://www.runoob.com/wp-content/uploads/2026/03/6c1e7ac0-4c98-4438-9c17-e8a5f15cc922.png)


注册完成后点击右上角的**下载**按钮：


![](https://www.runoob.com/wp-content/uploads/2026/01/1d73bf5c-6bb9-417c-abbf-75987b0b4459.png)


选择 **QoderWork** 选项，根据你的电脑系统，下载安装程序：


![](https://www.runoob.com/wp-content/uploads/2026/03/dde8b342-216b-4767-b27e-fa3bca287f35.png)


下载后，双击安装，安装完成界面如下：


![](https://www.runoob.com/wp-content/uploads/2026/03/e4de6860-f6a5-4f3a-9b96-8be4bf185774.png)


QoderWork 可以：


- 理解自然语言任务
- 自动规划执行步骤
- 调用本地文件和应用
- 自动完成多步骤任务

典型应用场景：


| 场景 | 说明 |
| --- | --- |
| 文件整理 | 自动识别文件类型，智能整理项目文件 |
| 照片管理 | 按时间、地点、主题自动分类整理本地照片 |
| 数据分析 | 分析数据结构，生成统计报表与可视化图表 |
| 文档创作 | 撰写报告、制作演示文稿、处理表格数据 |
| 研究整合 | 汇总多源信息，提炼关键洞察 |


比如你说一句：


```
分析这个 Excel 销售表，并生成一个 PPT 汇报。
```


QoderWork 可以自动：


- 读取 Excel
- 分析销售数据
- 生成图表
- 写分析报告
- 生成 PPT


整个流程一次完成。


我们先创建一个 QoderWork 的工作目录：


```
mkdir  qoderwork-runoob-test
```


进入该目录：

```
cd qoderwork-runoob-test
```
 我们来创建测试数据，直接复制以下内容，粘贴到记事本/文本编辑器，保存为 **sales_test.csv** 文件：


```
订单ID,商品名称,商品品类,销售单价,销售数量,销售日期,客户姓名,客户地区,销售人员,佣金比例
OD2026001,iPhone 14,电子产品,5999.00,2,2026-01-05,张三,北京,李明,0.05
OD2026002,MacBook Pro,电子产品,12999.00,1,2026-01-06,李四,上海,王红,0.08
OD2026003,耐克运动鞋,服饰鞋帽,799.00,1,2026-01-07,王五,广州,张丽,0.03
OD2026004,家用咖啡机,家居家电,1299.00,1,2026-01-08,赵六,深圳,李明,0.05
OD2026005,无线耳机,电子产品,899.00,3,2026-01-09,钱七,杭州,王红,0.08
OD2026006,羽绒服,服饰鞋帽,1599.00,1,2026-01-10,孙八,成都,张丽,0.03
OD2026007,全自动洗衣机,家居家电,3999.00,1,2026-01-11,周九,武汉,李明,0.05
OD2026008,iPad Air,电子产品,3799.00,2,2026-01-12,吴十,西安,王红,0.08
OD2026009,跑步机,运动器材,2999.00,1,2026-01-13,郑一,南京,张丽,0.03
OD2026010,智能手表,电子产品,1999.00,1,2026-01-14,王二,天津,李明,0.05
OD2026011,羊毛衫,服饰鞋帽,599.00,2,2026-01-15,李三,重庆,王红,0.08
OD2026012,空气净化器,家居家电,1899.00,1,2026-01-16,张四,青岛,张丽,0.03
OD2026013,游戏手柄,电子产品,399.00,4,2026-01-17,王五,大连,李明,0.05
OD2026014,登山包,运动器材,499.00,1,2026-01-18,赵六,厦门,王红,0.08
OD2026015,电饭煲,家居家电,899.00,2,2026-01-19,钱七,福州,张丽,0.03
OD2026016,蓝牙音箱,电子产品,599.00,3,2026-01-20,孙八,长沙,李明,0.05
OD2026017,牛仔裤,服饰鞋帽,299.00,2,2026-01-21,周九,沈阳,王红,0.08
OD2026018,微波炉,家居家电,799.00,1,2026-01-22,吴十,哈尔滨,张丽,0.03
OD2026019,健身器材套装,运动器材,1599.00,1,2026-01-23,郑一,石家庄,李明,0.05
OD2026020,平板电脑,电子产品,2799.00,1,2026-01-24,王二,太原,王红,0.08
OD2026021,运动T恤,服饰鞋帽,199.00,5,2026-01-25,李三,郑州,张丽,0.03
OD2026022,吸尘器,家居家电,1499.00,1,2026-01-26,张四,济南,李明,0.05
OD2026023,电脑显示器,电子产品,1299.00,2,2026-01-27,王五,合肥,王红,0.08
OD2026024,瑜伽垫,运动器材,199.00,3,2026-01-28,赵六,南昌,张丽,0.03
OD2026025,茶叶礼盒,食品饮品,399.00,3,2026-01-29,钱七,昆明,李明,0.05
OD2026026,皮鞋,服饰鞋帽,899.00,1,2026-01-30,孙八,兰州,王红,0.08
OD2026027,电烤箱,家居家电,699.00,1,2026-01-31,周九,银川,张丽,0.03
OD2026028,机械键盘,电子产品,499.00,2,2026-02-01,吴十,西宁,李明,0.05
OD2026029,篮球,运动器材,199.00,2,2026-02-02,郑一,乌鲁木齐,王红,0.08
OD2026030,坚果礼盒,食品饮品,299.00,6,2026-02-03,王二,拉萨,张丽,0.03
```


[下载 sales_test.csv](https://static.jyshare.com/download/sales_test.csv)


![](https://www.runoob.com/wp-content/uploads/2026/03/9495483b-1f14-4d05-9cfe-6b382a2f2a86.png)


然后打开 QoderWork，左下角的选择工作目录设置为 qoderwork-runoob-test：


![](https://www.runoob.com/wp-content/uploads/2026/03/641ceef3-f228-43c0-8ac6-3bf7dde6ed97.png)


输入内容：


```
分析该目录下的 Excel 销售表 ，并生成一个 PPT 汇报 。
```


![](https://www.runoob.com/wp-content/uploads/2026/03/9687b3d4-69d9-4b57-9237-4e427d6b98a3.png)

从上图可以看到，QoderWork 已经分析好步骤并开始执行任务了。


执行完成后 qoderwork-runoob-test 目录下会生成一个 ppt 文件，提示如下：


![](https://www.runoob.com/wp-content/uploads/2026/03/e548faaa-ca05-4253-9d44-8cd1ffe2e8bf.png)

我们可以直接打开 PPT 看下，效果不错：


![](https://www.runoob.com/wp-content/uploads/2026/03/37201abb-bc74-48ec-9bf6-61fee2430d07.png)


此外，我们可以在输入框使用 **@** 来调用专门生成 ppt 的 skills 来生成：


![](https://www.runoob.com/wp-content/uploads/2026/03/76760cd7-bac8-48c9-80c0-7626e384bbe8.png)

生成过程就会使用该 Skills：


![](https://www.runoob.com/wp-content/uploads/2026/03/0c02ff99-5e5f-4b07-a7c0-3a2dd27edc90.png)


---

## QoderWork 与其他 AI 产品区别


### 与 ChatGPT / Claude 的区别


| 类型 | ChatGPT / Claude | QoderWork |
| --- | --- | --- |
| 本质 | AI对话助手 | AI桌面执行Agent |
| 能力 | 给建议 | 直接执行任务 |
| 文件处理 | 手动上传 | 直接访问本地 |
| 自动化 | 弱 | 强 |
| 使用场景 | 写作、问答 | 实际办公工作 |


简单理解：


- ChatGPT 是大脑。
- QoderWork 是手脚。


### 与 OpenClaw / Claude Code 的关系


如果放在 **AI Agent 工具谱系**里：


| 产品 | 类型 |
| --- | --- |
| Claude Code | 编程 Agent |
| OpenClaw | 自动化 Agent |
| QoderWork | 桌面办公 Agent |


QoderWork 的定位其实是：**桌面版 AI 办公助手 + 自动化 Agent**









	  AI 思考中...





			** [CC Switch 一键切换 API](https://www.runoob.com/cc-switch.html)
			[OpenClaw Skills — ClawHub](https://www.runoob.com/openclaw-skills.html) **













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