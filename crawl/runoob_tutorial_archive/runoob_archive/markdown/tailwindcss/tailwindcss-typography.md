# Tailwind CSS 排版

- Source: https://www.runoob.com/tailwindcss/tailwindcss-typography.html

Tailwind CSS 的 **Typography**（排版）功能是一组实用工具，帮助开发者高效地设计文本样式。它包括设置字体、字重、行高、字距、文本对齐等基本排版属性，同时还支持复杂的排版需求，如响应式字体大小、文本阴影、文本装饰等。


### 1. 字体（Font Family）


Tailwind 提供了一些工具类来设置字体系列（font-family），可以通过类名轻松应用。


#### 常用工具类：


- `font-sans`: 设置无衬线字体。
- `font-serif`: 设置衬线字体。
- `font-mono`: 设置等宽字体。


## 实例


```css
<p class="font-sans ...">测试文本内容 ...</p>
<p class="font-serif ...">测试文本内容 ...</p>
<p class="font-mono ...">测试文本内容 ...</p>
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)


### 2. 字体大小（Font Size）


字体大小可以通过 Tailwind 的 `text-*` 工具类进行控制，支持从 `text-xs` 到 `text-9xl` 的多种大小，甚至可以自定义字体大小。


#### 常用工具类：


- `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`, ..., `text-9xl`


## 实例


```css
<p class="text-sm ...">测试文本内容 ...</p>
<p class="text-base ...">测试文本内容 ...</p>
<p class="text-lg ...">测试文本内容 ...</p>
<p class="text-xl ...">测试文本内容 ...</p>
<p class="text-2xl ...">测试文本内容 ...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 3. 字体粗细（Font Weight）


字体粗细可以通过 `font-*` 工具类来控制，Tailwind 提供了从 `font-thin` 到 `font-black` 的多种粗细选项。


#### 常用工具类：


- `font-thin`: 超细字体
- `font-light`: 轻字体
- `font-normal`: 普通字体
- `font-medium`: 中等粗细字体
- `font-semibold`: 半粗字体
- `font-bold`: 粗体
- `font-extrabold`: 更粗字体
- `font-black`: 极粗字体


## 实例


```css
<p class="font-light ...">测试文本内容 ...</p>
<p class="font-normal ...">测试文本内容 ...</p>
<p class="font-medium ...">测试文本内容 ...</p>
<p class="font-semibold ...">测试文本内容 ...</p>
<p class="font-bold ...">测试文本内容 ...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 4. 行高（Line Height）


行高（即行间距）可以通过 `leading-*` 工具类来控制。Tailwind 提供了多种行高选项，从 `leading-none` 到 `leading-loose`，可以根据需要调整。


#### 常用工具类：


- `leading-none`: 行高为 1
- `leading-tight`: 紧凑行高
- `leading-snug`: 稍微紧凑行高
- `leading-normal`: 默认行高
- `leading-relaxed`: 放松行高
- `leading-loose`: 松散行高


## 实例


```css
<p class="leading-normal ...">So I started to walk into the water...</p>
<p class="leading-relaxed ...">So I started to walk into the water...</p>
<p class="leading-loose ...">So I started to walk into the water...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)


### 5. 字间距（Letter Spacing）


字间距可以通过 `tracking-*` 工具类来控制。常用的字间距选项包括 `tracking-tight`、`tracking-normal` 和 `tracking-wide`，用于调整字母之间的空隙。


#### 常用工具类：


- `tracking-tight`: 紧凑字间距
- `tracking-normal`: 默认字间距
- `tracking-wide`: 宽字间距
- `tracking-wider`: 更宽字间距
- `tracking-wide`: 极宽字间距


## 实例


```css
<p class="tracking-tight ...">测试文本内容 ...</p>
<p class="tracking-normal ...">测试文本内容 ...</p>
<p class="tracking-wide ...">测试文本内容 ...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)


### 6. 文本颜色（Text Color）


Tailwind 提供了多种文本颜色类，允许你为文本设置不同的颜色。你可以使用 `text-*` 工具类来设置颜色。


#### 常用工具类：


- `text-gray-500`: 中等灰色
- `text-red-500`: 红色
- `text-blue-500`: 蓝色
- `text-green-500`: 绿色


## 实例


```css
<p class="text-sky-400/100">测试文本内容...</p>
<p class="text-sky-400/75">测试文本内容...</p>
<p class="text-sky-400/50">测试文本内容...</p>
<p class="text-sky-400/25">测试文本内容...</p>
<p class="text-sky-400/0">测试文本内容...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 7. 文本对齐（Text Alignment）


Tailwind 提供了简单的工具类来控制文本对齐方式。你可以使用 `text-left`、`text-center` 或 `text-right` 来设置文本的对齐方式。


#### 常用工具类：


- `text-left`: 左对齐
- `text-center`: 居中对齐
- `text-right`: 右对齐


## 实例


```css
<p class="text-left">这是左对齐的文本</p>
<p class="text-center">这是居中对齐的文本</p>
<p class="text-right">这是右对齐的文本</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 8. 文本修饰（Text Decoration）


你可以使用 `underline`, `line-through` 和 `no-underline` 来控制文本的下划线和删除线。


#### 常用工具类：


- `underline`: 添加下划线
- `line-through`: 添加删除线
- `no-underline`: 去除下划线


## 实例


```css
<p class="underline ...">测试文本内容 ...</p>
<p class="overline ...">测试文本内容 ...</p>
<p class="line-through ...">测试文本内容 ...</p>
<p class="no-underline ...">测试文本内容 ...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 9. 文本装饰（Text Transform）


Tailwind 提供了 `uppercase`、`lowercase` 和 `capitalize` 类来控制文本的大小写转换。


#### 常用工具类：


- `uppercase`: 全部大写
- `lowercase`: 全部小写
- `capitalize`: 每个单词首字母大写


## 实例


```css
<p class="normal-case ...">测试文本内容 ...</p>
<p class="uppercase ...">测试文本内容 ...</p>
<p class="lowercase ...">测试文本内容 ...</p>
<p class="capitalize ...">测试文本内容 ...</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 10. 文本阴影（Text Shadow）


Tailwind 允许你为文本添加阴影效果，使用 `text-shadow` 工具类。


#### 常用工具类：


- `text-shadow`: 设置简单的文本阴影（此功能需要自定义插件或扩展）。


## 实例


```css
<p class="text-shadow">这段文本有阴影效果</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)

### 11. 响应式字体（Responsive Font Size）


Tailwind 支持响应式设计，你可以在不同屏幕大小下设置不同的字体大小。通过为不同的屏幕尺寸添加前缀如 `sm:`, `md:`, `lg:`, `xl:` 等来控制字体大小。


## 实例


```css
<p class="text-sm sm:text-base md:text-lg lg:text-xl xl:text-2xl">这是响应式文本大小</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_typography1)








	  AI 思考中...





			** [Tailwind CSS 表格](https://www.runoob.com/tailwindcss-table.html)
			[Tailwind CSS 背景颜色](https://www.runoob.com/tailwindcss-backgrounds.html) **













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