'''
如何定义一个列表:
1. 空列表: []
2. 非空列表: ['a', 1, 'b', True, 9.9], [[], [], []]
'''
# 注意: 列表的定义可以使用乘法 *
l = [1] * 10
print(l) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print('1.', '*-' * 30)
# 1. 列表的切片(和字符串的切片是一样的)
list = ['牛奶', '面包', '火腿肠', '辣条', '臭豆腐']
print(list[:2]) # ['牛奶', '面包']
print(list[1:-1]) # ['面包', '火腿肠', '辣条'], 同样是含头不含尾.
print(list[::-1]) # 同样的倒序排列.


# 2. 列表的增删改查
print('2.1', '*-' * 30)
## 2.1 添加元素: append, insert
'''
    - append() 在列表末尾追加元素.
    - insert() 在指定位置插入元素.
        - insert(index, object) 在指定下标元素的前面(记住, 是前面)插入新元素.
'''
print('append:')
list1 = []
list2 = ['面包']
list1.append('火腿肠')
print(list1) # ['火腿肠']
list1.append('酸奶')
list1.append('辣条')
print(list1) # ['火腿肠', '酸奶', '辣条']

list2.append('薯条')
# list1 = list1 + list2 # 直接用加号实现列表的合并!(将2个列表中的元素加到一个列表中了)
# print(list1) # ['火腿肠', '酸奶', '辣条', '面包', '薯条']
'''
总结 - 加号的用法:
1. 数字: 数学运算 n = 1 + 1
2. 字符串: 字符串的拼接 s = 'aa' + 'bb'
3. 列表: 列表的合并 list = [1, 2] + ['a', 'b']
'''
## 注: 除了用 + 实现列表元素的合并, 还可以使用 extend() 函数!
list1.extend(list2)
print(list1)
list1.append(list2) # append() 是将整个列表作为一个元素加入到另一个列表中, 注意和 extend() 区分.
print(list1)

print('insert:')
list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.insert(3, '方便面')
print(list) # ['火腿肠', '酸奶', '辣条', '方便面', '面包', '薯条']

list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.insert(-1, '方便面')
# 这里'方便面'没有插入到列表最后, 因为它插入在最后一个元素的前面!
print(list) # ['火腿肠', '酸奶', '辣条', '面包', '方便面', '薯条']

# 那么, 如何将元素插入到列表最后呢? 选择一个比列表最后一个元素还大的下标即可.
list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.insert(len(list), '方便面') # 直接用 len(list) 是最方便的, 因为列表中最后一个元素的下标是 len(l) - 1.
print(list) # ['火腿肠', '酸奶', '辣条', '面包', '薯条', '方便面']


print('2.2', '*-' * 30)
## 2.2 删除元素: pop, remove, clear, del(和 pop 类似)
'''
    - pop(index): 根据下标删除列表中的主要元素(下标不能超出范围, 否则会 IndexError)
    - remove(): 根据元素名称删除列表中的元素(从左往右删除第一个指定名称的元素, 若不存在会 VlaueError)
        - 那如何删除列表中指定名称的全部元素呢? 参见下面的代码!
    - clear(): 清空列表元素.
    - del list: 删除列表的指针.
        - del 也可以用于字符串中.
'''
print('pop:')
list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.pop(3) # 删除下标为3的元素(第4个)
print(list) # ['火腿肠', '酸奶', '辣条', '薯条']

list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.pop(-2) # 删除倒数第二个元素
print(list) # ['火腿肠', '酸奶', '辣条', '薯条']

list = ['火腿肠', '酸奶', '辣条', '面包', '薯条']
list.pop() # 如果什么都不写, 默认从列表末尾弹出一个元素(和 append 是相反的动作)
print(list) # ['火腿肠', '酸奶', '辣条', '面包']

print('remove:')
list = ['火腿肠', '酸奶', '辣条', '面包', '薯条', '酸奶']
list.remove('酸奶') # 可以看出: remove 是从左往右删掉第一个同名元素.
print(list) # ['火腿肠', '辣条', '面包', '薯条', '酸奶']

