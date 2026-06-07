# Python 实现推理与规划

- Source: https://www.runoob.com/ai-agent/python-reasoning-planning.html

本章节介绍 AI Agent 的核心智能能力，即推理与规划能力。


不同于传统的指令执行模式，具备推理能力的 Agent 能够进行复杂的思考过程。


它能够将复杂任务分解为可执行的步骤，并基于上下文做出决策。


---


## ReAct 框架


ReAct（Reasoning + Acting）是一种将推理与行动相结合的框架。


在 ReAct 模式中，Agent 会交替进行推理和行动，形成一个闭环。


推理指导行动，行动结果又反馈给推理过程，如此循环往复。


ReAct 模拟了人类的问题解决过程：在采取行动前先思考，行动后观察结果，然后基于新信息继续推理。


### 工作原理


ReAct 的核心思想可以概括为三个阶段的循环：


第一步，推理阶段。Agent 基于当前上下文生成下一步的行动思考。


第二步，行动阶段。Agent 执行选定的工具或动作。


第三步，观察阶段。Agent 接收行动结果，更新上下文，返回第一步继续推理。


### 代码实现


下面是一个 ReAct Agent 的简化实现：


## ReAct Agent 基本实现


```
class ReActAgent:
    """
    ReAct 框架的 Agent 实现
    核心机制：推理 -> 行动 -> 观察 -> 推理（循环）
    """

    def __init__(self, llm, tools, max_iterations=5):
        # LLM 实例，用于推理和生成
        self.llm = llm
        # 可用工具列表
        self.tools = tools
        # 最大迭代次数，防止无限循环
        self.max_iterations = max_iterations

    def run(self, task):
        """
        执行 ReAct 循环
        :param task: 用户任务描述
        :return: 执行结果
        """
        # 初始化上下文，包含任务和历史信息
        context = {
            "task": task,
            "steps": [],      # 已执行步骤的记录
            "observations": []  # 观察结果的记录
        }

        for i in range(self.max_iterations):
            # 阶段一：推理 - 基于当前上下文生成下一步行动
            reasoning = self.llm.reason(context)

            # 判断是否需要执行工具，还是直接返回答案
            if reasoning.needs_action:
                # 选择要使用的工具
                action = reasoning.select_tool(self.tools)
                # 执行工具并获取观察结果
                observation = action.execute(reasoning.tool_input)
                # 将观察结果添加到上下文
                context["observations"].append(observation)
            else:
                # 不需要行动，直接返回推理得出的答案
                return reasoning.answer

        # 达到最大迭代次数仍未完成
        return "达到最大迭代次数限制"
```


### 典型应用场景


ReAct 模式特别适合以下场景：


需要在环境中探索、收集信息后才能完成的任务。


智能搜索场景：Agent 需要先搜索信息，再基于搜索结果进行推理和总结。


对话式问答：Agent 需要通过多轮对话澄清需求并获取信息。


复杂问题求解：问题不能一步解决，需要多个中间步骤。


**
注意：ReAct 模式的优势在于它的灵活性，能够根据每一步的执行结果动态调整后续行动。但这也意味着执行路径可能不稳定，适合需要探索的任务。


---


## 思维链（Chain of Thought, CoT）


思维链是一种促使模型展示逐步推理过程的技术。


CoT 不是让模型直接给出答案，而是引导它先展示推理步骤，再得出最终结论。


### 为什么需要思维链


直接让模型输出答案存在几个问题：


复杂推理的中间步骤容易被忽略或跳过。


难以定位错误发生在哪里。


用户无法理解模型的思考过程。


思维链通过要求模型展示推理过程，解决了这些问题。


### Zero-shot CoT


Zero-shot CoT 是一种无需示例即可激发逐步推理能力的方法。


只需要在提示词末尾添加 "让我们一步一步地思考" 这样的触发语句。


## Zero-shot CoT 示例


```
# Zero-shot CoT 的提示词模板
prompt = """
问题：小明有 5 个苹果，小红给了他 3 个，小明吃掉了 2 个，还剩多少个？
让我们一步一步地思考：
"""

# 调用语言模型
response = llm.generate(prompt)

# 模型输出示例：
# 第一步：计算小明收到苹果后的总数
# 小明原来有 5 个苹果，小红给了他 3 个
# 5 + 3 = 8 个
#
# 第二步：计算吃掉后的数量
# 小明吃掉了 2 个
# 8 - 2 = 6 个
#
# 结论：还剩 6 个苹果
```


