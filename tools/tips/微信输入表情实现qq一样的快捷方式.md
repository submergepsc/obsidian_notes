为了让微信实现qq这样快捷输入表情的方式，使用的是`AutoHotKey`脚本。
1. 官网下载应用[https://www.autohotkey.com](https://www.autohotkey.com/)（注意下载v2）
2. 运行软件，新建一个`.ahk`文件，使用notepad打开
3. 复制如下脚本并运行.ahk文件。
```shell
; === 微信快捷表情配置 ===
; 语法说明：:*:/缩写::[替换的文字]
; :*: 的意思是“不需要按空格或回车，输入完缩写立刻自动替换”

:*:/wl::[捂脸]
:*:/wc::[旺柴]
:*:/jz::[机智]
:*:/lk::[裂开]
:*:/cg::[吃瓜]
:*:/zm::[皱眉]
:*:/gz::[鼓掌]
:*:/xh::[笑脸]
:*:/xy::[呲牙]
:*:/hx::[害羞]

; 你可以按照上面的格式，无限添加你想要的表情
```

![Pasted image 20260411011304 | 200](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260411011304.png)

![Pasted image 20260411011229 | 200](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260411011229.png)

4. 效果：
![PixPin 2026 04 11 01 18 45 | 400](https://raw.githubusercontent.com/submergepsc/imgur/main/PixPin_2026-04-11_01-18-45.gif)


5. 改进：设置成仅在微信触发，/nwc这样的格式触发多次和更多种表情的快捷方式。
6. 还实现了随机表情的功能。
```shell
#Requires AutoHotkey v2.0
Persistent()  ; 强制后台运行

; 1. 🌟 你的表情库 (Map 字典，用来精准匹配)
global emojis := Map(
    "wx", "[微笑]", "pz", "[撇嘴]", "se", "[色]", "fd", "[发呆]", "dy", "[得意]", 
    "ll", "[流泪]", "hx", "[害羞]", "bz", "[闭嘴]", "shui", "[睡]", "dk", "[大哭]", 
    "wl", "[捂脸]", "wc", "[旺柴]", "jz", "[机智]", "lk", "[裂开]", "cg", "[吃瓜]", 
    "zm", "[皱眉]", "ye", "[耶]", "dl", "[打脸]", "wa", "[哇]", "jia", "[加油]"
)

; 1.5 🎲 提取所有表情，生成一个“盲盒抽卡池” (Array 数组，用来随机抽取)
global emojiArray := []
for abbr, emoji in emojis {
    emojiArray.Push(emoji)
}

; 2. 限制快捷键只在“微信组”生效（包含各种马甲，防漏杀）
GroupAdd("WeChatGroup", "ahk_exe WeChat.exe")
GroupAdd("WeChatGroup", "ahk_exe Weixin.exe")
GroupAdd("WeChatGroup", "ahk_class WeChatMainWndForPC")
GroupAdd("WeChatGroup", "ahk_class ChatWnd")
HotIfWinActive("ahk_group WeChatGroup")

; 3. 引擎启动：瞬间生成精准表情组合
for abbr, emoji in emojis {
    Hotstring(":?*:/" abbr, SendDynamicEmoji)
    Loop 100 {
        Hotstring(":?*:/" A_Index abbr, SendDynamicEmoji)
    }
}

; 🌟 3.5 盲盒特权通道：单独为 rn (random) 注册快捷键
Hotstring(":?*:/rn", SendDynamicEmoji)
Loop 100 {
    Hotstring(":?*:/" A_Index "rn", SendDynamicEmoji)
}

HotIfWinActive() ; 结束微信窗口限制


; ==========================================
; 👇 v2 触发处理器 (升级版：支持盲盒)
; ==========================================
SendDynamicEmoji(ThisHotkey) {
    trigger := StrReplace(ThisHotkey, ":?*:/", "")
    RegExMatch(trigger, "^(\d*)([a-zA-Z]+)$", &match)
    
    count := match[1] == "" ? 1 : Integer(match[1])
    abbr := match[2]
    outStr := ""
    
    ; 🌟 核心逻辑分流
    if (abbr == "rn") {
        ; 如果敲的是 rn，进入随机盲盒模式！
        Loop count {
            ; 每次循环都从抽卡池里随机挑一个
            randomIndex := Random(1, emojiArray.Length)
            outStr .= emojiArray[randomIndex]
        }
    } else {
        ; 如果敲的是普通的缩写，进入精准输出模式
        emoji := emojis[abbr]
        Loop count {
            outStr .= emoji
        }
    }
    
    ; 瞬间输出
    SendText(outStr)
}
```
![PixPin 2026 04 11 02 13 28|300](https://raw.githubusercontent.com/submergepsc/imgur/main/PixPin_2026-04-11_02-13-28.gif)
![PixPin 2026 04 12 13 02 21|300](https://raw.githubusercontent.com/submergepsc/imgur/main/assets/PixPin_2026-04-12_13-02-21.gif)

7. 为了避免每次开机都要专门运行这个脚本，实现开机自启：
	1. 写入注册表
			首先`ctrl+shift+c`复制文件地址，然后`win+R`输入`regedit`回车，在导航栏输入`计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`回车，然后右键空白->新建->字符串值，输入名称和路径。
	2. 或者右键脚本新建快捷方式并复制，然后`win+R`输入`shell:startup`,把快捷方式粘贴进去。
现在每次开机后就能自动启动该脚本了。

