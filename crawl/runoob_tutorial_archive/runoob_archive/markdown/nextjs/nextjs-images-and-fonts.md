# Next.js 图片和字体

- Source: https://www.runoob.com/nextjs/nextjs-images-and-fonts.html

Next.js 提供了内置的图片和字体优化功能，旨在提升应用性能和用户体验。

Next.js 的图片和字体优化功能为开发者提供了强大的工具，帮助构建高性能、用户体验优秀的 Web 应用。


| 功能 | 说明 |
| --- | --- |
| 图片优化 | 使用 组件，支持本地和远程图片，自动优化尺寸和加载性能。 |
| 字体优化 | 使用 next/font 模块，支持 Google 字体和本地字体，自动托管和优化加载。 |
| 静态资源管理 | 将静态资源放入 public 目录，通过 /filename 直接访问。 |


---


## 静态资源管理

Next.js 允许将静态资源（如图片、字体等）存放在 public 目录下。

这些资源可以通过 /filename 直接访问。


目录结构示例：


```
my-next-app/
├── app/
├── public/
│   ├── images/
│   │   └── logo.png
│   └── fonts/
│       └── my-font.woff2
├── package.json
└── next.config.js
```


**public/images/logo.png** 可以通过 **/images/logo.png** 访问。


## 图片优化

Next.js 提供了 `` 组件，用于优化图片加载。它扩展了 HTML 的 `` 元素，提供了以下功能：

- **尺寸优化**：自动为不同设备提供正确尺寸的图片，支持现代图片格式（如 WebP）。
- **视觉稳定性**：防止图片加载时的布局偏移（Layout Shift）。
- **更快加载**：使用原生浏览器懒加载，仅在图片进入视口时加载。
- **资源灵活性**：支持按需调整图片尺寸，即使是远程图片。

### 使用 组件


从 `next/image` 导入 `` 组件，并在组件中使用。


## 实例


```javascript
import Image from 'next/image';

export default function Page() {
  return <Image src="/images/logo.png" alt="Logo" width={500} height={300} />;
}
```


### 本地图片


本地图片可以直接从 public 目录引用。


## 实例


```javascript
import Image from 'next/image';
import profilePic from './me.png';

export default function Page() {
  return (
    <Image
      src={profilePic}
      alt="Picture of the author"
      // width 和 height 会自动从图片文件中获取
      // blurDataURL 和 placeholder 可选
    />
  );
}
```


### 远程图片


远程图片需要手动指定 width 和 height，以避免布局偏移。


## 实例


```javascript
import Image from 'next/image';

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  );
}
```


### 配置远程图片

在 next.config.js 中配置允许的远程图片域名。


## 实例


```javascript
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
      },
    ],
  },
};

export default nextConfig;
```


---


## 字体优化

Next.js 提供了 `next/font` 模块，用于优化字体加载。它支持自动托管字体文件，提升隐私和性能。


### 使用 Google 字体

从 next/font/google 导入字体，并应用到 HTML 元素。


## 实例


```javascript
import { Geist } from 'next/font/google';

const geist = Geist({
  subsets: ['latin'],
});

export default function Layout({ children }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  );
}
```


如果使用非可变字体，需要指定 weight：


## 实例


```javascript
import { Roboto } from 'next/font/google';

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
});

export default function Layout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  );
}
```


### 使用本地字体

从 next/font/local 导入本地字体文件。


## 实例


```javascript
import localFont from 'next/font/local';

const myFont = localFont({
  src: './my-font.woff2',
});

export default function Layout({ children }) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  );
}
```


如果使用多个字体文件：


## 实例


```javascript
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
});
```









	  AI 思考中...





			** [Next.js Tailwind CSS](https://www.runoob.com/nextjs-tailwindcss.html)
			[Next.js 组件与布局](https://www.runoob.com/nextjs-components-layout.html) **













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