### Few-shot CoT


Few-shot CoT 通过提供包含详细推理过程的示例，帮助模型学习特定的推理模式。


当 Zero-shot CoT 效果不佳时，可以尝试 Few-shot CoT。


## Few-shot CoT 示例


```
# Few-shot CoT 的提示词模板
prompt = """
示例 1：
问题：小张有 10 元钱，买了 3 本书，每本 2 元，还剩多少？
让我们一步一步地思考：
- 小张原来有 10 元
- 每本书 2 元，买了 3 本，花费 3 × 2 = 6 元
- 10 - 6 = 4 元
答案：还剩 4 元

示例 2：
问题：一只猫每小时抓 2 只老鼠，8 小时抓了多少只？
让我们一步一步地思考：
- 每小时抓 2 只老鼠
- 8 小时抓了 8 × 2 = 16 只
答案：抓了 16 只

问题：{user_question}
让我们一步一步地思考：
"""

response = llm.generate(prompt)
```


### 思维链的优势


思维链技术带来三个核心价值：


可追溯性：将复杂推理分解为可追踪的中间步骤，便于理解推理过程。


可解释性：增强模型的可解释性，让用户知道答案从何而来。


准确性提升：显著提升复杂推理任务的准确率，尤其在数学和逻辑任务上效果明显。


---


## Tree of Thoughts（ToT）


思维树是思维链的扩展，它不再局限于线性推理。


ToT 在每个推理节点探索多条可能的路径，形成树状结构。


这使得 Agent 能够进行多路径探索、回溯和全局评估。


### 与思维链的区别


CoT 采用线性推理，每一步依赖前一步的结论，适合有明确路径的问题。


ToT 采用空间推理，同时考虑多个可能的分支，适合需要探索和规划的问题。


### 代码实现


## ToT Agent 基本实现


```
class ToTAgent:
    """
    Tree of Thoughts Agent 实现
    核心机制：在每个节点生成多个候选分支，评估后选择最优继续
    """

    def __init__(self, llm, max_depth=4, beam_size=3):
        # LLM 实例
        self.llm = llm
        # 最大搜索深度
        self.max_depth = max_depth
        # 每层保留的候选节点数量（beam width）
        self.beam_size = beam_size

    def solve(self, problem):
        """
        使用 ToT 框架解决问题
        :param problem: 问题描述
        :return: 最优解
        """
        # 创建根节点，包含问题作为初始状态
        root = ThoughtNode(problem, depth=0)
        # 初始化前沿节点列表（待扩展的节点）
        frontier = [root]

        # 逐层扩展
        for depth in range(self.max_depth):
            # 存储所有候选节点
            all_candidates = []

            # 遍历所有前沿节点
            for node in frontier:
                # 为当前节点生成多个候选下一步
                candidates = self.llm.generate_thoughts(
                    node.content,    # 当前节点内容
                    n=self.beam_size  # 生成数量
                )
                # 创建新节点并加入候选列表
                for cand in candidates:
                    all_candidates.append(
                        ThoughtNode(cand, depth + 1, parent=node)
                    )

            # 评估所有候选节点
            evaluated = self.evaluator.rank(all_candidates)

            # 选择最优的 beam_size 个节点作为下一轮前沿
            frontier = evaluated[:self.beam_size]

            # 检查是否找到解决方案
            if self.is_solution(frontier):
                break

        # 回溯找到最优解
        return self.backtrack_best(frontier)
```


### 应用场景


ToT 特别适合需要做选择或规划的场景：


创意写作：生成多个故事发展方向，评估后选择最优。


战略规划：评估多个行动方案的潜在结果。


复杂决策：需要考虑多种可能性的决策问题。


---


## 任务规划与 MCTS


蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）是一种用于复杂决策问题的启发式搜索算法。


MCTS 在 Agent 规划中有广泛应用，尤其适合游戏 AI 和复杂任务规划。


### 核心思想


MCTS 通过模拟随机游戏来评估每个决策节点的潜在价值。


它不需要评估所有可能的路径，而是通过抽样和统计来指导搜索方向。


### MCTS 的四个步骤


第一步，选择（Selection）：从根节点开始，递归选择最优子节点直到达到叶节点。


