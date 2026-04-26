 



# 📦 **项目整体架构**

FlightSystem 采用**分层架构设计**：

```
FlightSystem (航班管理系统)
├── model/       (数据模型层 - 基础组件)
├── dao/         (数据访问接口层)
├── dao_impl/    (数据访问实现层)
├── db/          (数据库管理层)
├── backend/     (业务逻辑层)
├── app/         (主应用程序)
├── ui_client/   (客户端界面)
├── ui_admin/    (管理员界面)
└── test/        (测试程序)
```

---

# 🎯 **Model 层 - 五个基础组件详解**

Model 层是整个系统的**数据模型基础**，定义了系统中的5个核心实体类。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model)

### **1️⃣ City (城市类)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model/City.h)

### **2️⃣ Airport (机场类)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model/Airport.h)

### **3️⃣ Airplane (飞机类)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model/Airplane.h)

### **4️⃣ Flight (航班类)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model/Flight.h)

### **5️⃣ Ticket (机票类)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/model/Ticket.h)

---

## 📊 **Model 层总结**

### **五个基础组件及其关系**

| 组件         | 作用     | 核心属性                                                     | 数据库表   |
| ------------ | -------- | ------------------------------------------------------------ | ---------- |
| **City**     | 城市信息 | id, name, code, country                                      | `city`     |
| **Airport**  | 机场信息 | id, name, code, cityId, terminalCount                        | `airport`  |
| **Airplane** | 飞机型号 | id, model, seatsEconomy, seatsBusiness, seatsFirst           | `airplane` |
| **Flight**   | 航班信息 | id, flightNo, airplaneId, departAirportId, arriveAirportId, departTime, arriveTime, status | `flight`   |
| **Ticket**   | 机票信息 | id, flightId, class, price, totalSeats, remainSeats          | `ticket`   |

### **实体关系图 (ER)**

```
┌─────────┐
│  City   │ 1
│ (城市)   │───────┐
└─────────┘       │
                  │ 1:N
                  │
                  ▼ N
              ┌──────────┐
              │ Airport  │
              │ (机场)    │
              └──────────┘
                  │
                  │ N:1 (出发)
                  ▼
┌──────────┐  ┌─────────┐  ┌─────────┐
│ Airplane │  │ Flight  │  │ Ticket  │
│ (飞机)    │──│ (航班)   │──│ (机票)   │
└──────────┘  └─────────┘  └─────────┘
     1:N           1:N
```

### **详细说明**

#### **1. City (城市)**
- **用途**：存储城市基本信息
- **属性**：
  - `id`: 主键，自增
  - `name`: 城市名称（如"北京"）
  - `code`: 城市代码（如"BJS"）
  - `country`: 国家（如"中国"）
- **关系**：一个城市可以有多个机场

#### **2. Airport (机场)**
- **用途**：存储机场信息
- **属性**：
  - `id`: 主键
  - `name`: 机场名称（如"首都国际机场"）
  - `code`: 机场代码（如"PEK"）
  - `cityId`: 外键，关联城市
  - `terminalCount`: 航站楼数量
- **关系**：
  - 属于一个城市（N:1）
  - 作为航班的出发地或到达地

#### **3. Airplane (飞机)**
- **用途**：存储飞机型号配置
- **属性**：
  - `id`: 主键
  - model: 机型（如"Boeing 737"）
  - `seatsEconomy`: 经济舱座位数
  - `seatsBusiness`: 商务舱座位数
  - `seatsFirst`: 头等舱座位数
- **关系**：一架飞机可以执行多个航班

#### **4. Flight (航班)**
- **用途**：存储航班信息（核心实体）
- **属性**：
  - `id`: 主键
  - `flightNo`: 航班号（如"CA1234"）
  - `airplaneId`: 外键，关联飞机
  - `departAirportId`: 外键，出发机场
  - `arriveAirportId`: 外键，到达机场
  - `departTime`: 起飞时间
  - `arriveTime`: 到达时间
  - `status`: 状态（"normal", "delayed", "cancelled"）
- **关系**：
  - 使用一架飞机（N:1）
  - 从一个机场出发（N:1）
  - 到达一个机场（N:1）
  - 有多个舱位的机票（1:N）

#### **5. Ticket (机票)**
- **用途**：存储机票库存和价格
- **属性**：
  - `id`: 主键
  - `flightId`: 外键，关联航班
  - `class`: 舱位等级（"economy", "business", "first"）
  - `price`: 票价
  - `totalSeats`: 总座位数
  - `remainSeats`: 剩余座位数
- **关系**：
  - 属于一个航班（N:1）
  - **注意**：一个航班通常有3条 Ticket 记录（经济舱、商务舱、头等舱各一条）

---

### **设计特点**

1. **简单 POJO 类**：
   - 只包含数据字段和 getter/setter
   - 无业务逻辑
   - 符合单一职责原则

2. **不可变性支持**：
   - 使用 `const` 修饰 getter 方法
   - 确保数据封装

3. **默认构造函数**：
   - 所有类都提供无参构造（用于查询失败时返回空对象）
   - 提供带参构造（用于从数据库构造对象）

4. **类型安全**：
   - 使用 Qt 类型（`QString`, `QDateTime`）
   - 自动内存管理

---

-  



# db层

好的！现在详细介绍 **DB 层（数据库管理层）**。

## 📂 **DB 层 (Database Management Layer)**

DB 层负责**数据库连接的统一管理**，采用**单例模式**确保全局只有一个数据库连接实例。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/db)

---

## 🎯 **DBManager 类详解**

### **头文件 (dbmanager.h)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/db/DBManager.h)

### **实现文件 (dbmanager.cpp)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/db/dbmanager.cpp)

### **配置文件 (config/db.ini)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/config/db.ini)

---

## 📊 **DBManager 核心设计详解**

### **1. 单例模式 (Meyers' Singleton)**

```cpp
static DBManager& instance() {
    static DBManager instance;  // 局部静态变量，C++11 保证线程安全
    return instance;
}
```

#### **设计原理**

**为什么用单例？**
- ✅ **全局唯一连接**：避免创建多个数据库连接，浪费资源
- ✅ **统一管理**：所有 DAO 共享同一个连接
- ✅ **线程安全**：C++11 标准保证静态局部变量初始化是线程安全的
- ✅ **延迟初始化**：第一次调用时才初始化

#### **使用方式**

```cpp
// 在 DAO 实现类中
CityDaoImpl::CityDaoImpl() {
    m_db = DBManager::instance().db();  // 获取单例的数据库连接
}

// 在业务逻辑中
QSqlDatabase db = DBManager::instance().db();
db.transaction();  // 开启事务
```

#### **防止拷贝和赋值（完整版应有）**

```cpp
// 当前代码缺少这部分，建议补充：
class DBManager {
public:
    // ...
    
    // 禁止拷贝
    DBManager(const DBManager&) = delete;
    DBManager& operator=(const DBManager&) = delete;
    
private:
    DBManager();
};
```

---

### **2. 配置文件解析（QSettings）**

```cpp
QString configPath = QDir::cleanPath(QDir::currentPath() + "/../../../../config/db.ini");
QSettings settings(configPath, QSettings::IniFormat);
```

#### **配置文件格式（INI）**

```ini
[database]              # 节 (Section)
host=127.0.0.1         # 键值对 (Key=Value)
port=3306
user=root
password=491122
database=flightsystem
```

#### **读取配置**

```cpp
// 语法：settings.value("节/键", 默认值)
QString host = settings.value("database/host", "127.0.0.1").toString();
int port = settings.value("database/port", 3306).toInt();
QString user = settings.value("database/user", "root").toString();
QString password = settings.value("database/password", "").toString();
QString database = settings.value("database/database", "").toString();
```

**参数说明**：
- **第一个参数**：`"section/key"` 格式的配置路径
- **第二个参数**：默认值（配置文件不存在或键缺失时使用）
- **类型转换**：`.toString()`, `.toInt()`, `.toBool()` 等

#### **路径处理**

```cpp
QString configPath = QDir::cleanPath(QDir::currentPath() + "/../../../../config/db.ini");
```

**路径分析**：
```
当前工作目录：C:\...\FlightSystem\build\Desktop_Qt_6_10_0_MinGW_64_bit-Debug\app\debug
../          → C:\...\FlightSystem\build\Desktop_Qt_6_10_0_MinGW_64_bit-Debug\app
../../       → C:\...\FlightSystem\build\Desktop_Qt_6_10_0_MinGW_64_bit-Debug
../../../    → C:\...\FlightSystem\build
../../../../ → C:\...\FlightSystem
最终路径：    → C:\...\FlightSystem\config\db.ini
```

**QDir::cleanPath()** 作用：
- 规范化路径（将 `../` 解析为实际路径）
- 移除多余的分隔符
- 统一使用 `/`（跨平台兼容）

