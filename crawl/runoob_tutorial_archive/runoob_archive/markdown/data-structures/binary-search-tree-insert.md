# 二分搜索树节点的插入

- Source: https://www.runoob.com/data-structures/binary-search-tree-insert.html

首先定义一个二分搜索树，Java 代码表示如下:


```
public class BST<Key extends Comparable<Key>, Value> {

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
    public BST() {
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
}
```


Node 表示节点，count 代表节点的数量。


以下实例向如下二分搜索树中插入元素 61 的步骤：


![](https://www.runoob.com/wp-content/uploads/2020/09/insert-01.png)


（1）需要插入的元素 61 比 42 大，比较 42 的右子树根节点。


![](https://www.runoob.com/wp-content/uploads/2020/09/insert-02.png)


（2）61 比 59 大，所以需要把 61 移动到 59 右子树相应位置，而此时为空，直接插入作为 59 的右子节点。


![](https://www.runoob.com/wp-content/uploads/2020/09/insert-03.png)


插入操作也是一个递归过程，分三种情况，等于、大于、小于。


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-BinarySearchTreeInsert.zip)


## src/runoob/binary/BinarySearchTreeInsert.java 文件代码：


```
package runoob.binary;

/**
 * 二分搜索树插入新的元素
 */

public class BinarySearchTreeInsert<Key extends Comparable<Key>, Value> {

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
    public BinarySearchTreeInsert() {
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
    public void insert(Key key, Value value) {
        root = insert(root, key, value);
    }

    //核心代码---开始
    // 向以node为根的二分搜索树中, 插入节点(key, value), 使用递归算法
    // 返回插入新节点后的二分搜索树的根
    private Node insert(Node node, Key key, Value value) {
        if (node == null) {
            count++;
            return new Node(key, value);
        }
        if (key.compareTo(node.key) == 0)
            node.value = value;
        else if (key.compareTo(node.key) < 0)
            node.left = insert(node.left, key, value);
        else    // key > node->key
            node.right = insert(node.right, key, value);

        return node;
    }
    //核心代码---结束
}
```










	  AI 思考中...





			** [二分搜索树](https://www.runoob.com/binary-search-tree.html)
			[二分搜索树节点的查找](https://www.runoob.com/binary-search-tree-search.html) **