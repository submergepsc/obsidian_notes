# TypeScript 综合项目实战

- Source: https://www.runoob.com/typescript/ts-comprehensive-project.html

本教程通过一个完整的项目案例，综合运用 TypeScript 的各种特性。


从项目搭建到实际开发，完整展示 TypeScript 在实际项目中的应用。


---






  项目实战：任务管理系统



  前端 (React + TS)

    Vite + React 18
    组件 + Hooks
    类型安全的 UI




后端 (Node.js) Express + TS RESTful API 类型定义 数据存储 In-Memory (演示) 项目功能特性 任务 CRUD 操作 类型安全的 API 状态管理 --- ## 为什么需要综合项目实战 学习 TypeScript 语法后，需要通过实际项目来巩固知识。


本教程展示一个完整的任务管理系统，涵盖前端、后端和类型定义。


通过这个项目，可以掌握 TypeScript 在实际开发中的最佳实践。


**
项目目标：**创建任务管理系统，包含任务创建、查询、更新、删除功能。


---


## 项目结构


使用 Monorepo 风格组织项目结构。


## 目录结构


```javascript
task-manager/
├── src/
│   ├── types/                 # 类型定义
│   │   ├── task.ts           # 任务类型
│   │   ├── api.ts            # API 类型
│   │   └── index.ts          # 类型导出
│   │
│   ├── services/             # 服务层
│   │   ├── taskService.ts   # 任务服务
│   │   └── index.ts
│   │
│   ├── components/           # React 组件
│   │   ├── TaskList.tsx     # 任务列表
│   │   ├── TaskItem.tsx     # 任务项
│   │   ├── TaskForm.tsx     # 任务表单
│   │   └── index.ts
│   │
│   ├── hooks/                # 自定义 Hooks
│   │   ├── useTasks.ts      # 任务状态管理
│   │   └── index.ts
│   │
│   ├── App.tsx               # 主应用
│   ├── App.css               # 样式
│   └── main.tsx              # 入口文件
│
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts
```


**
目录划分：**按功能划分目录，类型定义、服务层、组件分离。


---


## 类型定义


首先定义项目的核心类型。


## src/types/task.ts


```javascript
// 任务状态枚举
export type TaskStatus = "pending" | "in-progress" | "completed";

// 任务优先级枚举
export type TaskPriority = "low" | "medium" | "high";

// 任务接口定义
export interface Task {
    id: string;               // 任务ID
    title: string;            // 任务标题
    description?: string;      // 任务描述（可选）
    status: TaskStatus;       // 任务状态
    priority: TaskPriority;   // 任务优先级
    createdAt: string;        // 创建时间
    updatedAt: string;         // 更新时间
    dueDate?: string;         // 截止日期（可选）
    tags?: string[];          // 标签（可选）
}

// 创建任务的输入类型
export interface CreateTaskInput {
    title: string;
    description?: string;
    priority: TaskPriority;
    dueDate?: string;
    tags?: string[];
}

// 更新任务的输入类型
export interface UpdateTaskInput {
    title?: string;
    description?: string;
    status?: TaskStatus;
    priority?: TaskPriority;
    dueDate?: string;
    tags?: string[];
}

// 任务过滤选项
export interface TaskFilter {
    status?: TaskStatus;
    priority?: TaskPriority;
    search?: string;
}
```


**
类型分层：**将输入类型、输出类型、过滤类型分开定义，便于维护。


---


## API 类型定义


定义 API 相关的类型。


src/types/api.ts


```javascript
// 通用 API 响应类型
export interface ApiResponse<T> {
    success: boolean;
    data?: T;
    error?: string;
    message?: string;
}

// 分页元数据
export interface PaginationMeta {
    total: number;
    page: number;
    pageSize: number;
    totalPages: number;
}

// 分页响应类型
export interface PaginatedResponse<T> {
    items: T[];
    meta: PaginationMeta;
}

// 请求错误类型
export interface ApiError {
    code: string;
    message: string;
    details?: Record<string, string>;
}

// HTTP 方法类型
export type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

// 任务相关的 API 端点
export interface TaskEndpoints {
    getAll: "/api/tasks";
    getById: "/api/tasks/:id";
    create: "/api/tasks";
    update: "/api/tasks/:id";
    delete: "/api/tasks/:id";
}
```