---

### **3. 数据库连接建立**

```cpp
m_db = QSqlDatabase::addDatabase("QMYSQL");  // 添加 MySQL 驱动
m_db.setHostName(host);                      // 设置主机
m_db.setPort(port);                          // 设置端口
m_db.setUserName(user);                      // 设置用户名
m_db.setPassword(password);                  // 设置密码
m_db.setDatabaseName(database);              // 设置数据库名

if (!m_db.open()) {                          // 尝试连接
    qDebug() << "数据库连接失败:" << m_db.lastError().text();
} else {
    qDebug() << "数据库连接成功";
}
```

#### **QSqlDatabase::addDatabase() 参数**

| 驱动名称   | 数据库类型 | 说明             |
| ---------- | ---------- | ---------------- |
| `QMYSQL`   | MySQL      | 你正在使用的     |
| `QMARIADB` | MariaDB    | 兼容 MySQL       |
| `QSQLITE`  | SQLite     | 轻量级本地数据库 |
| `QPSQL`    | PostgreSQL | 开源关系型数据库 |
| `QODBC`    | ODBC       | 通用数据库接口   |
| `QOCI`     | Oracle     | 商业数据库       |

#### **连接参数配置**

```cpp
m_db.setHostName(host);        // 127.0.0.1 (本地) 或 IP 地址
m_db.setPort(port);            // 3306 (MySQL 默认端口)
m_db.setUserName(user);        // root (管理员账户)
m_db.setPassword(password);    // 491122 (你的密码)
m_db.setDatabaseName(database);// flightsystem (数据库名)
```

#### **连接测试**

```cpp
if (!m_db.open()) {
    // 连接失败，可能原因：
    // 1. MySQL 服务未启动
    // 2. 用户名/密码错误
    // 3. 数据库不存在
    // 4. 驱动未安装（qsqlmysql.dll 和 libmysql.dll）
    qDebug() << "数据库连接失败:" << m_db.lastError().text();
} else {
    qDebug() << "数据库连接成功";
}
```

---

### **4. 公共接口方法**

#### **获取数据库连接**

```cpp
QSqlDatabase& db() { 
    return m_db;  // 返回引用，避免拷贝
}
```

**使用场景**：
```cpp
// DAO 实现类中
QSqlQuery query(DBManager::instance().db());

// 事务处理
QSqlDatabase db = DBManager::instance().db();
db.transaction();
// ... 执行多个操作 ...
db.commit();
```

#### **关闭数据库连接**

```cpp
void close() {
    if (m_db.isOpen())
        m_db.close();
}
```

**使用场景**：
```cpp
// 程序退出时
DBManager::instance().close();
```

---

## 🏗️ **DBManager 架构图**

### **初始化流程**

```
程序启动
    ↓
第一次调用 DBManager::instance()
    ↓
触发 DBManager 构造函数
    ↓
读取 config/db.ini 配置
    ↓
创建 QSqlDatabase 对象
    ↓
设置连接参数（host, port, user, password, database）
    ↓
调用 m_db.open() 建立连接
    ↓
连接成功 → "数据库连接成功"
连接失败 → "数据库连接失败: 错误信息"
    ↓
返回 DBManager 单例引用
    ↓
所有 DAO 共享此连接
```

### **调用链路**

```
┌─────────────────┐
│   应用程序       │
│   (main.cpp)    │
└────────┬────────┘
         │
         │ 1. 启动时自动初始化
         ▼
┌─────────────────────────┐
│   DBManager (单例)       │
│   - 读取 db.ini         │
│   - 建立 MySQL 连接      │
└────────┬────────────────┘
         │
         │ 2. 获取连接 instance().db()
         ▼
┌─────────────────────────┐
│   DAO 实现层             │
│   - CityDaoImpl         │
│   - AirportDaoImpl      │
│   - ...                 │
└────────┬────────────────┘
         │
         │ 3. 使用连接执行 SQL
         ▼
┌─────────────────────────┐
│   MySQL 数据库           │
│   - flightsystem        │
└─────────────────────────┘
```

---

## 🔍 **DB 层设计模式应用**

### **1. 单例模式 (Singleton)**
- **目的**：确保全局唯一数据库连接
- **实现**：Meyers' Singleton（局部静态变量）
- **优点**：线程安全、延迟初始化、自动销毁

### **2. 资源管理模式 (RAII)**
```cpp
class DBManager {
public:
    ~DBManager() {
        close();  // 析构时自动关闭连接
    }
};
```

### **3. 外观模式 (Facade)**
- 隐藏 Qt SQL 的复杂性
- 提供简单的 `instance().db()` 接口

---

## ⚙️ **配置文件设计优势**

### **为什么使用配置文件？**

✅ **分离配置与代码**：
```cpp
// ❌ 硬编码（不推荐）
m_db.setHostName("127.0.0.1");
m_db.setPassword("491122");

// ✅ 配置文件（推荐）
QString host = settings.value("database/host").toString();
m_db.setHostName(host);
```

✅ **环境切换方便**：
```ini
# 开发环境
[database]
host=127.0.0.1
database=flightsystem_dev

# 生产环境（修改配置文件即可）
[database]
host=192.168.1.100
database=flightsystem_prod
```

✅ **安全性**：
- 配置文件不会被编译到程序中
- 可以添加到 .gitignore，避免密码泄露

✅ **灵活性**：
- 不需要重新编译就能修改配置
- 支持默认值

---

## 🛠️ **改进建议（可选）**

### **1. 连接池（高级特性）**

```cpp
class DBManager {
private:
    QList<QSqlDatabase> m_pool;  // 连接池
    int m_maxConnections = 10;
    
public:
    QSqlDatabase getConnection() {
        // 从池中获取空闲连接
    }
    
    void releaseConnection(QSqlDatabase db) {
        // 归还连接到池
    }
};
```

### **2. 自动重连机制**

```cpp
bool DBManager::ensureConnected() {
    if (!m_db.isOpen()) {
        qDebug() << "连接已断开，尝试重连...";
        return m_db.open();
    }
    return true;
}
```

### **3. 日志记录**

```cpp
void DBManager::log(const QString& message) {
    QFile logFile("db_log.txt");
    if (logFile.open(QIODevice::Append)) {
        QTextStream out(&logFile);
        out << QDateTime::currentDateTime().toString("yyyy-MM-dd HH:mm:ss") 
            << " - " << message << "\n";
    }
}
```

### **4. 加密配置文件（安全性）**

```cpp
// 使用 Qt 的加密类
QByteArray encryptedPassword = settings.value("database/password").toByteArray();
QString password = decrypt(encryptedPassword);  // 自定义解密函数
```

---

## 📊 **DB 层总结**

| 特性         | 说明                                 |
| ------------ | ------------------------------------ |
| **核心类**   | DBManager（单例）                    |
| **设计模式** | 单例模式、外观模式、RAII             |
| **配置管理** | QSettings 读取 INI 文件              |
| **连接类型** | QMYSQL（MySQL 驱动）                 |
| **连接参数** | host, port, user, password, database |
| **生命周期** | 程序启动时初始化，退出时自动销毁     |
| **线程安全** | C++11 静态局部变量保证初始化线程安全 |
| **错误处理** | qDebug 输出错误信息                  |
| **代码量**   | 约 50 行                             |

---

## 🎯 **DB 层在整个架构中的作用**

```
应用程序启动
    ↓
【DB 层】DBManager 初始化
    ↓
读取 config/db.ini
    ↓
建立 MySQL 连接
    ↓
DAO_IMPL 层通过 DBManager::instance().db() 获取连接
    ↓
执行 SQL 操作
    ↓
应用程序退出，自动关闭连接
```

---

## 💡 **关键要点**

1. **单例模式**确保全局唯一数据库连接
2. **配置文件**实现配置与代码分离
3. **延迟初始化**第一次调用时才建立连接
4. **线程安全**C++11 保证静态局部变量初始化安全
5. **统一管理**所有 DAO 共享一个连接实例

---

**DB 层介绍完毕！接下来你想了解：**
- **Backend 层**（业务逻辑层，最复杂最重要）
- **完整的数据流程**（从 UI 到数据库的完整调用链）
- **App 层**（主程序入口）
- 还是其他？





好的！现在详细介绍 **DAO 层（数据访问接口层）**。

# 📂 **DAO 层 (Data Access Object Layer)**

DAO 层定义了数据访问的**统一接口规范**，采用**面向接口编程**的设计模式。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao)

---

## 🎯 **DAO 层架构设计**

### **设计理念**

