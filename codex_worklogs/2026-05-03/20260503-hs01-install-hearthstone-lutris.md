---
id: 20260503-hs01-install-hearthstone-lutris
name: install-hearthstone-lutris
slug: install-hearthstone-lutris
cwd: /home/loviya
summary: CN Hearthstone is installed; Battle.net launch reaches game but matchmaking crashes in libacsdk_x86, and a direct EXE diagnostic launcher was added.
tags:
  - lutris
  - hearthstone
  - battle.net
priority: normal
---

# Install Hearthstone With Lutris

## Current Snapshot

- status: 进行中
- goal: 在 Ubuntu 上通过 Wine/Lutris 路径安装并运行炉石传说。
- blocker: 国服 Battle.net 启动链路能进入游戏，但匹配阶段被 `libacsdk_x86.dll` 阻塞；直接打开 `Hearthstone.exe` 可用于诊断，但通常无法携带 Battle.net 登录 token。
- next: 运行 `/home/loviya/bin/hearthstone-cn-direct-exe` 验证直启行为；如出现战网登录/token 错误，回到 Battle.net 启动链路或改用 Windows/双系统方案。
- updated: 2026-05-04 05:03:32 +0800

## Key Results

- Lutris 已安装：`/usr/games/lutris`。
- 系统包已具备 Wine 相关基础组件：`lutris 0.5.14-2`、`wine 9.0~repack-4build3`、`wine32`、`wine64`、`winetricks 20240105-2`、`gamemode 1.8.1-2build1`。
- Lutris 官网当前炉石脚本中，`hearthstone-standard` 会创建 64-bit Wine prefix 并安装 Battle.net；`hearthstone-battlenet-launcher` 依赖已有 `battlenet-standard`，主要用于增加炉石启动入口。
- Lutris 脚本下载的旧 `Battle.net-Setup-enUS.exe` 会在 `http://us.patch.battle.net:1119/patch` 处返回 404，并报 `BLZBNTBTS00000029`。
- 暴雪官方下载页当前重定向到 `https://downloader.battle.net/download/installer/win/1.0.63/Battle.net-Setup.exe`；已保存为 `/home/loviya/Games/hearthstone-installers/Battle.net-Setup-current.exe`。
- 旧的半成品 prefix 已备份为 `/home/loviya/Games/hearthstone.failed-20260504-0114`。
- 新的 `/home/loviya/Games/hearthstone` prefix 中已存在 `/home/loviya/Games/hearthstone/drive_c/Program Files (x86)/Battle.net/Battle.net.exe`。
- 桌面窗口列表已出现 `Battle.net Login`，说明 Battle.net 客户端已启动到登录界面。
- 国服下载页 `https://download.battlenet.com.cn/zh-cn/` 的安装器重定向到 `https://downloader.battlenet.com.cn/download/installer/win/1.0.63/Battle.net-Setup-CN.exe`；已保存为 `/home/loviya/Games/hearthstone-cn-installers/Battle.net-CN-Setup.exe`。
- 国服安装器在 `http://cn.patch.battle.net:1119` 获取版本文件时失败，报 `BLZBNTBTS00000028`；已将失败 prefix 备份为 `/home/loviya/Games/hearthstone-cn.failed-20260504-0331`。
- 可用方案是复制已成功安装的 Battle.net 客户端到 `/home/loviya/Games/hearthstone-cn`，将配置改为 `zhCN`、`CN`、`cn.actual.battlenet.com.cn`、`account.battlenet.com.cn` 后启动。
- 当前国服 Battle.net 主进程参数包含 `--setlanguage=zhCN --setregion=CN --proxy-server=http://127.0.0.1:7897`，窗口标题为 `战网`。
- 国服炉石日志 `/home/loviya/Games/hearthstone-cn/drive_c/Program Files (x86)/Hearthstone/Logs/Hearthstone_2026_05_04_03_59_45/Hearthstone.log` 显示已登录 `Region: CN`，并进入 `ConnectingToHearthstone`、`LaunchGame`、`BNET_QUEUE_UPDATED`。
- 崩溃栈中的 `/home/loviya/Games/hearthstone-cn/drive_c/Program Files (x86)/Hearthstone/Hearthstone_Data/Plugins/x86/libacsdk_x86.dll` 是 32-bit Windows DLL，导出 `AntiCheatSDK_antiCheatCheck*` 等接口，且字符串包含 `VMProtect`、`IsDebuggerPresent`。
- 已新增国服启动脚本 `/home/loviya/bin/hearthstone-cn-battlenet` 和桌面入口 `/home/loviya/.local/share/applications/hearthstone-cn-battlenet.desktop`；脚本固定使用 `/home/loviya/Games/hearthstone-cn`、`wine-11.6-staging-tkg-amd64`、`WINEESYNC=0`、`WINEFSYNC=0`、`zhCN`、`CN` 和本地代理参数。
- 匹配阶段最新日志 `/home/loviya/Games/hearthstone-cn/drive_c/users/loviya/AppData/LocalLow/Blizzard Entertainment/Hearthstone/Player.log` 显示：`Region: CN` -> `GameMgr.ChangeFindGameState() - state: BNET_QUEUE_DELAYED` -> `Crash!!!`。
- DXVK 2.6.2 已通过 symlink 存在于 `/home/loviya/Games/hearthstone-cn/drive_c/windows/system32` 与 `syswow64`；脚本已增加 `WINEDLLOVERRIDES=d3d11,dxgi=n,b`。
- Vulkan 图形会话检测可见 Intel iGPU 与 `NVIDIA GeForce RTX 4060 Laptop GPU`；脚本已设置 `VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json`、`DXVK_FILTER_DEVICE_NAME=NVIDIA GeForce RTX 4060 Laptop GPU`、`__NV_PRIME_RENDER_OFFLOAD=1`。
- 2026-05-04 04:29 已回退 `/home/loviya/bin/hearthstone-cn-battlenet` 中的 DXVK/NVIDIA 强制项；当前脚本仅保留国服、中文、代理和 `WINEESYNC=0 WINEFSYNC=0`，战网窗口已恢复为 `战网`。
- 2026-05-04 04:34 已将 `/home/loviya/Games/hearthstone-cn/drive_c/users/loviya/AppData/Local/Blizzard/Hearthstone/Cache` 备份为 `Cache.backup-20260504-043203`，并将 `options.txt` 备份为 `options.txt.backup-20260504-043203`；下次启动炉石会重建干净缓存和选项。
- 2026-05-04 04:35 清理缓存后仍复现 Wine page fault，回溯全部落在 `libacsdk_x86 (+0x319a39)` 等 AntiCheatSDK 内部地址；本地缓存、战网登录、国服切区和普通网络链路已基本排除。
- 2026-05-04 04:45 已关闭国服 Battle.net，创建国际服启动脚本 `/home/loviya/bin/hearthstone-global-battlenet` 和桌面入口 `/home/loviya/.local/share/applications/hearthstone-global-battlenet.desktop`，并启动 `/home/loviya/Games/hearthstone` prefix 中的 Battle.net，参数为 `--setlanguage=enUS --setregion=US`。
- 2026-05-04 04:48 确认国际服 prefix `/home/loviya/Games/hearthstone` 目前只有 Battle.net，尚未安装 `Hearthstone.exe`；已把 `Battle.net Login` 窗口切到前台等待用户登录。
- 2026-05-04 04:56 用户反馈前台没有出来；确认 `Battle.net Login` 窗口 ID `0x0e20000d` 状态为 `IsViewable`，坐标 `+80+120`、大小 `362x677`，已置顶并将鼠标移入窗口区域。
- 2026-05-04 05:03 切回国服已安装 exe 直启问题；确认 `/home/loviya/Games/hearthstone-cn/drive_c/Program Files (x86)/Hearthstone/Hearthstone.exe` 存在，并新增诊断入口 `/home/loviya/bin/hearthstone-cn-direct-exe`。

