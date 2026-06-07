# TypeScript + React 实战

- Source: https://www.runoob.com/typescript/ts-react.html

TypeScript 为 React 开发提供完整的类型支持，提高代码可靠性。


使用 TypeScript 可以让 React 组件、Props、State 等都有完整的类型检查，减少运行时错误。


**
React 教程查看：[https://www.runoob.com/vue3/react-tutorial.html](https://www.runoob.com/../react/react-tutorial.html)


---






  React + TypeScript 类型支持



  React 组件

    React.FC<Props>
    interface ButtonProps {
    text: string




  React Hooks

    useState<T>(initial)
    useEffect(() => {}, [])
    useCallback<T>(fn)




  事件处理

    React.FormEvent
    React.ChangeEvent
    React.MouseEvent




  TypeScript 带来的优势



  编译期类型检查



  智能代码补全



  重构更安全





--- ## 为什么需要在 React 中使用 TypeScript React 组件化开发会产生大量的 Props、State、Context 等数据流。


没有类型定义时，很难追踪数据的来源和结构，容易出现运行时错误。


TypeScript 为 React 提供了完整的类型系统：组件 Props 有类型检查、useState 有类型推断、事件处理有类型提示。


> 数据流：**React 中的数据流（Props、State、Context）都需要类型定义，TypeScript 可以确保数据流的类型安全。


---


## 创建项目


使用现代脚手架创建支持 TypeScript 的 React 项目。


## 初始化


```javascript
# 使用 Create React App（较慢但完整）
npx create-react-app my-app --template typescript

# 或使用 Vite（推荐，更快）
npm create vite@latest my-app -- --template react-ts
```


**
推荐：**Vite 是目前最推荐的 React 构建工具，速度快，开发体验好。


---


## 组件类型


使用 React.FC 类型定义函数组件。


## src/components/Button.tsx


```javascript
import React from "react";

// 定义按钮组件的 Props 类型
interface ButtonProps {
    text: string;                    // 按钮文字（必填）
    onClick: () => void;             // 点击回调（必填）
    disabled?: boolean;              // 是否禁用（可选，默认 false）
    variant?: "primary" | "secondary"; // 按钮变体（可选）
}

// 使用 React.FC 定义函数组件类型
const Button: React.FC<ButtonProps> = ({
    text,
    onClick,
    disabled = false,
    variant = "primary"
}) => {
    return (
        <button
            className={`btn btn-${variant}`}
            onClick={onClick}
            disabled={disabled}
        >
            {text}
        </button>
    );
};

export default Button;
```


**运行结果：**


```
Button 组件渲染成功
```


**
React.FC：**这是 React 函数组件的类型，包含了 children、propTypes 等内置类型。


---


## Props 类型


定义组件的 Props 接口，传递数据给子组件。


## src/components/UserCard.tsx


```javascript
import React from "react";

// 定义用户类型
interface User {
    id: number;           // 用户 ID
    name: string;        // 用户名
    email: string;       // 邮箱
    avatar?: string;     // 头像（可选）
}

// 定义用户卡片组件的 Props
interface UserCardProps {
    user: User;                       // 用户对象（必填）
    onEdit: (user: User) => void;    // 编辑回调
    onDelete: (id: number) => void;  // 删除回调
}

const UserCard: React.FC<UserCardProps> = ({ user, onEdit, onDelete }) => {
    return (
        <div className="user-card">
            {user.avatar && <img src={user.avatar} alt={user.name} />}
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <button onClick={() => onEdit(user)}>编辑</button>
            <button onClick={() => onDelete(user.id)}>删除</button>
        </div>
    );
};

export default UserCard;
```


**类型传递：**通过 Props 传递类型，确保整个组件树的数据类型一致。

---


## useState 类型


为 useState 提供类型参数，确保状态类型正确。


## src/components/Counter.tsx


```javascript
import React, { useState } from "react";

const Counter: React.FC = () => {
    // 基础类型：显式指定 number 类型
    const [count, setCount] = useState<number>(0);

    // 对象类型：指定对象类型
    const [user, setUser] = useState<{ name: string; age: number }>({
        name: "Alice",
        age: 25
    });

    return (
        <div>
            <p>计数: {count}</p>
            <button onClick={() => setCount(c => c + 1)}>+1</button>
            <button onClick={() => setCount(c => c - 1)}>-1</button>

            <p>用户: {user.name}, {user.age}</p>
            <button onClick={() => setUser({ ...user, age: user.age + 1 })}>
                年龄+1
            </button>
        </div>
    );
};

export default Counter;
```


**运行结果：**


```
Counter 组件渲染成功
```


**
泛型参数：**useState 中的 T 就是状态的类型，如果提供初始值，TypeScript 可以自动推断。


---


## useEffect 类型


useEffect 同样有完整的类型支持。


## src/components/DataFetcher.tsx


```javascript
import React, { useState, useEffect } from "react";

// 定义用户类型
interface User {
    id: number;
    name: string;
}

const DataFetcher: React.FC = () => {
    // 用户列表状态
    const [users, setUsers] = useState<User[]>([]);
    // 加载状态
    const [loading, setLoading] = useState<boolean>(true);
    // 错误状态
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        // 模拟获取数据
        fetch("/api/users")
            .then(res => res.json())
            .then(data => {
                setUsers(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setLoading(false);
            });
    }, []);  // 空依赖数组：只在组件挂载时执行一次

    if (loading) return <div>加载中...</div>;
    if (error) return <div>错误: {error}</div>;

    return (
        <ul>
            {users.map(user => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    );
};

export default DataFetcher;
```


**
依赖数组：**useEffect 的第二个参数是依赖数组，TypeScript 会检查回调中使用的变量是否都已在数组中声明。


---


## 事件处理


React 事件有专门的类型定义。


## src/components/Form.tsx


```javascript
import React, { useState } from "react";

const Form: React.FC = () => {
    // 字符串类型的状态
    const [name, setName] = useState<string>("");

    // 表单提交事件处理
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();  // 阻止表单默认提交
        console.log("提交:", name);
    };

    // 输入框变化事件处理
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setName(e.target.value);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={name}
                onChange={handleChange}
                placeholder="输入名字"
            />
            <button type="submit">提交</button>
        </form>
    );
};

export default Form;
```


**运行结果：**


```
Form 组件渲染成功
```


**
事件类型：**React 为每种 DOM 事件都提供了类型，如 FormEvent、ChangeEvent、MouseEvent 等。


---


## 注意事项


- **React.FC：**推荐使用，可获得完整的类型支持
- **Props 接口：**为每个组件定义 Props 类型
- **useState 泛型：**复杂类型需要显式指定
- **事件类型：**使用 React 提供的事件类型


**
最佳实践：**将类型定义和组件放在同一文件，或集中管理在 types 目录。


---


## 总结


TypeScript 大幅提升了 React 开发体验。


- **React.FC：**React 函数组件的标准类型
- **Props：**使用 interface 定义组件属性
- **useState：**使用泛型参数指定状态类型
- **useEffect：**完整的类型支持
- **事件：**使用 React 事件类型避免 any


**
建议：**新项目直接使用 TypeScript，可以显著减少运行时错误。









	  AI 思考中...





			** [TypeScript + Vue3 实战](https://www.runoob.com/ts-vue3.html)
			[TypeScript 综合项目实战](https://www.runoob.com/ts-comprehensive-project.html) **













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