```
┌─────────────────────────────────┐
│      业务逻辑层 (Backend)        │
└────────────┬────────────────────┘
             │ 依赖抽象接口
             ▼
┌─────────────────────────────────┐
│       DAO 接口层 (抽象)          │  ← 我们现在在这里
│  • CityDao                      │
│  • AirportDao                   │
│  • AirplaneDao                  │
│  • FlightDao                    │
│  • TicketDao                    │
└────────────┬────────────────────┘
             │ 实现
             ▼
┌─────────────────────────────────┐
│    DAO 实现层 (具体实现)         │
│  • CityDaoImpl                  │
│  • AirportDaoImpl               │
│  • ...                          │
└─────────────────────────────────┘
```

**核心思想**：
- **依赖倒置原则**：高层模块（Backend）依赖抽象（DAO接口），不依赖具体实现
- **开闭原则**：对扩展开放，对修改关闭（可以随时切换实现，如从 MySQL 切换到 PostgreSQL）
- **接口隔离**：每个 DAO 只定义该实体需要的操作

---

## 📋 **五个 DAO 接口详解**

### **1️⃣ CityDao - 城市数据访问接口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao/CityDao.h)

### **2️⃣ AirportDao - 机场数据访问接口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao/AirportDao.h)

### **3️⃣ AirplaneDao - 飞机数据访问接口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao/AirplaneDao.h)

### **4️⃣ FlightDao - 航班数据访问接口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao/FlightDao.h)

### **5️⃣ TicketDao - 机票数据访问接口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao/TicketDao.h)

---

## 📊 **DAO 接口层总结**

### **统一的 CRUD 操作接口**

所有 DAO 接口都遵循**相同的方法命名规范**，这是标准的 DAO 模式：

| 方法        | 返回类型        | 参数            | 功能                    | 说明                    |
| ----------- | --------------- | --------------- | ----------------------- | ----------------------- |
| `insert()`  | `int`           | `const Entity&` | **创建** - 插入新记录   | 返回自增ID，失败返回 -1 |
| `update()`  | `bool`          | `const Entity&` | **更新** - 修改已有记录 | 成功返回 true           |
| `remove()`  | `bool`          | `int id`        | **删除** - 删除指定记录 | 成功返回 true           |
| `getById()` | `Entity`        | `int id`        | **查询** - 根据主键查询 | 查询失败返回空对象      |
| `getAll()`  | `QList<Entity>` | 无              | **查询** - 查询所有记录 | 返回列表，可能为空      |

---

### **接口设计要点**

#### **1. 纯虚函数 (Pure Virtual Functions)**

```cpp
virtual int insert(const City& city) = 0;  // = 0 表示纯虚函数
```

- **作用**：强制子类必须实现这些方法
- **好处**：确保所有实现类提供完整的数据访问功能

#### **2. 虚析构函数**

```cpp
virtual ~CityDao() = default;
```

- **作用**：确保通过基类指针删除派生类对象时，能正确调用派生类析构函数
- **关键**：避免内存泄漏

#### **3. const 引用传参**

```cpp
virtual int insert(const City& city) = 0;
```

- **优点**：
  - 避免拷贝（性能优化）
  - `const` 保证不会修改传入的对象
  - 引用传递，效率高

#### **4. insert() 返回 int 而非 bool**

```cpp
virtual int insert(const City& city) = 0;  // 返回自增ID
```

**为什么？**
- 插入后需要获取数据库自动生成的 ID
- 返回值：
  - 成功：返回新记录的 ID（如 `1`, `2`, `3`...）
  - 失败：返回 `-1`

**使用场景**：
```cpp
// 先插入航班，获取航班ID
int flightId = flightDao->insert(flight);

// 然后用航班ID插入机票
Ticket ticket(0, flightId, "economy", 500.0, 100, 100);
ticketDao->insert(ticket);
```

#### **5. 查询失败返回空对象**

```cpp
virtual City getById(int id) = 0;  // 失败返回 City()
```

**判断方式**：
```cpp
City city = cityDao->getById(999);
if (city.id() == 0) {  // ID 为 0 表示无效对象
    qDebug() << "城市不存在";
}
```

---

### **接口职责划分**

| DAO 接口        | 管理的数据 | 典型使用场景                            |
| --------------- | ---------- | --------------------------------------- |
| **CityDao**     | 城市信息   | 查询城市列表、根据城市代码查找城市      |
| **AirportDao**  | 机场信息   | 根据城市ID查询该城市的所有机场          |
| **AirplaneDao** | 飞机型号   | 查询可用飞机、获取座位配置              |
| **FlightDao**   | 航班信息   | 查询航班、根据时间/路线搜索航班         |
| **TicketDao**   | 机票库存   | 查询剩余座位、更新余票数量（订票/退票） |

---

### **设计模式应用**

#### **1. 策略模式 (Strategy Pattern)**

```cpp
// Backend 不关心具体实现，只使用接口
class Backend {
private:
    CityDao* cityDao;  // 指向接口，可以是任何实现
};

// 可以轻松切换实现
cityDao = new CityDaoImpl();           // MySQL 实现
// cityDao = new CityDaoPostgresImpl(); // PostgreSQL 实现
// cityDao = new CityDaoRedisImpl();    // Redis 实现
```

#### **2. 工厂模式 (Factory Pattern)**

```cpp
// 可以通过工厂创建 DAO 实例
class DaoFactory {
public:
    static CityDao* createCityDao(DatabaseType type) {
        switch (type) {
            case MySQL: return new CityDaoImpl();
            case PostgreSQL: return new CityDaoPostgresImpl();
            default: return nullptr;
        }
    }
};
```

#### **3. 依赖注入 (Dependency Injection)**

```cpp
// Backend 构造函数可以接受 DAO 接口
Backend::Backend(CityDao* cityDao) {
    this->cityDao = cityDao;  // 注入具体实现
}
```

---

### **接口优势总结**

✅ **解耦**：业务逻辑与数据库实现分离  
✅ **可测试**：可以创建 Mock DAO 进行单元测试  
✅ **可维护**：修改数据库实现不影响业务逻辑  
✅ **可扩展**：轻松添加新的数据源（如缓存层）  
✅ **统一规范**：所有 DAO 遵循相同的接口设计

---

### **当前接口的局限性（可选优化）**

虽然当前接口已经很完善，但如果需要优化，可以考虑：

#### **潜在优化点：**

1. **条件查询方法**
   ```cpp
   // 当前：只能 getAll() 然后循环过滤
   virtual City getByCode(const QString& code) = 0;  // 直接查询
   virtual QList<Airport> getByCityId(int cityId) = 0;  // 直接查询
   ```

2. **分页查询**
   ```cpp
   virtual QList<Flight> getByPage(int page, int pageSize) = 0;
   ```

3. **批量操作**
   ```cpp
   virtual bool insertBatch(const QList<City>& cities) = 0;
   ```

**但你之前撤销了这些优化，说明当前的基础接口已经满足需求！** 👍

---

## 🎯 **DAO 层在整个架构中的位置**

```
用户界面 (UI)
    ↓
业务逻辑 (Backend)
    ↓ 调用接口
【DAO 接口层】 ← 我们刚讲完
    ↓ 实现
DAO 实现层 (Impl)
    ↓
数据库管理 (DBManager)
    ↓
MySQL 数据库
```

---

**DAO 接口层介绍完毕！接下来你想了解：**
- **DAO_IMPL 层**（具体实现，如何用 SQL 操作数据库）
- **DB 层**（数据库连接管理）
- **Backend 层**（业务逻辑层）
- 还是其他？













好的！现在详细介绍 **DAO_IMPL 层（数据访问实现层）**。

# 📂 **DAO_IMPL 层 (Data Access Object Implementation Layer)**

DAO_IMPL 层是 DAO 接口的**具体实现**，使用 **Qt SQL 框架**与 MySQL 数据库交互。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl)

---

## 🎯 **DAO_IMPL 层架构**

### **实现关系图**

```
┌──────────────┐         ┌──────────────────┐
│   CityDao    │ ◄─────  │  CityDaoImpl     │
│  (接口)       │  implements  │  (实现类)      │
└──────────────┘         └──────────────────┘
                                │
                                │ 使用
                                ▼
                         ┌──────────────────┐
                         │   QSqlDatabase   │
                         │   QSqlQuery      │
                         │   (Qt SQL)       │
                         └──────────────────┘
                                │
                                ▼
                         ┌──────────────────┐
                         │  MySQL Database  │
                         └──────────────────┘
```

---

## 📋 **五个 DAO 实现类详解**

### **1️⃣ CityDaoImpl - 城市数据访问实现**

#### **头文件 (city_dao_impl.h)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/city_dao_impl.h)

#### **实现文件 (city_dao_impl.cpp)** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/city_dao_impl.cpp)

---

### **2️⃣ AirportDaoImpl - 机场数据访问实现** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/airport_dao_impl.h)

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/airport_dao_impl.cpp#1-1)，行 1 到 51

---

### **3️⃣ FlightDaoImpl - 航班数据访问实现** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/flight_dao_impl.h)

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/flight_dao_impl.cpp#1-1)，行 1 到 61

