'''
字典的定义: {'key1':value1, 'key2':value2, 'key3':value3, ...}
    - 字典没有下标或切片操作, 目前所学的数据类型中, 只有字符串/列表/元组有下标和切片操作.
    - 注意: key 是唯一的, 所以在添加的时候出现同名 key, value 会覆盖原来的值.
'''
print('1.', '*' * 25)
dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
# 1. 添加和修改
'''
    - dict[key] = value, 为 dict 添加一个新的 key-value. 
    - dict1.update(dict2), 把 dict2 中的元素全部添加到 dict1 中.
'''
dict['job'] = 'Developer'
# {'name': 'Nathan', 'age': 31, 'salary': 10000, 'job': 'Developer'}
print(dict)
dict['salary'] *= 1.2
# {'name': 'Nathan', 'age': 31, 'salary': 12000, 'job': 'Developer'}
print(dict)
# 总结: 字典的添加和修改元素是一样的操作, 如果 key 在字典中不存在, 就是添加; 若 key 已存在, 则是修改.

dict1 = {'name': 'Nathan', 'age': 31, 'salary': 10000}
dict2 = {'gender': 'M'}
# 可以看出, A.update(B) 的功能是将字典 B 中的内容添加到字典 A 中! 这个功能和列表中的 extend() 很相似.
dict1.update(dict2) 
print(dict1) # {'name': 'Nathan', 'age': 31, 'salary': 10000, 'gender': 'M'}


print('2.', '*' * 25)
# 2. 字典的删除: pop, popitem, clear
'''
    - dict.pop(key): 根据 key 来删除整个键值对, 其返回值是所删除元素的 value 值.
    - dict.popitem(): 删除字典中最后一个元素, 返回一个元组 (key, value).
        - 注: 当字典为空时, 使用此方法会抛出异常.
    - del: 类似于 pop, 系统自带的删除操作.
    - dict.clear(): 清空 dict 中的所有元素, 没有返回值.
'''
dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
print(dict.pop('age'), dict)  # 31 {'name': 'Nathan', 'salary': 10000}

dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
print(dict.popitem(), dict)  # ('salary', 10000) {'name': 'Nathan', 'age': 31}

dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
del dict['salary']  # 类似于 pop(key)
print(dict)  # {'name': 'Nathan', 'age': 31}
del dict  # 直接删除 dict 指针
print(dict, type(dict))  # <class 'dict'> <class 'type'>

dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
dict.clear()  # 清空字典中的所有元素, 没有返回值.
print(dict)  # {}


print('3.', '*' * 25)
# 3. 字典的查询
'''
    - dict.get(key): 通过 key 获取 value.
    - dict[key]: 效果和 dict.get(key) 是一样的, 二者的差别在于: 若所查询的 key 不存在,
        - dict.get(key) 会默认返回 None(还可以自定义).
        - dict[key] 会抛出 KeyError. 
'''
dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
value1 = dict.get('name')
value2 = dict['name']  # 这里二者是等价的.
print(value1, value2)

value1 = dict.get('key', -1)  # 没有找到, 返回-1
# value2 = dict['key'] # 抛出异常: KeyError: 'key'
print(value1)  # -1


print('4.1', '*' * 25)
# 4. 字典的遍历:
dict = {'name': 'Nathan', 'age': 31, 'salary': 10000}
# 4.1 对 key 进行遍历
for k in dict:  # 直接对字典进行遍历, 默认是拿到字典所有的 key
    print(k, end='\t')  # name    age     salary
print()
# 结果发现遍历出来的都是 key!

for k in dict.keys():  # dict.keys() 可以拿到字典中所有的 key, 并将其放在一个列表中!
    print(k, end='\t')  # name    age     salary
print()

print(dict.keys())  # dict_keys(['name', 'age', 'salary'])
# 可以看出, 这种方法获得的列表和标准列表有点不一样, 不过可以使用 list() 方法转化!
print(list(dict.keys()))  # ['name', 'age', 'salary']

print('4.2', '*' * 25)
# 4.2 对 value 进行遍历
for v in dict.values():  # dict.values() 会将字典中的所有 value 放到一个列表当中.
    print(v, end='\t')  # Nathan  31      10000
print()

print(dict.values())  # dict_values(['Nathan', 31, 10000])
print(list(dict.values()))  # ['Nathan', 31, 10000]

print('4.3', '*' * 25)
# 4.3 对 key-value 进行遍历
for k, v in dict.items(): # dict.items() 会将字典中的所有 key-value 放在一个元组组成的列表里.
    print('{0}\t{1}'.format(k, v))
'''
    输出结果为:
    name    Nathan
    age     31
    salary  10000
'''
print(dict.items()) # dict_items([('name', 'Nathan'), ('age', 31), ('salary', 10000)])
print(list(dict.items())) # [('name', 'Nathan'), ('age', 31), ('salary', 10000)]


print('5.', '*' * 25)
# 5. 字典和列表结合的复杂操作
role1 = {'name': 'Nathan', 'age': 31, 'salary': 10000}
role2 = {'name': 'Liyuting', 'age': 28, 'salary': 12000}
roles = [role1, role2]
print(roles)

# 删除每个人的年龄信息, 如何操作?
for role in roles:
    role.pop('age')
else:
    print(roles)

print('练习:', '*' * 25)
'''
    练习: 使用列表定义一个书架, 里面可以存放3本书, 使用字典表示每一本书.
        要求:
        1. 要可以循环添加书籍, 添加到3本停止循环, 但是, 不可添加同名书籍!
        2. 每本书中要包含书名/作者/价格信息.
'''
books = [] # 定义一个空列表, 作为书架
while True:
    if len(books) == 3: # 当书架中存放到3本书时, 停止添加.
        break
    # 手动输入需要传入的书籍信息, 一次性传入多个信息
    name, author, price = input('请输入书籍名称/作者/价格, 并用空格分隔:').split(' ') # split将字符串拆分成3部分.
    # 输入书名后, 需要先对书架进行查询, 看看书架中是否有同名书籍!
    for book in books: # 遍历书架 books, books 为空时此循环会直接跳过.
        if name == book.get('name'): # 判断书名是否重复
            print('书名重复, 请重新输入!')
            break
    else: # for循环体没有被中断过才会执行 else
        books.append({'name': name, 'author': author, 'price': price})
        print('书籍《%s》已加入书架' % name)
        print('^' * 30)

# 读取书架中的内容, 并展示
print('书架中共有%d本书, 基本信息如下:' % len(books))
for book in books: # books 是一个列表, book 是列表中的字典!
    print('《{0}》作者: {1}, 价格: {2}'.format(book.get('name'), book.get('author'), book.get('price')))

