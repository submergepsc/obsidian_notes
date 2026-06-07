# Markdown 图片

- Source: https://www.runoob.com/markdown/md-image.html

图片能让文档更加生动和易于理解。

Markdown 的图片语法简洁而灵活。


Markdown 图片语法格式如下：


```
![替代文字](图片路径)
![替代文字](图片路径 "图片标题")
```


- 开头一个感叹号 !
- 接着一个方括号，里面放上图片的替代文字
- 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上选择性的 'title' 属性的文字。


**相对路径示例：**


```
![项目截图](./images/screenshot.png)
![用户界面](../assets/ui-demo.jpg "用户界面演示")
![图标](images/icon.svg "应用图标")
```


**绝对路径示例：**


```
![本地图片](/Users/username/Documents/image.png)
![系统截图](C:\Users\username\Pictures\screenshot.png)
```


**路径使用建议：**


- 推荐使用相对路径，便于项目移植
- 建议创建专门的图片文件夹（如 images/、assets/）
- 使用有意义的文件名，便于管理
- 注意路径分隔符在不同操作系统中的差异


直接引用网络图片：


```
![RUNOOB 图标](https://static.jyshare.com/images/runoob-logo.png)

![RUNOOB 图标](https://static.jyshare.com/images/runoob-logo.png "RUNOOB")
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/A042DF30-C232-46F3-8436-7D6C35351BBD.jpg)


当然，你也可以像网址那样对图片网址使用变量:


```
这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾为变量赋值（网址）

[1]: https://static.jyshare.com/images/runoob-logo.png
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/75AA6EBF-CC57-44A6-A585-5EE3DD94E42A.jpg)


Markdown 还没有办法指定图片的高度与宽度，如果你需要的话，你可以使用普通的  标签。


