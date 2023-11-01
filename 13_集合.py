'''
集合: set, 其底层是通过字典实现的, 可以简单理解为集合是只包含 key 的字典.
集合的特点: 无序, 没有重复(为何没有重复? 因为字典中的 key 是不允许重复的).
    因为无序, 所以集合没有下标和切片的概念.
集合的定义: set1 = {'key1', 'key2', 'key3', ...}
    同样是花括号, dict 是 key-value 键值对, 而 set 只包含 key!
''' 
# 集合有什么作用呢?
## 可以消除 list 中的重复元素
list1 = [1, 1, 3, 4, 4, 7, 8, 9, 1]
set1 = set(list1) # 将 list 强行转化为 set, 即可消除重复值!
print(set1) # {1, 3, 4, 7, 8, 9}

print('1.', '*-' * 20)
# 1. 集合的定义
# 定义一个空列表
list1 = []
# 定义一个空元组
tuple1 = ()
# 定义一个空字典
dict1 = {} # 集合的符号和字典的符号一样, 但无法这样定义一个空集合了.
# 定义一个空集合
set1 = set()


print('2.', '*-' * 20)
# 2. 往集合中添加元素: add, update
'''
    - set.add(object): 往集合中添加元素.
    - set1.update(set2): 将 set2 中的所有元素添加到 set1 当中.
'''
set1.add('a')
print(set1) # {'a'}
set1.add('b')
print(set1) # {'b', 'a'}
set1.add('a') # 重复添加元素, 不起任何作用.
print(set1) # {'b', 'a'}

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
set1.update(set2) # 将 set2 中的元素添加到 set1 中, 并消除重复元素.
print(set1) # {'b', 'a', 'd', 'c'}

print('练习', '*-' * 20)
# 练习1: 产生5组由字母和数字组成的4位验证码(不允许重复), 然后打印出来.
import random
# 创建一个存放验证码的集合, 确保其中的验证码不会重复!
valid_set = set()
# 每次从 key 中获取一位验证码, 通过循环获得4位验证码.
key = 'abcdefghijklmnopqrstuvwxyz0123456789'
while len(valid_set) < 5: # 当集合中存放5组验证码时, 结束循环.
    valid_code = '' # 外层循环每次开始时, 要创建一个空的验证码字符串.
    for i in range(4):
        # index = random.randint(0, len(key) - 1) # 随机产生一个下标
        # valid_code += key[index] # 随机选出 key 中的一位, 追加到验证码字符串的末尾, 在 for 循环中追加4次.
        r = random.choice(key) # 随机从指定字符串中选中一个, 比 randint() 更直观!
        valid_code += r 
    else:
        # 将产生的4位验证码字符串添加到集合中, 然后 while 循环继续, 直到 valid_set 中包含5个字符串.
        valid_set.add(valid_code)
else: # while 循环结束后, 将验证码打印出来.
    print('共产生{}组验证码, 如下所示:'.format(len(valid_set)))
    for i in valid_set:
        print('\t', i)


print('3.', '*-' * 20)
# 3. 删除集合中的元素: remove, discard, del, clear, pop
'''
    - remove 和 discard 的功能差不多, 都是根据 key 来删除指定元素. 区别在于:
        - set.remove(key)  如果传入的 key 不存在, 会抛出 KeyError.
        - set.discard(key) 如果传入的 key 不存在, 没有任何反应.
    - del set 删除集合指针
    - set.clear() 清空集合
        - del 和 clear 同列表/字典中的功能相同, 这里不赘述.
    - set.pop() 随机删除集合中的一个元素. 它和列表及字典中的 pop 不一样.
        复习一下:
        - list.pop(index) 根据下标弹出列表中的一个元素, 不写下标就弹出列表末尾的元素.
        - dict.pop(key) 根据字典中的 key 值弹出一个元素, 返回值是这个 key 对应的 value.
'''
set1 = {'Apple', 'Amazon', 'Google', 'Tesla'}
set1.remove('Apple')
print(set1) # {'Google', 'Amazon', 'Tesla'}
set1.discard('Google')
print(set1) # {'Amazon', 'Tesla'}
set1.discard('Microsoft') # key 不存在, 没有反应.
print(set1) # {'Tesla', 'Amazon'}
# set1.remove('Microsoft') # KeyError: 'Microsoft'
# 所以, remove() 在使用前需要先判断一下:
if 'Microsoft' in set1:
    set1.remove('Microsoft')
else:
    print('你输入的公司不存在于集合中!')


# 4. 集合的数学运算: 交集 intersection, 并集 union, 差集 difference
# 函数使用太麻烦, 集合可以直接使用符号来运算
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
# 交集符号 &, 与: 也好理解, 就是说该元素存在于 set1 与 set2 中, 只有4, 5, 6了.
print(set1 & set2) # {4, 5, 6}
# 并集符号 |, 或: 该元素存在于 set1 或 set2 中, 所以可以是 1~9
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 差集符号 -, 减: A - B, 集合A有且集合B没有的元素.
print(set1 - set2) # {1, 2, 3}
print(set2 - set1) # {8, 9, 7} 