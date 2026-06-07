# 机器学习 - 强化学习示例

- Source: https://www.runoob.com/ml/ml-reinforcement-learning.html

想象一下，你在教一只小狗学习坐下这个指令。你不会直接告诉它坐下这个单词是什么意思，而是通过奖励和惩罚来引导它。


- 当小狗偶然做出坐下的动作时，你立刻给它一块零食（**奖励**）。
- 当它做错时，你就不给零食（**惩罚**）。


经过多次尝试，小狗最终会明白坐下这个指令与获得零食之间的关联，从而学会这个技能。


**强化学习** 就是让计算机（或智能体）通过类似试错的方式，在与环境的互动中学习如何做出最优决策，以获得最大累积奖励的一种机器学习方法。


**强化学习**与我们之前学过的监督学习（有标准答案）和无监督学习（寻找数据内在结构）有本质区别。强化学习的核心是 **智能体** 与 **环境** 的持续交互。


---


## 核心概念解析


在深入代码之前，我们先来理解几个关键概念，它们就像游戏规则，定义了强化学习世界如何运转。


- **智能体：**智能体就是我们的学习者或决策者。在上面的比喻中，它就是那只小狗。在程序中，它是一个算法，负责观察环境、做出动作并从结果中学习。
- **环境：**环境是智能体所处的外部世界。它接收智能体的动作，并给出两个反馈：新的环境状态和本次动作带来的即时奖励。
- **状态：**状态是环境在某一时刻的具体情况描述。例如，在一个走迷宫的游戏里，状态就是智能体当前所在的位置坐标。
- **动作：**动作是智能体在某个状态下可以做出的选择。比如，在迷宫中，动作可以是向上、向下、向左、向右。
- **奖励：**奖励是环境对智能体动作的直接评价信号，通常是一个数值。**正奖励** 表示鼓励，**负奖励** 表示惩罚。智能体的终极目标就是最大化从开始到结束所获得的 **总奖励（累积奖励）**。
- **策略：**策略是智能体的行为准则，它定义了在每一个可能的状态下，应该选择哪个动作。学习的过程，本质上就是优化这个策略的过程。


为了更直观地理解这些概念如何协同工作，我们来看一下强化学习的基本交互流程：


![](https://www.runoob.com/wp-content/uploads/2025/12/42443f92-f7cc-42c3-949e-155572a81941.png)


这个循环会一直持续，直到达到终止状态（如游戏通关或失败）。


---


## 经典问题：悬崖寻路


为了将理论付诸实践，我们将使用一个经典的强化学习示例环境：**CliffWalking-v0**（悬崖寻路）。它来自 `gymnasium` 库（原 OpenAI Gym 的维护分支）。


### 环境描述


- **场景**：一个 4x12 的网格世界。
- **起点**：左下角（坐标 [3, 0]）。
- **终点**：右下角（坐标 [3, 11]）。
- **悬崖**：最底部一排除了起点和终点的所有位置（[3, 1] 到 [3, 10]），掉入悬崖会获得巨大惩罚并回到起点。
- **目标**：智能体要从起点安全地走到终点，并避免掉下悬崖。
- **动作**：上（0）、右（1）、下（2）、左（3）。
- **奖励**： 每走一步普通网格：-1（鼓励用更少步数到达）
- 掉下悬崖：-100，并被送回起点
- 到达终点：0，并结束本次尝试


---


## 算法简介：Q-Learning


我们将使用 **Q-Learning** 算法来解决这个问题。它是一种 **无模型** 的强化学习算法，意味着智能体不需要预先知道环境的运作规则（如状态转移概率），它通过不断尝试来学习。


它的核心是一个名为 **Q表** 的表格。


- **行** 代表所有可能的状态。
- **列** 代表所有可能的动作。
- **单元格的值（Q值）** 代表在某个状态下，采取某个动作的长期期望收益。


Q-Learning 的学习过程可以概括为以下几步，它展示了智能体如何通过一次经验来更新自己的知识（Q表）：


![](https://www.runoob.com/wp-content/uploads/2025/12/ml-reinforcement-learning-runoob-1.png)


### 核心公式：贝尔曼方程


Q表更新的数学基础是贝尔曼方程，其更新公式如下：


\[ Q(S, A) \leftarrow Q(S, A) + \alpha [R + \gamma \max_{a} Q(S', a) - Q(S, A)] \]


让我们拆解这个公式中的每个部分：


| 符号 | 含义 | 类比解释 |
| --- | --- | --- |
| \( Q(S, A) \) | 状态S下动作A原有的Q值 | 你之前对在十字路口直行这个决策的旧评分 |
| \(\alpha \) | 学习率 (0







	  AI 思考中...





			** [机器学习 – PCA 可视化案例](https://www.runoob.com/ml-pca-visualization-case.html)
			[机器学习-学习路线](https://www.runoob.com/ml-how-to-learn.html) **













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