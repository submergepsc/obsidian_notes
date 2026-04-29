# 在一台机器上规划任务 - OI Wiki

- Source: https://oi-wiki.org/misc/job-order/

# 在一台机器上规划任务

你有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个任务，要求你找到一个代价最小的顺序执行他们．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个任务花费的时间是 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个任务等待 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间会花费 𝑓𝑖(𝑡)fi(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的代价．

形式化地说，给出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个函数 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求一个排列 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最小化

𝐹(𝑝)=𝑛∑𝑖=1𝑓𝑝𝑖(𝑖−1∑𝑗=1𝑡𝑝𝑗)F(p)=∑i=1nfpi(∑j=1i−1tpj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 特殊的代价函数

### 线性代价函数

首先我们考虑所有的函数是线性的函数，即 𝑓𝑖(𝑥) =𝑐𝑖𝑥 +𝑑𝑖fi(x)=cix+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是非负整数．显然我们可以事先把常数项加起来，因此函数就转化为了 𝑓𝑖(𝑥) =𝑐𝑖𝑥fi(x)=cix![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式．

考虑两个排列 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝′p′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝′p′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是把 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置上的数和 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置上的数交换得到的排列．则

𝐹(𝑝′)−𝐹(𝑝)=𝑐𝑝′𝑖𝑖−1∑𝑗=1𝑡𝑝′𝑗+𝑐𝑝′𝑖+1𝑖∑𝑗=1𝑡𝑝′𝑗−(𝑐𝑝𝑖𝑖−1∑𝑗=1𝑡𝑝𝑗+𝑐𝑝𝑖+1𝑖∑𝑗=1𝑡𝑝𝑗)=𝑐𝑝𝑖𝑡𝑝𝑖+1−𝑐𝑝𝑖+1𝑡𝑝𝑖F(p′)−F(p)=cpi′∑j=1i−1tpj′+cpi+1′∑j=1itpj′−(cpi∑j=1i−1tpj+cpi+1∑j=1itpj)=cpitpi+1−cpi+1tpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是我们使用如果 𝑐𝑝𝑖𝑡𝑝𝑖+1 −𝑐𝑝𝑖+1𝑡𝑝𝑖 >0cpitpi+1−cpi+1tpi>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就交换的策略做一下排序就可以了．写成 𝑐𝑝𝑖𝑡𝑝𝑖 >𝑐𝑝𝑖+1𝑡𝑝𝑖+1cpitpi>cpi+1tpi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，就可以理解为将排列按 𝑐𝑖𝑡𝑖citi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 升序排序．

处理这个问题，我们的思路是考虑微扰后的变换情况，贪心地选取最优解．

### 指数代价函数

考虑代价函数的形式为 𝑓𝑖(𝑥) =𝑐𝑖e𝑎𝑥fi(x)=cieax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐𝑖 ≥0,𝑎 >0ci≥0,a>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们沿用之前的思路，考虑将 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置上的数交换引起的代价变化．最终得到的算法是将排列按照 1−e𝑎𝑡𝑖𝑐𝑖1−eatici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 升序排序．

### 相同的单增函数

我们考虑所有的 𝑓𝑖(𝑥)fi(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是同一个单增函数．那么显然我们将排列按照 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 升序排序即可．

## Livshits–Kladov 定理

Livshits–Kladov 定理成立，当且仅当代价函数是以下三种情况：

  * 线性函数：𝑓𝑖(𝑡) =𝑐𝑖𝑡 +𝑑𝑖fi(t)=cit+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐𝑖 ≥0ci≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 指数函数：𝑓𝑖(𝑡) =𝑐𝑖e𝑎𝑡 +𝑑𝑖fi(t)=cieat+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐𝑖,𝑎 >0ci,a>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 相同的单增函数：𝑓𝑖(𝑡) =𝜙(𝑡)fi(t)=ϕ(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝜙(𝑡)ϕ(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个单增函数．

定理是在假设代价函数足够平滑（存在三阶导数）的条件下证明的．在这三种情况下，问题的最优解可以通过简单的排序在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内解决．

**本页面主要译自博文[Задача Джонсона с одним станком](http://e-maxx.ru/algo/johnson_problem_1) 与其英文翻译版 [Scheduling jobs on one machine](https://cp-algorithms.com/schedules/schedule_one_machine.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/4/23 03:45:48，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/job-order.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/job-order.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [sshwy](https://github.com/sshwy), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [HeRaNO](https://github.com/HeRaNO), [lailai0916](https://github.com/lailai0916), [ouuan](https://github.com/ouuan)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
