# 深度优先遍历与连通分量

- Source: https://www.runoob.com/data-structures/graph-theory-deep.html

深度优先遍历(Depth First Search)的主要思想是首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点。当没有未访问过的顶点时，则回到上一个顶点，继续试探别的顶点，直至所有的顶点都被访问过。


下图示例的图从 0 开始遍历顺序如右图所示：


![](https://www.runoob.com/wp-content/uploads/2020/10/deep-01.png)


无向图 G 的一个极大连通子图称为 G 的一个连通分量（或连通分支）。连通图只有一个连通分量，即其自身；非连通的无向图有多个连通分量。连通分量与连通分量之间没有任何边相连。深度优先遍历可以用来求连通分量。


下面以求连通分量为例，来实现图的深度优先遍历，称为 dfs。下面代码片段中，visited 数组记录 dfs 的过程中节点是否被访问，ccount 记录联通分量个数，id 数组代表每个节点所对应的联通分量标记，两个节点拥有相同的 id 值代表属于同一联通分量。


```
...
// 构造函数, 求出无权图的联通分量
public Components(Graph graph){
    // 算法初始化
    G = graph;
    visited = new boolean[G.V()];
    id = new int[G.V()];
    ccount = 0;
    for( int i = 0 ; i < G.V() ; i ++ ){
        visited[i] = false;
        id[i] = -1;
    }
    // 求图的联通分量
    for( int i = 0 ; i < G.V() ; i ++ )
        if( !visited[i] ){
            dfs(i);
            ccount ++;
        }
}
...
```


图的深度优先遍历是个递归过程，实现代码：


```
...
// 图的深度优先遍历
void dfs( int v ){

    visited[v] = true;
    id[v] = ccount;

    for( int i: G.adj(v) ){
        if( !visited[i] )
            dfs(i);
    }
}
...
```




### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-Graph-Theory.zip)


## src/runoob/graph/Components.java 文件代码：


```
package runoob.graph;

import runoob.graph.read.Graph;

/**
 * 深度优先遍历
 */
public class Components {

    Graph G;                    // 图的引用
    private boolean[] visited;  // 记录dfs的过程中节点是否被访问
    private int ccount;         // 记录联通分量个数
    private int[] id;           // 每个节点所对应的联通分量标记

    // 图的深度优先遍历
    void dfs( int v ){

        visited[v] = true;
        id[v] = ccount;

        for( int i: G.adj(v) ){
            if( !visited[i] )
                dfs(i);
        }
    }

    // 构造函数, 求出无权图的联通分量
    public Components(Graph graph){

        // 算法初始化
        G = graph;
        visited = new boolean[G.V()];
        id = new int[G.V()];
        ccount = 0;
        for( int i = 0 ; i < G.V() ; i ++ ){
            visited[i] = false;
            id[i] = -1;
        }

        // 求图的联通分量
        for( int i = 0 ; i < G.V() ; i ++ )
            if( !visited[i] ){
                dfs(i);
                ccount ++;
            }
    }

    // 返回图的联通分量个数
    int count(){
        return ccount;
    }

    // 查询点v和点w是否联通
    boolean isConnected( int v , int w ){
        assert v >= 0 && v < G.V();
        assert w >= 0 && w < G.V();
        return id[v] == id[w];
    }
}
```









	  AI 思考中...





			** [相邻节点迭代器](https://www.runoob.com/graph-theory-iter.html)
			[寻路算法](https://www.runoob.com/graph-theory-path.html) **













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