**
API 类型：**统一的响应格式和错误处理类型，便于前后端对接。


---


## 任务服务层


实现任务管理的业务逻辑。


## src/services/taskService.ts


```javascript
// 导入类型定义
import {
    Task,
    CreateTaskInput,
    UpdateTaskInput,
    TaskFilter,
    TaskStatus,
    TaskPriority
} from "../types/task";

// 生成唯一ID
function generateId(): string {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// 模拟数据库（内存存储）
let tasks: Task[] = [
    {
        id: "1",
        title: "学习 TypeScript",
        description: "掌握 TypeScript 基础和高级特性",
        status: "completed",
        priority: "high",
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        tags: ["学习", "TypeScript"]
    },
    {
        id: "2",
        title: "开发任务管理系统",
        description: "使用 React + TypeScript 开发",
        status: "in-progress",
        priority: "high",
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        tags: ["项目", "实战"]
    }
];

// 任务服务类
class TaskService {
    // 获取所有任务
    getAll(filter?: TaskFilter): Task[] {
        let result = [...tasks];

        if (filter) {
            if (filter.status) {
                result = result.filter(t => t.status === filter.status);
            }
            if (filter.priority) {
                result = result.filter(t => t.priority === filter.priority);
            }
            if (filter.search) {
                const search = filter.search.toLowerCase();
                result = result.filter(t =>
                    t.title.toLowerCase().includes(search) ||
                    t.description?.toLowerCase().includes(search)
                );
            }
        }

        return result;
    }

    // 根据ID获取任务
    getById(id: string): Task | undefined {
        return tasks.find(t => t.id === id);
    }

    // 创建任务
    create(input: CreateTaskInput): Task {
        const now = new Date().toISOString();
        const task: Task = {
            id: generateId(),
            title: input.title,
            description: input.description,
            status: "pending",
            priority: input.priority,
            createdAt: now,
            updatedAt: now,
            dueDate: input.dueDate,
            tags: input.tags
        };

        tasks.push(task);
        return task;
    }

    // 更新任务
    update(id: string, input: UpdateTaskInput): Task | null {
        const index = tasks.findIndex(t => t.id === id);
        if (index === -1) return null;

        const task = tasks[index];
        const updated: Task = {
            ...task,
            ...input,
            updatedAt: new Date().toISOString()
        };

        tasks[index] = updated;
        return updated;
    }

    // 删除任务
    delete(id: string): boolean {
        const index = tasks.findIndex(t => t.id === id);
        if (index === -1) return false;

        tasks.splice(index, 1);
        return true;
    }

    // 更新任务状态
    updateStatus(id: string, status: TaskStatus): Task | null {
        return this.update(id, { status });
    }
}

// 导出服务实例
export const taskService = new TaskService();
```


**
服务层：**业务逻辑集中在服务层，便于测试和维护。


---


## 自定义 Hook


使用 Hook 管理任务状态。


src/hooks/useTasks.ts


