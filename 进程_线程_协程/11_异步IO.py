'''
协程可以使我们在单线程之中实现并发. 为什么能这样呢? 
 - 传统的单线程爬虫在遇到 IO 时会等待, 等 IO 返回结果后再继续进行下一步操作.
 - 而协程运用了"IO多路复用原理"(即 IO 时 CPU 可以去干其他事), 一旦程序进入 IO 时, 
   协程就会跳转到另一个任务上执行.
    - 放到爬虫上就是协程成功爬到第一个链接数据, 遇到 IO 就去爬取下一个链接.

协程的核心原理: 
 - 使用了一个超级循环(while True)
 - 配合"IO多路复用原理".

asyncio - 异步IO
    import asyncio
    # 获取事件循环
    loop = asyncio.get_event_loop()
    # 定义协程
    async def myfunc(url):
        await get_url(url)
    # 创建Task列表
    tasks = [loop.create_task(myfunc(url)) for url in urls]
    # 执行爬虫事件列表
    loop.run_until_complete(asyncio.wait(tasks))
 - 注意: 在异步IO编程中依赖的库, 必须支持异步IO的特性.
    - 爬虫中常用的 requests 库就不支持异步IO, 需要用 aiohttp 来代替.

异步IO中还可以通过信号量 asyncio.Semaphore 来控制协程同时执行的任务数, 可以简单理解为协程默认
是个不限数量的线程池, 太多线程抢夺系统资源反而会降低运行速度, 信号量设为10就是线程池中放10个线程.
'''
# 无法导入 aiohttp? 可能是 Python 版本的问题, 之前用 Python3.12 不行, 
# 换成 Python3.11.5 就可以下载了.
import asyncio, aiohttp, blog_spider, time

'''async 是 Python 中用来定义异步函数或协程的关键字. 这里是定义了一个异步函数!
 - 异步函数允许在函数内部使用 await 关键字, 表明该行代码会以非阻塞的异步操作执行.
    - 这可以有效提升程序的并发性(也就提升了性能).
'''
async def async_craw(url):
    """这是一个运用了异步IO技术的爬虫方法!
    async with...as: 这里先定义了一个异步上下文管理器. 它和异步函数之前的区别/联系是: 
        - 异步函数主要用于执行异步任务, 而异步上下文管理器主要用于异步资源管理.
    aiohttp.ClientSession(): 它创建了一个 aiohttp 客户端会话对象.
        - 该对象用于执行异步的 HTTP 请求(Get/Post),  管理连接池, 设置请求头, 等等.
            - session.get(url) 和 requests.get(url) 很相似.
    resp = session.get(url): 它返回了一个 ClientResponse 对象.
        - 通过这个对象, 可以获取响应的状态码/响应头/响应正文等信息.
    resp 的常用属性及方法:
        - HTTP状态码: 表示请求的成功, 重定向或错误 -> resp.status
        - HTTP头部信息: 通常是一个字典 -> resp.headers
            - 可使用 resp.headers['header_name'] 来获取特定头部的值.
        - 响应的文本内容: 比如 HTML/XML 等 -> await resp.text()
        - 响应的二进制内容: 比如图片等信息 -> await resp.read()
        - 响应的 JSON 文件 -> await resp.json()
        - 检查响应的状态码: 若状态表表示请求失败, 会抛出异常 -> resp.raise_for_status()
        - 请求信息: 如请求方法, URL 等 -> resp.request_info
        - 响应的URL: 可能会与请求URL不同 -> resp.url
        - 请求方法 -> resp.method
    """
    # aiohttp.ClientSession() 中的内容我也不知道啥意思, 报错了, 查了一下, 填进去就没问题了
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            # await 的时候, 超级循环不会等待, 而是继续下一个链接的爬取
            result = await resp.text()
            print(f'craw url: {url}, {len(result)}')

'''创建超级循环
 - 通过这行代码为当前线程创建一个异步IO的事件循环(又称超级循环).
 - 事件循环是异步编程中的核心, 它用于调度和管理异步任务的执行(确保了任务以非阻塞的方式运行).
 - 每个线程都只有一个事件循环, 这种方式确保了事件循环在多线程下的线程安全性.
'''
loop = asyncio.get_event_loop()
'''
loop.create_task()和进程池的 p.apply_async(func, args=(x, ))很相似.
    - 但这里更方便的是, 可以将函数连同参数一起传进去 async_craw(url).
这里用列表推导式, 不断将 loop.create_task() 返回值存到列表中.
'''
tasks = [loop.create_task(async_craw(url)) for url in blog_spider.urls]

# 增加计时
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f'此次运行用时{end-start}秒')
# 耗时0.48秒, 对比一下单线程爬虫的5.51秒和多线程爬虫的1.53秒确实差距很大!