## 因为要删除的元素不存在会报错, 所以我们用 remove() 时需要先判断是否存在要删除的元素.
if '汉堡' in list:
    list.remove('汉堡')
else:
    print('不存在\'汉堡\'!')

## 删除列表中全部同名元素!
list = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶'] # 共有4个酸奶
n = 0
while '酸奶' in list:
    list.remove('酸奶')
    n += 1 # 统计共计删除多少个元素.
else:
    print('列表中的酸奶已经全部删除! 共删除%d个酸奶.' % n)
    print(list)

print('clear:')
list.clear()
print(list) # []
list.append('Apple')
print(list) # ['Apple']

print('del:')
list = ['火腿肠', '酸奶', '辣条', '面包', '薯条', '酸奶']
del list[1]
print(list)
## 在上面的用法中, del 和 pop 是等价的, 但下面的用法仅限 del:
list.clear() # 它是把列表中的内容清空
print(list, type(list)) # [] <class 'list'>
del list # 它是把整个列表删除(列表本身还在, 只是把列表的指针删除了.)
print(list, type(list)) # <class 'list'> <class 'type'>


print('2.3', '*-' * 30)
## 2.3 修改: 使用 index() 查找需要修改元素的下标, 然后直接赋值进行修改.(类似于字符串中的 find)
list = ['火腿肠', '酸奶', '拖鞋', '辣条', '面包', '薯条']
print('修改之前:', list)
i = list.index('拖鞋') # 找到需要修改的元素的位置
list[i] = '可乐' # 重新赋值, 进行修改
print('修改之后:', list)

print('2.4', '*-' * 30)
## 2.4 查找: in, index, count
'''
    - in, 判断某元素是否存在于列表中.
        - not in
    - index(object), 查找指定元素, 返回其下标.
    - count(object), 统计指定元素出现的次数, 如果列表中不存在返回0.
        - 所以可以用 count() 代替 in, 如: if s.count('a') != 0 和 if 'a' in s 是等价的.
'''
list = ['火腿肠', '酸奶', '酸奶', '辣条', '面包', '酸奶', '薯条', '酸奶'] # 共有4个酸奶
# 我们这里可以使用 count() 重构上面的循环删除的代码.
n = list.count('酸奶')
for i in range(n): # n 为0不会报错, 这里的循环不会执行.
    list.remove('酸奶')
else:
    print('列表中的酸奶已经全部删除! 共删除%d个酸奶.' % n)
    print(list)


print('3.', '*-' * 30)
# 3. 排序: sort, reverse
'''
    - sort() 对列表进行升序或者降序排序.
        - 默认是按照升序进行排序的, 如果需要降序, 需要传入关键字参数 reverse=True.
    - reverse() 就是对原列表进行倒序排序, 和切片中的 [::-1] 是一个效果.
'''
# 练习: 生成8个0-100之间的随机数, 并保存到列表中.
import random
numbers = []
def score_random():
    numbers.clear() # 每次调用此函数之前, 先将 numbers 列表清空.
    for i in range(8):
        numbers.append(random.randint(0, 100))
    else:
        print('排序之前:', numbers)

score_random() # 这样可以确保每次调用函数后, 会产生一个新的无序的列表!
numbers.sort() # 默认是升序排序.
print('sort排序:', numbers)

score_random()
numbers.sort(reverse=True) # reverse=True, 表示降序排序.
print('sort排序:', numbers)

score_random()
numbers.reverse()
print('reverse倒序:', numbers)

## 练习: 使用上面的 score_random(), 然后用键盘输入一个 1-100 之间的数字, 并保持列表有序.
score_random()
flag = True
numbers.sort()
print(numbers)
while flag:
    new_num = int(input('请输入一个0-100的数字:'))
    if 100 >= new_num >= 0:
        for i in numbers:
            if new_num < i:
                index = numbers.index(i)
                numbers.insert(index, new_num)
                print(numbers)
                break
        else:
            numbers.append(new_num) # 为了防止上面 break 之后再执行一次此代码, 用 for...else 结构!
            print(numbers)
    else:
        print('你输入的数字不在0-100范围内, 程序已退出.')
        flag = False # 使用这种方式可以在内层控制外层循环的开关, 不要轻易使用 break!