## Decisions

- 本机未找到已有 Hearthstone/Battle.net Lutris 安装目录，优先启动 `hearthstone-standard`。
- 不直接使用 `hearthstone-battlenet-launcher`，因为它要求先安装 Battle.net Standard。
- `wine-ge-8-26-x86_64` 直接运行新版 Battle.net 安装器时触发 `wineserver` 断言失败；改用本机已有 `wine-11.6-staging-tkg-amd64` 在干净 prefix 中完成 Battle.net 安装。
- 国服不要继续使用国际服 `/home/loviya/Games/hearthstone`；国服运行路径固定为 `/home/loviya/Games/hearthstone-cn`，避免 US/CN 登录配置互相污染。
- 不替换、不删除、不绕过 `libacsdk_x86.dll`；只测试 Wine runner、启动环境和图形/网络参数。若该反作弊/安全 SDK 在 Wine 下持续崩溃，后续应转向 Windows/双系统/支持 GPU 的虚拟化等官方客户端环境。
- 直接运行 `Hearthstone.exe` 只作为诊断路径；炉石这类 Battle.net 游戏通常需要 Battle.net 发起启动并传递登录 token，直启 exe 不应被当成稳定替代入口。

## Commands

- `command -v lutris`
- `lutris --version`
- `dpkg-query -W -f='${Package} ${Version} ${Status}\n' lutris wine winetricks wine64 wine32 gamemode mangohud`
- `find /home/loviya -maxdepth 3 -iname '*Hearthstone*' -o -iname '*Battle.net*' -o -iname '*battle*net*'`
- `wget -O /home/loviya/Games/hearthstone-installers/Battle.net-Setup-current.exe 'https://downloader.battle.net//download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live'`
- `mv /home/loviya/Games/hearthstone /home/loviya/Games/hearthstone.failed-20260504-0114`
- `env DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus XAUTHORITY=/run/user/1000/gdm/Xauthority XDG_RUNTIME_DIR=/run/user/1000 WINEPREFIX=/home/loviya/Games/hearthstone WINEARCH=win64 /home/loviya/.local/share/lutris/runners/wine/wine-11.6-staging-tkg-amd64/bin/wine /home/loviya/Games/hearthstone-installers/Battle.net-Setup-current.exe --lang=enUS '--installpath=C:\\Program Files (x86)\\Battle.net'`
- `wget -O /home/loviya/Games/hearthstone-cn-installers/Battle.net-CN-Setup.exe 'https://downloader.battlenet.com.cn/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live'`
- `cp -a /home/loviya/Games/hearthstone /home/loviya/Games/hearthstone-cn`
- `setsid -f env DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus XAUTHORITY=/run/user/1000/gdm/Xauthority XDG_RUNTIME_DIR=/run/user/1000 WINEPREFIX=/home/loviya/Games/hearthstone-cn WINEARCH=win64 http_proxy=http://127.0.0.1:7897/ https_proxy=http://127.0.0.1:7897/ HTTP_PROXY=http://127.0.0.1:7897/ HTTPS_PROXY=http://127.0.0.1:7897/ no_proxy=localhost,127.0.0.1 NO_PROXY=localhost,127.0.0.1 /home/loviya/.local/share/lutris/runners/wine/wine-11.6-staging-tkg-amd64/bin/wine '/home/loviya/Games/hearthstone-cn/drive_c/Program Files (x86)/Battle.net/Battle.net.exe' --setlanguage=zhCN --setregion=CN --proxy-server=http://127.0.0.1:7897 --proxy-bypass-list='<-loopback>'`
- `/home/loviya/bin/hearthstone-cn-battlenet`

