import logging

from tools import noneTool
import ollama

from prompts import SystemPromptTemplate, MemoryPromptTemplate, CostarPromptTemplate, ReactPromptTemplate, HtmlPattern

logger = logging.getLogger('Agent')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class Agent:
    def __init__(self, model_name, tools=[noneTool]):

        self.model_name = model_name
        self.question = None
        self.state = 'null'
        self.states: list[str] = ['start', 'think', 'act', 'observe', 'end']
        self.think_pattern = HtmlPattern('think')
        self.action_pattern = HtmlPattern('action')
        self.action_input_pattern = HtmlPattern('action_input')
        self.observation_pattern = HtmlPattern('observation')
        self.answer_pattern = HtmlPattern('answer')
        self.latest_response = None
        self.latest_answer = None
        self.history = []
        self.tools = {tool.name: tool for tool in tools}

        self.react_step = 0
        self.action_name = None
        self.action_input = None

    def call_action(self, action_name: str, action_input: str) -> str:
        return self.tools[action_name](action_input)

    def run(self):
        while True:
            question = input(">>")
            prompt = self._cat_prompt(question)
            ret = ollama.generate(self.model_name, prompt)
            logger.info(ret.response)
            self.latest_response = ret.response
            self.history.append(f"<question>{question}</question>\n")
            while True:
                think = self.think_pattern(self.latest_response)[0]
                action = self.action_pattern(self.latest_response)
                prompt += f"<think>{think}</think>\n"
                self.history.append(f"<think>{think}</think>\n")
                if len(action) > 0 and action != 'None':
                    self.action_name = action[0]
                    self.action_input = self.action_input_pattern(self.latest_response)
                    observation = self.call_action(self.action_name, self.action_input)

                    prompt += f"<action>{self.action_name}</action>\n"
                    prompt += f"<action_input>{self.action_input}</action_input>\n"
                    prompt += f"<observation>{observation}</observation>\n"

                    self.history.append(f"<action>{self.action_name}</action>\n")
                    self.history.append(f"<action_input>{self.action_input}</action_input>\n")
                    self.history.append(f"<observation>{observation}</observation>\n")
                    logger.info(prompt)
                    ret = ollama.generate(self.model_name, prompt)
                    logger.info(ret.response)
                    self.latest_response = ret.response
                else:
                    self.latest_answer = self.answer_pattern(self.latest_response)[-1]
                    self.history.append(f"<answer>{self.latest_answer}</answer>\n")
                    print(self.history)
                    print(self.latest_answer)
                    break

    def _cat_prompt(self, question):
        components = [
            CostarPromptTemplate(context="你的名字叫Fake Soulde, 我需要你作为我的生活助手，辅助我处理日常事务",
                                 objective="你需要对聊天内容做出积极回应，辅助处理问题，包括专业问题、日程问题等",
                                 style="日常聊天风格",
                                 tone="轻松但严谨",
                                 audience="你需要与我进行对话，我是一个在读研究生，有科研任务和项目。同时，还需要进行日常交流聊天",
                                 response="你需要对聊天内容回复，提供相应的内容信息或者提供问题的解决方案"),
            MemoryPromptTemplate(memory="".join(self.history)),
            # ThinkPromptTemplate(),
            ReactPromptTemplate(tools=''.join([t.prompt for t in self.tools.values()]),
                                tool_names=''.join([i+"，" for i in self.tools.keys()])),
            SystemPromptTemplate(input=question)
        ]
        prompt = "".join(components)
        # logger.info(f'current prompt: \n{prompt}')
        return prompt
