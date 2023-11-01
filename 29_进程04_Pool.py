# 1.4 进程池 Pool: 如果一次需要大量进程, 使用进程池会比较方便.
import time, random, os
from multiprocessing import Pool

def long_time_task(name):
    print('运行任务[%s](%s)...' % (name, os.getpid()))
    # 任务开始时间的时间戳
    start = time.time()
    time.sleep(random.random() * 2) # random.random() 产生一个 0~1 的随机数
    # 任务结束时间的时间戳
    end = time.time()
    print('任务[%s]执行完毕, 耗时%0.2f秒.' % (name, end - start))

if __name__ == '__main__':
    print('父进程(%s)正在运行...' % os.getpid())
    '''通过 Pool(n) 来创建进程池:
     - 这里的 n 表示进程池中最多可以同时运行的进程数, 默认是当前电脑 CPU 的核心数.
    '''
    p = Pool() # 可以看出, 我的电脑是4核的!
    for i in range(1, 10):
        # 利用循环来不断给进程池中的子进程分配任务.
        p.apply_async(long_time_task, args=(i, ))
        '''对比一下 Process 和 Pool 可以发现: 
         - Process 在创建进程时麻烦一点, 调用进程时只需 p.start()
         - Pool 在创建进程时很简单, 但在调用进程时需要 p.apply_async(func, args=(xxx, ))
        '''
    print('等待子进程执行完毕...')
    '''注意这两句代码: 
        p.close()
        p.join()
     - 这两句代码在进程池中是必不可少的, 且先后顺序要不可以调, 先 close 再 join.
     - p.close(): 进程池用完之后必须要关闭, 否则会报错"ValueError: Pool is still running"
     - p.join(): 不同于 Process, 进程池和主进程是"同生共死"的, 也就是说, 一旦主进程结束了, 不管
       进程池中的任务是否完成, 进程池也同时会被关闭, 所以, 这里需要阻塞一下主进程.
    '''
    p.close()
    p.join()
    print('所有子进程运行结束!')
    print('父进程运行结束!')