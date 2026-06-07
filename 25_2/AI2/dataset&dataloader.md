
```python
import torch
from torch.utils.data import DataLoader, Dataset

```

这行导入：
```python
from torch.utils.data import DataLoader, Dataset
```
意思是从 PyTorch 的数据处理模块里导入两个核心工具：

| 名称           | 中文理解  | 作用                            |
| ------------ | ----- | ----------------------------- |
| `Dataset`    | 数据集类  | 负责定义“数据从哪里来、怎么取一条数据”          |
| `DataLoader` | 数据加载器 | 负责把数据集按批次取出、打乱、多进程读取、拼成 batch |

PyTorch 官方教程也把它们称为两个基础数据原语：`Dataset` 保存样本及其标签，`DataLoader` 在 `Dataset` 外面包一层可迭代对象，方便训练时逐批读取数据。([PyTorch Docs](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html?utm_source=chatgpt.com "Datasets & DataLoaders — PyTorch Tutorials 2.12.0+ ..."))
## 1. 为什么需要 `Dataset` 和 `DataLoader`
训练神经网络时，通常不是一次性把所有数据丢进模型，而是分批训练。
比如你有 10000 条数据，每次取 32 条训练：
```python
for x, y in dataloader:
    pred = model(x)
    loss = loss_fn(pred, y)
```
这里的核心问题是：
1. 数据怎么读取？
2. 标签怎么对应？
3. 每次取多少条？
4. 要不要打乱？
5. 图片、文本、时间序列怎么预处理？
6. 数据很多时，怎么加快读取？
`Dataset` 解决前两个问题，`DataLoader` 解决后面几个问题。
# 2. `Dataset` 是什么
`Dataset` 可以理解为一个**数据集模板类**。
你一般不会直接使用 `Dataset`，而是自己写一个类继承它：
```python
from torch.utils.data import Dataset
class MyDataset(Dataset):
    def __init__(self):
        pass
    def __len__(self):
        pass
    def __getitem__(self, index):
        pass
```
它主要要求你实现两个方法：
```python
def __len__(self):
```
返回数据集总共有多少条数据。
```python
def __getitem__(self, index):
```
根据索引 `index` 返回一条数据。
## 3. 一个最简单的 `Dataset` 示例
假设现在有 4 条训练数据：
```python
import torch
from torch.utils.data import Dataset
class SimpleDataset(Dataset):
    def __init__(self):
        self.x = torch.tensor([
            [1.0],
            [2.0],
            [3.0],
            [4.0]
        ])
        self.y = torch.tensor([
            [2.0],
            [4.0],
            [6.0],
            [8.0]
        ])
    def __len__(self):
        return len(self.x)
    def __getitem__(self, index):
        return self.x[index], self.y[index]
```
这表示：
```python
x = 1.0 -> y = 2.0
x = 2.0 -> y = 4.0
x = 3.0 -> y = 6.0
x = 4.0 -> y = 8.0
```
使用：
```python
dataset = SimpleDataset()
print(len(dataset))
print(dataset[0])
```
输出大致是：
```python
4
(tensor([1.]), tensor([2.]))
```
也就是说，`Dataset` 本质上要让你的数据支持这种访问方式：
```python
dataset[0]
dataset[1]
dataset[2]
```
# 4. `DataLoader` 是什么
`DataLoader` 是数据加载器。
官方文档中说，`DataLoader` 会把数据集和采样器组合起来，并提供一个可迭代对象；它支持 map-style 和 iterable-style 数据集，也支持单进程或多进程加载、加载顺序控制、自动批处理等功能。([PyTorch Docs](https://docs.pytorch.org/docs/stable/data.html?utm_source=chatgpt.com "torch.utils.data"))
简单说，`DataLoader` 可以帮你：

|功能|解释|
|---|---|
|`batch_size`|每次取多少条数据|
|`shuffle`|是否打乱数据|
|`num_workers`|是否使用多进程加速读取|
|`drop_last`|最后一批不够 batch size 时是否丢弃|
|`collate_fn`|自定义如何把多条数据拼成一个 batch|

## 5. `Dataset` 配合 `DataLoader`
继续使用刚才的 `SimpleDataset`：
```python
from torch.utils.data import DataLoader
dataset = SimpleDataset()
dataloader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)
for batch_x, batch_y in dataloader:
    print("batch_x:", batch_x)
    print("batch_y:", batch_y)
```
可能输出：
```python
batch_x: tensor([[3.],
                 [1.]])
batch_y: tensor([[6.],
                 [2.]])
batch_x: tensor([[4.],
                 [2.]])
batch_y: tensor([[8.],
                 [4.]])
```
注意这里设置了：
```python
batch_size=2
```
所以每次取 2 条数据。
设置了：
```python
shuffle=True
```
所以数据顺序可能被打乱。
# 6. 它们在训练代码中的位置
标准训练流程一般是这样：
```python
dataset = MyDataset(...)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
for epoch in range(10):
    for x, y in dataloader:
        pred = model(x)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```
这里可以这样理解：
```python
Dataset
```
负责管理原始数据。
```python
DataLoader
```
负责一批一批地把数据拿出来。
```python
model
```
负责预测。
```python
loss_fn
```
负责计算误差。
```python
optimizer
```
负责更新参数。
# 7. `Dataset` 的三个核心部分
一般自定义 `Dataset` 时，结构如下：
```python
class MyDataset(Dataset):
    def __init__(self, data_path):
        # 1. 初始化数据路径、读取文件名、读取标签等
        pass
    def __len__(self):
        # 2. 返回数据集长度
        pass
    def __getitem__(self, index):
        # 3. 根据 index 返回一条数据
        pass
```
## `__init__`
通常用来保存路径、读取标签文件、初始化 transform。
例如：
```python
def __init__(self, csv_path):
    self.data = pd.read_csv(csv_path)
```
## `__len__`
告诉 PyTorch 数据集有多少条。
例如：
```python
def __len__(self):
    return len(self.data)
```
## `__getitem__`
根据索引返回一条样本。
例如：
```python
def __getitem__(self, index):
    x = self.data.iloc[index, :-1].values
    y = self.data.iloc[index, -1]
    return x, y
```
# 8. 更接近真实场景的例子：读取表格数据
假设你的数据是这样的：

|feature1|feature2|label|
|---|---|---|
|1.2|3.4|0|
|2.1|1.8|1|
|3.3|4.5|0|

可以这样写：
```python
import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
class TableDataset(Dataset):
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.x = self.data.iloc[:, :-1].values
        self.y = self.data.iloc[:, -1].values
        self.x = torch.tensor(self.x, dtype=torch.float32)
        self.y = torch.tensor(self.y, dtype=torch.long)
    def __len__(self):
        return len(self.x)
    def __getitem__(self, index):
        return self.x[index], self.y[index]
dataset = TableDataset("data.csv")
dataloader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)
for x, y in dataloader:
    print(x.shape)
    print(y.shape)
```
如果 `batch_size=32`，那么：
```python
x.shape
```
可能是：
```python
torch.Size([32, 2])
```
表示这一批有 32 条数据，每条数据有 2 个特征。
```python
y.shape
```
可能是：
```python
torch.Size([32])
```
表示这一批有 32 个标签。
# 9. `DataLoader` 常用参数详解
## `dataset`
传入你定义好的数据集。
```python
DataLoader(dataset)
```
## `batch_size`
每次取多少条数据。
```python
DataLoader(dataset, batch_size=32)
```
如果总共有 100 条数据，`batch_size=32`，那么每个 epoch 大约有 4 个 batch：
```python
32 + 32 + 32 + 4
```
## `shuffle`
是否打乱数据。
```python
DataLoader(dataset, shuffle=True)
```
训练集一般设置：
```python
shuffle=True
```
测试集一般设置：
```python
shuffle=False
```
原因是训练时打乱数据可以减少模型对顺序的依赖，而测试时通常希望结果可复现。
## `num_workers`
用几个子进程读取数据。
```python
DataLoader(dataset, num_workers=4)
```
一般：
```python
num_workers=0
```
表示主进程读取，最稳定，但可能慢。
```python
num_workers=2 或 4
```
表示开多个进程并行读取，图片数据集常用。
如果数据很小，`num_workers` 太大反而可能变慢。
## `drop_last`
最后一个 batch 不够指定大小时，是否丢掉。
```python
DataLoader(dataset, batch_size=32, drop_last=True)
```
假设有 100 条数据，`batch_size=32`：
不丢弃时：
```python
32 + 32 + 32 + 4
```
丢弃时：
```python
32 + 32 + 32
```
在 BatchNorm 或某些对 batch 大小敏感的训练中，`drop_last=True` 有时更稳定。
## `collate_fn`
自定义如何把多条数据合并成一个 batch。
默认情况下，`DataLoader` 会自动把多条 tensor 堆叠起来。
但是如果你的数据长度不一样，比如 NLP 文本、时间序列长度不同，就可能需要自己写 `collate_fn`。
例如：
```python
def my_collate_fn(batch):
    xs, ys = zip(*batch)
    return xs, ys
dataloader = DataLoader(
    dataset,
    batch_size=4,
    collate_fn=my_collate_fn
)
```
# 10. `Dataset` 和 `DataLoader` 的关系
可以这样理解：
```text
Dataset：一本书
DataLoader：帮你按页数、顺序、批量方式翻书的人
```
或者：
```text
Dataset：仓库，里面存着所有样本
DataLoader：搬运工，每次搬一批数据给模型
```
更具体一点：
```text
Dataset[index] 取一条数据
DataLoader 每次取一批数据
```
# 11. `Dataset` 不一定要一次性读取所有数据
这是一个容易误解的地方。
你可以在 `__init__` 里面只保存文件路径，不真正读取全部数据。
例如图片任务中，常见写法是：
```python
class ImageDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform
    def __len__(self):
        return len(self.image_paths)
    def __getitem__(self, index):
        image_path = self.image_paths[index]
        label = self.labels[index]
        image = Image.open(image_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label
```
这样只有在取到某个 `index` 时，才会真正读取对应图片。
这对于大规模图片数据非常重要，因为不可能一次性把所有图片都放进内存。
# 12. 什么时候需要自己写 `Dataset`
以下情况通常需要自己写：

|场景|是否需要自定义 Dataset|
|---|---|
|数据是简单 tensor|不一定|
|数据在 csv 里|通常需要|
|数据是图片文件夹|通常需要|
|数据是时间序列窗口|通常需要|
|数据需要复杂预处理|通常需要|
|数据来自多个文件|通常需要|

如果数据已经是 tensor，可以用 PyTorch 自带的 `TensorDataset`，不一定要自己写类。
例如：
```python
from torch.utils.data import TensorDataset, DataLoader
x = torch.randn(100, 10)
y = torch.randint(0, 2, (100,))
dataset = TensorDataset(x, y)
dataloader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)
```
# 13. 在时间序列预测里的常见写法
你之前提到过用过去一段时间预测未来一段时间，这种情况通常也会用 `Dataset`。
例如：用过去 512 个点预测未来 96 个点。
```python
class TimeSeriesDataset(Dataset):
    def __init__(self, values, input_len=512, pred_len=96):
        self.values = torch.tensor(values, dtype=torch.float32)
        self.input_len = input_len
        self.pred_len = pred_len
    def __len__(self):
        return len(self.values) - self.input_len - self.pred_len + 1
    def __getitem__(self, index):
        x_start = index
        x_end = index + self.input_len
        y_start = x_end
        y_end = x_end + self.pred_len
        x = self.values[x_start:x_end]
        y = self.values[y_start:y_end]
        return x, y
```
使用：
```python
dataset = TimeSeriesDataset(values, input_len=512, pred_len=96)
dataloader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)
```
这里：
```python
x
```
表示过去 512 个时间点。
```python
y
```
表示未来 96 个时间点。
# 14. 常见错误
## 错误 1：忘记继承 `Dataset`
错误写法：
```python
class MyDataset:
    ...
```
推荐写法：
```python
class MyDataset(Dataset):
    ...
```
## 错误 2：忘记写 `__len__`
如果没有 `__len__`，`DataLoader` 不知道数据集有多长。
## 错误 3：忘记写 `__getitem__`
如果没有 `__getitem__`，`DataLoader` 不知道怎么取数据。
## 错误 4：返回的数据类型不对
比如返回的是字符串、列表、numpy 数组，有时模型不能直接处理。
一般建议在 `__getitem__` 里返回 tensor：
```python
return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.long)
```
不过如果你用了 `transform`，也可以在 transform 里转 tensor。
## 错误 5：标签类型不对
分类任务中，`CrossEntropyLoss` 通常要求标签是 `torch.long` 类型，并且标签形状通常是：
```python
[batch_size]
```
而不是：
```python
[batch_size, 1]
```
# 15. 总结
这行代码：
```python
from torch.utils.data import DataLoader, Dataset
```
导入的是 PyTorch 中最常用的数据处理工具。
核心关系是：
```text
Dataset：定义数据怎么取
DataLoader：定义数据怎么批量送进模型
```
最重要的是记住：
```python
class MyDataset(Dataset):
    def __len__(self):
        return 数据总数
    def __getitem__(self, index):
        return 第 index 条数据
```
然后用：
```python
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```
训练时：
```python
for x, y in dataloader:
    ...
```
从实际写代码角度看，`Dataset` 是你组织数据的地方，`DataLoader` 是你训练模型时真正循环读取数据的地方。