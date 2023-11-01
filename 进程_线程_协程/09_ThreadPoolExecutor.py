'''本节大纲:
1. 线程池的原理
 - 线程的生命周期:
   新建 -> 就绪 -> 运行 -> 阻塞 (-> 就绪) -> 终止
    - 新建: th = Thread(target=func, args=(xx, )), 只会执行一次
    - 就绪: th.start(), 就绪状态后, 只要获得 CPU 资源, 即可运行.
    - 运行: th.run(), 此方法不用调用, 会自动执行.
    - 阻塞: 当遇到 sleep/IO 时, 就会进入阻塞状态, 阻塞结束会重新进入就绪状态.
    - 终止: 所有任务完成, 线程终止, th.join() 结束. (也只会执行一次)
 - 还需要知晓的是, 新建线程系统需要分配资源, 终止线程系统需要回收资源, 这两者都会造成系统的开销, 
   如果可以重用线程, 就可以减去新建/终止线程造成的开销.
 - 为了实现这个目的(线程的重用), 便引入了线程池技术!

2. 使用线程池的好处
 - 提升性能: 因为减去了新建/终止线程造成的开销, 也就提升了系统性能.
 - 适用场景: 适合处理突发性大量请求或需要大量线程完成任务, 且任务处理所需时间较短的情况.
 - 代码优势: 使用线程池语法上比自己手动新建线程更加简洁!

3. ThreadPoolExecutor 的使用语法
    from concurrent.futures import ThreadPoolExecutor, as_completed
    # 第一种方法
    with ThreadPoolExecutor() as pool:
        results = pool.map(craw, urls) # 第一个参数是函数名, 第二个参数是个列表
        # 这里的 result 和 url (urls是个列表) 是一一对应的
        for result in results:
            print(result)
    
    # 第二种方法
    with ThreadPoolExecutor() as pool:
        futures = [pool.submit(craw, url) for url in urls]
        # 第一种遍历方式
        for future in futures:
            print(future.result())
        # 第二种遍历方式
        for future in as_completed(futures):
            print(future.result())
        # 第二种方式更好, 因为第一种方式按顺序返回, 第二种方式谁先完成先返回谁.

4. 使用线程池改造爬虫程序
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import blog_spider

# craw
'''代码逻辑分析:
ThreadPoolExecutor()
 - 这里 ThreadPoolExecutor 是一个类, 这里通过该类创建了一个相应类型的对象.
 - ThreadPoolExecutor() 中可以传入一个参数 max_workers=n, 可以在线程池中创建 n 个线程.
    - 如果不写此参数, 默认创建和当前计算机内核核心数量相同的线程数.
 - 建议使用 with...as 语句来创建线程池, 这样代码风格保持了统一性, 且不用手动关闭线程池!

executor.submit()
 - executor 是一个 ThreadPoolExecutor 类型的线程池对象.
 - 通过 submit() 方法可以往线程池中添加任务, 其使用方法和手动创建线程很相似:
    - 第一个参数是函数名, 表示线程池将要执行什么动作;
    - 第二个参数是向待执行函数中传递的参数, 这里一次传递单个参数, 而不是传递一个元组.
 - 不过这里 executor.submit() 比 th = Thread(target=func, args=(x, ) 刚方便的是:
    - executor.submit() 返回的是一个 Future 对象, 里面包含了"未来"可以获得的结果.
        - 可通过 future.result() 这种方式获取执行结果(这个方法会阻塞, 直到取回结果).
    - 而 Thread() 返回的是一个线程对象, 执行结果还需要一个队列去储存及传递.
'''
with ThreadPoolExecutor() as executor:
    # futures = []
    # for url in blog_spider.urls:
    #     future = executor.submit(blog_spider.craw, url)
    #     futures.append(future)
    # 上面这段代码用列表推导式来写会更加简洁:
    futures = [executor.submit(blog_spider.craw, url) for url in blog_spider.urls]
    # 这里的 futures 是什么? 首先它是一个列表, 列表中装了一个个 Future 对象
    # 每个 Future 对象中包含了 craw(url) 方法获得的一页博客园网页文本.
    
    # for future in futures:
    #     print(len(future.result())) 
    '''这里为何不直接使用 for 循环, 而要加一个 as_completed()?
     - 因为 future.result() 会阻塞, 直到获取结果.
     - 而 as_completed() 会优先返回处理完毕的结果, 可以更大程度利用并发性能.
    '''
    htmls = []
    for future in as_completed(futures):
        html = future.result()
        htmls.append(html)
        print(len(html))

print('craw over!')

# parse
with ThreadPoolExecutor() as executor:
    # 如果嫌上面的方法太麻烦? 可以使用 map() 批量传参
    # 这里 map() 返回的就不是 Future 对象了, 而就是一个 map, 它可迭代, 可使用 list 强转.
    results = executor.map(blog_spider.parse, htmls)
    # 这里的 results 是什么? map() 依次将每个 html 传给 parse(), 返回了一个包含一页链接+标题
    # 的元组的列表, 即 [(url1, title1), (url2, title2), ...], results 中有50页这样的列表
    for result in results:
        # 这里的每个 result 都是一个列表, 可以对其再遍历一次.
        for article in result: # 这里的 article 是一个元组, 进行分开打印
            print(article[0], article[1])


