# Node.js 连接 MongoDB

- Source: https://www.runoob.com/nodejs/nodejs-mongodb.html

MongoDB是一种文档导向数据库管理系统，由C++撰写而成。


本章节我们将为大家介绍如何使用 Node.js 来连接 MongoDB，并对数据库进行操作。


如果你还没有 MongoDB 的基本知识，可以参考我们的教程：[MongoDB 教程](https://www.runoob.com/../mongodb/mongodb-tutorial.html)。 ### 安装驱动 本教程使用了[淘宝定制的 cnpm 命令](https://www.runoob.com/nodejs-npm.html)进行安装：


```
$ cnpm install mongodb
```


安装成功后 我们就可以使用 MongoClient 对象来连接数据库了：


## 实例


```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 如果你使用的是远程 MongoDB，请相应更改 URI

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("Connected successfully to server");

    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行以上代码，输出结果为：


```
Connected successfully to server
```


连接参数说明：


- `MongoClient`：这是 MongoDB 的客户端，用于连接到数据库。
- `uri`：这是 MongoDB 的连接字符串，格式为 `mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]`。
- `useNewUrlParser` 和 `useUnifiedTopology` 是一些选项，用于避免一些旧的连接行为。


接下来我们来实现增删改查功能。


---

## 创建数据库


要在 MongoDB 中创建一个数据库，首先我们需要创建一个 MongoClient 对象，然后配置好指定的 URL 和 端口号。


如果数据库不存在，MongoDB 将创建数据库并建立连接。


## 创建连接



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 这里可以执行数据库操作，例如创建集合或插入文档
        const collection = database.collection('exampleCollection');
        const doc = { name: "Example", type: "Test" };
        const result = await collection.insertOne(doc);

        console.log(`新文档已创建，ID 为: ${result.insertedId}`);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行以上代码，输出结果为：


```
成功连接到服务器
新文档已创建，ID 为: 6678e18e0bb3f4247be610d8
```


---

## 创建集合

我们可以使用 createCollection() 方法来创建集合：

## 创建集合



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建一个新文档
        const doc = { name: "Example", type: "Test" };

        // 插入文档到集合
        const result = await collection.insertOne(doc);

        console.log(`新文档已创建，ID 为: ${result.insertedId}`);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行以上代码，输出结果为：


```
成功连接到服务器
集合 exampleCollection 创建成功
新文档已创建，ID 为: 6678e1b5c742b3ebd57f9759
```


---


## 数据库操作( CURD )


与 MySQL 不同的是 MongoDB 会自动创建数据库和集合，所以使用前我们不需要手动去创建。


### 插入数据


以下实例我们连接数据库 runoob 的 exampleCollection 表，并插入一条数据条数据，使用** insertOne()**：


## 插入一条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建一个新文档
        const doc = { name: "Alice", age: 25, address: "Wonderland" };

        // 插入文档到集合
        const result = await collection.insertOne(doc);

        console.log(`新文档已创建，ID 为: ${result.insertedId}`);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行以下命令输出就结果为：


```javascript
成功连接到服务器
集合 exampleCollection 创建成功
新文档已创建，ID 为: 6678e1d1f9503dc2e0e2a20b
```


从输出结果来看，数据已插入成功。


我们也可以打开 MongoDB 的客户端查看数据，如：


```
> show dbs
runoob  0.000GB          # 创建了 runoob 数据库

> use runoob             # 切换到 runoob 数据库

runoob> show tables
exampleCollection        # 创建了 exampleCollection 集合（数据表）
                    # 自动创建了 site 集合（数据表）
