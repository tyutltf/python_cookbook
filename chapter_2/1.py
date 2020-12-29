# 针对任意多的分隔符拆分字符串

line='asdf fhj, djah; fajk,   lll'
import re

print(re.split(r'[,;\s]\s*',line))

res=re.split(r'(?:,|;|\s)\s*',line)
print(res)