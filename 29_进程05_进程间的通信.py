# 1.5 进程间的通信
'''Queue 和 Pipes
   由于全局变量在进程之间是相互独立的, 无法帮助我们实现进程间的通信, 而 Python 中的
   multiprocessing 模块提供了 Queue/Pipes 等多种方式帮助我们实现进程间的通信!
'''
import time, os, random
from multiprocessing import Process, Queue

# 写数据进程执行的代码
def write(q):
    print('写进程(%s)正在运行...' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('往队列里写入数据: [%s]' % value)
        # 往队列中写入数据使用队列的 put() 方法!
        q.put(value)
        time.sleep(random.random() * 3)

# 读数据进程执行的代码
def read(q):
    print('读进程(%s)正在运行...' % os.getpid())
    while True:
        # 从队列中读取数据使用队列的 get() 方法!
        value = q.get()
        print('从队列中读取数据: [%s]' % value)

if __name__ == '__main__':
    # 通过父进程创建一个队列, 并将其传给子进程
    q = Queue(2)
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join() # 后续代码等 pw 进程结束后才会执行
    # 由于 pr 执行的是个死循环, 所以不能用 join 而要用 terminate 强行终止.
    pr.terminate() # pw 结束后, 把 pr 强行终止.

'''代码逻辑分析:
 - 子进程的创建这里就不再赘述了, 同上面的区别仅在于这里传入了一个参数: 队列 q.
 - pw 写进程执行了 write 方法, 通过循环往队列中写入三个字母 A, B, C, 这里使用 sleep() 
   是为了模拟现实情况中可以读写同时进行, 不加 sleep() 写进程会在读进程执行之前就写完了.
 - pr 读进程是使用死循环来不断从读列中读取数据, 分析一下 get(block=True, timeout=None):
    - get 方法的 block 参数默认为 True, 表示阻塞, 即如果取不到数据, 这个进程就一直卡着...
    - timeout 参数后面可以加数字, 但加了会抛出超时异常.
    - 一般这两个参数取默认值就好.
 - pw.join() 指后面的代码先不执行, 等写进程结束后再继续执行后续代码.
    - 这里是为了防止后面的 pr.terminate() 把读进程先终止了.
'''