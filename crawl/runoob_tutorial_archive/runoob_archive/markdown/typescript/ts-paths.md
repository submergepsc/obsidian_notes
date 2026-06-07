# TypeScript 路径映射 paths

- Source: https://www.runoob.com/typescript/ts-paths.html

paths 是 tsconfig.json 中的配置选项，用于配置模块路径别名。


它可以让导入路径更简洁，同时保持代码的组织结构清晰。


---






  路径映射 paths 工作原理



  原始导入路径

    import Button from
      "../../components/Button"




使用别名导入 import Button from "@/components/Button" tsconfig paths 配置 paths 配置项 baseUrl 基准路径 paths 路径别名 rootDirs 根目录 --- ## 为什么需要路径映射 随着项目规模增长，文件目录会越来越深。


使用相对路径导入文件（如 ../../../components/Button）会让代码难以阅读和维护。


路径映射允许我们使用别名（如 @/components/Button）来替代冗长的相对路径。


**
别名：**路径别名让导入路径更简洁，同时便于调整项目结构。


---


## 基本配置


在 tsconfig.json 中配置 paths 和 baseUrl。


## tsconfig.json


```javascript
{
    "compilerOptions": {
        // 基准路径：所有路径别名的根目录
        "baseUrl": ".",

        // 路径映射配置
        "paths": {
            // @/ 开头的别名，指向 src 目录
            "@/*": ["src/*"],

            // @components 开头的别名
            "@components/*": ["src/components/*"],

            // @utils 开头的别名
            "@utils/*": ["src/utils/*"],

            // @services 开头的别名
            "@services/*": ["src/services/*"],

            // @assets 开头的别名
            "@assets/*": ["src/assets/*"],

            // @types 开头的别名
            "@types/*": ["src/types/*"]
        }
    }
}
```


**
baseUrl：**设置 baseUrl 后，paths 中的路径将相对于此目录解析。


---


## 使用路径别名


配置完成后，可以在代码中使用别名导入模块。


## src/components/Button.tsx


```javascript
// 使用路径别名导入
import { Button } from '@/components/Button';
import { User } from '@types/user';
import { fetchUser } from '@services/userApi';
import { formatDate } from '@utils/date';

// 导入样式
import styles from '@/components/Button.module.css';

// 导入图片
import logo from '@assets/logo.png';

// 使用导入的模块
const handleClick = () => {
    console.log('按钮点击');
};

const userButton = new Button({
    text: '用户',
    onClick: handleClick
});

console.log('组件加载成功');
```


**
语法：**在 paths 配置中使用 * 作为通配符，导入时用 * 匹配实际路径。


---


## Webpack 别名配置


如果使用 Webpack，还需要配置 resolve.alias 以支持运行时。


## webpack.config.js


```javascript
// 导入 webpack 模块
const path = require('path');

// Webpack 配置
module.exports = {
    // 其他配置...
    resolve: {
        // 路径别名配置，需要与 tsconfig.json 保持一致
        alias: {
            // @ 开头的别名
            '@': path.resolve(__dirname, 'src'),

            // 其他别名
            '@components': path.resolve(__dirname, 'src/components'),
            '@utils': path.resolve(__dirname, 'src/utils'),
            '@services': path.resolve(__dirname, 'src/services'),
            '@types': path.resolve(__dirname, 'src/types'),
            '@assets': path.resolve(__dirname, 'src/assets')
        },

        // 文件扩展名
        extensions: ['.ts', '.tsx', '.js', '.jsx', '.json']
    }
};
```


**
运行时要一致：**Webpack 的 alias 配置必须与 TypeScript 的 paths 配置保持一致，否则运行时会出现模块找不到的错误。


---


## Vite 配置


使用 Vite 时，需要在 tsconfig.json 和 vite.config.ts 中同时配置。


## vite.config.ts


```javascript
// 导入 vite 模块
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// Vite 配置
export default defineConfig({
    plugins: [react()],

    // 路径别名配置
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
            '@components': path.resolve(__dirname, './src/components'),
            '@utils': path.resolve(__dirname, './src/utils'),
            '@services': path.resolve(__dirname, './src/services'),
            '@types': path.resolve(__dirname, './src/types'),
            '@assets': path.resolve(__dirname, './src/assets')
        }
    }
});
```


**
Vite：**Vite 使用 Rollup 作为打包引擎，需要在 resolve.alias 中配置别名。


---


## 多项目路径配置


在 Monorepo 项目中，可以配置跨包的路径别名。


## tsconfig.json (Monorepo)


```javascript
{
    "compilerOptions": {
        // 基准路径
        "baseUrl": ".",

        // 路径映射，支持跨包引用
        "paths": {
            // 引用当前包的模块
            "@/*": ["src/*"],

            // 引用其他包的模块
            "@my-ui/button": ["packages/ui-button/src/index.ts"],
            "@my-ui/modal": ["packages/ui-modal/src/index.ts"],
            "@my-utils/date": ["packages/utils-date/src/index.ts"],
            "@my-hooks/useFetch": ["packages/hooks-use-fetch/src/index.ts"]
        }
    }
}
```


**
Monorepo：**在 Monorepo 项目中，paths 可以引用其他包的源码路径。


---


## 注意事项


- **baseUrl 必需：**paths 需要与 baseUrl 配合使用
- **通配符匹配：**使用 * 匹配任意路径
- **保持一致：**Webpack/Vite 配置必须与 tsconfig 保持一致
- **相对路径：**paths 中的路径是相对于 baseUrl 的


**
最佳实践：**使用路径别名可以让代码更简洁，但不要滥用，建议统一命名规范。


---


## 总结


路径映射是 TypeScript 项目中管理导入路径的重要工具。


- **paths：**配置路径别名
- **baseUrl：**设置基准路径
- **通配符：**使用 * 匹配任意字符
- **构建工具：**Webpack/Vite 需要同步配置


**
建议：**为常用目录设置路径别名，提高代码可读性和可维护性。








	  AI 思考中...





			** [TypeScript 协变与逆变](https://www.runoob.com/ts-covariance.html)
			[TypeScript 项目引用 References](https://www.runoob.com/ts-references.html) **













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