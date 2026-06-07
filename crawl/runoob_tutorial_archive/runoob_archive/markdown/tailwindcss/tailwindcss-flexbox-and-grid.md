# Tailwind CSS 与 Flexbox 和 Grid 布局

- Source: https://www.runoob.com/tailwindcss/tailwindcss-flexbox-and-grid.html

Tailwind CSS 提供了强大的工具类来管理布局，特别是 Flexbox 和 Grid。

Flexbox 和 Grid 这些工具类使得你可以非常高效地创建响应式、灵活的布局，而无需编写自定义的 CSS。


Tailwind CSS 的理念是通过低层级的实用类（utility-first）来控制布局，灵活组合类以满足不同的设计需求。

---


## 1、Flexbox 布局

Flexbox 是一种布局模式，可以帮助开发者创建一维的（水平或垂直）布局。

Tailwind CSS 提供了多个简洁的工具类来控制 Flexbox 布局的各个方面，包括方向、对齐、伸缩等。


### 设置 Flex 容器

要创建一个 Flexbox 布局，首先需要将元素设为 flex 容器。


## 实例


```css
<div class="flex">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex1)

flex 将元素的 display 设置为 flex，即启用 Flexbox 布局。


flex 项初始大小的工具类及其对应的 CSS 属性：






| Tailwind类名 | CSS属性及值 | 描述 |
| --- | --- | --- |
| basis-0 | flex-basis:0px; | 设置flex项的基础大小为0px。 |
| basis-1 | flex-basis:0.25rem; | 设置flex项的基础大小为4px。 |
| basis-2 | flex-basis:0.5rem; | 设置flex项的基础大小为8px。 |
| basis-3 | flex-basis:0.75rem; | 设置flex项的基础大小为12px。 |
| basis-4 | flex-basis:1rem; | 设置flex项的基础大小为16px。 |
| basis-5 | flex-basis:1.25rem; | 设置flex项的基础大小为20px。 |
| basis-6 | flex-basis:1.5rem; | 设置flex项的基础大小为24px。 |
| basis-7 | flex-basis:1.75rem; | 设置flex项的基础大小为28px。 |
| basis-8 | flex-basis:2rem; | 设置flex项的基础大小为32px。 |
| basis-9 | flex-basis:2.25rem; | 设置flex项的基础大小为36px。 |
| basis-10 | flex-basis:2.5rem; | 设置flex项的基础大小为40px。 |
| basis-11 | flex-basis:2.75rem; | 设置flex项的基础大小为44px。 |
| basis-12 | flex-basis:3rem; | 设置flex项的基础大小为48px。 |
| basis-14 | flex-basis:3.5rem; | 设置flex项的基础大小为56px。 |
| basis-16 | flex-basis:4rem; | 设置flex项的基础大小为64px。 |
| basis-20 | flex-basis:5rem; | 设置flex项的基础大小为80px。 |
| basis-24 | flex-basis:6rem; | 设置flex项的基础大小为96px。 |
| basis-28 | flex-basis:7rem; | 设置flex项的基础大小为112px。 |
| basis-32 | flex-basis:8rem; | 设置flex项的基础大小为128px。 |
| basis-36 | flex-basis:9rem; | 设置flex项的基础大小为144px。 |
| basis-40 | flex-basis:10rem; | 设置flex项的基础大小为160px。 |
| basis-44 | flex-basis:11rem; | 设置flex项的基础大小为176px。 |
| basis-48 | flex-basis:12rem; | 设置flex项的基础大小为192px。 |
| basis-52 | flex-basis:13rem; | 设置flex项的基础大小为208px。 |
| basis-56 | flex-basis:14rem; | 设置flex项的基础大小为224px。 |
| basis-60 | flex-basis:15rem; | 设置flex项的基础大小为240px。 |
| basis-64 | flex-basis:16rem; | 设置flex项的基础大小为256px。 |
| basis-72 | flex-basis:18rem; | 设置flex项的基础大小为288px。 |
| basis-80 | flex-basis:20rem; | 设置flex项的基础大小为320px。 |
| basis-96 | flex-basis:24rem; | 设置flex项的基础大小为384px。 |
| basis-auto | flex-basis:auto; | 设置flex项的基础大小为自动。 |
| basis-px | flex-basis:1px; | 设置flex项的基础大小为1px。 |
| basis-0.5 | flex-basis:0.125rem; | 设置flex项的基础大小为2px。 |
| basis-1.5 | flex-basis:0.375rem; | 设置flex项的基础大小为6px。 |
| basis-2.5 | flex-basis:0.625rem; | 设置flex项的基础大小为10px。 |
| basis-3.5 | flex-basis:0.875rem; | 设置flex项的基础大小为14px。 |
| basis-1/2 | flex-basis:50%; | 设置flex项的基础大小为容器宽度的一半。 |
| basis-1/3 | flex-basis:33.333333%; | 设置flex项的基础大小为容器宽度的三分之一。 |
| basis-2/3 | flex-basis:66.666667%; | 设置flex项的基础大小为容器宽度的三分之二。 |
| basis-1/4 | flex-basis:25%; | 设置flex项的基础大小为容器宽度的四分之一。 |
| basis-2/4 | flex-basis:50%; | 设置flex项的基础大小为容器宽度的二分之一。 |
| basis-3/4 | flex-basis:75%; | 设置flex项的基础大小为容器宽度的四分之三。 |
| basis-1/5 | flex-basis:20%; | 设置flex项的基础大小为容器宽度的五分之一。 |
| basis-2/5 | flex-basis:40%; | 设置flex项的基础大小为容器宽度的五分之二。 |
| basis-3/5 | flex-basis:60%; | 设置flex项的基础大小为容器宽度的五分之三。 |
| basis-4/5 | flex-basis:80%; | 设置flex项的基础大小为容器宽度的五分之四。 |
| basis-1/6 | flex-basis:16.666667%; | 设置flex项的基础大小为容器宽度的六分之一。 |
| basis-2/6 | flex-basis:33.333333%; | 设置flex项的基础大小为容器宽度的六分之二。 |
| basis-3/6 | flex-basis:50%; | 设置flex项的基础大小为容器宽度的三分之二。 |
| basis-4/6 | flex-basis:66.666667%; | 设置flex项的基础大小为容器宽度的六分之四。 |
| basis-5/6 | flex-basis:83.333333%; | 设置flex项的基础大小为容器宽度的六分之五。 |
| basis-1/12 | flex-basis:8.333333%; | 设置flex项的基础大小为8.33%。 |
| basis-2/12 | flex-basis:16.666667%; | 设置flex项的基础大小为16.67%。 |
| basis-3/12 | flex-basis:25%; | 设置flex项的基础大小为25%。 |
| basis-4/12 | flex-basis:33.333333%; | 设置flex项的基础大小为33.33%。 |
| basis-5/12 | flex-basis:41.666667%; | 设置flex项的基础大小为41.67%。 |
| basis-6/12 | flex-basis:50%; | 设置flex项的基础大小为50%。 |
| basis-7/12 | flex-basis:58.333333%; | 设置flex项的基础大小为58.33%。 |
| basis-8/12 | flex-basis:66.666667%; | 设置flex项的基础大小为66.67%。 |
| basis-9/12 | flex-basis:75%; | 设置flex项的基础大小为75%。 |
| basis-10/12 | flex-basis:83.333333%; | 设置flex项的基础大小为83.33%。 |
| basis-11/12 | flex-basis:91.666667%; | 设置flex项的基础大小为91.67%。 |
| basis-full | flex-basis:100%; | 设置flex项的基础大小为100%。 |


## 实例


```css
<div class="flex flex-row">
  <div class="basis-1/4">01</div>
  <div class="basis-1/4">02</div>
  <div class="basis-1/2">03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex2)


