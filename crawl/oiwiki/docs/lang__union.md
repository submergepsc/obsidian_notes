# 联合体 - OI Wiki

- Source: https://oi-wiki.org/lang/union/

# 联合体

**联合体** （union）是特殊的类类型，它在一个时刻只能保有其一个非静态数据成员．

联合体在 2023 年正式被加入 NOI 大纲入门级中．

## 定义联合体

联合体声明的类说明符与类或 [结构体](../struct/) 的声明相似：

```text 1 2 3 4 ``` |  ```text union MyUnion { int x ; long long y ; } x ; ```   
---|---  
  
联合体的定义与结构体类似．按照上述定义，`MyUnion` 同样可以当作一种自定义类型使用．名称 `MyUnion` 可以省略．

## 访问/修改成员元素

与结构体类似，同样可以使用 `变量名.成员名` 进行访问．

联合体所占用的内存空间大小 **不小于** 其最大的成员的大小，所有成员 **共用内存空间与地址** ．当一个成员被赋值，由于内存共享，该联合体中的其他成员都会被覆盖．即同一时刻联合体中只能保存一个成员的值．

联合体的更多用法可以参见 [cppreference：联合体声明](https://zh.cppreference.com/w/cpp/language/union)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/union.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/union.md "edit.link.title")  
>  __本页面贡献者：[Molmin](https://github.com/Molmin), [r-value](https://github.com/r-value), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
