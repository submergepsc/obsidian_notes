# TypeScript 递归类型

- Source: https://www.runoob.com/typescript/ts-recursive-types.html

递归类型是一种引用自身的类型，在处理树结构、嵌套数据时非常有用。


TypeScript 支持递归类型定义，可以表达无限深度的数据结构。


---






  递归类型工作原理



  基础节点

    interface TreeNode {
    value: string
    }




递归引用 递归类型 interface TreeNode { value: string children?: TreeNode[] } 实际结构 root ├── child1 └── child2 递归类型应用场景 树形结构 嵌套对象 深度类型转换 --- ## 为什么需要递归类型 在现实世界中，数据结构往往是嵌套的。


例如，文件系统有文件夹和子文件夹，组织架构有部门和子部门，JSON 数据可以无限嵌套。


递归类型允许我们表达这种无限嵌套的结构，是处理树形数据的基石。


**
概念：**递归类型是指在类型定义中引用自身的类型，可以表达任意深度的嵌套结构。


---


## 树形结构


递归类型最常见的应用是表示树形结构。


## 实例


```javascript
// 定义树节点类型，children 引用自身
interface TreeNode {
    id: number;                    // 节点ID
    name: string;                  // 节点名称
    children?: TreeNode[];         // 子节点数组，递归引用
}

// 创建树形结构
const fileSystem: TreeNode = {
    id: 1,
    name: "根目录",
    children: [
        {
            id: 2,
            name: "文件夹1",
            children: [
                { id: 5, name: "文件A.txt" },
                { id: 6, name: "文件B.txt" }
            ]
        },
        {
            id: 3,
            name: "文件夹2",
            children: [
                { id: 7, name: "文件C.txt" }
            ]
        },
        {
            id: 4,
            name: "文件.txt"
        }
    ]
};

// 遍历树的函数
function traverse(node: TreeNode, depth: number = 0): void {
    const indent = "  ".repeat(depth);
    console.log(indent + "&#x1f4c1; " + node.name);

    if (node.children) {
        for (const child of node.children) {
            traverse(child, depth + 1);
        }
    }
}

traverse(fileSystem);
```


**运行结果：**


```
&#x1f4c1; 根目录
  &#x1f4c1; 文件夹1
    &#x1f4c1; 文件A.txt
    &#x1f4c1; 文件B.txt
  &#x1f4c1; 文件夹2
    &#x1f4c1; 文件C.txt
  &#x1f4c1; 文件.txt
```


**
文件系统：**树形结构是递归类型的经典应用，可以表示目录树、组织结构等。


---


## 嵌套列表


递归类型也可以表示嵌套的列表结构。


## 实例


```javascript
// 定义嵌套列表类型
type NestedList<T> = T | NestedList<T>[];

// 定义任务类型
interface Task {
    id: number;
    title: string;
    completed: boolean;
}

// 创建嵌套任务列表
const tasks: NestedList<Task> = [
    { id: 1, title: "项目A", completed: false },
    [
        { id: 2, title: "子任务1", completed: true },
        { id: 3, title: "子任务2", completed: false }
    ],
    { id: 4, title: "项目B", completed: false }
];

// 计算嵌套列表深度
function getDepth<T>(list: NestedList<T>, depth: number = 0): number {
    if (Array.isArray(list)) {
        let maxDepth = depth + 1;
        for (const item of list) {
            maxDepth = Math.max(maxDepth, getDepth(item, depth + 1));
        }
        return maxDepth;
    }
    return depth;
}

console.log("列表深度: " + getDepth(tasks));
```


**
联合类型：**使用 T | NestedList[] 可以同时处理单个元素和数组。


---


## 深度只读类型


使用递归类型实现深度只读转换。


## 实例


```javascript
// 深度只读类型 - 递归应用
type DeepReadonly<T> = T extends Function
    ? T  // 函数保持原样
    : T extends object
        ? { readonly [P in keyof T]: DeepReadonly<T[P]> }
        : T;

// 用户类型
interface User {
    name: string;
    profile: {
        email: string;
        address: {
            city: string;
            zip: string;
        };
    };
    friends: User[];
}

// 创建深度只读用户
const user: DeepReadonly<User> = {
    name: "Alice",
    profile: {
        email: "[email protected]",
        address: {
            city: "Beijing",
            zip: "100000"
        }
    },
    friends: []
};

// 尝试修改会报错
// user.name = "Bob"; // 错误：name 是只读的
// user.profile.address.city = "Shanghai"; // 错误：深层也是只读的

console.log("用户: " + user.name);
console.log("城市: " + user.profile.address.city);
```


