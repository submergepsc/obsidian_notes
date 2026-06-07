# 强化学习 Q-learning 与 SARSA

- Source: https://www.runoob.com/ml/ml-qlearning-sarsa.html

在人工智能的领域中，强化学习是一种让智能体通过与环境交互来学习如何达成目标的方法。

想象一下教一只小狗学习新指令：它做出一个动作（如坐下），你给予奖励（一块零食），它就会逐渐学会在听到指令时做出正确的反应。Q-learning 和 SARSA 就是强化学习中两种经典且至关重要的算法，它们是智能体学习**什么动作在什么状态下最好**的核心工具。本文将为你清晰地解析这两种算法的原理、区别与实现。


---


## 强化学习与马尔可夫决策过程基础


在深入 Q-learning 和 SARSA 之前，我们需要理解它们共同的理论框架。


### 核心概念


强化学习问题通常被建模为 **马尔可夫决策过程**。它包含以下几个关键要素：


- **智能体**： 做出决策和学习的主体。
- **环境**： 智能体交互的外部世界。
- **状态**： 在特定时刻，对环境的描述。
- **动作**： 智能体在某个状态下可以执行的操作。
- **奖励**： 智能体执行动作后，环境反馈的即时收益信号。
- **策略**： 智能体在给定状态下选择动作的规则，是学习的目标。


### 目标与价值函数


智能体的终极目标是最大化长期累积奖励，而不仅仅是即时奖励。为此，我们引入了**价值函数**。


- **状态价值函数 V(s)**： 表示从状态 `s` 开始，遵循特定策略能获得的期望累积奖励。
- **动作价值函数 Q(s, a)**： 表示在状态 `s` 下执行动作 `a`，然后遵循特定策略能获得的期望累积奖励。**Q-learning 和 SARSA 的核心就是学习这个 Q 函数。**


为了平衡即时奖励和未来奖励，我们使用**折扣因子 γ** (取值范围通常为 [0, 1])。未来第 k 步的奖励会被乘以 γ^k，这意味着智能体更看重近期奖励。


---


## Q-learning：离策略的时序差分学习


Q-learning 是一种**离策略**算法，由 Watkins 于 1989 年提出。它的核心思想是智能体通过学习一个最优的 Q 值表来间接找到最优策略。


### 算法核心：Q 值更新公式


Q-learning 的学习过程通过以下公式驱动： `Q(s_t, a_t) ← Q(s_t, a_t) + α * [ r_{t+1} + γ * max_{a} Q(s_{t+1}, a) - Q(s_t, a_t) ]`


让我们拆解这个公式：


- `Q(s_t, a_t)`： 在时间 `t`，状态 `s_t` 下采取动作 `a_t` 的当前估计值。
- `α`： **学习率**，控制新信息覆盖旧信息的程度（0







	  AI 思考中...





			** [强化学习探索vs开采](https://www.runoob.com/ml-exploration-exploitation.html)
			[深度强化学习](https://www.runoob.com/ml-deep-reinforcement-learning.html) **













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