runoob> db.exampleCollection.find()
[
  {
    _id: ObjectId('6678e1d1f9503dc2e0e2a20b'),
    name: 'Alice',
    age: 25,
    address: 'Wonderland'
  }
]
```


如果要插入多条数据可以使用 **insertMany()**：


## 插入多条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((key, index) => {
            console.log(`文档 ${index + 1}: ${result.insertedIds[key]}`);
        });
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行输出结果为：


```
成功连接到服务器
集合 exampleCollection 创建成功
3 个新文档已创建，ID 为:
文档 1: 6678e30e80ac30e5e689f13a
文档 2: 6678e30e80ac30e5e689f13b
文档 3: 6678e30e80ac30e5e689f13c
```


### 查询数据


可以使用 find() 来查找数据, find() 可以返回匹配条件的所有数据。 如果未指定条件，find() 返回集合中的所有数据。 ## find()
```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 查询集合中的所有文档
        const query = {}; // 空查询对象表示查询所有文档
        const options = { projection: { _id: 0, name: 1, age: 1, address: 1 } }; // 仅选择需要的字段
        const cursor = collection.find(query, options);

        // 打印查询到的所有文档
        const allValues = await cursor.toArray();
        console.log("查询到的文档:");
        console.log(allValues);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```
 执行输出结果为：


```
成功连接到服务器
集合 exampleCollection 创建成功
3 个新文档已创建，ID 为:
文档 1: 0
文档 2: 1
文档 3: 2
查询到的文档:
[
  { name: 'Alice', age: 25, address: 'Wonderland' },
  { name: 'Bob', age: 30, address: 'Builderland' },
  { name: 'Charlie', age: 35, address: 'Chocolate Factory' }
]
```


以下实例检索 name 为 "Alice" 的实例：


## 查询指定条件的数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 使用 name 参数查询文档
        const query = { name: "Alice" }; // 搜索条件
        const options = { projection: { _id: 0, name: 1, age: 1, address: 1 } }; // 仅选择需要的字段
        const cursor = collection.find(query, options);

        // 打印查询到的文档
        const allValues = await cursor.toArray();
        console.log("查询到的文档:");
        console.log(allValues);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行以下命令输出就结果为：


```javascript
成功连接到服务器
集合 exampleCollection 创建成功
3 个新文档已创建，ID 为:
文档 1: 0
文档 2: 1
文档 3: 2
查询到的文档:
[
  { name: 'Alice', age: 25, address: 'Wonderland' }
]
```


### 更新数据


我们也可以对数据库的数据进行修改，以下实例将 name 为 "Alice" 的 数据：


## 更新一条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 指定条件，根据 name 参数更新数据
        const filter = { name: "Alice" }; // 搜索条件
        const updateDoc = {
            $set: {
                age: 28,
                address: "New Wonderland"
            },
        };

        const updateResult = await collection.updateOne(filter, updateDoc);

        console.log(`${updateResult.matchedCount} 个文档匹配筛选条件`);
        console.log(`${updateResult.modifiedCount} 个文档已更新`);

        // 查询更新后的文档
        const updatedDocument = await collection.findOne(filter);
        console.log("更新后的文档:");
        console.log(updatedDocument);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行成功后，输出结果如下：


```javascript
成功连接到服务器
集合 exampleCollection 创建成功
3 个新文档已创建，ID 为:
文档 1: 0
文档 2: 1
文档 3: 2
1 个文档匹配筛选条件
1 个文档已更新
更新后的文档:
{
  _id: new ObjectId('6678e1d1f9503dc2e0e2a20b'),
  name: 'Alice',
  age: 28,
  address: 'New Wonderland'
}
```


如果要更新所有符合条的文档数据可以使用 **updateMany()**：


## 更新多条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Alice", age: 28, address: "Old Wonderland" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 指定条件，根据 name 参数更新多个文档
        const filter = { name: "Alice" }; // 搜索条件
        const updateDoc = {
            $set: {
                address: "Updated Wonderland"
            },
        };

        const updateResult = await collection.updateMany(filter, updateDoc);

        console.log(`${updateResult.matchedCount} 个文档匹配筛选条件`);
        console.log(`${updateResult.modifiedCount} 个文档已更新`);

        // 查询更新后的文档
        const updatedDocuments = await collection.find(filter).toArray();
        console.log("更新后的文档:");
        console.log(updatedDocuments);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


### 删除数据


以下实例将 name 为 "Alice" 的数据删除 :


## 删除一条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 指定条件，根据 name 参数删除一个文档
        const filter = { name: "Alice" }; // 搜索条件

        const deleteResult = await collection.deleteOne(filter);

        console.log(`${deleteResult.deletedCount} 个文档已删除`);

        // 查询集合中的所有文档，确认删除
        const remainingDocuments = await collection.find({}).toArray();
        console.log("剩余的文档:");
        console.log(remainingDocuments);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


执行成功后，输出结果为：


```javascript
成功连接到服务器
集合 exampleCollection 创建成功
3 个新文档已创建，ID 为:
文档 1: 0
文档 2: 1
文档 3: 2
1 个文档已删除
剩余的文档:
[
  {
    _id: new ObjectId('6678e18e0bb3f4247be610d8'),
    name: 'Example',
    type: 'Test'
  },
...
```


如果要删除多条语句可以使用 **deleteMany()** 方法 以下实例将 type 为 en 的所有数据删除 :


## 删除多条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Alice", age: 28, address: "Old Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 指定条件，根据 name 参数删除多个文档
        const filter = { name: "Alice" }; // 搜索条件

        const deleteResult = await collection.deleteMany(filter);

        console.log(`${deleteResult.deletedCount} 个文档已删除`);

        // 查询集合中的所有文档，确认删除
        const remainingDocuments = await collection.find({}).toArray();
        console.log("剩余的文档:");
        console.log(remainingDocuments);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


### 排序


排序 使用 sort() 方法，该方法接受一个参数，规定是升序(1)还是降序(-1)。


例如：


```
{ type: 1 }  // 按 type 字段升序
{ type: -1 } // 按 type 字段降序
```


按 type 升序排列:


## 排序



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" },
            { name: "Dave", age: 20, address: "Dreamland" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 使用 sort() 方法对文档进行排序
        // 按 age 字段升序排序
        const sortedDocsAsc = await collection.find().sort({ age: 1 }).toArray();
        console.log("按 age 字段升序排序后的文档:");
        console.log(sortedDocsAsc);

        // 按 age 字段降序排序
        const sortedDocsDesc = await collection.find().sort({ age: -1 }).toArray();
        console.log("按 age 字段降序排序后的文档:");
        console.log(sortedDocsDesc);

    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


### 查询分页


如果要设置指定的返回条数可以使用 **limit()** 方法，该方法只接受一个参数，指定了返回的条数。


## limit()：读取两条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" },
            { name: "Dave", age: 20, address: "Dreamland" },
            { name: "Eve", age: 22, address: "Eden" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 使用 limit() 方法限制查询结果的数量
        const limitedDocs = await collection.find().limit(3).toArray();
        console.log("限制查询结果为 3 条文档:");
        console.log(limitedDocs);

    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


如果要指定跳过的条数，可以使用 **skip()** 方法。


skip() 方法用于跳过指定数量的文档，并返回剩余文档的查询结果。


## skip(): 跳过前面两条数据，读取两条数据



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('runoob');

        // 使用 createCollection 方法创建集合
        const collectionName = 'exampleCollection';
        await database.createCollection(collectionName);
        console.log(`集合 ${collectionName} 创建成功`);

        // 获取集合
        const collection = database.collection(collectionName);

        // 创建多个新文档
        const docs = [
            { name: "Alice", age: 25, address: "Wonderland" },
            { name: "Bob", age: 30, address: "Builderland" },
            { name: "Charlie", age: 35, address: "Chocolate Factory" },
            { name: "Dave", age: 20, address: "Dreamland" },
            { name: "Eve", age: 22, address: "Eden" }
        ];

        // 插入多个文档到集合
        const result = await collection.insertMany(docs);

        console.log(`${result.insertedCount} 个新文档已创建，ID 为:`);
        Object.keys(result.insertedIds).forEach((id, index) => {
            console.log(`文档 ${index + 1}: ${id}`);
        });

        // 使用 skip() 方法跳过前两个文档，返回剩余的文档
        const skippedDocs = await collection.find().skip(2).toArray();
        console.log("跳过前两个文档后的查询结果:");
        console.log(skippedDocs);

    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


### 连接操作


mongoDB 不是一个关系型数据库，但我们可以使用 **$lookup** 来实现左连接。


$lookup 是 MongoDB 中用于执行左外连接（left outer join）的聚合管道操作符。它可以用来在一个集合中查找另一个集合中匹配条件的文档，并将它们合并在一起。


例如我们有两个集合数据分别为：


集合1：orders


```
[
  { "_id": 1, "product_id": 101, "quantity": 2 },
  { "_id": 2, "product_id": 102, "quantity": 1 },
  { "_id": 3, "product_id": 103, "quantity": 4 }
]
```


集合2：products


```
[
  { "_id": 101, "name": "Product A", "price": 50 },
  { "_id": 102, "name": "Product B", "price": 70 },
  { "_id": 103, "name": "Product C", "price": 100 },
  { "_id": 104, "name": "Product D", "price": 120 }
]
```


现在我们希望通过 $lookup 操作将 orders 集合中的 product_id 字段与 products 集合中的 _id 字段进行关联，获取每个订单中的产品详细信息。

以下是如何实现这个功能的 MongoDB 聚合示例：


## 实例



```javascript
const { MongoClient } = require('mongodb');

async function main() {
    // MongoDB 连接 URI
    const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

    // 创建一个新的 MongoClient
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // 连接到 MongoDB 服务器
        await client.connect();

        console.log("成功连接到服务器");

        // 指定数据库
        const database = client.db('mydatabase');

        // orders 集合
        const ordersCollection = database.collection('orders');

        // products 集合
        const productsCollection = database.collection('products');

        // 定义聚合管道，使用 $lookup 进行左外连接
        const pipeline = [
            {
                $lookup: {
                    from: 'products',         // 关联的集合名
                    localField: 'product_id', // 本地集合中用于关联的字段
                    foreignField: '_id',      // 关联集合中用于关联的字段
                    as: 'productDetails'      // 输出结果中包含的字段名
                }
            }
        ];

        // 执行聚合操作
        const result = await ordersCollection.aggregate(pipeline).toArray();

        // 输出查询结果
        console.log("左外连接查询结果:");
        console.log(result);

    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

main().catch(console.error);
```


### 删除集合


我们可以使用 **drop()** 方法来删除集合：


## drop()



```javascript
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("runoob");
    // 删除 test 集合
    dbo.collection("test").drop(function(err, delOK) {  // 执行成功 delOK 返回 true，否则返回 false
        if (err) throw err;
        if (delOK) console.log("集合已删除");
        db.close();
    });
});
```


---


## 使用 Promise

Promise 是一个 ECMAScript 6 提供的类，目的是更加优雅地书写复杂的异步任务。

如果你还不了解 Promise，可以参考 [JavaScript Promise](https://www.runoob.com/../js/js-promise.html)。


以下实例使用 Promise 创建集合：


## 实例


```javascript
const { MongoClient } = require('mongodb');

