# AI Agent 垂直应用场景

- Source: https://www.runoob.com/ai-agent/vertical-applications.html

不同领域对 Agent 有不同的需求和特点。


通过领域定制，Agent 能够提供更专业的服务。


---


## 代码 Agent


代码 Agent 是当前最成功的 Agent 应用领域之一。


能够理解代码库、编写新代码、调试问题。


### 核心能力


**代码补全**：根据上下文预测下一段代码。


**代码生成**：根据自然语言描述生成代码。


**代码审查**：发现代码中的问题和改进点。


**Bug 定位**：分析错误信息，定位问题根源。


**代码重构**：提出并执行代码优化建议。


### 代表系统


| 系统 | 开发公司 | 特点 |
| --- | --- | --- |
| GitHub Copilot | GitHub/OpenAI | 代码补全为主，实时建议 |
| Claude Code | Anthropic | 命令行助手，深度代码理解 |
| Devin | Cognition | 自主编程，端到端任务执行 |
| Cursor | Cursor | AI 代码编辑器，深度 IDE 集成 |


### 代码实现示例


## Text2SQL Agent 实现


```
class Text2SQLAgent:
    """
    Text2SQL Agent
    将自然语言转换为 SQL 查询
    """

    def __init__(self, llm, schema):
        self.llm = llm
        # 数据库 Schema 信息
        self.schema = schema

    def convert(self, question):
        """
        将自然语言问题转换为 SQL
        :param question: 自然语言问题
        :return: SQL 查询语句
        """
        prompt = f"""
你是一个 SQL 专家。

数据库 Schema：
{self.schema}

规则：
1. 只生成 SELECT 查询（不支持 INSERT/UPDATE/DELETE）
2. 使用合理的表别名
3. 添加必要的 JOIN 条件
4. 使用清晰的列别名

问题：{question}

请生成对应的 SQL 查询。
"""
        sql = self.llm.generate(prompt)

        # 安全检查
        return self.sanitize(sql)

    def sanitize(self, sql):
        """
        SQL 安全检查
        确保不包含危险操作
        """
        # 转小写检查
        sql_lower = sql.lower().strip()

        # 检查是否只包含 SELECT
        forbidden_keywords = [
            "insert", "update", "delete", "drop",
            "create", "alter", "truncate", "exec",
            "execute", "grant", "revoke"
        ]

        for keyword in forbidden_keywords:
            if keyword in sql_lower:
                raise ValueError(f"禁止的关键字: {keyword}")

        return sql

    def execute(self, question, db_connection):
        """
        执行 Text2SQL 查询
        """
        sql = self.convert(question)
        cursor = db_connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return {"columns": columns, "rows": results}
```


---


## 数据分析 Agent


数据分析 Agent 能够理解数据需求，执行查询，生成分析报告。


让非技术人员也能进行复杂的数据分析。


### 核心能力


**数据理解**：理解数据库结构和数据含义。


**查询生成**：Text2SQL，将自然语言转为查询。


**可视化**：生成图表建议和配置。


**报告生成**：分析结果，生成自然语言报告。


### 代码实现


## 数据分析 Agent 实现


