'''
本节主要回答两个问题: 
1. 为什么需要并发编程? 
2. 怎样使用并发编程?
'''

'''
1. 为什么要引入并发编程?
 先看看两个应用并发编程的实际场景: 
    - 场景一: 一个网络爬虫, 如果顺序爬取需要花费1小时, 采用并发下载会将时间减少到20分钟.
    - 场景二: 一个APP在后台请求了大量的外部资源, 优化之前每次打开需要3s, 采用异步并发将时间减少到200ms.
 由此, 我们可知:
    - 使用并发, 可以大幅度提升程序的运行速度.
    - 并且, 学习并掌握并发编程, 是高级别/高收入程序员的必备能力!

2. 具体有哪些提升程序速度的方法?
    - 多线程并发 -> threading
    - 多CPU并行 -> multiprocessing
    - 多机器并行(属于大数据) -> hadoop/hive/spark

3. Python对并发编程有哪些支持?
 主要有以下三个模块:
    - 多进程: multiprocessing模块, 利用多核CPU的能力, 真正并行执行任务.
    - 多线程: threading模块.
    - 异步IO: asyncio模块, 在单线程利用CPU和IO同时执行的原理, 实现函数异步执行.
 Python还提供了其他辅助方法:
    - 使用 Lock 对资源加锁, 防止冲突访问. 
    - 使用 Queue 实现不同线程/不同进程之间的数据通信, 实现生产者-消费者模式
        - 对于爬虫来说, 生产者就是边爬取, 消费者就是边解析.
    - 使用线程池Pool/进程池Pool, 简化线程/进程的任务提交, 等待结束, 获取结果.
    - 使用 subprocessing 启动外部程序的进程, 并进行输入输出交互. 
'''