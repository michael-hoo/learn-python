# 线程
'''线程的创建和使用
 - 线程的创建和使用同进程很相似:
    - 创建进程: p = Process(target=func, args=(xxx,))
    - 创建线程: t = Thread(target=func, args=(xxx,))
    - 使用进程: p.start()
    - 使用线程: t.start()
'''
from threading import Thread
from time import sleep
from random import random

def download(n):
    images = ['a1.jpg', 'b2.jpg', 'c3.jpg']
    for img in images:
        print('正在下载{}...'.format(img))
        sleep(n)
        print('{}下载成功'.format(img))

def upload():
    files = ['user.txt', 'password.txt', 'money.txt']
    for file in files:
        print('正在上传{}...'.format(file))
        sleep(random() * 2)
        print('{}上传成功!'.format(file))

# 创建两个线程, 让它们分别执行不同的任务.
t1 = Thread(target=download, args=(1, ), name='线程1')
t2 = Thread(target=upload, name='线程2')
t1.start()
t2.start()

'''线程的状态: 
 1.新建状态 t = Thread()
 2.就绪状态 t.start()
 3.运行状态 t.run()
 4.阻塞状态 sleep()
 5.结束状态 t.terminate()
 - 新建状态和结束状态在线程中都只会进行一次(正如人的出生和死亡).
 - 就绪状态/运行状态/阻塞状态 会形成一个闭环: 
    - 就绪状态 -> 运行状态, 线程一切准备就绪, 使用 run() 方法即可使其运行.
    - 运行状态 -> 阻塞状态, 线程在进行 IO 或其他操作时, CPU会交给其他线程, 进入阻塞状态.
    - 阻塞状态 -> 就绪状态, 线程的 IO 操作结束可以继续执行时, 就进入了就绪状态.
'''