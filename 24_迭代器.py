'''
可迭代对象: 
  1. 生成器
  2. 字符串, 列表, 元组, 字典, 集合

如何判断一个对象是否可迭代? -> isinstance()
'''
from typing import Iterable # Iterable 需要额外导入

l = [1, 2, 3]
print(isinstance(l, Iterable)) # True
# 原理: 所有可迭代对象均继承了 Iterable 这个类(), 即 Iterable 是 list, tuple, set 等的父类
# 只要继承了这个类, 都是可迭代的!
print(isinstance('abc', Iterable)) # True, 所以, 字符串也是可迭代的
print(isinstance(123, Iterable)) # False, 而整型不是可迭代的


'''
迭代器: 可以被 next() 函数调用并不断返回下一个值的对象称为"迭代器" - Iterator

迭代器的特点:
 - 迭代是访问集合元素的一种方式, 而迭代器是一个可以记住遍历位置的对象.
 - 迭代器对象从集合的第一个元素开始访问, 直到所有的元素被访问完结束.
 - 迭代器只能往前, 不能后退.

Iterable 是否都是 Iterator ?
 - 不是, 使用 next() 方法直接调用列表会报错.
 - 生成器是可迭代的, 同时也是迭代器.
 - list 是可迭代的, 但不是迭代器.

如何将 Iterable 对象变成 Iterator 呢?
 - 使用 iter() 方法即可.
 - iter(Iterable) -> Iterator
 - 参考下面的代码
'''
l = [1, 2, 3, 4, 5]
# 可以看到 ll 就是一个迭代器
ll = iter(l) # <list_iterator object at 0x10fb2fd00>
print(ll)
# 对迭代器使用 next() 方法
print(next(ll)) # 1
print(next(ll)) # 2
print(next(ll)) # 3
'''
感觉有点生成器的感觉了, 那如果我用 l = iter([i for i in range(1000)]) 这种方式会占内存吗? 

生成器与迭代器:
 - 生成器是迭代器, 但迭代器不一定是生成器, 比如 iter(list) 是迭代器, 但不是生成器.
'''