```javascript
// 导入 React Hooks 和类型
import { useState, useEffect, useCallback } from "react";
import {
    Task,
    CreateTaskInput,
    UpdateTaskInput,
    TaskFilter,
    TaskStatus,
    TaskPriority
} from "../types/task";
import { taskService } from "../services/taskService";

// Hook 返回的状态类型
interface UseTasksReturn {
    tasks: Task[];
    loading: boolean;
    error: string | null;
    filter: TaskFilter;
    // 操作方法
    createTask: (input: CreateTaskInput) => Promise<void>;
    updateTask: (id: string, input: UpdateTaskInput) => Promise<void>;
    deleteTask: (id: string) => Promise<void>;
    updateStatus: (id: string, status: TaskStatus) => Promise<void>;
    setFilter: (filter: TaskFilter) => void;
    refresh: () => void;
}

// 初始化默认过滤器
const defaultFilter: TaskFilter = {};

export function useTasks(): UseTasksReturn {
    // 任务列表状态
    const [tasks, setTasks] = useState<Task[]>([]);
    // 加载状态
    const [loading, setLoading] = useState(true);
    // 错误状态
    const [error, setError] = useState<string | null>(null);
    // 过滤条件
    const [filter, setFilter] = useState<TaskFilter>(defaultFilter);

    // 加载任务列表
    const loadTasks = useCallback(() => {
        setLoading(true);
        setError(null);

        try {
            const data = taskService.getAll(filter);
            setTasks(data);
        } catch (err) {
            setError(err instanceof Error ? err.message : "加载失败");
        } finally {
            setLoading(false);
        }
    }, [filter]);

    // 初始加载和过滤器变化时重新加载
    useEffect(() => {
        loadTasks();
    }, [loadTasks]);

    // 创建任务
    const createTask = useCallback(async (input: CreateTaskInput) => {
        try {
            taskService.create(input);
            loadTasks();
        } catch (err) {
            setError(err instanceof Error ? err.message : "创建失败");
        }
    }, [loadTasks]);

    // 更新任务
    const updateTask = useCallback(async (id: string, input: UpdateTaskInput) => {
        try {
            taskService.update(id, input);
            loadTasks();
        } catch (err) {
            setError(err instanceof Error ? err.message : "更新失败");
        }
    }, [loadTasks]);

    // 删除任务
    const deleteTask = useCallback(async (id: string) => {
        try {
            taskService.delete(id);
            loadTasks();
        } catch (err) {
            setError(err instanceof Error ? err.message : "删除失败");
        }
    }, [loadTasks]);

    // 更新任务状态
    const updateStatus = useCallback(async (id: string, status: TaskStatus) => {
        try {
            taskService.updateStatus(id, status);
            loadTasks();
        } catch (err) {
            setError(err instanceof Error ? err.message : "状态更新失败");
        }
    }, [loadTasks]);

    // 刷新任务列表
    const refresh = useCallback(() => {
        loadTasks();
    }, [loadTasks]);

    return {
        tasks,
        loading,
        error,
        filter,
        createTask,
        updateTask,
        deleteTask,
        updateStatus,
        setFilter,
        refresh
    };
}
```


**
自定义 Hook：**将状态管理和业务逻辑封装在 Hook 中，组件更简洁。


---


## React 组件


使用 Hook 创建任务列表组件。


## src/components/TaskList.tsx


```javascript
// 导入 React 和自定义 Hook
import React from "react";
import { useTasks } from "../hooks/useTasks";
import { Task, TaskStatus, TaskPriority } from "../types/task";

// 任务项组件 Props
interface TaskItemProps {
    task: Task;
    onStatusChange: (id: string, status: TaskStatus) => void;
    onDelete: (id: string) => void;
}

// 任务项组件
const TaskItem: React.FC<TaskItemProps> = ({
    task,
    onStatusChange,
    onDelete
}) => {
    // 状态样式映射
    const statusStyles: Record<TaskStatus, string> = {
        "pending": "status-pending",
        "in-progress": "status-progress",
        "completed": "status-completed"
    };

    // 优先级样式映射
    const priorityLabels: Record<TaskPriority, string> = {
        "low": "低",
        "medium": "中",
        "high": "高"
    };

    return (
        <div className={`task-item ${statusStyles[task.status]}`}>
            <div className="task-content">
                <h3 className="task-title">{task.title}</h3>
                {task.description && (
                    <p className="task-description">{task.description}</p>
                )}
                <div className="task-meta">
                    <span className={`priority priority-${task.priority}`}>
                        {priorityLabels[task.priority]}
                    </span>
                    <span className="task-date">
                        {new Date(task.createdAt).toLocaleDateString()}
                    </span>
                </div>
            </div>
            <div className="task-actions">
                <select
                    value={task.status}
                    onChange={(e) => onStatusChange(task.id, e.target.value as TaskStatus)}
                    className="status-select"
                >
                    <option value="pending">待处理</option>
                    <option value="in-progress">进行中</option>
                    <option value="completed">已完成</option>
                </select>
                <button
                    onClick={() => onDelete(task.id)}
                    className="delete-btn"
                >
                    删除
                </button>
            </div>
        </div>
    );
};

// 任务列表组件
export const TaskList: React.FC = () => {
    // 使用自定义 Hook 获取任务状态
    const {
        tasks,
        loading,
        error,
        updateStatus,
        deleteTask
    } = useTasks();

    // 渲染加载状态
    if (loading) {
        return <div className="loading">加载中...</div>;
    }

    // 渲染错误状态
    if (error) {
        return <div className="error">错误: {error}</div>;
    }

    // 渲染空状态
    if (tasks.length === 0) {
        return (
            <div className="empty">
                <p>暂无任务</p>
                <p>点击上方按钮创建新任务</p>
            </div>
        );
    }

    // 渲染任务列表
    return (
        <div className="task-list">
            {tasks.map(task => (
                <TaskItem
                    key={task.id}
                    task={task}
                    onStatusChange={updateStatus}
                    onDelete={deleteTask}
                />
            ))}
        </div>
    );
};

export default TaskList;
```


