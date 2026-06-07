# TypeScript + Node.js 实战

- Source: https://www.runoob.com/typescript/ts-nodejs.html

TypeScript 在 Node.js 后端开发中广泛应用，本教程介绍 Node.js 项目的 TypeScript 配置和使用。


使用 TypeScript 可以让 Node.js 代码更安全、更易维护，特别适合中大型后端项目。


**
Node.js 教程查看：[https://www.runoob.com/nodejs/nodejs-tutorial.html](https://www.runoob.com/../nodejs/nodejs-tutorial.html)


---






  Node.js + TypeScript 项目结构



  项目配置

    package.json
    tsconfig.json
    ts-node




  源代码 (src/)

    types/ - 类型定义
    services/ - 业务逻辑
    routes/ - 路由处理




  编译输出 (dist/)

    .js - JavaScript
    .d.ts - 类型声明
    .map - 源码映射




  Node.js
  运行时
  执行 JS



  开发流程



  npm install 安装依赖



  tsc 编译 TypeScript



  node 运行 JavaScript



  API 请求测试





--- ## 为什么需要在 Node.js 中使用 TypeScript Node.js 项目通常涉及复杂的业务逻辑和数据处理，代码行数会快速增长。


使用 TypeScript 可以：提供编译期类型检查，减少运行时错误；利用 IDE 智能提示，提高开发效率；代码更易读和维护。


许多大型 Node.js 项目（如NestJS）都推荐或默认使用 TypeScript。


> 优势：**TypeScript 的静态类型检查可以在开发时发现潜在问题，比运行时调试更高效。


---


## 项目初始化


首先初始化 Node.js 项目并安装 TypeScript 相关依赖。


## 初始化项目


```javascript
# 初始化 npm
npm init -y

# 安装 TypeScript 和 Node.js 类型定义
# -D 表示安装为开发依赖
npm install -D typescript @types/node ts-node nodemon

# 初始化 tsconfig.json
npx tsc --init
```


**
说明：**`@types/node` 提供了 Node.js API 的类型定义，`ts-node` 可以直接运行 TypeScript 文件，`nodemon` 监听文件变化自动重启。


---


## tsconfig.json 配置


配置 TypeScript 编译器选项，针对 Node.js 项目进行优化。


## tsconfig.json


```javascript
{
    "compilerOptions": {
        // 编译目标：ES2020
        "target": "ES2020",

        // 模块系统：CommonJS（Node.js 原生支持）
        "module": "commonjs",

        // 启用的库
        "lib": ["ES2020"],

        // 输出目录
        "outDir": "./dist",

        // 源码根目录
        "rootDir": "./src",

        // 严格模式（始终开启）
        "strict": true,

        // ES 模块互操作
        "esModuleInterop": true,

        // 跳过库检查
        "skipLibCheck": true,

        // 强制文件名大小写一致
        "forceConsistentCasingInFileNames": true,

        // 模块解析策略
        "moduleResolution": "node",

        // 生成声明文件
        "declaration": true
    },
    // 要编译的文件
    "include": ["src/**/*"],
    // 排除的文件
    "exclude": ["node_modules", "dist"]
}
```


**
推荐配置：**Node.js 项目推荐使用 `module: "commonjs"`，这是 Node.js 原生支持的模块系统。


---


## 定义类型


在 types 目录中定义项目的类型接口。


## src/types/index.ts


```javascript
// 用户类型定义
export interface User {
    id: number;         // 用户 ID
    name: string;       // 用户名
    email: string;      // 邮箱
    createdAt: Date;   // 创建时间
}

// 创建用户的数据传输对象
export interface CreateUserDTO {
    name: string;       // 用户名（必填）
    email: string;     // 邮箱（必填）
    password: string;   // 密码（必填）
}

// API 响应类型（泛型）
export interface ApiResponse<T> {
    success: boolean;   // 是否成功
    data?: T;         // 成功时的数据
    error?: string;   // 失败时的错误信息
}
```


**
类型定义：**将类型定义集中放在 types 目录，便于维护和复用。


---


## 实现服务


在 services 目录中实现业务逻辑，使用定义好的类型。


## src/services/userService.ts


```javascript
// 导入类型定义
import { User, CreateUserDTO, ApiResponse } from "../types";

// 用户服务类
class UserService {
    // 用户列表（内存存储）
    private users: User[] = [];
    // 下一个用户 ID
    private nextId = 1;

    // 创建用户
    createUser(dto: CreateUserDTO): ApiResponse<User> {
        try {
            // 创建用户对象
            const user: User = {
                id: this.nextId++,
                name: dto.name,
                email: dto.email,
                createdAt: new Date()
            };
            this.users.push(user);
            return { success: true, data: user };
        } catch (error) {
            return { success: false, error: "创建用户失败" };
        }
    }

    // 获取单个用户
    getUser(id: number): ApiResponse<User> {
        const user = this.users.find(u => u.id === id);
        if (!user) {
            return { success: false, error: "用户不存在" };
        }
        return { success: true, data: user };
    }

    // 获取所有用户
    getAllUsers(): ApiResponse<User[]> {
        return { success: true, data: this.users };
    }
}

// 导出单例
export default new UserService();
```


**运行结果：**


```
UserService 实例化成功
```


**
服务层：**业务逻辑集中在 service 层，便于测试和复用。


---


## 创建 API 路由


使用 Express 框架创建 RESTful API。


## src/index.ts


```javascript
import express, { Request, Response } from "express";
import userService from "./services/userService";

// 创建 Express 应用
const app = express();
// 解析 JSON 请求体
app.use(express.json());

// 获取所有用户
app.get("/api/users", (req: Request, res: Response) => {
    const result = userService.getAllUsers();
    res.json(result);
});

// 获取单个用户
app.get("/api/users/:id", (req: Request, res: Response) => {
    const id = parseInt(req.params.id);
    const result = userService.getUser(id);
    res.json(result);
});

// 创建用户
app.post("/api/users", (req: Request, res: Response) => {
    const result = userService.createUser(req.body);
    res.json(result);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`服务器运行在 http://localhost:${PORT}`);
});
```


**运行结果：**


```
服务器运行在 http://localhost:3000
```


**
类型提示：**使用 `Request` 和 `Response` 类型，IDE 会提供完整的属性提示。


---


## package.json 脚本


配置 npm 脚本，简化开发流程。


## package.json


```javascript
{
    "scripts": {
        // 编译 TypeScript
        "build": "tsc",

        // 运行编译后的 JavaScript
        "start": "node dist/index.js",

        // 开发模式：使用 nodemon 监听变化自动重启
        "dev": "nodemon --exec ts-node src/index.ts",

        // 运行测试
        "test": "jest"
    }
}
```


**
开发效率：**使用 `npm run dev` 可以实现代码修改后自动重启服务器。


---


## 注意事项


- **严格模式：**始终启用 strict: true
- **模块选择：**Node.js 项目使用 commonjs
- **类型定义：**安装 @types/node 获取 API 类型
- **开发工具：**使用 ts-node 实现热重载


**
最佳实践：**保持类型定义和业务逻辑分离，便于测试和维护。


---


## 总结


TypeScript 是 Node.js 后端开发的优秀选择。


- **项目配置：**使用 tsconfig.json 配置编译选项
- **类型定义：**在 types 目录集中管理接口
- **服务层：**业务逻辑与路由分离
- **路由：**使用 Express 创建 RESTful API
- **开发工具：**ts-node、nodemon 提高开发效率


**
建议：**新项目直接使用 TypeScript，老项目可以逐步迁移。








	  AI 思考中...





			** [TypeScript 性能优化](https://www.runoob.com/ts-performance.html)
			[TypeScript + Vue3 实战](https://www.runoob.com/ts-vue3.html) **













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