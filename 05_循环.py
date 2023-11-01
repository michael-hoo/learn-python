print('for...else:', '*' * 30)
# 1. for...else 结构
for i in range(3):
    # password = input('请输入您的密码：')
    password = '1234'
    if password == 'password':
        print('登录成功！')
        break # 密码验证成功，直接跳出循环，else语句便不会再执行。
    print('密码错误！')
else: # 注：只有循环体中的代码正常结束(没被打断)时，else 中的语句才会被执行。
    print('手机暂被锁定，1分钟后再试！')

## 同理，也有 while...else 结构。

print('while True:', '*' * 30)

'''
    while 和 for 循环的区别：
    - 当循环次数固定时，优先使用 for (所以 for 循环也可以也可称为迭代、遍历……)
    - 当循环次数不固定(但有条件)时，优先使用 while 循环。
'''
n = 0
while True:
    print(n)
    n += 1
    if n == 3:
        break

print('break and continue:', '*' * 30)

# 2. 跳出语句：break 和 continue
## continue 是想要正常完成循环，只排除/过滤某些不想要的结果。
## break 只想从众多结果中找到自己想要的，并不要求完整跑完循环。
# 例子：打印 1～10 中不能被3整除的数字。
for i in range(1, 11):
    if i % 3 == 0: # 整除就是取余为0.
        continue # 通过这种方式把可以被3整除的数字过滤掉。
    print(i)

print('循环的嵌套:', '*' * 30)

# 3. 循环的嵌套
'''
    练习：要求打印如下图形。
    *
    **
    ***
    ****
    *****
'''
## 方法一：丑陋的方法
i = 1 # i 用来控制行数
s = '*'
while i <= 5:
    print(s)
    i += 1
    s += '*' # 字符串的拼接

print('*' * 30)

## 方法二：机智的方法！
n = 1
while n <= 5:
    print('*' * n) # 直接用循环变量控制打印的 * 数量！
    n += 1

print('*' * 30)

## 方法三：循环的嵌套
n = 1
while n <= 5: # 利用外层循环控制行。
    m = 1
    while m <= n: # 利用内层循环控制打印，利用 m 和 n 的差值对比，来控制当前行打印的次数。
        print('*', end='') # 内层循环没进行一次，就打印一颗星，这里不换行，换行由外层循环控制。
        m += 1
    n += 1
    print() # 在外层循环中控制换行，外层循环每执行一次就换一次行。

print('练习一:', '*' * 30)

'''
    练习一：打印如下图形。
    *****
    ****
    ***
    **
    *
'''
## 方法一：聪明的办法
n = 0
while n < 5:
    print('*' * (5-n))
    n += 1

print('*' * 30)

## 方法二：循环的嵌套
n = 0
while n < 5:
    m = 5
    while m > n:
        print('*', end='')
        m -= 1
    n += 1
    print()

print('练习二:', '*' * 30)
'''
    练习二：打印九九乘法表。
'''
n = 1
while n <= 9:
    m = 1
    while m <= n:
        print('%d * %d = %d' % (n, m, n*m), end='\t')
        m += 1
    n += 1
    print()