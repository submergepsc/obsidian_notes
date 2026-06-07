# 分治算法

- Source: https://www.runoob.com/data-structures/dsa-divide-and-conquer.html

分治法（英语：Divide and conquer）是建基于多项分支递归的一种很重要的算法范型，字面上的解释是"分而治之"，就是把一个复杂的问题分成两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。


简单来说，分治就是三个步骤：**分解 -> 解决 -> 合并**。


**
想象一下，你面前有一大堆积木需要按颜色分类。如果直接动手，可能会眼花缭乱。一个更聪明的办法是：先把这堆积木分成两小堆，然后分别对这两小堆进行分类，最后把分好类的两小堆合并起来。这个 "分而治之"** 的过程，就是分治算法的核心思想。


**分治算法**就像是一个聪明的团队领导解决大问题的方法：


- **分解（Divide）**：将大问题拆分成若干个相同类型的小问题
- **解决（Conquer）**：递归地解决这些小问题
- **合并（Combine）**：将小问题的解合并成原问题的解


**现实案例：**


- **公司管理**：CEO→部门经理→团队主管→普通员工
- **军队指挥**：司令→军长→师长→团长→连长
- **图书整理**：先按大类分，再按小类分，最后按字母排序
- **寻宝游戏**：将大地图分成小块，逐块搜索


| 问题特征 | 其他方法 | 分治方法 |
| --- | --- | --- |
| 大规模数据 | 可能效率低下 | 分解后并行处理 |
| 复杂结构 | 难以直接解决 | 简化子问题 |
| 可递归定义 | 需要复杂逻辑 | 天然适合递归 |
| 独立子问题 | 难以并行化 | 完美支持并行 |


---


## 核心思想与步骤


分治算法通常遵循一个清晰的三步框架，我们可以用下面的流程图来直观理解：


