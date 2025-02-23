from .Template import Template

costar_prompt = '''
## COSTAR Requirements ##
# CONTEXT #
{context}

# OBJECTIVE #
{objective}

# STYLE #
{style}

# TONE #
{tone}

# AUDIENCE #
{audience}

# RESPONSE #
{response}
'''
costar_prompt_example = '''
## COSTAR Requirements ##
# CONTEXT #
我需要你作为我的生活助手，辅助我处理日常事务

# OBJECTIVE #
你需要对聊天内容做出积极回应，辅助处理问题，包括专业问题、日程问题等

# STYLE #
日常聊天风格

# TONE #
轻松但严谨

# AUDIENCE #
你需要与我进行对话，我是一个在读研究生，有科研任务和项目

# RESPONSE #
你需要对聊天内容回复，提供相应的内容信息或者提供问题的解决方案
'''
memory_prompt = '''
## MEMORY ##
以下是和用户的聊天记录，请在回答问题时利用以下历史信息
{memory}
'''
rag_prompt = '''
## RAG ##
{rag}
'''
react_prompt = '''
## REACT ##
按照给定的格式回答以下问题。
你可以使用下面这些工具：

{tools}

回答时需要遵循以下格式，保证<answer>前有一个<think>：
<think>回答这个上述我需要做些什么</think>
<action>上述列出的工具中的其中一个工具名，必须要在{tool_names}中。</action>
<action_input>选择工具所需要的输入</action_input>
<observation>选择工具返回的结果</observation>
...（这个思考/行动/行动输入/观察可以重复N次）
<think>我现在知道最终答案</think>
<answer>原始输入问题的最终答案</answer>

比如：
<think>Let me solve this step by step.</think>
<action>Search</action>
<action_input>What is the capital of France?</action_input>
<observation>Paris is the capital of France.</observation>
<think>Now I know the answer.</think>
<answer>Paris</answer>
'''
tools_prompt = '''
---
Tool Name: {tool_name}
Tool Description: {tool_description}
Tool Input: {tool_parameters}
'''
think_prompt = '''
## COT ##

按照给定的格式回答以下问题。
回答时需要遵循以下格式：
<think>回答这个上述我需要做些什么</think>
...（这个思考可以重复N次）
<think>我现在知道最终答案</think>
<answer>原始输入问题的最终答案</answer>

比如：
<think>Let me solve this step by step.</think>
<think>在为用户进行直流有刷电机驱动电路的选型时，需要综合考虑多个因素，如电压、电流、功耗和成本等。以下是详细的选型建议：
1. MOSFET或IGBT器件：选择合适的功率MOSFET或IGBT，满足5A额定电流的需求，并确保在特定工作条件下能正常运行。
2. 控制信号：使用PWM信号控制电机的正反转，并考虑电路稳定性和响应速度等因素。
3. 其他组件：如栅极驱动器、开关元件等，需要与MOSFET或IGBT配合使用以实现有效的电压和电流控制。</think>
<think>综合这些因素，在设计中选择合适的器件和拓扑结构将有助于满足用户的12V电机5A额定电流要求。</think>

<answer>在直流有刷电机的驱动电路选型时，可以选择适合的工作电压（如MOSFET或IGBT）来满足5A额定电流的需求。使用PWM信号进行控制，并综合考虑各个组件的选择和配合以实现稳定的性能。</answer>
'''

system_prompt = '''
## Question ##
{input}
'''
COT_prompt = '''
Let me solve this step by step.
'''
CostarPromptTemplate = Template(costar_prompt)
MemoryPromptTemplate = Template(memory_prompt)
RAGPromptTemplate = Template(rag_prompt)
ReactPromptTemplate = Template(react_prompt)
ToolsPromptTemplate = Template(tools_prompt)
ThinkPromptTemplate = Template(think_prompt)
SystemPromptTemplate = Template(system_prompt)
COTPromptTemplate = Template(COT_prompt)
