'''
这一节我们想要通过单线程和多线程的方式分别从博客园中爬取数据, 以此来对比
单线程爬虫和多线程爬虫在效率上的差距!
'''
import time, requests
from threading import Thread

# 待爬取的URL列表
urls = [f'https://www.cnblogs.com/#p{page}' for page in range(1, 50+1)]
'''f-string
上面链接字符串前面的'f', 它用于创建一个格式化字符串(f-string), 这是Python3.6
及以上版本的功能, 可以往字符串中插入变量! 有点像format()的升级版本!
'''

# 先创建一个爬虫方法
def craw(url):
    # requests.get(url)相当于向指定url发送了一个get请求, 并获取从服务器返回的数据.
    response = requests.get(url)
    # 从返回对象中提取网页用其text属性, 如果是二进制内容用content.
    print(url, len(response.text)) # 这里为了演示, 只需知晓response.text的长度即可.

# 使用单线程调用爬虫方法
def single_thread():
    print('单线程爬虫开始运行...')
    # 通过for循环不断调用爬虫方法, 这是典型的单线程模式.
    for url in urls: # 从列表中遍历链接, 然后将链接交给爬虫去处理.
        craw(url)

# 创建多线程, 并用多线程调用爬虫方法
def multi_thread():
    """_summary_: 利用for循环为每一个URL生成一个线程, 并追加到threads列表中.
    """
    print('多线程爬虫开始运行...')
    # 创建一个空列表, 用于存放线程对象
    threads = []
    for url in urls:
        # 将生成后的线程追加到列表中
        threads.append(
            # 每个线程均以craw()方法为目标, 并把URL作为参数传入
            Thread(target=craw, args=(url, ))
        )
    # 利用for循环逐一启动所有线程
    for thread in threads: # 这才叫编程啊, 太优雅了!
        thread.start()
    # 利用for循环逐一同步所有线程
    for thread in threads:
        thread.join()
    
if __name__ == '__main__':
    start = time.time()
    single_thread() # 5.51s
    end = time.time()
    print('单线程爬虫运行结束, 此次耗时{}秒!'.format(end - start))
    # 单线程爬虫运行结束, 此次耗时7.67094612121582秒!

    start = time.time()
    multi_thread() # 1.53s
    end = time.time()
    print('多线程爬虫运行结束, 此次耗时{}秒!'.format(end - start))
    # 多线程爬虫运行结束, 此次耗时3.0046448707580566秒!
    # 由此可以看出, 单线程和多线程爬虫在效率上的差别!
    # 并且, 这个差距会随着你的CPU性能而进一步加大!