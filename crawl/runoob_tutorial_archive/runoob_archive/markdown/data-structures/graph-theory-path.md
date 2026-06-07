# 寻路算法

- Source: https://www.runoob.com/data-structures/graph-theory-path.html

图的寻路算法也可以通过深度优先遍历 dfs 实现，寻找图 graph 从起始 s 点到其他点的路径，在上一小节的实现类中添加全局变量 from数组记录路径，from[i] 表示查找的路径上i的上一个节点。


首先构造函数初始化寻路算法的初始条件，**from = new int[G.V()]** 和 **from = new int[G.V()]**，并在循环中设置默认值，visited 数组全部为false，from 数组全部为 -1 值，后面对起始节点进行 dfs 的递归处理。


```
...
// 构造函数, 寻路算法, 寻找图graph从s点到其他点的路径
public Path(Graph graph, int s){
    // 算法初始化
    G = graph;
    assert s >= 0 && s < G.V();
    visited = new boolean[G.V()];
    from = new int[G.V()];
    for( int i = 0 ; i < G.V() ; i ++ ){
        visited[i] = false;
        from[i] = -1;
    }
    this.s = s;
    // 寻路算法
    dfs(s);
}
...
```


那么判断 s 点到 w 点是否有路径，只要查询 visited 对应数组值即可。


```
...
boolean hasPath(int w){
    assert w >= 0 && w < G.V();
    return visited[w];
}
...
```


获取 s 点到 w 点的具体路径，我们用 path 方法来实现，先判断是否连通，可调用 hasPath 方法，由构造函数可知只需通过 from 数组往上追溯就能找到所有的路径。


```
...
Vector<Integer> path(int w){
    assert hasPath(w) ;
    Stack<Integer> s = new Stack<Integer>();
    // 通过from数组逆向查找到从s到w的路径, 存放到栈中
    int p = w;
    while( p != -1 ){
        s.push(p);
        p = from[p];
    }
    // 从栈中依次取出元素, 获得顺序的从s到w的路径
    Vector<Integer> res = new Vector<Integer>();
    while( !s.empty() )
        res.add( s.pop() );
    return res;
}
...
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-Graph-Theory.zip)


## src/runoob/graph/Path.java 文件代码：


```
package runoob.graph;

import runoob.graph.read.Graph;

import java.util.Stack;
import java.util.Vector;

/**
 * 寻路
 */
public class Path {
    // 图的引用
    private Graph G;
    // 起始点
    private int s;
    // 记录dfs的过程中节点是否被访问
    private boolean[] visited;
    // 记录路径, from[i]表示查找的路径上i的上一个节点
    private int[] from;

    // 图的深度优先遍历
    private void dfs( int v ){
        visited[v] = true;
        for( int i : G.adj(v) )
            if( !visited[i] ){
                from[i] = v;
                dfs(i);
            }
    }

    // 构造函数, 寻路算法, 寻找图graph从s点到其他点的路径
    public Path(Graph graph, int s){
        // 算法初始化
        G = graph;
        assert s >= 0 && s < G.V();
        visited = new boolean[G.V()];
        from = new int[G.V()];
        for( int i = 0 ; i < G.V() ; i ++ ){
            visited[i] = false;
            from[i] = -1;
        }
        this.s = s;
        // 寻路算法
        dfs(s);
    }

    // 查询从s点到w点是否有路径
    boolean hasPath(int w){
        assert w >= 0 && w < G.V();
        return visited[w];
    }

    // 查询从s点到w点的路径, 存放在vec中
    Vector<Integer> path(int w){

        assert hasPath(w) ;

        Stack<Integer> s = new Stack<Integer>();
        // 通过from数组逆向查找到从s到w的路径, 存放到栈中
        int p = w;
        while( p != -1 ){
            s.push(p);
            p = from[p];
        }

        // 从栈中依次取出元素, 获得顺序的从s到w的路径
        Vector<Integer> res = new Vector<Integer>();
        while( !s.empty() )
            res.add( s.pop() );

        return res;
    }

    // 打印出从s点到w点的路径
    void showPath(int w){

        assert hasPath(w) ;

        Vector<Integer> vec = path(w);
        for( int i = 0 ; i < vec.size() ; i ++ ){
            System.out.print(vec.elementAt(i));
            if( i == vec.size() - 1 )
                System.out.println();
            else
                System.out.print(" -> ");
        }
    }
}
```









	  AI 思考中...





			** [深度优先遍历与连通分量](https://www.runoob.com/graph-theory-deep.html)
			[广度优先遍历与最短路径](https://www.runoob.com/graph-theory-short-path.html) **













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