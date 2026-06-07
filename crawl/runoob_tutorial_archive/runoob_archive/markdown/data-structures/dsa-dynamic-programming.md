# 动态规划

- Source: https://www.runoob.com/data-structures/dsa-dynamic-programming.html

动态规划（英语：Dynamic programming，简称 DP）是一种在数学、管理科学、计算机科学、经济学和生物信息学中使用的，通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。


**
想象一下，你正在爬一个 `n` 级的楼梯。每次你可以爬 `1` 级或 `2` 级台阶。

那么，爬到楼顶总共有多少种不同的方法呢？


如果你从最顶层的目标（第 `n` 级）开始想，可能会觉得复杂。

但如果我们换个思路：要到达第 `n` 级台阶，你只能从第 `n-1` 级跨一步上来，或者从第 `n-2` 级跨两步上来**。所以，到达第 `n` 级的方法数，就等于到达第 `n-1` 级的方法数加上到达第 `n-2` 级的方法数。


这种**将一个大问题分解为若干个重叠的子问题，并通过保存子问题的解来避免重复计算，从而高效解决原问题**的方法，就是动态规划（Dynamic Programming，简称 DP）。


### 核心思想


动态规划的核心是 **记住求过的解** 。

动态规划通常用于解决具有以下性质的问题：


- **重叠子问题**：在递归求解过程中，同一个子问题会被多次计算。
- **最优子结构**：一个问题的最优解包含其子问题的最优解。


我们可以用一个简单的流程图来理解动态规划的解题思路：


