'''实现"生产者-消费者"模式的多线程爬虫
1. 先了解一下多组件的Pipeline技术架构
 - 在编程中, 复杂的事情一般不会一下子做完, 而是会分成很多步骤一步步完成. 比如:
    输入数据 --CPU1--> 中间数据 --CPU2--> 中间数据 --CPU3--> ... --CPUX--> 输出数据
 - 这样的架构就被称为Pipeline架构(名字很形象, "管道").
 - 而生成者消费者模式就是一个典型的(或者说基本的)Pipeline技术架构. 比如: 
    输入数据 --CPU(生产者)--> 中间数据 --CPU(消费者)--> 输出数据
2. "生产者-消费者"爬虫的架构
    输入数据 --CPU(生产者)--> 中间数据 --CPU(消费者)--> 输出数据
    - 输入数据: 待爬取的URL列表
    - 生产者: 线程组1 -> 进行网页下载
    - 中间数据: 下载好的网页队列(除了队列还有其他通信方式)
    - 消费者: 线程组2 -> 对网页进行解析存储
    - 输出数据: MySQL, Excel...
3. 多线程数据通信的方法 - queue.Queue
   queue.Queue是可以用于多线程之间的、线程安全的数据通信.
    1. 导入类库: from queue import Queue
    2. 创建队列: q = Queue()
    3. 添加元素: q.put(item)
    4. 获取元素: q.get()
        - 注意: put和get都是阻塞的, 若队列已满, put会卡住; 若队列已空, get会卡住.
    5. 查询状态:
        - 查看元素的多少: q.qsize()
        - 判断队列是否为空: q.empty()
        - 判断队列是否已满: q.full()
4. 代码编写实现生成者消费者爬虫
    程序还是有 bug, 爬到的文章列表都是第一页的一直在重复...
'''
# 先用生产者-消费者模式编写一个爬虫模块
import blog_spider, time, random, threading
from queue import Queue

# 执行生产者
def do_craw(url_queue: Queue, html_queue: Queue): # Queue 指示参数类型, 增强代码可读性
    """代码逻辑分析:
    从队列 url_queue 中获取的 url, 交给 craw() 方法来处理;
    并将处理的结果, 放到队列 html_queue 中.
    """
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f'craw {url}',
              'url_queue.size=', url_queue.qsize())
        time.sleep(1) # 随机睡眠1到2秒
        if url_queue.qsize() == 0:
            break

# 执行消费者
def do_parse(html_queue: Queue, file):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html) # 这里的 results 是 [(), (), (), ...]
        for result in results:
            file.write(str(result) + '\n')
        print(threading.current_thread().name, 'results size', len(results), 
              'html_queue.size=', html_queue.qsize())
        time.sleep(2) # 随机睡眠1到2秒 
        if html_queue.qsize() == 0:
            break


if __name__ == '__main__':
    # 创建两个队列, 给生产者和消费者用
    url_queue = Queue()
    html_queue = Queue()

    # 利用循环将 blog_spider 模块中的 urls 不断 put 进队列中
    for url in blog_spider.urls:
        # print('if __name == __main__:', url) # 这里的 url 没问题
        url_queue.put(url)

    # 创建3个生产者线程, 来执行 do_craw 方法, 并把两个队列作为参数传入
    for i in range(10):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), 
                             name=f'craw{i}')
        t.start()
    
    file = open('进程_线程_协程/blog_title.txt', 'w')
    for i in range(5):
        t = threading.Thread(target=do_parse, args=(html_queue, file), 
                                name=f'parse{i}')
        t.start()               