## Launch Lutris Hearthstone Installer

- updated: 2026-05-03 12:27:00 +0800
- cwd: `/home/loviya`
- source instruction: `帮我使用lutris安装一下炉石传说`
- problem:
  - 普通命令环境调用 `lutris --version` 会尝试初始化 GTK，因无法访问图形显示而报错。
  - 炉石的 Lutris 安装过程需要下载 Battle.net 安装器，并打开 Windows 安装/登录窗口。
- improvement:
  - 确认依赖已安装，并根据 Lutris 当前脚本选择 `lutris:install/hearthstone-standard`。
- result:
  - 准备通过系统 URL handler 启动 Lutris GUI 安装器。
- next:
  - 启动安装器后，在图形窗口中完成 Battle.net 安装、登录，并在 Battle.net 内安装 Hearthstone。

## Replace Failing Lutris Battle.net Installer

- updated: 2026-05-04 01:21:23 +0800
- cwd: `/home/loviya`
- source instruction: `继续帮我处理在我的ubuntu中玩炉石传说的问题`
- problem:
  - Lutris `hearthstone-standard` 创建了 Wine prefix，但旧缓存安装器没有生成 `Battle.net.exe`。
  - 安装器日志显示旧版本请求 `http://us.patch.battle.net:1119/patch` 返回 404，错误码为 `BLZBNTBTS00000029`。
  - 在旧 prefix 中运行新版安装器时，残留 Battle.net Agent 连续返回 `Agent init returned status code=401`。
