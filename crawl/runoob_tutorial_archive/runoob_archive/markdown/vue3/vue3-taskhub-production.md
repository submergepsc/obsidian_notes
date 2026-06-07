# 项目部署

- Source: https://www.runoob.com/vue3/vue3-taskhub-production.html

经过前几个章节的打磨，我们创建的 TaskHub 项目功能已经非常完善了，现在我们要跨出最后一步：**将它从本地开发环境推向生产服务器**。


在企业级落地中，我们需要确保代码在不同环境（测试、生产）能自动切换配置，并且加载速度极快。


---


## 环境变量管理：一套代码，多处运行


在真实开发中，API 地址或一些配置在开发环境和线上环境是不一样的。


Vite 默认支持 `.env` 文件。


在项目根目录下创建两个文件：


**`.env.development` (本地开发)**


```
VITE_API_BASE_URL=http://localhost:3000/api
VITE_APP_TITLE=TaskHub (Dev)
```


**`.env.production` (线上生产)**


```
VITE_API_BASE_URL=https://api.taskhub.com
VITE_APP_TITLE=TaskHub
```


**说明：**


- Vite 要求变量必须以 **`VITE_`** 开头才能被暴露给客户端代码。
- 在代码中通过 `import.meta.env.VITE_API_BASE_URL` 访问。


---


## 打包优化：极致的加载速度


当项目引入了 Vue Router, Pinia 等库后，打包出的 `index.js` 会变得很大。我们需要通过"分包"和"压缩"来优化。


### 分包策略 (Manual Chunks)


修改 `vite.config.js`，将第三方库打包成独立的 JS 文件，利用浏览器缓存。


## 实例


```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // 将 vue 相关库打包在一起
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          // 其他第三方库（如以后引入的 axios 或 echarts）
          // 'utils-vendor': ['axios'],
        }
      }
    }
  }
})
```


### Gzip 压缩配置


安装插件：`npm install -D vite-plugin-compression`


## 实例


```javascript
import viteCompression from 'vite-plugin-compression'

export default defineConfig({
  plugins: [
    // ...
    viteCompression({
      threshold: 10240, // 超过 10kb 的文件才压缩
      algorithm: 'gzip',
      ext: '.gz'
    })
  ]
})
```


---


## 自动化部署 (CI/CD)


我们以最流行的 **GitHub Actions** 为例，当你把代码推送到 GitHub 时，它会自动帮你打包并部署到 GitHub Pages 或你的服务器。


### 创建 Workflow 脚本


在项目根目录创建 `.github/workflows/deploy.yml`：


```
name: Deploy TaskHub

on:
  push:
    branches: [ main ] # 监听 main 分支的推送

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout &#x1f6ce;&#xfe0f;
        uses: actions/checkout@v4

      - name: Install and Build &#x1f527;
        run: |
          npm install
          npm run build

      - name: Deploy &#x1f680;
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          folder: dist # 打包产物目录
          branch: gh-pages # 部署到这个分支
```


---


## Docker 容器化落地 (进阶)


如果你的公司使用容器云，你需要一个 `Dockerfile`。它能保证你的 TaskHub 在任何服务器上的运行环境都一模一样。


在根目录创建 `Dockerfile`：


```
# 1. 使用 Nginx 镜像作为基础
FROM nginx:alpine

# 2. 将打包后的 dist 目录复制到 Nginx 的静态资源目录
COPY dist/ /usr/share/nginx/html/

# 3. 复制自定义 nginx 配置（解决单页面应用路由 404 问题）
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```


---


## TaskHub 项目全路线总结


到这里，你已经完成了一个从零开始、基于 **Vue 3 (JavaScript) + Tailwind v4** 的企业级实战项目：


- **架构层**：Vite + Tailwind v4 + Vue Router + Pinia。
- **逻辑层**：Composition API + 自定义 Composables 复用。
- **性能层**：shallowRef + v-memo + 打包分包。
- **工程层**：环境变量 + CI/CD 自动化部署。

整个项目目录结构：


```
src/
├── assets/          # 静态资源
├── components/      # 高复用原子组件 (Header, Input, Item, Filter)
├── composables/     # 自定义逻辑钩子 (useLocalStorage, useNotification)
├── router/          # 路由配置与权限守卫
├── stores/          # Pinia 状态仓库 (TaskStore)
├── views/           # 页面级组件 (Dashboard, Login)
├── App.vue          # 全局容器与页面过渡动画
└── main.js          # 项目入口
```


相关命令：


```
# 安装依赖
npm install

# 本地开发
npm run dev

# 生产打包
npm run build
```









	  AI 思考中...





			** [逻辑复用与性能优化](https://www.runoob.com/vue3-taskhub-optimization.html)
			[Vue3 is 属性](https://www.runoob.com/vue3-is-attr.html) **













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