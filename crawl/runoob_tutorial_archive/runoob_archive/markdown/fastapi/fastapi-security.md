# FastAPI 安全认证

- Source: https://www.runoob.com/fastapi/fastapi-security.html

FastAPI 内置了多种安全工具，支持 OAuth2、JWT 令牌、API Key 等常见的认证和授权方式。本节介绍如何实现基于 OAuth2 + JWT 的用户认证。


---


## 安全认证概述


FastAPI 支持的安全方案：


| 方案 | 适用场景 | 说明 |
| --- | --- | --- |
| HTTP Basic Auth | 简单内部服务 | 用户名密码编码在请求头中，安全性较低 |
| API Key | 服务间调用 | 通过请求头、查询参数或 Cookie 传递密钥 |
| OAuth2 + JWT | 前后端分离应用 | 最常用的方案，安全且灵活 |


---


## OAuth2 密码模式 + JWT


这是前后端分离应用中最常用的认证方案。流程：


- 客户端发送用户名和密码到 `/token` 端点
- 服务器验证凭据，返回 JWT 访问令牌
- 客户端在后续请求中携带令牌（`Authorization: Bearer `）
- 服务器验证令牌，识别用户身份


### 1. 安装依赖


```
pip install "python-jose[cryptography]" passlib[bcrypt]
```


### 2. 完整示例


## 实例


```python
from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# ===== 配置 =====
SECRET_KEY = "your-secret-key-keep-it-secret"  # 生产环境使用环境变量
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ===== 密码哈希 =====
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== OAuth2 方案 =====
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ===== 数据模型 =====
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

# ===== 模拟数据库 =====
fake_users_db = {
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "[email protected]",
        "hashed_password": pwd_context.hash("secret"),  # 密码: secret
        "disabled": False,
    }
}

# ===== 工具函数 =====
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)

def get_user(db: dict, username: str) -> UserInDB | None:
    """从数据库获取用户"""
    if username in db:
        return UserInDB(**db[username])
    return None

def authenticate_user(db: dict, username: str, password: str):
    """验证用户凭据"""
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """创建 JWT 访问令牌"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """从令牌中获取当前用户（依赖函数）"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    """获取当前活跃用户"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="用户已被禁用")
    return current_user

# ===== 路由 =====
app = FastAPI()

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """登录获取令牌"""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """获取当前用户信息（需要认证）"""
    return current_user

@app.get("/users/me/items")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """获取当前用户的条目（需要认证）"""
    return [{"item_id": "Foo", "owner": current_user.username}]
```


---


## 代码解析


### 密码哈希


使用 `passlib` 的 bcrypt 算法对密码进行哈希处理，确保数据库中不存储明文密码：


| 函数 | 说明 |
| --- | --- |
| pwd_context.hash(password) | 将明文密码转为哈希值 |
| pwd_context.verify(plain, hashed) | 验证明文密码是否匹配哈希值 |


### JWT 令牌


JWT（JSON Web Token）是一种安全的令牌格式，包含用户信息和过期时间：


| 操作 | 函数 | 说明 |
| --- | --- | --- |
| 创建令牌 | jwt.encode() | 将数据编码为 JWT 字符串 |
| 解析令牌 | jwt.decode() | 解析并验证 JWT 字符串 |
| 设置过期 | "exp": expire | 令牌的过期时间 |
| 存储用户标识 | "sub": username | 令牌的主体（通常是用户名） |


### OAuth2PasswordBearer


告诉 FastAPI 从 `Authorization: Bearer ` 请求头中获取令牌：


```
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```


`tokenUrl="token"` 指定客户端获取令牌的端点路径，会出现在 API 文档中。


**
`SECRET_KEY` 必须保密且足够复杂，生产环境应使用环境变量存储。如果密钥泄露，攻击者可以伪造任意用户的令牌。


---


## 使用 API 文档测试


配置 OAuth2 后，Swagger UI 会出现"Authorize"按钮：


- 点击 **"Authorize"**
- 输入用户名和密码（如 `alice` / `secret`）
- 点击 **"Authorize"** 获取令牌
- 之后的所有请求都会自动携带令牌


---


## 小结


- OAuth2 + JWT 是前后端分离应用最常用的认证方案
- 密码必须哈希存储，不能明文保存
- JWT 令牌包含用户标识和过期时间
- 使用依赖注入（`Depends`）实现认证逻辑的复用
- 生产环境中 SECRET_KEY 必须保密









	  AI 思考中...





			** [FastAPI 静态文件](https://www.runoob.com/fastapi-static-files.html)
			[FastAPI 测试](https://www.runoob.com/fastapi-testing.html) **













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