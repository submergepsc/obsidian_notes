# PyCharm 代码编辑

- Source: https://www.runoob.com/pycharm/pycharm-code-editor.html

PyCharm 作为专业的 Python IDE，提供了强大的代码编辑功能。


本章节将详细介绍代码编辑的核心功能，包括智能补全、快捷键操作、代码重构等高效开发技巧。


---


## 基本编辑功能


### 代码补全（Code Completion）


PyCharm 提供多种智能补全方式：



| 补全类型 | 触发方式 | 说明 |
| --- | --- | --- |
| 基本补全 | Ctrl + Space（Win/Linux）⌘ + Space（Mac） | 显示变量、函数、类等建议 |
| 智能类型补全 | Ctrl + Shift + Space | 根据上下文推荐更精准的类型 |
| 文件名补全 | 输入路径时自动触发 | 快速补全文件路径 |
| 动态模板补全 | 输入缩写（如 main + Tab） | 快速生成代码片段（如 if __name__ ==...） |

输入 **im + Tab** → 自动补全为 **import**:


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-1.png)

输入 **for + Tab** → 生成完整 **for** 循环结构:


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-2.png)


---


### 语法高亮（Syntax Highlighting）


PyCharm 自动对代码元素着色：


- **关键字**（`def`, `class`）：蓝色
- **字符串**：绿色
- **注释**：灰色
- **错误语法**：红色波浪线


**自定义高亮**：


- ` 设置 → 编辑器 → 配色方案（Color Scheme）`
- 调整 Python 语法元素的颜色


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-3.png)


---


### 代码折叠（Code Folding）



| 操作 | 快捷键（Win/Linux） | 快捷键（Mac） |
| --- | --- | --- |
| 折叠当前代码块 | Ctrl + - | ⌘ + - |
| 展开当前代码块 | Ctrl + + | ⌘ + + |
| 折叠所有代码块 | Ctrl + Shift + - | ⌘ + Shift + - |
| 展开所有代码块 | Ctrl + Shift + + | ⌘ + Shift + + |

鼠标移动到编辑器代码区域的左边可以看到有个向下的箭头，点击它也能折叠：


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-4.png)


**支持折叠的代码结构**：


- 函数/方法
- 类定义
- 多行注释
- 导入语句组


---


## 快捷键与高效操作


### 常用快捷键速查表



| 功能 | 快捷键（Win/Linux） | 快捷键（Mac） |
| --- | --- | --- |
| 复制当前行 | Ctrl + D | ⌘ + D |
| 删除当前行 | Ctrl + Y | ⌘ + Delete |
| 移动行 | Alt + Shift + ↑/↓ | ⌥ + ⇧ + ↑/↓ |
| 快速修复建议 | Alt + Enter | ⌥ + Enter |
| 跳转到定义 | Ctrl + B | ⌘ + B |
| 查看参数提示 | Ctrl + P | ⌘ + P |


---


### 多行编辑与批量操作


#### 列选择模式（Column Selection）


- 按住 `Alt`（Win）或 `⌥`（Mac） + 鼠标拖动
- 或使用 `Alt + Shift + Insert` 切换列模式


**应用场景**：


```
# 批量修改多个变量前缀
old_name = 1    →  new_name = 1
old_value = 2   →  new_value = 2
```


#### 多光标编辑


- 按住 `Alt` + 鼠标点击（添加多个光标）
- 或 `Ctrl + G`（Win）/ `⌘ + G`（Mac） 选择相同单词


---


## 代码格式化与重构


### 自动格式化代码


- **格式化当前文件**： - `Ctrl + Alt + L`（Win/Linux） - `⌥ + ⌘ + L`（Mac）
- **格式化选中代码**： - 选中代码 → 右键 → **Reformat Code**


**配置格式化规则**：**` 设置 → 编辑器 → 代码样式 → Python`


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-5.png)


---


### 重命名变量/函数（安全重构）


- 选中标识符（变量/函数名）
- **右键 → Refactor → Rename**
- 或快捷键 `Shift + F6`
- 输入新名称 → 按 `Enter`


效果**：


- 所有引用该标识符的地方同步更新
- 支持跨文件重命名


---


### 提取方法（Extract Method）


将选中代码片段提取为新方法：


- 选中代码块
- `Ctrl + Alt + M`（Win）/ `⌘ + ⌥ + M`（Mac）
- 输入方法名 → 确认


## 实例


```python
# 提取前
def process_data(data):
    cleaned = []
    for item in data:
        if item.is_valid():  # ← 选中这部分代码
            cleaned.append(item)
    return cleaned

# 提取后
def process_data(data):
    cleaned = []
    for item in data:
        if is_valid_item(item):
            cleaned.append(item)
    return cleaned

def is_valid_item(item):  # ← 自动生成的新方法
    return item.is_valid()
```


---


### 内联（Inline）


将方法/变量内联到调用处：


- 光标定位到方法名/变量
- `Ctrl + Alt + N`（Win）/ `⌘ + ⌥ + N`（Mac）


```
# 内联前
def calculate_discount(price):
    return price * 0.9

total = calculate_discount(100)  # ← 光标在此行

# 内联后
total = 100 * 0.9  # ← 方法调用被替换为实际代码
```


---


## 高级编辑技巧


### 实时模板（Live Templates）


快速生成常用代码模式：


- 输入缩写（如 `iter`） → 按 `Tab`
- 预置模板： - `main` → 生成 `if __name__ == '__main__'` - `try` → 生成完整 try-except 块


**自定义模板**：**`设置 → 编辑器 → 实时模板`


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-6.png)


在代码编辑器中输入 iter 就可以显示模板信息：


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-7.png)


---


### 代码意图动作（Alt+Enter）


根据上下文快速修复或优化代码：


- 自动导入缺失的包
- 转换字符串格式（f-string / format）
- 优化条件表达式


操作**：光标定位到警告/建议处 → `Alt + Enter`


![](https://www.runoob.com/wp-content/uploads/2025/04/pycharm-codeeditor-8.png)


---


## 总结：高效编辑工作流


- **编写阶段**： - 用代码补全 (`Ctrl + Space`) 快速输入 - 用动态模板生成重复结构
- **优化阶段**： - 格式化代码 (`Ctrl + Alt + L`) - 用 `Alt + Enter` 快速修复问题
- **重构阶段**： - 提取方法 (`Ctrl + Alt + M`) - 安全重命名 (`Shift + F6`)








	  AI 思考中...





			** [Pycharm 文件与文件夹操作](https://www.runoob.com/pycharm-file.html)
			[PyCharm 运行与调试](https://www.runoob.com/pycharm-run-debug.html) **













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