// MongoDB 连接 URI
const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

// 创建一个新的 MongoClient
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

// 使用 Promise 封装连接数据库的过程
function connectDB() {
    return new Promise((resolve, reject) => {
        // 连接到 MongoDB 服务器
        client.connect((err) => {
            if (err) {
                reject(err);
            } else {
                console.log("成功连接到 MongoDB 服务器");
                resolve(client.db()); // 返回数据库实例
            }
        });
    });
}

// 使用示例
connectDB()
    .then(database => {
        // 这里可以继续执行数据库操作
        console.log("连接到数据库成功");

        // 示例：输出数据库的名称
        console.log("数据库名称:", database.databaseName);

        // 如果需要进行其他操作，可以在这里继续编写代码
        // 比如查询、插入文档等

        // 最后关闭连接
        client.close();
    })
    .catch(err => {
        console.error("连接数据库时发生错误:", err);
    });
```


### Promise 数据操作


现在我们在一个程序中实现四个连续操作：增加 、查询 、更改 、删除。


## 实例


```javascript
const { MongoClient, ObjectId } = require('mongodb');

// MongoDB 连接 URI
const uri = "mongodb://localhost:27017"; // 请根据你的 MongoDB 服务器地址进行修改

// 创建一个新的 MongoClient
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

// 使用 Promise 封装连接数据库的过程
function connectDB() {
    return new Promise((resolve, reject) => {
        // 连接到 MongoDB 服务器
        client.connect((err) => {
            if (err) {
                reject(err);
            } else {
                console.log("成功连接到 MongoDB 服务器");
                resolve(client.db()); // 返回数据库实例
            }
        });
    });
}