选择时使用 UCB（Upper Confidence Bound）公式平衡探索与利用。


第二步，扩展（Expansion）：在叶节点添加一个或多个子节点。


第三步，模拟（Simulation）：从新节点开始，随机模拟游戏直到结束。


第四步，反向传播（Backpropagation）：更新模拟路径上所有节点的统计信息。


### 代码实现


## MCTS 规划器实现


```
import math

class MCTSNode:
    """
    MCTS 树节点
    存储节点状态、统计数据和子节点关系
    """

    def __init__(self, state, parent=None, action=None):
        # 当前状态
        self.state = state
        # 父节点引用
        self.parent = parent
        # 从父节点到达此节点的动作
        self.action = action
        # 子节点列表
        self.children = []
        # 此节点的访问次数
        self.visit_count = 0
        # 此节点的累计奖励值
        self.reward = 0.0

    def is_fully_expanded(self):
        """检查是否已扩展所有可能的子节点"""
        return len(self.children) > 0

    def is_terminal(self):
        """检查是否为终止节点（游戏结束或目标达成）"""
        return self.state.is_terminal()

    def uct_child(self):
        """
        使用 UCT 公式选择最优子节点
        UCT = reward/visits + C * sqrt(ln(parent_visits)/visits)
        C 是探索常数，通常设为 sqrt(2)
        """
        # 探索常数，平衡探索与利用
        C = math.sqrt(2)

        return max(
            self.children,
            key=lambda c: c.reward / c.visit_count +
                         C * math.sqrt(math.log(self.visit_count) / c.visit_count)
        )

class MCTSPlanner:
    """
    MCTS 规划器
    使用蒙特卡洛树搜索为 Agent 生成行动规划
    """

    def __init__(self, simulation_limit=1000, exploration_constant=1.41):
        # 最大模拟次数
        self.simulation_limit = simulation_limit
        # 探索常数
        self.exploration_constant = exploration_constant

    def plan(self, initial_state):
        """
        从初始状态开始规划
        :param initial_state: 初始状态
        :return: 最优动作
        """
        # 创建根节点
        root = MCTSNode(initial_state)

        # 执行多次模拟
        for _ in range(self.simulation_limit):
            # 1. 选择：从根节点向下选择最优子节点直到叶节点
            node = self._selection(root)

            # 2. 扩展：如果不是终止节点，扩展一个新节点
            if not node.is_terminal():
                node = self._expansion(node)

            # 3. 模拟：从新节点开始随机模拟到终止
            reward = self._simulation(node)

            # 4. 反向传播：更新路径上所有节点的统计
            self._backpropagation(node, reward)

        # 返回根节点最优子节点对应的动作
        return root.best_child().action

    def _selection(self, node):
        """选择阶段：选择最优子节点"""
        while node.is_fully_expanded() and not node.is_terminal():
            node = node.uct_child()
        return node

    def _expansion(self, node):
        """扩展阶段：添加新子节点"""
        # 生成所有可能的动作
        possible_actions = node.state.get_possible_actions()
        # 为每个动作创建一个子节点
        for action in possible_actions:
            new_state = node.state.apply_action(action)
            child = MCTSNode(new_state, parent=node, action=action)
            node.children.append(child)
        # 返回随机一个子节点（也可使用确定性策略）
        return node.children[0]

    def _simulation(self, node):
        """模拟阶段：随机模拟到游戏结束"""
        state = node.state
        while not state.is_terminal():
            # 随机选择动作
            actions = state.get_possible_actions()
            action = random.choice(actions)
            state = state.apply_action(action)
        # 返回最终奖励
        return state.get_reward()

    def _backpropagation(self, node, reward):
        """反向传播：更新统计信息"""
        while node is not None:
            node.visit_count += 1
            node.reward += reward
            node = node.parent
```


> 注意：MCTS 的计算成本较高，适合需要深度规划但有明确终止条件的场景。对于实时性要求高的任务，可能需要限制模拟次数或使用其他方法。


---


## Reflexion（自我反思）


Reflexion 是一种让 Agent 具有自我反思能力的技术。


通过为 Agent 添加反思机制，它能够在失败后分析错误原因，调整策略并重试。


### 核心思想


Agent 不仅执行动作，还要观察结果并反思：我为什么失败？下次应该如何改进？


这种能力对于持续学习和自我改进至关重要。