```
class DataAnalysisAgent:
    """
    数据分析 Agent
    理解数据需求，执行分析，生成报告
    """

    def __init__(self, llm, db_connection, chart_generator):
        self.llm = llm
        self.db = db_connection
        self.chart_generator = chart_generator

    def analyze(self, request):
        """
        处理数据分析请求
        """
        # 第一步：理解分析需求
        intent = self.parse_intent(request)

        # 第二步：生成查询
        query = self.generate_query(intent)

        # 第三步：执行查询
        data = self.execute_query(query)

        # 第四步：分析数据
        analysis = self.perform_analysis(data, intent)

        # 第五步：生成可视化建议
        charts = self.suggest_charts(analysis)

        # 第六步：生成报告
        report = self.generate_report(analysis, charts)

        return {
            "intent": intent,
            "query": query,
            "data": data,
            "analysis": analysis,
            "charts": charts,
            "report": report
        }

    def parse_intent(self, request):
        """解析用户意图"""
        prompt = f"""
分析以下数据请求，提取关键信息：

请求：{request}

请提取：
1. 分析目标（比较、趋势、分布等）
2. 涉及的表和字段
3. 时间范围（如果有）
4. 筛选条件（如果有）
"""
        return self.llm.generate(prompt)

    def generate_query(self, intent):
        """生成 SQL 查询"""
        prompt = f"""
基于以下意图生成 SQL 查询：

{intent}

数据库 Schema：
{self.get_schema()}
"""
        return self.llm.generate(prompt)

    def execute_query(self, query):
        """执行查询"""
        cursor = self.db.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        return {"columns": columns, "rows": rows}

    def perform_analysis(self, data, intent):
        """执行数据分析"""
        # 简化实现
        import statistics

        rows = data["rows"]
        columns = data["columns"]

        analysis = {
            "row_count": len(rows),
            "summary": {}
        }

        # 对数值列计算统计信息
        for i, col in enumerate(columns):
            if self.is_numeric(rows, i):
                values = [row[i] for row in rows if row[i] is not None]
                if values:
                    analysis["summary"][col] = {
                        "min": min(values),
                        "max": max(values),
                        "avg": statistics.mean(values),
                        "median": statistics.median(values)
                    }

        return analysis

    def suggest_charts(self, analysis):
        """推荐可视化图表"""
        suggestions = []

        # 根据分析类型推荐图表
        if "trend" in str(analysis).lower():
            suggestions.append({
                "type": "line",
                "description": "折线图，适合展示趋势变化"
            })

        if "comparison" in str(analysis).lower():
            suggestions.append({
                "type": "bar",
                "description": "柱状图，适合对比不同类别"
            })

        suggestions.append({
            "type": "table",
            "description": "数据表格，展示详细数据"
        })

        return suggestions

    def generate_report(self, analysis, charts):
        """生成分析报告"""
        prompt = f"""
基于以下分析结果，生成自然语言报告：

分析结果：
{analysis}

推荐图表：
{charts}

请生成一份清晰的分析报告。
"""
        return self.llm.generate(prompt)
```


---


## 客服 Agent


客服 Agent 需要处理多轮对话，理解用户意图，提供准确的回复。


是 AI 落地最广泛的场景之一。


### 核心能力


**意图识别**：理解用户想做什么。


**槽位填充**：提取关键信息（时间、地点等）。


**对话状态跟踪**：管理多轮对话上下文。


**回复生成**：生成自然、专业的回复。


### 代码实现


## 客服 Agent 实现


```
class CustomerServiceAgent:
    """
    客服 Agent
    处理用户咨询，提供服务支持
    """

    def __init__(self, llm, knowledge_base, dialogue_manager):
        self.llm = llm
        # 知识库
        self.knowledge_base = knowledge_base
        # 对话管理器
        self.dialogue_manager = dialogue_manager

    def handle(self, user_input, session_id):
        """
        处理用户消息
        """
        # 获取对话历史
        history = self.dialogue_manager.get_history(session_id)

        # 识别用户意图
        intent = self.recognize_intent(user_input, history)

        # 根据意图处理
        if intent.type == "greeting":
            response = self.handle_greeting()
        elif intent.type == "inquiry":
            response = self.handle_inquiry(intent)
        elif intent.type == "complaint":
            response = self.handle_complaint(intent)
        elif intent.type == "order_status":
            response = self.handle_order_status(intent)
        elif intent.type == "refund":
            response = self.handle_refund(intent)
        else:
            response = self.handle_general(user_input)

        # 更新对话历史
        self.dialogue_manager.add_message(
            session_id,
            {"role": "user", "content": user_input}
        )
        self.dialogue_manager.add_message(
            session_id,
            {"role": "assistant", "content": response}
        )

        return response

    def recognize_intent(self, text, history):
        """识别用户意图"""
        prompt = f"""
分析用户消息，识别意图类型。

当前消息：{text}

对话历史：
{history}

意图类型：
- greeting: 打招呼
- inquiry: 咨询问题
- complaint: 投诉
- order_status: 查订单
- refund: 退款
- goodbye: 道别

请输出意图类型和置信度。
"""
        result = self.llm.generate(prompt)
        return Intent.parse(result)

    def handle_inquiry(self, intent):
        """处理咨询"""
        # 从知识库检索相关内容
        relevant_docs = self.knowledge_base.search(intent.query)

        if relevant_docs:
            # 有相关文档，基于文档回答
            prompt = f"""
基于以下文档回答用户问题。

文档：
{relevant_docs}

问题：{intent.query}
"""
            return self.llm.generate(prompt)
        else:
            # 没有相关文档，转人工或记录
            return "这个问题我需要进一步了解，请稍等我来为您查询。"

class Intent:
    """用户意图"""

    def __init__(self, type, query, confidence):
        self.type = type
        self.query = query
        self.confidence = confidence

    @classmethod
    def parse(cls, text):
        """解析意图文本"""
        # 简化实现
        return cls(type="inquiry", query=text, confidence=0.9)
```


