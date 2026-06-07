# TypeScript Monorepo 配置

- Source: https://www.runoob.com/typescript/ts-monorepo.html

Monorepo 是一种将多个项目放在同一个代码仓库中的开发模式。


TypeScript 通过项目引用和工具链支持 Monorepo，可以高效管理多个包。


---






  Monorepo 项目结构



  根目录 (root)
  package.json | tsconfig.json | lerna.json | turbo.json



  packages/ 目录



  utils



  ui-components



  hooks



  app



  管理工具：npm workspaces | yarn workspaces | pnpm | lerna | turbo





--- ## 为什么需要 Monorepo 当项目包含多个包（如工具库、组件库、应用程序）时，传统方式需要维护多个代码仓库。


Monorepo 将所有包放在同一个仓库中，共享代码更方便，版本管理更统一。


TypeScript 的项目引用功能让 Monorepo 项目的类型检查和构建更高效。


**
概念：**Monorepo（单一仓库）将多个相关项目放在同一个代码仓库中，便于代码共享和协调开发。


---


## pnpm Workspace


pnpm 是现代的包管理器，原生支持 Workspace 功能。


## 根目录 package.json


```javascript
{
    "name": "my-monorepo",
    "version": "1.0.0",
    "private": true,

    // 启用 pnpm workspace
    "packages": [
        "packages/*"
    ],

    // 开发依赖
    "devDependencies": {
        "typescript": "^5.0.0"
    },

    // 脚本
    "scripts": {
        "build": "pnpm -r run build",
        "clean": "pnpm -r run clean",
        "type-check": "pnpm -r run type-check"
    }
}
```


**
pnpm：**pnpm 的 Workspace 功能可以自动将 packages 目录下的包链接在一起。


---


## 项目结构


创建 Monorepo 项目的目录结构。


## 目录结构


```javascript
my-monorepo/
├── packages/
│   ├── utils/              # 工具包
│   │   ├── src/
│   │   │   └── index.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   ├── ui-components/      # UI 组件包
│   │   ├── src/
│   │   │   ├── Button.tsx
│   │   │   └── index.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   └── app/                # 应用程序
│       ├── src/
│       │   └── index.tsx
│       ├── package.json
│       └── tsconfig.json
│
├── package.json            # 根目录配置
├── tsconfig.base.json     # 基础配置
└── pnpm-workspace.yaml    # pnpm 配置
```


**
packages：**所有包都放在 packages 目录下，每个包有独立的 package.json 和 tsconfig.json。


---


## 基础 TypeScript 配置


创建基础配置供所有包使用。


## tsconfig.base.json


```javascript
{
    // 编译器选项
    "compilerOptions": {
        // 目标版本
        "target": "ES2020",

        // 模块系统
        "module": "ESNext",

        // 严格模式
        "strict": true,

        // 跳过库类型检查
        "skipLibCheck": true,

        // 启用 ES 模块互操作
        "esModuleInterop": true,

        // 强制文件名大小写一致
        "forceConsistentCasingInFileNames": true,

        // 模块解析
        "moduleResolution": "bundler",

        // 解析 JSON 模块
        "resolveJsonModule": true,

        // 隔离模块
        "isolatedModules": true,

        // 不生成输出文件
        "noEmit": true
    }
}
```


**
继承：**各包的 tsconfig.json 继承基础配置，只覆盖需要自定义的选项。


---


## 工具包配置


为工具包配置 TypeScript。


## packages/utils/tsconfig.json


```javascript
{
    // 继承基础配置
    "extends": "../../tsconfig.base.json",

    // 编译器选项
    "compilerOptions": {
        // 输出目录
        "outDir": "./dist",

        // 声明文件目录
        "declarationDir": "./dist/types",

        // 生成声明文件
        "declaration": true,

        // 生成入口文件的声明
        "declarationMap": true,

        // 模块导出方式
        "module": "ESNext",

        // 启用项目引用
        "composite": true
    },

    // 包含的文件
    "include": ["src/**/*"],

    // 排除的文件
    "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```


**
composite：**启用项目引用后，TypeScript 可以增量编译此包。


---


## 应用程序配置


为主应用程序配置 TypeScript 并引用其他包。


## packages/app/tsconfig.json


```javascript
{
    // 继承基础配置
    "extends": "../../tsconfig.base.json",

    // 编译器选项
    "compilerOptions": {
        // 输出目录
        "outDir": "./dist",

        // JSX 配置
        "jsx": "react-jsx",

        // 路径别名
        "baseUrl": ".",
        "paths": {
            "@my-utils/*": ["../utils/src/*"],
            "@my-ui/*": ["../ui-components/src/*"]
        }
    },

    // 项目引用
    "references": [
        { "path": "../utils" },
        { "path": "../ui-components" }
    ],

    // 包含的文件
    "include": ["src/**/*"],

    // 排除的文件
    "exclude": ["node_modules", "dist"]
}
```


**
路径别名：**可以配置路径别名直接引用同仓库的其他包。


---


## 包之间的依赖


在 package.json 中声明对同仓库包的依赖。


## packages/app/package.json


```javascript
{
    "name": "@my-org/app",
    "version": "1.0.0",
    "private": true,

    "dependencies": {
        // 引用同仓库的包
        "@my-org/utils": "workspace:*",
        "@my-org/ui-components": "workspace:*",

        // 外部依赖
        "react": "^18.2.0",
        "react-dom": "^18.2.0"
    },

    "devDependencies": {
        // 开发依赖
        "@types/react": "^18.2.0",
        "typescript": "^5.0.0"
    }
}
```


**
workspace：**使用 workspace:* 指向同仓库的其他包，pnpm 会自动解析。


---


## 构建脚本


为 Monorepo 创建统一的构建脚本。


## 根目录 package.json


```javascript
{
    "scripts": {
        // 构建所有包
        "build": "pnpm -r run build",

        // 清理所有构建产物
        "clean": "pnpm -r run clean",

        // 类型检查
        "type-check": "pnpm -r run type-check",

        // 测试所有包
        "test": "pnpm -r run test",

        // 增量构建
        "build:watch": "pnpm -r --parallel run build:watch",

        // 启动应用
        "dev": "pnpm --filter @my-org/app run dev"
    }
}
```


**
pnpm -r：**递归执行所有包的同名脚本。


---


## 注意事项


- **包命名规范：**使用 @org-name/package 格式
- **独立版本：**每个包可以独立版本管理
- **workspace 协议：**使用 workspace:* 引用同仓库包
- **构建顺序：**被依赖的包需要先构建


**
最佳实践：**Monorepo 适合管理多个相关项目，可以显著提高代码复用和开发效率。


---


## 总结


Monorepo 是现代前端项目管理的推荐模式。


- **pnpm Workspace：**原生支持 Monorepo
- **项目引用：**实现增量编译
- **路径别名：**便捷引用同仓库包
- **统一管理：**共享配置和依赖


**
建议：**当项目包含多个相关包时，优先考虑 Monorepo 方案。









	  AI 思考中...





			** [TypeScript 项目引用 References](https://www.runoob.com/ts-references.html)
			[TypeScript 设计模式](https://www.runoob.com/ts-design-patterns.html) **













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