`conda env list`查看多少个python环境，或者`conda info --envs`;
`conda activate env_name`激活某个环境
`conda deactivate`退出这个环境

#  配置特殊问题
 这是一个非常经典的 Python “依赖地狱（Dependency Hell）”问题。遇到这个红色的 `ERROR: ResolutionImpossible` 报错，真的很容易让人抓狂，但其实背后的逻辑很清晰。

### 为什么会报错？（问题出在哪）

报错信息里最关键的一句是：`pywin32` **no matching distributions available for your environment**。

1. **死板的依赖锁**：Obsidian 终端插件依赖的 `pywinctl` 这个库，它的作者非常“死板”地把底层库 `pywin32` 的版本死死钉在了 `==302`。
2. **Python 版本太新**：你目前使用的 Python 版本（无论是之前的 3.13、3.14 还是 3.15）都非常新。而 `pywin32` 是一个深度调用 Windows C API 的底层库，它的 `302` 老版本根本没有为这些最新的 Python 版本编译过对应的安装包（Wheel）。
3. **陷入死局**：`pip` 发现你想装 `pywinctl` -> 必须装 `pywin32==302` -> 但你的 Python 版本装不上 `pywin32==302` -> `pip` 崩溃放弃。

---

### 怎么解决？（提供两条路线）

这里有两个非常程序员思维的解法。我个人**强烈推荐路线一**，最干净利落。

#### 路线一：暴力绕过依赖检查（最快，直接在你当前环境解决）
既然 `pywinctl` 非要老版本的 `pywin32`，那我们就骗过它。我们先跳过依赖检查强行把 `pywinctl` 装上，然后再手动给系统装一个最新版的、能适配你当前 Python 版本的 `pywin32`。

在你的 PowerShell `(base)` 环境里，依次执行下面两行命令：

1. **无视依赖，强行安装 `pywinctl` 和另一个需要的库**：
   ```powershell
   pip install pywinctl typing_extensions --no-deps
   ```
