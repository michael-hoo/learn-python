'''
目录:
1. 引用
2. 闭包
    - 嵌套函数
    - nonlocal
    - 闭包的定义(三要素)
3. 装饰器
    - 
'''
print('1**' * 20)
# 1. 引用和函数参数的引用
## sys.getrefcount(a): 查看有几个指针指向 a 所对应/指向的对象.
import sys

l1 = [1, 2, 3, 4, 5]
l2 = l1 # 这里实际是将 l1 的地址赋值给 l2
l3 = l1
print(id(l1), id(l2), id(l3)) # 这三个值相等, 说明指向的是同一个对象.

print('数量:', sys.getrefcount(l1)) # 数量: 4
# 为什么是4个, 而不是3个? 因为调用 getrefcount(l1) 方法中已经有一个了.

del l3 # 删除一个指针
print('数量:', sys.getrefcount(l1)) # 数量: 4


print('2**' * 20)
# 2. 闭包
# 闭包是一种特殊的函数嵌套, 所以我们先看看函数嵌套是什么?
## 2.1 函数嵌套
def outer():
    a = 100
    def inner():
        b = 200
        print('I am inner!')
'''
为什么函数可以以这种方式定义?
- 因为函数本身也可以看成一个变量, 可以尝试 print(outer, inner). 
- a 是个变量, 可以定义在 outer() 函数中, inner 也是一个变量, 自然也可以!
'''
# print(outer, inner) # NameError: name 'inner' is not defined. 这里会报错, 因为 inner 是定义在函数内部的.
# print(a) # 正如你也无法在函数外部打印变量 a 一样.
print(outer) # <function outer at 0x10e7c05e0>

# 对函数进行修改
def outer():
    a = 100
    def inner():
        b = 200
        print('I am inner!')
    print(a, inner) 

outer() # 调用 outer 后, 这样就可以打印 a 和 inner 了

### 2.1.1 locals()
def outer():
    a = 100
    def inner():
        b = 200
        print('I am inner!')
    # locals(): 查看函数内部的局部变量. 它会将函数内部定义的变量名和值以字典的形式存储起来.
    print(locals()) # {'a': 100, 'inner': <function outer.<locals>.inner at 0x1019687c0>}

outer()

### 2.1.2 nonlocal
# 继续对以上代码进行重构...
def outer():
    a = 100
    def inner():
        nonlocal a
        b = 200
        b += a # 内部函数可以调用外部函数的变量, 但不可以修改(和全局变量/局部变量一个逻辑)
        a += 1 # # 如果非要修改, 可以在上面加个 nonlocal
        print('I am Inner!', 'b =', b, 'a =', a)
    inner()

outer()
# 运行结果: I am Inner! b = 300 a = 101

## 2.2 闭包的定义
'''
闭包满足以下三个条件: 
1. 它是一个嵌套函数;
2. 内部函数引用了外部函数的变量;
3. 返回值是内部函数.
以下就是一个典型的闭包.
'''
def outer(n):
    a = 10

    def inner():
         b = a + n
         print('Inner():', b)

    return inner

result = outer(5)
print(result) # <function outer.<locals>.inner at 0x102c107c0>
# result 是内部函数的地址, 调用之后产生计算结果.
result() # Inner(): 15

## 2.3 闭包有什么用呢? 在装饰器里会用到


print('3**' * 20)
# 3. 装饰器
'''
为什么要用装饰器?
因为写代码要遵循"开放封闭"的原则, 虽然这个原则主要用于面向对象开发, 但对于函数式编程也适用, 简单来说, 
它规定已经实现的功能的代码不可以被修改,但可以被扩展, 即:
- 封闭: 已实现的功能代码块.
- 开放: 对扩展开放.
而通过装饰器, 我们可以实践这一原则! 即装饰器可以使我们在不修改其他函数代码的前提下, 扩展其功能!
'''
## 3.1 定义装饰器: 装饰器相对于闭包有个不同在于, 装饰器的外部函数需要可以传入一个(函数)参数.
def decorator(func):
    print('->' * 20)
    def wrapper():
        func() # 这个应该是调用装饰器的函数.
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('房子已经精装修...')
    print('->' * 20)
    return wrapper

# 这里的操作是这样的: house = decorator(house)
@decorator # 装饰器的使用方法: 直接用 @ 加上你定义的装饰器的函数名即可
def house():
    print('毛坯房...')

