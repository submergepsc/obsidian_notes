# Java 实例 - 队列（Queue）用法

- Source: https://www.runoob.com/java/data-queue.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


队列是一种特殊的线性表，它只允许在表的前端进行删除操作，而在表的后端进行插入操作。


LinkedList类实现了Queue接口，因此我们可以把LinkedList当成Queue来用。


以下实例演示了队列（Queue）的用法：


## Main.java 文件



```java
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        //add()和remove()方法在失败的时候会抛出异常(不推荐)
        Queue<String> queue = new LinkedList<String>();
        //添加元素
        queue.offer("a");
        queue.offer("b");
        queue.offer("c");
        queue.offer("d");
        queue.offer("e");
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("poll="+queue.poll()); //返回第一个元素，并在队列中删除
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("element="+queue.element()); //返回第一个元素
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("peek="+queue.peek()); //返回第一个元素
        for(String q : queue){
            System.out.println(q);
        }
    }
}
```


以上代码运行输出结果为：


```
a
b
c
d
e
===
poll=a
b
c
d
e
===
element=b
b
c
d
e
===
peek=b
b
c
d
e
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 利用堆栈将中缀表达式转换成后缀表达式](https://www.runoob.com/data-intopost.html)
			[Java 实例 – 压栈出栈的方法实现字符串反转](https://www.runoob.com/data-reverse.html) **