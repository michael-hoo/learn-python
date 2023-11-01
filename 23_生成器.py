'''
集合推导式 -> 类似于列表推导式, 多了一个去重功能.
 格式: 将列表推导式的 [] -> ()
'''
l = [1, 1, 2, 3, 5, 5, 7]
s = {x for x in l}
print(s)  # {1, 2, 3, 5, 7}, 集合会自动去重.
s = {x*x for x in l}
print(s)  # {1, 4, 9, 49, 25}, 集合是无序的.
s = {x for x in l if x > 3}
print(s)  # {5, 7}

'''
字典推导式
'''
# 练习: 对于一个字典, 我想交换它的 key 和 value, 怎么办?
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {v: k for k, v in d1.items()}
print(d2)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# 如果 value 有重复的, 可以交换吗?
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 3}  # 'd': 3
d2 = {v: k for k, v in d1.items()}
print(d2)  # {1: 'a', 2: 'b', 3: 'd'}
# 也可以, 不过 key 值重复会丢失相关数据, 这里丢失的是 'c': 3, 为什么丢失的是它呢?
# 可以这样理解, 先存入字典的是 3: 'b', 但又来了个 3: 'd' 将其覆盖了.


'''
生成器
 - 为什么需要生成器?
   虽然我们可以通过列表推导式直接创建一个列表, 但是, 受内存限制, 列表容量肯定是有限的, 比如, 创建一个包含100万个元素的
   列表就会占用很大空间. 如果列表元素可以通过某种算法推算出来, 那我们能否只在需要用到的时候再推算出列表后续元素呢? 
   这样就不用创建完整的 list, 从而节省了大量空间. 
   而在 Python 中, 这种一边循环一边计算的机制, 就成为"生成器", 即 generator. 
 - 如何创建生成器?
   1. 通过列表推导式得到生成器.
   2. 用函数定义生成器.
'''
# 1. 通过列表推导式得到生成器
# 练习: 我们需要得到一个等差数列 [0, 3, 6, 9, 12, 15, ...] 应该怎么做?
l = [i for i in range(0, 20, 3)]
print(l)  # [0, 3, 6, 9, 12, 15, 18]
# 而生成器只需要将列表推导式的 [] -> () 即可
# g = (i for i in range(0, 20, 3))
g = (i*3 for i in range(10)) # 这个方法比上面的更好
print(g)  # <generator object <genexpr> at 0x103b17510>, 这是一个生成器.
# 这个生成器应该怎么用呢? 可以通过 __next__() 方法来得到一个生成器元素.
print(g.__next__())  # 0
print(g.__next__())  # 3
print(g.__next__())  # 6
# 可以看到: 每调用一次 g.__next__() 方法, 就会产生一个元素.

# 另外一种使用生成器的方式: next(g)
print(next(g))  # 9
# 可以看出: 这里 next(g) 产生的值是接着上面 g.__next__() 的.
# 注意: 生成器产生的元素读完了, 再调用 next(), 会抛出异常 StopIteration.

print('*' * 30)

g = (i*3 for i in range(10))
def run_generator():
  while True:
      try:
        print(next(g))
      except: # 这样就可以处理因为调用生成器而产生的异常问题.
        print('没有更多元素了.')
        break

run_generator()


# 2. 用函数定义生成器 yield
'''
一个函数中只要用了 yield 关键字, 就意味着它不再是函数, 而是一个生成器.
'''
def func():
  n = 0
  while True:
    n += 1
    return n

print(func()) # 1
print(func()) # 1
# 上面虽然定义了一个死循环, 但是 return 语句会及时"打断"函数, 所以函数的返回值为1, 且无论调用多少次都不会变.
# 只要把上面的 return 换成 yield, 原函数就会变成一个生成器. 
'''
⭐️ return 和 yield 之间的区别可以这样理解:
 - return 是直接终止函数的运行.
 - yield 是中断函数的运行, 且保留这个断点, 下次调用 next() 时, 会从这个断点处继续运行.
 下面将函数改写成一个生成器.
'''
def func():
  n = 0
  while True:
    n += 1
    yield n

print(func()) # <generator object func at 0x10abc0c40>, 确实变成生成器了.
g = func()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3

# 练习: 使用生成器写一个斐波那契数列
def fib():
  i, j = 1, 0 # i 用来不断产生斐波那契数列, j 只是辅助.
  while True:
    i, j = i+j, i
    yield i

g = fib()
for i in range(10):
  print(next(g), end=' ')

'''
总结 - 生成器的方法: 
- __next__()
- send(value): 用于传参, 不太理解, 后续用到再查吧.
'''

print()
print('*' * 30)

# 3. 生成器的应用: 协程 (进程 > 线程 > 协程)
# 练习: 在搬砖的同时进行听歌
def task1(n):
  for i in range(1, n):
    print('正在搬第{}块砖!'.format(i))
    yield # 这里可以只用 yield 的暂停功能, 不往外传值.

def task2(n):
  for i in range(1, n):
    print('正在听第{}首歌!'.format(i))
    yield

g1 = task1(9)
g2 = task2(5)
# 如果只是常规函数的话, 这里一定是顺序执行的, 先执行9次 task1(搬砖), 再执行5次 task2(听歌), 不可交叉进行
# 所以, 要在函数中加 yield
while True:
  try:
    g1.__next__()
    g2.__next__() # 这样便可以实现任务的交叉进行!!! ⭐️
  except: # 不断调用 __next__() 最后一定会报错, 所以进行一下异常处理.
    break # 这里只是不想看到报错信息, 所以不写代码也可以.