2. **手动安装最新版的 `pywin32`**（[官方 PyPI 页面](https://pypi.org/project/pywin32/)）：
   ```powershell
   pip install pywin32
   ```
*执行完这两步，Obsidian 插件需要的环境大概率就彻底打通了。*

####  为 Obsidian 建立专属的旧版本环境（最优雅，隔离污染）
作为日常折腾开发环境的标准操作，既然你已经有了 Conda，最完美的做法是利用 Conda 强大的环境隔离能力，为 Obsidian 单独开一个 Python 3.10 的虚拟环境（这个版本对各种老旧依赖的兼容性最好）。

1. **创建一个名为 `obsidian_env` 的 Python 3.10 环境**：
   ```powershell
   conda create -n obsidian_env python=3.10 -y
   ```
2. **激活这个环境**：
   ```powershell
   conda activate obsidian_env
   ```
3. **在这个环境里正常安装依赖**（因为是 3.10，`pywin32==302` 可以顺利安装）：
   ```powershell
   pip install pywinctl typing_extensions
   ```
4. **获取路径并填入 Obsidian**：
   ```powershell
   where.exe python
   ```
   *把输出的带有 `obsidian_env` 的那个绝对路径复制，填进 Obsidian 的「Python 可执行文件」设置里。*

---

这两种方法都能完美解决你的问题。**你打算先试试第一种最快的“暴力绕过”法，还是顺手建一个干净的 Conda 虚拟环境呢？** 如果执行过程中还有奇怪的报错，随时把报错代码丢给我。



# 环境下载后
太棒了！既然这个名为 `obsidian_env` 的专属环境已经顺利创建完毕（这通常是国内配置开发环境时最折腾的一步），接下来的操作就如同行云流水了。

我们现在要把之前缺失的依赖包在这个干净的环境里装好，并把它和 Obsidian 连接起来。请严格按照以下步骤在你的 PowerShell 中操作：

### 第一步：激活并进入你的专属环境
你需要先告诉系统，接下来的操作都在这个新环境里进行。
```powershell
conda activate obsidian_env
```
*(成功后，你命令行最前面的提示符会从 `(base)` 变成 `(obsidian_env)`。)*

### 第二步：安装 Obsidian 终端所需的依赖
因为我们为你创建的是高兼容性的 Python 3.10 环境，之前那个让你抓狂的 `pywin32==302` 依赖冲突问题将不复存在。直接输入并回车：
```powershell
pip install pywinctl typing_extensions
```
*(等待进度条跑完，出现 `Successfully installed...` 字样即可。)*

### 第三步：获取这个专属 Python 的绝对路径
我们需要把这个配好药的“专属胶囊”的准确地址找出来，交给 Obsidian。
```powershell
where.exe python
```
终端会输出一到两行路径。**请复制带有 `obsidian_env` 字眼的那一行完整路径**（通常长这样：`C:\Users\15056\miniconda3\envs\obsidian_env\python.exe` 或类似的 Anaconda 路径）。

### 第四步：完成 Obsidian 的最终配置
回到 Obsidian 的 Terminal 插件设置页面，做最后两处关键的确认：

1. **修正终端壳层（非常重要）**：
   把你之前填错位置的 **`可执行文件`** 这一栏，改回 Windows 默认的 PowerShell 或 CMD 路径。你可以直接填入：
   `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` 
   或者简单点填 `cmd.exe`。
2. **挂载专属 Python**：
   在底部的 **`Python可执行文件`** 这一栏，粘贴你刚才在第三步复制的那个带有 `obsidian_env` 的绝对路径。

---

**最后一步：** 彻底关闭 Obsidian 并重新打开它。

现在，尝试呼出你的整合终端吧！配置完这套干净的环境后，终端成功弹出来了吗？如果还有任何红色的报错提示，随时发给我。

# ssl证书问题，换源 ,pip 下载问题
哈哈，这可不是什么“钱快乐”，这是典型的网络被“拦截”的情况！遇到这个 `CondaSSLError` （SSL 证书验证错误），简直是国内配置开发环境的必经之路。

问题出在 Conda 默认试图连接国外的官方服务器（`repo.anaconda.com`）。当你后台开着 Nekobox、v2rayN 这类代理工具时，Conda 的下载流量在经过代理端口时，其严格的 SSL 证书安全验证机制就会报错，并强行断开连接。

要扫清这个障碍，顺利把 `obsidian_env` 跑起来，你有两种选择：

###  换用国内清华镜像源（🌟 强烈推荐，一劳永逸）
这是最正规且最长效的做法。特别是在中大的校园网环境下，换用国内镜像源不仅能彻底解决 SSL 报错，后续下载任何 Python 包的速度都会直接起飞，也不用再来回开关代理了。

在 PowerShell 中依次复制并回车运行以下这四行命令：

```powershell
# 1. 清除现有的默认源配置
conda config --remove-key channels

# 2. 添加清华大学的 main 仓库镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

# 3. 添加清华大学的 free 仓库镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# 4. 设置在下载时显示具体的源链接（方便确认是否成功走国内源）
conda config --set show_channel_urls yes
```




# python可执行文件路径问题
![Pasted image 20260410192906](https://raw.githubusercontent.com/submergepsc/imgur/main/assets/Pasted image 20260410192906.png)
这两个报错其实指向的是同一个核心问题：**Obsidian 的插件试图调用 Python，但它“看”不到或者无法执行你填写的那个路径。**

我们来拆解一下这两个弹窗的意思，以及为什么会发生（尤其是咱们刚才已经在终端里验证了那个路径是百分之百存在的）。

### 1. 为什么会报错？

* **黄色弹窗 (`ENOENT` 错误)：**
    `ENOENT` 是编程界非常著名的错误代码，全称是 "Error NO ENTry"，通俗翻译就是**“找不到文件或目录”**。插件试图去 `C:\Users\15056\anaconda3\envs\obsidian_env\python.exe` 这个绝对路径抓取 Python 启动，但是系统反馈“没找到”。
* **粉色弹窗 (`file cannot be empty` 错误)：**
    这是黄色报错引发的**连锁反应**。因为第一次没找到路径（或者路径读取失败变成了空值），插件内部在走下一步程序时，接收到了一个空字符串 `""`，于是系统再次崩溃，抱怨说“你传给我的文件名不能是空的呀”。

### 2. 既然路径是真的，为什么插件说找不到？

这通常是 **Obsidian 插件设置里的输入格式问题**。请进入你这个插件的设置页面（看背景像是配置 Terminal 或某个执行代码的插件），尝试以下几个修复方案：

#### 方案一：检查“隐形杀手”（多余的空格或引号）
你刚才可能是从终端里复制了那个路径粘贴到插件设置里的。
* **动作：** 仔细检查路径的**最前面**和**最后面**，是不是不小心多复制了一个**空格**？或者是不是路径两边加上了**双引号 `"`**？
* **纠正：** 确保输入框里**只有**纯粹的路径，两头干干净净。

#### 方案二：把反斜杠 `\` 换成正斜杠 `/`（最常见修复法）
Obsidian 是基于 Electron（Node.js）开发的，在 Windows 系统下，底层代码有时候对默认的反斜杠 `\` 解析会出 Bug（把它当成了转义符）。
* **动作：** 在插件设置里，把路径里所有的 `\` 手动改成 `/`。
* **改为：** `C:/Users/15056/anaconda3/envs/obsidian_env/python.exe`
* *(或者试试双反斜杠：`C:\\Users\\15056\\anaconda3\\envs\\obsidian_env\\python.exe`)*



# 最终配置
其实就是解决这个python问题
![](assets/Pasted%20image%2020260410193039.png)
![](assets/Pasted%20image%2020260410193042.png)

 