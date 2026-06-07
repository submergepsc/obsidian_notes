# 加密有关英文
## HTTPS / TLS 相关
| 缩写        | 全称                                 | 中文含义     | 作用                |
| --------- | ---------------------------------- | -------- | ----------------- |
| **HTTP**  | HyperText Transfer Protocol        | 超文本传输协议  | 浏览器和服务器传输网页数据的协议  |
| **HTTPS** | HyperText Transfer Protocol Secure | 安全的 HTTP | HTTP + TLS，加密传输   |
| **TLS**   | Transport Layer Security           | 传输层安全协议  | HTTPS 背后的安全协议     |
| **SSL**   | Secure Sockets Layer               | 安全套接字层   | TLS 的前身，已过时       |
| **TCP**   | Transmission Control Protocol      | 传输控制协议   | HTTPS 底层依赖的可靠传输协议 |

## 非对称加密 / 签名相关
| 缩写          | 全称                                         | 中文含义                       | 作用                  |
| ----------- | ------------------------------------------ | -------------------------- | ------------------- |
| **RSA**     | Rivest–Shamir–Adleman                      | RSA 算法                     | 以三位发明者姓氏命名，可用于加密和签名 |
| **ECC**     | Elliptic Curve Cryptography                | 椭圆曲线密码学                    | 一类基于椭圆曲线的密码体系       |
| **ECDSA**   | Elliptic Curve Digital Signature Algorithm | 椭圆曲线数字签名算法                 | 用于数字签名              |
| **EdDSA**   | Edwards-curve Digital Signature Algorithm  | Edwards 曲线数字签名算法           | 现代数字签名算法            |
| **Ed25519** | Edwards-curve 25519                        | 基于 Curve25519 的 EdDSA 签名算法 | 常见现代签名算法            |

## 密钥交换相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**DH**|Diffie-Hellman|Diffie-Hellman 密钥交换|双方协商共享密钥|
|**DHE**|Diffie-Hellman Ephemeral|临时 DH 密钥交换|支持前向安全性|
|**ECDH**|Elliptic Curve Diffie-Hellman|椭圆曲线 DH 密钥交换|基于椭圆曲线的密钥交换|
|**ECDHE**|Elliptic Curve Diffie-Hellman Ephemeral|临时椭圆曲线 DH 密钥交换|现代 HTTPS 常用，支持前向安全性|
|**X25519**|X25519 Diffie-Hellman function|基于 Curve25519 的密钥交换算法|TLS 1.3 常用曲线/算法|

## 对称加密相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**AES**|Advanced Encryption Standard|高级加密标准|主流对称加密算法|
|**DES**|Data Encryption Standard|数据加密标准|老旧对称加密算法，已不安全|
|**3DES**|Triple Data Encryption Standard|三重 DES|DES 的增强版，也基本淘汰|
|**RC4**|Rivest Cipher 4 / Ron's Code 4|RC4 流加密算法|已不安全|

## AES 工作模式 / AEAD 相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**AEAD**|Authenticated Encryption with Associated Data|带关联数据的认证加密|同时提供加密和防篡改|
|**GCM**|Galois/Counter Mode|伽罗瓦/计数器模式|AES 常用认证加密模式|
|**CBC**|Cipher Block Chaining|密码分组链接模式|老式分组加密模式|
|**CTR**|Counter Mode|计数器模式|把分组加密变成类似流加密|
|**CCM**|Counter with CBC-MAC|计数器模式 + CBC-MAC|一种 AEAD 模式|
|**ECB**|Electronic Codebook|电子密码本模式|不安全，不应使用|
|**OCB**|Offset Codebook Mode|偏移码本模式|一种 AEAD 模式|

