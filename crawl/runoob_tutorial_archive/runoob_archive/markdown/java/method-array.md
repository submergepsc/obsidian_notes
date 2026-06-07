# Java 实例 - 输出数组元素

- Source: https://www.runoob.com/java/method-array.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过重载 MainClass 类的 printArray 方法输出不同类型(整型, 双精度及字符型)的数组：


## MainClass.java 文件



```java
public class MainClass {
    public static void printArray(Integer[] inputArray) {
        for (Integer element : inputArray){
            System.out.printf("%s ", element);
            System.out.println();
        }
    }
    public static void printArray(Double[] inputArray) {
        for (Double element : inputArray){
            System.out.printf("%s ", element);
            System.out.println();
        }
    }
    public static void printArray(Character[] inputArray) {
        for (Character element : inputArray){
            System.out.printf("%s ", element);
            System.out.println();
        }
    }
    public static void main(String args[]) {
        Integer[] integerArray = { 1, 2, 3, 4, 5, 6 };
        Double[] doubleArray = { 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7 };
        Character[] characterArray = { 'H', 'E', 'L', 'L', 'O' };
        System.out.println("输出整型数组:");
        printArray(integerArray);
        System.out.println("\n输出双精度型数组:");
        printArray(doubleArray);
        System.out.println("\n输出字符型数组:");
        printArray(characterArray);
    }
}
```


以上代码运行输出结果为：


```
输出整型数组:
1
2
3
4
5
6

输出双精度型数组:
1.1
2.2
3.3
4.4
5.5
6.6
7.7

输出字符型数组:
H
E
L
L
O
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 方法重载](https://www.runoob.com/method-overloading.html)
			[Java 实例 – 汉诺塔算法](https://www.runoob.com/method-tower.html) **