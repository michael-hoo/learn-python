print('*1-' * 20)
'''
1. 如何计算时间差?
'''
import time
from datetime import datetime
a = datetime.now()
# time.sleep(1.23456) # 测试时用
b = datetime.now()
# 计算 b 和 a 之间的时间差
print(b - a) # 0:00:01.239431
# 用秒来表示时间差(不足一秒的部分会被丢弃, 日常使用够用了)
print((b - a).seconds) # 1 返回一个整型数字, 所以会丢失部分时间, 但在不需要那么精确到时候用.
print((b - a).microseconds) # 239431 虽然 microseconds 是微秒的意思, 但这里显然不是微秒.
# 参考上面三行的输出, 可以看出: b - a == (b-a).seconds + (b-a).microseconds/10^6
print((b - a).seconds + (b - a).microseconds / 10 ** 6) # 1.239431


print('*2-' * 20)
'''
2. 对于包含字典的列表, 如 [{'a': 1}, {'b': 2}, {'c': 3}], 如何根据某个 key, 删除列表中的指定字典呢?
(假设我们要删除列表中 key 为 'b' 的字典)
'''
# 第一步: 获取指定字典.
def get_dict(list, key='a'):
    for d in list: # 从列表中依次遍历每个字典
        if key in d:
            return d
    else:
        return None

l1 = [{'a': 1}, {'b': 2}, {'c': 3}]
print(get_dict(l1)) # {'a': 1}
print(get_dict(l1, 'c')) # {'c': 3}
print(get_dict(l1, 'd')) # None

# 第二步: 根据查询到的字典找到其在列表中的下标(使用 index 方法).
l = [{'a': 1}, {'b': 2}, {'c': 3}]
i = l.index(get_dict(l, 'b'))
print(i) # 1 成功找到其下标!!!

# 第三步: 根据下标删除列表中的指定元素.
l.pop(i)
print(l) # [{'a': 1}, {'c': 3}]
# 达成目标!

# 另一种方法: 试了一下, 可以不用 pop(), 直接把字典放到列表中的 remove() 方法也可以实现此操作.
# 等于上面的第二步和第三步变成一步了, 这样会更简单!
l = [{'a': 1}, {'b': 2}, {'c': 3}]
l.remove(get_dict(l, 'c'))
print(l) # [{'a': 1}, {'b': 2}]


print('*3-' * 20)
'''
3. Python 获取单元素字典的 key 和 value.
获取字典中的 key 当然可以在循环中使用 d.keys() 来遍历, 但对于单元素字典这样写太过于繁琐.
以下方法更简单:
'''
# 方法一
d = {'a': 1}
(key, value), = d.items() # 这种方法有点神奇!
print(key, value) # a 1

# 方法二: 此方法我可以理解
d = {'a': 1}
key= list(d)[0]
print(key) # a
# 为什么会有这样的结果? 不妨看看 list(d) 发生了什么.
print(list(d)) # ['a']
# 应该是将 dict 转化为 list, 默认是把字典中的所有 key 放在一个列表中.
# 可以验证一下:
d1 = {'a': 1, 'b': 2}
print(list(d1)) # ['a', 'b'] 果然如此!

# 那么, 如何获取单元素字典中的 value 值呢? 可以用字典的 values() 方法.
print(list(d.values())) # [1]
# 所以, 可以这样获得 value:
value = list(d.values())[0]

# 方法三: 这个方法也挺神奇
d = {'a': 1}
key, = d
values, = d.values()
print(key, values) # a 1


print('*4-' * 20)
'''
4. 利用递归实现九九乘法表!!!
'''
def test(i=9, j=9):
    print('{} * {} = {}'.format(i, j, i*j), end='\t')
    if i == 1:
        return
    else:
        if j == 1:
            print()
            test(i-1, i-1)
        else:
            test(i, j-1)

# test()

print()
print('*5-' * 20)

'''
5. 使用递归遍历目录下的所有文件(包括文件夹)
'''
import os

def print_dir(tar_dir):
    file_list = os.listdir(tar_dir)
    for file_name in file_list:
        file_path = os.path.join(tar_dir, file_name) # 文件/目录的完整路径
        if os.path.isdir(file_path):
            print_dir(file_path) # 他的代码和我的有何区别? 我在这里用了 return...
        else:
            print(file_path)

# print_dir('/Users/hunan/Documents/Python 学习笔记')

print('*6-' * 20)
'''
6. f-string
'''
import random

r = random.random()
print(f'产生一个随机数: {r}')
# 有了这个东西, %s/format()谁还用啊???
