# 二分搜索树节点的查找

- Source: https://www.runoob.com/data-structures/binary-search-tree-search.html

二分搜索树没有下标, 所以针对二分搜索树的查找操作, 这里定义一个 contain 方法, 判断二分搜索树是否包含某个元素, 返回一个布尔型变量, 这个查找的操作一样是一个递归的过程, 具体代码实现如下:


```
...
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
...
```


以下实例在二分搜索树中寻找 43 元素


![](https://www.runoob.com/wp-content/uploads/2020/09/search-01.png)


**(1)** 元素 43 比根节点 42 大，需要在右子节点继续比较。


![](https://www.runoob.com/wp-content/uploads/2020/09/search-02.png)


**(2)** 元素 43 比 59 小，需要在左子节点继续比较。


![](https://www.runoob.com/wp-content/uploads/2020/09/search-03.png)

**(3)** 元素 43 比 51 小，需要在左子节点继续比较。

![](https://www.runoob.com/wp-content/uploads/2020/09/search-04.png)


**(4)** 查找 51 的左子节点 43，正好和相等，结束。


如果需要查找 key 对应的 value，代码如下所示:


```
...
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
...
```


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-BinarySearchTreeSearch.zip)


## src/runoob/binary/BinarySearchTreeSearch.java 文件代码：


```
package runoob.binary;

/**
 * 二分搜索树查找
 */
public class BinarySearchTreeSearch<Key extends Comparable<Key>, Value> {
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
    // 根节点
    private Node root;
    // 树种的节点个数
    private int count;

    // 构造函数, 默认构造一棵空二分搜索树
    public BinarySearchTreeSearch() {
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
}
```










	  AI 思考中...





			** [二分搜索树节点的插入](https://www.runoob.com/binary-search-tree-insert.html)
			[二分搜索树深度优先遍历](https://www.runoob.com/binary-search-traverse.html) **