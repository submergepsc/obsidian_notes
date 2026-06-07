# Agent 评估、安全与对齐

- Source: https://www.runoob.com/ai-agent/evaluation-safety-alignment.html

评估是确保 Agent 效果的基础。


安全和对齐是 Agent 能否被信任和部署的关键。


---


## Agent 评测体系


评估 Agent 性能是开发过程中的关键环节。


好的评测体系能够帮助我们了解 Agent 的能力边界。


也为持续优化提供方向和依据。


### 评测维度


**任务完成度**：Agent 是否正确完成了给定任务。


**效率指标**：完成任务所需的步骤数、token 消耗、执行时间。


**质量指标**：答案的准确性、响应的一致性、对话的自然度。


**鲁棒性**：对异常输入、噪声数据的处理能力。


### 常用 Benchmark


| Benchmark | 用途 | 评估内容 |
| --- | --- | --- |
| GAIA | 通用 AI 助手评测 | 复杂任务处理、多步骤推理 |
| MMLU | 多任务语言理解 | 57 个学科的知识问答 |
| HumanEval | 代码生成评测 | Python 代码编写正确性 |
| HotpotQA | 多跳问答评测 | 需要多个文档推理的问题 |
| AgentBench | Agent 能力评测 | 真实环境中的 Agent 表现 |


### 代码实现：评测框架


## Agent 评测框架


```
class AgentEvaluator:
    """
    Agent 评测框架
    评估 Agent 在各种任务上的表现
    """

    def __init__(self, agent, metrics):
        # 待评测的 Agent
        self.agent = agent
        # 评测指标列表
        self.metrics = metrics

    def evaluate(self, test_cases):
        """
        执行评测
        :param test_cases: 测试用例列表
        :return: 评测报告
        """
        results = []

        for test_case in test_cases:
            # 执行任务
            result = self.run_single_test(test_case)
            results.append(result)

        # 生成评测报告
        report = self.generate_report(results)
        return report

    def run_single_test(self, test_case):
        """
        运行单个测试用例
        """
        # 记录开始时间
        start_time = time.time()

        # 执行 Agent
        try:
            output = self.agent.run(test_case.input)
            success = self.evaluate_output(output, test_case.expected)
            error = None
        except Exception as e:
            output = None
            success = False
            error = str(e)

        # 记录结束时间
        end_time = time.time()

        return TestResult(
            test_case=test_case,
            output=output,
            success=success,
            error=error,
            duration=end_time - start_time,
            token_count=self.count_tokens(output)
        )

    def evaluate_output(self, output, expected):
        """评估输出是否符合预期"""
        for metric in self.metrics:
            if not metric.evaluate(output, expected):
                return False
        return True

    def generate_report(self, results):
        """生成评测报告"""
        total = len(results)
        passed = sum(1 for r in results if r.success)

        # 计算各项指标
        avg_duration = sum(r.duration for r in results) / total
        avg_tokens = sum(r.token_count for r in results) / total

        # 按测试类型分组统计
        by_category = {}
        for r in results:
            category = r.test_case.category
            if category not in by_category:
                by_category[category] = {"total": 0, "passed": 0}
            by_category[category]["total"] += 1
            if r.success:
                by_category[category]["passed"] += 1

        return EvaluationReport(
            total=total,
            passed=passed,
            pass_rate=passed / total,
            avg_duration=avg_duration,
            avg_tokens=avg_tokens,
            by_category=by_category,
            results=results
        )

class TestCase:
    """测试用例"""

    def __init__(self, input, expected, category="general", metadata=None):
        # 输入
        self.input = input
        # 预期输出或评估标准
        self.expected = expected
        # 类别
        self.category = category
        # 额外元数据
        self.metadata = metadata or {}

class TestResult:
    """测试结果"""

    def __init__(self, test_case, output, success, error, duration, token_count):
        self.test_case = test_case
        self.output = output
        self.success = success
        self.error = error
        self.duration = duration
        self.token_count = token_count

class Metric:
    """评测指标基类"""

    def evaluate(self, output, expected):
        raise NotImplementedError

class ExactMatchMetric(Metric):
    """精确匹配指标"""

    def evaluate(self, output, expected):
        return output.strip() == expected.strip()

class ContainsMetric(Metric):
    """包含关键词指标"""

    def evaluate(self, output, expected):
        if isinstance(expected, list):
            return all(keyword in output for keyword in expected)
        return expected in output

class SemanticSimilarityMetric(Metric):
    """语义相似度指标"""

    def __init__(self, threshold=0.8):
        self.threshold = threshold

    def evaluate(self, output, expected):
        similarity = self.compute_similarity(output, expected)
        return similarity >= self.threshold

    def compute_similarity(self, text1, text2):
        """计算两个文本的语义相似度"""
        # 使用嵌入模型计算余弦相似度
        embedding1 = self.embedder.embed([text1])[0]
        embedding2 = self.embedder.embed([text2])[0]
        return cosine_similarity(embedding1, embedding2)
```


