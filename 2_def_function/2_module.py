import pizza
import pizza as p
from pizza import tell
from pizza import tell as te

"""
    调用pizza模块
"""
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
    直接import函数
"""
tell()

"""
    别名te
"""
te()

"""
    模块别名
"""
p.tell()