// 添加文档的函数
function insertDocument(db, document) {
    const collection = db.collection('documents');
    return new Promise((resolve, reject) => {
        collection.insertOne(document, (err, result) => {
            if (err) {
                reject(err);
            } else {
                console.log("添加文档成功");
                resolve(result);
            }
        });
    });
}

// 查询文档的函数
function findDocuments(db) {
    const collection = db.collection('documents');
    return new Promise((resolve, reject) => {
        collection.find({}).toArray((err, docs) => {
            if (err) {
                reject(err);
            } else {
                console.log("查询文档结果:");
                console.log(docs);
                resolve(docs);
            }
        });
    });
}

// 更新文档的函数
function updateDocument(db, id, updatedValues) {
    const collection = db.collection('documents');
    return new Promise((resolve, reject) => {
        collection.updateOne({ _id: ObjectId(id) }, { $set: updatedValues }, (err, result) => {
            if (err) {
                reject(err);
            } else {
                console.log("更新文档成功");
                resolve(result);
            }
        });
    });
}

// 删除文档的函数
function deleteDocument(db, id) {
    const collection = db.collection('documents');
    return new Promise((resolve, reject) => {
        collection.deleteOne({ _id: ObjectId(id) }, (err, result) => {
            if (err) {
                reject(err);
            } else {
                console.log("删除文档成功");
                resolve(result);
            }
        });
    });
}