# house()
'''
装饰器的执行逻辑:
- 装饰器 decorator 和函数 house 定义完毕后, 即便不对这两个函数调用, decorator 也会被执行(可以看第117/125行的代码输出)
- 这是因为 house 函数上方用了 @decorator, 你可以理解为它已经调用了 decorator(), 并将 house 的函数名作为参数传入了, 即:
    - house -> decorator(func) -> decorator(house)
    - 它这里是把 house 指向的函数的地址赋值给了 func (注意区分函数在内存的实体和函数变量名的区别).
    - 所以, wrapper() 已经知道 house 需要执行的代码了, 并将函数调用封装在其中的 func() 当中!
    - 并且, 这之后装饰器会将 house 这个变量的指针指向 wrapper()!!! 即 house = wrapper
        - 这一步是 return wrapper 实现的.
        - 这也是为何下面调用 house() 时, 实际执行的却是 wrapper()!
- 但由于 decorator 内部定义了一个内部函数, 并将内部函数进行返回, 返回的是 wrapper 函数变量, 而非对其调用.
- 但当我们调用 house() 时, 装饰器内部的函数 wrapper() 才会被调用, 并且 wrapper() 会在其内部调用 house(), 所以, 
  它可以通过在 house() 之前或之后加入代码, 从而实现对 house() 功能上的扩展, 并且, 没有对 house() 的代码改动.
- 这就是对"开放封闭"原则的应用!!!
'''

## 3.2 装饰器的常用功能
'''
常用功能:
- 引入日志
- 函数执行时间统计
- 执行函数前的预备处理
- 执行函数后的清理功能
- 权限校验等场景
- 缓存
'''

## 3.3 带参数的装饰器
def decorator(func):
    # 给 wrapper 加入 *args 和 **kw, 这个装饰器就是万能的, 可以传入任何参数!
    def wrapper(*args, **kw): # 定义一个可变参数, 就可以对有任意数量参数的函数使用了!
        print('准备装修...')
        func(*args, **kw) # 这里也要用 *, 因为传入多个参数是以元组的形式传入的, 需要拆包.
        print('正在精装修房子...')
        print('装修成功!')
    return wrapper

@decorator
def house(address):
    print('房子的地址在{}, 是一个毛坯房'.format(address))

@decorator
def factory(address, area):
    print('工厂的地址在{}, 面积约{}平方米'.format(address, area))

house('淮南东方蓝海')
factory('淮南化肥厂', 10000)

## 3.4 带返回值的装饰器
def decorator(func):
    def wrapper(*args, **kw):
        r = func(*args, **kw) # 这里用 r 来接收原函数的返回值, 然后在下面 return 出去, 等于是返回值的传递.
        print('预计装修费用是:{}元'.format(r))
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('房子已经精装修...')
        return r
    return wrapper

def house():
    print('我是一个毛坯房!')
    return 100000

cost = house()
print(cost)


print('4**' * 20)
# 4. 递归函数: 如果一个函数在内部不调用其他函数, 而是调用自己本身的话, 这个函数就是递归函数.
'''
递归需要遵循的原则: 
1. 必须要有"出口"(要有明确的结束条件).
2. 每次递归需要向"出口"靠近一步.
'''
def test(i):
    if i <= 0:
        return '*'
    print('*' * i)
    return test(i - 1)

test(5)
# 注意: 递归函数需要有明确的结束条件, 否则就会报栈溢出异常(RecursionError: maximum recursion depth exceeded)

# def test(i=0):
#     print(i)
#     return test(i + 1)

# test()
# 经过我自己测试, 加上上网查询, 知晓: Python 大概在执行1000次递归后就会报栈溢出.


'''
利用递归实现九九乘法表!!!
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

test()

print()
# 练习: 使用递归实现斐波那契数列 1, 1, 2, 3, 5, 8, 13, 21, 34...
def test(i=1, j=0):
    if i > 1000:
        print()
        return
    print(i, end=' ')
    return test(i+j, i)

test()


print('5**' * 20)
# 5. 匿名函数 lambda
'''
匿名函数的定义格式: 
    lambda 参数列表: 运算表达式(返回值表达式)
