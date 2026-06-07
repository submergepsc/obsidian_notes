# Java 实例 - 查找数组中的重复元素

- Source: https://www.runoob.com/java/arrays-compare.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何在 java 中找到重复的元素：


## Main.java 文件



```java
public class MainClass {
    public static void main(String[] args)
    {
        int[] my_array = {1, 2, 5, 5, 6, 6, 7, 2, 9, 2};
        findDupicateInArray(my_array);

    }

    public static void findDupicateInArray(int[] a) {
        int count=0;
        for(int j=0;j<a.length;j++) {
            for(int k =j+1;k<a.length;k++) {
                if(a[j]==a[k]) {
                    count++;
                }
            }
            if(count==1)
               System.out.println( "重复元素 : " +  a[j] );
            count = 0;
        }
    }
}
```


以上代码运行输出结果为：


```
重复元素 : 5
重复元素 : 6
重复元素 : 2
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 数组扩容](https://www.runoob.com/arrays-extension.html)
			[Java 实例 – 删除数组元素](https://www.runoob.com/arrays-remove.html) **