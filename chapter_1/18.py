# 将名称映射到序列的元素中 命名元组

from collections import namedtuple

PerSnews=namedtuple('PerSnews',['name','age','phone','address'])

one_news=PerSnews('zs','18','123123123','中国中央广播电视台')

print(one_news)
print(one_news.name)

a,b,c,d=one_news
print(b)