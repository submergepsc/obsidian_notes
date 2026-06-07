# TypeScript 项目引用 References

- Source: https://www.runoob.com/typescript/ts-references.html

项目引用是 TypeScript 提供的组织大型项目的功能，允许将 TypeScript 项目拆分为更小的部分。


它可以实现增量构建、更好的代码组织和更快的编译速度。


---






  项目引用 References 原理



  主项目 (app)

    package.json
    tsconfig.json
    references: [...]




组件库 (ui) Button, Modal, Input 工具库 (utils) formatDate, request 类型定义 (types) User, API Response --- ## 为什么需要项目引用 随着项目增长，单一的 tsconfig.json 会导致编译速度变慢。


项目引用允许将项目拆分为独立的子项目，每个子项目可以独立编译。


这不仅提高了编译速度，还提供了更好的代码组织方式。


**
概念：**项目引用允许一个 TypeScript 项目引用其他项目，实现增量编译和更好的代码组织。


---


## 创建引用项目


首先创建被引用的子项目。


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

        // 生成 sourcemap
        "sourceMap": true,

        // 是否为库
        "composite": true
    },

    // 包含的文件
    "include": ["src/**/*"],

    // 排除的文件
    "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```


**
composite：**设置为 true 启用项目引用功能，这是被引用的项目必须设置的选项。


---


## 主项目配置


在主项目的 tsconfig.json 中配置 references。


## tsconfig.json (主项目)


```javascript
{
    // 继承基础配置
    "extends": "./tsconfig.base.json",

    // 编译器选项
    "compilerOptions": {
        // 输出目录
        "outDir": "./dist",

        // 声明文件目录
        "declarationDir": "./dist/types",

        // 生成声明文件
        "declaration": true,

        // 生成 sourcemap
        "sourceMap": true
    },

    // 项目引用配置
    "references": [
        // 引用 utils 项目
        { "path": "./packages/utils" },

        // 引用 ui 项目
        { "path": "./packages/ui" },

        // 引用 types 项目
        { "path": "./packages/types" }
    ],

    // 包含的文件
    "include": ["src/**/*"],

    // 依赖包含的节点模块
    // "files": []
}
```


**
references：**数组中的每个对象指定一个引用的项目路径，path 相对于当前项目。


---


## 类型引用


在代码中使用被引用项目的类型。


## src/index.ts


```javascript
// 导入工具函数（来自 utils 包）
import { formatDate, formatCurrency } from '@my-utils/format';

// 导入组件（来自 ui 包）
import { Button, Modal, Input } from '@my-ui/core';

// 导入类型（来自 types 包）
import { User, ApiResponse } from '@my-types/common';

// 定义用户数据
const user: User = {
    id: 1,
    name: "Alice",
    email: "[email protected]"
};

// 格式化日期
const dateStr = formatDate(new Date(), "YYYY-MM-DD");
console.log("日期: " + dateStr);

// 格式化货币
const price = formatCurrency(999);
console.log("价格: " + price);

// 创建用户界面
const button = new Button({
    text: "提交",
    variant: "primary"
});

console.log("应用初始化成功");
```


**
导入方式：**被引用项目的导出可以直接导入，TypeScript 会自动解析类型。


---


## 增量构建


项目引用支持增量构建，只编译修改的部分。


## 构建命令


```javascript
# 构建整个项目（包括所有引用）
npm run build

# 只构建主项目（不重新构建依赖）
npm run build -- --build

# 清理并重建
npm run clean
npm run build

# 增量构建（推荐）
# 修改某个包后，只重新编译该包和依赖它的包
npx tsc -b packages/utils
npx tsc -b packages/ui
npx tsc -b .
```


**
增量构建：**使用 -b (build) 选项时，TypeScript 会自动检测哪些项目需要重新编译。


---


## 注意事项


- **composite 选项：**被引用的项目必须设置 composite: true
- **输出目录：**每个项目需要独立的输出目录
- **声明文件：**被引用项目需要生成声明文件
- **构建顺序：**依赖的项目需要先构建


**
最佳实践：**将公共代码拆分为独立包，使用项目引用进行管理，提高编译效率。


---


## 总结


项目引用是 TypeScript 管理大型项目的核心功能。


- **references：**配置项目引用关系
- **composite：**启用项目引用
- **增量构建：**只编译修改的部分
- **代码组织：**拆分为独立模块


**
建议：**在大型项目中，使用项目引用来组织代码，提高开发效率。









	  AI 思考中...





			** [TypeScript 路径映射 paths](https://www.runoob.com/ts-paths.html)
			[TypeScript Monorepo 配置](https://www.runoob.com/ts-monorepo.html) **













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