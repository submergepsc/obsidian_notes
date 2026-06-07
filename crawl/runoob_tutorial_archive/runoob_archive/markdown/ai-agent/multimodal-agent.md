# 多模态 Agent

- Source: https://www.runoob.com/ai-agent/multimodal-agent.html

多模态 Agent 能够处理和理解多种类型的输入。


包括图像、语音、视频等，而不仅仅是文本。


---


## 什么是多模态


多模态（Multimodal）指同时处理多种信息模态的能力。


人类通过多种感官接收信息：视觉、听觉、触觉等。


多模态 AI 旨在让机器具有类似的能力。


### 常见的模态类型


**文本（Text）**：自然语言文字，是最常见的模态。


**图像（Image）**：静态图片，包括照片、图表、截图等。


**语音（Audio）**：声音信号，包括语音、音乐、环境声等。


**视频（Video）**：连续的图像序列，包含时间和空间信息。


**文档（Document）**：包含文本、表格、图表等混合内容的复合文档。


### 为什么需要多模态 Agent


单一模态的 Agent 有很大局限。


用户的需求是多样化的，不能要求所有人都用文本描述问题。


很多信息天然是多模态的，如截图中包含文本和视觉信息。


---


## 图像理解


图像理解是当前最成熟的多模态能力。


现代多模态模型（如 GPT-4V、Gemini）能够理解和分析图像内容。


使得 Agent 能够"看见"并理解视觉信息。


### 核心能力


**视觉问答（VQA）**：根据图像内容回答问题。


**图像描述（Captioning）**：生成图像的文字描述。


**文档理解**：理解文档截图、表格、图表等。


**屏幕理解**：理解 GUI 界面、应用截图等。


### 代码实现


## 多模态 Agent 实现


```
class MultimodalAgent:
    """
    多模态 Agent 实现
    能够处理图像、文本等多种输入
    """

    def __init__(self, vision_model, llm, tools):
        # 视觉模型：分析图像
        self.vision_model = vision_model
        # 语言模型：推理和生成
        self.llm = llm
        # 可用工具列表
        self.tools = tools

    def process_image(self, image, task):
        """
        处理图像输入
        :param image: 图像数据（可以是 PIL Image、URL 或 base64）
        :param task: 任务描述
        :return: 处理结果
        """
        # 使用视觉模型分析图像
        image_description = self.vision_model.analyze(image)

        # 结合文本任务进行推理
        prompt = f"""图像内容描述：
{image_description}

用户任务：{task}

请根据图像内容和任务要求执行相应操作。
"""
        reasoning = self.llm.reason(prompt)

        # 如果需要执行操作，选择合适的工具
        if reasoning.needs_action:
            return self.execute_action(reasoning.action)

        return reasoning.result

    def process_text(self, text, context=None):
        """
        处理文本输入
        """
        prompt = f"""
任务：{text}
上下文：{context or "无"}
"""
        return self.llm.generate(prompt)

    def process_mixed(self, image, text, task):
        """
        处理图像和文本混合输入
        """
        # 分析图像
        image_description = self.vision_model.analyze(image)

        # 构建多模态提示
        prompt = f"""图像内容：
{image_description}

附加文本信息：{text}

用户任务：{task}

请结合图像和文本信息来完成用户任务。
"""
        return self.llm.generate(prompt)

class VisionModel:
    """
    视觉模型封装
    支持多种视觉理解能力
    """

    def __init__(self, model_name="gpt-4-vision-preview"):
        self.model_name = model_name

    def analyze(self, image):
        """
        分析图像内容
        返回详细的文字描述
        """
        # 实际调用视觉模型 API
        # 这里简化处理
        response = self.call_vision_api(image, prompt="""
请详细描述这张图像的内容。
包括：
1. 图像中的主要对象和场景
2. 文字内容（如果有）
3. 图表或数据信息（如果有）
4. 重要的细节和特征
""")
        return response.description

    def analyze_chart(self, image):
        """
        专门分析图表类型图像
        """
        response = self.call_vision_api(image, prompt="""
这是一个图表图像。
请提取：
1. 图表类型（柱状图、折线图、饼图等）
2. 标题和轴标签
3. 所有数据点的数值
4. 主要趋势和结论
""")
        return response

    def analyze_document(self, image):
        """
        分析文档类型图像
        """
        response = self.call_vision_api(image, prompt="""
这是一个文档截图。
请提取：
1. 文档类型（PDF 截图、网页、PPT 等）
2. 标题和主要文字内容
3. 表格内容（如果存在）
4. 文档结构
""")
        return response
```


### 典型应用场景


**图表分析**：自动解读数据图表，提取数据趋势和结论。


**截图理解**：理解软件界面截图，进行 UI 自动化操作。


**文档处理**：处理扫描文档、PDF 截图等。


**视觉问答**：根据图片回答用户问题。


---