**
组件拆分：**将 TaskItem 拆分为独立组件，代码更清晰。


---


## 主应用组件


整合所有组件，组成完整的应用。


## src/App.tsx


```javascript
// 导入 React 和类型
import React, { useState } from "react";
import { TaskList } from "./components/TaskList";
import { useTasks } from "./hooks/useTasks";
import { CreateTaskInput, TaskPriority } from "./types/task";
import "./App.css";

// 任务表单组件 Props
interface TaskFormProps {
    onSubmit: (input: CreateTaskInput) => void;
}

// 任务表单组件
const TaskForm: React.FC<TaskFormProps> = ({ onSubmit }) => {
    // 表单状态
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [priority, setPriority] = useState<TaskPriority>("medium");

    // 提交处理
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();

        if (!title.trim()) {
            alert("请输入任务标题");
            return;
        }

        onSubmit({
            title: title.trim(),
            description: description.trim() || undefined,
            priority
        });

        // 重置表单
        setTitle("");
        setDescription("");
        setPriority("medium");
    };

    return (
        <form onSubmit={handleSubmit} className="task-form">
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="输入任务标题"
                className="form-input"
            />
            <input
                type="text"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="输入任务描述（可选）"
                className="form-input"
            />
            <select
                value={priority}
                onChange={(e) => setPriority(e.target.value as TaskPriority)}
                className="form-select"
            >
                <option value="low">低优先级</option>
                <option value="medium">中优先级</option>
                <option value="high">高优先级</option>
            </select>
            <button type="submit" className="submit-btn">
                添加任务
            </button>
        </form>
    );
};

// 主应用组件
const App: React.FC = () => {
    // 使用自定义 Hook
    const { createTask, error } = useTasks();

    // 渲染错误提示
    const renderError = () => {
        if (!error) return null;
        return <div className="app-error">{error}</div>;
    };

    return (
        <div className="app">
            <header className="app-header">
                <h1>TypeScript 任务管理系统</h1>
                <p>综合实战项目</p>
            </header>

            {renderError()}

            <main className="app-main">
                <TaskForm onSubmit={createTask} />
                <TaskList />
            </main>

            <footer className="app-footer">
                <p>Powered by TypeScript + React</p>
            </footer>
        </div>
    );
};

export default App;
```


**
组件组合：**通过组合简单的组件构建复杂的 UI。


---


## 项目配置


项目的 TypeScript 和构建配置。


## tsconfig.json


```javascript
{
    "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": true,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "skipLibCheck": true,

        "moduleResolution": "bundler",
        "allowImportingTsExtensions": true,
        "resolveJsonModule": true,
        "isolatedModules": true,
        "noEmit": true,
        "jsx": "react-jsx",

        "strict": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,
        "noFallthroughCasesInSwitch": true
    },
    "include": ["src"],
    "references": [{ "path": "./tsconfig.node.json" }]
}
```


**
严格模式：**启用 strict 获得最完整的类型检查。


---


## 注意事项


- **类型优先：**先定义类型，再编写实现代码
- **接口 vs 类型：**对象类型用接口，联合类型用类型别名
- **分层架构：**类型、服务、组件分层组织
- **Hook 封装：**业务逻辑封装在 Hook 中


**
最佳实践：**类型定义是 TypeScript 项目的基础，要认真设计。


---


## 总结


通过这个综合项目，我们实践了 TypeScript 的核心概念。


- **类型定义：**Task、CreateTaskInput、TaskFilter 等接口
- **服务层：**TaskService 封装业务逻辑
- **自定义 Hook：**useTasks 管理状态
- **React 组件：**类型安全的组件开发
- **项目配置：**严格的 TypeScript 配置


**
建议：**多参与实际项目，在实践中加深对 TypeScript 的理解。










	  AI 思考中...





			** [TypeScript + React 实战](https://www.runoob.com/ts-react.html)














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