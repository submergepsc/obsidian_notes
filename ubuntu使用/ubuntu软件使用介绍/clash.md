我明白你的意思，咱们之前的对话比较长，信息点也比较碎。我把你最关心的、以及刚才咱们费了半天劲才搞定的核心信息给你做个**“终极汇总”**。

以后如果你重启电脑发现“断网”或者“不通”，直接看这一张表就行：

### 1. 核心运行信息（你的专属配置）
根据咱们刚才的排查，你这台机器的真实情况如下：
* **核心程序**：`mihomo` (Clash Meta)
* **管理工具**：`clashctl`
* **配置文件路径**：`/home/loviya/clashctl/resources/runtime.yaml`
* **Web 控制面板地址**：`http://127.0.0.1:9090/ui`
* **控制面板密码 (Secret)**：需要在终端运行 `cat /home/loviya/clashctl/resources/runtime.yaml | grep secret` 查看。

---

### 2. 代理端口（填在浏览器里的）
不管你用 Firefox 还是 Edge，设置代理时请认准这两个数字：
* **HTTP/HTTPS 代理**：`127.0.0.1` 端口 **`7890`**
* **SOCKS5 代理**：`127.0.0.1` 端口 **`7891`**
* **混合端口 (Mixed)**：`127.0.0.1` 端口 **`7890`** (推荐填这个)

---

### 3. 常用命令清单（建议收藏）
你不需要背，记不住就回来翻一下：

| 功能 | 命令 |
| :--- | :--- |
| **开启代理环境** | `clashon` |
| **关闭代理环境** | `clashoff` |
| **查看订阅列表** | `clashsub ls` |
| **更新/切换订阅** | `clashsub use [编号]` |
| **查看面板信息** | `clashui` |
| **验证是否连通** | `curl -I https://www.google.com` |
| **查看核心进程** | `ps -ef \| grep clash` |

---

### 4. 为什么重启后会“坏掉”？
这是因为重启后，**系统环境变量**和**TUN 模式的网卡路由**都会重置。
* **解决流程**：
    1. 终端执行 `clashon`。
    2. 如果用了 TUN 模式感觉断网，执行 `clashtun off`。
    3. 检查控制面板，点一下 **⚡ 测速**，确保节点是**绿色数字**。
    4. 确保 **Firefox/Edge** 的手动代理设置（7890）没有被系统重置。



### 5. 仓库地址汇总
* **clashctl 工具**：`https://github.com/zsh-run/clashctl`
* **Mihomo 核心**：`https://github.com/MetaCubeX/mihomo`
* **控制面板**：`https://github.com/MetaCubeX/metacubexd`


### ***老子用的是这个*** ->
`https://github.com/nelvko/clash-for-linux-install`
**Gemini 的碎碎念：**
你现在已经跨过了 Linux 最难的“网络关”。刚才那个 `HTTP/1.1 200 OK` 出现的时候，其实你已经成功了。剩下的只是如何让浏览器更听话的问题。

现在你的 Edge 浏览器能顺利打开谷歌了吗？如果还是不行，告诉我它的报错提示，咱们把这最后一步钉死。


---

# 其他几个clashforlinux仓库
你提到的“linux杨”大概率是输入法把“Linux上”、“Linux版”或者是某位作者的名字（比如 **wanhebin** 或 **wnlen**）给打滑了吧？😂

如果你在找之前在 Linux 环境下用过的那个著名的终端版 Clash 仓库，目前圈子里最经典和最活跃的主要是以下几个。在 Ubuntu 终端里折腾各种系统级配置和开发环境时，这些纯 CLI 的代理管理脚本确实比图形界面更契合键鼠党的需求：

### 1\. 活跃重构版：wnlen / clash-for-linux (极客首选)

这可能是你最近印象比较深的一个，它是对经典版本的高阶重构，目前更新非常勤快，完美适配了最新的 Mihomo (Clash Meta) 内核。

  * **GitHub 仓库**: [wnlen/clash-for-linux](https://github.com/wnlen/clash-for-linux)
  * **核心特色**: 提供了一套非常优雅的 `clashctl` 命令行管理工具。你可以直接在终端敲 `clashon` 和 `clashoff` 来无缝开关代理，或者用 `clashctl select` 在命令行调出面板切换节点，操作行云流水。

### 2\. 一键部署增强版：nelvko / clash-for-linux-install

另一个目前维护得极好、也是大家在 Linux 服务器或本地开发机上常用的版本。

  * **GitHub 仓库**: [nelvko/clash-for-linux-install](https://github.com/nelvko/clash-for-linux-install)
  * **核心特色**: 极简的一键自动安装，会自动识别系统架构并下载对应内核，同时会自动把代理配置注册为 systemd 系统服务，支持开机自启，非常省心。

### 3\. 经典原版：wanhebin / clash-for-linux

这是最早在圈子里极其普及的一个纯 Shell 脚本版本，很多后来的开源项目都是受它启发或直接 Fork 它的。

  * **GitHub 仓库**: [wanhebin/clash-for-linux](https://www.google.com/search?q=https://github.com/wanhebin/clash-for-linux) （注：如果原版由于某些原因隐藏，GitHub 上有大量同名的完整镜像，例如 `LopSdir/clash-for-linux`）
  * **核心特色**: 非常硬核的纯脚本实现，完全依靠手动编辑 `.env` 文件和执行 `start.sh` 运行，没有任何多余的依赖。

**小建议**：
如果你追求快捷指令和精简的本地化管理，**第一款 (wnlen/clash-for-linux)** 的快捷命令以及对终端代理变量环境（`http_proxy`）的自动接管，绝对是最契合高效工作流的选择。



 