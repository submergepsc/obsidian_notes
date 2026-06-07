# Python 统计一个字符串中的元音字母数量

- Source: https://www.runoob.com/python3/python-vowel-count.html

[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Python3 实例](https://www.runoob.com/python3-examples.html)


在 Python 中，我们可以通过遍历字符串中的每个字符，并检查它是否是元音字母（a, e, i, o, u）来统计字符串中元音字母的数量。以下是一个简单的示例代码。


## 实例


```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# 示例字符串
text = "Hello, World!"
print(f"元音字母的数量是: {count_vowels(text)}")
```


代码解析：


- `vowels = "aeiouAEIOU"`：定义了一个包含所有元音字母的字符串，包括大小写。
- `count = 0`：初始化一个计数器，用于记录元音字母的数量。
- `for char in s:`：遍历字符串 `s` 中的每个字符。
- `if char in vowels:`：检查当前字符是否是元音字母。
- `count += 1`：如果是元音字母，计数器加1。
- `return count`：返回最终的元音字母数量。
- `text = "Hello, World!"`：定义一个示例字符串。
- `print(f"元音字母的数量是: {count_vowels(text)}")`：调用 `count_vowels` 函数并打印结果。


输出结果：


```
元音字母的数量是: 3
```


[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Python3 实例](https://www.runoob.com/python3-examples.html)








	  AI 思考中...





			** [Python 判断一个年份是否是闰年](https://www.runoob.com/python-leap-year.html)
			[Python __name__ 与 __main__](https://www.runoob.com/python3-name-main.html) **













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