- improvement:
  - 从暴雪官方下载重定向下载新版 `Battle.net-Setup.exe`。
  - 将旧 prefix 备份到 `/home/loviya/Games/hearthstone.failed-20260504-0114`，用 `wine-11.6-staging-tkg-amd64` 创建干净 prefix 并安装 Battle.net。
- result:
  - `/home/loviya/Games/hearthstone/drive_c/Program Files (x86)/Battle.net/Battle.net.exe` 已生成。
  - 桌面窗口列表出现 `Battle.net Login`，Battle.net 已启动到登录界面。
- next:
  - 用户登录 Battle.net 后安装 Hearthstone；安装完成后验证 Lutris game id 启动入口和桌面快捷方式。

## Switch To China Hearthstone Region

- updated: 2026-05-04 03:42:51 +0800
- cwd: `/home/loviya`
- source instruction: `我想要使用中国版区的炉石传说`
- problem:
  - 用户需要国服炉石，而不是国际服 Battle.net。
  - 国服安装器 `Battle.net-Setup-CN.exe` 能启动，但访问 `http://cn.patch.battle.net:1119` 版本文件失败并报 `BLZBNTBTS00000028`。
- improvement:
  - 下载并保存国服官方安装器到 `/home/loviya/Games/hearthstone-cn-installers/Battle.net-CN-Setup.exe`。
  - 将失败的国服安装 prefix 备份到 `/home/loviya/Games/hearthstone-cn.failed-20260504-0331`。
  - 复制已安装好的 Battle.net 客户端为 `/home/loviya/Games/hearthstone-cn`，并把配置切到 `zhCN`、`CN`、`cn.actual.battlenet.com.cn`、`account.battlenet.com.cn`。
- result:
  - 国服专用 Battle.net 已启动；进程参数包含 `--setlanguage=zhCN --setregion=CN`。
  - 桌面窗口标题为 `战网`，已经切到前台。
- next:
  - 用户在 `战网` 窗口登录国服账号，安装炉石传说；安装完成后再创建/验证国服启动入口。

## CN Hearthstone AntiCheatSDK Wine Crash

- updated: 2026-05-04 04:12:57 +0800
- cwd: `/home/loviya`
- source instruction: `Unhandled exception: page fault ... in libacsdk_x86 ... 运行过程中出错了`
- problem:
  - 用户从国服战网启动炉石后遇到 Wine `wow64 32-bit code` page fault，回溯落在 `libacsdk_x86.dll`。
  - 炉石自己的日志显示这次并非没有进入国服：`Region: CN` 已出现，随后进入 `LaunchGame` 和 `BNET_QUEUE_UPDATED`。
- improvement:
  - 定位到 `Hearthstone_Data/Plugins/x86/libacsdk_x86.dll`，确认其导出 `AntiCheatSDK_*` 并带 VMProtect/调试检测字符串。
  - 直接运行 `Hearthstone.exe -launch -uid hs_beta` 加 `WINEESYNC=0 WINEFSYNC=0` 未复现 `libacsdk` 崩溃，但因为不是战网发起，游戏拿不到登录 token 并报“无法通过暴雪战网服务进行登录”。
  - 新增 `/home/loviya/bin/hearthstone-cn-battlenet` 和 `/home/loviya/.local/share/applications/hearthstone-cn-battlenet.desktop`，让战网及其子进程继承 `WINEESYNC=0 WINEFSYNC=0`、国服区服、中文和代理参数。
  - 已关闭旧参数启动的战网，并用新脚本启动新 `战网` 窗口到前台。
- result:
  - 当前可重复入口是 `/home/loviya/bin/hearthstone-cn-battlenet`。
  - 新战网进程参数包含 `--setlanguage=zhCN --setregion=CN --proxy-server=http://127.0.0.1:7897`。
- next:
  - 用户在当前前台 `战网` 窗口内点炉石“开始游戏”复测；若同样崩在 `libacsdk_x86.dll`，记录为国服安全/反作弊 SDK 与 Wine 不兼容的阻塞。

