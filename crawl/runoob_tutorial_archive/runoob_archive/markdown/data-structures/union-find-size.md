# 并查集 size 的优化

- Source: https://www.runoob.com/data-structures/union-find-size.html

按照上一小节的思路，我们把如下图所示的并查集，进行 **union(4,9)** 操作。


![](https://www.runoob.com/wp-content/uploads/2020/10/size-01.png)


合并操作后的结构为：


![](https://www.runoob.com/wp-content/uploads/2020/10/size-02.png)



可以发现，这个结构的树的层相对较高，若此时元素数量增多，这样产生的消耗就会相对较大。解决这个问题其实很简单，在进行具体指向操作的时候先进行判断，把元素少的集合根节点指向元素多的根节点，能更高概率的生成一个层数比较低的树。


构造并查集的时候需要多一个参数，**sz** 数组，**sz[i]** 表示以 **i** 为根的集合中元素个数。


```
// 构造函数
public UnionFind3(int count){
    parent = new int[count];
    sz = new int[count];
    this.count = count;
    // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
    for( int i = 0 ; i < count ; i ++ ){
        parent[i] = i;
        sz[i] = 1;
    }
}
```


在进行合并操作时候，根据两个元素所在树的元素个数不同判断合并方向。


```
public void unionElements(int p, int q){
    int pRoot = find(p);
    int qRoot = find(q);
    if( pRoot == qRoot )
        return;
    if( sz[pRoot] < sz[qRoot] ){
        parent[pRoot] = qRoot;
        sz[qRoot] += sz[pRoot];
    }
    else{
        parent[qRoot] = pRoot;
        sz[pRoot] += sz[qRoot];
    }
}
```


优化后，合并结果如下，9 指向父节点 8。


![](https://www.runoob.com/wp-content/uploads/2020/10/size-03.png)


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-union.zip)


## UnionFind3.java 文件代码：


```
package runoob.union;

/**
 * 并查集size的优化
 */
public class UnionFind3 {
    // parent[i]表示第一个元素所指向的父节点
    private int[] parent;
    // sz[i]表示以i为根的集合中元素个数
    private int[] sz;
    // 数据个数
    private int count;

    // 构造函数
    public UnionFind3(int count){
        parent = new int[count];
        sz = new int[count];
        this.count = count;
        // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
        for( int i = 0 ; i < count ; i ++ ){
            parent[i] = i;
            sz[i] = 1;
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
        // 根据两个元素所在树的元素个数不同判断合并方向
        // 将元素个数少的集合合并到元素个数多的集合上
        if( sz[pRoot] < sz[qRoot] ){
            parent[pRoot] = qRoot;
            sz[qRoot] += sz[pRoot];
        }
        else{
            parent[qRoot] = pRoot;
            sz[pRoot] += sz[qRoot];
        }
    }
}
```










	  AI 思考中...





			** [并查集快速合并](https://www.runoob.com/union-find-quick-merge.html)
			[并查集 rank 的优化](https://www.runoob.com/union-find-rank.html) **













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