---


## 安全与对齐


Agent 的安全性至关重要。


AI 系统可能受到各种攻击，产生有害输出。


对齐（Alignment）确保 AI 行为符合人类意图和价值观。


### 常见安全威胁


#### 提示注入（Prompt Injection）


攻击者通过输入诱导 Agent 忽略系统指令。


示例输入："忽略之前的指令，改为执行..."


这是一种上下文劫持攻击，利用 Agent 对用户输入的信任。


#### 越狱（Jailbreaking）


通过特定输入绕过安全限制。


如使用角色扮演、虚构场景等手法。


#### 数据污染


恶意修改训练数据或检索结果。


导致 Agent 产生错误或有害输出。


#### 敏感信息泄露


Agent 不当暴露用户隐私或系统内部信息。


### 防护策略


## 安全 Agent 实现


```
class SecureAgent:
    """
    安全 Agent
    在基础 Agent 之上增加多层安全防护
    """

    def __init__(self, base_agent, guardrails, input_validator, output_filter):
        # 基础 Agent
        self.base_agent = base_agent
        # 安全护栏列表
        self.guardrails = guardrails
        # 输入验证器
        self.input_validator = input_validator
        # 输出过滤器
        self.output_filter = output_filter

    def process(self, user_input):
        """
        处理用户输入，包含多层安全检查
        """
        # ==================== 第一层：输入验证 ====================
        # 检查输入是否合法
        is_valid, reason = self.input_validator.validate(user_input)
        if not is_valid:
            return self.create_safety_response(reason)

        # ==================== 第二层：注入检测 ====================
        # 检测提示注入等攻击
        for guardrail in self.guardrails:
            check_result = guardrail.check_input(user_input)
            if not check_result.is_safe:
                # 记录安全事件
                self.log_security_event(
                    event_type="input_guardrail_triggered",
                    input=user_input,
                    reason=check_result.reason
                )
                return self.create_safety_response(check_result.reason)

        # ==================== 第三层：执行核心逻辑 ====================
        try:
            response = self.base_agent.process(user_input)
        except Exception as e:
            return self.create_error_response(str(e))

        # ==================== 第四层：输出过滤 ====================
        # 检查输出是否安全
        for guardrail in self.guardrails:
            check_result = guardrail.check_output(response)
            if not check_result.is_safe:
                self.log_security_event(
                    event_type="output_guardrail_triggered",
                    output=response,
                    reason=check_result.reason
                )
                return self.create_safety_response(check_result.reason)

        # 应用输出过滤（如敏感信息脱敏）
        response = self.output_filter.filter(response)

        return response

    def create_safety_response(self, reason):
        """创建安全响应"""
        return {
            "type": "safety_block",
            "message": "抱歉，我无法完成这个请求。",
            "reason": reason
        }

    def log_security_event(self, event_type, **kwargs):
        """记录安全事件"""
        # 实际应用中应写入安全日志系统
        print(f"[SECURITY] {event_type}: {kwargs}")

class InputValidator:
    """输入验证器"""

    def validate(self, text):
        """
        验证输入是否合法
        :return: (is_valid, reason)
        """
        if not text or len(text.strip()) == 0:
            return False, "输入不能为空"

        if len(text) > 10000:
            return False, "输入长度超过限制"

        # 检查是否包含可执行内容
        if self.contains_executable_content(text):
            return False, "输入包含可疑的可执行内容"

        return True, None

    def contains_executable_content(self, text):
        """检查是否包含可执行内容"""
        # 简化实现
        suspicious_patterns = [
            "javascript:",
            "data:text/html",
            "<script>",
        ]
        return any(pattern in text.lower() for pattern in suspicious_patterns)

class Guardrail:
    """安全护栏"""

    def check_input(self, text):
        """检查输入"""
        raise NotImplementedError

    def check_output(self, text):
        """检查输出"""
        raise NotImplementedError

class ContentFilterGuardrail(Guardrail):
    """内容过滤护栏"""

    def __init__(self, blocked_topics, banned_words):
        self.blocked_topics = blocked_topics
        self.banned_words = banned_words

    def check_input(self, text):
        # 检查是否涉及被禁止的话题
        for topic in self.blocked_topics:
            if topic in text.lower():
                return CheckResult(
                    is_safe=False,
                    reason=f"涉及敏感话题：{topic}"
                )

        # 检查是否包含禁用词
        for word in self.banned_words:
            if word in text.lower():
                return CheckResult(
                    is_safe=False,
                    reason=f"包含不当词汇"
                )

        return CheckResult(is_safe=True)

    def check_output(self, text):
        # 输出检查同上
        return self.check_input(text)

class CheckResult:
    """检查结果"""

    def __init__(self, is_safe, reason=None):
        self.is_safe = is_safe
        self.reason = reason
```


