# Markdown 代码

- Source: https://www.runoob.com/markdown/md-code.html

Markdown 提供了多种方式来展示代码，从简单的行内代码到复杂的代码块，满足不同场景下的代码展示需求。

---


## 行内代码


如果是段落上的一个函数或片段的代码可以用反引号把它包起来（**`**），例如：


```
`printf()` 函数
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/C928FDA3-E0A7-4AFF-AB2A-B3AF44F93DF9.jpg)


**常见用法示例：**


- 函数名：使用 `console.log()` 输出信息
- 变量名：将值赋给 `userName` 变量
- 命令行：运行 `npm install` 安装依赖
- 键盘按键：按 `Ctrl+C` 复制内容
- 文件名：编辑 `index.html` 文件


![](https://www.runoob.com/wp-content/uploads/2019/03/ea6411ee-963b-4878-a357-2a0f5a296c0f.png)


### 特殊字符转义

当需要在行内代码中显示反引号或其他特殊字符时，需要进行转义处理。


显示反引号的方法：

** 使用双反引号包围单反引号：**


```
``使用 `反引号` 包围代码``
```


渲染效果：


![](https://www.runoob.com/wp-content/uploads/2019/03/3ce97b07-7191-4aba-8778-3f2e09dfea80.png)


**使用多个反引号包围：**


```
```包含 `` 双反引号的代码```
```


渲染效果：


![](https://www.runoob.com/wp-content/uploads/2019/03/8fbadd85-e959-4afb-8e60-865b6d77f945.png)


**其他特殊字符处理：**


- HTML 标签：`` 元素
- 数学符号：计算 `x + y = z`
- 特殊符号：使用 ` ` 表示空格


---


## 代码区块


### 缩进式代码块


代码区块使用 **4 个空格**或者一个**制表符（Tab 键）**。


语法格式：


```
正常文本段落

    这是缩进式代码块
    每行前面有四个空格
    保持代码的原始格式

继续正常文本
```


![](https://www.runoob.com/wp-content/uploads/2019/03/4f10cc30-1ff6-4970-89ae-b7133bf274eb.png)


实例如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/55EDFE05-5F27-458E-AFE0-7B96685C9603.jpg)


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/6DC89E5C-B41A-4938-97D8-D7D06B879F91.jpg)


### 三反引号代码块


你也可以用 **```** 包裹一段代码，并指定一种语言（也可以不指定）：


```
```
多行代码内容
可以包含空行
保持原有缩进
```
```


![](https://www.runoob.com/wp-content/uploads/2019/03/d680c492-f0c1-47e8-9835-b12fcbab3238.png)


三反引号（**```**）是最常用的代码块语法，支持语法高亮和多行代码展示。


```
```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/88F52386-2F98-4D7E-8935-E43BECA6D868.jpg)


**注意事项：**


- 缩进式代码块前后需要空行分隔
- 所有代码行必须保持一致的缩进
- 不支持语法高亮
- 在列表中使用时需要8个空格缩进


### 语言标识和语法高亮


在三反引号后添加语言标识符可以启用语法高亮功能。


**常用语言标识符列表：**


- `javascript` / `js` - JavaScript
- `python` / `py` - Python
- `html` - HTML
- `css` - CSS
- `sql` - SQL
- `json` - JSON
- `xml` - XML
- `yaml` / `yml` - YAML
- `bash` / `shell` - Shell脚本
- `java` - Java
- `cpp` / `c++` - C++
- `csharp` / `c#` - C#
- `php` - PHP
- `ruby` / `rb` - Ruby
- `go` - Go语言
- `rust` - Rust
- `typescript` / `ts` - TypeScript


**JavaScript:**


```
```javascript
const users = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 }
];

const adults = users.filter(user => user.age >= 18);
console.log(adults);
```
```


**Python:**


```
```python
def calculate_area(radius):
    """计算圆的面积"""
    import math
    return math.pi * radius ** 2

# 使用函数
area = calculate_area(5)
print(f"圆的面积是: {area:.2f}")
```
```


**SQL:**


```
```sql
SELECT u.name, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.name, u.email
ORDER BY order_count DESC
LIMIT 10;
```
```


![](https://www.runoob.com/wp-content/uploads/2019/03/e819b3a7-4406-45b4-8772-c67bbe422bd0-1.png)


---


## 代码块的高级特性


### 行号显示

某些 Markdown 渲染器支持显示行号，通过特定的语法或配置实现。

**语法示例（部分支持）：**


```
```javascript {.line-numbers}
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(10));
```
```


![](https://www.runoob.com/wp-content/uploads/2019/03/813e23c9-7923-47cd-b6a6-a1536a55da67.png)


或者使用：


```
```javascript showLineNumbers
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);
const sum = doubled.reduce((a, b) => a + b, 0);
console.log(`总和: ${sum}`);
```
```


### 代码差异对比

用于显示代码的添加、删除或修改，常用于展示版本控制中的变更。


**Diff 语法：**


```
```diff
function calculateTotal(items) {
-   let total = 0;
+   let total = 0.0;

    for (let item of items) {
-       total += item.price;
+       total += parseFloat(item.price);
    }

+   // 保留两位小数
+   total = Math.round(total * 100) / 100;
    return total;
}
```
```


![](https://www.runoob.com/wp-content/uploads/2019/03/653e1bce-e2d7-4c8b-8329-7b5ecfef3807.png)


**Git 风格的差异显示：**


```
```diff
@@ -1,5 +1,8 @@
 function greetUser(name) {
-    console.log("Hello " + name);
+    if (!name) {
+        throw new Error("Name is required");
+    }
+    console.log(`Hello, ${name}!`);
 }
```
```


**语言特定的差异对比：**


```
```javascript
// 之前的代码
const oldFunction = () => {
    var x = 10;  // &#x274c; 使用 var
    console.log("Value: " + x);  // &#x274c; 字符串拼接
}

// 改进后的代码
const newFunction = () => {
    const x = 10;  // &#x2705; 使用 const
    console.log(`Value: ${x}`);  // &#x2705; 模板字符串
}
```
```


![](https://www.runoob.com/wp-content/uploads/2019/03/3ba07b77-1570-48b8-86dd-a041a52ece21.png)








	  AI 思考中...





			** [Markdown 引用块](https://www.runoob.com/md-block.html)
			[Markdown 链接](https://www.runoob.com/md-link.html) **













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