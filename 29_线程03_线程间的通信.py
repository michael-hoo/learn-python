'''生产者与消费者: 用来实现两个线程之间的通信.
 - 可以使用队列来实现线程间的同步(和进程很相似).
 - Python 的 queue 模块中提供了同步的/线程安全的队列类, 包括 FIFO(先入先出)队列 Queue, 
   LIFO(后入先出)队列 LifoQueue 和优先级队列 PriorityQueue, 这些队列都实现了锁原语
   (可以理解为原子操作, 要么不做, 要么就做完), 能够在多线程中直接使用.
'''
from random import randint
from time import sleep
from queue import Queue
from threading import Thread

# 生产者要执行的方法
def produce(q):
    i = 0
    while i < 6:
        # 随机产生一个 1~100 的整数, 并存往队列中.
        num = randint(1, 100)
        q.put(num)
        print('{}. 生产者产生数据: {}'.format(i, num))
        sleep(1)
        i += 1
    q.put(None) # 这里往队列中 put 一个空值, 是为了 consume() 方法中的循环结束判断.

# 消费者要执行的方法
def consume(q):
    while True:
        num = q.get()
        if num is None:
            break
        print('消费者取到数据: %d' % num)
        sleep(2)
    # 完成任务
    q.task_done() # q.task_done() 与 q.join() 有关, 起标记作用, 具体用法以后再说吧~

if __name__ == '__main__':
    q = Queue(6)

    # 创建生产者线程
    th1 = Thread(target=produce, args=(q, ))
    th1.start()
    # 创建消费者进程
    th2 = Thread(target=consume, args=(q, ))
    th2.start()

    # q.join()
    th1.join()
    th2.join()
    print('主线程结束!')