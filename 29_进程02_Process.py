# 1.2 创建一个进程之二: Process
import os
from multiprocessing import Process
"""我们可以通过 Process 类创建一个进程对象
    创建对象时可以传入的参数: 
     - target: 用来指定子进程要执行的方法.
     - name: 用于定义子进程的名字(可以通过 p1.name, p2.name 来调用传入的属性).
     - args: 用于在调用方法时, 给该方法传参.
        - 注意: 这里传入的 args 参数需要是可迭代的, 如果只传入一个参数, 要以元组的方式来传入!   
    进程对象的常用方法: 
     - p.start(): 启动进程并执行任务
     - p.run(): 只是执行任务, 并没有启动进程(调用 start 会自动执行 run)
        - start() 和 run() 之间的关系和 __new__ 同 __init__ 的关系很相似!
     - p.terminate(): 强制终止进程
     - p.join(): 会阻塞后续代码(当然也会阻塞主进程), 直到调用 join() 方法的子进程执行完毕.
        - 此方法常用于进程间的同步!
"""
# 创建子进程要执行的任务
def run_proc(name):
    # os.getpid()是获取当前进程ID, 同理, os.getppid()是获取父进程的ID.
    print('正在运行子进程{}({})...'.format(name, os.getpid()))

if __name__ == '__main__':
    print('正在运行父进程({})...'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('子进程将要开始运行...')
    # 通过 Process 类只是创建了一个子进程, 调用 start() 方法才会运行子进程.
    p.start()
    # join() 方法会阻塞主进程直到子进程运行结束, 常用于进程间的同步!
    p.join() # 可以把此行注释掉, 看看下一行代码执行顺序有何不同?
    print('父进程结束!')
    """问: 子进程用完后需要手动关闭吗?
        一般不用, 因为子进程和主进程一样, 执行完毕之后就会释放掉, 你 print 一行代码后需要关闭吗? 
        除非你让子进程去执行一些死循环任务时, 可以达到某条件之后, 让其强行结束 -> p.terminate()
    """