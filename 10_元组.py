'''
    - 元组和列表很相似, 但是元组中的内容是不能修改的(不能增加/删除/修改元素).
    - 元组(tuple), 列表[list], 字典{dict}
'''
# 1. 元组的定义
t1 = ()
print(type(t1)) # <class 'tuple'>
t2 = ('aa')
print(type(t2)) # <class 'str'>, 不是元组
t2 = ('aa',)
print(type(t2)) # <class 'tuple'>
# 注意: 元组中只有一个元组, 必须添加逗号, 否则创建的就不是元组! 比如: (1,), ('a',)

# 2. 元组支持下标和切片
t3 = ('苹果', '香蕉', '橘子')
print(t3[1]) # 香蕉
print(t3[::-1]) # ('橘子', '香蕉', '苹果')

# 输入上面的 t3. 你能看到元组只有两个方法可以用: count, index
t3 = ('苹果', '香蕉', '橘子', '苹果')
print(t3.count('苹果')) # 2

index = t3.index('苹果') # 查询第一个"苹果"的下标位置.
print(index) # 0
index = t3.index('苹果', 1) # 可以指定从某个下标的元素开始查询, 这里从下标为1的元素开始查, 所以返回的是第二个"苹果"下标!
# index(object, start, end) 含头不含尾
print(index) # 3

print(len(t3)) # 4

if '香蕉' in t3:
    print('香蕉在元组的下标是%d' % t3.index('香蕉'))
else:
    print('不包含香蕉')

# 3. 元组的修改: 元组虽然不能直接修改, 但可以转成列表再进行修改!
t = (1, 2, 3, 4, 5, 6)
print(id(t), t)
l = list(t) # 元组转列表
l.append('AI')
print(id(l), l) # [1, 2, 3, 4, 5, 6, 'AI']
t = tuple(l) # 列表转元组
print(id(t), t) # (1, 2, 3, 4, 5, 6, 'AI')
# 但其实本质上是用元组创建了一个新列表, 再用新列表创建一个新元组, 并把之前的 t 指向新元组.