# 并查集快速查找

- Source: https://www.runoob.com/data-structures/union-find-quick.html

本小节基于上一小节并查集的结构介绍基础操作，查询和合并和判断是否连接。


查询元素所在的集合编号，直接返回 **id** 数组值，**O(1)** 的时间复杂度。


```
...
private int find(int p) {
    assert p >= 0 && p < count;
    return id[p];
}
...
```


合并元素 **p** 和元素 **q** 所属的集合， 合并过程需要遍历一遍所有元素, 再将两个元素的所属集合编号合并，这个过程是 **O(n)** 复杂度。


```
...
public void unionElements(int p, int q) {
    int pID = find(p);
    int qID = find(q);
    if (pID == qID)
        return;
    for (int i = 0; i < count; i++)
        if (id[i] == pID)
            id[i] = qID;
}
...
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/10/runoob-algorithm-union.zip)


## UnionFind1.java 文件代码：


```
package runoob.union;

/**
 * 第一版union-Find
 */
public class UnionFind1 {
    // 我们的第一版Union-Find本质就是一个数组
    private int[] id;
    // 数据个数
    private int count;

    public UnionFind1(int n) {
        count = n;
        id = new int[n];
        // 初始化, 每一个id[i]指向自己, 没有合并的元素
        for (int i = 0; i < n; i++)
            id[i] = i;
    }

    // 查找过程, 查找元素p所对应的集合编号
    private int find(int p) {
        assert p >= 0 && p < count;
        return id[p];
    }

    // 查看元素p和元素q是否所属一个集合
    // O(1)复杂度
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }

    // 合并元素p和元素q所属的集合
    // O(n) 复杂度
    public void unionElements(int p, int q) {

        int pID = find(p);
        int qID = find(q);

        if (pID == qID)
            return;

        // 合并过程需要遍历一遍所有元素, 将两个元素的所属集合编号合并
        for (int i = 0; i < count; i++)
            if (id[i] == pID)
                id[i] = qID;
    }
}
```









	  AI 思考中...





			** [并查集基础](https://www.runoob.com/union-find-basic.html)
			[并查集快速合并](https://www.runoob.com/union-find-quick-merge.html) **













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