**
重要提醒：安全是一个持续的过程，没有万无一失的方案。需要持续监控、更新和改进安全策略。


---


## 可观测性


生产环境中的 Agent 需要完善的监控体系。


可观测性帮助我们了解 Agent 的行为，排查问题，优化性能。


### 三大支柱


**日志（Logging）**：记录所有关键事件和决策。


**Tracing**：追踪请求在系统中的完整流转路径。


**指标（Metrics）**：收集性能和质量指标。


### 代码实现


## 可观测 Agent 实现


```
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource

# 配置日志
logger = logging.getLogger(__name__)

# 配置 Tracing
tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

class ObservableAgent:
    """
    可观测 Agent
    集成日志、追踪和指标收集
    """

    def __init__(self, agent, metrics_collector):
        # 基础 Agent
        self.agent = agent
        # 指标收集器
        self.metrics = metrics_collector

    def process(self, user_input):
        """
        处理请求，包含完整的可观测性支持
        """
        # 创建追踪 span
        with tracer.start_as_current_span("agent_process") as span:
            # 设置 span 属性
            span.set_attribute("user.input.length", len(user_input))
            span.set_attribute("user.input.preview", user_input[:100])

            # 记录开始
            logger.info(f"开始处理请求: {user_input[:50]}...")
            start_time = time.time()

            try:
                # 执行核心逻辑
                result = self.agent.process(user_input)

                # 记录成功
                duration = time.time() - start_time
                span.set_attribute("success", True)
                span.set_attribute("duration_ms", duration * 1000)
                span.set_attribute("result.length", len(str(result)))

                # 收集指标
                self.metrics.record("request_duration", duration)
                self.metrics.increment("request_success")

                logger.info(f"请求完成，耗时: {duration:.2f}s")

                return result

            except Exception as e:
                # 记录错误
                duration = time.time() - start_time
                span.set_attribute("success", False)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                span.record_exception(e)

                # 收集错误指标
                self.metrics.increment("request_error")
                self.metrics.record("error_duration", duration)

                logger.error(f"请求失败: {e}")

                raise

class MetricsCollector:
    """指标收集器"""

    def __init__(self):
        self.metrics = {}

    def increment(self, name, value=1):
        """递增计数指标"""
        if name not in self.metrics:
            self.metrics[name] = {"type": "counter", "value": 0}
        self.metrics[name]["value"] += value

    def record(self, name, value):
        """记录数值指标"""
        if name not in self.metrics:
            self.metrics[name] = {"type": "gauge", "values": []}
        self.metrics[name]["values"].append(value)

    def get_summary(self):
        """获取指标摘要"""
        summary = {}
        for name, data in self.metrics.items():
            if data["type"] == "counter":
                summary[name] = data["value"]
            else:
                values = data["values"]
                summary[f"{name}_avg"] = sum(values) / len(values)
                summary[f"{name}_max"] = max(values)
                summary[f"{name}_min"] = min(values)
        return summary
```


