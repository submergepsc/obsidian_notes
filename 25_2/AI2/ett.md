## 一句话理解
**Benchmark（基准测试）就是模型之间统一考试用的“标准试卷 + 考试规则 + 评分方法”。**
`ETTh1` 本身是一份公开时间序列数据；当大家约定在它上面使用相同的预测任务、训练/测试划分、预测长度和指标进行比较时，它就成为了一个 **benchmark dataset / benchmark task**。
# 1. Dataset、Benchmark、Metric 分别是什么
|概念|含义|在你当前实验里的例子|
|---|---|---|
|Dataset|原始数据文件|`ETTh1.csv`|
|Task|模型要解决的问题|用历史油温预测未来油温|
|Benchmark|统一数据、切分、预测长度、指标后的标准比较方案|在 ETTh1 上按统一规则比较 TimesFM、Chronos、Informer|
|Metric|最后打分的方法|MAE、RMSE、Quantile Loss、CRPS|

可以把它类比为考试：

|考试概念|时间序列实验对应物|
|---|---|
|试卷|ETTh1 数据集|
|考试范围|输入长度、预测长度、变量设置|
|评分规则|MAE、MSE、CRPS 等|
|考生|TimesFM、Chronos、Informer、Autoformer 等模型|

所以，论文里写：
> We evaluate our model on standard benchmarks including ETTh1, ETTh2, ETTm1 and ETTm2.
意思就是：
> 我们在大家常用的标准公开数据和评价规则上测试模型，以便与已有模型公平比较。
# 2. ETT 是什么
`ETT` 是 **Electricity Transformer Temperature**，即**电力变压器温度数据集**。
它来自真实电力系统，主要记录：
- 变压器油温；
- 不同类型的电力负荷；
- 时间戳。
该数据集覆盖约两年时间，即 **2016 年 7 月到 2018 年 7 月**。`ETT-small` 包含两个站点的两台变压器数据，最常用于长序列时间预测实验。([GitHub](https://github.com/zhouhaoyi/ETDataset "GitHub - zhouhaoyi/ETDataset: The Electricity Transformer dataset is collected to support the further investigation on the long sequence forecasting problem. · GitHub"))
你下载的 CSV 中有这些字段：

|字段|含义|
|---|---|
|`date`|时间|
|`HUFL`|High Use Full Load|
|`HULL`|High Use Less Load|
|`MUFL`|Middle Use Full Load|
|`MULL`|Middle Use Less Load|
|`LUFL`|Low Use Full Load|
|`LULL`|Low Use Less Load|
|`OT`|Oil Temperature，油温，通常作为预测目标|

其中你当前脚本预测的是：
```text
OT = Oil Temperature
```
也就是：根据过去一段时间的油温，预测未来油温。
# 3. ETTh1、ETTh2、ETTm1、ETTm2 分别是什么意思
ETT-small 通常使用四个文件：

|数据集|`h/m` 的含义|`1/2` 的含义|时间粒度|大致数据量|
|---|---|---|--:|--:|
|`ETTh1`|`h` = hourly|第 1 台变压器/站点|每小时一次|约 17,420 行|
|`ETTh2`|`h` = hourly|第 2 台变压器/站点|每小时一次|约 17,420 行|
|`ETTm1`|`m` = minute-level variant|第 1 台变压器/站点|每 15 分钟一次|70,080 行|
|`ETTm2`|`m` = minute-level variant|第 2 台变压器/站点|每 15 分钟一次|70,080 行|

这里的核心区别是：
```text
h = 小时级数据
m = 更细粒度的 15 分钟数据
1 / 2 = 两个不同变压器站点
```
官方数据仓库说明，小时级版本用于快速开发，而细粒度版本每小时记录四次，因此序列长度显著增加。([GitHub](https://github.com/zhouhaoyi/ETDataset "GitHub - zhouhaoyi/ETDataset: The Electricity Transformer dataset is collected to support the further investigation on the long sequence forecasting problem. · GitHub"))
你现在正在运行的是：
```text
ETTh1 = 第 1 个变压器站点的小时级数据
```
# 4. 为什么 ETT 会成为标准 benchmark
ETT 最初随 **Informer** 论文广泛传播。Informer 研究的是 **Long Sequence Time-Series Forecasting，长序列时间序列预测**，即根据较长历史，预测较长未来。论文和官方代码将 ETT 用作主要实验数据，随后 Autoformer、FEDformer、PatchTST、iTransformer、TimesFM 等大量研究都继续在 ETT 上报告结果。([arXiv](https://arxiv.org/abs/2012.07436?utm_source=chatgpt.com "Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting")) ([GitHub](https://github.com/zhouhaoyi/Informer2020 "GitHub - zhouhaoyi/Informer2020: The GitHub repository for the paper \"Informer\" accepted by AAAI 2021. · GitHub"))
它适合做基准测试，主要因为：

|原因|含义|
|---|---|
|数据公开|大家都能下载相同数据|
|时间跨度较长|包含季节性、趋势和周期变化|
|有多种时间粒度|可测试小时级与更高频预测|
|有单变量和多变量任务|既可只预测 `OT`，也可利用负荷特征|
|适合测试长预测窗口|可测试未来 96、192、336、720 个时间点|
|已被大量论文使用|方便与已有结果横向比较|

例如：
- 在 `ETTh1` 上预测未来 `96` 小时；
- 在 `ETTm1` 上预测未来 `96` 个 15 分钟点，即未来 `24` 小时；
- 在相同设置下比较不同模型的 MAE 或 MSE。
这就构成了标准化比较。
# 5. ETT 中常见的三种预测任务
在 Informer 等时间序列论文中，ETT 常见三种设置：

|设置|输入|输出|解释|
|---|---|---|---|
|`S`|只输入 `OT`|预测 `OT`|单变量预测|
|`M`|输入全部变量|预测全部变量|多变量预测多变量|
|`MS`|输入全部变量|只预测 `OT`|多变量辅助预测单目标|

Informer 官方代码中明确将这三类任务定义为 `S`、`M` 和 `MS`，并将 `OT` 作为 `S` 与 `MS` 设置中的默认目标变量。([GitHub](https://github.com/zhouhaoyi/Informer2020 "GitHub - zhouhaoyi/Informer2020: The GitHub repository for the paper \"Informer\" accepted by AAAI 2021. · GitHub"))
你当前 TimesFM 脚本使用的是：
```text
输入：过去 512 个小时的 OT
输出：未来 96 个小时的 OT
```
所以属于：
```text
ETTh1 / S / context=512 / horizon=96
```
也就是 **ETTh1 上的单变量预测实验**。
# 6. 预测长度 96、192、336、720 是什么
标准长周期预测论文中，经常设置以下预测长度：

|数据集|`96` 个时间点表示什么|
|---|--:|
|`ETTh1` / `ETTh2`|未来 96 小时，即 4 天|
|`ETTm1` / `ETTm2`|未来 96 个 15 分钟，即 24 小时|

以小时级 `ETTh1` 为例：

|Horizon|实际未来范围|
|--:|--:|
|`96`|未来 4 天|
|`192`|未来 8 天|
|`336`|未来 14 天|
|`720`|未来 30 天|

预测窗口越长，通常越难，因为模型需要更好地把握：
- 日周期；
- 周周期；
- 长期趋势；
- 异常波动。
Informer 官方代码提供了 `seq_len` 和 `pred_len` 参数用于配置历史输入长度与未来预测长度；后续长周期预测研究普遍沿用 ETT 上的多种 horizon 设置。([GitHub](https://github.com/zhouhaoyi/Informer2020 "GitHub - zhouhaoyi/Informer2020: The GitHub repository for the paper \"Informer\" accepted by AAAI 2021. · GitHub"))
# 7. 你当前运行的实验算不算 benchmark 实验
## 算是在 benchmark 数据集上测试，但目前还不是严格可对论文表格的标准结果
你现在的脚本做的是：

|项目|当前设置|
|---|---|
|数据集|`ETTh1`|
|变量|只预测 `OT`|
|输入长度|`512` 小时|
|预测长度|`96` 小时|
|测试方式|只预测数据末尾的一个窗口|
|模型|TimesFM 2.5|
|模式|Zero-shot，不在 ETTh1 上训练|

这适合做：
- 验证本地环境是否跑通；
- 快速得到第一张预测图；
- 快速比较 TimesFM 与简单基线；
- 后续与 Chronos 进行同规则零样本比较。
但是，它不能直接与某篇监督学习论文中的结果表格严格对比，因为论文通常还会固定：
- 训练集、验证集、测试集划分；
- 标准化方式；
- 多个预测窗口的平均结果；
- 是否使用全部变量；
- 是否在训练集上进行训练或微调；
- 输入长度与预测长度；
- 使用 MSE、MAE 还是其他指标。
也就是说：
```text
使用 ETTh1 数据集 ≠ 自动等于复现了 ETTh1 标准 benchmark 结果
```
你必须同时遵循相同实验协议，结果才是严格可比的。
# 8. TimesFM 与传统模型在 benchmark 上比较时有什么区别
传统模型，例如 Informer、Autoformer、PatchTST，通常采用：
```text
在 ETTh1 训练集上训练
→ 在验证集上调参
→ 在测试集上评估
```
而你现在使用的 TimesFM 是基础模型，采用：
```text
不在 ETTh1 上重新训练
→ 直接输入历史 OT
→ 输出未来预测
```
这叫：
```text
Zero-shot forecasting
```
Google 对 TimesFM 的介绍强调，它是预训练时间序列基础模型，可在未专门训练的新数据集上直接执行零样本预测，并在多个公开 benchmark 上与监督学习方法比较。([Google Research](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/?utm_source=chatgpt.com "A decoder-only foundation model for time-series forecasting"))
因此你的实验研究问题可以写成：
> 在不对目标数据集进行专项训练的条件下，预训练时间序列基础模型 TimesFM 能否在标准 ETT 数据集上取得有竞争力的预测效果？
这与传统论文中的问题稍有不同：
> 在 ETTh1 训练集上训练后，哪种监督模型预测效果最好？
# 9. 一个直观例子
假设有三种模型：

|模型|是否在 ETTh1 上训练|测试数据|MAE|
|---|--:|---|--:|
|Seasonal Naive|否|ETTh1 测试集|0.85|
|TimesFM|否，zero-shot|ETTh1 测试集|0.62|
|Informer|是|ETTh1 测试集|0.58|

你可以得出：
```text
TimesFM 在无需针对 ETTh1 训练的情况下，显著优于简单基线，
并接近经过专门训练的 Informer。
```
但不能简单说：
```text
TimesFM 一定优于 Informer。
```
因为两者训练条件不同。
# 10. Benchmark 也不是绝对真实世界表现
ETT 很常用，但它也有局限：

|局限|含义|
|---|---|
|行业范围单一|只反映电力变压器相关序列|
|`ETT-small` 规模有限|主要只有两个站点的数据|
|时间范围固定|只覆盖约两年历史数据|
|被大量反复测试|模型可能针对该类数据进行了间接优化|
|不代表你的真实应用|在 ETT 上好，不一定在你的实际负荷或设备数据上好|

因此比较严谨的研究通常会采用多个 benchmark，例如：

|数据集|场景|
|---|---|
|ETT|变压器油温与负荷|
|Electricity / ECL|电力消耗|
|Traffic|交通流量|
|Weather|气象变量|
|Exchange|汇率|
|ILI|流感样病例数据|

如果一个模型在多个不同领域的数据上都表现良好，才能更有力地说明它具备通用预测能力。
## 你现在最需要记住的结构
```text
ETT
└── Electricity Transformer Temperature，电力变压器温度数据集
    ├── ETTh1：站点 1，小时级
    ├── ETTh2：站点 2，小时级
    ├── ETTm1：站点 1，15 分钟级
    └── ETTm2：站点 2，15 分钟级
```
而：
```text
Benchmark
=
公开数据集
+
统一任务设置
+
统一训练/测试划分
+
统一预测长度
+
统一评价指标
```
你当前的实验可以表述为：
> 本实验首先在标准时间序列预测数据集 ETTh1 上，对 TimesFM 2.5 执行单变量零样本快速验证，使用过去 512 小时的油温序列预测未来 96 小时油温。该实验用于验证基础模型的本地运行流程并获得初步结果；后续将通过统一滚动窗口与多个模型比较，形成完整 benchmark 评估。