'''
def test(a):
    return a + 1

t1 = lambda a: a+1
print(t1(3)) # 4

t2 = lambda x, y: x * y
print(t2(2, 3)) # 6

'''
匿名函数的使用场景: 
- 常用在高阶函数中, 作为参数传递. 下面举例说明:
'''
# 定义了一个高阶函数 func
def func(a, f):
    print('->' * 10, a)
    r = f(a) # 传入的参数 f 是一个函数, 则此函数 func 就是高阶函数.
    print('->' * 10, r)

# 当我们需要调用某高阶函数, 且其中一个参数需要传入函数时, 刚好没有合适的函数可以用, 这时就可以自己写一个匿名函数!
func(8, lambda x: x*x)


print('6**' * 20)
# 6. 高阶函数
'''
什么是高阶函数?
- 在 Python 中, 函数也是一种数据类型 - function 型.
- 之前我们也学习过, 函数名也是一种变量名, 它们本质上都是指向一块内存地址的指针. 
- 所以, 函数也可以作为函数参数进行传递!
- 把其他函数作为参数传递的函数, 我们就将其成为"高阶函数", 比如上面的 func().
'''
print(type(func)) # <class 'function'>, 函数是 function 型的.

'''
系统中提供了哪些高阶函数? 
- max/min/sorted

'''
# 6.1 max/min/sorted
l = [('Nathan', 31), ('Mike', 65), ('Tom', 33), ('Rose', 18)]
# 我想找出列表 l 中的最大年龄?
max_age = max(l, key=lambda x: x[1])
'''
    分析代码逻辑:
    - max()函数的第一个参数是可迭代对象, 所以, 当我传入 1, 2, 3, 5 这样多个参数时也是可以的, 它会以元组的形式传入.
    - max()函数的第二个参数 key 后面需要传入一个函数, 这里传入了一个匿名函数.
        - 而传入这个函数的作用是: 对每个可迭代对象(iterable), 均使用 key 后面的函数处理后, 再选出最大值.
        - 也就是说, 这里是对列表 l 中的每一个元素先用 lambda 函数处理一下.
            - 而这里的 lambda 公式的意义是: 你每给我一个 x, 我返回一个 x[1].
            - 而刚好 l 中的每一个元素都是一个元组, x[1] 对应的是其年龄部分. 
            - 也就是说, lambda 函数处理过的结果是 [31, 65, 33, 18], 然后再执行 max([31, 65, 33, 18])!
    - 当然, 这里返回的是 ('Mike', 65), 而不仅仅是 65, 可能是 max() 不会对可迭代对象本身发生修改. 
    - 底层的原理以后再说.
'''
print(max_age) # ('Mike', 65)

# 同理, 我想找出列表最小年龄, 可以这样:
min_age = min(l, key=lambda x: x[1])
print(min_age) # ('Rose', 18)

# 同理, 如果我想把上面的列表按照年龄排序, 可以这样:
l1 = sorted(l, key=lambda x: x[1]) # sorted() 和 l.sort() 不一样, 它有返回值(是排序后的列表), 所以需要接一下.
print(l1) # [('Rose', 18), ('Nathan', 31), ('Tom', 33), ('Mike', 65)]
# 同样的, 按照年龄反向排序, 可以加上关键字 reverse=True.
l2 = sorted(l, key=lambda x: x[1], reverse=True) # [('Mike', 65), ('Tom', 33), ('Nathan', 31), ('Rose', 18)]
print(l2)

# 6.2 filter() 过滤函数
l = [('Nathan', 31), ('Mike', 65), ('Tom', 33), ('Rose', 18), ('李雨婷', 20)]
result = filter(lambda x: x[1] > 20, l)
'''
    分析代码逻辑:
    - filter()函数同样需要传入两个参数:
        - 第一个参数是过滤方法(是个函数), 且这个方法的返回值必须为 True/False.
            - 返回值为 True, 则该元素可以留下来.
            - 返回值为 False, 则该元素被过滤掉.
        - 第二个参数为一个可迭代对象, 过滤方法会逐一作用到这个可迭代对象中的每一个元素上.
    - filter()函数的返回值也是一个 filter, 所以直接打印 result 会返回 <filter object at...>
    - 但是对于可迭代对象, 我们可以将其强转为 list, 就可以看到其中的结果了! list(filter object)
