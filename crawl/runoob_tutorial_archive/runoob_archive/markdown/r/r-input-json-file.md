# R JSON 文件

- Source: https://www.runoob.com/r/r-input-json-file.html

JSON: **J**ava**S**cript **O**bject **N**otation(JavaScript 对象表示法)。


JSON 是存储和交换文本信息的语法。


JSON 类似 XML，但比 XML 更小、更快，更易解析。


如果你对 JSON 还不了解，可以先查阅：[JSON 教程](https://www.runoob.com/../json/json-tutorial.html)


R 语言读写 JSON 文件需要安装扩展包，我们可以在 R 到控制台输入以下命令来安装：


```
install.packages("rjson", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


查看是否安装成功：


```
> any(grepl("rjson",installed.packages()))
[1] TRUE
```


创建 sites.json 文件，json 文件与测试脚本同一目录下，代码如下：


## 实例



```r
{
   "id":["1","2","3"],
   "name":["Google","Runoob","Taobao"],
   "url":["www.google.com","www.runoob.com","www.taobao.com"],
   "likes":[ 111,222,333]
}
```


接下来我们可以使用 rjson 包来载入 json 文件的数据。

查看数据，某一行使用 **[ ]**, 指定的行和列使用 **[[ ]]**:


## 实例


```r
# 载入 rjson 包
library("rjson")

# 获取 json 数据
result <- fromJSON(file = "sites.json")

# 输出结果
print(result)

print("===============")

# 输出第 1 列的结果
print(result[1])

print("===============")
# 输出第 2 行第 2 列的结果
print(result[[2]][[2]])
```


执行以上代码输出结果为：


```
$id
[1] "1" "2" "3"

$name
[1] "Google" "Runoob" "Taobao"

$url
[1] "www.google.com" "www.runoob.com" "www.taobao.com"

$likes
[1] 111 222 333

[1] "==============="
$id
[1] "1" "2" "3"

[1] "==============="
[1] "Runoob"
```


我们也可以使用 **as.data.frame()** 函数将 json 文件数据可以转为数据框类型，这样我们就更方便对数据进行操作：


## 实例


```r
# 载入 rjson 包
library("rjson")

# 获取 json 数据
result <- fromJSON(file = "sites.json")

# 转为数据框
json_data_frame <- as.data.frame(result)

print(json_data_frame)
```


执行以上代码输出结果为：


```
id   name            url likes
1  1 Google www.google.com   111
2  2 Runoob www.runoob.com   222
3  3 Taobao www.taobao.com   333
```









	  AI 思考中...





			** [R XML 文件](https://www.runoob.com/r-input-xml-file.html)
			[R MySQL 连接](https://www.runoob.com/r-mysql-connect.html) **













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