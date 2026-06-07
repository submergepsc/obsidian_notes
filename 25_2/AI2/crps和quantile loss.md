# Quantile Loss 与 CRPS：概率预测评价指标笔记
本文统一采用**损失函数**的记法：
$$
\text{指标越小，说明预测越好。}  
$$
需要注意：不同文献中可能存在两类记号差异：
1. 有些资料将 **Quantile Score** 定义为 Quantile Loss 的 $2$ 倍；
2. 有些理论文献将评分规则写成“越大越好”的奖励形式，而实际预测评测中更常见的是“越小越好”的损失形式。
因此，在阅读论文或复现代码时，应以具体公式为准。
# 1. 从点预测到概率预测
## 1.1 点预测
点预测只给出未来的一个预测值。例如，对未来第 $24$ 个小时的负荷进行预测：
$$
\hat{y}_{t+24}=100  
$$
其中：
- $t$：当前时间点；
- $h$：预测步长；
- $\hat{y}_{t+h}$：对未来时刻 $t+h$ 的预测值；
- $y_{t+h}$：未来实际观测值。
点预测常用指标包括 MAE 和 MSE。
### MAE：平均绝对误差
$$
\mathrm{MAE}
\frac{1}{N}  
\sum_{i=1}^{N}  
\left|  
y_i-\hat{y}_i  
\right|  
$$
### MSE：平均平方误差
$$
\mathrm{MSE}
\frac{1}{N}  
\sum_{i=1}^{N}  
\left(  
y_i-\hat{y}_i  
\right)^2  
$$
这些指标评价的是：
$$
\text{单个预测值距离真实值有多远。}  
$$
## 1.2 概率预测
现实中的未来通常存在不确定性。与其只输出一个预测值，模型还可以输出：
- 多个分位数，例如 P10、P50、P90；
- 一个完整的概率分布；
- 多条从预测分布中采样得到的未来轨迹。
例如，模型对未来负荷给出以下预测：

|分位数|预测值|含义|
|--:|--:|---|
|P10|$80$|真实值低于 $80$ 的概率约为 $10\\\%$|
|P50|$100$|中位数预测|
|P90|$130$|真实值低于 $130$ 的概率约为 $90\\\%$|

概率预测不仅关心预测中心是否准确，还关心：
- 预测范围是否合理；
- 预测分布是否过宽或过窄；
- 真实值是否与预测分布相匹配；
- 模型是否合理表达了未来的不确定性。
因此，需要使用专门的概率预测评价指标：

|模型输出形式|常用评价指标|
|---|---|
|单个预测值|MAE、RMSE|
|一个或多个分位数|Quantile Loss|
|完整概率分布或大量预测样本|CRPS|

# 2. 基本符号
| 符号                   | 含义                      |
| -------------------- | ----------------------- |
| $y$                  | 最终观测到的真实值               |
| $\hat{y}$            | 模型给出的点预测值               |
| $\tau$               | 分位数水平，满足 $0<\tau<1$     |
| $\hat{q}_{\tau}$     | 模型预测的 $\tau$ 分位数        |
| $F(z)$               | 模型给出的预测累积分布函数           |
| $X\sim F$            | 从预测分布 $F$ 中抽取的随机样本      |
| $X'\sim F$           | 与 $X$ 独立、来自同一预测分布的另一个样本 |
| $x_1,x_2,\ldots,x_m$ | 模型生成的有限个预测样本            |
| $\mathbf{1}{\cdot}$  | 指示函数，条件成立时取 $1$，否则取 $0$ |

# 3. Quantile Loss：评价某一个分位数
## 3.1 什么是分位数预测？
设未来真实值为随机变量 $Y$。预测分布的 $\tau$ 分位数记为：
$$
\hat{q}_{\tau}  
$$
它的含义是：
$$
P\left(  
Y\le \hat{q}_{\tau}  
\right)  
\approx  
\tau  
$$
例如：
$$
\hat{q}_{0.9}=130  
$$
表示模型认为：
$$
P\left(  
Y\le130  
\right)  
\approx  
= 0.9
$$
也就是说，未来真实值有大约 $90\\\%$ 的概率不超过 $130$。
常见分位数包括：

|分位数|记号|含义|
|--:|--:|---|
|P10|$\hat{q}_{0.1}$|偏低位置的预测|
|P50|$\hat{q}_{0.5}$|中位数预测|
|P90|$\hat{q}_{0.9}$|偏高位置的预测|

