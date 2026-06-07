# PyCharm 版本控制集成

- Source: https://www.runoob.com/pycharm/pycharm-git.html

PyCharm 提供了完整的 Git/GitHub 集成功能，让开发者可以直接在 IDE 中完成版本控制操作。


---


## 配置 Git/GitHub


- 打开 `文件/PyCharm → 设置 → 版本控制 → Git`
- 在 "Git 可执行文件路径" 中确认 PyCharm 已自动检测到 Git
- 点击 **测试** 按钮验证 Git 是否可用


![](https://www.runoob.com/wp-content/uploads/2025/04/74f71db3-678b-4b34-821e-7d8b720b0a45.png)


### 配置用户信息


在终端运行：


```
git config --global user.name "Your Name"
git config --global user.email "[email protected]"
```


### 集成 GitHub


** 1. 添加 GitHub 账户：**


- `文件/PyCharm → 设置 → 版本控制 → GitHub`
- 点击 **+** 添加账户
- 选择登录方式： **通过 Github 登录**：通过浏览器授权登录
- **通过令牌登录**：使用个人访问令牌



![](https://www.runoob.com/wp-content/uploads/2025/04/0fd16128-d02e-4c6f-ad1a-153e04f463b9.png)


** 2. SSH 配置（可选）：**


- 生成 SSH 密钥：`ssh-keygen -t ed25519 -C "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"`
- 将公钥添加到 GitHub 账户的 SSH keys 设置中


---


## 基本操作


我们可以在工具栏上的版本控制按钮创建 Git 仓库：


![](https://www.runoob.com/wp-content/uploads/2025/04/567955aa-3d3f-4dbc-b749-fd1bdc32fb3a.png)


之后项目上的版本控制按钮就会变成 master（主分支）：


![](https://www.runoob.com/wp-content/uploads/2025/04/78d58518-d4d9-44fa-82ea-45341fb49846.png)


### 提交与推送


#### 提交代码



在 **提交工具窗口**（Commit Tool Window）中：


- 勾选要提交的文件
- 输入提交信息
- 选择操作： **提交**（Commit）：仅本地提交
- **提交并推送**（Commit and Push）：提交后立即推送到远程




![](https://www.runoob.com/wp-content/uploads/2025/04/be919b04-e44a-4302-895b-f1c9f726036f.png)


**快捷键**：


- 提交：`Ctrl+K`（Win/Linux） / `⌘K`（Mac）
- 推送：`Ctrl+Shift+K`（Win/Linux） / `⌘⇧K`（Mac）


#### 查看变更



文件状态颜色标记：


- **蓝色**：已修改
- **绿色**：新增
- **灰色**：未跟踪
- **红色**：冲突


![](https://www.runoob.com/wp-content/uploads/2025/04/c4bcf6be-cdc9-46c8-b5c1-6160b1634aac.png)


### 拉取与合并


#### 拉取最新代码


- `Git → Pull` 或 `Ctrl+T`（Win/Linux） / `⌘T`（Mac）
- 选择合并策略： - **Merge**：保留所有提交历史 - **Rebase**：线性历史记录


#### 合并分支


- `Git → 分支 → 合并分支`
- 选择要合并的目标分支
- 解决可能的冲突（见 6.3 节）


### 查看历史与差异


#### 查看提交历史


- `Git → 显示历史` 或 `Alt+9`
- 功能： - 查看文件/项目历史 - 比较不同版本 - 回滚到特定版本


#### 比较差异


- **文件差异**： - 右键文件 → `Git → 比较与当前分支` - 或 `Ctrl+D`（Win/Linux） / `⌘D`（Mac）
- **行内差异**： - 修改的行会显示彩色标记 - 点击标记查看具体修改内容


---


## 6.3 解决冲突


### 1. 冲突产生场景


- 多人修改同一文件的同一区域
- 合并分支时出现冲突
- 拉取代码时提示冲突


### 2. 解决步骤


- **打开合并工具** - 冲突时会自动弹出合并对话框 - 或手动打开：`Git → 解决冲突`
- **三窗格对比界面** - **左侧**：你的版本（当前分支） - **右侧**：他人版本（合并分支） - **中间**：合并结果编辑区
- **处理冲突** - 点击 **>>** 接受左侧更改 - 点击 **


### 储藏（Stash）变更


- 临时保存未完成的修改： `Git → 储藏`
- 恢复：`Git → 取消储藏`


### 交互式变基


- `Git → 交互式变基`
- 可以： - 重新排序提交 - 合并提交 - 修改提交信息








	  AI 思考中...





			** [PyCharm 运行与调试](https://www.runoob.com/pycharm-run-debug.html)
			[PyCharm 数据库工具](https://www.runoob.com/pycharm-dbtool.html) **













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