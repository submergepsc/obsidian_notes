# Linux hg 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

hg 是 Mercurial 分布式版本控制系统的命令行工具。Mercurial 是一个轻量级的分布式版本控制系统，由 Python 编写，与 Git 类似但设计上更简洁。

* * *

## hg 基本概念

### 版本控制系统

版本控制系统(VCS)用于跟踪文件变更历史，支持多人协作开发。分为集中式(如SVN)和分布式(如Git、Mercurial)。

### 分布式VS集中式

  * **分布式** ：每个开发者都有完整的仓库副本和历史记录
  * **集中式** ：只有一个中央仓库存储所有历史记录



### Mercurial特点

  * 简单直观的命令设计
  * 高性能处理大型项目
  * 跨平台支持
  * 可扩展的插件系统



* * *

## hg 安装与配置

### 安装方法

## 实例

```bash
# Ubuntu/Debian sudo apt-get install mercurial # CentOS/RHEL sudo yum install mercurial # macOS (使用Homebrew) brew install mercurial
```


### 基本配置

编辑 `~/.hgrc` 文件：

## 实例

```bash
[ ui ] username = Your Name
```


* * *

## hg 常用命令详解

### 仓库操作

## 实例

```bash
# 初始化新仓库 hg init 项目名 # 克隆现有仓库 hg clone https: // example.com / repo
```


### 文件跟踪

## 实例

```bash
# 添加文件到版本控制 hg add 文件名 # 查看仓库状态 hg status # 提交变更 hg commit -m "提交说明"
```


### 分支管理

## 实例

```bash
# 创建新分支 hg branch 分支名 # 切换分支 hg update 分支名 # 查看所有分支 hg branches
```


### 变更历史

## 实例

```bash
# 查看提交历史 hg log # 查看特定文件的修改历史 hg log 文件名 # 显示变更内容 hg diff
```


### 远程操作

## 实例

```bash
# 拉取远程变更 hg pull # 推送本地变更 hg push # 查看远程仓库 hg paths
```


* * *

## hg 高级用法

### 撤销更改

## 实例

```bash
# 撤销工作目录修改 hg revert 文件名 # 回退到特定版本 hg update -r 版本号
```


### 合并分支

## 实例

```bash
# 合并另一分支到当前分支 hg merge 分支名 # 解决冲突后标记为已解决 hg resolve -m 文件名
```


### 打标签

## 实例

```bash
# 创建标签 hg tag 标签名 # 查看所有标签 hg tags
```


* * *

## hg 与 Git 比较

特性 | hg (Mercurial) | Git  
---|---|---  
学习曲线 | 较平缓 | 较陡峭  
命令设计 | 更一致 | 更灵活  
分支模型 | 命名分支 | 轻量分支  
Windows支持 | 原生支持好 | 需要Git Bash  
插件系统 | 强大 | 强大  
  
* * *

## 实际应用示例

### 示例1：创建新项目

## 实例

```bash
# 1. 创建项目目录 mkdir myproject cd myproject # 2. 初始化仓库 hg init # 3. 创建文件并添加 echo "Hello World" & gt; README.txt hg add README.txt # 4. 提交初始版本 hg commit -m "Initial commit"
```


### 示例2：团队协作流程

## 实例

```bash
# 1. 克隆远程仓库 hg clone https: // team-server.com / project # 2. 创建特性分支 hg branch feature-x hg commit -m "Start feature X" # 3. 开发完成后推送到服务器 hg push \--new-branch # 4. 其他成员获取更新 hg pull hg update feature-x
```


* * *

## 常见问题解决

### 问题1：提交了错误内容

## 实例

```bash
# 回退到最后一次提交 hg rollback # 或者创建反向变更 hg backout 错误提交ID
```


### 问题2：合并冲突

  1. 冲突文件会包含标记
  2. 编辑文件解决冲突
  3. 标记为已解决
  4. 完成合并提交



## 实例

```bash
hg resolve -m 冲突文件 hg commit -m "Merge conflict resolved"
```


### 问题3：找回删除的文件

## 实例

```bash
# 查看删除历史 hg log \--removed # 恢复特定版本的文件 hg revert -r 版本号 文件名
```


* * *

## 最佳实践建议

  1. **频繁提交** ：小步提交，保持每个提交的原子性
  2. **描述性消息** ：提交信息应清晰说明变更内容
  3. **分支策略** ：为长期分支(如开发、发布)和短期特性分支使用不同策略
  4. **定期同步** ：经常执行 pull/push 保持与团队同步
  5. **备份重要分支** ：关键分支推送到远程服务器



* * *

## 学习资源推荐

  1. 官方文档：<https://www.mercurial-scm.org/guide>
  2. 《Mercurial: The Definitive Guide》电子书
  3. hg 内置帮助：`hg help` 或 `hg help 命令名`
  4. 交互式教程：<https://hginit.com/>



通过掌握 hg 命令，你可以高效管理项目版本，与团队协作开发。虽然 Git 目前更流行，但 Mercurial 的简洁设计使其在某些场景下仍是优秀选择。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