## 3.2 Quantile Loss 的定义
Quantile Loss 又称为 **Pinball Loss**。
设：
- $y$：真实值；
- $\hat{q}_{\tau}$：模型预测的 $\tau$ 分位数；
- $\tau$：分位数水平。
则 Quantile Loss 定义为：
$$
L_{\tau}  
\left(  
y,\hat{q}_{\tau}  
\right)
\begin{cases}  
\tau  
\left(  
y-\hat{q}_{\tau}  
\right),  
&  
y\ge \hat{q}_{\tau}  
\\[6pt]  
\left(  
1-\tau  
\right)  
\left(  
\hat{q}_{\tau}-y  
\right),  
&  
y<\hat{q}_{\tau}  
\end{cases}  
$$
也可以写成紧凑形式：
$$
L_{\tau}  
\left(  
y,\hat{q}_{\tau}  
\right)
=  \left[
\tau -
\mathbf{1}  
\left\{  
y<\hat{q}_{\tau}  
\right\}  
\right]  
\left(  
y-\hat{q}_{\tau}  
\right)  
$$
其中，指示函数为：
$$
\mathbf{1}  
\left\{  
y<\hat{q}_{\tau}  
\right\}
\begin{cases}  
1,  
&  
y<\hat{q}_{\tau}  
\\[4pt]  
0,  
&  
y\ge \hat{q}_{\tau}  
\end{cases}  
$$
## 3.3 为什么 Quantile Loss 采用不对称惩罚？
MAE 对高估和低估的惩罚是相同的：
$$
\left|  
y-\hat{y}  
\right|  
$$
但是，对于分位数预测，高估和低估的含义不同。
例如，假设模型预测 P90 为：
$$
\hat{q}_{0.9}=100  
$$
P90 本来应该是一个偏高的预测位置，因此：
- 如果真实值超过 P90，说明模型对高位风险估计不足；
- 如果真实值低于 P90，并不一定说明模型预测很差，因为 P90 原本就应高于大部分观测值。
### 情况一：真实值为 $110$
此时模型预测过低：
$$
y=110>\hat{q}_{0.9}=100  
$$
损失为：
$$
L_{0.9}  
\left(  
110,100  
\right)
= 0.9
\left(  
110-100  
\right)
= 9
$$
### 情况二：真实值为 $90$
此时模型预测偏高：
$$
y=90<\hat{q}_{0.9}=100  
$$
损失为：
$$
L_{0.9}  
\left(  
90,100  
\right)
= \left(
1-0.9  
\right)  
\left(  
100-90  
\right)
= 1
$$
因此，对于 P90：

|情况|惩罚权重|解释|
|---|--:|---|
|真实值高于预测值|$0.9$|对高位风险估计不足，惩罚较重|
|真实值低于预测值|$0.1$|P90 本就应偏高，惩罚较轻|

## 3.4 不同分位数的惩罚方向
|分位数|当预测低于真实值时|当预测高于真实值时|解释|
|--:|--:|--:|---|
|P10，$\tau=0.1$|惩罚较轻|惩罚较重|P10 应位于偏低位置|
|P50，$\tau=0.5$|惩罚相同|惩罚相同|中位数预测|
|P90，$\tau=0.9$|惩罚较重|惩罚较轻|P90 应位于偏高位置|

## 3.5 P50 的 Quantile Loss 与 MAE 的关系
当：
$$
\tau=0.5  
$$
时，无论真实值高于还是低于预测值，Quantile Loss 都可以写成：
$$
L_{0.5}  
\left(  
y,\hat{q}_{0.5}  
\right)
= 0.5
\left|  
y-\hat{q}_{0.5}  
\right|  
$$
因此：
$$
\boxed{  
\text{P50 的 Quantile Loss 与 MAE 具有相同的最优预测目标。}  
}  
$$
它们都倾向于预测条件中位数，只是在当前定义下，P50 Quantile Loss 的数值是绝对误差的一半。
有些资料将 Quantile Score 定义为：
$$
Q_{\tau}
2L_{\tau}  
$$
那么：
$$
Q_{0.5}  
\left(  
y,\hat{q}_{0.5}  
\right)
\left|  
y-\hat{q}_{0.5}  
\right|  
$$
此时，P50 Quantile Score 与绝对误差在数值上完全一致。
## 3.6 Quantile Loss 计算示例
假设真实值为：
$$
y=100  
$$
模型输出三个分位数预测：

|分位数|预测值|
|--:|--:|
|P10|$80$|
|P50|$95$|
|P90|$130$|

### P10 的 Quantile Loss
因为：
$$
100\ge80  
$$
所以：
$$
L_{0.1}
= 0.1
\left(  
100-80  
\right)
= 2
$$
### P50 的 Quantile Loss
因为：
$$
100\ge95  
$$
所以：
$$
L_{0.5}
= 0.5
\left(  
100-95  
\right)
= 2.5
$$
### P90 的 Quantile Loss
因为：
$$
100<130  
$$
所以：
$$
L_{0.9}
= \left(
1-0.9  
\right)  
\left(  
130-100  
\right)
= 3
$$
如果对这三个分位数的损失做简单平均，则：
$$
\frac{  
L_{0.1}  
+  
L_{0.5}  
+  
L_{0.9}  
}{3}
= \frac{
2+2.5+3  
}{3}
= 2.5
$$
这个结果表示模型在 P10、P50、P90 三个指定位置上的平均分位数预测误差。
## 3.7 Quantile Loss 评价的是什么？
Quantile Loss 评价的是：
$$
\text{某一个指定分位数的位置是否准确。}  
$$
例如：

