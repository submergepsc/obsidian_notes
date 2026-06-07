# Markdown 数学公式

- Source: https://www.runoob.com/markdown/md-math.html

### LaTeX 数学公式基础


在 Markdown 中，数学公式通过 LaTeX 语法来表示。LaTeX 是一个强大的排版系统，特别适用于包含复杂数学公式的文档。


#### 基本语法结构


- **命令**：以反斜杠 `\` 开头，如 `\alpha`、`\sum`
- **参数**：用花括号 `{}` 包围，如 `\frac{a}{b}`
- **下标**：使用 `_`，如 `x_1`
- **上标**：使用 `^`，如 `x^2`
- **分组**：用花括号将多个字符组合，如 `x_{i+1}`


#### 常用 LaTeX 命令


```
\alpha, \beta, \gamma  % 希腊字母
\sum, \prod, \int      % 求和、乘积、积分
\frac{分子}{分母}      % 分数
\sqrt{表达式}          % 平方根
\sqrt[n]{表达式}       % n次根
```


### 行内公式与块级公式


#### 行内公式


行内公式使用单个美元符号 `$` 包围，公式会嵌入到文本中，如：文本中的变量 $x = 5$ 和函数 $f(x) = x^2 + 2x + 1$。


```
文本中的变量 $x = 5$ 和函数 $f(x) = x^2 + 2x + 1$。
```


![](https://www.runoob.com/wp-content/uploads/2025/05/446e3e7c-6804-4c30-865d-a40d79e00568.png)


#### 块级公式


块级公式使用双美元符号 `**$$**` 包围，公式会独立成行并居中显示：


E = mc^2


\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}


```
$$E = mc^2$$

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$
```


![](https://www.runoob.com/wp-content/uploads/2025/05/50d6bdb1-3519-4723-98a8-d5ffac85f714.png)


#### 多行公式


使用 `align` 环境创建多行对齐公式：


**\begin{align} f(x) &= ax^2 + bx + c \ f'(x) &= 2ax + b \ f''(x) &= 2a \end{align}


```
$$
    \begin{align}
    f(x) &= ax^2 + bx + c \\
    f'(x)  &= 2ax + b \\
    f''(x)  &= 2a
    \end{align}
    $$
```


![](https://www.runoob.com/wp-content/uploads/2025/05/162677d1-b935-444e-be28-7aebe60887ec.png)


---


## 常用数学符号


### 基本运算符号


- 加减乘除：`+`, `-`, `\times`, `\div`
- 分数：`\frac{a}{b}` → $\frac{a}{b}$
- 根号：`\sqrt{x}`, `\sqrt[n]{x}` → $\sqrt{x}$, $\sqrt[n]{x}$
- 指数：`x^2`, `e^{i\pi}` → $x^2$, $e^{i\pi}$


### 比较符号


- 等于：`=`, `\neq`, `\equiv` → $=$, $\neq$, $\equiv$
- 大小：``, `\leq`, `\geq` → $$, $\leq$, $\geq$
- 约等于：`\approx`, `\sim` → $\approx$, $\sim$


### 集合符号


- 属于：`\in`, `\notin` → $\in$, $\notin$
- 包含：`\subset`, `\supset` → $\subset$, $\supset$
- 交并：`\cap`, `\cup` → $\cap$, $\cup$
- 空集：`\emptyset` → $\emptyset$


### 希腊字母


常用希腊字母及其 LaTeX 表示：


| 小写 | 大写 | LaTeX | 小写 | 大写 | LaTeX |
| --- | --- | --- | --- | --- | --- |
| α | Α | \alpha | ν | Ν | \nu |
| β | Β | \beta | ο | Ο | o |
| γ | Γ | \gamma | π | Π | \pi |
| δ | Δ | \delta | ρ | Ρ | \rho |
| ε | Ε | \epsilon | σ | Σ | \sigma |
| θ | Θ | \theta | τ | Τ | \tau |
| λ | Λ | \lambda | φ | Φ | \phi |
| μ | Μ | \mu | ω | Ω | \omega |


### 特殊函数和符号


- 三角函数：`\sin`, `\cos`, `\tan`
- 对数：`\log`, `\ln`
- 极限：`\lim_{x \to 0}`
- 求和：`\sum_{i=1}^{n}`
- 积分：`\int_{a}^{b}`
- 无穷：`\infty`


### 矩阵表示 使用 matrix 环境： \begin{pmatrix}a & b \c & d\end{pmatrix}
```
$$
    \begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}
    $$
```
 不同括号类型的矩阵： pmatrix：圆括号 $\begin{pmatrix} a & b \ c & d \end{pmatrix}$ bmatrix：方括号 $\begin{bmatrix} a & b \ c & d \end{bmatrix}$ vmatrix：行列式 $\begin{vmatrix} a & b \ c & d \end{vmatrix}$ AI 思考中... Markdown 分割线 Markdown 图表绘制 点我分享笔记







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