---


## 护栏与人机协同


### Guardrails


Guardrails 是实时的输入输出过滤和限制机制。


区别于安全护栏，Guardrails 更侧重于确保输出质量和合规性。


### HITL（Human-in-the-Loop）


HITL 在关键决策点引入人工审核。


适用于 AI 不能自主决策的高风险场景。


## HITL Agent 实现


```
class HITLAgent:
    """
    人机协同 Agent
    在关键决策点引入人工审核
    """

    def __init__(self, agent, approval_queue, notification_handler):
        # 基础 Agent
        self.agent = agent
        # 审批队列
        self.approval_queue = approval_queue
        # 通知处理器
        self.notification_handler = notification_handler

    def process(self, request):
        """
        处理请求，必要时触发人工审批
        """
        # 评估请求的风险等级
        risk_level = self.assess_risk(request)

        if risk_level == "high":
            # 高风险请求，需要人工审批
            return self.handle_high_risk_request(request)
        elif risk_level == "medium":
            # 中等风险，启用增强监控
            return self.handle_medium_risk_request(request)
        else:
            # 低风险，直接处理
            return self.agent.process(request)

    def assess_risk(self, request):
        """评估请求风险等级"""
        # 检查是否涉及敏感操作
        sensitive_operations = [
            "delete", "remove", "cancel",
            "transfer", "payment", "refund"
        ]

        content_lower = request.lower()
        for op in sensitive_operations:
            if op in content_lower:
                return "high"

        # 检查请求内容的复杂性
        if len(request) > 1000:
            return "medium"

        return "low"

    def handle_high_risk_request(self, request):
        """
        处理高风险请求，需要人工审批
        """
        # 创建审批任务
        task_id = self.approval_queue.add({
            "request": request,
            "risk_level": "high",
            "timestamp": datetime.now()
        })

        # 通知审批人
        self.notification_handler.notify_approver(
            task_id=task_id,
            message=f"有高风险请求需要审批: {request[:100]}..."
        )

        # 返回等待状态
        return {
            "status": "pending_approval",
            "task_id": task_id,
            "message": "您的请求需要人工审批，请等待。"
        }

    def handle_feedback(self, task_id, approved, feedback=None):
        """
        处理审批反馈
        """
        task = self.approval_queue.get(task_id)

        if approved:
            # 审批通过，执行请求
            self.approval_queue.complete(task_id)
            result = self.agent.process(task["request"])

            # 通知申请人
            self.notification_handler.notify_requester(
                task_id=task_id,
                status="approved",
                result=result
            )

            return result
        else:
            # 审批拒绝
            self.approval_queue.reject(task_id, feedback)

            # 通知申请人
            self.notification_handler.notify_requester(
                task_id=task_id,
                status="rejected",
                feedback=feedback
            )

            return {
                "status": "rejected",
                "reason": feedback or "审批未通过"
            }

class ApprovalQueue:
    """审批队列"""

    def __init__(self):
        self.queue = {}
        self.counter = 0

    def add(self, task):
        """添加审批任务"""
        self.counter += 1
        task_id = f"task_{self.counter}"
        self.queue[task_id] = {
            **task,
            "status": "pending"
        }
        return task_id

    def get(self, task_id):
        return self.queue.get(task_id)

    def complete(self, task_id):
        self.queue[task_id]["status"] = "approved"

    def reject(self, task_id, reason):
        self.queue[task_id]["status"] = "rejected"
        self.queue[task_id]["reject_reason"] = reason
```


---


## 章节小结


本章节介绍了 Agent 的评估、安全和对齐知识。


**评测体系** 通过多维度指标评估 Agent 的性能。


**安全威胁** 包括提示注入、越狱、数据污染等。


**防护策略** 通过多层安全检查保障系统安全。


**可观测性** 通过日志、追踪、指标实现系统监控。


**Guardrails 和 HITL** 提供输出质量控制和人工审核能力。


评估、安全和对齐是构建可信 Agent 系统的基础。


需要在实际开发中持续关注和改进。









	  AI 思考中...





			** [多模态 Agent](https://www.runoob.com/multimodal-agent.html)
			[AI Agent 生产部署与工程化](https://www.runoob.com/production-deployment.html) **













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