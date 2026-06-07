# Lua 数组

- Source: https://www.runoob.com/lua/lua-arrays.html

数组，就是相同数据类型的元素按一定顺序排列的集合，可以是一维数组和多维数组。


在 Lua 中，数组不是一种特定的数据类型，而是一种用来存储一组值的数据结构。

实际上，Lua 中并没有专门的数组类型，而是使用一种被称为 **"table"** 的数据结构来实现数组的功能。


Lua 数组的索引键值可以使用整数表示，数组的大小不是固定的。


在 Lua 索引值是以 **1** 为起始，但你也可以指定 0 开始。


---


## 一维数组


一维数组是最简单的数组，其逻辑结构是线性表。


使用索引访问数组元素：


## 实例


```lua
-- 创建一个数组
local myArray = {10, 20, 30, 40, 50}

-- 访问数组元素
print(myArray[1])  -- 输出 10
print(myArray[3])  -- 输出 30
```


以上代码执行输出结果为：


```
10
30
```


要计算数组的长度（即数组中元素的个数），你可以使用 **#** 操作符：


## 实例


```lua
local myArray = {10, 20, 30, 40, 50}

-- 计算数组长度
local length = #myArray

print(length) -- 输出 5
```


以上代码执行输出结果为：


```
5
```


一维数组可以用 **for** 循环出数组中的元素，如下实例：


## 实例


```lua
-- 创建一个数组
local myArray = {10, 20, 30, 40, 50}

-- 循环遍历数组
for i = 1, #myArray do
    print(myArray[i])
end
```


以上代码执行输出结果为：


```
10
20
30
40
50
```


lua 索引默认从 1 开始：


## 实例


```lua
array = {"Lua", "Tutorial"}

for i= 0, 2 do
   print(array[i])
end
```


以上代码执行输出结果为：


```
nil
Lua
Tutorial
```


正如你所看到的，我们可以使用整数索引来访问数组元素，如果指定的索引没有值则返回 **nil**。 除此外我们还可以以负数为数组索引值：


## 实例


```lua
array = {}

for i= -2, 2 do
   array[i] = i *2
end

for i = -2,2 do
   print(array[i])
end
```


以上代码执行输出结果为：


```
-4
-2
0
2
4
```


我们也可以修改数组中元素：


## 实例


```lua
-- 创建一个数组
local myArray = {10, 20, 30, 40, 50}

-- 修改数组元素
myArray[2] = 25

-- 循环遍历数组
for i = 1, #myArray do
    print(myArray[i])
end
```


以上代码执行输出结果为：


```
10
25
30
40
50
```


我们也可以向数组中添加元素：


## 实例


```lua
-- 创建一个数组
local myArray = {10, 20, 30, 40, 50}

-- 添加新元素到数组末尾
myArray[#myArray + 1] = 60

-- 循环遍历数组
for i = 1, #myArray do
    print(myArray[i])
end
```


以上代码执行输出结果为：


```
10
20
30
40
50
60
```


我们也可以删除数组中元素：


## 实例


```lua
-- 创建一个数组
local myArray = {10, 20, 30, 40, 50}

-- 删除第三个元素
table.remove(myArray, 3)

-- 循环遍历数组
for i = 1, #myArray do
    print(myArray[i])
end
```


以上代码执行输出结果为：


```
10
20
40
50
```


---


## 多维数组


多维数组即数组中包含数组或一维数组的索引键对应一个数组。


以下是一个三行三列的阵列多维数组：


## 实例


```lua
-- 初始化数组
array = {}
for i=1,3 do
   array[i] = {}
      for j=1,3 do
         array[i][j] = i*j
      end
end

-- 访问数组
for i=1,3 do
   for j=1,3 do
      print(array[i][j])
   end
end
```


以上代码执行输出结果为：


```
1
2
3
2
4
6
3
6
9
```


不同索引键的三行三列阵列多维数组：


## 实例


```lua
-- 初始化数组
array = {}
maxRows = 3
maxColumns = 3
for row=1,maxRows do
   for col=1,maxColumns do
      array[row*maxColumns +col] = row*col
   end
end

-- 访问数组
for row=1,maxRows do
   for col=1,maxColumns do
      print(array[row*maxColumns +col])
   end
end
```


以上代码执行输出结果为：


```
1
2
3
2
4
6
3
6
9
```


正如你所看到的，以上的实例中，数组设定了指定的索引值，这样可以避免出现 nil 值，有利于节省内存空间。








	  AI 思考中...





			** [Lua 字符串](https://www.runoob.com/lua-strings.html)
			[Lua 迭代器](https://www.runoob.com/lua-iterators.html) **













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