[![](https://www.runoob.com/wp-content/uploads/2025/12/0c933768-2609-4d8a-95b1-adab861d8b9f.png)](https://www.runoob.com/wp-content/uploads/2025/12/0c933768-2609-4d8a-95b1-adab861d8b9f.png)


上图展示了解决一个动态规划问题的典型步骤：从定义问题开始，通过分析找到子问题结构，然后用状态和状态转移方程将其形式化，最后通过明确的初始条件和计算顺序得到答案。


---


## 从递归到动态规划：爬楼梯问题


让我们用经典的 **"爬楼梯"** 问题来感受从递归到动态规划的优化过程。


### 问题描述


假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶？


### 方法一：暴力递归（低效）


根据开头的分析，我们可以直接写出递归公式： `f(n) = f(n-1) + f(n-2)` 其中， `f(1) = 1`, `f(2) = 2`。


## 实例


```
def climb_stairs_recursive(n: int) -> int:
    """递归解法"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

# 测试
print(f"爬到第 5 级台阶的方法数（递归）: {climb_stairs_recursive(5)}")  # 输出: 8
```


**缺点分析**：这种递归存在大量的重复计算。例如，计算 `f(5)` 需要 `f(4)` 和 `f(3)`，计算 `f(4)` 又需要 `f(3)` 和 `f(2)`，这里的 `f(3)` 就被计算了两次。当 `n` 很大时，时间复杂度是指数级的 `O(2^n)`，效率极低。


### 方法二：带备忘录的递归（自顶向下）


我们可以用一个数组（"备忘录"）来存储已经计算过的结果，避免重复计算。


## 实例


```
def climb_stairs_memo(n: int) -> int:
    """带备忘录的递归（自顶向下）"""
    # 初始化备忘录，-1 表示未计算
    memo = [-1] * (n + 1)

    def helper(x: int) -> int:
        # 基础情况
        if x == 1:
            return 1
        if x == 2:
            return 2
        # 如果已经计算过，直接返回结果
        if memo[x] != -1:
            return memo[x]
        # 否则，计算并存入备忘录
        memo[x] = helper(x - 1) + helper(x - 2)
        return memo[x]

    return helper(n)

print(f"爬到第 5 级台阶的方法数（备忘录）: {climb_stairs_memo(5)}")  # 输出: 8
```


这种方法的时间复杂度降到了 `O(n)`，因为每个子问题只计算一次。空间复杂度为 `O(n)`。这已经是一种动态规划思想，称为 **"自顶向下"** 或 **"记忆化搜索"**。


### 方法三：递推数组（自底向上，标准DP）


我们直接从最小的子问题开始，一步步递推到原问题。通常用一个数组 `dp` 来存储状态。


## 实例


```
def climb_stairs_dp(n: int) -> int:
    """动态规划（自底向上）"""
    if n <= 2:
        return n
    # 1. 定义状态数组：dp[i] 表示爬到第 i 级台阶的方法数
    dp = [0] * (n + 1)
    # 2. 确定初始条件
    dp[1] = 1
    dp[2] = 2
    # 3. 状态转移：根据状态转移方程递推
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # 4. 返回最终结果
    return dp[n]

print(f"爬到第 5 级台阶的方法数（DP）: {climb_stairs_dp(5)}")  # 输出: 8
```


### 方法四：空间优化（滚动数组）


观察状态转移方程 `dp[i] = dp[i-1] + dp[i-2]`，我们发现当前状态只依赖于前两个状态。因此，我们不需要保存整个 `dp` 数组，只用两个变量滚动更新即可。


## 实例


```
def climb_stairs_optimized(n: int) -> int:
    """动态规划（空间优化版）"""
    if n <= 2:
        return n
    # 只用两个变量代表 dp[i-1] 和 dp[i-2]
    prev, curr = 1, 2  # 对应 dp[1], dp[2]
    for i in range(3, n + 1):
        # 计算新的当前值
        new_curr = prev + curr
        # 滚动更新变量，为下一轮循环做准备
        prev, curr = curr, new_curr
    return curr

print(f"爬到第 5 级台阶的方法数（优化DP）: {climb_stairs_optimized(5)}")  # 输出: 8
```


优化后，空间复杂度从 `O(n)` 降到了 `O(1)`。


---


## 动态规划解题框架


通过爬楼梯问题，我们可以总结出解决动态规划问题的通用四步曲：


### 步骤 1: 定义状态


用一个或多个数组（通常叫 `dp`）来表示子问题的解。关键是弄清楚 `dp[i]` 或者 `dp[i][j]` 代表什么含义。

**

在爬楼梯问题中，我们定义 `dp[i]` 为"爬到第 `i` 级台阶的方法总数"。


### 步骤 2: 确定状态转移方程


找出 `dp[i]` 与之前状态（如 `dp[i-1]`, `dp[i-2]`）之间的关系。这是动态规划的核心和难点。


> 在爬楼梯问题中，状态转移方程为： `dp[i] = dp[i-1] + dp[i-2]`。


### 步骤 3: 确定初始条件（Base Case）


最小的、不可再分的子问题的解。这是递推的起点，必须手动定义。


> 在爬楼梯问题中，初始条件为： `dp[1] = 1`, `dp[2] = 2`。


### 步骤 4: 确定计算顺序并计算


确定是"自顶向下"（记忆化递归）还是"自底向上"（循环递推），并确保在计算 `dp[i]` 时，它所依赖的子问题都已经被计算过了。


> 在爬楼梯问题中，我们采用自底向上，从 `i=3` 循环到 `i=n`。


---


## 经典案例：斐波那契数列


斐波那契数列是动态规划最直接的例子，其定义本身就是状态转移方程。


问题**：求斐波那契数列的第 `n` 项。 `F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) (n>=2)`


## 实例


```
def fibonacci(n: int) -> int:
    """动态规划求斐波那契数"""
    if n < 2:
        return n
    # 空间优化写法
    prev, curr = 0, 1  # F(0), F(1)
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# 测试数据
test_n = 10
print(f"斐波那契数列第 {test_n} 项是: {fibonacci(test_n)}")  # 输出: 55
```


---


## 进阶案例：零钱兑换


这是一个更典型的、展示最优子结构的问题。


**问题描述**：给你一个整数数组 `coins`，表示不同面额的硬币，以及一个整数 `amount`，表示总金额。计算并返回可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 `-1`。你可以认为每种硬币的数量是无限的。


### 问题分析与 DP 设计


- **定义状态**：`dp[i]` 表示凑成总金额 `i` 所需的最少硬币个数。
- **状态转移方程**：对于金额 `i`，我们可以遍历每一种面额的硬币 `coin`。如果 `coin  nums[j]`，则 `dp[i] = max(dp[i], dp[j] + 1)`。
- 初始时，每个 `dp[i]` 至少为 1（只包含自身）。









	  AI 思考中...





			** [贪心算法](https://www.runoob.com/dsa-greedy-algorithm.html)
			[高级树结构](https://www.runoob.com/dsa-advanced-tree.html) **













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