### Flex 方向

flex-direction 控制主轴的方向（即 Flex 容器内项目排列的方向）。

Tailwind 提供了以下工具类来设置方向：


- `flex-row`: 默认值，子项按水平方向从左到右排列。
- `flex-row-reverse`: 子项按水平方向从右到左排列。
- `flex-col`: 子项按垂直方向从上到下排列。
- `flex-col-reverse`: 子项按垂直方向从下到上排列。


## 实例


```css
<div class="flex flex-row ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>

<div class="flex flex-row-reverse ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>

<div class="flex flex-col ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex3)


### Flex 包裹（Flex Wrap）

默认情况下，Flexbox 容器中的项目会在单行内排列。

如果你希望它们换行，可以使用 flex-wrap 工具类。


- `flex-wrap`: 允许项目换行。
- `flex-nowrap`: 禁止项目换行。
- `flex-wrap-reverse`: 反向换行。


## 实例


```css
<div class="flex flex-nowrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>

<div class="flex flex-wrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>

<div class="flex flex-wrap-reverse">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex4)


### Flex 项目的伸缩性

Flexbox 允许元素的大小根据可用空间进行伸缩。

Tailwind CSS 提供了以下工具类来控制伸缩：


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| flex-1 | flex: 1 1 0%; | 使 flex 项具有等量的 flex 增长和收缩能力，基础大小为 0%，常用于创建等宽或等高的 flex 布局。 |
| flex-auto | flex: 1 1 auto; | 使 flex 项具有自动的基础大小和等量的 flex 增长和收缩能力，常用于让 flex 项填充额外空间。 |
| flex-initial | flex: 0 1 auto; | 使 flex 项具有自动的基础大小，不增长但可以收缩，用于保持元素的自然大小，除非空间不足。 |
| flex-none | flex: none; | 防止 flex 项增长或收缩，使其保持基础大小，常用于固定元素的大小。 |