|指标|评价内容|
|---|---|
|$L_{0.1}$|P10 是否准确|
|$L_{0.5}$|P50 是否准确|
|$L_{0.9}$|P90 是否准确|

Quantile Loss 适用于以下场景：
- 分位数回归；
- 输出 P10、P50、P90 的时间序列模型；
- 电力负荷概率预测；
- 风电与光伏功率预测；
- 需求预测与库存规划；
- 需要重点评价高位风险或低位风险的任务。
# 4. CRPS：评价整个预测分布
## 4.1 CRPS 的基本含义
CRPS 的全称是：
$$
\text{Continuous Ranked Probability Score}  
$$
中文通常翻译为：
$$
\text{连续秩概率评分}  
$$
Quantile Loss 只评价某一个分位数；CRPS 评价的是：
$$
\text{整个预测分布与最终真实结果之间的整体差异。}  
$$
在本文采用的损失形式下：
$$
\mathrm{CRPS}\ge0  
$$
并且：
$$
\mathrm{CRPS}=0  
$$
表示预测分布与真实结果完全一致。
## 4.2 什么是 CDF？
CDF 是 **累积分布函数**，记为：
$$
F(z)
P  
\left(  
X\le z  
\right)  
$$
它表示：
$$
\text{模型认为未来真实值不超过 }z\text{ 的概率。}  
$$
例如：
$$
F(100)=0.7  
$$
表示模型认为：
$$
P  
\left(  
X\le100  
\right)
= 0.7
$$
即未来真实值不超过 $100$ 的概率为 $70\\\%$。
## 4.3 真实值对应的 CDF
假设最终真实值为：
$$
y=100  
$$
因为真实结果已经确定，所以它对应的是一个阶跃函数：
$$
H_y(z)=
\mathbf{1}  
\left\{  
z\ge y  
\right\}  
$$
其中：
$$
H_y(z)
\begin{cases}  
0,  
&  
z<y  
\\[4pt]  
1,  
&  
z\ge y  
\end{cases}  
$$
当 $y=100$ 时：
$$
H_{100}(z)
\begin{cases}  
0,  
&  
z<100  
\\[4pt]  
1,  
&  
z\ge100  
\end{cases}  
$$
其含义是：
- 当 $z<100$ 时，真实值不超过 $z$ 的判断结果为 $0$；
- 当 $z\ge100$ 时，真实值不超过 $z$ 的判断结果为 $1$。
## 4.4 CRPS 的 CDF 定义
CRPS 定义为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
=  \int_{-\infty}^{+\infty}
\left[  
F(z) -
\mathbf{1}  
\left\{  
z\ge y  
\right\}  
\right]^2  
,dz  
$$
也可以使用 $H_y(z)$ 写为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
\int_{-\infty}^{+\infty}  
\left[  
F(z)-H_y(z)  
\right]^2  
,dz  
$$
其中：
- $F(z)$：模型预测的 CDF；
- $H_y(z)$：真实值对应的阶跃 CDF；
- $z$：沿着目标变量数值范围移动的阈值。
因此，CRPS 可以理解为：
$$
\boxed{  
\mathrm{CRPS}
\text{预测 CDF 与真实 CDF 之间的平方距离面积。}  
}  
$$
# 5. CRPS 中的平方究竟平方了什么？
这是理解 CRPS 最关键、也最容易混淆的部分。
## 5.1 平方的不是预测值与真实值的距离
CRPS 原始公式中确实存在平方：
$$
\left[  
F(z)-
\mathbf{1}  
\left\{  
z\ge y  
\right\}  
\right]^2  
$$
但是，这里的平方作用在：
$$
\text{预测 CDF 与真实 CDF 在位置 }z\text{ 处的纵向高度差}  
$$
而不是作用在：
$$
x-y  
$$
因此，CRPS 的样本表达式中最终出现绝对值，而不是平方误差。
## 5.2 单点预测示例
假设模型只给出一个确定预测值：
$$
x=90  
$$
真实值为：
$$
y=100  
$$
预测值 $90$ 对应的阶跃 CDF 为：
$$
H_{90}(z)
\mathbf{1}  
\left\{  
z\ge90  
\right\}  
$$
真实值 $100$ 对应的阶跃 CDF 为：
$$
H_{100}(z)
\mathbf{1}  
\left\{  
z\ge100  
\right\}  
$$
比较这两个阶跃函数：

| $z$ 的范围       | $H_{90}$z$$ | $H_{100}$z$$ | 高度差 | 高度差平方 |
| ------------- | ----------: | -----------: | --: | ----: |
| $z<90$        |         $0$ |          $0$ | $0$ |   $0$ |
| $90\le z<100$ |         $1$ |          $0$ | $1$ |   $1$ |
| $z\ge100$     |         $1$ |          $1$ | $0$ |   $0$ |

因此：
$$
\int_{-\infty}^{+\infty}  
\left[  
H_{90}(z)
- H_{100}(z)
\right]^2  
dz
= \int_{90}^{100}
 1
