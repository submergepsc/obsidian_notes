# 并查集 rank 的优化

- Source: https://www.runoob.com/data-structures/union-find-rank.html

上一小节介绍了并查集基于 size 的优化，但是某些场景下，也会存在某些问题，如下图所示，操作 union(4,2)。


![](https://www.runoob.com/wp-content/uploads/2020/10/rank-01.png)


根据上一小节，size 的优化，元素少的集合根节点指向元素多的根节点。操作完后，层数变为4，比之前增多了一层，如下图所示：


![](https://www.runoob.com/wp-content/uploads/2020/10/rank-02.png)


由此可知，依靠集合的 size 判断指向并不是完全正确的，更准确的是，根据两个集合层数，具体判断根节点的指向，层数少的集合根节点指向层数多的集合根节点，如下图所示，这就是基于 rank 的优化。


![](https://www.runoob.com/wp-content/uploads/2020/10/rank-03.png)


我们在并查集的属性中，添加 rank 数组，rank[i] 表示以 i 为根的集合所表示的树的层数。


```
...
private int[] rank;   // rank[i]表示以i为根的集合所表示的树的层数
private int[] parent; // parent[i]表示第i个元素所指向的父节点
private int count;    // 数据个数
...
```


构造函数相应作出修改：


```
...
// 构造函数
public UnionFind4(int count){
    rank = new int[count];
    parent = new int[count];
    this.count = count;
    // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
    for( int i = 0 ; i < count ; i ++ ){
        parent[i] = i;
        rank[i] = 1;
    }
}
...
```


合并两元素的时候，需要比较根节点集合的层数，整个过程是 O(h)复杂度，h为树的高度。


```
...
public void unionElements(int p, int q){
    int pRoot = find(p);
    int qRoot = find(q);
    if( pRoot == qRoot )
        return;

    if( rank[pRoot] < rank[qRoot] ){
        parent[pRoot] = qRoot;
    }
    else if( rank[qRoot] < rank[pRoot]){
        parent[qRoot] = pRoot;
    }
    else{ // rank[pRoot] == rank[qRoot]
        parent[pRoot] = qRoot;
        rank[qRoot] += 1;   // 此时, 我维护rank的值
    }
}
...
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-union.zip)


## UnionFind3.java 文件代码：


```
package runoob.union;
/**
 * 基于rank的优化
 */
public class UnionFind4 {
    private int[] rank;   // rank[i]表示以i为根的集合所表示的树的层数
    private int[] parent; // parent[i]表示第i个元素所指向的父节点
    private int count;    // 数据个数
    // 构造函数
    public UnionFind4(int count){
        rank = new int[count];
        parent = new int[count];
        this.count = count;
        // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
        for( int i = 0 ; i < count ; i ++ ){
            parent[i] = i;
            rank[i] = 1;
        }
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
        if( rank[pRoot] < rank[qRoot] ){
            parent[pRoot] = qRoot;
        }
        else if( rank[qRoot] < rank[pRoot]){
            parent[qRoot] = pRoot;
        }
        else{ // rank[pRoot] == rank[qRoot]
            parent[pRoot] = qRoot;
            rank[qRoot] += 1;   // 维护rank的值
        }
    }
}
```










	  AI 思考中...





			** [并查集 size 的优化](https://www.runoob.com/union-find-size.html)
			[并查集路径压缩](https://www.runoob.com/union-find-compress.html) **













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