```
<img src="https://static.jyshare.com/images/runoob-logo.png" width="50%">
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/55F2A67D-F4BD-4960-AC55-DC690A415878.jpg)


**使用 CDN 服务：**


```
![示例图片](https://cdn.jsdelivr.net/gh/user/repo/image.png)
![Unsplash 图片](https://images.unsplash.com/photo-1506905925346-21bda4d32df4)
```


网络图片注意事项：


- 确保图片 URL 的稳定性和可访问性
- 注意图片的版权问题
- 考虑加载速度和网络环境
- 建议本地备份重要图片


### 图片 alt 文本的重要性

Alt 文本（替代文字）在图片无法显示时提供替代信息，同时对无障碍访问和 SEO 很重要：


**好的 alt 文本示例：**


```
![苹果公司总部大楼外观，现代玻璃幕墙建筑](./images/apple-headquarters.jpg)
![网站流量统计图表，显示过去六个月的访问量呈上升趋势](./charts/traffic-stats.png)
![用户登录界面，包含用户名和密码输入框](./screenshots/login-page.png)
```


**避免的 alt 文本：**


```
![图片](image.jpg)  // 太简单，没有描述性
![](image.jpg)      // 完全没有 alt 文本
![点击这里](image.jpg)  // 不描述图片内容
```


**alt 文本最佳实践：**


- 简洁但有描述性
- 描述图片的主要内容和用途
- 避免使用"图片"、"照片"等冗余词汇
- 对于装饰性图片，可以使用空的 alt 文本
- 考虑上下文，提供有意义的信息


---


## 图片尺寸控制（HTML方式）

标准 Markdown 不支持直接控制图片尺寸，但可以使用 HTML 标签。


**使用 HTML img 标签：**


```
<img src="image.jpg" alt="描述文字" width="300" height="200">
<img src="image.jpg" alt="描述文字" width="50%">
<img src="image.jpg" alt="描述文字" style="width: 300px; height: auto;">
```


**响应式图片：**


```
<img src="image.jpg" alt="描述文字" style="max-width: 100%; height: auto;">
```


**图片对齐：**


```
<!-- 居中对齐 -->
<div align="center">
  <img src="image.jpg" alt="居中图片" width="400">
</div>

<!-- 左对齐（默认） -->
<img src="image.jpg" alt="左对齐图片" style="float: left; margin-right: 20px;">

<!-- 右对齐 -->
<img src="image.jpg" alt="右对齐图片" style="float: right; margin-left: 20px;">
```


---


## 链接和图片的高级用法


### 图片链接组合

将图片作为链接的可点击元素。


基本语法：


```
[![图片alt文本](图片URL)](链接URL)
```


实际示例：


```
[![GitHub项目截图](./images/project-screenshot.png)](https://github.com/username/project)
[![访问官网](https://example.com/logo.png)](https://example.com "点击访问官网")
```


**常见应用场景：**


```
<!-- 项目徽章 -->
[![Build Status](https://travis-ci.org/user/repo.svg?branch=master)](https://travis-ci.org/user/repo)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<!-- 应用商店下载 -->
[![App Store](./images/app-store-badge.png)](https://apps.apple.com/app/your-app)
[![Google Play](./images/google-play-badge.png)](https://play.google.com/store/apps/details?id=com.yourapp)
```


### 相对路径与绝对路径

相对路径的优势：


```
<!-- 项目结构 -->
project/
├── README.md
├── docs/
│   ├── guide.md
│   └── images/
│       └── screenshot.png
└── assets/
    └── logo.png

<!-- 在 README.md 中 -->
![Logo](./assets/logo.png)

<!-- 在 docs/guide.md 中 -->
![Screenshot](./images/screenshot.png)
![Logo](../assets/logo.png)
```


路径规划建议：


- 在项目根目录创建统一的资源文件夹
- 使用描述性的文件夹名称
- 保持路径结构的一致性
- 考虑静态网站生成器的路径规则


### 图片居中和对齐

**方法一：HTML + CSS**


```
<div style="text-align: center;">
  <img src="image.jpg" alt="居中图片" style="max-width: 100%;">
</div>
```


** 方法二：使用 HTML 对齐属性**


```
<p align="center">
  <img src="image.jpg" alt="居中图片" width="400">
</p>
```


** 方法三：创建图片画廊**


```
<div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
  <img src="image1.jpg" alt="图片1" style="width: 30%; margin: 10px;">
  <img src="image2.jpg" alt="图片2" style="width: 30%; margin: 10px;">
  <img src="image3.jpg" alt="图片3" style="width: 30%; margin: 10px;">
</div>
```


实用的图片展示模板：


```
## 产品展示

### 主要功能
<table>
  <tr>
    <td align="center">
      <img src="./images/feature1.png" width="200" alt="功能1">
      <br>
      <strong>智能识别</strong>
      <br>
      <sub>AI驱动的图像识别技术</sub>
    </td>
    <td align="center">
      <img src="./images/feature2.png" width="200" alt="功能2">
      <br>
      <strong>快速处理</strong>
      <br>
      <sub>毫秒级响应速度</sub>
    </td>
  </tr>
</table>

### 界面预览
| 移动端 | 桌面端 |
|:---:|:---:|
| ![移动界面](./images/mobile.png) | ![桌面界面](./images/desktop.png) |
| 响应式设计，完美适配 | 大屏体验，功能齐全 |
```


**性能优化建议：**


- 优化图片大小和格式（WebP > PNG > JPG）
- 使用适当的图片尺寸，避免在网页中缩放大图
- 考虑使用图片压缩工具
- 为不同设备准备不同尺寸的图片


### 链接和图片的故障排除

**常见问题及解决方案：**


- 链接无法点击：检查语法格式，确保方括号和圆括号正确配对
- 图片无法显示：验证图片路径和文件存在性
- 图片过大：使用 HTML 控制尺寸或优化图片文件
- 链接在新窗口打开：使用 HTML **** 标签


**调试技巧：**


```
<!-- 测试链接是否有效 -->
测试链接：[点击测试](https://httpbin.org/get)

<!-- 测试图片路径 -->
![测试图片](./images/test.png)
<!-- 如果不显示，尝试绝对路径或检查文件名大小写 -->
```


通过掌握链接和图片的各种用法，你可以创建内容丰富、导航清晰的 Markdown 文档。这些技能对于编写技术文档、项目说明和在线内容都非常重要。








	  AI 思考中...





			** [Markdown 链接](https://www.runoob.com/md-link.html)
			[Markdown 表格](https://www.runoob.com/md-table.html) **













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