## Matchmaking Crash After Entering CN Game

- updated: 2026-05-04 04:20:20 +0800
- cwd: `/home/loviya`
- source instruction: `可以打开炉石传说,可以进入游戏,但是进入开始匹配到一般就弹出错误`
- problem:
  - 国服炉石已经能进入游戏，但匹配进行到一半弹错并退出。
  - 最新 `Player.log` 在 `GameMgr.ChangeFindGameState() - state: BNET_QUEUE_DELAYED` 后记录 `Crash!!!`。
- improvement:
  - 确认这次不是普通战网登录失败：日志仍显示 `Region: CN`，并且游戏已经进入匹配队列状态。
  - 确认前缀已有 DXVK 2.6.2 的 `d3d11.dll`/`dxgi.dll` symlink，但原启动脚本没有显式 DLL override。
  - 更新 `/home/loviya/bin/hearthstone-cn-battlenet`，加入 `WINEDLLOVERRIDES=d3d11,dxgi=n,b`、DXVK 日志、NVIDIA Vulkan ICD、DXVK 设备过滤和 PRIME offload 环境变量。
  - 关闭旧战网，使用更新后的脚本重新启动，并确认进程环境已继承这些变量。
- result:
  - 当前前台 `战网` 窗口来自更新后的 DXVK/NVIDIA 启动环境。
- next:
  - 用户从当前战网窗口启动炉石并再次匹配；若仍崩溃，读取新的 `Hearthstone_...` 目录、`Player.log` 和 DXVK 日志判断是否已排除 WineD3D/显卡路径。

## Roll Back Global DXVK Battle.net Launch

- updated: 2026-05-04 04:29:14 +0800
- cwd: `/home/loviya`
- source instruction: `战网现在都启动不了了`
- problem:
  - 将 DXVK/NVIDIA 强制项加到 `/home/loviya/bin/hearthstone-cn-battlenet` 后，Battle.net 自身启动/显示异常。
  - 用户还从 Lutris 启动过另一套英文 Battle.net，导致同时存在国服脚本和 Lutris `wine-ge` 两套 Battle.net 进程。
- improvement:
  - 从国服脚本中移除 `WINEDLLOVERRIDES=d3d11,dxgi=n,b`、`DXVK_*`、`VK_ICD_FILENAMES`、`__NV_PRIME_RENDER_OFFLOAD`、`__GLX_VENDOR_LIBRARY_NAME`。
  - 关闭所有 Battle.net/Agent/Lutris Hearthstone 残留进程，只用国服脚本重新启动。
- result:
  - 当前只剩国服 Battle.net 进程，参数包含 `--setlanguage=zhCN --setregion=CN`，窗口标题恢复为 `战网`。
  - 进程环境确认仅保留 `WINEPREFIX=/home/loviya/Games/hearthstone-cn`、`WINEESYNC=0`、`WINEFSYNC=0`，没有 DXVK/NVIDIA 强制变量。
- next:
  - 不再把显卡/DXVK 试验参数放进 Battle.net 全局入口；如需继续测试匹配崩溃，应设计只影响 `Hearthstone.exe` 的启动方式或改用另一份临时脚本。

## Reset Hearthstone Local Cache Before Retest

- updated: 2026-05-04 04:34:00 +0800
- cwd: `/home/loviya`
- source instruction: `还是游戏打开后准备玩,匹配到一般就停止了`
- problem:
  - 匹配崩溃再次复现：日志路径 `Hearthstone_2026_05_04_04_28_37`，状态从 `BNET_QUEUE_DELAYED` 到 `BNET_QUEUE_UPDATED` 后 `Crash!!!`。
  - `Player.log` 反复记录 `UberText LoadCachedData() failed` 和 `Failed to load config file`，说明本地缓存/选项也有异常信号。
- improvement:
  - 没有动游戏安装文件、账号数据或 Battle.net 配置。
  - 将本地炉石缓存目录改名为 `Cache.backup-20260504-043203`。
  - 将本地 `options.txt` 改名为 `options.txt.backup-20260504-043203`。
- result:
  - 当前只保留国服 `战网` 窗口，炉石下次启动会重新生成干净缓存和选项。
- next:
  - 用户从战网重新启动炉石并匹配；若仍崩溃，继续读取新 `Player.log`，判断是否已经排除本地缓存/配置原因。