**
递归转换：**DeepReadonly 会递归地将所有嵌套对象属性转换为只读。


---


## 深度可选类型


使用递归类型实现深度可选转换。


## 实例


```javascript
// 深度可选类型 - 递归应用
type DeepPartial<T> = T extends object
    ? { [P in keyof T]?: DeepPartial<T[P]> }
    : T;

// 配置类型
interface AppConfig {
    database: {
        host: string;
        port: number;
        credentials: {
            username: string;
            password: string;
        };
    };
    server: {
        port: number;
        ssl: boolean;
    };
}

// 使用深度可选，可以只提供部分配置
const partialConfig: DeepPartial<AppConfig> = {
    database: {
        host: "localhost"
        // port 和 credentials 可选
    }
    // server 可选
};

console.log("数据库主机: " + partialConfig.database?.host);
```


**
可选嵌套：**DeepPartial 递归地将所有属性变为可选，便于处理部分配置。


---


## 链式数据结构


递归类型可以表示链表等链式数据结构。


## 实例


```javascript
// 链表节点类型
interface ListNode<T> {
    value: T;              // 当前节点的值
    next?: ListNode<T>;    // 下一个节点，递归引用
}

// 创建链表
const linkedList: ListNode<number> = {
    value: 1,
    next: {
        value: 2,
        next: {
            value: 3,
            next: {
                value: 4,
                next: undefined
            }
        }
    }
};

// 遍历链表
function traverseList<T>(node: ListNode<T>): void {
    let current: ListNode<T> | undefined = node;
    const values: T[] = [];

    while (current) {
        values.push(current.value);
        current = current.next;
    }

    console.log("链表值: " + values.join(" -> "));
}

traverseList(linkedList);

// 计算链表长度
function getLength<T>(node: ListNode<T>): number {
    let length = 0;
    let current: ListNode<T> | undefined = node;

    while (current) {
        length++;
        current = current.next;
    }

    return length;
}

console.log("链表长度: " + getLength(linkedList));
```


**
链表：**ListNode 通过 next 引用自身，形成链式结构，是递归类型的经典应用。


---


## 联合类型的递归


使用递归类型处理 JSON 数据的联合类型。


**
JSON 类型：**递归类型可以精确表达 JSON 的所有可能类型。


## 实例


```javascript
// JSON 值的递归类型定义
type JSONValue = string | number | boolean | null | JSONValue[] | { [key: string]: JSONValue };

// 定义配置对象
const config: JSONValue = {
    "name": "my-app",
    "version": "1.0.0",
    "enabled": true,
    "settings": {
        "debug": false,
        "ports": [3000, 8080],
        "metadata": {
            "author": "Alice",
            "tags": ["web", "typescript"]
        }
    }
};

// 获取 JSON 值的函数
function getValue(obj: JSONValue, path: string): JSONValue | undefined {
    const keys = path.split(".");
    let current: JSONValue | undefined = obj;

    for (const key of keys) {
        if (current && typeof current === "object" && !Array.isArray(current)) {
            current = (current as { [key: string]: JSONValue })[key];
        } else {
            return undefined;
        }
    }

    return current;
}

console.log("版本: " + getValue(config, "version"));
console.log("端口: " + getValue(config, "settings.ports"));
console.log("作者: " + getValue(config, "settings.metadata.author"));
```


---


## 注意事项


- **递归基例：**确保递归类型有终止条件，避免无限递归
- **条件类型：**递归通常与条件类型结合使用
- **深度限制：**TypeScript 编译器对递归深度有限制
- **性能考虑：**深度递归可能影响类型检查性能


**
最佳实践：**递归类型是处理树形和嵌套数据的利器，熟练掌握可以解决很多复杂的类型问题。


---


## 总结


递归类型是 TypeScript 类型系统中的高级特性。


- **自引用：**类型定义中引用自身
- **树形结构：**表达无限嵌套的数据
- **深度转换：**实现深度只读、深度可选等工具类型
- **链式结构：**表示链表等线性递归结构


**
建议：**在处理嵌套数据时，优先考虑使用递归类型来保证类型安全。









	  AI 思考中...





			** [TypeScript 索引类型与 keyof 关键字](https://www.runoob.com/ts-indexed-types.html)
			[TypeScript 协变与逆变](https://www.runoob.com/ts-covariance.html) **













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