---

### **4️⃣ TicketDaoImpl - 机票数据访问实现** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/dao_impl/ticket_dao_impl.cpp#1-1)，行 1 到 46

---

## 📊 **DAO_IMPL 层核心技术详解**

### **1. Qt SQL 核心类**

#### **QSqlDatabase - 数据库连接**
```cpp
QSqlDatabase m_db;  // 成员变量，存储数据库连接

CityDaoImpl::CityDaoImpl() {
    m_db = DBManager::instance().db();  // 从单例获取连接
}
```

**作用**：
- 管理数据库连接
- 每个 DaoImpl 持有一个连接引用
- 通过 DBManager 单例统一管理

#### **QSqlQuery - SQL 查询执行器**
```cpp
QSqlQuery query(m_db);  // 创建查询对象，关联数据库连接
```

**核心方法**：
| 方法             | 作用                      | 示例                                               |
| ---------------- | ------------------------- | -------------------------------------------------- |
| `prepare()`      | 准备 SQL 语句（预编译）   | `query.prepare("SELECT * FROM city WHERE id=:id")` |
| `bindValue()`    | 绑定参数（防止 SQL 注入） | `query.bindValue(":id", 123)`                      |
| `exec()`         | 执行 SQL                  | `query.exec()`                                     |
| `next()`         | 移动到下一条记录          | `while (query.next())`                             |
| `value()`        | 获取字段值                | `query.value("name").toString()`                   |
| `lastInsertId()` | 获取自增ID                | `query.lastInsertId().toInt()`                     |
| `lastError()`    | 获取错误信息              | `query.lastError().text()`                         |

---

### **2. SQL 预编译与参数绑定（防止 SQL 注入）**

#### **❌ 不安全的拼接方式**
```cpp
// 危险！容易被 SQL 注入攻击
QString sql = "SELECT * FROM city WHERE code='" + code + "'";
```

**攻击示例**：
```cpp
code = "BJS' OR '1'='1";  // 恶意输入
// 最终 SQL: SELECT * FROM city WHERE code='BJS' OR '1'='1'
// 返回所有城市！
```

#### **✅ 安全的参数绑定**
```cpp
QSqlQuery query(m_db);
query.prepare("SELECT * FROM city WHERE code=:code");  // 占位符
query.bindValue(":code", code);  // 自动转义，安全
query.exec();
```

**优点**：
- ✅ **防止 SQL 注入**：参数会被自动转义
- ✅ **性能优化**：预编译语句可被数据库缓存
- ✅ **类型安全**：自动处理类型转换

---

### **3. INSERT 操作详解**

```cpp
int CityDaoImpl::insert(const City& city) {
    QSqlQuery query(m_db);
    
    // 1. 准备 SQL（不包含 id，因为是自增字段）
    query.prepare("INSERT INTO city(name, code, country) VALUES(:name, :code, :country)");
    
    // 2. 绑定参数
    query.bindValue(":name", city.name());
    query.bindValue(":code", city.code());
    query.bindValue(":country", city.country());
    
    // 3. 执行
    if (!query.exec()) {
        qDebug() << "Insert city failed:" << query.lastError().text();
        return -1;  // 失败返回 -1
    }
    
    // 4. 返回自增ID（重要！）
    return query.lastInsertId().toInt();
}
```

**关键点**：
- **不插入 ID**：数据库自动生成
- **返回自增 ID**：`lastInsertId()` 获取刚插入记录的 ID
- **错误处理**：失败返回 -1，成功返回新 ID

**使用示例**：
```cpp
City city(0, "北京", "BJS", "中国");  // ID 传 0，插入时忽略
int newId = cityDao->insert(city);
if (newId > 0) {
    qDebug() << "插入成功，新ID:" << newId;
}
```

---

### **4. UPDATE 操作详解**

```cpp
bool CityDaoImpl::update(const City& city) {
    QSqlQuery query(m_db);
    
    // 1. 准备 UPDATE 语句（包含 WHERE 条件）
    query.prepare("UPDATE city SET name=:name, code=:code, country=:country WHERE id=:id");
    
    // 2. 绑定所有字段（包括 WHERE 的 id）
    query.bindValue(":name", city.name());
    query.bindValue(":code", city.code());
    query.bindValue(":country", city.country());
    query.bindValue(":id", city.id());  // WHERE 条件
    
    // 3. 执行并返回结果
    if (!query.exec()) {
        qDebug() << "Update city failed:" << query.lastError().text();
        return false;
    }
    return true;
}
```

**注意**：
- **必须有 WHERE**：否则会更新所有记录！
- **ID 必须存在**：更新不存在的 ID 不会报错，但 `numRowsAffected()` 为 0

---

### **5. DELETE 操作详解**

```cpp
bool CityDaoImpl::remove(int id) {
    QSqlQuery query(m_db);
    
    // 1. 准备 DELETE 语句
    query.prepare("DELETE FROM city WHERE id=:id");
    
    // 2. 绑定 ID
    query.bindValue(":id", id);
    
    // 3. 执行
    if (!query.exec()) {
        qDebug() << "Delete city failed:" << query.lastError().text();
        return false;
    }
    return true;
}
```

**注意**：
- **级联删除**：如果有外键约束，可能删除失败
- **软删除**：实际项目中常用状态标记代替真删除

---

### **6. SELECT 单条记录**

```cpp
City CityDaoImpl::getById(int id) {
    QSqlQuery query(m_db);
    
    // 1. 准备查询
    query.prepare("SELECT id, name, code, country FROM city WHERE id=:id");
    query.bindValue(":id", id);
    
    // 2. 执行
    if (!query.exec()) {
        qDebug() << "Query city failed:" << query.lastError().text();
        return City();  // 失败返回空对象
    }
    
    // 3. 移动到第一条记录
    if (query.next()) {
        // 4. 构造对象并返回
        return City(query.value("id").toInt(),
                    query.value("name").toString(),
                    query.value("code").toString(),
                    query.value("country").toString());
    }
    
    return City();  // 未找到，返回空对象
}
```

**关键点**：
- **`query.next()`**：移动游标到下一条记录，首次调用移动到第一条
- **`query.value("字段名")`**：按字段名获取值（推荐）
- **也可用索引**：`query.value(0)` 获取第一个字段
- **类型转换**：`.toInt()`, `.toString()`, `.toDouble()` 等

---

### **7. SELECT 多条记录**

```cpp
QList<City> CityDaoImpl::getAll() {
    QList<City> list;  // 结果列表
    QSqlQuery query(m_db);
    
    // 1. 执行查询（不需要 prepare，没有参数）
    if (!query.exec("SELECT id, name, code, country FROM city")) {
        qDebug() << "Query all cities failed:" << query.lastError().text();
        return list;  // 失败返回空列表
    }
    
    // 2. 循环遍历所有记录
    while (query.next()) {
        list.append(City(query.value("id").toInt(),
                         query.value("name").toString(),
                         query.value("code").toString(),
                         query.value("country").toString()));
    }
    
    return list;
}
```

**流程**：
1. 执行查询
2. `while (query.next())` 遍历所有记录
3. 每次循环构造一个对象添加到列表
4. 返回列表（可能为空）

---

### **8. 处理日期时间字段（Flight 示例）**

```cpp
// INSERT 时
query.bindValue(":depart_time", flight.departTime());  // QDateTime 自动转换
query.bindValue(":arrive_time", flight.arriveTime());

// SELECT 时
Flight(query.value("id").toInt(),
       query.value("flight_no").toString(),
       // ...
       query.value("depart_time").toDateTime(),  // 转换为 QDateTime
       query.value("arrive_time").toDateTime(),
       query.value("status").toString());
```

**Qt SQL 自动类型映射**：
| MySQL 类型 | Qt 类型   | 转换方法        |
| ---------- | --------- | --------------- |
| INT        | int       | `.toInt()`      |
| VARCHAR    | QString   | `.toString()`   |
| DOUBLE     | double    | `.toDouble()`   |
| DATETIME   | QDateTime | `.toDateTime()` |
| DATE       | QDate     | `.toDate()`     |
| TIME       | QTime     | `.toTime()`     |

---

## 🔍 **DAO_IMPL 层设计模式应用**

### **1. 单例模式（数据库连接）**
```cpp
m_db = DBManager::instance().db();  // 从单例获取连接
```

### **2. 工厂模式（对象构造）**
```cpp
// 从数据库记录"工厂"生成对象
return City(query.value("id").toInt(),
            query.value("name").toString(),
            query.value("code").toString(),
            query.value("country").toString());
```

### **3. 模板方法模式**
所有 DaoImpl 都遵循相同的实现模式：
1. 准备 SQL
2. 绑定参数
3. 执行
4. 处理结果

---

## ⚠️ **错误处理策略**

