# Markdown 列表

- Source: https://www.runoob.com/markdown/md-lists.html

Markdown 支持**有序列表**和**无序列表**。

---


## 无序列表


无序列表使用星号(*****)、加号(**+**)或是减号(**-**)作为列表标记，这些标记后面要添加一个空格，然后再填写内容：


```
* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项
- 第二项
- 第三项
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/89446A8E-6D83-4666-AACC-980145D5F070.jpg)


** 选择建议：**


- 建议统一使用减号 **-**，因为它在视觉上更清晰
- 在同一文档中保持一致的标记方式
- 标记符号后必须有一个空格


---

## 有序列表

有序列表用于展示有顺序要求的步骤或项目。


有序列表使用数字并加上 **.** 号来表示，如：


```
1. 第一项
2. 第二项
3. 第三项
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/560384BB-2B00-41D5-ACF2-18972F7F2775.jpg)


### 数字可以不连续

Markdown 会自动修正数字顺序：


```
1. 第一项
3. 第二项（实际显示为2）
7. 第三项（实际显示为3）
```


![](https://www.runoob.com/wp-content/uploads/2019/03/9f7e5c81-773d-47dd-ac64-2ab63e4b6159.png)


从指定数字开始：


```
5. 第五项
6. 第六项
7. 第七项
```


![](https://www.runoob.com/wp-content/uploads/2019/03/5fccf8c0-adb4-4afa-9375-1b822b08db2a.png)


---

## 列表嵌套


### 列表嵌套技巧


列表可以嵌套使用，创建多层次的结构：


**无序列表嵌套**：


```
- 水果
  - 苹果
    - 红苹果
    - 绿苹果
  - 香蕉
  - 橙子
- 蔬菜
  - 胡萝卜
  - 白菜
```


**有序列表嵌套**：


```
1. 准备阶段
   1. 收集资料
   2. 制定计划
2. 执行阶段
   1. 开始实施
   2. 监控进度
3. 总结阶段
```


**混合嵌套**：


```
1. 主要任务
   - 子任务A
   - 子任务B
     1. 详细步骤1
     2. 详细步骤2
   - 子任务C
2. 次要任务
```


列表混合嵌套只需在子列表中的选项前面添加两个或四个空格即可：


```
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素
```


显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2019/03/8ED795DA-F124-4E70-BA71-57CD9CF958A4.jpg)


**嵌套规则**：


- 子列表需要缩进 2-4 个空格（推荐 2 个）
- 保持一致的缩进长度
- 可以无限层嵌套，但实际使用中建议不超过 3 层


### 任务列表（复选框列表）


任务列表是 GitHub 风格 Markdown 的扩展功能，现在被广泛支持：


**基本语法**：


```
- [ ] 未完成的任务
- [x] 已完成的任务
- [ ] 另一个未完成的任务
```


渲染效果：


![](https://www.runoob.com/wp-content/uploads/2019/03/0b3d8130-90a3-4583-b052-bf480c0200bb.png)


**实际应用示例**：


```
## 项目待办清单

### 设计阶段
- [x] 需求分析
- [x] 原型设计
- [ ] UI 设计

### 开发阶段
- [ ] 前端开发
  - [x] 页面布局
  - [ ] 交互功能
  - [ ] 响应式适配
- [ ] 后端开发
  - [ ] 数据库设计
  - [ ] API 开发
  - [ ] 性能优化

### 测试阶段
- [ ] 单元测试
- [ ] 集成测试
- [ ] 用户验收测试
```


![](https://www.runoob.com/wp-content/uploads/2019/03/4d1979a3-ee29-4825-b2ba-242ebb5b80af.png)


**使用技巧**：


- 方括号内的空格和 x 很重要：`[ ]` 和 `[x]`
- 可以与嵌套列表结合使用
- 在项目管理、学习计划、生活清单中特别有用
- 某些编辑器支持点击复选框来切换状态


**高级列表技巧**：


*列表项中包含多段内容*：


```
1. 第一项

   这是第一项的详细说明，需要与列表项对齐缩进。

   还可以包含第二段内容。

2. 第二项

   > 可以在列表项中使用引用
```


![](https://www.runoob.com/wp-content/uploads/2019/03/e8b7f9c4-8525-4bf3-94b8-3fe434ec5f4e.png)


*列表项中的换行*：


```
- 这是一个很长的列表项，
  需要换行显示，注意第二行需要与第一行对齐
- 另一个列表项
```


![](https://www.runoob.com/wp-content/uploads/2019/03/e4e5200a-a545-4a7f-aed2-232d0480462f.png)


通过掌握这些基础语法，你已经能够创建结构清晰、格式规范的 Markdown 文档了。这些语法是日常写作中最常用的，熟练掌握它们将大大提高你的文档编写效率。









	  AI 思考中...





			** [Markdown 文本格式](https://www.runoob.com/md-paragraph.html)
			[Markdown 引用块](https://www.runoob.com/md-block.html) **













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