## 语音处理


语音交互为 Agent 提供了更自然的交互方式。


用户可以直接说话与 Agent 交流，无需打字。


### 语音处理流程


**语音识别（ASR）**：将语音信号转换为文本。


**语义理解（NLU）**：理解文本的含义和用户意图。


**对话管理（DM）**：管理对话状态，决定回复策略。


**语音合成（TTS）**：将文本回复转换为语音输出。


### 代码示例


## 语音处理 Agent


```
class VoiceAgent:
    """
    语音交互 Agent
    支持语音输入和语音输出
    """

    def __init__(self, asr_model, tts_model, nlu_model, dialogue_manager):
        # 自动语音识别模型
        self.asr_model = asr_model
        # 文本转语音模型
        self.tts_model = tts_model
        # 语义理解模型
        self.nlu_model = nlu_model
        # 对话管理器
        self.dialogue_manager = dialogue_manager

    def process_voice_input(self, audio_data):
        """
        处理语音输入
        :param audio_data: 原始音频数据
        :return: 语音响应（可选）
        """
        # 第一步：语音识别 - 将语音转为文本
        text = self.asr_model.transcribe(audio_data)

        # 第二步：语义理解 - 理解用户意图
        intent = self.nlu_model.parse(text)

        # 第三步：对话管理 - 生成响应
        response = self.dialogue_manager.respond(intent)

        # 第四步：检查是否需要语音输出
        if response.should_speak:
            # 语音合成 - 将文本转为语音
            audio_response = self.tts_model.synthesize(response.text)
            return {
                "text": response.text,
                "audio": audio_response,
                "intent": intent
            }

        return {
            "text": response.text,
            "audio": None,
            "intent": intent
        }

    def process_text_input(self, text):
        """
        处理文本输入（语音转文字后的处理）
        """
        # 语义理解
        intent = self.nlu_model.parse(text)

        # 对话管理
        response = self.dialogue_manager.respond(intent)

        return {
            "text": response.text,
            "intent": intent
        }

class ASRModel:
    """语音识别模型"""

    def transcribe(self, audio_data):
        """
        将语音转为文本
        :param audio_data: 音频数据（ WAV、MP3 等格式）
        :return: 识别的文本
        """
        # 实际调用 ASR API
        # 例如：Whisper、DeepSpeech 等
        text = self.recognition_api(audio_data)
        return text

class TTSModel:
    """文本转语音模型"""

    def synthesize(self, text, voice_id="default"):
        """
        将文本转为语音
        :param text: 要转换的文本
        :param voice_id: 语音风格 ID
        :return: 音频数据
        """
        # 调用 TTS API
        audio = self.synthesis_api(text, voice=voice_id)
        return audio

class DialogueManager:
    """对话管理器"""

    def __init__(self, llm):
        self.llm = llm
        self.conversation_history = []

    def respond(self, intent):
        """
        根据用户意图生成响应
        """
        # 更新对话历史
        self.conversation_history.append({
            "role": "user",
            "content": intent.raw_text
        })

        # 使用 LLM 生成响应
        prompt = self.build_prompt(intent)
        response_text = self.llm.generate(prompt)

        # 更新对话历史
        self.conversation_history.append({
            "role": "assistant",
            "content": response_text
        })

        return DialogueResponse(
            text=response_text,
            should_speak=True
        )

    def build_prompt(self, intent):
        """构建提示词"""
        return f"""
对话历史：
{self.conversation_history}

用户最新意图：{intent}

请生成合适的回复。
"""
```


---


## 视频理解


视频理解是最复杂的多模态任务之一。


视频同时包含时间维度和空间维度的信息。


需要处理帧序列、音频、字幕等多种数据。


### 视频理解的核心挑战


**时序建模**：理解物体在时间上的变化和动作序列。


**多帧融合**：有效融合多个帧的信息。


**音频同步**：结合视频和音频信息。


**计算成本**：处理视频的计算量远大于单张图像。


### 常见处理策略


**采样策略**：均匀采样或关键帧采样。


**帧级分析**：先分析单个帧，再汇总。


**光流融合**：利用光流信息捕捉运动。


---


## 多模态 Agent 的应用


### 智能相册管理


自动识别照片内容，进行分类和搜索。


如：根据场景（海滩、山景）、人物、活动等组织照片。


### 视频内容分析


自动生成视频摘要，提取关键片段。


如：从长视频中提取精彩片段、生成章节概要。


### 无障碍辅助


为视障用户提供图像描述服务。


描述周围环境、读取文档、识别物体等。


### 视频会议助手


实时分析会议视频，提取要点和行动项。


自动生成会议纪要和待办事项。










	  AI 思考中...





			** [AI Agent 工具与外部集成](https://www.runoob.com/tools-integration.html)
			[Agent 评估、安全与对齐](https://www.runoob.com/evaluation-safety-alignment.html) **













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