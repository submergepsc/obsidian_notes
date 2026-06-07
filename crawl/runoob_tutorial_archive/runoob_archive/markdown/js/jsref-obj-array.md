# JavaScript Array 对象

- Source: https://www.runoob.com/js/jsref-obj-array.html

---


JavaScript 中的 Array 对象是用于存储多个值的特殊类型的对象。


Array 是按顺序存储元素的，可以根据索引（从 0 开始）来访问它们。


## 创建数组


可以通过几种方式创建数组：


使用 Array 构造函数：


```
let arr1 = new Array(3);  // 创建一个长度为 3 的空数组
let arr2 = new Array(1, 2, 3);  // 创建一个包含 1, 2, 3 的数组
```


使用字面量（推荐）：


```
let arr = [1, 2, 3];  // 创建一个包含 1, 2, 3 的数组
```


第一个数组元素的索引值为 0，第二个索引值为 1，以此类推。


更多有关 JavaScript Array 内容请参考 [JavaScript Array 对象](https://www.runoob.com/js-obj-array.html)。


---


## 数组属性


| 属性 | 描述 |
| --- | --- |
| constructor | 返回创建数组对象的原型函数。 |
| length | 设置或返回数组元素的个数。 |
| prototype | 允许你向数组对象添加属性或方法。 |


---


## Array 对象方法


| 方法 | 描述 |
| --- | --- |
| [...] | 创建一个新数组。 |
| concat() | 连接两个或更多的数组，并返回结果。 |
| copyWithin() | 从数组的指定位置拷贝元素到数组的另一个指定位置中。 |
| entries() | 返回数组的可迭代对象。 |
| every() | 检测数值元素的每个元素是否都符合条件。 |
| fill() | 使用一个固定值来填充数组。 |
| filter() | 检测数值元素，并返回符合条件所有元素的数组。 |
| find() | 返回符合传入测试（函数）条件的数组元素。 |
| findIndex() | 返回符合传入测试（函数）条件的数组元素索引。 |
| forEach() | 数组每个元素都执行一次回调函数。 |
| from() | 通过给定的对象中创建一个数组。 |
| fromAsync() | 从异步可迭代对象、可迭代对象或类数组对象创建一个新的数组。 |
| includes() | 判断一个数组是否包含一个指定的值。 |
| indexOf() | 搜索数组中的元素，并返回它所在的位置。 |
| isArray() | 判断对象是否为数组。 |
| join() | 把数组的所有元素放入一个字符串。 |
| keys() | 返回数组的可迭代对象，包含原始数组的键(key)。 |
| map() | 通过指定函数处理数组的每个元素，并返回处理后的数组。 |
| pop() | 删除数组的最后一个元素并返回删除的元素。 |
| push() | 向数组的末尾添加一个或更多元素，并返回新的长度。 |
| reduce() | 将数组元素计算为一个值（从左到右）。 |
| reduceRight() | 将数组元素计算为一个值（从右到左）。 |
| reverse() | 反转数组的元素顺序。 |
| shift() | 删除并返回数组的第一个元素。 |
| slice() | 选取数组的一部分，并返回一个新数组。 |
| some() | 检测数组元素中是否有元素符合指定条件。 |
| sort() | 对数组的元素进行排序。 |
| splice() | 从数组中添加或删除元素。 |
| toString() | 把数组转换为字符串，并返回结果。 |
| toLocaleString() | 根据当前环境的语言设置（locale）来格式化数组中的每个元素。 |
| unshift() | 向数组的开头添加一个或更多元素，并返回新的长度。 |
| valueOf() | 返回数组对象的原始值。 |
| Array.of() | 将一组值转换为数组。 |
| Array.at() | 用于接收一个整数值并返回该索引对应的元素，允许正数和负数。负整数从数组中的最后一个元素开始倒数。 |
| Array.flat() | 创建一个新数组，这个新数组由原数组中的每个元素都调用一次提供的函数后的返回值组成。 |
| Array.flatMap() | 使用映射函数映射每个元素，然后将结果压缩成一个新数组。 |
| Array.with() | 更新数组元素。 |
| Array.findLastIndex() | 对数组中的每个元素执行一个函数。 |
| Array.lastIndexOf() | 对数组中的每个元素执行一个函数。 |
| Array.findLast() | 对数组中的每个元素执行一个函数。 |
| Array.toReversed() | 反转数组中元素的顺序。 |
| Array.toSorted() | 对数组中的元素按字母顺序进行排序。 |
| Array.toSpliced() | 向数组中添加和/或移除元素。 |
| [Symbol.iterator]() | 返回一个数组迭代器对象，该对象会产生数组中每个索引的值。 |








	  AI 思考中...





			** [JavaScript concat() 方法](https://www.runoob.com/../jsref/jsref-concat-array.html)
			[JavaScript Boolean constructor 属性](https://www.runoob.com/../jsref/jsref-constructor-boolean.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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