## CN Matchmaking Blocked By libacsdk_x86

- updated: 2026-05-04 04:35:53 +0800
- cwd: `/home/loviya`
- source instruction: `Unhandled exception: page fault ... in libacsdk_x86 ...`
- problem:
  - 清理本地缓存和选项后，国服炉石仍在匹配/对战入口阶段崩溃。
  - 用户提供的 Wine 回溯显示 page fault 发生在 `libacsdk_x86 (+0x319a39)`，后续多层调用仍在 `libacsdk_x86` 内部。
- improvement:
  - 确认当前系统只剩国服 `Battle.net.exe --setlanguage=zhCN --setregion=CN`，没有 `Hearthstone.exe` 或 `winedbg` 残留。
  - 保留稳定的国服 Battle.net 启动脚本，不再把 DXVK/NVIDIA 试验参数放进 Battle.net 全局入口。
- result:
  - 国服战网和国服炉石启动链路可用，但 Wine 下无法稳定进入可玩的匹配/对战阶段。
  - 主要阻塞是国服 `libacsdk_x86.dll` AntiCheatSDK/安全组件与 Wine wow64 32-bit 路径不兼容。
- next:
  - 不绕过、不替换安全组件；如需稳定玩国服，应改用 Windows、双系统或 Windows 虚拟化/GPU 直通方案。

## Switch Back To Global Hearthstone

- updated: 2026-05-04 04:45:11 +0800
- cwd: `/home/loviya`
- source instruction: `国际副呢` / `对`
- problem:
  - 国服 Wine 路径已确认被 `libacsdk_x86.dll` 匹配阶段崩溃阻塞。
  - 用户希望改测国际服。
- improvement:
  - 保留国服 prefix `/home/loviya/Games/hearthstone-cn`，不再改动。
  - 关闭国服 Battle.net/Agent，避免和国际服争用 Agent/窗口。
  - 创建 `/home/loviya/bin/hearthstone-global-battlenet`，固定使用 `/home/loviya/Games/hearthstone`、`wine-11.6-staging-tkg-amd64`、`enUS`、`US`。
  - 创建桌面入口 `/home/loviya/.local/share/applications/hearthstone-global-battlenet.desktop`。
- result:
  - 国际服 Battle.net 已启动，进程参数为 `--setlanguage=enUS --setregion=US`，窗口标题为 `Battle.net Login`。
  - 当前国际服 prefix 暂未发现 `Hearthstone.exe`，需要在 Battle.net 内安装 Hearthstone。
  - `Battle.net Login` 窗口已切到前台。
  - 用户反馈窗口没有明显弹出；后续定位到窗口在主屏左上区域，已置顶。
- next:
  - 用户在前台登录国际服账号，安装 Hearthstone，然后测试启动和匹配。

## Direct CN Hearthstone EXE Diagnostic Launcher

- updated: 2026-05-04 05:03:32 +0800
- cwd: `/home/loviya`
- source instruction: `转换一下工作流,目前我已经安装了国服的炉石传说,能不能用相关软件直接打开这个exe文件`
- problem:
  - 用户希望从“国际服 Battle.net 登录”切回“国服已安装炉石能否直接打开 exe”。
  - 国服 `Hearthstone.exe` 已存在，但直接运行可能缺少 Battle.net 传入的登录 token。
- improvement:
  - 新增 `/home/loviya/bin/hearthstone-cn-direct-exe`，使用国服 Wine prefix、`wine-11.6-staging-tkg-amd64`、本地代理和 `WINEESYNC=0 WINEFSYNC=0` 直接运行 `Hearthstone.exe -launch -uid hs_beta`。
  - 新增桌面入口 `/home/loviya/.local/share/applications/hearthstone-cn-direct-exe.desktop`。
- result:
  - 可以用该入口验证 exe 能否被 Wine 直接打开。
  - 预计如果游戏需要账号会话，直启仍会报 Battle.net 登录/token 相关错误，不能替代 Battle.net 正常启动链路。
- next:
  - 运行 `/home/loviya/bin/hearthstone-cn-direct-exe` 做直启测试；如仍不能联网进入游戏，结论是必须由 Battle.net 启动，国服 Wine 阻塞仍在安全组件/匹配阶段。
