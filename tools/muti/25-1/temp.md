完美!测试全部通过! 现在我为您整理后端接口文档,方便前端程序员使用:

## 📚 Backend 接口文档 (API Reference)

### 🔧 获取Backend实例
```cpp
Backend& backend = Backend::instance();  // 单例模式
```

---

## 📋 客户端接口 (Client APIs)

### 1️⃣ 基础查询接口

| 接口方法                         | 功能说明             | 返回类型          |
| -------------------------------- | -------------------- | ----------------- |
| `getAllCities()`                 | 获取所有城市         | `QList<City>`     |
| `getCityById(int id)`            | 根据ID查询城市       | `City`            |
| `getCityByCode(QString code)`    | 根据代码查询城市     | `City`            |
| `getAllAirports()`               | 获取所有机场         | `QList<Airport>`  |
| `getAirportById(int id)`         | 根据ID查询机场       | `Airport`         |
| `getAirportByCode(QString code)` | 根据代码查询机场     | `Airport`         |
| `getAirportsByCity(int cityId)`  | 查询某城市的所有机场 | `QList<Airport>`  |
| `getAllAirplanes()`              | 获取所有飞机         | `QList<Airplane>` |
| `getAirplaneById(int id)`        | 根据ID查询飞机       | `Airplane`        |

### 2️⃣ 航班查询接口

| 接口方法                                                     | 功能说明                       | 返回类型                  |
| ------------------------------------------------------------ | ------------------------------ | ------------------------- |
| `searchFlights(QString fromCityCode, QString toCityCode, QDate date)` | **搜索航班**(按城市代码和日期) | `QList<FlightDetailInfo>` |
| `getAllFlights()`                                            | 获取所有航班详情               | `QList<FlightDetailInfo>` |
| `getFlightDetail(int flightId)`                              | 获取单个航班详情               | `FlightDetailInfo`        |

### 3️⃣ 机票预订接口

| 接口方法                                                     | 功能说明     | 返回类型 |
| ------------------------------------------------------------ | ------------ | -------- |
| `checkTicketAvailability(int flightId, QString ticketClass, int quantity)` | **检查余票** | `bool`   |
| `bookTicket(int flightId, QString ticketClass, int quantity, QString& errorMsg)` | **预订机票** | `bool`   |
| `cancelBooking(int flightId, QString ticketClass, int quantity, QString& errorMsg)` | **取消预订** | `bool`   |

---

## 🔐 管理员接口 (Admin APIs)

### 4️⃣ 航班管理接口

| 接口方法                                           | 功能说明         | 返回类型       |
| -------------------------------------------------- | ---------------- | -------------- |
| `addFlight(Flight& flight, QString& errorMsg)`     | 添加新航班       | `int` (航班ID) |
| `updateFlight(Flight& flight, QString& errorMsg)`  | 更新航班信息     | `bool`         |
| `updateFlightStatus(int flightId, QString status)` | **更新航班状态** | `bool`         |
| `deleteFlight(int flightId, QString& errorMsg)`    | 删除航班         | `bool`         |

### 5️⃣ 飞机管理接口

| 接口方法                             | 功能说明     | 返回类型       |
| ------------------------------------ | ------------ | -------------- |
| `addAirplane(Airplane& airplane)`    | 添加飞机     | `int` (飞机ID) |
| `updateAirplane(Airplane& airplane)` | 更新飞机信息 | `bool`         |
| `deleteAirplane(int airplaneId)`     | 删除飞机     | `bool`         |

### 6️⃣ 城市/机场管理接口

| 接口方法                       | 功能说明 | 返回类型       |
| ------------------------------ | -------- | -------------- |
| `addCity(City& city)`          | 添加城市 | `int` (城市ID) |
| `addAirport(Airport& airport)` | 添加机场 | `int` (机场ID) |

---

## 📦 数据结构

### `FlightDetailInfo` (航班详细信息)
```cpp
struct FlightDetailInfo {
    int flightId;                    // 航班ID
    QString flightNo;                // 航班号
    QString departCityName;          // 出发城市
    QString departAirportName;       // 出发机场
    QString departAirportCode;       // 出发机场代码
    QDateTime departTime;            // 出发时间
    QString arriveCityName;          // 到达城市
    QString arriveAirportName;       // 到达机场
    QString arriveAirportCode;       // 到达机场代码
    QDateTime arriveTime;            // 到达时间
    QString airplaneModel;           // 飞机型号
    QString status;                  // 航班状态
    QMap<QString, TicketInfo> tickets; // 机票信息(按舱位)
};
```

### `TicketInfo` (机票信息)
```cpp
struct TicketInfo {
    int ticketId;           // 机票ID
    QString ticketClass;    // 舱位类型 ("economy"/"business"/"first")
    double price;           // 价格
    int totalSeats;         // 总座位数
    int remainSeats;        // 剩余座位数
    bool available();       // 是否有余票
};
```

---

 