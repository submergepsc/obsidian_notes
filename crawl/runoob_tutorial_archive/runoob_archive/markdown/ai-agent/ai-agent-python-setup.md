# Python 智能体环境配置

- Source: https://www.runoob.com/ai-agent/ai-agent-python-setup.html

在开始构建 AI Agent 之前，我们需要搭建合适的开发环境。


Python 是 AI 和机器学习领域最流行的语言，拥有丰富的库和工具支持。


### 1. Python 版本选择


对于 AI Agent 开发，我们推荐使用 **Python 3.9 或更高版本**。


以下版本是常见选择：


- **Python 3.9**：稳定性好，兼容性最佳
- **Python 3.10**：性能改进，新特性
- **Python 3.11+**：最新版本，性能最佳


**注意**：某些库可能对 Python 版本有特定要求，建议查看官方文档。


### 2. 安装 Python


#### Windows 系统


- 访问 [Python 官网](https://www.python.org/downloads/)
- 下载最新版本的 Python 安装程序（3.9 或更高版本）
- 运行安装程序，**务必勾选 **Add Python to PATH****
- 完成安装后，打开命令提示符（CMD）或 PowerShell，输入： **python --version**，应显示 Python 版本号。


#### macOS 系统


macOS 通常预装了 Python，但可能是旧版本。推荐使用 Homebrew 安装：


```
# 安装 Homebrew（如果尚未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install [email protected]

# 验证安装
python3 --version
```


#### Linux 系统


大多数 Linux 发行版已预装 Python。如需要特定版本：


```
# Ubuntu/Debian
sudo apt update
sudo apt install python3.9 python3-pip

# CentOS/RHEL
sudo yum install python39 python39-pip

# 验证安装
python3 --version
```


### 3. 虚拟环境配置


使用虚拟环境可以隔离不同项目的依赖，避免版本冲突。


#### 创建虚拟环境


```
# 创建项目目录
mkdir ai-agent-project
cd ai-agent-project
```


使用 uv 创建并激活虚拟环境，更多相关内容可以阅读 [uv 教程](https://www.runoob.com/../python3/uv-tutorial.html)。


安装 uv


```
pip install uv
```


使用 uv 命令创建：


```
# 创建名为 .venv 的虚拟环境（默认）
uv venv

# 激活环境（macOS/Linux）
source .venv/bin/activate

# 激活环境（Windows）
.venv\Scripts\activate
```


其他工具：


```
# 使用 venv，Python 3.3+ 内置
python -m venv venv

# 或使用 conda（如果已安装 Anaconda/Miniconda）
conda create -n ai-agent python=3.9
conda activate ai-agent
```


#### 激活虚拟环境


**Windows：**


```
venv\Scripts\activate
```


** macOS/Linux：**


```
source venv/bin/activate
```


激活后，命令行提示符通常会显示虚拟环境名称（如 **(venv)**）。


#### 退出虚拟环境


```
deactivate
```


### 4. 包管理工具 pip


pip 是 Python 的包管理工具，用于安装第三方库。


**常用命令**：


```
# 升级 pip 到最新版本
pip install --upgrade pip

# 安装包
pip install package_name

# 安装特定版本
pip install package_name==1.2.3

# 从 requirements.txt 安装所有依赖
pip install -r requirements.txt

# 列出已安装的包
pip list

# 生成 requirements.txt
pip freeze > requirements.txt
```


### 5. 开发目录结构建议


一个良好的项目结构有助于代码管理和维护：


```
ai-agent-project/
├── .env                    # 环境变量文件（不提交到Git）
├── .gitignore             # Git忽略文件
├── requirements.txt       # 项目依赖
├── README.md             # 项目说明
├── src/                  # 源代码目录
│   ├── __init__.py
│   ├── agents/          # Agent相关代码
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   └── weather_agent.py
│   ├── tools/           # 工具定义
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   └── web_search.py
│   ├── memory/          # 记忆系统
│   │   ├── __init__.py
│   │   ├── short_term.py
│   │   └── vector_memory.py
│   └── utils/           # 工具函数
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
├── tests/               # 测试代码
│   ├── __init__.py
│   ├── test_agents.py
│   └── test_tools.py
├── examples/            # 示例代码
│   ├── basic_agent.py
│   └── multi_tool_agent.py
└── notebooks/           # Jupyter笔记本
    └── experiments.ipynb
```


---


## 必备库安装


AI Agent 开发需要一系列第三方库的支持。以下是核心库的安装方法和简要介绍。


### 核心库安装


创建 `requirements.txt` 文件，包含以下内容：


```
# 基础库
python-dotenv>=1.0.0      # 环境变量管理
pydantic>=2.0.0           # 数据验证和设置管理
loguru>=0.7.0             # 日志记录

# AI/ML 相关
openai>=1.0.0             # OpenAI API
anthropic>=0.7.0          # Claude API
google-generativeai>=0.3.0 # Gemini API
sentence-transformers>=2.2.0 # Embedding 模型
chromadb>=0.4.0           # 向量数据库

# Agent 框架
langchain>=0.1.0          # LangChain 框架
langchain-community>=0.0.10 # LangChain 社区工具
langchain-openai>=0.0.5   # LangChain OpenAI 集成
llama-index>=0.10.0       # LlamaIndex（可选）
semantic-kernel>=0.9.0    # Semantic Kernel（可选）

# 工具和工具
requests>=2.31.0          # HTTP 请求
beautifulsoup4>=4.12.0    # HTML 解析
pandas>=2.0.0             # 数据处理
numpy>=1.24.0             # 数值计算

# 开发工具
pytest>=7.4.0             # 测试框架
black>=23.0.0             # 代码格式化
flake8>=6.0.0             # 代码检查
jupyter>=1.0.0            # Jupyter 笔记本
```


安装所有依赖：


```
pip install -r requirements.txt
```


### 主要库介绍


#### 1. LangChain


LangChain 是最流行的 AI Agent 开发框架，提供了构建链式（Chain）和代理（Agent）应用的工具。


```
# LangChain 基本使用示例
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# 初始化 LLM
llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

# 创建工具
tools = [
    Tool(
        name="计算器",
        func=lambda x: str(eval(x)),
        description="用于数学计算"
    )
]

# 创建 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 运行 Agent
result = agent.run("计算 25 的平方根")
print(result)
```


#### 2. LlamaIndex


LlamaIndex（原 GPT Index）专注于文档索引和检索，适合构建基于文档的问答系统。


```
# LlamaIndex 基本使用示例
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import OpenAI

# 加载文档
documents = SimpleDirectoryReader("./data").load_data()

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 创建查询引擎
query_engine = index.as_query_engine()

# 查询
response = query_engine.query("文档中提到了哪些AI技术？")
print(response)
```


#### 3. Semantic Kernel


Semantic Kernel 是微软推出的框架，强调可扩展性和企业级应用。


```
# Semantic Kernel 基本使用示例
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

# 初始化内核
kernel = sk.Kernel()
api_key = "your-openai-api-key"
kernel.add_text_completion_service(
    "dv",
    OpenAITextCompletion("text-davinci-003", api_key)
)

# 定义技能
skill = kernel.import_semantic_skill_from_directory("./skills", "ExampleSkill")

# 运行技能
context = kernel.create_new_context()
context["input"] = "介绍一下人工智能"
result = skill["Summarize"](context)
print(result)
```


### 安装验证


创建一个验证脚本 `verify_installation.py`：


## 实例


```
# verify_installation.py
import sys

def check_package(package_name, import_name=None):
    """检查包是否安装"""
    import_name = import_name or package_name
    try:
        __import__(import_name)
        print(f"{package_name} 安装成功")
        return True
    except ImportError:
        print(f"{package_name} 未安装")
        return False

def main():
    print("检查 AI Agent 开发环境...")
    print("=" * 50)

    # 检查 Python 版本
    python_version = sys.version_info
    print(f"Python 版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if python_version.major == 3 and python_version.minor >= 9:
        print("Python 版本符合要求 (>=3.9)")
    else:
        print("Python 版本不符合要求，需要 3.9 或更高版本")

    print("\n检查核心库...")

    # 基础库
    check_package("dotenv", "dotenv")
    check_package("pydantic")
    check_package("loguru")

    # AI/ML 库
    check_package("openai")
    check_package("anthropic")
    check_package("chromadb")
    check_package("sentence_transformers", "sentence_transformers")

    # Agent 框架
    check_package("langchain")
    check_package("llama_index", "llama_index")

    # 工具库
    check_package("requests")
    check_package("pandas")
    check_package("numpy")

    print("\n" + "=" * 50)
    print("环境检查完成！")

if __name__ == "__main__":
    main()
```


运行验证：


```
python verify_installation.py
```


### 常见安装问题解决


#### 1. 安装速度慢或超时


```
# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用阿里云镜像
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```


#### 2. 版本冲突


```
# 创建新的虚拟环境
python -m venv new_venv
source new_venv/bin/activate  # 或 venv\Scripts\activate

# 重新安装，让 pip 自动解决依赖
pip install --upgrade pip
pip install langchain openai
```


#### 3. 特定平台问题（如 Apple Silicon）


```
# 对于 Apple Silicon (M1/M2/M3)，可能需要特定版本
pip install grpcio==1.48.2  # 解决某些兼容性问题

# 或使用 conda
conda install -c conda-forge grpcio
```


---


## API Key 管理


AI Agent 开发需要访问各种 API 服务（如 OpenAI、Anthropic、DeepSeek 等），安全、有效地管理 API Key 至关重要。


### 1. 为什么需要安全管理 API Key？


- **防止泄露**：API Key 泄露可能导致经济损失
- **访问控制**：不同环境使用不同的 Key
- **方便配置**：团队协作时统一配置方式
- **环境隔离**：开发、测试、生产环境使用不同的 Key


### 2. 环境变量管理（推荐）


使用 `.env` 文件管理敏感信息，不提交到版本控制系统。


#### 创建 .env 文件


```
# API Keys
OPENAI_API_KEY=sk-你的OpenAI密钥
ANTHROPIC_API_KEY=你的Claude密钥
GOOGLE_API_KEY=你的Gemini密钥
SERPAPI_API_KEY=你的搜索API密钥

# 应用配置
APP_ENV=development
LOG_LEVEL=INFO
DEBUG=true

# 数据库配置（如使用）
VECTOR_DB_PATH=./data/vector_db
MAX_MEMORY_ITEMS=1000
```


#### 创建 .gitignore 文件


确保 `.env` 文件不被提交到 Git：


```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# 环境变量
.env
.env.local
.env.*.local

# 数据文件
data/
*.db
*.sqlite
*.sqlite3

# 日志
logs/
*.log

# 编辑器
.vscode/
.idea/
*.swp
*.swo
```


#### 使用 python-dotenv 加载环境变量


## 实例


```
# config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    """应用配置"""

    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

    # 应用配置
    APP_ENV = os.getenv("APP_ENV", "development")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    # 数据库配置
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vector_db")
    MAX_MEMORY_ITEMS = int(os.getenv("MAX_MEMORY_ITEMS", "1000"))

    @classmethod
    def validate(cls):
        """验证必要配置"""
        missing = []

        if not cls.OPENAI_API_KEY:
            missing.append("OPENAI_API_KEY")

        if missing:
            raise ValueError(f"缺少必要的环境变量: {', '.join(missing)}")

# 使用示例
config = Config()
print(f"环境: {config.APP_ENV}")
print(f"调试模式: {config.DEBUG}")
```


### 3. 安全使用 API Key


#### 在代码中使用环境变量


```
import os
from openai import OpenAI

# 从环境变量读取 API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY 环境变量未设置")

# 初始化 OpenAI 客户端
client = OpenAI(api_key=api_key)

# 使用客户端
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "你好"}]
)
```


#### 使用配置类


## 实例


```
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from config import Config

class LLMClientFactory:
    """LLM 客户端工厂"""

    @staticmethod
    def create_openai_client(model="gpt-3.5-turbo", **kwargs):
        """创建 OpenAI 客户端"""
        Config.validate()  # 验证配置

        return ChatOpenAI(
            model=model,
            openai_api_key=Config.OPENAI_API_KEY,
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_tokens", 1000)
        )

    @staticmethod
    def create_anthropic_client(model="claude-3-sonnet-20240229", **kwargs):
        """创建 Anthropic 客户端"""
        from langchain.chat_models import ChatAnthropic

        Config.validate()

        return ChatAnthropic(
            model=model,
            anthropic_api_key=Config.ANTHROPIC_API_KEY,
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_tokens", 1000)
        )

# 使用示例
llm = LLMClientFactory.create_openai_client()
response = llm.predict("你好，请介绍一下自己")
print(response)
```


### 4. 多环境配置


对于大型项目，可能需要不同的环境配置：


#### 环境特定的 .env 文件


```
# .env.development (开发环境)
OPENAI_API_KEY=sk-dev-key
APP_ENV=development
DEBUG=true

# .env.production (生产环境)
OPENAI_API_KEY=sk-prod-key
APP_ENV=production
DEBUG=false
```


#### 动态加载环境配置


```
# config_manager.py
import os
from pathlib import Path
from dotenv import load_dotenv

class ConfigManager:
    """配置管理器"""

    def __init__(self, env=None):
        self.env = env or os.getenv("APP_ENV", "development")
        self.load_config()

    def load_config(self):
        """加载配置"""
        # 先加载通用配置
        load_dotenv(dotenv_path=Path('.') / '.env')

        # 加载环境特定配置
        env_file = Path('.') / f'.env.{self.env}'
        if env_file.exists():
            load_dotenv(dotenv_path=env_file, override=True)

        # 加载本地覆盖配置（不提交到Git）
        local_file = Path('.') / f'.env.{self.env}.local'
        if local_file.exists():
            load_dotenv(dotenv_path=local_file, override=True)

    def get(self, key, default=None):
        """获取配置值"""
        return os.getenv(key, default)

# 使用示例
config = ConfigManager(env="development")
print(f"当前环境: {config.get('APP_ENV')}")
print(f"API Key: {config.get('OPENAI_API_KEY')[:10]}...")  # 只显示前10个字符
```


### 5. 密钥轮换和监控


对于生产环境，建议实施密钥轮换和监控：


```
# key_manager.py
import os
import time
from datetime import datetime, timedelta

class APIKeyManager:
    """API Key 管理器"""

    def __init__(self):
        self.keys = {}
        self.key_history = []
        self.load_keys()

    def load_keys(self):
        """加载 API Keys"""
        # 可以从环境变量、数据库或密钥管理服务加载
        self.keys = {
            "openai": {
                "current": os.getenv("OPENAI_API_KEY"),
                "previous": os.getenv("OPENAI_API_KEY_PREVIOUS"),
                "created_at": datetime.now(),
                "rotation_days": 30  # 30天轮换一次
            },
            "anthropic": {
                "current": os.getenv("ANTHROPIC_API_KEY"),
                "previous": None,
                "created_at": datetime.now(),
                "rotation_days": 30
            }
        }

    def get_key(self, service):
        """获取当前可用的 Key"""
        key_info = self.keys.get(service)
        if not key_info:
            raise ValueError(f"未配置服务 {service} 的 API Key")

        # 检查是否需要轮换
        if self.should_rotate(key_info):
            self.rotate_key(service)

        return key_info["current"]

    def should_rotate(self, key_info):
        """检查是否需要轮换 Key"""
        rotation_days = key_info.get("rotation_days", 30)
        created_at = key_info.get("created_at", datetime.now())

        age = datetime.now() - created_at
        return age.days >= rotation_days

    def rotate_key(self, service):
        """轮换 API Key"""
        # 在实际应用中，这里会从密钥管理服务获取新 Key
        print(f"轮换 {service} 的 API Key...")

        key_info = self.keys[service]
        key_info["previous"] = key_info["current"]
        # 这里应该从安全的地方获取新 Key
        # key_info["current"] = get_new_key_from_vault(service)
        key_info["created_at"] = datetime.now()

        # 记录历史
        self.key_history.append({
            "service": service,
            "rotated_at": datetime.now(),
            "old_key": key_info["previous"][:10] + "..." if key_info["previous"] else None
        })

# 使用示例
key_manager = APIKeyManager()
openai_key = key_manager.get_key("openai")
print(f"OpenAI Key: {openai_key[:10]}...")
```


---


## 开发工具推荐


选择合适的开发工具可以大幅提高开发效率。以下是一些推荐的开发工具。


### 1. 代码编辑器/IDE


#### Visual Studio Code（推荐）


**下载地址**：[https://code.visualstudio.com/](https://code.visualstudio.com/)


**推荐扩展**：


- **Python**：Python 语言支持
- **Pylance**：高级 Python 语言服务器
- **Jupyter**：Jupyter 笔记本支持
- **GitLens**：Git 增强功能
- **Prettier**：代码格式化
- **Code Spell Checker**：拼写检查
- **Rainbow CSV**：CSV 文件高亮
- **Thunder Client**：API 测试工具


**VS Code 配置**（`.vscode/settings.json`）：


```
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "88"
    ],
    "python.testing.pytestEnabled": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "always"
        }
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/.venv": true,
        "**/venv": true
    }
}
```


#### PyCharm（专业版）


**下载地址**：[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)


**特点**：


- 专业的 Python IDE
- 强大的调试功能
- 数据库工具集成
- 科学计算支持


### 2. 版本控制：Git


Git 是必不可少的版本控制工具。


**基础配置**：


```
# 配置用户信息
git config --global user.name "你的姓名"
git config --global user.email "你的邮箱"

# 配置默认编辑器（可选）
git config --global core.editor "code --wait"

# 创建 Git 仓库
cd ai-agent-project
git init

# 添加所有文件
git add .

# 提交
git commit -m "初始提交：AI Agent 项目"

# 连接到远程仓库（如 GitHub）
git remote add origin https://github.com/你的用户名/ai-agent-project.git
git branch -M main
git push -u origin main
```


### 3. 调试工具


#### Python 调试器（pdb）


```
# 在代码中插入断点
import pdb

def complex_function(x):
    pdb.set_trace()  # 这里会进入调试器
    result = x * 2
    return result

# 常用 pdb 命令：
# n(ext) - 执行下一行
# s(tep) - 进入函数
# c(ontinue) - 继续执行
# l(ist) - 显示代码
# p(rint) - 打印变量值
# q(uit) - 退出调试器
```


#### VS Code 调试配置


`.vscode/launch.json`：


```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "Python: 测试",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/tests",
            "console": "integratedTerminal",
            "justMyCode": true,
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```


### 4. 测试工具


#### pytest


```
# tests/test_agent.py
import pytest
from src.agents.base_agent import BaseAgent

def test_agent_initialization():
    """测试 Agent 初始化"""
    agent = BaseAgent(name="测试Agent")
    assert agent.name == "测试Agent"
    assert agent.messages == []

def test_agent_add_message():
    """测试添加消息"""
    agent = BaseAgent()
    agent.add_message("user", "你好")

    assert len(agent.messages) == 1
    assert agent.messages[0]["role"] == "user"
    assert agent.messages[0]["content"] == "你好"
```


运行测试：


```
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_agent.py

# 运行特定测试函数
pytest tests/test_agent.py::test_agent_initialization

# 显示详细输出
pytest -v

# 显示覆盖率报告
pytest --cov=src
```


### 5. 代码质量和格式化


#### black（代码格式化）


```
# 格式化所有 Python 文件
black .

# 检查哪些文件需要格式化
black --check .

# 格式化单个文件
black src/agents/base_agent.py
```


#### flake8（代码检查）


```
# 检查代码质量
flake8 src/

# 忽略特定错误
flake8 --ignore=E501,W503 src/

# 显示错误统计
flake8 --statistics src/
```


#### pre-commit（Git 钩子）


创建 `.pre-commit-config.yaml`：


```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: [--max-line-length=88]
```


安装 pre-commit：


```
pip install pre-commit
pre-commit install
```


### 6. 文档工具


#### Jupyter Notebook


用于实验和文档：


```
# 启动 Jupyter
jupyter notebook

# 或使用 JupyterLab
jupyter lab
```


#### MkDocs（文档生成）


创建 `docs/` 目录和 `mkdocs.yml`：


```
site_name: AI Agent 项目文档
site_url: https://your-project.com
nav:
  - 首页: index.md
  - API文档: api.md
  - 使用指南: guide.md
theme: readthedocs
```


生成文档：


```
# 安装 MkDocs
pip install mkdocs mkdocs-material

# 本地预览
mkdocs serve

# 构建文档
mkdocs build
```


### 7. 容器化工具（可选）


#### Docker


`Dockerfile`：


```
FROM python:3.9-slim

WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY src/ ./src/
COPY .env.example .env

# 设置环境变量
ENV PYTHONPATH=/app

# 运行应用
CMD ["python", "src/main.py"]
```


`docker-compose.yml`：


```
version: '3.8'

services:
  ai-agent:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
```


### 8. 监控和日志


#### loguru（日志库）


```
from loguru import logger
import sys

# 配置日志
logger.remove()  # 移除默认处理器
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

logger.add(
    "logs/app_{time}.log",
    rotation="500 MB",  # 每500MB轮转
    retention="30 days",  # 保留30天
    compression="zip",  # 压缩旧日志
    level="DEBUG"
)

# 使用日志
logger.info("应用启动")
logger.debug(f"配置加载: {config}")
logger.error("API调用失败", exc_info=True)
```









	  AI 思考中...





			** [记忆系统设计](https://www.runoob.com/ai-agent-memory-system-design.html)
			[AI Agent 问答实例](https://www.runoob.com/ai-agent-answer-demo.html) **













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