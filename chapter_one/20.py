# 将多个映射合并为单个映射

a={'x':1,'y':3}
b={'z':2,'y':4}

from collections import ChainMap
c=ChainMap(a,b)

# 如果键重复，选择第一个字典里的键
print(c['x'])
print(c['y'])