## 实例


```css
<div class="flex">
  <div class="flex-none w-14 ...">
    01
  </div>
  <div class="flex-initial w-64 ...">
    02
  </div>
  <div class="flex-initial w-32 ...">
    03
  </div>
</div>

<div class="flex">
  <div class="flex-none w-14 ...">
    01
  </div>
  <div class="flex-1 w-64 ...">
    02
  </div>
  <div class="flex-1 w-32 ...">
    03
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex5)


### flex-grow 属性


以下是控制 flex 项的 flex-grow 属性的工具类及其对应的 CSS 属性：


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| grow | flex-grow: 1; | 允许 flex 项增长以填充额外空间，其增长比例为 1。 |
| grow-0 | flex-grow: 0; | 防止 flex 项增长以填充额外空间，其增长比例为 0。 |


## 实例


```css
<div class="flex ...">
  <div class="flex-none w-14 h-14 ...">
    01
  </div>
  <div class="grow h-14 ...">
    02
  </div>
  <div class="flex-none w-14 h-14 ...">
    03
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex6)


### flex-shrink 属性

以下是控制 flex 项的 flex-shrink 属性的工具类及其对应的 CSS 属性：


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| shrink | flex-shrink: 1; | 允许 flex 项在必要时缩小以适应 flex 容器，其缩小比例为 1。 |
| shrink-0 | flex-shrink: 0; | 防止 flex 项在必要时缩小以适应 flex 容器，其缩小比例为 0。 |


## 实例


