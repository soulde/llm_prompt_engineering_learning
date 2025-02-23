import re
from copy import deepcopy


class Template:
    def __init__(self, template: str):
        self.template = template
        self._pattern = re.compile(r'\{([^}]*)\}')
        self._params = self._pattern.findall(template)
        for i in self._params:
            if '{' in i or '}' in i:
                raise ValueError(f"A recursive template is not allowed")

    @property
    def params(self):
        return self._params

    def __call__(self, **kwargs):
        out = deepcopy(self.template)
        for k, v in kwargs.items():
            if k not in self._params:
                raise ValueError(f"Template does not have parameter {k}")
            out = out.replace(f'{{{k}}}', str(v))
        for i in self._params:
            if i not in kwargs:
                out = out.replace(f'{{{i}}}', '')

        return out
    def __str__(self):
        return self.template



if __name__ == '__main__':
    template = "你好，{name}。"
    t = Template(template)
    print(t.params)
    print(t(name='张三'))
    print(t(name='李四'))
    print(t)
