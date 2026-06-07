# Markdown 高级技巧

- Source: https://www.runoob.com/markdown/md-advance.html

### 支持的 HTML 元素


不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。


目前支持的 HTML 元素有：`      `等 ，如：


```
使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑
```


输出结果为：


![](https://www.runoob.com/wp-content/uploads/2019/03/81999271-F914-428D-B7BF-164BDC67CAAC.jpg)


### 转义


Markdown 使用了很多特殊符号来表示特定的意义，如果需要显示特定的符号则需要使用转义字符，Markdown 使用反斜杠转义特殊字符：


```
**文本加粗**
\*\* 正常显示星号 \*\*
```


输出结果为：


![](https://www.runoob.com/wp-content/uploads/2019/03/403f0a87adf7a521e79b49b676ad5473w.png)


Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：


```
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  小括号
#   井字号
+   加号
-   减号
.   英文句点
!   感叹号
```


### 公式


**Markdown Preview Enhanced** 使用 [KaTeX](https://github.com/Khan/KaTeX) 或者 [MathJax](https://github.com/mathjax/MathJax) 来渲染数学表达式。


KaTeX 拥有比 MathJax 更快的性能，但是它却少了很多 MathJax 拥有的特性。你可以查看 KaTeX supported functions/symbols 来了解 KaTeX 支持那些符号和函数。


默认下的分隔符：


- `$...$` 或者 `\(...\)` 中的数学表达式将会在行内显示。
- `$$...$$` 或者 `\[...\]` 或者 ````math` 中的数学表达式将会在块内显示。


![](https://www.runoob.com/wp-content/uploads/2019/03/0e408954-fda8-11e5-9eb4-562d7c0ca431.gif)


```
$$
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
$$
$$
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
$$
```


输出结果为：


![](https://www.runoob.com/wp-content/uploads/2019/03/A9031CEB-04DB-4822-9C98-2E99489D3662.jpeg)









	  AI 思考中...





			** [Markdown 表格](https://www.runoob.com/md-table.html)
			[Markdown 编辑器](https://www.runoob.com/md-editor.html) **