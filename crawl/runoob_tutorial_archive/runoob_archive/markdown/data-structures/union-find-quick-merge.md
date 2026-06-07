# 并查集快速合并

- Source: https://www.runoob.com/data-structures/union-find-quick-merge.html

对于一组数据，并查集主要支持两个动作：


- **union(p,q) ** - 将 p 和 q 两个元素连接起来。
- **find(p)** - 查询 p 元素在哪个集合中。
- **isConnected(p,q)** - 查看 p 和 q 两个元素是否相连接在一起。


在上一小节中，我们用 **id** 数组的形式表示并查集，实际操作过程中查找的时间复杂度为 **O(1)**，但连接效率并不高。

本小节，我们将用另外一种方式实现并查集。把每一个元素，看做是一个节点并且指向自己的父节点，根节点指向自己。如下图所示，节点 3 指向节点 2，代表 3 和 2 是连接在一起的，节点2本身是根节点，所以指向自己。


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-01.png)

同样用数组表示并查集，但是下面一组元素用 **parent** 表示当前元素指向的父节点，每个元素指向自己，都是独立的。


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-02.png)


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-03.png)


如果此时操作 **union(4,3)**，将元素 4 指向元素 3：


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-04.png)


数组也进行相应改变：


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-05.png)


判断两个元素是否连接，只需要判断根节点是否相同即可。

如下图，节点 4 和节点 9 的根节点都是 8，所以它们是相连的。


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-06.png)


连接两个元素，只需要找到它们对应的根节点，使根节点相连，那它们就是相连的节点。

假设要使上图中的 6 和 4 相连，只需要把 6 的根节点 5 指向 4 的根节点 8 即可。


![](https://www.runoob.com/wp-content/uploads/2020/10/quickUnion-07.png)


构建这种指向父节点的树形结构， 使用一个数组构建一棵指向父节点的树，parent[i] 表示 i 元素所指向的父节点。


```
...
private int[] parent;
private int count;  // 数据个数
...
```


查找过程, 查找元素 p 所对应的集合编号，不断去查询自己的父亲节点, 直到到达根节点，根节点的特点 parent[p] == p，O(h) 复杂度, h 为树的高度。


```
...
private int find(int p){
    assert( p >= 0 && p < count );
    while( p != parent[p] )
        p = parent[p];
    return p;
}
...
```


合并元素 p 和元素 q 所属的集合，分别查询两个元素的根节点，使其中一个根节点指向另外一个根节点，两个集合就合并了。这个操作是 O(h) 的时间复杂度，h 为树的高度。


```
public void unionElements(int p, int q){
    int pRoot = find(p);
    int qRoot = find(q);
    if( pRoot == qRoot )
        return;
    parent[pRoot] = qRoot;
}
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-union.zip)


## UnionFind2.java 文件代码：


```
package runoob.union;
/**
 * 第二版unionFind
 */
public class UnionFind2 {
    // 我们的第二版Union-Find, 使用一个数组构建一棵指向父节点的树
    // parent[i]表示第一个元素所指向的父节点
    private int[] parent;
    private int count;  // 数据个数
    // 构造函数
    public UnionFind2(int count){
        parent = new int[count];
        this.count = count;
        // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
        for( int i = 0 ; i < count ; i ++ )
            parent[i] = i;
    }
    // 查找过程, 查找元素p所对应的集合编号
    // O(h)复杂度, h为树的高度
    private int find(int p){
        assert( p >= 0 && p < count );
        // 不断去查询自己的父亲节点, 直到到达根节点
        // 根节点的特点: parent[p] == p
        while( p != parent[p] )
            p = parent[p];
        return p;
    }
    // 查看元素p和元素q是否所属一个集合
    // O(h)复杂度, h为树的高度
    public boolean isConnected( int p , int q ){
        return find(p) == find(q);
    }
    // 合并元素p和元素q所属的集合
    // O(h)复杂度, h为树的高度
    public void unionElements(int p, int q){
        int pRoot = find(p);
        int qRoot = find(q);
        if( pRoot == qRoot )
            return;
        parent[pRoot] = qRoot;
    }
}
```










	  AI 思考中...





			** [并查集快速查找](https://www.runoob.com/union-find-quick.html)
			[并查集 size 的优化](https://www.runoob.com/union-find-size.html) **













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