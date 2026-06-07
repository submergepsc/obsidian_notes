# PyCharm 文件与文件夹操作

- Source: https://www.runoob.com/pycharm/pycharm-file.html

PyCharm 提供了强大的文件管理功能，让开发者可以高效组织项目结构。

本部分将详细介绍文件与文件夹的创建、移动、重命名、搜索等操作。


---


## 1. 文件与文件夹基本操作


### 1.1 创建新文件/文件夹


#### 方法1：右键菜单创建


- 在 **项目工具窗口（Project View）** 中右键目标目录
- 选择： - **新建 → Python 文件**（创建 `.py` 文件） - **新建 → 目录**（创建文件夹） - 其他文件类型（HTML、JSON 等）


![](https://www.runoob.com/wp-content/uploads/2025/04/eb6c08e0-0366-499f-b4a8-37af76831ab5.png)


#### 方法2：快捷键创建


- **新建文件**：`Alt + Insert`（Windows/Linux） / `⌘N`（Mac）
- **新建目录**：同上操作，选择 "Directory"


---


### 1.2 重命名文件/文件夹


#### 安全重命名（推荐）


![](https://www.runoob.com/wp-content/uploads/2025/04/559ccee0-2045-48e0-ae86-9f447e620925.png)


- 选中文件 → 右键 → **重构（Refactor）→ 重命名（Rename）**
- 或使用快捷键：`Shift + F6`
- 输入新名称 → 按 `Enter` 确认


**优势**：


- 自动更新所有引用该文件的代码
- 避免因手动重命名导致导入错误


#### 直接重命名（不推荐）


- 右键 → **重命名**（可能破坏代码引用）


---


### 1.3 移动文件/文件夹


![](https://www.runoob.com/wp-content/uploads/2025/04/d9a7036a-fa09-4302-82a7-0b2ad1f769bb.png)


#### 安全移动（推荐）


- 选中文件 → 右键 → **重构（Refactor）→ 移动（Move）**
- 或快捷键：`F6`
- 选择目标目录 → 点击 **Refactor**


**效果**：


- 自动修复所有导入路径
- 例如：将 `utils/helper.py` 移动到 `core/` 下，所有 `from utils.helper import xxx` 会自动更新为 `from core.helper import xxx`


#### 拖放移动（不推荐）


- 直接拖拽文件可能导致导入路径错误


---


### 1.4 删除文件/文件夹


#### 安全删除


![](https://www.runoob.com/wp-content/uploads/2025/04/9507767d-c28e-4520-b101-8130dcfd9fdf.png)


- 选中文件 → 右键 → **重构（Refactor）→ 安全删除（Safe Delete）**
- 或快捷键：`Alt + Delete`
- PyCharm 会检查是否有代码引用该文件 → 确认删除


#### 普通删除


- 右键 → **删除（Delete）**（不会检查引用）


---


## 2. 文件内容操作


### 2.1 快速导航


| 操作 | 快捷键（Windows/Linux） | 快捷键（Mac） |
| --- | --- | --- |
| 跳转到文件 | Ctrl + Shift + N | ⌘ + Shift + O |
| 跳转到类 | Ctrl + N | ⌘ + O |
| 跳转到符号（方法/变量） | Ctrl + Alt + Shift + N | ⌘ + Option + O |
| 最近打开的文件 | Ctrl + E | ⌘ + E |


---


### 2.2 代码搜索与替换


![](https://www.runoob.com/wp-content/uploads/2025/04/d5649105-ba08-40f7-9900-67407f078fde.png)


#### 项目内搜索


- **全局搜索**：`Ctrl + Shift + F`（Mac：`⌘ + Shift + F`） - 支持正则表达式、大小写匹配、文件类型过滤
- **当前文件搜索**：`Ctrl + F`（Mac：`⌘ + F`）


#### 替换操作


- **全局替换**：`Ctrl + Shift + R`（Mac：`⌘ + Shift + R`）
- **当前文件替换**：`Ctrl + R`（Mac：`⌘ + R`）


---


### 2.3 文件对比


- 选中两个文件 → 右键 → **比较文件（Compare Files）**
- 或使用 **版本控制工具** 查看文件修改差异


---


## 3. 高级文件管理技巧


### 3.1 文件模板


**自定义新建文件时的默认内容**：


- ** 设置 → 编辑器 → 文件和代码模板** ![](https://www.runoob.com/wp-content/uploads/2025/04/74272f4f-f7eb-4d77-a267-3464e58ee7bb.png)
- 选择 **Python Script**，修改模板：
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: ${USER}
@Date: ${DATE}
@Description:
"""

def main():
    pass

if __name__ == '__main__':
    main()
```
 ![](https://www.runoob.com/wp-content/uploads/2025/04/e4c6286a-4fd3-416a-a3e6-a88087aa47a6.png)


---


### 3.2 本地历史记录


PyCharm 自动记录文件修改历史（无需 Git）：


- 右键文件 → **本地历史 → 显示历史（Local History → Show History）** ![](https://www.runoob.com/wp-content/uploads/2025/04/9f2fd9c9-e1a2-4b2c-907c-a9961c26f21e.png)
- 可恢复任意时间点的版本 ![](https://www.runoob.com/wp-content/uploads/2025/04/b30d1baa-640e-4c13-840c-34c239e36ebd.png)


---


### 3.3 文件标记


- **书签（Bookmarks）**： 添加书签：`F11`（行级）/ `Ctrl + F11`（带标记）
- 查看书签：`Shift + F11`




**TODO 注释**：



会在 **TODO 工具窗口** 中集中显示




---


## 4. 常见问题解答


### Q1：如何隐藏特定文件/文件夹？


- 右键文件 → **Mark Directory as → Excluded**
- 或编辑 `.idea/.gitignore`


### Q2：如何批量重命名文件？


- 选中多个文件 → `Shift + F6`
- 使用模式替换（如 `test_*.py → spec_*.py`）


### Q3：如何恢复误删的文件？


- 右键项目根目录 → **Local History → Show History**
- 找到删除前的版本 → 恢复


---


## 5. 操作速查表



| 操作 | 快捷键（Win/Linux） | 快捷键（Mac） |
| --- | --- | --- |
| 新建文件 | Alt + Insert | ⌘N |
| 重命名 | Shift + F6 | ⇧F6 |
| 移动文件 | F6 | F6 |
| 安全删除 | Alt + Delete | ⌘Delete |
| 全局搜索 | Ctrl + Shift + F | ⌘ + Shift + F |
| 跳转到文件 | Ctrl + Shift + N | ⌘ + Shift + O |








	  AI 思考中...





			** [PyCharm 创建与管理项目](https://www.runoob.com/pycharm-new-project.html)
			[PyCharm 代码编辑](https://www.runoob.com/pycharm-code-editor.html) **













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