例如：
```text
AES-GCM
```
意思是：
```text
使用 AES 算法，并采用 GCM 认证加密模式
```
## 哈希 / 摘要相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**Hash**|Hash Function|哈希函数 / 散列函数|生成数据指纹|
|**MD5**|Message Digest Algorithm 5|消息摘要算法第 5 版|已不安全|
|**SHA**|Secure Hash Algorithm|安全哈希算法|哈希算法家族|
|**SHA-1**|Secure Hash Algorithm 1|安全哈希算法第 1 版|已不推荐|
|**SHA-256**|Secure Hash Algorithm 256-bit|输出 256 位摘要的 SHA 算法|现代常用|
|**SHA-384**|Secure Hash Algorithm 384-bit|输出 384 位摘要的 SHA 算法|TLS 中常见|
|**SHA-512**|Secure Hash Algorithm 512-bit|输出 512 位摘要的 SHA 算法|安全强度高|

## MAC / 完整性校验相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**MAC**|Message Authentication Code|消息认证码|验证消息没有被篡改|
|**HMAC**|Hash-based Message Authentication Code|基于哈希的消息认证码|常用于接口签名、完整性校验|
|**CMAC**|Cipher-based Message Authentication Code|基于分组密码的消息认证码|基于 AES 等分组算法的 MAC|

## 密钥派生相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**KDF**|Key Derivation Function|密钥派生函数|从原始秘密生成密钥|
|**HKDF**|HMAC-based Key Derivation Function|基于 HMAC 的密钥派生函数|TLS 1.3 常用|
|**PBKDF2**|Password-Based Key Derivation Function 2|基于密码的密钥派生函数第 2 版|常用于密码派生|
|**bcrypt**|Blowfish-based crypt|基于 Blowfish 思想的密码哈希算法|密码存储|
|**scrypt**|script / sequential memory-hard function|内存困难型密码派生函数|密码存储|
|**Argon2**|Argon2|密码哈希算法|现代密码存储推荐方案之一|

## 证书体系相关
|缩写|全称|中文含义|作用|
|---|---|---|---|
|**CA**|Certificate Authority|证书颁发机构|给网站证书做可信签名|
|**PKI**|Public Key Infrastructure|公钥基础设施|管理公钥、证书、CA 的体系|
|**CSR**|Certificate Signing Request|证书签名请求|网站向 CA 申请证书时提交的请求|
|**CRL**|Certificate Revocation List|证书吊销列表|记录已失效证书|
|**OCSP**|Online Certificate Status Protocol|在线证书状态协议|查询证书是否被吊销|
|**SNI**|Server Name Indication|服务器名称指示|TLS 握手时告诉服务器要访问哪个域名|
|**ECH**|Encrypted ClientHello|加密的 ClientHello|加密 TLS 握手中的部分敏感信息|

# 和 HTTPS 最相关的几个重点缩写
你当前重点记这几个就够了：

|缩写|全称|在 HTTPS 中的作用|
|---|---|---|
|**TLS**|Transport Layer Security|HTTPS 的安全层|
|**CA**|Certificate Authority|证明证书可信|
|**RSA**|Rivest–Shamir–Adleman|服务器身份认证 / 签名|
|**ECDSA**|Elliptic Curve Digital Signature Algorithm|服务器身份认证 / 签名|
|**ECDHE**|Elliptic Curve Diffie-Hellman Ephemeral|协商会话密钥|
|**HKDF**|HMAC-based Key Derivation Function|派生真正使用的密钥|
|**AES**|Advanced Encryption Standard|对称加密|
|**GCM**|Galois/Counter Mode|AES 的认证加密模式|
|**AEAD**|Authenticated Encryption with Associated Data|加密 + 防篡改|
|**SHA**|Secure Hash Algorithm|摘要 / 密钥派生相关|

最核心的一条线：
```text
CA / 证书：证明公钥是谁的
RSA / ECDSA：证明服务器拥有私钥
ECDHE：协商共享秘密
HKDF：派生会话密钥
AES-GCM / ChaCha20-Poly1305：加密并保护 HTTP 数据
```
