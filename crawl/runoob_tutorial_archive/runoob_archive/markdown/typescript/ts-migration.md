# TypeScript 从 JavaScript 迁移

- Source: https://www.runoob.com/typescript/ts-migration.html

将现有 JavaScript 项目逐步迁移到 TypeScript。


---


## 迁移策略


- 添加 tsconfig.json
- 重命名 .js 为 .ts
- 逐步添加类型注解
- 启用严格模式


---


## 配置 tsconfig.json


## tsconfig.json


```javascript
{
    "compilerOptions": {
        // 初始阶段：宽松配置
        "target": "ES2020",
        "module": "commonjs",
        "strict": false,
        "noImplicitAny": false,
        "strictNullChecks": false,
        "skipLibCheck": true,

        // 允许 JS 文件
        "allowJs": true,
        "checkJs": false,

        // 输出目录
        "outDir": "./dist",
        "rootDir": "./src"
    },
    "include": ["src/**/*"],
    "exclude": ["node_modules", "dist"]
}
```


---


## 逐步启用严格检查


## 分阶段启用


```javascript
// 阶段 1: 基础迁移
{
    "compilerOptions": {
        "strict": false,
        "noImplicitAny": false
    }
}

// 阶段 2: 启用类型检查
{
    "compilerOptions": {
        "strict": true,
        "noImplicitAny": true,
        "strictNullChecks": true
    }
}

// 阶段 3: 完全严格
{
    "compilerOptions": {
        "strict": true,
        "noImplicitAny": true,
        "strictNullChecks": true,
        "strictFunctionTypes": true,
        "strictPropertyInitialization": true
    }
}
```


---


## JSDoc 类型注释


在 JavaScript 中使用 JSDoc 添加类型。


## utils.js


```javascript
/**
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function add(a, b) {
    return a + b;
}

/**
 * @typedef {Object} User
 * @property {number} id
 * @property {string} name
 * @property {string} email
 */

/**
 * @param {number} id
 * @returns {Promise<User>}
 */
function getUser(id) {
    return fetch(`/api/users/${id}`).then(r => r.json());
}
```


**运行结果：**


```
JSDoc 注释添加成功
```


---


## 类型声明文件


为没有类型定义的模块创建声明。


## src/types/my-module.d.ts


```javascript
declare module "my-module" {
    export function doSomething(param: string): void;
    export class MyClass {
        constructor(options: { name: string });
        name: string;
    }
}
```


---


## declare 关键字


## 实例


```javascript
// 声明全局变量
declare var GLOBAL_CONFIG: {
    apiUrl: string;
    version: string;
};

// 声明全局函数
declare function myFunction(param: string): void;

// 声明命名空间
declare namespace MyNamespace {
    function doSomething(): void;
}

// 使用
console.log(GLOBAL_CONFIG.apiUrl);
myFunction("hello");
MyNamespace.doSomething();
```


**运行结果：**


```
声明成功
```


---


## 迁移工具


- **tsc --allowJs：**编译 JS 文件
- **checkJs：**检查 JS 类型
- **// @ts-check：**单文件类型检查
- **// @ts-ignore：**忽略错误


## legacy.js


```javascript
// @ts-check
// @ts-ignore
var result = someLegacyFunction();
```


---


## 最佳实践


- 从关键模块开始迁移
- 添加单元测试
- 逐步启用严格模式
- 使用 JSDoc 注释
- 创建类型声明文件


---


## 总结


- **渐进式：**逐步迁移
- **JSDoc：**类型注释
- **声明文件：**.d.ts
- **严格模式：**分阶段启用


---









	  AI 思考中...





			** [TypeScript 模板字面量类型](https://www.runoob.com/ts-template-literal.html)
			[TypeScript 单元测试](https://www.runoob.com/ts-unit-testing.html) **













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