// 使用示例：连续执行增加、查询、更改、删除操作
async function performOperations() {
    try {
        const database = await connectDB();

        // 添加文档
        const insertResult = await insertDocument(database, { name: "Document 1" });

        // 查询文档
        const findResult = await findDocuments(database);

        // 更新文档
        const updatedDocId = insertResult.insertedId; // 使用插入文档返回的 ID 进行更新
        const updateResult = await updateDocument(database, updatedDocId, { name: "Updated Document 1" });

        // 删除文档
        const deleteResult = await deleteDocument(database, updatedDocId);

        // 输出操作结果
        console.log("最终操作完成:");
        console.log("删除文档结果:", deleteResult);

    } catch (err) {
        console.error("执行操作时发生错误:", err);
    } finally {
        // 确保在完成后关闭连接
        await client.close();
    }
}

// 执行操作
performOperations();
```


执行结果：


```
数据库已连接
[ { _id: 5f1664966833e531d83d3ac6, site: 'runoob.com' } ]
[ { _id: 5f1664966833e531d83d3ac6, site: 'example.com' } ]
[]
```










	  AI 思考中...





			** [Node.js 连接 MySQL](https://www.runoob.com/nodejs-mysql.html)
			[Node.js 构建简单应用](https://www.runoob.com/nodejs-build-app.html) **