### 代码实现


## Reflexion Agent 实现


```
class ReflexionAgent:
    """
    具有自我反思能力的 Agent
    核心机制：执行 -> 评审 -> 反思 -> 重试
    """

    def __init__(self, actor, reviewer, max_retries=3):
        # 执行器：负责执行具体任务
        self.actor = actor
        # 评审器：负责评估执行结果
        self.reviewer = reviewer
        # 最大重试次数
        self.max_retries = max_retries

    def run(self, task):
        """
        执行带自我反思的任务
        :param task: 任务描述
        :return: 执行结果
        """
        # 维护执行历史
        history = []

        for attempt in range(self.max_retries):
            # 阶段一：尝试执行任务
            result = self.actor.execute(task, history)

            # 记录本次尝试
            history.append({
                "attempt": attempt,
                "result": result
            })

            # 阶段二：评审结果
            feedback = self.reviewer.evaluate(task, result)

            # 阶段三：检查是否成功
            if feedback.is_success:
                return result

            # 阶段四：反思失败原因
            # 生成新的策略提示，指导下一次尝试
            reflection = self.reviewer.reflect(
                task,           # 原始任务
                result,         # 失败结果
                feedback        # 评审反馈
            )

            # 将反思结果添加到历史，供下次尝试参考
            history.append({
                "type": "reflection",
                "content": reflection
            })

        # 所有重试都失败，返回历史记录
        return history

class Reviewer:
    """评审器：评估执行结果并生成反思"""

    def evaluate(self, task, result):
        """
        评估执行结果
        :return: 包含是否成功及详细反馈的对象
        """
        # 检查结果是否满足任务要求
        is_success = self.check_success(task, result)

        if is_success:
            return EvaluationResult(is_success=True)
        else:
            # 生成失败原因分析
            failure_reasons = self.analyze_failures(task, result)
            return EvaluationResult(
                is_success=False,
                reasons=failure_reasons
            )

    def reflect(self, task, result, feedback):
        """
        生成反思内容
        帮助 Actor 理解失败原因并改进策略
        """
        prompt = f"""
任务：{task}
执行结果：{result}
失败原因：{feedback.reasons}

请分析失败原因，并给出改进建议。
重点说明：
1. 哪里出了问题？
2. 下次应该如何避免？
3. 需要改变什么策略？
"""
        return self.llm.generate(prompt)
```


### 应用场景


Reflexion 特别适合以下场景：


需要持续改进的任务，如对话系统、代码生成等。


错误代价高但重试成本低的场景。


需要从失败中学习的情况。


---


## 任务分解策略


复杂任务通常需要分解为可管理的子任务。


有效的任务分解是规划能力的基础。


### 递归任务分解


将任务递归地分解为更小的子任务，直到子任务可以直接执行。


## 递归任务分解


```
def decompose(task, is_executable_fn, decompose_fn):
    """
    递归分解任务
    :param task: 要分解的任务
    :param is_executable_fn: 判断任务是否可直接执行的函数
    :param decompose_fn: 分解任务的函数
    :return: 可执行任务列表
    """
    # 如果任务可以直接执行，直接返回
    if is_executable_fn(task):
        return [task]

    # 分解任务为子任务
    subtasks = decompose_fn(task)

    # 递归分解每个子任务
    result = []
    for subtask in subtasks:
        # 对子任务递归调用分解函数
        result.extend(
            decompose(subtask, is_executable_fn, decompose_fn)
        )

    return result

# 示例：判断任务是否可执行
def is_code_complete(task):
    """检查任务是否可以直接执行代码"""
    return task.get("type") == "code" and len(task.get("dependencies", [])) == 0

# 示例：分解复杂任务
def decompose_programming_task(task):
    """分解编程任务"""
    if "write_function" in task["type"]:
        return [
            {"type": "understand_requirements", "task": task["spec"]},
            {"type": "write_code", "spec": task["spec"]},
            {"type": "write_tests", "function": task["function_name"]},
            {"type": "verify_tests", "function": task["function_name"]}
        ]
    return [task]
```


### 平行任务分解


识别可以并行执行的独立子任务，提高执行效率。


这是加速任务执行的关键策略。


### 层次任务分解


将任务分为不同抽象层次，高层任务调用低层任务，形成任务层次树。


适合需要多层抽象的复杂系统。


