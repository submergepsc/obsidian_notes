# TypeScript 性能优化

- Source: https://www.runoob.com/typescript/ts-performance.html

TypeScript 项目的性能优化涉及编译速度、运行时性能和代码体积等多个方面。


本教程介绍常见的性能优化技巧，帮助构建更高效的 TypeScript 应用。


---






  TypeScript 性能优化维度



  编译速度
  增量构建 | skipLibCheck



  运行时性能
  类型推断 | 避免 any



  包体积
  Tree Shaking | 懒加载



  关键优化策略



  skipLibCheck
  跳过库类型检查



  incremental
  增量编译



  Project References
  项目引用


---


## 为什么需要性能优化


TypeScript 虽然提供了强大的类型系统，但使用不当会影响编译速度和运行性能。


大型项目的编译可能需要数分钟，严重影响开发体验。


本教程介绍的配置和技巧可以显著提升 TypeScript 项目的性能。


**
优化目标：**更快的编译速度、更小的打包体积、更高的运行时性能。


---


## 编译配置优化


通过优化 tsconfig.json 配置来提升编译速度。


## tsconfig.json 优化配置


```javascript
{
    "compilerOptions": {
        // 启用增量编译，保存上次编译信息
        "incremental": true,

        // 跳过 node_modules 的类型检查
        // 大幅提升编译速度
        "skipLibCheck": true,

        // 跳过声明文件的生成（仅在最终构建时生成）
        "noEmit": true,

        // 启用快速增量构建
        "assumeChangesOnlyAffectDirectDependencies": true,

        // 并行执行
        "parallel": true,

        // 启用缓存
        "tsBuildInfoFile": ".tsbuildinfo",

        // 不需要解析的文件
        "exclude": [
            "node_modules",
            "dist",
            "build",
            "**/*.test.ts"
        ]
    }
}
```


**
skipLibCheck：**这是最重要的优化选项，可以将编译时间减少 50% 以上。


---


## 项目引用优化


使用项目引用将大型项目拆分为小模块，实现增量编译。


## packages/utils/tsconfig.json


```javascript
{
    // 继承基础配置
    "extends": "../../tsconfig.base.json",

    "compilerOptions": {
        "composite": true,
        "outDir": "./dist",
        "declaration": true,
        "declarationMap": true
    },

    "include": ["src/**/*"],
    "exclude": ["node_modules", "dist"]
}
```


**
composite：**启用后，TypeScript 会生成 .tsbuildinfo 文件来加速后续编译。


---


## 类型推断优化


充分利用 TypeScript 的类型推断，避免过度标注。


实例


```javascript
// 不好的写法：过度标注类型
const name: string = "Alice";
const age: number = 25;
const isActive: boolean = true;

// 好的写法：利用类型推断
const name = "Alice";
const age = 25;
const isActive = true;

// 函数返回值类型可以省略（TypeScript 会自动推断）
function add(a: number, b: number) {
    return a + b;
}

// 复杂对象使用类型推断
const user = {
    id: 1,
    name: "Bob",
    email: "[email protected]"
};
// TypeScript 会推断出:
// { id: number; name: string; email: string }

// 只有在类型推断不准确时才需要显式标注
const elements: HTMLElement[] = [];
```


**
减少标注：**TypeScript 的类型推断已经很智能，大部分情况下不需要显式标注类型。


---


## 避免使用 any


使用 any 会失去类型检查的优势，影响运行时性能。


## 实例


```javascript
// 不好的写法：使用 any
function processData(data: any): any {
    return data.value;
}

// 好的写法：使用 unknown 或具体类型
function processData<T extends { value: string }>(data: T): string {
    return data.value;
}

// 如果真的不知道类型，使用 unknown
function parseJSON(json: string): unknown {
    return JSON.parse(json);
}

// 使用时进行类型检查
const data = parseJSON('{"key": "value"}');
if (typeof data === "object" && data !== null) {
    const obj = data as { key: string };
    console.log(obj.key);
}

// 更好的做法：使用泛型
function identity<T>(value: T): T {
    return value;
}

const result = identity("hello");
console.log("结果: " + result);
```


**
unknown vs any：**unknown 是类型安全的 any，使用前需要进行类型检查。


---


## 接口 vs 类型别名


根据场景选择合适的类型定义方式。


## 实例


```javascript
// 接口：适合定义对象类型，支持声明合并
interface User {
    id: number;
    name: string;
}

// 扩展接口
interface User {
    email: string;
}

// 类型别名：适合联合类型、元组、函数类型
type ID = string | number;
type Status = "pending" | "success" | "error";
type Callback = (data: string) => void;

// 工具类型通常使用 type
type PartialUser = Partial<User>;
type ReadonlyUser = Readonly<User>;

// 性能考虑：接口的编译速度通常比类型别名快
// 对于简单的对象类型，可以使用 interface
interface Point {
    x: number;
    y: number;
}

// 对于联合类型，使用 type
type Shape = Circle | Square | Triangle;
```


**
选择建议：**对象类型使用接口，联合类型使用 type，功能类型使用 type。


---


## 构建工具优化


配置构建工具以获得最佳性能。


## vite.config.ts


```javascript
// 导入 vite
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Vite 配置优化
export default defineConfig({
    plugins: [react()],

    // 构建优化
    build: {
        // 启用代码拆分
        rollupOptions: {
            output: {
                // 手动分包
                manualChunks: {
                    'vendor': ['react', 'react-dom'],
                    'utils': ['lodash', 'axios']
                }
            }
        },

        // 压缩代码
        minify: 'terser',

        // 生成 sourcemap
        sourcemap: false,

        // 块大小限制
        chunkSizeWarningLimit: 500
    },

    // 开发服务器优化
    server: {
        // 启用热更新
        hmr: {
            overlay: true
        }
    },

    // 优化依赖解析
    optimizeDeps: {
        include: ['react', 'react-dom'],
        exclude: ['some-large-library']
    }
});
```


**
代码分割：**使用 manualChunks 将大型库分离，减少主包体积。


---


## Tree Shaking


配置模块以支持 Tree Shaking，消除未使用的代码。


## src/utils/index.ts


```javascript
// 使用 ES 模块导出，支持 Tree Shaking
export function add(a: number, b: number): number {
    return a + b;
}

export function subtract(a: number, b: number): number {
    return a - b;
}

export function multiply(a: number, b: number): number {
    return a * b;
}

export function divide(a: number, b: number): number {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

// 具名导出比默认导出更有利于 Tree Shaking
// 错误：export default 会阻止 Tree Shaking
// export default { add, subtract, multiply, divide };

// 正确：使用具名导出
console.log("工具模块加载");
```


**
具名导出：**使用具名导出而不是默认导出，可以让构建工具更好地进行 Tree Shaking。


---


## 注意事项


- **skipLibCheck：**生产环境必须开启
- **增量编译：**开发环境建议开启
- **避免 any：**使用 unknown 代替
- **Tree Shaking：**使用 ES 模块和具名导出


**
最佳实践：**在开发初期就设置好优化配置，避免后期重构。


---


## 总结


TypeScript 性能优化涉及多个方面。


- **编译优化：**skipLibCheck、incremental、project references
- **类型优化：**利用推断、避免 any、选择合适的类型定义
- **构建优化：**代码分割、Tree Shaking、依赖优化
- **运行时优化：**类型安全、泛型约束


**
建议：**定期检查编译时间和包体积，持续优化项目性能。









	  AI 思考中...





			** [TypeScript 设计模式](https://www.runoob.com/ts-design-patterns.html)
			[TypeScript + Node.js 实战](https://www.runoob.com/ts-nodejs.html) **













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