\,dz
= 10
$$
而：
$$
\left|  
90-100  
\right|
= 10
$$
因此，一般地：
$$
\boxed{  
\int_{-\infty}^{+\infty}  
\left[  
H_a(z)-H_b(z)  
\right]^2  
,dz
\left|  
a-b  
\right|  
}  
$$
## 5.3 为什么不是平方误差？
在 $90\le z<100$ 这段区间中，两个 CDF 的纵向高度差是：
$$
1  
$$
所以其平方为：
$$
1^2=1  
$$
而这段区间的横向长度为：
$$
100-90=10  
$$
因此积分得到的面积是：
$$
1\times10=10  
$$
而不是：
$$
\left(  
100-90  
\right)^2
= 100
$$
所以：
$$
\boxed{  
\text{CRPS 中的平方没有消失，而是在积分后表现为绝对距离。}  
}  
$$
更准确地说：
$$
\boxed{  
\text{CDF 纵向高度差的平方经过横向积分，得到预测值之间的绝对距离。}  
}  
$$
# 6. CRPS 的期望表达式
如果从预测分布 $F$ 中独立抽取两个样本：
$$
X,X'  
\overset{\mathrm{i.i.d.}}{\sim}  
F  
$$
则 CRPS 可以等价写为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
=  \mathbb{E}
\left|  
X-y  
\right| -
\frac{1}{2}  
\mathbb{E}  
\left|  
X-X'  
\right|  
$$
这个公式由两部分构成。
## 6.1 第一项：预测样本离真实值有多远
$$
\mathbb{E}  
\left|  
X-y  
\right|  
$$
它表示：
$$
\text{从预测分布中抽出的样本，平均距离真实值有多远。}  
$$
如果模型生成的预测样本整体远离真实值，这一项会变大。
## 6.2 第二项：预测分布内部有多分散
$$
\frac{1}{2}  
\mathbb{E}  
\left|  
X-X'  
\right|  
$$
它表示：
$$
\text{从预测分布中抽出的两个样本，平均相差多远。}  
$$
完整公式中第二项前面带有减号：
$$
\frac{1}{2}  
\mathbb{E}  
\left|  
X-X'  
\right|  
$$
但这不能简单理解为：
$$
\text{预测分布越宽越好。}  
$$
更准确的解释是：
> 第一项将每个预测样本分别与真实值比较；第二项用于修正预测样本之间合理存在的内部差异，使最终评价对象真正成为整个预测分布，而不是若干个互不相关的点预测。
如果模型随意将预测范围扩大，第一项也会显著增大，因此最终 CRPS 通常仍会变差。
# 7. CRPS 的样本计算公式
## 7.1 有限预测样本形成经验分布
假设模型生成了 $m$ 个预测样本：
$$
x_1,x_2,\ldots,x_m  
$$
将这些样本看作一个经验预测分布，每个样本的概率均为：
$$
\frac{1}{m}  
$$
那么经验 CDF 为：
$$
F_m(z)
\frac{1}{m}  
\sum_{i=1}^{m}  
\mathbf{1}  
\left\{  
z\ge x_i  
\right\}  
$$
对这个经验分布，CRPS 可以写成：
$$
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
=  \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right| -
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_i-x_j  
\right|  
$$
## 7.2 第一项的含义
$$
\frac{1}{m}  
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right|  
$$
表示：
$$
\text{所有预测样本与真实值之间的平均绝对距离。}  
$$
这一项越小，说明预测样本整体越靠近真实值。
## 7.3 第二项的含义
$$
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_i-x_j  
\right|  
$$
表示：
$$
\text{所有预测样本两两之间平均距离的一半。}  
$$
之所以分母中出现 $m^2$，是因为：
- 第一个样本 $x_i$ 有 $m$ 种选择；
- 第二个样本 $x_j$ 也有 $m$ 种选择；
- 因此，共有 $m^2$ 个有序组合。
当 $i=j$ 时：
$$
\left|  
x_i-x_i  
\right|
= 0
$$
因此，这些对角项虽然被纳入求和，但不会影响最终结果。
# 8. 从 CDF 定义推导 CRPS 样本公式
## 8.1 定义阶跃函数
记：
$$
H_a(z)
\mathbf{1}  
\left\{  
z\ge a  
\right\}  
$$
则经验 CDF 可以写成：
$$
F_m(z)
\frac{1}{m}  
\sum_{i=1}^{m}  
H_{x_i}(z)  
$$
真实值对应的 CDF 为：
$$
H_y(z)  
$$
因此：
$$
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
=  \int_{-\infty}^{+\infty}
\left[  
\frac{1}{m}  
\sum_{i=1}^{m}  
H_{x_i}(z)
-
H_y(z)  
\right]^2  
,dz  
$$
## 8.2 使用平方距离分解恒等式
固定某个位置 $z$，令：
$$
a_i
H_{x_i}(z)  
$$
$$
b
H_y(z)  
$$
以及：
$$
\bar{a}
= \frac{1}{m}
\sum_{i=1}^{m}  
a_i
F_m(z)  
$$
则有如下恒等式：
$$
\left(  
\bar{a}-b  
\right)^2
= \frac{1}{m}
\sum_{i=1}^{m}  
\left(  
a_i-b  
\right)^2
-
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left(  
a_i-a_j  
\right)^2  
$$
将阶跃函数代入后得到：
$$
\left[  
F_m(z)-H_y(z)  
\right]^2
= \frac{1}{m}
\sum_{i=1}^{m}  
\left[  
H_{x_i}(z)-H_y(z)  
\right]^2
-
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left[  
H_{x_i}(z)-H_{x_j}(z)  
\right]^2  
$$
## 8.3 对整个数值轴积分
对 $z$ 积分：
$$
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
=  \frac{1}{m}
\sum_{i=1}^{m}  
\int_{-\infty}^{+\infty}  
\left[  
H_{x_i}(z)-H_y(z)  
\right]^2  
,dz
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\int_{-\infty}^{+\infty}  
\left[  
H_{x_i}(z)-H_{x_j}(z)  
\right]^2  
,dz  
$$
由于：
$$
\int_{-\infty}^{+\infty}  
\left[  
H_a(z)-H_b(z)  
\right]^2  
,dz
\left|  
a-b  
\right|  
$$
因此：
$$
\int_{-\infty}^{+\infty}  
\left[  
H_{x_i}(z)-H_y(z)  
\right]^2  
,dz
\left|  
x_i-y  
\right|  
$$
并且：
$$
\int_{-\infty}^{+\infty}  
\left[  
H_{x_i}(z)-H_{x_j}(z)  
\right]^2  
,dz
\left|  
x_i-x_j  
\right|  
$$
最终得到：
$$
\boxed{  
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
= # \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right|
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_i-x_j  
\right|  
}  
$$
这就是使用有限预测样本计算 CRPS 的公式。
# 9. CRPS 完整计算示例
假设真实值为：
$$
y=100  
$$
模型生成两个等概率预测样本：
$$
x_1=90,  
\qquad  
x_2=110  
$$
因此：
$$
m=2  
$$
## 9.1 使用样本公式计算
### 第一项：预测样本到真实值的平均距离
$$
\frac{1}{2}  
\left(  
\left|  
90-100  
\right|  
+  
\left|  
110-100  
\right|  
\right)
= \frac{
10+10  
}{2}
= 10
$$
### 第二项：预测样本内部距离的一半
共有四个有序组合：

