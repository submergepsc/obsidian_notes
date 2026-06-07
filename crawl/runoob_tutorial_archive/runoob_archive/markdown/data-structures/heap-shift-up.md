# 堆的 shift up

- Source: https://www.runoob.com/data-structures/heap-shift-up.html

本小节介绍如何向一个最大堆中添加元素，称为 **shift up**。

假设我们对下面的最大堆新加入一个元素52，放在数组的最后一位，52大于父节点16，此时不满足堆的定义，需要进行调整。


![](https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-01.png)



首先交换索引为 5 和 11 数组中数值的位置，也就是 52 和 16 交换位置。


![](https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-02.png)


此时 52 依然比父节点索引为 2 的数值 41 大，我们还需要进一步挪位置。


![](https://www.runoob.com/wp-content/uploads/2020/09/shiftUp-03.png)

这时比较 52 和 62 的大小，52 已经比父节点小了，不需要再上升了，满足最大堆的定义。我们称这个过程为最大堆的 shift up。


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-HeapShiftUp.zip)


## src/runoob/heap/HeapShiftUp.java 文件代码：


```
package runoob.heap;

/**
 * 往堆中添加一元素
 */
public class HeapShiftUp<T extends Comparable> {

    protected T[] data;
    protected int count;
    protected int capacity;

    // 构造函数, 构造一个空堆, 可容纳capacity个元素
    public HeapShiftUp(int capacity){
        data = (T[])new Comparable[capacity+1];
        count = 0;
        this.capacity = capacity;
    }
    // 返回堆中的元素个数
    public int size(){
        return count;
    }

    // 返回一个布尔值, 表示堆中是否为空
    public boolean isEmpty(){
        return count == 0;
    }
    // 像最大堆中插入一个新的元素 item
    public void insert(T item){
        assert count + 1 <= capacity;
        data[count+1] = item;
        count ++;
        shiftUp(count);
    }
    // 交换堆中索引为i和j的两个元素
    private void swap(int i, int j){
        T t = data[i];
        data[i] = data[j];
        data[j] = t;
    }

    //********************
    //* 最大堆核心辅助函数
    //********************
    private void shiftUp(int k){

        while( k > 1 && data[k/2].compareTo(data[k]) < 0 ){
            swap(k, k/2);
            k /= 2;
        }
    }

    // 测试 HeapShiftUp
    public static void main(String[] args) {
        HeapShiftUp<Integer> heapShiftUp = new HeapShiftUp<Integer>(100);
        int N = 50; // 堆中元素个数
        int M = 100; // 堆中元素取值范围[0, M)
        for( int i = 0 ; i < N ; i ++ )
            heapShiftUp.insert( new Integer((int)(Math.random() * M)) );
        System.out.println(heapShiftUp.size());

    }
}
```









	  AI 思考中...





			** [堆的基本存储](https://www.runoob.com/heap-storage.html)
			[堆的 shift down](https://www.runoob.com/heap-shift-down.html) **













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