```css
<div class="flex ...">
  <div class="flex-none w-14 h-14 ...">
    01
  </div>
  <div class="shrink w-64 h-14 ...">
    02
  </div>
  <div class="flex-none w-14 h-14 ...">
    03
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex7)


---


## 排序


以下是用于控制 flex 项或 grid 项排列顺序的工具类及其对应的 CSS 属性：


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| order-1 | order: 1; | 将 flex 项或 grid 项的排列顺序设置为 1。 |
| order-2 | order: 2; | 将 flex 项或 grid 项的排列顺序设置为 2。 |
| order-3 | order: 3; | 将 flex 项或 grid 项的排列顺序设置为 3。 |
| order-4 | order: 4; | 将 flex 项或 grid 项的排列顺序设置为 4。 |
| order-5 | order: 5; | 将 flex 项或 grid 项的排列顺序设置为 5。 |
| order-6 | order: 6; | 将 flex 项或 grid 项的排列顺序设置为 6。 |
| order-7 | order: 7; | 将 flex 项或 grid 项的排列顺序设置为 7。 |
| order-8 | order: 8; | 将 flex 项或 grid 项的排列顺序设置为 8。 |
| order-9 | order: 9; | 将 flex 项或 grid 项的排列顺序设置为 9。 |
| order-10 | order: 10; | 将 flex 项或 grid 项的排列顺序设置为 10。 |
| order-11 | order: 11; | 将 flex 项或 grid 项的排列顺序设置为 11。 |
| order-12 | order: 12; | 将 flex 项或 grid 项的排列顺序设置为 12。 |
| order-first | order: -9999; | 将 flex 项或 grid 项的排列顺序设置为最前。 |
| order-last | order: 9999; | 将 flex 项或 grid 项的排列顺序设置为最后。 |
| order-none | order: 0; | 将 flex 项或 grid 项的排列顺序设置为默认顺序，即不改变其顺序。 |


## 实例


```css
<div class="flex justify-between ...">
  <div class="order-last">01</div>
  <div>02</div>
  <div>03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex8)


---


## Grid (网格) 布局

Grid 是另一种布局模型，允许你在行和列中精确地定位元素，并且能够轻松创建复杂的布局。

Tailwind CSS 提供了强大的工具类来操作网格布局。


以下是 Tailwind CSS 中用于指定网格布局中列数的工具类及其对应的 CSS 属性：


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| grid-cols-1 | grid-template-columns: repeat(1, minmax(0, 1fr)); | 创建一个包含1列的网格布局。 |
| grid-cols-2 | grid-template-columns: repeat(2, minmax(0, 1fr)); | 创建一个包含2列的网格布局。 |
| grid-cols-3 | grid-template-columns: repeat(3, minmax(0, 1fr)); | 创建一个包含3列的网格布局。 |
| grid-cols-4 | grid-template-columns: repeat(4, minmax(0, 1fr)); | 创建一个包含4列的网格布局。 |
| grid-cols-5 | grid-template-columns: repeat(5, minmax(0, 1fr)); | 创建一个包含5列的网格布局。 |
| grid-cols-6 | grid-template-columns: repeat(6, minmax(0, 1fr)); | 创建一个包含6列的网格布局。 |
| grid-cols-7 | grid-template-columns: repeat(7, minmax(0, 1fr)); | 创建一个包含7列的网格布局。 |
| grid-cols-8 | grid-template-columns: repeat(8, minmax(0, 1fr)); | 创建一个包含8列的网格布局。 |
| grid-cols-9 | grid-template-columns: repeat(9, minmax(0, 1fr)); | 创建一个包含9列的网格布局。 |
| grid-cols-10 | grid-template-columns: repeat(10, minmax(0, 1fr)); | 创建一个包含10列的网格布局。 |
| grid-cols-11 | grid-template-columns: repeat(11, minmax(0, 1fr)); | 创建一个包含11列的网格布局。 |
| grid-cols-12 | grid-template-columns: repeat(12, minmax(0, 1fr)); | 创建一个包含12列的网格布局。 |
| grid-cols-none | grid-template-columns: none; | 不创建网格列，子元素将不使用网格布局。 |
| grid-cols-subgrid | grid-template-columns: subgrid; | 使用子网格布局，子元素将继承父网格的列定义。 |


## 实例


