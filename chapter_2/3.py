# 利用shell通配符做字符串匹配

from fnmatch import fnmatch,fnmatchcase

print(fnmatch('foo.txt','*.txt'))

print(fnmatch('foot.txt','?o.txt'))

print(fnmatch('Dat45.csv','Dat[0-9]*'))