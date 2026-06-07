# TypeScript 编译选项

- Source: https://www.runoob.com/typescript/ts-compiler-options.html

TypeScript 编译器（tsc）有众多编译选项，本教程详细介绍常用的编译选项及其作用。






  TypeScript 编译过程与编译选项



  TypeScript 源码
  .ts / .tsx
  包含类型注解



TypeScript 编译器 (tsc) 编译选项作用： • 类型检查 (strict) • 输出格式 (module) • 目标版本 (target) • 声明文件 (declaration) ...更多选项 编译输出 .js - JavaScript .d.ts - 类型声明 .map - Source Map 编译选项分类 类型检查 strict noImplicitAny strictNullChecks 输出控制 outDir declaration sourceMap 模块系统 module moduleResolution esModuleInterop 语言特性 target lib jsx --- ## 输出控制选项 ## 实例
```javascript
{
    "compilerOptions": {
        // 输出目录
        "outDir": "./dist",

        // 源码根目录
        "rootDir": "./src",

        // 生成 .d.ts 声明文件
        "declaration": true,

        // 声明文件输出目录
        "declarationDir": "./types",

        // 生成 source map
        "sourceMap": true,

        // 生成 .js.map 文件
        "mapRoot": "./map"
    }
}
```
 --- ## 类型检查选项 ## 实例
```javascript
{
    "compilerOptions": {
        // 严格模式（推荐始终开启）
        "strict": true,

        // 检查 null 和 undefined
        "strictNullChecks": true,

        // 检查 this 参数
        "noImplicitThis": true,

        // 严格函数类型
        "strictFunctionTypes": true,

        // 严格属性初始化
        "strictPropertyInitialization": true,

        // 不允许隐式 any
        "noImplicitAny": true,

        // 不允许返回 void
        "noImplicitReturns": true,

        // 开启所有严格检查
        "strict": true
    }
}
```
 --- ## 模块选项 ## 实例
```javascript
{
    "compilerOptions": {
        // 模块系统
        "module": "commonjs",

        // 模块解析策略
        "moduleResolution": "node",

        // 解析基础路径
        "baseUrl": ".",

        // 路径别名
        "paths": {
            "@/*": ["src/*"]
        },

        // ES 模块互操作
        "esModuleInterop": true,

        // 允许默认导入
        "allowSyntheticDefaultImports": true,

        // 隔离模块
        "isolatedModules": true
    }
}
```
 --- ## ES 特性选项 ## 实例
```javascript
{
    "compilerOptions": {
        // 编译目标
        "target": "ES2020",

        // 启用的库
        "lib": ["ES2020", "DOM"],

        // 允许未使用的局部变量
        "noUnusedLocals": true,

        // 允许未使用的参数
        "noUnusedParameters": true,

        // 代码降级
        "downlevelIteration": true
    }
}
```
 --- ## 实验性选项 ## 实例
```javascript
{
    "compilerOptions": {
        // 启用装饰器
        "experimentalDecorators": true,

        // 启用装饰器元数据
        "emitDecoratorMetadata": true,

        // 启用异步迭代器
        "emitDecoratorMetadata": true,

        // 跳过库检查
        "skipLibCheck": true
    }
}
```
 --- ## 常用编译选项组合 ## 实例
```javascript
// Node.js 项目推荐配置
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "commonjs",
        "lib": ["ES2020"],
        "outDir": "./dist",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "moduleResolution": "node",
        "declaration": true
    }
}
```
 --- ## 编译选项表 | 类别 | 常用选项 | | --- | --- | | 输出 | outDir, rootDir, declaration, sourceMap | | 类型检查 | strict, strictNullChecks, noImplicitAny | | 模块 | module, moduleResolution, paths, esModuleInterop | | ES 特性 | target, lib, downlevelIteration | | 实验性 | experimentalDecorators, emitDecoratorMetadata | --- ## 总结 - **严格模式：**始终启用 strict: true - **目标版本：**根据环境选择合适的 target - **模块系统：**根据部署环境选择 module - **类型声明：**库开发时启用 declaration AI 思考中... ** [TypeScript tsconfig.json 配置](https://www.runoob.com/ts-tsconfig.html) [TypeScript 枚举（Enum）](https://www.runoob.com/ts-enum.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
**

[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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