### **当前策略**：
```cpp
if (!query.exec()) {
    qDebug() << "Insert city failed:" << query.lastError().text();
    return -1;  // 或 return false / return City()
}
```

### **改进建议（可选）**：
```cpp
// 1. 使用异常（更符合 C++ 习惯）
if (!query.exec()) {
    throw DatabaseException(query.lastError().text());
}

// 2. 返回 Optional（C++17）
std::optional<City> getById(int id);

// 3. 返回结果对象（携带错误信息）
struct Result<T> {
    bool success;
    T data;
    QString error;
};
```

---

## 📊 **DAO_IMPL 层总结**

| 特性           | 说明                             |
| -------------- | -------------------------------- |
| **核心技术**   | Qt SQL (QSqlQuery, QSqlDatabase) |
| **SQL 类型**   | MySQL                            |
| **安全措施**   | 参数绑定（防 SQL 注入）          |
| **错误处理**   | qDebug 日志 + 返回值判断         |
| **数据库连接** | 从 DBManager 单例获取            |
| **代码量**     | 每个 Impl 类约 100 行            |
| **职责**       | 纯数据访问，无业务逻辑           |

---

-  











# bachend层

好的！现在我来详细介绍 **Backend 层（业务逻辑层）**，这是整个系统最核心的部分。让我先检查当前的 Backend 实现状态。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/backend)

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/backend/backend.h)

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/backend/backend.cpp#1-1)，行 1 到 51

很好！我发现 Backend 层已经有了完整的接口定义和部分实现。让我查看完整的实现： 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/backend/backend.cpp)

完美！Backend 层已经有完整的实现了。现在让我详细介绍这个核心业务逻辑层的设计和实现。

---

# 📊 **Backend 层 (业务逻辑层) 完整解析**

## 🎯 **Backend 层的架构定位**

```
┌─────────────────────────────────┐
│       UI 层 (界面)               │
│   • 用户操作                     │
│   • 数据展示                     │
└────────────┬────────────────────┘
             │ 调用业务方法
             ▼
┌─────────────────────────────────┐
│   【Backend 层 (业务逻辑)】      │  ← 我们现在在这里
│   • 单例模式管理                 │
│   • 组合多个 DAO 操作            │
│   • 事务控制                     │
│   • 业务规则验证                 │
│   • 数据聚合与转换               │
└────────────┬────────────────────┘
             │ 调用数据访问方法
             ▼
┌─────────────────────────────────┐
│   DAO_IMPL 层 (数据访问)         │
│   • 执行 SQL                     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   MySQL 数据库                   │
└─────────────────────────────────┘
```

---

## 📋 **Backend 类结构详解**

### **1. 核心数据结构**

#### **TicketInfo - 机票信息**

```cpp
struct TicketInfo {
    int ticketId;           // 机票ID
    QString ticketClass;    // 舱位等级 (economy/business/first)
    double price;           // 价格
    int totalSeats;         // 总座位数
    int remainSeats;        // 剩余座位数
    
    bool available() const {  // 便利方法：是否有余票
        return remainSeats > 0;
    }
};
```

**用途**：封装单个舱位的机票信息

#### **FlightDetailInfo - 航班详情（聚合数据）**

```cpp
struct FlightDetailInfo {
    // 航班基本信息
    int flightId;
    QString flightNo;          // 航班号 (如 "CA1234")
    
    // 出发信息（聚合了 City + Airport + Flight 的数据）
    QString departCityName;     // 北京
    QString departAirportName;  // 首都国际机场
    QString departAirportCode;  // PEK
    QDateTime departTime;       // 2025-11-21 08:00:00
    
    // 到达信息
    QString arriveCityName;     // 上海
    QString arriveAirportName;  // 浦东国际机场
    QString arriveAirportCode;  // PVG
    QDateTime arriveTime;       // 2025-11-21 10:30:00
    
    // 飞机信息
    QString airplaneModel;      // Boeing 737
    
    // 状态
    QString status;             // normal/delayed/cancelled
    
    // 机票信息（按舱位分类）
    QMap<QString, TicketInfo> tickets;  // {"economy": {...}, "business": {...}}
};
```

**关键点**：
- **数据聚合**：将 5 个表（flight, airport, city, airplane, ticket）的数据合并
- **业务视图**：UI 可以直接使用，无需再查询多个表
- **QMap 存储票务**：key 是舱位等级，value 是票务详情

---

### **2. 单例模式实现**

```cpp
// ========== 单例模式 ==========
static Backend& instance();

Backend(const Backend&) = delete;              // 禁止拷贝
Backend& operator=(const Backend&) = delete;   // 禁止赋值
```

#### **实现代码**

```cpp
Backend& Backend::instance() {
    static Backend instance;  // Meyers' Singleton
    return instance;
}

Backend::Backend() {
    qDebug() << "Backend 初始化...";
    
    // 初始化所有 DAO（依赖注入）
    cityDao = new CityDaoImpl();
    airportDao = new AirportDaoImpl();
    airplaneDao = new AirplaneDaoImpl();
    flightDao = new FlightDaoImpl();
    ticketDao = new TicketDaoImpl();
    
    qDebug() << "Backend 初始化完成";
}

Backend::~Backend() {
    // RAII：析构时自动释放资源
    delete cityDao;
    delete airportDao;
    delete airplaneDao;
    delete flightDao;
    delete ticketDao;
}
```

**设计优势**：
- ✅ **全局唯一**：整个应用只有一个 Backend 实例
- ✅ **延迟初始化**：首次调用 `instance()` 时才创建
- ✅ **线程安全**：C++11 保证静态局部变量初始化线程安全
- ✅ **自动清理**：程序退出时自动析构，释放 DAO 资源

---

## 🔍 **Backend 功能模块详解**

### **模块 1: 基础数据查询**

这部分提供简单的 CRUD 包装，直接调用 DAO 方法。

#### **城市管理**

```cpp
QList<City> Backend::getAllCities() {
    return cityDao->getAll();  // 直接转发给 DAO
}

City Backend::getCityById(int id) {
    return cityDao->getById(id);
}

City Backend::getCityByCode(const QString& code) {
    // 当前实现：getAll() + 循环过滤
    QList<City> cities = cityDao->getAll();
    for (const City& city : cities) {
        if (city.code() == code) {
            return city;
        }
    }
    return City();  // 未找到返回空对象
}
```

**优化建议**（之前你撤销了）：
```cpp
// 在 DAO 层添加 getByCode() 方法，直接用 SQL WHERE 查询
City Backend::getCityByCode(const QString& code) {
    return cityDao->getByCode(code);  // 使用优化后的 DAO
}
```

#### **机场管理**

```cpp
QList<Airport> Backend::getAirportsByCity(int cityId) {
    // 过滤出指定城市的所有机场
    QList<Airport> result;
    QList<Airport> allAirports = airportDao->getAll();
    for (const Airport& airport : allAirports) {
        if (airport.cityId() == cityId) {
            result.append(airport);
        }
    }
    return result;
}
```

**使用场景**：
```cpp
// 查询北京的所有机场
City beijing = Backend::instance().getCityByCode("BJS");
QList<Airport> airports = Backend::instance().getAirportsByCity(beijing.id());
// 结果：["首都国际机场 PEK", "大兴国际机场 PKX"]
```

---

### **模块 2: 航班查询（核心业务逻辑）**

这是 Backend 层最复杂的部分，涉及**多表关联查询**和**数据聚合**。

#### **2.1 getFlightDetail() - 航班详情聚合**

```cpp
FlightDetailInfo Backend::getFlightDetail(int flightId) {
    FlightDetailInfo info;
    
    // ===== 步骤1: 查询航班基本信息 =====
    Flight flight = flightDao->getById(flightId);
    if (flight.id() == 0) {
        qDebug() << "航班不存在:" << flightId;
        return info;  // 返回空对象
    }
    
    info.flightId = flight.id();
    info.flightNo = flight.flightNo();
    info.departTime = flight.departTime();
    info.arriveTime = flight.arriveTime();
    info.status = flight.status();
    
    // ===== 步骤2: 查询出发机场和城市（JOIN 的模拟）=====
    Airport departAirport = airportDao->getById(flight.departAirportId());
    if (departAirport.id() != 0) {
        City departCity = cityDao->getById(departAirport.cityId());
        info.departCityName = departCity.name();
        info.departAirportName = departAirport.name();
        info.departAirportCode = departAirport.code();
    }
    
    // ===== 步骤3: 查询到达机场和城市 =====
    Airport arriveAirport = airportDao->getById(flight.arriveAirportId());
    if (arriveAirport.id() != 0) {
        City arriveCity = cityDao->getById(arriveAirport.cityId());
        info.arriveCityName = arriveCity.name();
        info.arriveAirportName = arriveAirport.name();
        info.arriveAirportCode = arriveAirport.code();
    }
    
    // ===== 步骤4: 查询飞机型号 =====
    Airplane airplane = airplaneDao->getById(flight.airplaneId());
    if (airplane.id() != 0) {
        info.airplaneModel = airplane.model();
    }
    
    // ===== 步骤5: 查询所有舱位的机票信息 =====
    QList<Ticket> allTickets = ticketDao->getAll();
    for (const Ticket& ticket : allTickets) {
        if (ticket.flightId() == flightId) {
            TicketInfo tInfo;
            tInfo.ticketId = ticket.id();
            tInfo.ticketClass = ticket.tClass();
            tInfo.price = ticket.price();
            tInfo.totalSeats = ticket.totalSeats();
            tInfo.remainSeats = ticket.remainSeats();
            info.tickets[ticket.tClass()] = tInfo;  // 按舱位分类
        }
    }
    
    return info;
}
```

