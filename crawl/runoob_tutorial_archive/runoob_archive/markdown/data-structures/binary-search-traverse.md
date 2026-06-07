# 二分搜索树深度优先遍历

- Source: https://www.runoob.com/data-structures/binary-search-traverse.html

二分搜索树遍历分为两大类，深度优先遍历和层序遍历。


深度优先遍历分为三种：先序遍历（preorder tree walk）、中序遍历（inorder tree walk）、后序遍历（postorder tree walk），分别为：


- **1、前序遍历：**先访问当前节点，再依次递归访问左右子树。
- **2、中序遍历**：先递归访问左子树，再访问自身，再递归访问右子树。
- **3、后序遍历**：先递归访问左右子树，再访问自身节点。


前序遍历结果图示：


![](https://www.runoob.com/wp-content/uploads/2020/09/traverse-01.png)


对应代码示例：


```
...
// 对以node为根的二叉搜索树进行前序遍历, 递归算法
private void preOrder(Node node){

    if( node != null ){
        System.out.println(node.key);
        preOrder(node.left);
        preOrder(node.right);
    }
}
...
```


中序遍历结果图示：


![](https://www.runoob.com/wp-content/uploads/2020/09/traverse-02.png)


对应代码示例：


```
...
// 对以node为根的二叉搜索树进行中序遍历, 递归算法
private void inOrder(Node node){

    if( node != null ){
        inOrder(node.left);
        System.out.println(node.key);
        inOrder(node.right);
    }
}
...
```


后序遍历结果图示：


![](https://www.runoob.com/wp-content/uploads/2020/09/traverse-03.png)


对应代码示例：


```
...
// 对以node为根的二叉搜索树进行后序遍历, 递归算法
private void postOrder(Node node){

    if( node != null ){
        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.key);
    }
}
...
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-Traverse.zip)


## src/runoob/binary/Traverse.java 文件代码：


```
package runoob.binary;

/**
 * 优先遍历
 */

public class Traverse<Key extends Comparable<Key>, Value>  {

    // 树中的节点为私有的类, 外界不需要了解二分搜索树节点的具体实现
    private class Node {
        private Key key;
        private Value value;
        private Node left, right;

        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
            left = right = null;
        }
    }

    private Node root;  // 根节点
    private int count;  // 树种的节点个数

    // 构造函数, 默认构造一棵空二分搜索树
    public Traverse() {
        root = null;
        count = 0;
    }

    // 返回二分搜索树的节点个数
    public int size() {
        return count;
    }

    // 返回二分搜索树是否为空
    public boolean isEmpty() {
        return count == 0;
    }

    // 向二分搜索树中插入一个新的(key, value)数据对
    public void insert(Key key, Value value){
        root = insert(root, key, value);
    }

    // 查看二分搜索树中是否存在键key
    public boolean contain(Key key){
        return contain(root, key);
    }

    // 在二分搜索树中搜索键key所对应的值。如果这个值不存在, 则返回null
    public Value search(Key key){
        return search( root , key );
    }

    // 二分搜索树的前序遍历
    public void preOrder(){
        preOrder(root);
    }

    // 二分搜索树的中序遍历
    public void inOrder(){
        inOrder(root);
    }

    // 二分搜索树的后序遍历
    public void postOrder(){
        postOrder(root);
    }

    //********************
    //* 二分搜索树的辅助函数
    //********************

    // 向以node为根的二分搜索树中, 插入节点(key, value), 使用递归算法
    // 返回插入新节点后的二分搜索树的根
    private Node insert(Node node, Key key, Value value){

        if( node == null ){
            count ++;
            return new Node(key, value);
        }

        if( key.compareTo(node.key) == 0 )
            node.value = value;
        else if( key.compareTo(node.key) < 0 )
            node.left = insert( node.left , key, value);
        else    // key > node->key
            node.right = insert( node.right, key, value);

        return node;
    }

    // 查看以node为根的二分搜索树中是否包含键值为key的节点, 使用递归算法
    private boolean contain(Node node, Key key){

        if( node == null )
            return false;

        if( key.compareTo(node.key) == 0 )
            return true;
        else if( key.compareTo(node.key) < 0 )
            return contain( node.left , key );
        else // key > node->key
            return contain( node.right , key );
    }

    // 在以node为根的二分搜索树中查找key所对应的value, 递归算法
    // 若value不存在, 则返回NULL
    private Value search(Node node, Key key){

        if( node == null )
            return null;

        if( key.compareTo(node.key) == 0 )
            return node.value;
        else if( key.compareTo(node.key) < 0 )
            return search( node.left , key );
        else // key > node->key
            return search( node.right, key );
    }

    // 对以node为根的二叉搜索树进行前序遍历, 递归算法
    private void preOrder(Node node){

        if( node != null ){
            System.out.println(node.key);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    // 对以node为根的二叉搜索树进行中序遍历, 递归算法
    private void inOrder(Node node){

        if( node != null ){
            inOrder(node.left);
            System.out.println(node.key);
            inOrder(node.right);
        }
    }

    // 对以node为根的二叉搜索树进行后序遍历, 递归算法
    private void postOrder(Node node){

        if( node != null ){
            postOrder(node.left);
            postOrder(node.right);
            System.out.println(node.key);
        }
    }
}
```









	  AI 思考中...





			** [二分搜索树节点的查找](https://www.runoob.com/binary-search-tree-search.html)
			[二分搜索树层序遍历](https://www.runoob.com/binary-search-level-traverse.html) **













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