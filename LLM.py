from zhipuai import ZhipuAI

api_key = 'd0ed1a25b5e3daf2eb6d0b0208d39ac0.gBwioR9Db5iDjtPz'


class LLM:
    def __init__(self, api_key):
        self.system_prompt = ''
        self.client = ZhipuAI(api_key=api_key)
        self.model = "glm-4-flash"
        self.temperature = 0.7
        self.max_tokens = 1024
        self.top_p = 0.95

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
        )
        return response.choices[0].message.content

    def set_system_prompt(self, prompt):
        self.system_prompt = prompt


if __name__ == "__main__":
    llm = LLM(api_key=api_key)
    with open("prompts/system_prompt", encoding='utf-8') as f:
        data = f.read()
        llm.set_system_prompt(data)

    print(llm.generate("你好，世界！"))
