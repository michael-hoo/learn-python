import os, random
# 1. 进程
# 1.1 创建一个进程之一: fork() 此方法仅适用于 Linux/Unix/macOS 系统中
def creat_rand_num():
    os.fork() # 创建一个子进程
    num = random.randint(1, 10000)
    # os.getpid() 可以获得当前进程的 id
    print('随机数: {1} - ({0})'.format(os.getpid(), num))

# creat_rand_num()
'''
我们虽然只调用了一次上述函数, 却可以发现有两个输出结果!
    随机数 - 5337: 6467
    随机数 - 5338: 8274
这是因为我们在产生随机数之前调用了 os.fork() 函数, 这个函数非常特殊, 它的功能是为当前进程创建一个子进程, 
但是它被调用一次会产生两个返回值: 0和子进程的pid
    <0 则表示子进程创建失败
    =0 这是子进程的返回值
    >0 这是父进程中的返回值(也是子进程的pid)
特点: 
    1. 子进程会继承父进程几乎全部代码(即fork()前所定义的所有内容).
    2. 子进程有自己的独立标识符 - pid (和父进程是不一样的)
    3. 父进程, 子进程独立存在, 在各自的存储空间上运行, 互不影响.
    4. 创建子进程用来执行和父进程不同的任务是多任务中的常见方法. 
'''

# 再通过一段代码来进一步理解子进程:
def make_child_process():
    id = os.fork() # os.fork() 会产生两个返回值, 上面介绍了
    if id < 0:
        print('进程创建失败!')
    elif id == 0:
        # 获取当前进程pid的方法 -> os.getpid(); 获取父进程pid的方法 -> os.getppid()
        print('这是子进程{}, 它的父进程是{}'.format(os.getpid(), os.getppid()))
    else:
        # 父进程的返回值 id 就是它的子进程的 pid
        print('这是父进程{}, 它的子进程是{}'.format(os.getpid(), id))

make_child_process() # 注意: 这个方法和上面的方法不要同时调用, 否则会互相干扰.
'''上述函数同样有两个输出: 
    这是父进程5452, 它的子进程是5453
    这是子进程5453, 它的父进程是5452
   可见, 其实父进程的 pid 和子进程的 pid 是差不多的, 相差1.    
'''