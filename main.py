from Agent import Agent
from tools import searchTool, noneTool

if __name__ == '__main__':
    agent = Agent("minicpm-v", tools=[searchTool, noneTool])
    agent.run()