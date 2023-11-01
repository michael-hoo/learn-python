'''本节大纲:
1. 有了多线程, 为什么还需要多进程?
   不赘述, 前面已经说了.
2. 多进程 multiprocessing 知识梳理
   大部分内容之前在 29_进程 中已经学过了, 但这里有些新东西可以作为补充.
    1. 进程锁
        from multiprocessing import Lock
        lock = Lock()
        with lock:
            # 需要加锁的代码
            pass
    2. 进程池: 具体可以参考 ThreadPoolExecutor 部分
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            # 方法一
            results = executor.map(craw, urls)
            # 方法二
            future = executor.submit(craw, url)
            result = future.result()
    3. ThreadPoolExecutor 和 multiprocessing.Pool 之间的异同
        相同点:
            - 都可以利用多核, 实现并行执行任务(多进程).
            - 都可以使用上下文管理器(with)来自动管理进程池的创建和销毁.
        不同点:
            - multiprocessing.Pool 更早, 而 ProcessPoolExecutor 在 Python3.2 之后可用
            - ProcessPoolExecutor 需要 executor.submit() 或 executor.map() 来提交任务
            - 而 Pool 需要用 pool.apply() 或 pool.map() 来提交任务(感觉更简洁啊).
            - 可扩展性: multiprocessing.Pool 提供了更多的高级功能, 如进程间通信, 进程间锁等,
              适用于更复杂的并发场景, ProcessPoolExecutor 相对更加简洁实用.
        总的来说, 都差不多, 官方说 Concurrent.futures 是更高级别的接口(更容易调用).
3. 代码实战: 单线程、多线程、多进程对比 CPU 密集计算速度
'''
import math, time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

Primes = [112272535095293] * 30

# 创建一个 CPU 密集型函数: 计算一个数字是不是素数
def is_prime(n):
    """什么是素数? 
     - 除了1以外, 一个数字如果只能被1和其自身整除, 则称其为素数.
     - 这里代码的细节不需要懂, 只需知道它是计算密集型函数即可.
     - 因为这里只是想对比单线程/多线程/多进程之间的速度差距
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

# 用单线程实现这项任务
def single_thread():
    print('单线程运算开始运行...')
    for num in Primes:
        is_prime(num)

# 用多线程来实现这项任务
def multi_thread():
    print('多线程运算开始运行...')
    with ThreadPoolExecutor(max_workers=4) as executor:
        resutls = executor.map(is_prime, Primes)
        return resutls

# 用多进程来实现这项任务
def multi_process():
    print('多进程运算开始运行...')
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(is_prime, Primes)
        return results

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print(f'单线程运算结束, 此次运行耗时{end-start}秒!')

    start = time.time()
    multi_thread()
    end = time.time()
    print(f'多线程运算结束, 此次运行耗时{end-start}秒!')

    start = time.time()
    multi_process()
    end = time.time()
    print(f'多线程运算结束, 此次运行耗时{end-start}秒!')

'''计算结果:
 - 单线程耗时: 18.39秒
 - 多线程耗时: 19.01秒
 - 多进程耗时: 11.21秒
所以, 对于CPU密集型任务: 多进程 > 单线程 > 多线程
'''