'''
print(result) # <filter object at 0x10ab57400>
print(list(result)) # [('Nathan', 31), ('Mike', 65), ('Tom', 33)]

# 6.3 map() 映射
l = [('Nathan', 31), ('Mike', 65), ('Tom', 33), ('Rose', 18), ('李雨婷', 20)]
result = map(lambda x: x[0].title(), l)
'''
    分析代码逻辑:
    - map()函数的格式和 filter() 类似, 第一个参数是函数, 第二个参数是可迭代的执行对象.
    - 不同的是, map() 是用传入的函数(这里是 lambda 函数)对可迭代对象依次进行处理.
    - 比如, 这里是将每个元素(都是元组)的第一个元素首字母大写, 并提取出来.
        - 下面的代码是将每个元素的第二个元素加10, 并提取出来.
    - 需要注意的是, map() 的返回值也是 map, 它也是个可迭代对象, 所以可以通过 list(map) 进行强转.
'''
print(result) # <map object at 0x1026d37f0>
print(list(result)) # ['Nathan', 'Mike', 'Tom', 'Rose', '李雨婷']
result = map(lambda x: x[1]+10, l)
print(list(result)) # [41, 75, 43, 28, 30]
'''
    有个问题: 如果我想同时对 x[0], x[1] 进行处理该怎样操作呢?
    就是返回值还是列表包着元组.
'''

# 6.4 reduce()
# 它不是系统函数, 需要额外导入一下.
from functools import reduce

result = reduce(lambda x,y: x+y, [1, 2, 3, 4, 5])
'''
    分析代码逻辑: 
    - reduce() 和 map(), filter() 格式上很接近, 都是两个参数:
        - 第一个参数是执行操作的函数.
        - 第二个参数是待执行对象.
    - 不同的是, reduce() 传入的函数参数需要具有两个参数, 因为它需要不断从操作对象中选出两个元素进行迭代运算.
    - 就拿 reduce(lambda x,y: x+y, [1, 2, 3, 4, 5]) 来说吧:
        - reduce 先从列表中取出两个元素 1,2 并使用 lambda 函数对它们进行处理, x+y -> 1+2
        - 然后, reduce 将上面计算后的结果(1+2), 也就是3, 当成第一个元素, 再从列表中拿出一个元素3作为第二个元素.
        - 继续用 lambda 函数来处理: x+y -> 3+3, 结果为6.
        - 后续的操作是一样的: 
            - 6作为第一个元素, 4作为第二个元素, 6+4 -> 10.
            - 10作为第一个元素, 5作为第二个元素, 10+5 -> 15.
            - 列表中没有元素了, 所以返回最终结果 15.
'''
print(result) # 15, reduce()返回的是一个具体结果, 而不是像 map()/filter() 那样返回可迭代对象, 所以不需要用 list().
'''
reduce() 还有什么用?
- 目前看来, 计算累加/累乘, reduce 还是挺方便的.
- 还有什么功能呢? 再试试字符串拼接.
'''
# 比如, 计算 1~10 的累乘(10的阶乘).
result = reduce(lambda x,y: x*y, range(1, 11))
print(result) # 3628800

# 实现字符串拼接
# l = ['', '*', '**', '***', '****', '*****']
l = ['*' * i for i in range(10)] # 使用这种方式生成不比上面酷?
print(l)
result = reduce(lambda x,y: x+y+'\n', l)
print(result) # 哈哈, 也可以

# 6.5 zip() 打包函数
'''
zip()函数格式:
    zip(iterable1, iterable2, iterable3, ...)
    zip() 函数可以传入任意个可迭代对象作为参数, 然后按照下标将它们一一对应起来, 下面用代码进行详细介绍.
'''
l1 = ['a', 'b', 'c', 'd', 'e'] # 5个元素
l2 = [1, 2, 3, 4, 5, 6, 7] # 7个元素
l3 = ['甲', '乙', '丙', '丁', '戊', '己'] # 6个元素

z = zip(l1, l2, l3)
print(z) # <zip object at 0x1103b1b00>
print(list(z))
# 返回结果是: [('a', 1, '甲'), ('b', 2, '乙'), ('c', 3, '丙'), ('d', 4, '丁'), ('e', 5, '戊')]
'''
    分析代码逻辑:
    - 不难看出, zip() 函数是将列表 l1,l2,l3 中的每一个元素, 按照下标打包成一个个元组了.
        - 比如, l1,l2,l3 中的第一个元素分别是 'a', 1, '甲' -> ('a', 1, '甲')
    - 并且, 如果每个列表中的元素不一样, zip() 返回的列表长度会与最短的列表相同, 其他列表多余的元素会丢失.
    - zip() 的返回值是一个 zip 对象, 它也是可迭代对象, 所以也可以用 list() 进行强转.
    - 强转后的格式是: list(zip object)
        - [(), (), (), (), ...]
'''