| $x_i$ | $x_j$ | $\left|x_i-x_j\right|$ |  
|---:|---:|---:|  
| $90$ | $90$ | $0$ |  
| $90$ | $110$ | $20$ |  
| $110$ | $90$ | $20$ |  
| $110$ | $110$ | $0$ |

因此：
$$
\frac{1}{2\times2^2}  
\left(  
0+20+20+0  
\right)
= \frac{40}{8}
= 5
$$
最终：
$$
\mathrm{CRPS}
= 10-5
= 5
$$
## 9.2 使用 CDF 原始定义验证
由两个样本 $90$ 与 $110$ 形成的经验 CDF 为：
$$
F_2(z)
\begin{cases}  
0,  
&  
z<90  
\\[4pt]  
0.5,  
&  
90\le z<110  
\\[4pt]  
1,  
&  
z\ge110  
\end{cases}  
$$
真实值 $100$ 对应的阶跃 CDF 为：
$$
H_{100}(z)
\begin{cases}  
0,  
&  
z<100  
\\[4pt]  
1,  
&  
z\ge100  
\end{cases}  
$$
### 区间一：$90\le z<100$
在该区间内：
$$
F_2(z)=0.5,  
\qquad  
H_{100}(z)=0  
$$
因此：
$$
\left[  
F_2(z)-H_{100}(z)  
\right]^2
= \left(
0.5-0  
\right)^2
= 0.25
$$
区间长度为：
$$
100-90=10  
$$
该区间对 CRPS 的贡献为：
$$
0.25\times10
= 2.5
$$
### 区间二：$100\le z<110$
在该区间内：
$$
F_2(z)=0.5,  
\qquad  
H_{100}(z)=1  
$$
因此：
$$
\left[  
F_2(z)-H_{100}(z)  
\right]^2
= \left(
0.5-1  
\right)^2
= 0.25
$$
区间长度为：
$$
110-100=10  
$$
该区间对 CRPS 的贡献为：
$$
0.25\times10
= 2.5
$$
所以：
$$
\mathrm{CRPS}
= 2.5+2.5
= 5
$$
这与样本公式的计算结果完全一致。
# 10. 用几个预测分布理解 CRPS
仍然假设真实值为：
$$
y=100  
$$

|模型|预测样本|第一项|第二项|CRPS|解释|
|---|---|--:|--:|--:|---|
|A|$100,100$|$0$|$0$|$\mathbf{0}$|完美预测|
|B|$90,90$|$10$|$0$|$\mathbf{10}$|错误且过度自信|
|C|$90,110$|$10$|$5$|$\mathbf{5}$|合理表达了一部分不确定性|
|D|$0,200$|$100$|$50$|$\mathbf{50}$|预测范围过宽，信息价值很低|

