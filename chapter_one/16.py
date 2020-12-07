# 筛选序列中的元素

mylist=[1,4,-5,10,-7,2,3,-1]

x_than_0=[x for x in mylist if x>0]

print(x_than_0)

# 生成器表达式会更节省内存消耗
y_than_0=(x for x in mylist if x>0)

print(y_than_0)

# 创建布尔序列
z_true=[x>0 for x in mylist]
print(z_true)