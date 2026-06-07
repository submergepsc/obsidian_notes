# TypeScript tsconfig.json 配置

- Source: https://www.runoob.com/typescript/ts-tsconfig.html

tsconfig.json 是 TypeScript 项目的配置文件，用于指定编译选项和项目设置。


---


## 基本配置


最基础的 tsconfig.json 文件。


## 实例


```javascript
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "commonjs",
        "strict": true,
        "outDir": "./dist"
    },
    "include": ["src/**/*"],
    "exclude": ["node_modules", "dist"]
}
```


配置说明：


- **target：**编译目标 JavaScript 版本
- **module：**使用的模块系统
- **strict：**启用所有严格类型检查
- **outDir：**输出目录


---


## 编译目标版本


使用 target 指定编译到的 JavaScript 版本。


## 实例


```javascript
// tsconfig.json
{
    "compilerOptions": {
        // ES3, ES5, ES6/ES2015, ES2020, ESNext
        "target": "ES2020"
    }
}
```


不同目标的输出差异：


```
// target: ES5 - 使用 var
var greeting = "Hello";

// target: ES2020 - 使用 let/const
let greeting = "Hello";
```


---


## 模块系统


配置模块化方案。


## 实例


```javascript
{
    "compilerOptions": {
        "module": "commonjs",
        // 可选: none, commonjs, amd, umd, es6, es2020, esnext
    }
}
```


---


## 严格模式


strict 选项启用所有严格类型检查。


## 实例


```javascript
{
    "compilerOptions": {
        "strict": true,
        // 等同于开启以下所有选项：
        // "strictNullChecks": true,
        // "noImplicitAny": true,
        // "strictFunctionTypes": true,
        // 等等
    }
}
```


**
建议：**始终启用 strict: true，这是最佳实践。


---


## 路径别名


配置路径别名简化导入。


## 实例


```javascript
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": ["src/*"],
            "@components/*": ["src/components/*"]
        }
    }
}
```


使用方式：


```
import Button from "@components/Button";
import { Header } from "@/components";
```


---


## 文件包含与排除


控制哪些文件包含在编译中。


## 实例


```javascript
{
    "include": ["src/**/*"],
    "exclude": [
        "node_modules",
        "dist",
        "**/*.test.ts",
        "**/*.spec.ts"
    ]
}
```


---


## 常用编译选项一览


| 选项 | 说明 |
| --- | --- |
| target | 编译目标版本 |
| module | 模块系统 |
| strict | 严格模式 |
| outDir | 输出目录 |
| rootDir | 源码根目录 |
| esModuleInterop | 允许 ES 模块互操作 |
| skipLibCheck | 跳过库检查 |
| declaration | 生成 .d.ts 声明文件 |


---


## 总结


- **tsconfig.json：**TypeScript 项目配置文件
- **compilerOptions：**编译选项核心配置
- **include/exclude：**控制文件范围
- **路径别名：**简化导入路径
- **strict: true：**始终启用严格模式








	  AI 思考中...





			** [TypeScript vs JavaScript 对比](https://www.runoob.com/typescript-vs-javascript.html)
			[TypeScript 编译选项](https://www.runoob.com/ts-compiler-options.html) **













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