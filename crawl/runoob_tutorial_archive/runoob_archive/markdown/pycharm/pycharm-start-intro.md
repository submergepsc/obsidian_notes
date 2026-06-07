# PyCharm 界面说明

- Source: https://www.runoob.com/pycharm/pycharm-start-intro.html

PyCharm 的默认界面主要分为以下几个区域：


![](https://www.runoob.com/wp-content/uploads/2025/04/d805426b-8ebc-4c77-a927-378eb068740a.png)


- **顶部菜单栏**：文件(File)、编辑(Edit)、视图(View)、导航(Navigate)等
- **工具栏**：常用操作快捷按钮
- **导航栏**：显示当前文件路径的简化导航
- **侧边工具窗口**：左右两侧的各种功能面板
- **编辑器区域**：中央的代码编辑区
- **状态栏**：底部显示项目状态信息


## 二、主要功能区域详解


### 1. 顶部菜单栏（中文对照）


- **文件(File)**：项目/文件操作（新建、打开、设置等）
- **编辑(Edit)**：代码编辑操作（复制、查找、代码生成等）
- **视图(View)**：界面显示控制（工具窗口、外观等）
- **导航(Navigate)**：代码跳转相关功能
- **代码(Code)**：代码重构和生成
- **重构(Refactor)**：代码重构功能
- **运行(Run)**：执行和调试
- **工具(Tools)**：集成工具（数据库、终端等）
- **版本控制(VCS)**：Git等版本控制
- **窗口(Window)**：窗口布局管理
- **帮助(Help)**：文档和支持


### 2. 工具栏图标（常用功能）


![](https://www.runoob.com/wp-content/uploads/2025/04/aba7fcca-2356-4c42-99bf-d8ee93e2038e.png)


- 运行按钮 ：运行当前项目/脚本
- 调试按钮 ：调试模式启动
- 提交按钮 ：版本控制提交
- 更新项目 ：从VCS更新
- 历史记录 ：查看本地历史
- 设置 ：可以打开设置窗口


### 3. 左侧工具窗口


![](https://www.runoob.com/wp-content/uploads/2025/04/0953d5c1-38b9-41fb-a24d-5364c9516a16.png)


**项目(Project)面板**：


- 显示项目目录结构
- 右键菜单提供文件操作
- 支持文件筛选和排序


**结构(Structure)面板**：


- 显示当前文件的代码结构（类、方法等）
- 可快速跳转到指定元素


**Python控制台(Python Console)**：


- 交互式Python执行环境
- 支持变量查看和代码片段执行


**终端(Terminal)**：


- 系统命令行终端
- 支持PowerShell/CMD/bash等


### 4. 右侧工具窗口


![](https://www.runoob.com/wp-content/uploads/2025/04/2b9f5538-89d9-4b19-bd5e-6a88b16235d5.png)


**AI 聊天**：


- AI 聊天窗口


**数据库(Database)**：


- 数据库连接管理
- SQL 查询执行和结果查看


### 5. 底部工具窗口


![](https://www.runoob.com/wp-content/uploads/2025/04/f16994e4-c055-4b2b-a7d7-921c9a228399-1.png)


**运行(Run)**：


- 程序输出显示
- 调试控制台


**问题(Problems)**：


- 代码错误和警告汇总
- 点击可跳转到问题代码


**TODO**：


- 收集代码中的TODO注释
- 按模块分组显示


**版本控制(Version Control)**：


- Git等版本控制操作
- 变更文件列表


### 6. 编辑器区域


![](https://www.runoob.com/wp-content/uploads/2025/04/9bc673b6-5a0b-4c81-8964-49346738a661.png)


- **标签页**：显示打开的文件，支持分组
- **代码编辑区**：主工作区域，支持： 语法高亮
- 代码折叠
- 行号显示
- 错误波浪线提示




**右侧滚动条**：显示代码分析标记（错误/警告等）




**装订区域**：显示断点、书签等




### 7. 状态栏


![](https://www.runoob.com/wp-content/uploads/2025/04/c460c92b-b0f7-4173-9c63-ef467425a35e.png)


- 解释器显示：当前使用的Python解释器
- 编码格式：文件编码（如UTF-8）
- 行尾符：LF/CRLF
- 光标位置：行:列指示
- 内存指示器：IDE内存使用情况


## 三、界面自定义技巧


- **调整布局**： - 拖动工具窗口标题可停靠/浮动 - 右键工具窗口标题可设置显示位置 - 视图(View) → 工具窗口(Tool Windows) 控制各面板显示
- **恢复默认布局**： - 窗口(Window) → 恢复默认布局(Restore Default Layout)
- **全屏模式**： - 视图(View) → 全屏模式(Enter Full Screen) - 或使用快捷键 Ctrl+Shift+F12
- **分屏编辑**： - 右键编辑器标签 → 拆分(Split) - 支持垂直/水平分屏


## 四、中文界面特殊说明


- **术语对照**： - "Refactor" → "重构" - "Inspect Code" → "检查代码" - "Run Configuration" → "运行配置"
- **中文输入问题**： - 如遇输入法不跟随，可尝试： 文件 → 设置 → 外观与行为 → 外观 → 取消勾选"使用原生输入法" - 或切换不同输入法
- **中文编码设置**： - 文件 → 设置 → 编辑器 → 文件编码 - 建议设置为UTF-8 - 可设置"透明转换"处理已有文件


## 五、常用视图模式


- **专注模式**： - 视图(View) → 进入专注模式(Distraction Free Mode) - 隐藏所有工具窗口，专注代码编辑
- **演示模式**： - 视图(View) → 进入演示模式(Presentation Mode) - 放大代码字体，适合演示
- **全项目视图**： - 双击Shift → 搜索"项目视图(Project View)" - 最大化项目结构浏览








	  AI 思考中...





			** [PyCharm 创建第一个 Python 项目](https://www.runoob.com/pycharm-first-python-project.html)
			[PyCharm 创建与管理项目](https://www.runoob.com/pycharm-new-project.html) **













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