```css
<div class="grid grid-cols-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>09</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex9)


- `grid`: 启用 Grid 布局。
- `grid-cols-{n}`: 设置网格的列数。
- `gap-{size}`: 设置列和行之间的间距。


### Grid 行与列

通过 `grid-template-columns` 和 `grid-template-rows` 控制列和行的宽度和高度。Tailwind 提供了如下的工具类来控制：


- `grid-cols-{n}`: 设置网格的列数（例如 `grid-cols-3` 表示三列）。
- `grid-rows-{n}`: 设置网格的行数（例如 `grid-rows-2` 表示两行）。
- `col-span-{n}`: 设置一个项目占用多少列。
- `row-span-{n}`: 设置一个项目占用多少行。


## 实例


```css
<div class="grid grid-cols-4 gap-4">
  <div>01</div>
  <!-- ... -->
  <div>05</div>
  <div class="grid grid-cols-subgrid gap-4 col-span-3">
    <div class="col-start-2">06</div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex10)


## 实例


```css
<div class="grid grid-cols-3 gap-4">
  <div class="...">01</div>
  <div class="...">02</div>
  <div class="...">03</div>
  <div class="col-span-2 ...">04</div>
  <div class="...">05</div>
  <div class="...">06</div>
  <div class="col-span-2 ...">07</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex11)


## 实例


```css
<div class="grid grid-rows-3 grid-flow-col gap-4">
  <div class="row-span-3 ...">01</div>
  <div class="col-span-2 ...">02</div>
  <div class="row-span-2 col-span-2 ...">03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex12)


### Grid 项目的定位

grid-column 和 grid-row 控制每个项目在网格中的位置。

你可以通过以下工具类来指定：


- `col-start-{n}`: 设置项目从第 n 列开始。
- `col-end-{n}`: 设置项目到第 n 列结束。
- `row-start-{n}`: 设置项目从第 n 行开始。
- `row-end-{n}`: 设置项目到第 n 行结束。


## 实例


```css
<div class="grid grid-cols-6 gap-4">
  <div class="col-start-2 col-span-4 ...">01</div>
  <div class="col-start-1 col-end-3 ...">02</div>
  <div class="col-end-7 col-span-2 ...">03</div>
  <div class="col-start-1 col-end-7 ...">04</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex13)


## 实例


```css
<div class="grid grid-rows-3 grid-flow-col gap-4">
  <div class="row-start-2 row-span-2 ...">01</div>
  <div class="row-end-3 row-span-2 ...">02</div>
  <div class="row-start-1 row-end-4 ...">03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex14)


---


## 对齐和分布

类似于 Flexbox，Grid 也提供了对齐和分布的选项。


justify-content 属性用于对齐容器内的子元素沿着主轴（水平方向）进行排列。


| Tailwind 类名 | CSS 属性及值 | 描述 |
| --- | --- | --- |
| justify-normal | justify-content: normal; | 使用默认的对齐方式，通常等同于 start。 |
| justify-start | justify-content: flex-start; | 将所有子元素移至容器的起始端。在水平布局中，子元素会靠左对齐。 |
| justify-end | justify-content: flex-end; | 将所有子元素移至容器的结束端。在水平布局中，子元素会靠右对齐。 |
| justify-center | justify-content: center; | 将所有子元素居中对齐。 |
| justify-between | justify-content: space-between; | 子元素之间的空间均等分布，两端不留空白。 |
| justify-around | justify-content: space-around; | 子元素之间的空间均等分布，两端留有一半的空白。 |
| justify-evenly | justify-content: space-evenly; | 子元素之间的空间完全均等，包括两端的空白。 |
| justify-stretch | justify-content: stretch; | 子元素被拉伸以填充容器，每个子元素占据相同的空间。 |


## 实例


```css
<div class="flex justify-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex15)

其他对齐设置：


- `justify-items`: 控制网格单元格内容的对齐方式。
- `justify-self`: 控制单个网格项目的对齐方式。
- `align-items`: 控制网格单元格的垂直对齐方式。
- `align-self`: 控制单个网格项目的垂直对齐方式。


## 实例


```css
<div class="grid justify-items-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_flex16)








	  AI 思考中...





			** [Tailwind CSS 布局类](https://www.runoob.com/tailwindcss-layout.html)
			[Tailwind CSS 间距](https://www.runoob.com/tailwindcss-spacing.html) **













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