由此可以看出：
- 模型 A 最好，因为预测准确且集中；
- 模型 B 错在非常确定地预测了错误结果；
- 模型 C 虽然不是单点准确预测，但真实值位于其预测分布中间；
- 模型 D 虽然覆盖了真实值，但预测范围过宽，最终 CRPS 仍然较差。
因此，CRPS 综合评价：
$$
\text{预测分布是否靠近真实值}  
$$
以及：
$$
\text{预测分布是否合理表达不确定性}  
$$
# 11. Quantile Loss 与 CRPS 的关系
## 11.1 直观关系
Quantile Loss 评价的是预测分布上的某一个位置，例如：
$$
\hat{q}_{0.1},  
\qquad  
\hat{q}_{0.5},  
\qquad  
\hat{q}_{0.9}  
$$
CRPS 则综合评价整个预测分布。
因此：
$$
\boxed{  
\text{Quantile Loss 评价单个分位数，CRPS 评价整个概率分布。}  
}  
$$
## 11.2 数学关系
设：
$$
F^{-1}(\tau)  
$$
表示预测分布的 $\tau$ 分位数。
在本文所采用的 Quantile Loss 定义下：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
= 2
\int_{0}^{1}  
L_{\tau}  
\left(  
y,F^{-1}(\tau)  
\right)  
,d\tau  
$$
如果将 Quantile Score 定义为：
$$
Q_{\tau}
2L_{\tau}  
$$
则：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
\int_{0}^{1}  
Q_{\tau}  
\left(  
y,F^{-1}(\tau)  
\right)  
,d\tau  
$$
也就是说：
$$
\boxed{  
\text{CRPS 可以理解为所有分位数损失的综合结果。}  
}  
$$
## 11.3 使用有限个分位数近似 CRPS
如果模型只输出：
$$
P10,  
\qquad  
P50,  
\qquad  
P90  
$$
那么可以计算：
$$
L_{0.1},  
\qquad  
L_{0.5},  
\qquad  
L_{0.9}  
$$
并求平均：
$$
\frac{  
L_{0.1}  
+  
L_{0.5}  
+  
L_{0.9}  
}{3}  
$$
但是，这个简单平均值并不严格等于 CRPS，因为 CRPS 理论上综合了从 $0$ 到 $1$ 的所有分位数。
如果模型输出较密集的分位数，例如：
$$
P01,  
P02,  
\ldots,  
P99  
$$
则可以使用数值积分近似 CRPS：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)  
\approx  
= 2
\sum_{k=1}^{K}  
w_k  
L_{\tau_k}  
\left(  
y,\hat{q}_{\tau_k}  
\right)  
$$
其中：
- $\tau_k$：第 $k$ 个分位数水平；
- $\hat{q}_{\tau_k}$：对应的分位数预测值；
- $w_k$：数值积分权重。
# 12. Quantile Loss、CRPS、MAE 与 MSE 的比较
|指标|模型输出形式|评价对象|是否评价不确定性|单位|
|---|---|---|--:|---|
|MAE|单个预测值|点预测绝对误差|否|与目标变量相同|
|MSE|单个预测值|点预测平方误差|否|目标变量单位的平方|
|Quantile Loss|指定分位数|某个分位数的位置准确性|部分体现|与目标变量相同|
|CRPS|完整分布或预测样本|整体概率预测质量|是|与目标变量相同|

## 12.1 Quantile Loss 与 MAE
当：
$$
\tau=0.5  
$$
时：
$$
L_{0.5}  
\left(  
y,\hat{q}_{0.5}  
\right)
= 0.5
\left|  
y-\hat{q}_{0.5}  
\right|  
$$
因此：
$$
\boxed{  
\text{P50 Quantile Loss 与 MAE 具有相同的最优预测目标。}  
}  
$$
## 12.2 CRPS 与 MAE
如果预测分布退化为一个确定的点预测：
$$
X=\hat{y}  
$$
那么：
$$
X'=X=\hat{y}  
$$
因此：
$$
\mathbb{E}  
\left|  
X-X'  
\right|
= 0
$$
CRPS 变为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
\left|  
\hat{y}-y  
\right|  
$$
因此：
$$
\boxed{  
\text{当概率预测退化为点预测时，CRPS 退化为绝对误差。}  
}  
$$
可以将 CRPS 理解为：
$$
\boxed{  
\text{MAE 从点预测推广到概率预测后的形式。}  
}  
$$
## 12.3 CRPS 与 MSE 的区别
MSE 直接计算：
$$
\left(  
\hat{y}-y  
\right)^2  
$$
因此，MSE 的单位是目标变量单位的平方。
CRPS 计算的是 CDF 之间的积分距离，最终单位与目标变量相同。
例如，如果预测对象是电力负荷，单位为 MW，则：

|指标|单位|
|---|---|
|MAE|MW|
|Quantile Loss|MW|
|CRPS|MW|
|MSE|$\mathrm{MW}^2$|

