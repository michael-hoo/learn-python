# 类型转换
print('*-1' * 20)
# 1. string, bool -> int
fst_num = '123'
snd_num = '456'
print(fst_num + snd_num) # 字符串的加法实际上就是字符串拼接。
print(int(fst_num) + int(snd_num)) # 将 string 型转化为 int 型之后，进行的就是加法运算了。
print(int(True), int(False)) # 将 bool 型转化为 int 型，True 会变成 1，False 会变成 0.

print('*-2' * 20)
# 2. list -> tuple, set
'''
    list -> tuple: 元素不可增加/删除/修改.
    list -> set: 元素有丢失风险(因为 list 允许重复, 而 set 不允许).
'''
l = [1, 1, 2, 3, 5, 5, 7]
t = tuple(l)
print(t) # (1, 1, 2, 3, 5, 5, 7)
s = set(l)
print(s) # {1, 2, 3, 5, 7}, 可以看到重复元素已经消失了.

print('*-3' * 20)
# 3. tuple -> list, set
t = (1, 2, 2, 3, 3, 5, 7, 7)
l = list(t)
print(l) # [1, 2, 2, 3, 3, 5, 7, 7]
s = set(t)
print(s) # {1, 2, 3, 5, 7}

print('*-4' * 20)
# 4. set -> list, tuple
s = {1, 1, 2, 3, 5, 5, 7}
print(s) # {1, 2, 3, 5, 7}, 可以看出, set 自己会删除重复元素.
l = list(s)
print(l) # [1, 2, 3, 5, 7]
t = tuple(s)
print(t) # (1, 2, 3, 5, 7)

print('*-5' * 20)
# 5. dict -> list, tuple, set
d = {'name': 'Nathan', 'age': 31, 'job': 'developer'}
l = list(d)
print(l) # ['name', 'age', 'job']
'''
可以看出, 把 dict 转化为 list, 默认只会将字典中的 key 拿出来存放到列表中, tuple/set 同理.
但是, 我们之前介绍过 dict.keys(), dict.values(), dict.items() 方法!
使用这些方法, 我们就可以将字典转化为我们想要的列表! tuple/set 同理.
'''
## d.keys()
l = list(d.keys())
print(l) # ['name', 'age', 'job'], 和直接转 d 效果一样.
## d.values()
l = list(d.values())
print(l) # ['Nathan', 31, 'developer'], 将字典中的 value 值转化为列表.
## d.items()
print(d.items()) # dict_items([('name', 'Nathan'), ('age', 31), ('job', 'developer')])
l = list(d.items()) # 可以转化为由几个元组(每个元组只包含两个元素)组成的列表.
print(l) # [('name', 'Nathan'), ('age', 31), ('job', 'developer')]

print('*-6' * 20)
# 6. list, tuple -> dict: 可以转, 但只有特殊的列表可以转.
# 对于普通列表, 我们将其转化为 dict 会报错.
# l = [1, 2, 3, 4, 5, 6]
# d = dict(l) # TypeError
l1 = [('a', 1), ('b', 2), ('c', 3)] # 对于这种特定类型的列表, 才可以转化为 dict!
l2 = [['A', 1], ('B', 2), ['C', 3]] # 列表里面不限于元组或列表.

d = dict(l1)
print(d) # {'a': 1, 'b': 2, 'c': 3}
d = dict(l2)
print(d) # {'A': 1, 'B': 2, 'C': 3}
'''
想法: 有没有发现? 其实这个过程和 list(d.itmes()) 是相反的!
'''
# tuple 转化为 dict 也是同样的道理.
t1 = (['a', 1], ['b', 2], ['c', 3])
t2 = (('A', 1), ['B', 2], ('C', 3))
d = dict(t1)
print(d) # {'a': 1, 'b': 2, 'c': 3}
d = dict(t2)
print(d) # {'A': 1, 'B': 2, 'C': 3}