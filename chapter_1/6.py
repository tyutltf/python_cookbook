# 在字典中将键映射到多个值上

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

print(d)


d = defaultdict(list)
pairs = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 4}
for k, v in pairs.items():
    d[k].append(v)
print(d)
