# Linux openssl 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

OpenSSL 是一个强大的开源加密工具包，提供了各种加密算法、证书管理功能和 SSL/TLS 协议实现。它是 Linux 系统中处理加密任务的事实标准工具。

OpenSSL 主要功能包括：

  * 创建和管理 SSL 证书
  * 加密/解密文件
  * 生成密钥对
  * 测试 SSL 连接
  * 计算哈希值
  * 数字签名验证



* * *

## 基本语法

openssl 命令的基本语法格式为：

```bash
openssl command [command_options] [command_args]
```


其中：

  * `command`：要执行的 OpenSSL 子命令（如 genrsa、req、x509 等）
  * `command_options`：子命令的选项参数
  * `command_args`：子命令的参数



* * *

## 常用子命令及示例

### 1\. 生成 RSA 密钥对

生成 2048 位的 RSA 私钥：

```bash
openssl genrsa -out private.key 2048
```


从私钥提取公钥：

```bash
openssl rsa -in private.key -pubout -out public.key
```


参数说明：

  * `-out`：指定输出文件
  * `2048`：密钥长度（位）
  * `-pubout`：输出公钥



### 2\. 创建自签名证书

生成 CSR（证书签名请求）：

```bash
openssl req -new -key private.key -out cert.csr
```


生成自签名证书（有效期365天）：

```bash
openssl req -x509 -new -key private.key -days 365 -out cert.crt
```


参数说明：

  * `-new`：创建新请求
  * `-key`：指定私钥文件
  * `-days`：证书有效期（天）
  * `-x509`：输出 X.509 格式证书



### 3\. 文件加密与解密

使用 AES-256-CBC 加密文件：

```bash
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.enc
```


解密文件：

```bash
openssl enc -d -aes-256-cbc -in encrypted.enc -out decrypted.txt
```


参数说明：

  * `-aes-256-cbc`：使用 AES-256-CBC 算法
  * `-salt`：添加随机盐值增强安全性
  * `-in`：输入文件
  * `-out`：输出文件
  * `-d`：解密模式



### 4\. 计算文件哈希值

计算 SHA-256 哈希：

```bash
openssl dgst -sha256 filename.txt
```


计算 MD5 哈希：

```bash
openssl dgst -md5 filename.txt
```


### 5\. 测试 SSL 连接

测试远程服务器的 SSL 证书：

```bash
openssl s_client -connect example.com:443 -showcerts
```


参数说明：

  * `-connect`：指定主机和端口
  * `-showcerts`：显示服务器证书链



* * *

## 高级用法

### 1\. 创建 PKCS#12 格式证书

将证书和私钥打包为 PKCS#12 文件：

```bash
openssl pkcs12 -export -in cert.crt -inkey private.key -out cert.p12
```


### 2\. 证书信息查看

查看证书详细信息：

```bash
openssl x509 -in cert.crt -text -noout
```


### 3\. 验证证书链

验证证书链完整性：

```bash
openssl verify -CAfile ca.crt cert.crt
```


* * *

## 安全注意事项

  1. **密钥保护** ：私钥文件应设置适当权限（如 600），避免泄露
  2. **算法选择** ：避免使用不安全的算法（如 MD5、SHA1）
  3. **密码强度** ：加密时使用强密码
  4. **证书有效期** ：定期更新过期证书
  5. **随机数生成** ：确保系统有足够的熵用于加密操作



* * *

## 常见问题解答

### Q1: 如何检查 OpenSSL 版本？

```bash
openssl version
```


### Q2: 如何生成更安全的 ECC 密钥？

```bash
openssl ecparam -genkey -name secp384r1 -out ecc.key
```


### Q3: 如何转换证书格式？

从 PEM 转换为 DER：

```bash
openssl x509 -in cert.pem -outform der -out cert.der
```


* * *

## 实践练习

  1. 生成一个 4096 位的 RSA 密钥对
  2. 创建一个有效期为 2 年的自签名证书
  3. 加密一个文本文件并使用相同密码解密
  4. 检查你常用网站的 SSL 证书信息



通过掌握 openssl 命令，你将能够处理各种加密和安全相关的任务，为系统安全和管理工作打下坚实基础。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
