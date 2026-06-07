# NVM 管理多版本 Node.js

- Source: https://www.runoob.com/nodejs/nodejs-nvm.html

nvm（Node Version Manager）是一个非常有用的工具，可以让您在同一台机器上安装和管理多个 Node.js 版本。


![](https://www.runoob.com/wp-content/uploads/2025/05/1_20ffnM3_eVpgVGGAbpuDjg.png)


### 为什么需要 nvm？


- 不同项目可能需要不同版本的 Node.js
- 测试应用在不同 Node.js 版本下的兼容性
- 方便升级和降级 Node.js 版本


### 安装 nvm


**在 macOS/Linux 上安装 nvm：**


```
# 使用 curl 安装
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# 或使用 wget 安装
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# 重新加载 shell 配置
source ~/.bashrc
# 或
source ~/.zshrc
```


**在 Windows 上安装 nvm-windows：**


- 下载 nvm-windows：[https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
- 下载 nvm-setup.zip
- 解压并运行安装程序


**nvm 常用命令：**


```
# 查看 nvm 版本
nvm --version

# 列出所有可安装的 Node.js 版本
nvm list-remote
# Windows 上使用
nvm list available

# 安装最新的 LTS 版本
nvm install --lts

# 安装特定版本
nvm install 18.17.0
nvm install 16.20.1

# 列出已安装的版本
nvm list
# 或
nvm ls

# 切换到特定版本
nvm use 18.17.0

# 设置默认版本
nvm alias default 18.17.0

# 查看当前使用的版本
nvm current

# 卸载特定版本
nvm uninstall 16.20.1
```


**实际使用示例：**


```
# 场景：为不同项目使用不同 Node.js 版本

# 项目 A 使用 Node.js 18
cd project-a
nvm use 18.17.0
node --version  # v18.17.0

# 项目 B 使用 Node.js 16
cd ../project-b
nvm use 16.20.1
node --version  # v16.20.1

# 为项目指定 Node.js 版本
echo "18.17.0" > .nvmrc
nvm use  # 自动使用 .nvmrc 中指定的版本
```


### 验证安装是否成功


**创建第一个 Node.js 程序：**


创建一个名为 `hello.js` 的文件：


## 实例


```javascript
// hello.js
console.log('Hello, Node.js!');
console.log('Node.js 版本:', process.version);
console.log('当前工作目录:', process.cwd());
console.log('操作系统:', process.platform);
```


**预期输出：**


```
Hello, Node.js!
Node.js 版本: v18.17.0
当前工作目录: /Users/username/projects
操作系统: darwin
```


**检查全局安装路径：**


```
# 查看 npm 全局包安装路径
npm config get prefix

# 查看 npm 配置
npm config list

# 查看 Node.js 安装路径
which node
# Windows 上使用
where node
```









	  AI 思考中...





			** [Node.js 基础概念](https://www.runoob.com/nodejs-intro.html)
			[Node.js 异步编程](https://www.runoob.com/nodejs-asynchronous.html) **













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