---


## Plan-and-Execute 模式


Plan-and-Execute 是一种将规划与执行分离的架构模式。


Agent 首先完整地规划整个任务流程，然后按计划执行。


### 与 ReAct 的区别


ReAct 是边推理边执行，更灵活但路径可能不稳定。


Plan-and-Execute 是先规划后执行，更稳定但缺乏动态调整能力。


### 代码实现


## Plan-and-Execute Agent 实现


```
class PlanAndExecuteAgent:
    """
    Plan-and-Execute 架构的 Agent
    核心机制：先完整规划，再按计划执行
    """

    def __init__(self, planner, executor):
        # 规划器：负责制定执行计划
        self.planner = planner
        # 执行器：负责执行具体步骤
        self.executor = executor

    def run(self, task):
        """
        执行任务
        分为规划阶段和执行阶段
        """
        # ==================== 规划阶段 ====================
        # 一次性生成完整的执行计划
        plan = self.planner.create_plan(task)

        # ==================== 执行阶段 ====================
        results = []

        # 按计划顺序执行
        for step in plan.steps:
            # 执行当前步骤
            result = self.executor.execute(step)
            results.append(result)

            # 检查是否需要重新规划
            # 例如：执行结果与预期不符，或出现意外情况
            if self.needs_replan(results):
                # 基于当前结果重新规划
                plan = self.planner.replan(task, results)

        # 整合所有结果
        return self.summarize(results)

    def needs_replan(self, results):
        """
        判断是否需要重新规划
        检查执行结果是否符合预期
        """
        # 获取最后一个结果
        last_result = results[-1]

        # 如果结果明显不符合预期，需要重规划
        if last_result.is_unexpected():
            return True

        # 如果结果导致后续步骤无法执行，需要重规划
        if last_result.blocks_future():
            return True

        return False

class Planner:
    """规划器：生成任务执行计划"""

    def create_plan(self, task):
        """创建初始执行计划"""
        prompt = f"""
任务：{task}

请制定详细的执行计划，包括：
1. 需要执行的步骤顺序
2. 每个步骤的具体操作
3. 步骤之间的依赖关系

输出格式：
步骤1: [操作描述]
步骤2: [操作描述]
...
"""
        plan_text = self.llm.generate(prompt)
        return Plan.parse(plan_text)

    def replan(self, task, results):
        """基于执行结果重新规划"""
        # 分析已完成的结果
        completed = [r for r in results if r.is_success]
        failed = [r for r in results if not r.is_success]

        # 生成调整后的计划
        prompt = f"""
原始任务：{task}
已完成步骤：{completed}
失败步骤：{failed}

请制定调整后的执行计划：
"""
        plan_text = self.llm.generate(prompt)
        return Plan.parse(plan_text)

class Executor:
    """执行器：执行具体的计划步骤"""

    def execute(self, step):
        """执行单个步骤"""
        # 根据步骤类型选择执行方式
        if step.type == "tool_call":
            return self.execute_tool_call(step)
        elif step.type == "code":
            return self.execute_code(step)
        elif step.type == "query":
            return self.execute_query(step)

        return Result(success=False, error="Unknown step type")
```


> 注意：Plan-and-Execute 模式适合任务结构相对稳定、可以提前规划的场景。对于需要灵活应变的环境，ReAct 模式可能更合适。


---


## 章节小结


本章节介绍了 AI Agent 的推理与规划核心能力。


**ReAct** 框架通过推理与行动的循环，让 Agent 能够边执行边调整策略。


**思维链（CoT）** 通过展示逐步推理过程，提升复杂任务的执行准确性。


**思维树（ToT）** 扩展了思维链，支持多路径探索和回溯。


**MCTS** 是一种启发式搜索算法，适合复杂决策和规划问题。


**Reflexion** 赋予 Agent 自我反思能力，从失败中学习和改进。


**任务分解策略** 是规划能力的基础，包括递归分解、平行分解和层次分解。


**Plan-and-Execute** 采用先规划后执行的模式，适合结构稳定的任务。


这些技术可以单独使用，也可以组合使用，构建更强大的 Agent 系统。









	  AI 思考中...





			** [RAG 与知识检索](https://www.runoob.com/retrieval-augmented-generation.html)
			[Python 实现 RAG 与知识检索](https://www.runoob.com/python-rag.html) **













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