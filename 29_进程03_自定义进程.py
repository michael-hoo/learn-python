# 1.3 自定义进程 -> 继承 Process 类
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    # 自定义进程必须要重写 run() 方法: 进程要做的事情都要放在 run 里面
    def run(self):
        n = 1
        while True:
            print('自定义进程名称: {}, {}'.format(self.name, n))
            sleep(1)
            n += 1
            if n == 10:
                break

if __name__ == '__main__':
    print('主进程开始运行...')
    p1 = MyProcess(name='小明')
    p2 = MyProcess(name='小红')
    # start 和 run 之间的关系与 __new__ 和 __init__ 的关系类似.
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程执行结束!')