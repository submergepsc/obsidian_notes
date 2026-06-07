# 这段代码整体在做什么
这段程序的任务是：
> 给 TimesFM 一条已经观察到的历史时间序列，让它**不经过重新训练**，直接预测未来 24 个时间点，并同时给出预测的不确定性范围。
代码里的例子没有使用 ETT 数据，而是人为构造了一条正弦曲线：
```python
np.sin(np.linspace(0, 20, 200))
```
模型把这 200 个连续数值当作“过去已经发生的历史”，然后预测接下来的 24 个数值。
完整流程是：
```text
构造一条历史序列
        ↓
加载已经预训练好的 TimesFM 2.5
        ↓
设置模型最多读取多少历史、最多预测多远
        ↓
输入历史序列
        ↓
输出未来 24 步的点预测 + 概率区间预测
```
TimesFM 2.5 是 Google Research 发布的预训练时间序列基础模型，当前 PyTorch 版本使用约 2 亿参数；它支持零样本预测与分位数预测输出。([GitHub](https://github.com/google-research/timesfm?utm_source=chatgpt.com "TimesFM $Time Series Foundation Model$ is a pretrained ..."))
# 1. 导入需要的库
```python
import torch, numpy as np, timesfm
```
等价于：
```python
import torch
import numpy as np
import timesfm
```
分别表示：

|库|作用|
|---|---|
|`torch`|PyTorch，负责运行神经网络模型|
|`numpy`，缩写为 `np`|处理数值数组，构造输入时间序列|
|`timesfm`|Google 官方 TimesFM 模型代码|

在你的 ETTh1 实验中：
```python
import numpy as np
```
负责保存油温数值，例如：
```python
[37.5, 37.8, 38.1, 38.0, ...]
```
而：
```python
import timesfm
```
负责调用已经训练好的时间序列预测模型。
# 2. 设置矩阵计算精度
```python
torch.set_float32_matmul_precision("high")
```
神经网络运行过程中需要大量矩阵乘法。这一行告诉 PyTorch：
> 对 `float32` 类型的矩阵运算，使用较高精度的计算设置。
它的作用主要是让模型在现代 GPU 上运行得更合适。它不会改变：
- 你输入的数据含义；
- 预测长度；
- 模型是否训练；
- ETT 数据集的内容。
可以先把它理解为：
```text
运行模型前的一项计算环境设置
```
# 3. 加载预训练模型
```python
model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
    "google/timesfm-2.5-200m-pytorch"
)
```
这部分你刚刚已经接触过，可以拆成四块理解：

|代码部分|含义|
|---|---|
|`model =`|把加载好的模型保存到变量 `model` 中|
|`TimesFM_2p5_200M_torch`|TimesFM 2.5、约 2 亿参数、PyTorch 版本|
|`from_pretrained(...)`|加载已经训练完成的模型参数|
|`"google/timesfm-2.5-200m-pytorch"`|Hugging Face 上的官方模型仓库名称|

执行这一行时，第一次会下载：
```text
config.json
model.safetensors
```
其中：

|文件|含义|
|---|---|
|`config.json`|模型结构与参数配置|
|`model.safetensors`|模型已经学习到的权重，约 925 MB|

这一步不是训练，而是：
```text
下载并加载一个已经训练好的预测模型
```
所以你的 ETTh1 实验属于：
```text
Zero-shot forecasting
零样本预测
```
即 TimesFM 没有针对你的 `ETTh1.csv` 重新训练，而是直接读取历史油温并预测未来油温。
# 4. 配置预测行为：`model.compile(...)`
```python
model.compile(timesfm.ForecastConfig(
    max_context=1024,
    max_horizon=256,
    normalize_inputs=True,
    use_continuous_quantile_head=True,
    force_flip_invariance=True,
    infer_is_positive=True,
    fix_quantile_crossing=True,
))
```
这一部分不是重新训练模型，而是在说明：
> 这次调用模型预测时，允许它读取多长的历史、预测多远、是否输出概率区间，以及如何约束结果。
## 4.1 `max_context=1024`
```python
max_context=1024
```
`context` 指模型看到的**历史序列长度**。
例如，假设你给模型过去 200 个数据点：
```python
inputs=[
    np.sin(np.linspace(0, 20, 200))
]
```
那么：
```text
实际输入历史长度 = 200
允许的最大历史长度 = 1024
```
因为：
```text
200 < 1024
```
所以这个输入可以处理。
在你的 ETTh1 实验中：
```python
CONTEXT = 512
```
表示你只给模型过去 512 小时的油温：
```text
过去 512 小时 OT
        ↓
预测未来 96 小时 OT
```
你可以将两种配置进行对比：

|代码示例|含义|
|---|---|
|`max_context=1024`|模型最多准备处理 1024 个历史点|
|你的脚本 `CONTEXT=512`|实际只输入过去 512 个小时|

`max_context` 是允许的最大历史窗口，并不表示你必须输入满 1024 个值。
## 4.2 `max_horizon=256`
```python
max_horizon=256
```
`horizon` 指要预测的未来长度。
这一项表示：
```text
本次配置最多允许模型预测未来 256 个时间点
```
但下面真正预测时写的是：
```python
model.forecast(horizon=24, ...)
```
所以这次实际只预测：
```text
未来 24 个时间点
```
两者关系是：
```text
实际预测长度 <= 配置允许的最大预测长度
```
即：
```text
24 <= 256
```
所以合法。
在你的 ETTh1 实验中：
```python
HORIZON = 96
```
由于 ETTh1 是小时级数据，因此：
```text
预测未来 96 个时间点
=
预测未来 96 小时
=
预测未来 4 天
```
## 4.3 `normalize_inputs=True`
```python
normalize_inputs=True
```
这表示模型在预测之前，会对输入时间序列进行内部标准化处理。
为什么要标准化？
不同时间序列的数值范围差异可能很大，例如：

|序列|数值范围示例|
|---|--:|
|油温|`20` 到 `60`|
|商店销量|`0` 到 `5000`|
|股票成交量|`100000` 到 `10000000`|

模型如果直接处理差异特别大的数值，预测可能不稳定。因此它会先在内部处理尺度差异，再把预测结果转换回原来的量纲。
对于你的 ETTh1 油温预测：
```text
输入仍然是原始 OT 油温
输出仍然是原始油温尺度
```
你不需要手动把油温改成百分比或者减去均值。
## 4.4 `use_continuous_quantile_head=True`
```python
use_continuous_quantile_head=True
```
这一项非常重要。
普通点预测只输出一个未来值，例如：
```text
未来第 1 小时油温 = 38.2
```
但是未来存在不确定性。打开这一项以后，模型除了输出一个中心预测，还会输出多个分位数：
```text
P10、P20、P30、...、P90
```
例如未来第一个小时，模型可能输出：

|输出|数值示例|含义|
|---|--:|---|
|P10|`36.8`|大约有 10\% 的可能低于该值|
|P50|`38.2`|中位数预测|
|P90|`40.1`|大约有 90\% 的可能低于该值|

于是：
```text
P10 到 P90
```
可以构成一个预测区间：
```text
未来油温大致可能落在 36.8 到 40.1 之间
```
TimesFM 2.5 引入了用于概率预测的连续分位数预测头，官方说明其可以输出长预测窗口上的分位数预测。([GitHub](https://github.com/google-research/timesfm?utm_source=chatgpt.com "TimesFM $Time Series Foundation Model$ is a pretrained ..."))
## 4.5 `force_flip_invariance=True`
```python
force_flip_invariance=True
```
这一项用于提高模型对数值方向变化的稳定性。
简单理解：
> 如果一条序列整体方向被翻转，例如所有数值乘以 `-1`，模型的预测行为也应当相应翻转，而不是出现完全不同的异常结果。
这一项属于模型推理时的稳健性约束。对你现在的 ETTh1 油温实验，可以保留官方示例中的设置，不需要单独修改。
## 4.6 `infer_is_positive=True`
```python
infer_is_positive=True
```
这一项用于处理**理论上不应出现负值**的时间序列。
例如：

|数据类型|能否为负数|
|---|--:|
|商品销量|通常不能|
|电力需求|通常不能|
|变压器油温摄氏度|在 ETT 数据范围中通常为正|
|收益率变化|可以为负|
|温度异常偏差|可以为负|

你的 `OT` 油温序列通常是正值，因此保留：
```python
infer_is_positive=True
```
是合理的。
但是，如果未来你预测的是：
```text
价格涨跌幅、误差、温度变化量、中心化后的序列
```
这种可能包含负值的数据，就不能盲目打开这一项。
## 4.7 `fix_quantile_crossing=True`
```python
fix_quantile_crossing=True
```
正常情况下，分位数必须满足：
```text
P10 <= P20 <= P30 <= ... <= P90
```
例如这是一组合理结果：

|分位数|预测油温|
|---|--:|
|P10|`36.8`|
|P50|`38.2`|
|P90|`40.1`|

但是模型有时可能产生不合理结果：

|分位数|预测油温|
|---|--:|
|P10|`39.0`|
|P50|`38.2`|
|P90|`37.5`|

这意味着：
```text
低分位数比高分位数还大
```
在概率含义上是不合理的，这种现象叫：
```text
Quantile Crossing
分位数交叉
```
打开：
```python
fix_quantile_crossing=True
```
就是让输出尽量满足：
```text
P10 <= P20 <= ... <= P90
```
官方 TimesFM 文档也将该设置解释为确保分位数按顺序排列。([GitHub](https://github.com/google-research/timesfm/blob/master/timesfm-forecasting/SKILL.md?utm_source=chatgpt.com "timesfm/timesfm-forecasting/SKILL.md at master"))
# 5. 构造一条假的历史时间序列
```python
np.sin(np.linspace(0, 20, 200))
```
这是整个示例中最容易看不懂的部分。
## 5.1 `np.linspace(0, 20, 200)`
```python
np.linspace(0, 20, 200)
```
表示：
> 在 `0` 到 `20` 之间，均匀生成 200 个数。
例如简化版本：
```python
np.linspace(0, 10, 6)
```
结果大致是：
```python
array([0., 2., 4., 6., 8., 10.])
```
所以：
```python
np.linspace(0, 20, 200)
```
会生成：
```text
200 个连续递增的位置点
```
## 5.2 `np.sin(...)`
```python
np.sin(np.linspace(0, 20, 200))
```
再对这 200 个位置计算正弦值，就会得到一条上下周期波动的曲线：
```text
      /\        /\        /\
     /  \      /  \      /
----/----\----/----\----/----
   /      \  /      \  /
  /        \/        \/
```
这条序列类似：
```python
[0.00, 0.10, 0.20, 0.30, ..., -0.45, ...]
```
其特点是：
- 一共有 200 个历史观测值；
- 数值在 `-1` 到 `1` 附近波动；
- 具有明显周期规律；
- 只是演示数据，不是真实业务数据。
## 5.3 这 200 个点在模型眼里是什么
模型并不知道它是用 `sin` 函数生成的。
模型只看到：
```text
历史序列：
第 1 个点，第 2 个点，第 3 个点，...，第 200 个点
```
然后模型尝试预测：
```text
第 201 个点到第 224 个点
```
因为：
```python
horizon=24
```
# 6. 真正进行预测：`model.forecast(...)`
```python
point, quantiles = model.forecast(
    horizon=24,
    inputs=[
        np.sin(np.linspace(0, 20, 200)),
    ]
)
```
这里有两个关键参数：

|参数|含义|
|---|---|
|`horizon=24`|预测未来 24 个时间点|
|`inputs=[...]`|输入一条或多条历史时间序列|

## 6.1 `horizon=24` 的含义
```python
horizon=24
```
不是固定表示 24 小时，而是：
```text
预测未来 24 个数据间隔
```
它代表多久，取决于原始数据的采样频率。

|输入数据频率|`horizon=24` 的含义|
|---|---|
|每小时一条数据|未来 24 小时|
|每 15 分钟一条数据|未来 6 小时|
|每天一条数据|未来 24 天|
|每周一条数据|未来 24 周|

因此：
- 对 `ETTh1` 而言，`horizon=24` 就是预测未来 24 小时；
- 对 `ETTm1` 而言，`horizon=24` 就是预测未来 24 个 15 分钟，即未来 6 小时。
你的快速实验中使用：
```python
HORIZON = 96
```
对于 `ETTh1` 来说，就是：
```text
未来 96 小时 = 未来 4 天
```
## 6.2 为什么 `inputs` 外面有中括号
代码写的是：
```python
inputs=[
    np.sin(np.linspace(0, 20, 200)),
]
```
注意有两层结构：
```python
inputs = [
    一条时间序列
]
```
TimesFM 支持一次预测多条独立时间序列，所以 `inputs` 必须是一个列表。
例如，预测一条序列：
```python
inputs = [
    第一条序列
]
```
预测三条序列：
```python
inputs = [
    第一条序列,
    第二条序列,
    第三条序列,
]
```
官方 README 的示例输入了两条独立序列，因此它的输出第一维为 `2`；你贴出来的代码只输入一条正弦序列，因此输出第一维为 `1`。([GitHub](https://github.com/google-research/timesfm?utm_source=chatgpt.com "TimesFM $Time Series Foundation Model$ is a pretrained ..."))
# 7. 非常重要：`inputs` 中的多条序列不是多个特征
这一点与你的 ETT 数据直接相关。
假设你写：
```python
inputs = [
    df["HUFL"].to_numpy(),
    df["HULL"].to_numpy(),
    df["OT"].to_numpy(),
]
```
这不表示：
```text
使用 HUFL 和 HULL 帮助预测 OT
```
而表示：
```text
分别预测 HUFL 自己的未来
分别预测 HULL 自己的未来
分别预测 OT 自己的未来
```
也就是三条**独立单变量预测任务**。
你当前正确的单变量油温预测写法是：
```python
inputs = [
    df["OT"].to_numpy()
]
```
含义是：
```text
输入历史 OT
预测未来 OT
```
如果以后要让模型同时利用：
```text
HUFL、HULL、MUFL、MULL、LUFL、LULL
```
来辅助预测未来 `OT`，那就属于协变量预测，需要使用 TimesFM 的 XReg / covariates 相关接口，而不是简单把各列放进 `inputs` 列表。TimesFM 官方说明，外部协变量功能需要使用 `forecast_with_covariates()` 相关工作流。([GitHub](https://github.com/google-research/timesfm/blob/master/timesfm-forecasting/SKILL.md?utm_source=chatgpt.com "timesfm/timesfm-forecasting/SKILL.md at master"))
# 8. 输出一：`point`
```python
point, quantiles = model.forecast(...)
```
其中：
```python
point
```
是点预测结果。
你的示例中：
```python
point.shape == (1, 24)
```
这个形状可以拆解为：

|维度|数值|含义|
|---|--:|---|
|第 1 维|`1`|你输入了 1 条历史序列|
|第 2 维|`24`|你要求预测未来 24 个时间点|

因此：
```python
point[0]
```
表示：
```text
第一条序列未来 24 个点的中心预测
```
例如可能类似：
```python
array([
    0.91, 0.85, 0.77, 0.68, ... 
])
```
其中：

|表达式|含义|
|---|---|
|`point[0, 0]`|第一条序列，未来第 1 个时间点的点预测|
|`point[0, 1]`|第一条序列，未来第 2 个时间点的点预测|
|`point[0, 23]`|第一条序列，未来第 24 个时间点的点预测|

按照 TimesFM 官方 forecasting 文档，`point_forecast` 对应中位数预测，即 P50。([GitHub](https://github.com/google-research/timesfm/blob/master/timesfm-forecasting/SKILL.md?utm_source=chatgpt.com "timesfm/timesfm-forecasting/SKILL.md at master"))
# 9. 输出二：`quantiles`
```python
quantiles
```
表示模型输出的概率预测结果。
你的示例中：
```python
quantiles.shape == (1, 24, 10)
```
三个维度分别表示：

|维度|数值|含义|
|---|--:|---|
|第 1 维|`1`|一条输入序列|
|第 2 维|`24`|未来 24 个时间点|
|第 3 维|`10`|每个未来时间点输出 10 个统计预测值|

需要注意：**第三维的 10 个值不是 P10 到 P100，也不是十个纯分位数。**
官方 README 对输出的说明是：
```text
quantile_forecast 的最后一维：
第 0 个值是 mean；
后面依次是 P10、P20、...、P90。
```
官方 forecasting 文档进一步说明，P50 对应 `point_forecast`。([GitHub](https://github.com/google-research/timesfm?utm_source=chatgpt.com "TimesFM $Time Series Foundation Model$ is a pretrained ...")) ([GitHub](https://github.com/google-research/timesfm/blob/master/timesfm-forecasting/SKILL.md?utm_source=chatgpt.com "timesfm/timesfm-forecasting/SKILL.md at master"))
具体索引如下：

|索引|代码|含义|
|--:|---|---|
|`0`|`quantiles[:, :, 0]`|Mean，均值预测|
|`1`|`quantiles[:, :, 1]`|P10|
|`2`|`quantiles[:, :, 2]`|P20|
|`3`|`quantiles[:, :, 3]`|P30|
|`4`|`quantiles[:, :, 4]`|P40|
|`5`|`quantiles[:, :, 5]`|P50，中位数预测|
|`6`|`quantiles[:, :, 6]`|P60|
|`7`|`quantiles[:, :, 7]`|P70|
|`8`|`quantiles[:, :, 8]`|P80|
|`9`|`quantiles[:, :, 9]`|P90|

也就是说：
```python
point[0]
```
与：
```python
quantiles[0, :, 5]
```
应当都表示未来 24 步的 P50 中位数预测。
你可以在本地验证：
```python
print(np.max(np.abs(point[0] - quantiles[0, :, 5])))
```
如果结果接近：
```text
0.0
```
就说明两者相同或只有极小浮点误差。
# 10. 怎样读取某一个未来时间点的预测结果
假设你想查看：
```text
第一条序列未来第 1 个时间点
```
可以写：
```python
future_step_1 = {
    "mean": quantiles[0, 0, 0],
    "p10": quantiles[0, 0, 1],
    "p50": quantiles[0, 0, 5],
    "p90": quantiles[0, 0, 9],
}
print(future_step_1)
```
可能输出类似：
```python
{
    "mean": 0.84,
    "p10": 0.62,
    "p50": 0.85,
    "p90": 1.04
}
```
这可以解释为：

|预测值|含义|
|---|---|
|`mean = 0.84`|平均意义下的预测中心|
|`p10 = 0.62`|偏低情形下的预测边界|
|`p50 = 0.85`|中位数点预测|
|`p90 = 1.04`|偏高情形下的预测边界|

因此：
```text
P10 到 P90
```
构成了一个中间 80\% 的预测区间：
```text
[0.62, 1.04]
```
# 11. 为什么要同时输出点预测和分位数预测
假设模型预测未来一小时油温。
只输出点预测：

|输出|值|
|---|--:|
|预测油温|`38.2`|

你只能知道模型认为最典型的未来值大约是 `38.2`。
如果输出分位数：

|输出|值|
|---|--:|
|P10|`36.9`|
|P50|`38.2`|
|P90|`41.0`|

你还能知道：
```text
模型认为未来油温有一定不确定性，
中间 80\% 的预测范围大约为 36.9 到 41.0。
```
这对于变压器油温非常有用：
- 点预测可以评价通常情况下预测准不准；
- P90 可以帮助观察较高温度风险；
- P10–P90 区间可以观察模型对不确定性的估计。
# 12. 把示例代码翻译成人话
原代码：
```python
import torch, numpy as np, timesfm
torch.set_float32_matmul_precision("high")
model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
    "google/timesfm-2.5-200m-pytorch"
)
model.compile(timesfm.ForecastConfig(
    max_context=1024, max_horizon=256, normalize_inputs=True,
    use_continuous_quantile_head=True, force_flip_invariance=True,
    infer_is_positive=True, fix_quantile_crossing=True,
))
point, quantiles = model.forecast(horizon=24, inputs=[
    np.sin(np.linspace(0, 20, 200)),
])
```
逐句翻译就是：
```text
导入 PyTorch、NumPy 和 TimesFM。
设置 PyTorch 的 float32 矩阵运算配置。
下载并加载 Google 已经训练好的 TimesFM 2.5 PyTorch 模型。
配置模型：
最多读取 1024 个历史数据点；
最多预测未来 256 个数据点；
内部对输入进行归一化；
同时输出分位数概率预测；
启用若干预测稳定性与合理性约束。
构造一条长度为 200 的正弦波历史序列。
把这条历史序列交给 TimesFM，
让模型预测未来 24 个点。
最终得到：
point：未来 24 点的中位数预测；
quantiles：未来 24 点的均值、P10 到 P90 预测。
```
# 13. 将它替换成你的 ETTh1 油温数据
示例中这一部分：
```python
np.sin(np.linspace(0, 20, 200))
```
只是假的历史数据。
在你的 ETTh1 实验中，应该替换为：
```python
context
```
其中 `context` 是过去 512 小时的真实油温：
```python
df = pd.read_csv("quickrun/ETTh1.csv", parse_dates=["date"])
values = df["OT"].astype("float32").to_numpy()
CONTEXT = 512
HORIZON = 96
context = values[-(CONTEXT + HORIZON):-HORIZON]
y_true = values[-HORIZON:]
point, quantiles = model.forecast(
    horizon=HORIZON,
    inputs=[context],
)
```
这一段的含义是：
```text
values
=
ETTh1 中所有历史油温
context
=
测试区间之前的 512 小时真实油温
y_true
=
接下来 96 小时已经发生的真实油温，用于评价模型
point
=
TimesFM 预测出的未来 96 小时 P50 油温
quantiles
=
TimesFM 预测出的未来 96 小时均值与 P10-P90 油温范围
```
对应图示为：
```text
过去 512 小时 OT                          未来 96 小时 OT
┌──────────────────────────────┐         ┌──────────────────────┐
│ 输入给 TimesFM 的历史数据      │  ───→   │ 模型预测 point / P10-P90 │
└──────────────────────────────┘         └──────────────────────┘
                                                 │
                                                 ↓
                                      与真实 y_true 比较计算误差
```
# 14. 你脚本里的输出应当怎样取
对于你的 `ETTh1 / OT / HORIZON=96` 实验：
```python
point, quantiles = model.forecast(
    horizon=96,
    inputs=[context],
)
```
输出尺寸应为：
```python
point.shape
# (1, 96)
quantiles.shape
# (1, 96, 10)
```
具体取值方式：
```python
point_pred = point[0]             # 未来 96 小时的 P50 点预测
mean_pred = quantiles[0, :, 0]    # 均值预测
p10 = quantiles[0, :, 1]          # P10
p50 = quantiles[0, :, 5]          # P50
p90 = quantiles[0, :, 9]          # P90
```
可以打印前五个预测结果：
```python
for h in range(5):
    print(
        f"未来第 {h+1} 小时: "
        f"P10={p10[h]:.3f}, "
        f"P50={p50[h]:.3f}, "
        f"P90={p90[h]:.3f}"
    )
```
例如得到：
```text
未来第 1 小时: P10=38.120, P50=39.245, P90=40.780
未来第 2 小时: P10=37.960, P50=39.110, P90=40.920
...
```
含义就是：
```text
未来第 1 小时，模型的中位数油温预测为 39.245；
偏低预测边界约为 38.120；
偏高预测边界约为 40.780。
```
# 15. 你的当前实验中各变量的对应关系
|示例代码中的概念|示例里的内容|你的 ETTh1 实验中的内容|
|---|---|---|
|历史序列|`np.sin(np.linspace(0, 20, 200))`|过去 512 小时的 `OT`|
|历史长度|`200`|`512`|
|预测长度|`24`|`96`|
|时间单位|没有真实单位|小时|
|点预测输出|未来 24 点 P50|未来 96 小时 P50 油温|
|分位数输出|未来 24 点 P10–P90|未来 96 小时 P10–P90 油温|
|真实值|示例没有提供|测试集中的真实 `OT`|
|能否计算 MAE|示例不能直接评价|你的实验可以评价|

## 最关键的三个理解
### 第一，模型输入的不是表格，而是一条时间序列
你的当前任务中输入是：
```python
inputs=[context]
```
其中 `context` 只是：
```text
过去 512 小时的 OT 数值
```
### 第二，`horizon` 表示预测多少个未来时间点
你的 `ETTh1` 是小时级数据，所以：
```python
horizon=96
```
表示：
```text
预测未来 96 小时，也就是未来 4 天
```
### 第三，`point` 和 `quantiles` 的区别
|输出|作用|
|---|---|
|`point[0]`|一条中心预测曲线，即 P50|
|`quantiles[0, :, 1]`|P10 下边界曲线|
|`quantiles[0, :, 5]`|P50 中位数曲线|
|`quantiles[0, :, 9]`|P90 上边界曲线|

你的预测图中：
```python
plt.plot(test_time, point_pred, label="TimesFM point forecast")
plt.fill_between(
    test_time,
    p10,
    p90,
    alpha=0.2,
    label="TimesFM P10-P90 interval",
)
```
表示：
```text
中间那条线 = TimesFM 认为最典型的未来油温走势
阴影范围     = TimesFM 对未来不确定性的估计
```