![](https://www.runoob.com/wp-content/uploads/2025/12/a919a147-6e3f-46fc-93ff-a690ca10496e.png) **上图说明**：算法首先判断当前问题是否简单到可以直接求解。如果是，则直接求解并返回结果；如果不是，则将其分解为若干子问题，递归求解每个子问题，最后将子问题的结果合并，得到最终答案。


具体来说，这三个步骤是：


- **分解**：将原问题分解成若干个规模较小、相互独立、且与原问题形式相同的子问题。
- **解决**：递归地求解各个子问题。如果子问题规模足够小，则直接求解。
- **合并**：将各个子问题的解合并，形成原问题的解。


---


## 分治算法的经典应用


为了让你更好地理解分治算法是如何工作的，我们来看两个最经典的例子。


### 应用一：归并排序


归并排序是分治思想的完美体现，其目标是**将一个无序数组排序成有序数组**。


**算法步骤：**


- **分解**：将当前数组从中间位置分成左右两个子数组。
- **解决**：递归地对左子数组和右子数组进行归并排序。
- **合并**：将两个已经排序好的有序子数组合并成一个新的有序数组。


**代码示例：**


## 实例


```
def merge_sort(arr):
    """
    归并排序主函数
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    # 1. 解决：如果数组长度为0或1，直接返回（基线条件）
    if len(arr) <= 1:
        return arr

    # 2. 分解：找到中间点，分割数组
    mid = len(arr) // 2
    left_half = arr[:mid]   # 左子数组
    right_half = arr[mid:]  # 右子数组

    # 3. 解决：递归排序左右子数组
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 4. 合并：将两个有序数组合并
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    合并两个有序列表
    :param left: 有序列表A
    :param right: 有序列表B
    :return: 合并后的有序列表
    """
    merged = []  # 用于存放合并结果的列表
    i = j = 0    # i和j分别是指向left和right的指针

    # 比较两个列表的头部，将较小的元素放入merged
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 将剩余的元素（如果有）直接添加到merged末尾
    # 因为left和right本身已有序，所以剩余部分也是有序的
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# 测试数据
test_array = [38, 27, 43, 3, 9, 82, 10]
print("原始数组:", test_array)
sorted_array = merge_sort(test_array)
print("排序后数组:", sorted_array)
# 输出：原始数组: [38, 27, 43, 3, 9, 82, 10]
# 输出：排序后数组: [3, 9, 10, 27, 38, 43, 82]
```


### 应用二：二分查找


二分查找用于在**一个已排序的数组**中快速定位目标值。它不断将搜索范围对半分解，是分治策略的简化版（通常只处理一个子问题，无需合并）。


**算法步骤：**


- **分解**：找到数组的中间元素。
- **解决**： - 如果中间元素等于目标值，查找成功。 - 如果目标值小于中间元素，则在左半部分递归查找。 - 如果目标值大于中间元素，则在右半部分递归查找。
- **合并**：二分查找通常不需要合并步骤，因为找到目标值后直接返回其位置即可。


**代码示例：**


## 实例


```
def binary_search(arr, target, low, high):
    """
    二分查找（递归版本）
    :param arr: 已排序的列表
    :param target: 要查找的目标值
    :param low: 当前查找范围的起始索引
    :param high: 当前查找范围的结束索引
    :return: 目标值的索引，如果未找到则返回 -1
    """
    # 基线条件：搜索范围无效，说明未找到目标
    if low > high:
        return -1

    # 分解：计算中间索引
    mid = (low + high) // 2

    # 解决：判断并递归
    if arr[mid] == target:
        return mid  # 找到目标，返回索引
    elif target < arr[mid]:
        # 目标在左半部分，递归查找左半部分
        return binary_search(arr, target, low, mid - 1)
    else:
        # 目标在右半部分，递归查找右半部分
        return binary_search(arr, target, mid + 1, high)

# 测试数据（必须是已排序的！）
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(sorted_list, target_value, 0, len(sorted_list) - 1)

if result != -1:
    print(f"目标值 {target_value} 在数组中的索引是: {result}")
else:
    print(f"目标值 {target_value} 不在数组中。")
# 输出：目标值 23 在数组中的索引是: 5
```


---


## 分治算法的特点与复杂度分析


### 算法特点


| 特点 | 说明 |
| --- | --- |
| 问题可分解 | 原问题必须能够被分解为规模更小的相似子问题。 |
| 子问题独立 | 子问题之间最好相互独立，这样求解和合并会更简单。 |
| 有终止条件 | 必须存在一个简单的基线条件，当问题规模足够小时可以直接求解。 |
| 解可合并 | 必须能有效地将子问题的解合并为原问题的解。 |


### 时间复杂度分析


分治算法的时间复杂度通常可以用 **主定理** 来分析，其递归关系一般形式为： $$ T(n) = aT(\frac{n}{b}) + f(n) $$ 其中：


- `n` 是问题规模。
- `a` 是分解出的子问题个数。
- `n/b` 是每个子问题的规模。
- `f(n)` 是分解和合并步骤所花费的时间。


例如，对于归并排序：


- `a = 2`（分成两个子数组）
- `b = 2`（每个子数组规模减半）
- `f(n) = O(n)`（合并两个有序数组需要线性时间）
- 根据主定理，其时间复杂度为 **O(n log n)**。


---


## 实践练习


现在，是时候动手巩固你对分治算法的理解了。请尝试完成以下练习：


**练习 1：实现快速排序** 快速排序是另一个经典的分治算法。它的思路是：


- **分解**：选择一个"基准"元素，将数组重新排列，所有比基准小的放在左边，比基准大的放在右边（分区操作）。
- **解决**：递归地对基准左右两边的子数组进行快速排序。
- **合并**：不需要显式合并，因为分区操作后数组已经部分有序。


**你的任务**：根据以上描述，尝试编写快速排序的 Python 代码。


**练习 2：寻找数组中的最大子数组和** 问题：给定一个整数数组（可能包含负数），找到一个具有最大和的连续子数组。 例如，对于 `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`，最大子数组是 `[4, -1, 2, 1]`，其和为 `6`。


**提示（分治思路）**：


- 将数组从中间分成左右两半。
- 最大子数组和可能出现在：**左半部分**、**右半部分**、或者**横跨中间点**。
- 递归求解左半部分和右半部分的最大子数组和。
- 计算横跨中间点的最大子数组和（需要从中间点向左、向右分别累加求最大）。
- 返回三者中的最大值。


尝试用分治策略解决这个问题。









	  AI 思考中...





			** [图论结构](https://www.runoob.com/dsa-graph.html)
			[贪心算法](https://www.runoob.com/dsa-greedy-algorithm.html) **













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