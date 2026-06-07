# 工具调用（Function Calling）

- Source: https://www.runoob.com/ai-agent/ai-agent-function-calling.html

Function Calling（函数调用）是让 LLM 能够使用外部工具的核心机制。

Function Calling（函数调用）允许模型决定何时调用工具、调用哪个工具，以及传递什么参数。


### 为什么需要 Function Calling？


想象一下，LLM 是一个聪明但手无寸铁的顾问。它知道很多知识，但不能：


- 获取实时信息（如最新天气、股票价格）
- 执行计算（如复杂的数学运算）
- 操作外部系统（如发送邮件、读写文件）


Function Calling 为 LLM 提供了双手，让它能够突破自身限制，执行实际任务。


### Function Calling 的工作原理


Function Calling 的基本流程如下：


![](https://www.runoob.com/wp-content/uploads/2026/02/runoob-funcall-runoob-scaled.png)


### 核心概念


- **工具定义**：描述一个工具的功能、参数和返回值
- **工具选择**：LLM 根据用户问题选择合适的工具
- **参数提取**：LLM 从问题中提取工具所需的参数
- **结果处理**：将工具执行结果整合到最终回答中


### 实例说明


假设我们有一个查询天气的工具，当用户问**北京今天天气如何？**时：


- LLM 识别出需要调用天气查询工具
- 从问题中提取参数：`city="北京"`, `date="今天"`
- 调用天气 API 获取数据
- 将天气数据整合成友好的回答返回给用户


---


## 工具定义与描述编写


要让 LLM 正确使用工具，首先需要清晰地定义工具，好的工具定义应该像一份清晰的说明书，让 LLM 明白：


- 这个工具是做什么的？
- 什么时候使用它？
- 需要什么参数？
- 参数是什么格式？


### 工具定义的结构


一个完整的工具定义通常包含以下部分：


## 实例


```
# 工具定义示例结构
weather_tool = {
    "name": "get_weather",  # 工具名称
    "description": "获取指定城市的天气信息",  # 工具描述
    "parameters": {  # 参数定义
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "城市名称，如'北京'、'上海'"
            },
            "date": {
                "type": "string",
                "description": "日期，格式'YYYY-MM-DD'，或'今天'、'明天'",
                "enum": ["今天", "明天", "后天"]
            }
        },
        "required": ["city"]  # 必填参数
    }
}
```


### 编写优质的工具描述


#### 1. 描述要清晰具体


- **不好的描述**：查询天气
- **好的描述**：获取指定城市在特定日期的天气信息，包括温度、湿度、风速和天气状况（晴、雨、多云等）


#### 2. 参数描述要详细


**不好的参数描述**：


```
"city": {"type": "string"}
```


**好的参数描述：**


```
"city": {
    "type": "string",
    "description": "完整的城市名称，如'北京市'、'上海市'。不要使用简称或拼音。"
}
```


#### 3. 使用枚举限制选项


对于有限的选项，使用枚举（enum）帮助 LLM 理解：


```
"unit": {
    "type": "string",
    "description": "温度单位",
    "enum": ["celsius", "fahrenheit"],
    "default": "celsius"
}
```


#### 4. 提供示例值


在描述中提供示例，帮助 LLM 理解格式：


```
"date": {
    "type": "string",
    "description": "日期，格式应为'YYYY-MM-DD'，例如'2024-06-15'"
}
```


### 实用工具定义示例


#### 1. 计算器工具


```
calculator_tool = {
    "name": "calculate",
    "description": "执行数学计算，支持加减乘除、幂运算等基本运算",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "数学表达式，如'2 + 3 * 4'、'sqrt(16)'、'sin(30)'"
            }
        },
        "required": ["expression"]
    }
}
```


#### 2. 搜索工具


```
search_tool = {
    "name": "search_web",
    "description": "在互联网上搜索最新信息",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "搜索关键词，尽量具体明确"
            },
            "num_results": {
                "type": "integer",
                "description": "返回结果数量，默认为5",
                "default": 5,
                "minimum": 1,
                "maximum": 10
            }
        },
        "required": ["query"]
    }
}
```


#### 3. 文件操作工具


```
file_tool = {
    "name": "read_file",
    "description": "读取指定文件的内容",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "文件的完整路径，如'/home/user/document.txt'"
            },
            "encoding": {
                "type": "string",
                "description": "文件编码，默认为'utf-8'",
                "default": "utf-8"
            }
        },
        "required": ["file_path"]
    }
}
```


### 工具定义的最佳实践


- **名称简洁明确**：使用动词开头，如 `get_`、`calculate_`、`search_`
- **描述完整详细**：说明工具的用途、适用场景和限制
- **参数验证充分**：定义参数类型、范围、格式要求
- **提供默认值**：为可选参数提供合理的默认值
- **考虑错误情况**：在描述中说明可能出现的错误和限制


### 工具定义的验证


定义工具后，应该进行验证测试：


```
def validate_tool_definition(tool_def):
    """验证工具定义是否完整"""
    required_fields = ["name", "description", "parameters"]

    for field in required_fields:
        if field not in tool_def:
            return False, f"缺少必要字段: {field}"

    # 检查参数结构
    if "properties" not in tool_def["parameters"]:
        return False, "参数定义缺少properties字段"

    return True, "工具定义完整"

# 测试验证
is_valid, message = validate_tool_definition(weather_tool)
print(f"验证结果: {is_valid}, 消息: {message}")
```


---


## 参数提取与验证


LLM 从用户问题中提取参数后，需要对这些参数进行验证和处理，确保工具能够正确执行。


### 参数提取过程


当 LLM 决定调用工具时，它会分析用户输入，提取出工具所需的参数：


```
用户输入: "查询北京明天的天气温度"
工具: get_weather
提取参数: {"city": "北京", "date": "明天"}
```


### 参数提取的挑战


参数提取可能遇到以下问题：


- **信息缺失**：用户没有提供所有必要信息
- **格式不符**：用户提供的格式与工具要求不符
- **歧义解析**：同一信息可能有多种解释
- **上下文依赖**：参数需要结合对话历史理解


### 参数验证方法


#### 1. 类型验证


确保参数类型符合要求：


```
def validate_parameters(params, tool_def):
    """验证参数类型"""
    errors = []

    for param_name, param_def in tool_def["parameters"]["properties"].items():
        if param_name in params:
            param_value = params[param_name]
            expected_type = param_def.get("type")

            # 类型检查
            if expected_type == "string" and not isinstance(param_value, str):
                errors.append(f"参数'{param_name}'应为字符串类型")
            elif expected_type == "integer" and not isinstance(param_value, int):
                errors.append(f"参数'{param_name}'应为整数类型")
            elif expected_type == "number" and not isinstance(param_value, (int, float)):
                errors.append(f"参数'{param_name}'应为数字类型")
            elif expected_type == "boolean" and not isinstance(param_value, bool):
                errors.append(f"参数'{param_name}'应为布尔类型")

    return errors
```


```


#### 2. 范围验证


检查参数值是否在允许范围内：


```
def validate_range(params, tool_def):
    """验证参数范围"""
    errors = []

    for param_name, param_def in tool_def["parameters"]["properties"].items():
        if param_name in params:
            param_value = params[param_name]

            # 检查最小值
            if "minimum" in param_def and param_value < param_def["minimum"]:
                errors.append(f"参数'{param_name}'不能小于{param_def['minimum']}")

            # 检查最大值
            if "maximum" in param_def and param_value > param_def["maximum"]:
                errors.append(f"参数'{param_name}'不能大于{param_def['maximum']}")

            # 检查枚举值
            if "enum" in param_def and param_value not in param_def["enum"]:
                errors.append(f"参数'{param_name}'必须是{param_def['enum']}中的一个")

    return errors
```


#### 3. 必填参数验证


确保所有必填参数都已提供：


```
def validate_required(params, tool_def):
    """验证必填参数"""
    errors = []
    required_params = tool_def["parameters"].get("required", [])

    for param_name in required_params:
        if param_name not in params:
            errors.append(f"缺少必填参数: {param_name}")

    return errors
```


### 完整的参数验证系统


## 实例


```
class ParameterValidator:
    """参数验证器"""

    def __init__(self, tool_def):
        self.tool_def = tool_def

    def validate(self, params):
        """执行完整的参数验证"""
        all_errors = []

        # 检查必填参数
        required_errors = self.validate_required(params)
        all_errors.extend(required_errors)

        # 检查参数类型
        type_errors = self.validate_type(params)
        all_errors.extend(type_errors)

        # 检查参数范围
        range_errors = self.validate_range(params)
        all_errors.extend(range_errors)

        # 检查额外参数（未定义的参数）
        extra_errors = self.validate_extra(params)
        all_errors.extend(extra_errors)

        return len(all_errors) == 0, all_errors

    def validate_required(self, params):
        """验证必填参数"""
        errors = []
        required_params = self.tool_def["parameters"].get("required", [])

        for param_name in required_params:
            if param_name not in params or params[param_name] is None:
                errors.append(f"缺少必填参数: {param_name}")

        return errors

    def validate_type(self, params):
        """验证参数类型"""
        errors = []

        for param_name, param_value in params.items():
            if param_name in self.tool_def["parameters"]["properties"]:
                param_def = self.tool_def["parameters"]["properties"][param_name]
                expected_type = param_def.get("type")

                if expected_type == "string" and not isinstance(param_value, str):
                    errors.append(f"参数'{param_name}'应为字符串类型，实际为{type(param_value).__name__}")
                elif expected_type == "integer" and not isinstance(param_value, int):
                    errors.append(f"参数'{param_name}'应为整数类型，实际为{type(param_value).__name__}")
                elif expected_type == "number" and not isinstance(param_value, (int, float)):
                    errors.append(f"参数'{param_name}'应为数字类型，实际为{type(param_value).__name__}")
                elif expected_type == "boolean" and not isinstance(param_value, bool):
                    errors.append(f"参数'{param_name}'应为布尔类型，实际为{type(param_value).__name__}")

        return errors

    def validate_range(self, params):
        """验证参数范围"""
        errors = []

        for param_name, param_value in params.items():
            if param_name in self.tool_def["parameters"]["properties"]:
                param_def = self.tool_def["parameters"]["properties"][param_name]

                # 检查最小值
                if "minimum" in param_def and param_value < param_def["minimum"]:
                    errors.append(f"参数'{param_name}'不能小于{param_def['minimum']}")

                # 检查最大值
                if "maximum" in param_def and param_value > param_def["maximum"]:
                    errors.append(f"参数'{param_name}'不能大于{param_def['maximum']}")

                # 检查枚举值
                if "enum" in param_def and param_value not in param_def["enum"]:
                    errors.append(f"参数'{param_name}'必须是{param_def['enum']}中的一个")

        return errors

    def validate_extra(self, params):
        """检查未定义的额外参数"""
        errors = []
        defined_params = set(self.tool_def["parameters"]["properties"].keys())
        provided_params = set(params.keys())

        extra_params = provided_params - defined_params
        if extra_params:
            errors.append(f"提供了未定义的参数: {', '.join(extra_params)}")

        return errors

# 使用示例
validator = ParameterValidator(weather_tool)
params = {"city": "北京", "date": "明天", "extra": "不应该有的参数"}
is_valid, errors = validator.validate(params)

if is_valid:
    print("参数验证通过")
else:
    print("参数验证失败:")
    for error in errors:
        print(f"  - {error}")
```


### 参数提取与验证的完整流程


![](https://www.runoob.com/wp-content/uploads/2026/02/runoob-funcall-runoob-2-scaled.png)


### 参数修正策略


当参数验证失败时，可以采取以下策略：


- **询问用户**：直接向用户询问缺失或错误的参数
- **使用默认值**：对于可选参数，使用预定义的默认值
- **智能推断**：根据上下文推断合理的参数值
- **格式转换**：将用户提供的格式转换为工具要求的格式


```
def fix_parameters(params, errors, tool_def):
    """尝试修正参数错误"""
    fixed_params = params.copy()

    for error in errors:
        if "缺少必填参数" in error:
            param_name = error.split(": ")[1]
            # 尝试从上下文推断或使用默认值
            if param_name == "date":
                fixed_params[param_name] = "今天"  # 使用当天作为默认值

        elif "应为字符串类型" in error:
            param_name = error.split("'")[1]
            # 尝试转换为字符串
            fixed_params[param_name] = str(params[param_name])

    return fixed_params
```


---


## 错误处理与重试机制


在实际应用中，工具调用可能会失败。健全的错误处理和重试机制是构建可靠 AI Agent 的关键。


###







	  AI 思考中...





			** [大语言模型基础（LLM）](https://www.runoob.com/ai-agent-llm.html)
			[记忆系统设计](https://www.runoob.com/ai-agent-memory-system-design.html) **













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