**相当于 SQL JOIN 查询**：
```sql
SELECT 
    f.id, f.flight_no, f.depart_time, f.arrive_time, f.status,
    dc.name AS depart_city, da.name AS depart_airport, da.code AS depart_code,
    ac.name AS arrive_city, aa.name AS arrive_airport, aa.code AS arrive_code,
    ap.model
FROM flight f
LEFT JOIN airport da ON f.depart_airport_id = da.id
LEFT JOIN city dc ON da.city_id = dc.id
LEFT JOIN airport aa ON f.arrive_airport_id = aa.id
LEFT JOIN city ac ON aa.city_id = ac.id
LEFT JOIN airplane ap ON f.airplane_id = ap.id
WHERE f.id = ?
```

**性能分析**：
- 🐌 **当前**：执行 6 次数据库查询（1 flight + 2 airport + 2 city + 1 airplane + 1 ticket 过滤）
- 🚀 **优化**：使用 SQL JOIN，一次查询完成

---

#### **2.2 searchFlights() - 航班搜索**

```cpp
QList<FlightDetailInfo> Backend::searchFlights(
    const QString& fromCityCode,  // "BJS"
    const QString& toCityCode,     // "SHA"
    const QDate& date              // 2025-11-21
) {
    QList<FlightDetailInfo> result;
    
    // ===== 步骤1: 查询出发和到达城市 =====
    City fromCity = getCityByCode(fromCityCode);
    City toCity = getCityByCode(toCityCode);
    
    if (fromCity.id() == 0 || toCity.id() == 0) {
        qDebug() << "城市代码无效:" << fromCityCode << toCityCode;
        return result;  // 返回空列表
    }
    
    // ===== 步骤2: 查询两个城市的所有机场 =====
    QList<Airport> fromAirports = getAirportsByCity(fromCity.id());
    QList<Airport> toAirports = getAirportsByCity(toCity.id());
    
    // ===== 步骤3: 遍历所有航班，筛选符合条件的 =====
    QList<Flight> allFlights = flightDao->getAll();
    for (const Flight& flight : allFlights) {
        // 检查日期是否匹配
        if (flight.departTime().date() != date) {
            continue;
        }
        
        // 检查是否从 fromCity 的某个机场出发
        bool matchDepart = false;
        for (const Airport& airport : fromAirports) {
            if (flight.departAirportId() == airport.id()) {
                matchDepart = true;
                break;
            }
        }
        
        // 检查是否到达 toCity 的某个机场
        bool matchArrive = false;
        for (const Airport& airport : toAirports) {
            if (flight.arriveAirportId() == airport.id()) {
                matchArrive = true;
                break;
            }
        }
        
        // 两个条件都满足，加入结果
        if (matchDepart && matchArrive) {
            result.append(getFlightDetail(flight.id()));
        }
    }
    
    qDebug() << "查询航班:" << fromCityCode << "->" << toCityCode 
             << "日期:" << date << "结果:" << result.size();
    
    return result;
}
```

**业务逻辑**：
1. 支持**城市级别搜索**（而非机场级别）
   - 北京有 PEK、PKX 两个机场
   - 上海有 PVG、SHA 两个机场
   - 搜索"北京→上海"会匹配所有 4 种组合

2. **日期精确匹配**
   - 只匹配起飞日期，不管时间

**使用示例**：
```cpp
// 搜索 2025-11-21 从北京到上海的所有航班
QList<FlightDetailInfo> flights = Backend::instance().searchFlights(
    "BJS", 
    "SHA", 
    QDate(2025, 11, 21)
);

// 结果可能包含：
// CA1234 PEK → PVG 08:00-10:30
// MU5678 PKX → SHA 09:00-11:30
```

---

### **模块 3: 机票预订（事务处理）**

这是 Backend 层最关键的部分，涉及**并发控制**和**事务管理**。

#### **3.1 bookTicket() - 预订机票**

```cpp
bool Backend::bookTicket(
    int flightId,
    const QString& ticketClass,  // "economy"
    int quantity,                 // 2
    QString& errorMsg             // 输出参数：错误信息
) {
    // ===== 步骤1: 获取数据库连接并开启事务 =====
    QSqlDatabase db = DBManager::instance().db();
    
    if (!db.transaction()) {
        errorMsg = "无法开启事务";
        qDebug() << errorMsg;
        return false;
    }
    
    // ===== 步骤2: 验证航班状态 =====
    Flight flight = flightDao->getById(flightId);
    if (flight.id() == 0) {
        db.rollback();
        errorMsg = "航班不存在";
        qDebug() << errorMsg;
        return false;
    }
    
    if (flight.status() != "normal") {
        db.rollback();
        errorMsg = "航班状态异常: " + flight.status();
        qDebug() << errorMsg;
        return false;
    }
    
    // ===== 步骤3: 查询机票信息 =====
    Ticket ticket;
    QList<Ticket> allTickets = ticketDao->getAll();
    bool found = false;
    for (const Ticket& t : allTickets) {
        if (t.flightId() == flightId && t.tClass() == ticketClass) {
            ticket = t;
            found = true;
            break;
        }
    }
    
    if (!found) {
        db.rollback();
        errorMsg = "该舱位不存在";
        qDebug() << errorMsg;
        return false;
    }
    
    // ===== 步骤4: 检查余票 =====
    if (ticket.remainSeats() < quantity) {
        db.rollback();
        errorMsg = QString("余票不足，仅剩 %1 张").arg(ticket.remainSeats());
        qDebug() << errorMsg;
        return false;
    }
    
    // ===== 步骤5: 更新余票（减少）=====
    ticket.setRemainSeats(ticket.remainSeats() - quantity);
    if (!ticketDao->update(ticket)) {
        db.rollback();
        errorMsg = "更新余票失败";
        qDebug() << errorMsg;
        return false;
    }
    
    // ===== 步骤6: 提交事务 =====
    if (!db.commit()) {
        db.rollback();
        errorMsg = "提交事务失败";
        qDebug() << errorMsg;
        return false;
    }
    
    qDebug() << "预订成功：航班" << flight.flightNo() 
             << "舱位" << ticketClass 
             << "数量" << quantity
             << "剩余" << ticket.remainSeats();
    
    return true;
}
```

**事务处理关键点**：

1. **ACID 原则**：
   - **原子性 (Atomicity)**：要么全部成功，要么全部回滚
   - **一致性 (Consistency)**：数据库从一个一致状态到另一个一致状态
   - **隔离性 (Isolation)**：并发事务互不干扰
   - **持久性 (Durability)**：提交后永久保存

2. **事务边界**：
   ```cpp
   db.transaction();  // 开始
   // ... 多个操作 ...
   db.commit();       // 提交
   // 或
   db.rollback();     // 回滚
   ```

3. **错误处理**：
   - 任何步骤失败都会 `rollback()`
   - 返回 `false` 并设置 `errorMsg`

4. **业务规则验证**：
   - 航班状态必须是 "normal"
   - 余票必须足够

**并发问题**（当前代码的潜在问题）：
```
时刻 T1: 用户A 查询余票 = 1
时刻 T2: 用户B 查询余票 = 1
时刻 T3: 用户A 预订成功，余票 = 0
时刻 T4: 用户B 预订成功，余票 = -1  ❌ 超售！
```

**解决方案**（优化建议）：
```sql
-- 使用悲观锁
SELECT * FROM ticket WHERE id=? FOR UPDATE;

-- 或使用乐观锁
UPDATE ticket SET remain_seats = remain_seats - ? 
WHERE id=? AND remain_seats >= ?;
```

---

#### **3.2 cancelBooking() - 取消预订**