# 13. 时间序列预测中的计算方法
假设需要预测未来 $H$ 个时间步：
$$
t+1,  
t+2,  
\ldots,  
t+H  
$$
## 13.1 模型只输出点预测
如果模型输出：
$$
\hat{y}_{t+1},  
\hat{y}_{t+2},  
\ldots,  
\hat{y}_{t+H}  
$$
则可以计算：
$$
\mathrm{MAE}
= # \frac{1}{H}
\sum_{h=1}^{H}  
\left|  
y_{t+h}
\hat{y}_{t+h}  
\right|  
$$
或者：
$$
\mathrm{RMSE}
= # \sqrt{
\frac{1}{H}  
\sum_{h=1}^{H}  
\left(  
y_{t+h}
\hat{y}_{t+h}  
\right)^2  
}  
$$
## 13.2 模型输出分位数预测
如果模型对每个未来时刻输出：
$$
\hat{q}_{0.1,t+h},  
\qquad  
\hat{q}_{0.5,t+h},  
\qquad  
\hat{q}_{0.9,t+h}  
$$
则对于固定分位数 $\tau$，跨预测窗口的平均 Quantile Loss 为：
$$
\overline{L}_{\tau}
\frac{1}{H}  
\sum_{h=1}^{H}  
L_{\tau}  
\left(  
y_{t+h},  
\hat{q}_{\tau,t+h}  
\right)  
$$
例如，可以分别报告：
$$
\overline{L}_{0.1},  
\qquad  
\overline{L}_{0.5},  
\qquad  
\overline{L}_{0.9}  
$$
它们分别反映：

|指标|评价内容|
|---|---|
|$\overline{L}_{0.1}$|低位预测质量|
|$\overline{L}_{0.5}$|中位数预测质量|
|$\overline{L}_{0.9}$|高位预测质量|

如果需要一个简单汇总指标，可以进一步计算：
$$
\overline{L}
\frac{1}{K}  
\sum_{k=1}^{K}  
\overline{L}_{\tau_k}  
$$
其中 $K$ 表示所评价的分位数数量。
## 13.3 模型输出预测样本或采样轨迹
如果模型对每个未来时间步生成 $m$ 个预测样本：
$$
x_{1,t+h},  
x_{2,t+h},  
\ldots,  
x_{m,t+h}  
$$
则对每一个预测步长 $h$，可以计算：
$$
\mathrm{CRPS}_{t+h}
= # \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_{i,t+h}
= # y_{t+h}
\right|
= # \frac{1}{2m^2}
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_{i,t+h}
x_{j,t+h}  
\right|  
$$
再对整个预测窗口求平均：
$$
\overline{\mathrm{CRPS}}
\frac{1}{H}  
\sum_{h=1}^{H}  
\mathrm{CRPS}_{t+h}  
$$
如果测试集中包含多个预测起点，还可以进一步对所有预测起点求平均。
# 14. 在时间序列基础模型评测中的指标选择
|模型输出形式|推荐指标|原因|
|---|---|---|
|只输出单个点预测|MAE、RMSE|不存在需要评价的预测分布|
|输出 P10、P50、P90|Quantile Loss|可以分别评价不同分位数|
|输出较密集的分位数网格|CRPS 或近似 CRPS|可以综合评价概率分布|
|输出大量采样轨迹|CRPS|可以直接通过样本公式计算|
|特别关注高负荷或高风险情形|P90、P95 Quantile Loss|聚焦高位预测能力|
|特别关注低负荷或下行风险|P05、P10 Quantile Loss|聚焦低位预测能力|
|需要一个总体概率预测评价指标|CRPS|便于整体比较模型|

# 15. 实际使用时的注意事项
## 15.1 Quantile Loss 的系数约定
有些资料将分位数损失定义为：
$$
L_{\tau}  
$$
有些资料使用：
$$
Q_{\tau}
2L_{\tau}  
$$
两种形式的模型排序通常相同，但具体数值相差 $2$ 倍。
因此，在报告实验结果时，应明确写出所使用的公式。
## 15.2 CRPS 的方向约定
本文采用的是损失形式：
$$
\mathrm{CRPS}  
\ge  
= 0
$$
且：
$$
\text{CRPS 越小越好。}  
$$
如果阅读到某些理论文献中的 CRPS 带有负号，或被描述为“越大越好”，通常是因为该文采用了奖励形式的 scoring rule 定义。
## 15.3 有限样本 CRPS 的两种版本
常见的经验分布 CRPS 公式为：
$$
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
= # \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right|
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_i-x_j  
\right|  
$$
它评价的是由当前 $m$ 个预测样本直接构成的经验分布。
在 ensemble forecasting 中，也可能看到有限 ensemble 偏差修正版：
$$
\mathrm{CRPS}_{\mathrm{fair}}
= # \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right|
\frac{1}{2m(m-1)}  
\sum_{i\ne j}  
\left|  
x_i-x_j  
\right|  
$$
两者的区别在于：

|公式|主要含义|
|---|---|
|分母为 $2m^2$ 的版本|评价当前经验分布本身|
|分母为 $2m(m-1)$ 的版本|对有限 ensemble 的抽样偏差进行修正|

