import re
from abc import ABC, abstractmethod
class Pattern(ABC):
    pass



class HtmlPattern(Pattern):
    def __init__(self, tag: str):
        self._pattern = re.compile(f'<{tag}>(.*?)</{tag}>')

    def __call__(self, text: str):
        return self._pattern.findall(text)




if __name__ == '__main__':
    p = HtmlPattern('think')
    print(p('<think>hello</think>'))