```cpp
bool Backend::cancelBooking(
    int flightId,
    const QString& ticketClass,
    int quantity,
    QString& errorMsg
) {
    QSqlDatabase db = DBManager::instance().db();
    
    if (!db.transaction()) {
        errorMsg = "无法开启事务";
        return false;
    }
    
    // 查询机票
    Ticket ticket;
    QList<Ticket> allTickets = ticketDao->getAll();
    bool found = false;
    for (const Ticket& t : allTickets) {
        if (t.flightId() == flightId && t.tClass() == ticketClass) {
            ticket = t;
            found = true;
            break;
        }
    }
    
    if (!found) {
        db.rollback();
        errorMsg = "该舱位不存在";
        return false;
    }
    
    // 检查是否超出总座位数（防止恶意退票）
    if (ticket.remainSeats() + quantity > ticket.totalSeats()) {
        db.rollback();
        errorMsg = "取消数量超出范围";
        return false;
    }
    
    // 更新余票（增加）
    ticket.setRemainSeats(ticket.remainSeats() + quantity);
    if (!ticketDao->update(ticket)) {
        db.rollback();
        errorMsg = "更新余票失败";
        return false;
    }
    
    if (!db.commit()) {
        db.rollback();
        errorMsg = "提交事务失败";
        return false;
    }
    
    qDebug() << "取消预订成功：数量" << quantity << "剩余" << ticket.remainSeats();
    return true;
}
```

**业务规则**：
- ✅ 退票后余票增加
- ✅ 余票不能超过总座位数（防止恶意操作）

---

### **模块 4: 管理员功能**

这部分提供航班、飞机、城市、机场的管理接口。

#### **4.1 addFlight() - 添加航班（带验证）**

```cpp
int Backend::addFlight(const Flight& flight, QString& errorMsg) {
    // ===== 业务规则验证 =====
    
    // 验证飞机是否存在
    Airplane airplane = airplaneDao->getById(flight.airplaneId());
    if (airplane.id() == 0) {
        errorMsg = "飞机不存在";
        return -1;
    }
    
    // 验证出发和到达机场是否存在
    Airport departAirport = airportDao->getById(flight.departAirportId());
    Airport arriveAirport = airportDao->getById(flight.arriveAirportId());
    if (departAirport.id() == 0 || arriveAirport.id() == 0) {
        errorMsg = "机场不存在";
        return -1;
    }
    
    // ===== 插入航班 =====
    int flightId = flightDao->insert(flight);
    if (flightId <= 0) {
        errorMsg = "插入航班失败";
        return -1;
    }
    
    qDebug() << "添加航班成功，ID:" << flightId;
    return flightId;  // 返回新航班ID
}
```

**业务逻辑**：
- **外键验证**：确保关联的飞机和机场存在
- **返回 ID**：成功返回航班ID，失败返回 -1

**使用场景**：
```cpp
// 创建新航班
Flight newFlight(
    0,              // ID 自动生成
    "CA1234",       // 航班号
    1,              // 飞机ID
    1,              // 出发机场ID (PEK)
    5,              // 到达机场ID (PVG)
    QDateTime::currentDateTime().addDays(7),  // 7天后起飞
    QDateTime::currentDateTime().addDays(7).addSecs(9000),  // 2.5小时后降落
    "normal"        // 状态
);

QString error;
int flightId = Backend::instance().addFlight(newFlight, error);
if (flightId > 0) {
    qDebug() << "航班创建成功，ID:" << flightId;
    
    // 创建机票
    Ticket economyTicket(0, flightId, "economy", 500.0, 150, 150);
    ticketDao->insert(economyTicket);
} else {
    qDebug() << "创建失败:" << error;
}
```

---

## 📊 **Backend 层设计模式总结**

### **1. 单例模式 (Singleton)**
```cpp
static Backend& instance();
```
- **作用**：全局唯一业务逻辑入口
- **优点**：统一管理，避免重复创建

### **2. 外观模式 (Facade)**
```cpp
// UI 层只需调用一个方法
QList<FlightDetailInfo> flights = Backend::instance().searchFlights("BJS", "SHA", date);
```
- **作用**：隐藏复杂的多 DAO 操作
- **优点**：简化客户端调用

### **3. 数据传输对象 (DTO)**
```cpp
struct FlightDetailInfo {
    // 聚合了多个实体的数据
};
```
- **作用**：减少网络/层间传输次数
- **优点**：UI 一次获取所有需要的数据

### **4. 事务脚本模式 (Transaction Script)**
```cpp
bool bookTicket(...) {
    db.transaction();
    // 步骤1、2、3...
    db.commit();
}
```
- **作用**：将业务逻辑组织为事务性操作
- **优点**：保证数据一致性

---

## 🎯 **Backend 层职责边界**

### **✅ Backend 层应该做的**
- 业务规则验证
- 多表数据聚合
- 事务管理
- 错误处理和日志
- 数据转换（Entity → DTO）

### **❌ Backend 层不应该做的**
- SQL 操作（交给 DAO）
- UI 逻辑（交给 View）
- 数据库连接管理（交给 DBManager）

---

## 📈 **性能优化建议**

### **当前问题**
```cpp
// 低效：N+1 查询问题
QList<Ticket> allTickets = ticketDao->getAll();  // 1次查询
for (const Ticket& ticket : allTickets) {
    if (ticket.flightId() == flightId) { ... }   // 内存过滤
}
```

### **优化方案**
```cpp
// 高效：在 DAO 层添加条件查询
QList<Ticket> tickets = ticketDao->getByFlightId(flightId);  // 1次带WHERE的查询
```

---

**Backend 层介绍完毕！这是整个系统的核心，连接了数据层和UI层。**

**你想继续了解：**
- **App 层**（主程序入口和 UI）
- **完整的业务流程**（从用户点击到数据库更新）
- **测试程序**（如何测试 Backend）
- 还是其他？







# app层的实现

好的！现在详细介绍 **App 层（应用程序主入口）**。让我先查看 App 层的文件结构和实现。 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app)

---

# 📱 **App 层 (应用程序层) 完整解析**

## 🎯 **App 层架构定位**

```
┌─────────────────────────────────────┐
│   【App 层 - 应用程序入口】          │  ← 我们现在在这里
│   • main.cpp (程序启动)              │
│   • MainWindow (主窗口界面)          │
│   • UI 事件处理                      │
│   • 调用 Backend 业务逻辑             │
└────────────┬────────────────────────┘
             │ 调用
             ▼
┌─────────────────────────────────────┐
│   Backend 层 (业务逻辑)              │
└─────────────────────────────────────┘
```

---

## 📋 **App 层文件结构** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app/app.pro)

### **app.pro 配置文件解析**

```qmake
QT += core gui widgets sql
```
- **core**: Qt 核心模块（必需）
- **gui**: GUI 基础模块
- **widgets**: 控件模块（窗口、按钮等）
- **sql**: SQL 数据库模块（QSqlDatabase、QSqlQuery）

```qmake
CONFIG += c++17
```
- 使用 C++17 标准

```qmake
TEMPLATE = app
```
- 项目类型：应用程序（生成 .exe）

```qmake
SOURCES += main.cpp mainwindow.cpp
HEADERS += mainwindow.h
FORMS += mainwindow.ui
```
- **SOURCES**: 源文件
- **HEADERS**: 头文件
- **FORMS**: Qt Designer 设计的 UI 文件（XML 格式）

```qmake
LIBS += -L$$PWD/../build/lib -ldb -lbackend -lmodel -lui_admin -lui_client -ldao_impl
```
- **链接依赖库**：
  - `-ldb`: 数据库管理层
  - `-lbackend`: 业务逻辑层
  - `-lmodel`: 数据模型层
  - `-ldao_impl`: DAO 实现层
  - `-lui_admin`: 管理员界面
  - `-lui_client`: 客户端界面

---

## 🚀 **main.cpp - 程序入口** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app/main.cpp)

我看到当前的 main.cpp 是一个简化的**数据库连接测试版本**。让我详细解析这两个版本。

---

## 📊 **main.cpp 详细解析**

### **版本 1: 原始完整版（已注释）**

```cpp
#include "mainwindow.h"
#include <QApplication>
#include <QSqlDatabase>
#include <QDebug>

int main(int argc, char *argv[])
{
    // ===== 步骤1: 创建 Qt 应用程序对象 =====
    QApplication a(argc, argv);
    
    // ===== 步骤2: 创建主窗口 =====
    MainWindow w;
    
    // ===== 步骤3: 输出支持的数据库驱动 =====
    qDebug() << "支持数据库：" << QSqlDatabase::drivers();
    // 输出示例：("QMYSQL", "QSQLITE", "QODBC", ...)
    
    // ===== 步骤4: 显示主窗口 =====
    w.show();
    
    // ===== 步骤5: 进入事件循环 =====
    return a.exec();
}
```

#### **QApplication 对象解析**

```cpp
QApplication a(argc, argv);
```

**作用**：
- 初始化 Qt 应用程序
- 管理应用程序的事件循环
- 处理命令行参数
- 管理全局资源（字体、颜色主题等）

**参数**：
- `argc`: 命令行参数数量
- `argv`: 命令行参数数组