---


## 调研 Agent


调研 Agent 能够自主进行深入调研，搜集和综合信息。


模拟人类研究员的工作方式。


### 核心能力


**搜索规划**：制定信息搜集计划。


**多源搜集**：从多个来源收集信息。


**信息验证**：交叉验证信息准确性。


**报告生成**：综合信息，生成结构化报告。


### 代码实现


## 调研 Agent 实现


```
class ResearchAgent:
    """
    调研 Agent
    自主进行深度调研，生成报告
    """

    def __init__(self, search_tools, llm):
        # 搜索工具列表
        self.search_tools = search_tools
        self.llm = llm

    def research(self, topic, depth=3):
        """
        执行调研任务
        :param topic: 调研主题
        :param depth: 调研深度（搜索轮数）
        """
        # 第一步：制定调研计划
        plan = self.create_research_plan(topic, depth)

        # 第二步：执行多轮搜索
        findings = []
        for phase in plan.phases:
            # 并行搜索多个方向
            phase_results = self.search_phase(phase)
            findings.extend(phase_results)

            # 综合当前发现
            synthesis = self.synthesize(findings)
            findings.append({
                "type": "synthesis",
                "content": synthesis,
                "phase": phase.number
            })

        # 第三步：生成最终报告
        report = self.generate_report(findings)

        return {
            "topic": topic,
            "plan": plan,
            "findings": findings,
            "report": report
        }

    def create_research_plan(self, topic, depth):
        """创建调研计划"""
        prompt = f"""
为以下调研主题制定详细计划：

主题：{topic}
深度：{depth}

请规划：
1. 需要调研的关键方向（3-5 个）
2. 每个方向需要回答的核心问题
3. 信息来源建议
"""
        return ResearchPlan.parse(self.llm.generate(prompt))

    def search_phase(self, phase):
        """执行单个搜索阶段"""
        results = []

        for query in phase.queries:
            # 使用搜索工具搜索
            for tool in self.search_tools:
                search_results = tool.search(query)
                results.extend(search_results)

        return results

    def synthesize(self, findings):
        """综合发现"""
        prompt = f"""
综合以下研究发现，提取关键信息：

发现列表：
{findings}

请提取：
1. 主要结论
2. 支持结论的证据
3. 存在的争议或不确定性
4. 需要进一步调研的问题
"""
        return self.llm.generate(prompt)

    def generate_report(self, findings):
        """生成最终报告"""
        prompt = f"""
基于以下研究发现，生成结构化报告：

研究发现：
{findings}

报告要求：
1. 执行摘要
2. 背景介绍
3. 主要发现（分主题）
4. 结论和建议
5. 参考来源

请生成完整报告。
"""
        return self.llm.generate(prompt)

class ResearchPlan:
    """调研计划"""

    @classmethod
    def parse(cls, text):
        """解析计划文本"""
        # 简化实现
        return cls(phases=[
            ResearchPhase(number=1, queries=["相关主题1"], goals=["了解基本概念"]),
            ResearchPhase(number=2, queries=["相关主题2"], goals=["深入分析"]),
        ])

    def __init__(self, phases):
        self.phases = phases

class ResearchPhase:
    """调研阶段"""

    def __init__(self, number, queries, goals):
        self.number = number
        self.queries = queries
        self.goals = goals
```


---


## 其他垂直应用


### RPA + Agent


RPA（机器人流程自动化）与 Agent 的结合。


能够实现更复杂的业务流程自动化。


Agent 赋予 RPA 智能决策能力。


### 游戏 NPC Agent


游戏中的 NPC（非玩家角色）Agent。


能够进行动态对话、情节生成、角色扮演。


创造更真实的游戏世界体验。


### 科研 Agent


AI for Science 正在改变科学研究。


**文献综述**：自动阅读和总结大量论文。


**实验设计**：提出实验方案和假设。


**数据分析**：处理实验数据，发现规律。


**论文写作**：辅助撰写科研论文。


---


## 章节小结


本章节介绍了 Agent 在各个垂直领域的应用。


**代码 Agent** 辅助编程，提高开发效率。


**数据分析 Agent** 让非技术人员也能分析数据。


**客服 Agent** 提供智能客户服务。


**调研 Agent** 自主进行深度调研。


还有 RPA+Agent、游戏 NPC、科研 Agent 等更多场景。


垂直领域的 Agent 需要结合领域知识进行定制。


选择合适的场景和切入点，是成功落地的关键。









	  AI 思考中...





			** [AI Agent 生产部署与工程化](https://www.runoob.com/production-deployment.html)














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