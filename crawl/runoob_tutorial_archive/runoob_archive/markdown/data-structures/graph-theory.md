# 图论基础和表示

- Source: https://www.runoob.com/data-structures/graph-theory.html

### 一、概念及其介绍

图论(Graph Theory)是离散数学的一个分支，是一门研究图(Graph)的学问。

图是用来对对象之间的成对关系建模的数学结构，由"节点"或"顶点"(Vertex）以及连接这些顶点的"边"（Edge）组成。

值得注意的是，图的顶点集合不能为空，但边的集合可以为空。图可能是无向的，这意味着图中的边在连接顶点时无需区分方向。否则，称图是有向的。下面左图是一个典型的无向图结构，右图则属于有向图。本章节介绍的图都是无向图。


![](https://www.runoob.com/wp-content/uploads/2020/10/graph-01.png)

图的分类：无权图和有权图，连接节点与节点的边是否有数值与之对应，有的话就是有权图，否则就是无权图。


**图的连通性：**在图论中，连通图基于连通的概念。在一个无向图 G 中，若从顶点 i 到顶点 j 有路径相连（当然从j到i也一定有路径），则称 i 和 j 是连通的。如果 G 是有向图，那么连接i和j的路径中所有的边都必须同向。如果图中任意两点都是连通的，那么图被称作连通图。如果此图是有向图，则称为强连通图（注意：需要双向都有路径）。图的连通性是图的基本性质。


**完全图：**完全是一个简单的无向图，其中每对不同的顶点之间都恰连有一条边相连。


**自环边：**一条边的起点终点是一个点。


**平行边：**两个顶点之间存在多条边相连接。


### 二、适用说明


图可用于在物理、生物、社会和信息系统中建模许多类型的关系和过程，许多实际问题可以用图来表示。因此，图论成为运筹学、控制论、信息论、网络理论、博弈论、物理学、化学、生物学、社会科学、语言学、计算机科学等众多学科强有力的数学工具。在强调其应用于现实世界的系统时，网络有时被定义为一个图，其中属性(例如名称)之间的关系以节点和或边的形式关联起来。


### 三、图的表达形式


**邻接矩阵：**1 表示相连接，0 表示不相连。


![](https://www.runoob.com/wp-content/uploads/2020/10/graph-02.png)


**邻接表：**只表达和顶点相连接的顶点信息


![](https://www.runoob.com/wp-content/uploads/2020/10/graph-03.png)


邻接表适合表示稀疏图 (Sparse Graph)


邻接矩阵适合表示稠密图 (Dense Graph)


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-Graph-Theory.zip)


**(1) 邻接矩阵**


## src/runoob/graph/DenseGraph.java 文件代码：


```
package runoob.graph;

/**
 * 邻接矩阵
 */
public class DenseGraph {
    // 节点数
    private int n;
    // 边数
    private int m;
    // 是否为有向图
    private boolean directed;
    // 图的具体数据
    private boolean[][] g;

    // 构造函数
    public DenseGraph( int n , boolean directed ){
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
}
```


**（2）邻接表**


## src/runoob/graph/SparseGraph.java 文件代码：


```
package runoob.graph;

import java.util.Vector;

/**
 * 邻接表
 */
public class SparseGraph {
    // 节点数
    private int n;
    // 边数
    private int m;
    // 是否为有向图
    private boolean directed;
    // 图的具体数据
    private Vector<Integer>[] g;

    // 构造函数
    public SparseGraph( int n , boolean directed ){
        assert n >= 0;
        this.n = n;
        this.m = 0;
        this.directed = directed;
        // g初始化为n个空的vector, 表示每一个g[i]都为空, 即没有任和边
        g = (Vector<Integer>[])new Vector[n];
        for(int i = 0 ; i < n ; i ++)
            g[i] = new Vector<Integer>();
    }
    // 返回节点个数
    public int V(){ return n;}
    // 返回边的个数
    public int E(){ return m;}
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
}
```









	  AI 思考中...





			** [并查集路径压缩](https://www.runoob.com/union-find-compress.html)
			[相邻节点迭代器](https://www.runoob.com/graph-theory-iter.html) **













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