**必要性**：
- ✅ **每个 Qt GUI 程序必须有且只有一个 QApplication 对象**
- ❌ 没有 QApplication，GUI 组件无法工作

#### **事件循环 (Event Loop)**

```cpp
return a.exec();
```

**作用**：
- 启动 Qt 事件循环
- 监听并处理事件（鼠标点击、键盘输入、定时器等）
- 程序一直运行，直到调用 `QApplication::quit()`

**事件循环流程**：
```
开始 → 等待事件 → 接收事件 → 分发事件 → 处理事件 → 返回等待
                     ↑                              ↓
                     └──────────────────────────────┘
```

**退出方式**：
```cpp
QApplication::quit();      // 退出事件循环
// 或
QCoreApplication::exit(0); // 退出并返回状态码
```

---

### **版本 2: 当前测试版（数据库连接测试）**

```cpp
#include <QCoreApplication>  // 核心应用（无 GUI）
#include <QtSql>
#include <QDebug>

int main(int argc, char *argv[])
{
    // ===== 使用 QCoreApplication 而非 QApplication =====
    QCoreApplication a(argc, argv);
    // 区别：QCoreApplication 用于控制台程序，QApplication 用于 GUI 程序

    // ===== 步骤1: 添加 MySQL 数据库驱动 =====
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    
    // ===== 步骤2: 设置连接参数 =====
    db.setHostName("localhost");         // 127.0.0.1 或 IP 地址
    db.setPort(3306);                    // MySQL 默认端口
    db.setDatabaseName("flightsystem");  // 数据库名
    db.setUserName("root");              // 用户名
    db.setPassword("491122");            // 密码

    // ===== 步骤3: 尝试连接数据库 =====
    if (!db.open()) {
        qDebug() << "数据库连接失败:" << db.lastError().text();
        return -1;  // 连接失败，退出程序
    }
    
    qDebug() << "数据库连接成功!";
    
    return 0;  // 直接退出，不进入事件循环
}
```

#### **QCoreApplication vs QApplication**

| 特性     | QCoreApplication     | QApplication    |
| -------- | -------------------- | --------------- |
| **用途** | 控制台程序           | GUI 程序        |
| **包含** | 核心功能（事件循环） | 核心 + GUI 支持 |
| **窗口** | ❌ 不支持             | ✅ 支持          |
| **大小** | 更小                 | 更大            |
| **示例** | 后台服务、命令行工具 | 桌面应用程序    |

#### **当前版本的作用**

这是一个**数据库连接测试程序**：
- ✅ 验证 QMYSQL 驱动是否正常加载
- ✅ 测试数据库连接参数是否正确
- ✅ 快速诊断数据库问题

**运行结果**：
```
数据库连接成功!
```

---

## 🖼️ **MainWindow - 主窗口类**

### **mainwindow.h - 头文件** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app/mainwindow.h)

#### **MainWindow 类解析**

```cpp
class MainWindow : public QMainWindow
{
    Q_OBJECT  // Qt 元对象系统宏（必需，用于信号槽机制）

public:
    MainWindow(QWidget *parent = nullptr);  // 构造函数
    ~MainWindow();                          // 析构函数

private:
    Ui::MainWindow *ui;  // UI 指针（由 Qt Designer 生成）
};
```

**关键元素**：

1. **Q_OBJECT 宏**
   ```cpp
   Q_OBJECT
   ```
   - **作用**：启用 Qt 的信号与槽机制
   - **必需性**：任何使用 signals/slots 的类都必须包含此宏
   - **位置**：类定义的第一行（在 public 前）

2. **继承 QMainWindow**
   ```cpp
   class MainWindow : public QMainWindow
   ```
   - **QMainWindow**：Qt 的主窗口基类
   - **提供**：菜单栏、工具栏、状态栏、中心窗口区域

3. **Ui::MainWindow 指针**
   ```cpp
   Ui::MainWindow *ui;
   ```
   - **来源**：由 `mainwindow.ui` 自动生成（uic 编译器）
   - **作用**：访问 UI 控件（按钮、文本框等）
   - **使用**：`ui->pushButton->setText("点击我");`

---

### **mainwindow.cpp - 实现文件** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app/mainwindow.cpp)

#### **MainWindow 实现解析**

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"  // 自动生成的 UI 头文件
```

**ui_mainwindow.h**：
- 由 Qt 的 uic（User Interface Compiler）自动生成
- 包含 `Ui::MainWindow` 类的定义
- **不要手动修改！**

---

#### **构造函数详解**

```cpp
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)           // 调用基类构造函数
    , ui(new Ui::MainWindow)        // 初始化 UI 对象
{
    ui->setupUi(this);  // 设置 UI（加载控件、布局等）
}
```

**初始化列表**：
```cpp
: QMainWindow(parent)
, ui(new Ui::MainWindow)
```
- **QMainWindow(parent)**：调用父类构造，设置父窗口
- **ui(new Ui::MainWindow)**：在堆上创建 UI 对象

**setupUi(this)**：
```cpp
ui->setupUi(this);
```
- **作用**：
  1. 创建所有 UI 控件（按钮、文本框等）
  2. 设置控件属性（大小、位置、文本等）
  3. 建立布局
  4. 连接信号和槽（如果在 Designer 中设置了）

---

#### **析构函数详解**

```cpp
MainWindow::~MainWindow()
{
    delete ui;  // 释放 UI 对象
}
```

**RAII 原则**：
- UI 对象在构造函数中 `new`
- 在析构函数中 `delete`
- 确保资源正确释放

---

### **mainwindow.ui - 界面设计文件** 

读取 [](file:///c%3A/Users/15056/Desktop/final/FlightSystem/app/mainwindow.ui)

#### **UI 文件解析**

这是一个 **XML 格式的界面描述文件**，由 Qt Designer 生成。

```xml
<widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
    <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>   <!-- 窗口宽度 -->
      <height>600</height> <!-- 窗口高度 -->
    </rect>
  </property>
  
  <property name="windowTitle">
    <string>MainWindow</string>  <!-- 窗口标题 -->
  </property>
  
  <widget class="QWidget" name="centralwidget"/>    <!-- 中心控件区域 -->
  <widget class="QMenuBar" name="menubar">...</widget>   <!-- 菜单栏 -->
  <widget class="QStatusBar" name="statusbar"/>     <!-- 状态栏 -->
</widget>
```

**当前 UI 结构**：
```
┌─────────────────────────────────┐
│ MainWindow (800x600)            │
├─────────────────────────────────┤
│ menubar (菜单栏)                 │
├─────────────────────────────────┤
│                                 │
│  centralwidget (中心区域)        │
│  (当前为空)                      │
│                                 │
├─────────────────────────────────┤
│ statusbar (状态栏)               │
└─────────────────────────────────┘
```

**注意**：当前是一个**空白窗口**，没有添加任何控件。

---

## 🔧 **完整的 App 层工作流程**

### **程序启动流程**

```
1. main() 函数开始
    ↓
2. 创建 QApplication 对象
    ↓
3. 创建 MainWindow 对象
    ├─→ 调用 MainWindow 构造函数
    ├─→ 创建 ui 对象 (new Ui::MainWindow)
    ├─→ 调用 ui->setupUi(this)
    │    ├─→ 解析 mainwindow.ui
    │    ├─→ 创建所有控件
    │    ├─→ 设置布局
    │    └─→ 连接信号槽
    └─→ 构造完成
    ↓
4. 显示主窗口 (w.show())
    ↓
5. 进入事件循环 (a.exec())
    ↓
6. 等待用户事件（点击、输入等）
    ↓
7. 用户关闭窗口
    ↓
8. 事件循环退出
    ↓
9. MainWindow 析构
    └─→ delete ui
    ↓
10. QApplication 析构
    ↓
11. 程序结束
```

---

## 🎨 **如何使用 Qt Designer 设计界面**

### **添加控件示例（假设要添加航班查询界面）**

#### **1. 使用 Qt Designer 打开 mainwindow.ui**

在 Qt Creator 中：
- 双击 mainwindow.ui
- 自动打开 Qt Designer

#### **2. 拖拽控件到中心区域**

假设设计一个简单的查询界面：

```xml
<!-- 修改后的 mainwindow.ui 示例 -->
<widget class="QWidget" name="centralwidget">
  <layout class="QVBoxLayout">
    <!-- 标题 -->
    <widget class="QLabel" name="labelTitle">
      <property name="text">
        <string>航班查询系统</string>
      </property>
      <property name="font">
        <font>
          <pointsize>20</pointsize>
          <weight>75</weight>
          <bold>true</bold>
        </font>
      </property>
    </widget>
    
    <!-- 出发城市 -->
    <widget class="QLineEdit" name="lineEditFrom">
      <property name="placeholderText">
        <string>出发城市代码 (如: BJS)</string>
      </property>
    </widget>
    
    
```