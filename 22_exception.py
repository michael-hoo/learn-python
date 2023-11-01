
# 1. 异常处理 try...except...finally
'''
格式:
    try:
        pass # 此处写可能会出现异常的代码
    except:
        pass # 如果有异常会执行此处代码
    finally:
        pass # 无论有无异常, 最终都会执行的代码
'''
def func():
    try: # 以下是可能会出现异常的代码
        n1 = int(input('请输入第一个数字:')) # 程序没有语法错误, 但用户在这里输入字母就会报错
        n2 = int(input('请输入第二个数字:'))
        sum = n1 + n2
        print('{0}加{1}的和是{2}'.format(n1, n2, sum))
    except: # 如果发生异常, 执行此处代码
        print('请确保您输入的是数字, 而不是字母或字符!!!')
    finally: # 不论是否出现异常, 此处的代码都会执行
        print('finally'.center(50, '*'))

# func()
'''
这样进行异常处理的好处是, 即便某部分代码出现了异常, 也不影响整个程序的运行.
'''

## 1.1 对于异常的精细捕获
def func():
    try: 
        n1 = int(input('请输入第一个数字:'))
        n2 = int(input('请输入第二个数字:'))
        operator = input('请输入您想要的计算方式(+ - * /)')

        if operator == '+':
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
        elif operator == '-':
            print('{} - {} = {}'.format(n1, n2, n1 - n2))
        elif operator == '*':
            print('{} * {} = {}'.format(n1, n2, n1 * n2))
        elif operator == '/':
            print('{} / {} = {}'.format(n1, n2, n1 / n2))
        else:
            print('请重新选择您想要的运算方式:')
            func() # 这里不想写循环了, 用递归试试
    except ValueError: # 数值输入问题用 ValueError 来捕获
        print('请输入数字!')
    except ZeroDivisionError: # 除数不能为零用 ZeroDivisionError 来捕获
        print('除数不能为零!')
    # 但总有些异常我们想象不到, 所以这里可以用 Exception 捕获剩余一切异常(Exception 是其他异常的父类)
    except Exception as err: # 如果想知道错误原因, 可以加上 as err. 这样既能知晓为何错? 又不影响程序运行.
        print('未知错误...', err)
    else: # else 和 finally 的区别在于: 不报异常才会执行 else, 但 finally 不管报不报异常都会执行.
        pass
    finally:
        pass

# func()

## 1.2 finally 的应用场景
'''
当我们在进行文件操作的时候, 如果在读文件时 open('xxx', 'r') 文件不存在, 则会报错, 这时 close() 方法没有调用, 
就会造成内存的浪费. 而我们可以在 finally 中调用 close() 方法, 这样不管是否出异常, 都能确保文件被关闭.

当然, 使用 with...as 语句就不用考虑 close 的问题了.
'''
def func():
    try:
        return 1
    except Exception as err:
        print(err)
    finally:
        return 3

x = func()
print(x) # 3
'''
为何这里返回3而不是1?
 - 因为 finally 非常特殊, 它是一定会被执行的. 
 - 即便 try 语句中已经 return 了, 但只要程序看到了 finally, 它就不会将它看成真的 return.
 - 而是继续执行 finally, 直到遇到了 finally 中的 return!
 - 可以简单理解为, finally 中的 return 将 try 中的 return 覆盖了.
'''


# 2. 抛出异常 raise
def register():
    # input_name = input('输入用户名:')
    input_name = 'admin'
    if len(input_name) < 6:
        raise Exception('用户名至少为6位!') # 主动抛出异常一般用自定义异常类, 后面会细说.
    else:
        print('您的用户名是%s!' % input_name)

try:
    register()
except Exception as err:
    print(err)
    print('注册失败!')
else:
    print('注册成功!')