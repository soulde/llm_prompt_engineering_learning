import ollama

from prompts import CostarPromptTemplate, ThinkPromptTemplate, SystemPromptTemplate, COTPromptTemplate


class COTAgent:
    def __init__(self, model_name):
        self.model_name = model_name

    def run(self):
        while True:
            # get user input
            user_input = input("User: ")
            # get response from model
            prompt = self._cat_prompt(user_input)
            # print(prompt)
            stream = ollama.generate(self.model_name, prompt, stream=True)
            for chunk in stream:
                print(chunk.response, end="", flush=True)
            print('\n')
    def _cat_prompt(self, question):
        # return CostarPromptTemplate(context="你的名字叫Fake Soulde, 我需要你作为我的生活助手，辅助我处理日常事务",
        #                             objective="你需要对聊天内容做出积极回应，辅助处理问题，包括专业问题、日程问题等",
        #                             style="日常聊天风格",
        #                             tone="轻松但严谨",
        #                             audience="你需要与我进行对话，我是一个在读研究生，有科研任务和项目。同时，还需要进行日常交流聊天",
        #                             response="你需要对聊天内容回复，提供相应的内容信息或者提供问题的解决方案") + ThinkPromptTemplate() + SystemPromptTemplate(
        #     input=question) + COTPromptTemplate()
        return SystemPromptTemplate(input=question) + COTPromptTemplate()


if __name__ == '__main__':
    agent = COTAgent('minicpm-v')
    agent.run()
