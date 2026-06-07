# 相邻节点迭代器

- Source: https://www.runoob.com/data-structures/graph-theory-iter.html

图论中最常见的操作就是遍历邻边，通过一个顶点遍历相关的邻边。邻接矩阵的遍历邻边的时间复杂度为 O(V)，邻接表可以直接找到，效率更高。


![](https://www.runoob.com/wp-content/uploads/2020/10/iter-01.png)


**邻接矩阵迭代:**


```
...
public Iterable<Integer> adj(int v) {
    assert v >= 0 && v < n;
    Vector<Integer> adjV = new Vector<Integer>();
    for(int i = 0 ; i < n ; i ++ )
        if( g[v][i] )
            adjV.add(i);
    return adjV;
}
...
```


**邻接表迭代：**


```
...
// 返回图中一个顶点的所有邻边
// 由于java使用引用机制，返回一个Vector不会带来额外开销,
public Iterable<Integer> adj(int v) {
    assert v >= 0 && v < n;
    return g[v];
}
...
```


对于这两种图的表达方式我们可以抽象出一个接口，生成这一套算法的框架，而不用去考虑底层是邻接表还是邻接矩阵。

本小节写了一个测试用例 GraphReadTest，通过调用抽象接口实现图的展示，可以在 read 包查看。


```
/**
 * 图的抽象接口
 */
public interface Graph {
    public int V();
    public int E();
    public void addEdge( int v , int w );
    boolean hasEdge( int v , int w );
    void show();
    public Iterable<Integer> adj(int v);
}
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-Graph-Theory.zip)


**（1）邻接矩阵迭代**


## src/runoob/graph/DenseGraphIterater.java 文件代码：


```
package runoob.graph;

import java.util.Vector;

/**
 * 邻接矩阵迭代
 */
public class DenseGraphIterater {
    // 节点数
    private int n;
    // 边数
    private int m;
    // 是否为有向图
    private boolean directed;
    // 图的具体数据
    private boolean[][] g;

    // 构造函数
    public DenseGraphIterater( int n , boolean directed ){
        assert n >= 0;
        this.n = n;
        this.m = 0;
        this.directed = directed;
        // g初始化为n*n的布尔矩阵, 每一个g[i][j]均为false, 表示没有任和边
        // false为boolean型变量的默认值
        g = new boolean[n][n];
    }
    // 返回节点个数
    public int V(){ return n;}
    // 返回边的个数
    public int E(){ return m;}

    // 向图中添加一个边
    public void addEdge( int v , int w ){
        assert v >= 0 && v < n ;
        assert w >= 0 && w < n ;
        if( hasEdge( v , w ) )
            return;
        g[v][w] = true;
        if( !directed )
            g[w][v] = true;
        m ++;
    }

    // 验证图中是否有从v到w的边
    boolean hasEdge( int v , int w ){
        assert v >= 0 && v < n ;
        assert w >= 0 && w < n ;
        return g[v][w];
    }
    // 返回图中一个顶点的所有邻边
    // 由于java使用引用机制，返回一个Vector不会带来额外开销,
    public Iterable<Integer> adj(int v) {
        assert v >= 0 && v < n;
        Vector<Integer> adjV = new Vector<Integer>();
        for(int i = 0 ; i < n ; i ++ )
            if( g[v][i] )
                adjV.add(i);
        return adjV;
    }
}
```


**（2）邻接表迭代**


## src/runoob/graph/SparseGraphIterater.java 文件代码：


```
package runoob.graph;

import java.util.Vector;

/**
 * 邻接表迭代
 */
public class SparseGraphIterater {

    private int n;  // 节点数
    private int m;  // 边数
    private boolean directed;    // 是否为有向图
    private Vector<Integer>[] g; // 图的具体数据

    // 构造函数
    public SparseGraphIterater( int n , boolean directed ){
        assert n >= 0;
        this.n = n;
        this.m = 0;    // 初始化没有任何边
        this.directed = directed;
        // g初始化为n个空的vector, 表示每一个g[i]都为空, 即没有任和边
        g = (Vector<Integer>[])new Vector[n];
        for(int i = 0 ; i < n ; i ++)
            g[i] = new Vector<Integer>();
    }
    public int V(){ return n;} // 返回节点个数
    public int E(){ return m;} // 返回边的个数

    // 向图中添加一个边
    public void addEdge( int v, int w ){

        assert v >= 0 && v < n ;
        assert w >= 0 && w < n ;

        g[v].add(w);
        if( v != w && !directed )
            g[w].add(v);

        m ++;
    }

    // 验证图中是否有从v到w的边
    boolean hasEdge( int v , int w ){

        assert v >= 0 && v < n ;
        assert w >= 0 && w < n ;

        for( int i = 0 ; i < g[v].size() ; i ++ )
            if( g[v].elementAt(i) == w )
                return true;
        return false;
    }

    // 返回图中一个顶点的所有邻边
    // 由于java使用引用机制，返回一个Vector不会带来额外开销,
    public Iterable<Integer> adj(int v) {
        assert v >= 0 && v < n;
        return g[v];
    }
}
```










	  AI 思考中...





			** [图论基础和表示](https://www.runoob.com/graph-theory.html)
			[深度优先遍历与连通分量](https://www.runoob.com/graph-theory-deep.html) **













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