from prompts import ToolsPromptTemplate


class Tool:
    def __init__(self, tool_name, tool_description, tool_parameters, func):
        self.name = tool_name
        self.description = tool_description
        self.parameters = tool_parameters
        self.prompt = ToolsPromptTemplate(
            tool_name=tool_name,
            tool_description=tool_description,
            tool_parameters=tool_parameters
        )
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


noneTool = Tool(
    tool_name="None",
    tool_description="不使用任何工具",
    tool_parameters='{}',
    func=lambda x: None
)


def fake_search(query):
    if "南京" in query and "天气" in query:
        return f"搜索结果: 南京今天1摄氏度，下雨。"
    else:
        return f"搜索结果: {query} 没有找到相关内容。"


searchTool = Tool(
    tool_name="Search",
    tool_description="一个可以搜索互联网的搜索引擎",
    tool_parameters='{"query": "搜索内容"}',
    func=fake_search
)
