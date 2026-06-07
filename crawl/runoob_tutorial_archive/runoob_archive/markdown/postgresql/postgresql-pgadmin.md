# PostgreSQL pgAdmin 工具

- Source: https://www.runoob.com/postgresql/postgresql-pgadmin.html

**pgAdmin** 是一个开源的 PostgreSQL 数据库管理工具，提供了图形化的界面来简化数据库的管理与操作。


pgAdmin 是 PostgreSQL 官方推荐的管理工具，支持从简单的查询到复杂的数据库管理任务，适合开发者和数据库管理员使用。


## 主要功能


- **数据库管理：**支持创建、修改和删除数据库、表、视图、索引等。
- **SQL 查询：**内置 SQL 查询编辑器，支持代码高亮、自动补全和查询历史。
- **数据导入与导出：**支持 CSV、Excel、SQL 等多种格式的数据导入导出。
- **备份与恢复：**提供数据库的备份和恢复工具，支持全量和增量备份。
- **可视化设计：**支持 ER 图的可视化展示，帮助理解数据库结构。
- **多版本支持：**支持 PostgreSQL 的多个版本。
- **远程连接：**支持对远程数据库进行管理，方便跨区域的数据库维护。


![](https://www.runoob.com/wp-content/uploads/2025/05/pgAdmin-runoob.webp)


---


## pgAdmin 的安装

pgAdmin 官方网站：[https://www.pgadmin.org/](https://www.pgadmin.org/)。


pgAdmin Github 源码地址：[https://github.com/pgadmin-org/](https://github.com/pgadmin-org/)。


pgAdmin 4 是对 pgAdmin 的完全重写，基于 Python、ReactJS 和 JavaScript 构建。

pgAdmin 4支持两种运行模式：


- **桌面模式：**通过 Electron 打包，可独立运行，适合个人使用。
- **Web 模式：**可部署在 Web 服务器上，支持多用户通过浏览器访问。


下载地址：[https://www.pgadmin.org/download/](https://www.pgadmin.org/download/)


![](https://www.runoob.com/wp-content/uploads/2025/05/44e7b7fc-af64-4797-84a5-2266a804e7be.png)


### Windows 系统安装


- 访问 [pgAdmin 官方网站](https://www.pgadmin.org/download/)
- 下载适用于 Windows 的安装程序
- 运行安装程序并按照向导完成安装
- 安装完成后，可以在开始菜单中找到 pgAdmin


### macOS 系统安装


- 使用 Homebrew 安装：`brew install --cask pgadmin4`
- 或从官网下载 macOS 版本的安装包
- 将 pgAdmin 拖放到 Applications 文件夹


### Linux 系统安装


对于基于 Debian 的系统（如 Ubuntu）：


```
sudo apt update
sudo apt install pgadmin4
```


对于基于 Red Hat 的系统（如 CentOS）：


```
sudo yum install pgadmin4
```


---


## pgAdmin 的基本使用


### 连接到 PostgreSQL 服务器


- 打开 pgAdmin
- 在左侧的"浏览器"面板中，右键点击"Servers"
- 选择"Create" > "Server..."
- 在弹出的对话框中填写连接信息： - **Name**：为连接起一个名称 - **Host**：数据库服务器地址（本地使用 localhost） - **Port**：PostgreSQL 端口（默认 5432） - **Maintenance database**：通常使用 postgres - **Username** 和 **Password**：数据库凭据


### 浏览数据库对象


成功连接后，你可以展开服务器节点查看：


- 数据库列表
- 每个数据库中的表、视图、函数等对象
- 用户和角色
- 其他服务器对象


---


## pgAdmin 的核心功能


### 数据库管理


- **创建数据库**： - 右键点击"Databases" > "Create" > "Database..." - 填写数据库名称和其他选项
- **删除数据库**： - 右键点击要删除的数据库 > "Delete/Drop" - 确认操作
- **备份和恢复**： - 右键点击数据库 > "Backup..." 或 "Restore..." - 选择备份文件位置和选项


### 表操作


- **创建表**： - 展开数据库 > 右键点击"Tables" > "Create" > "Table..." - 定义列名、数据类型和约束
- **查看和编辑数据**： - 右键点击表 > "View/Edit Data" > "All Rows" - 在数据网格中可以直接编辑数据
- **执行 SQL 查询**： - 点击工具栏上的"SQL"按钮 - 在查询编辑器中输入 SQL 语句 - 点击"Execute"按钮或按 F5 运行查询


---


## pgAdmin 的高级功能


### 查询工具


pgAdmin 提供了强大的查询工具，包括：


- 语法高亮
- 代码自动完成
- 查询执行计划分析
- 查询历史记录


### 性能监控


通过仪表板可以监控：


- 服务器状态
- 活动会话
- 锁信息
- 数据库统计信息


### 导入/导出数据


pgAdmin 支持多种数据格式的导入和导出：


- CSV
- JSON
- SQL 脚本
- Excel 文件


---


## pgAdmin 的使用技巧


- **快捷键**： - F5：执行查询 - Ctrl+Enter：执行选中的查询 - Ctrl+/：注释/取消注释代码
- **保存常用查询**： - 可以将常用查询保存为"Query Tool"的收藏夹
- **自定义界面**： - 通过"File" > "Preferences"自定义界面布局和设置
- **使用 ERD 工具**： - 可以生成数据库的实体关系图(ERD)
- **定期备份配置**： - pgAdmin 的配置存储在用户目录中，建议定期备份


---


## pgAdmin 的替代方案


虽然 pgAdmin 功能强大，但也有一些替代工具：


- **DBeaver**：支持多种数据库的通用工具
- **DataGrip**：JetBrains 推出的专业数据库 IDE
- **TablePlus**：现代化的轻量级数据库客户端
- **psql**：PostgreSQL 自带的命令行工具


---


## 常见问题解答


### 为什么 pgAdmin 启动很慢？


pgAdmin 是基于 Python 和 Web 技术的应用程序，首次启动可能需要一些时间加载。可以尝试：


- 确保系统满足最低要求
- 关闭不必要的浏览器标签
- 更新到最新版本


### 如何重置 pgAdmin 密码？


- 停止 pgAdmin 服务
- 删除用户目录中的 pgAdmin 配置文件
- 重新启动 pgAdmin


### 连接数据库时出现认证错误怎么办？


- 检查 PostgreSQL 的 pg_hba.conf 文件配置
- 确保用户名和密码正确
- 验证服务器是否允许远程连接（如果从外部连接）








	  AI 思考中...





			** [PostgreSQL 常用函数](https://www.runoob.com/postgresql-functions.html)














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