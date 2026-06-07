# Markdown 表格

- Source: https://www.runoob.com/markdown/md-table.html

表格和引用是 Markdown 中重要的内容组织工具。

表格能够清晰地展示结构化数据，而引用则用于突出重要信息或引用他人观点。


Markdown 制作表格使用 **|** 来分隔不同的单元格，使用 **-** 来分隔表头和其他行。


语法格式如下：


```
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```


以上代码显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2019/03/23EACC50-38E0-4284-B99A-6BC22E284BAC.jpg)


**语法要点**：


- 表头和数据行之间必须有分隔线
- 分隔线至少需要三个连字符 `**---**`
- 两端的竖线 `**|**` 是可选的，但建议保留以提高可读性
- 不需要严格对齐，但对齐后更美观


### 对齐方式


**我们可以设置表格的对齐方式：**


- **---:** 设置内容和标题栏居右对齐。
- **:---** 设置内容和标题栏居左对齐。
- **:---:** 设置内容和标题栏居中对齐。


实例如下：


```
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```


以上代码显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2019/03/87DE9D5C-44FB-4693-8735-194D3779EC3E.jpg)


### 复杂表格的处理技巧


#### 元格内容格式化


表格单元格内可以使用大部分 Markdown 语法：


```
| 功能 | 描述 | 状态 |
|------|------|:----:|
| **用户登录** | 支持邮箱和手机号登录 | &#x2705; |
| *密码重置* | 通过邮箱重置密码 | &#x26a0;&#xfe0f; |
| `API接口` | RESTful API 设计 | &#x2705; |
| [文档链接](https://example.com) | 查看详细文档 | &#x1f4d6; |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/c5c7b85b-e5fb-4426-96e8-104231224b1a.png)


### 处理长文本


当单元格内容较长时，可以使用以下技巧：


**换行处理**：


```
| 项目 | 详细说明 |
|------|----------|
| 需求分析 | 1. 收集用户需求<br>2. 分析业务场景<br>3. 确定功能范围 |
| 技术选型 | 前端：React + TypeScript<br>后端：Node.js + Express<br>数据库：MongoDB |
```


** 缩写和链接：**


```
| 技术栈 | 说明 | 官网 |
|--------|------|------|
| React | 用户界面库 | [链接](https://reactjs.org) |
| Vue.js | 渐进式框架 | [链接](https://vuejs.org) |
| Angular | 完整的框架 | [链接](https://angular.io) |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/f04d169a-84f7-4980-92e8-0057517f4f41.png)


### 表格中的特殊字符

某些字符在表格中有特殊含义，需要转义：


```
| 字符 | 转义方法 | 示例 |
|------|----------|------|
| 竖线 | `\|` | 显示 \| 符号 |
| 反斜杠 | `\\` | 显示 \\ 符号 |
| HTML | 直接使用 | <code>&lt;div&gt;</code> |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/4480f673-d6c2-4c2f-b5db-82e3b23c8133.png)


### 表格美化建议

**使用 Emoji 和符号**


```
| 状态 | 图标 | 说明 |
|:----:|:----:|------|
| 完成 | &#x2705; | 任务已完成 |
| 进行中 | &#x1f504; | 正在处理 |
| 待处理 | &#x23f3; | 等待开始 |
| 错误 | &#x274c; | 出现问题 |
| 警告 | &#x26a0;&#xfe0f; | 需要注意 |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/16b0568b-2f52-41da-9663-31d11e74ddd0.png)


### 数据表格最佳实践


财务数据表格：


```
| 月份 | 收入 | 支出 | 利润 | 增长率 |
|:----:|-----:|-----:|-----:|-------:|
| 1月 | ¥50,000 | ¥35,000 | ¥15,000 | - |
| 2月 | ¥55,000 | ¥38,000 | ¥17,000 | +13.3% |
| 3月 | ¥62,000 | ¥42,000 | ¥20,000 | +17.6% |
| **总计** | **¥167,000** | **¥115,000** | **¥52,000** | **+31.1%** |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/8270f992-60e7-4673-a2e7-66667d32b34e.png)


技术对比表格：


```
| 特性 | React | Vue.js | Angular | 评分 |
|------|:-----:|:------:|:-------:|:----:|
| 学习曲线 | 中等 | 简单 | 复杂 | Vue &#x2b50;&#x2b50;&#x2b50; |
| 性能表现 | 优秀 | 优秀 | 良好 | 平分 &#x2b50;&#x2b50;&#x2b50; |
| 生态系统 | 丰富 | 成长中 | 完整 | React &#x2b50;&#x2b50;&#x2b50; |
| 企业支持 | Facebook | 社区 | Google | Angular &#x2b50;&#x2b50;&#x2b50; |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/4fa5c968-fba0-4ab2-a769-c883f02ea04b.png)


### 响应式表格处理

对于复杂表格，可以考虑分解为多个简单表格。

移动端友好的设计：


```
### 基本信息
| 项目 | 值 |
|------|-----|
| 姓名 | 张三 |
| 年龄 | 25 |
| 职业 | 工程师 |

### 联系方式
| 类型 | 信息 |
|------|------|
| 邮箱 | [email protected] |
| 电话 | 138-0013-8000 |
| 地址 | 北京市朝阳区 |
```


![](https://www.runoob.com/wp-content/uploads/2019/03/def8568b-81da-4ff9-8868-057bd975d831.png)








	  AI 思考中...





			** [Markdown 图片](https://www.runoob.com/md-image.html)
			[Markdown 高级技巧](https://www.runoob.com/md-advance.html) **













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