在论文复现、代码比较和实验报告中，应确认具体采用的是哪一种公式。
## 15.4 Quantile Crossing 问题
当模型分别独立预测多个分位数时，有时可能出现：
$$
\hat{q}_{0.1}
\hat{q}_{0.5}  
$$
或者：
$$
\hat{q}_{0.5}
\hat{q}_{0.9}  
$$
这种情况称为 **Quantile Crossing**，即分位数交叉。
正常情况下应满足：
$$
\hat{q}_{0.1}  
\le  
\hat{q}_{0.5}  
\le  
\hat{q}_{0.9}  
$$
如果出现分位数交叉，说明模型输出的多个分位数不构成一个合理的分布。即使各自 Quantile Loss 不高，也可能影响整体概率预测解释。
## 15.5 多步轨迹预测中的限制
如果模型预测未来 $24$ 小时的一整条轨迹，逐时点计算 CRPS 可以评价每一个时刻的边际预测分布质量。
但是，逐时点 CRPS 不能直接评价：
- 不同未来时间点之间的相关性；
- 整条轨迹的联合分布结构；
- 峰值发生时间是否合理；
- 连续波动模式是否真实；
- 多变量之间的不确定性依赖关系。
因此，如果研究对象是完整轨迹或多变量联合预测，除逐时点 CRPS 外，还可能需要使用其他联合分布评价指标，例如 Energy Score 等。
# 16. 最终总结
## 16.1 Quantile Loss
Quantile Loss 的公式为：
$$
L_{\tau}  
\left(  
y,\hat{q}_{\tau}  
\right)
\begin{cases}  
\tau  
\left(  
y-\hat{q}_{\tau}  
\right),  
&  
y\ge \hat{q}_{\tau}  
\\[6pt]  
\left(  
1-\tau  
\right)  
\left(  
\hat{q}_{\tau}-y  
\right),  
&  
y<\hat{q}_{\tau}  
\end{cases}  
$$
核心理解：
$$
\boxed{  
\text{Quantile Loss 评价某一个指定分位数预测是否准确。}  
}  
$$
主要特点：
- 对高估与低估采用不对称惩罚；
- 不同分位数对应不同风险位置；
- P50 的 Quantile Loss 与 MAE 具有相同的最优预测目标；
- 适合评价模型输出的 P10、P50、P90 等分位数。
## 16.2 CRPS
CRPS 的 CDF 定义为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
= # \int_{-\infty}^{+\infty}
\left[  
F(z)
\mathbf{1}  
\left\{  
z\ge y  
\right\}  
\right]^2  
,dz  
$$
CRPS 的期望形式为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
= # \mathbb{E}
\left|  
X-y  
\right|
\frac{1}{2}  
\mathbb{E}  
\left|  
X-X'  
\right|  
$$
CRPS 的样本形式为：
$$
\mathrm{CRPS}  
\left(  
F_m,y  
\right)
= # \frac{1}{m}
\sum_{i=1}^{m}  
\left|  
x_i-y  
\right|
\frac{1}{2m^2}  
\sum_{i=1}^{m}  
\sum_{j=1}^{m}  
\left|  
x_i-x_j  
\right|  
$$
核心理解：
$$
\boxed{  
\text{CRPS 评价整个预测分布与真实结果之间的整体差异。}  
}  
$$
主要特点：
- 同时考虑预测位置与不确定性表达；
- 适合评价完整概率分布或大量预测样本；
- 当预测分布退化为单点预测时，CRPS 退化为绝对误差；
- CRPS 可以看作 MAE 在概率预测场景下的推广。
## 16.3 Quantile Loss 与 CRPS 的关系
二者之间的数学关系为：
$$
\mathrm{CRPS}  
\left(  
F,y  
\right)
= 2
\int_{0}^{1}  
L_{\tau}  
\left(  
y,F^{-1}(\tau)  
\right)  
,d\tau  
$$
因此：
$$
\boxed{  
\text{Quantile Loss 评价一个分位数，CRPS 综合评价整个预测分布。}  
}  
$$
## 16.4 最重要的易错点
CRPS 原始定义中确实存在平方：
$$
\left[  
F(z)
\mathbf{1}  
\left\{  
z\ge y  
\right\}  
\right]^2  
$$
但这个平方作用在：
$$
\text{CDF 的纵向高度差}  
$$
而不是作用在：
$$
\text{预测值与真实值之间的横向距离}  
$$
因此，在样本公式中出现的是：
$$
\left|  
x_i-y  
\right|  
$$
而不是：
$$
\left(  
x_i-y  
\right)^2  
$$
最终可以记为：
$$
\boxed{  
\text{CDF 高度差的平方经过积分后，表现为预测值之间的绝对距离。}  
}  
$$
# 参考文献
1. Gneiting, T., & Raftery, A. E. 2007. _Strictly Proper Scoring Rules, Prediction, and Estimation_. Journal of the American Statistical Association, 102(477), 359–378.
2. Hyndman, R. J., & Athanasopoulos, G. _Forecasting: Principles and Practice_, 3rd edition, Section 5.9: Evaluating distributional forecast accuracy.