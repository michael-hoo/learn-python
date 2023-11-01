from threading import Thread
from bs4 import BeautifulSoup
import requests, time

urls = [f'https://movie.douban.com/top250?start={id}&filter=' for id in range(0, 225+1, 25)]


def craw(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 请求成功
        print('请求成功!')
    else:
        print(f"请求失败，状态码: {response.status_code}")
    return response.text # 返回的就是网页内容(共10页)

def parse(html):
    # 对HTML中的"class=post-item-title"
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='title')
    return [(link['href'], link.get_text()) for link in links]

def multi_thread():
    """_summary_: 利用for循环为每一个URL生成一个线程, 并追加到threads列表中.
    """
    start = time.time()
    print('多线程爬虫开始运行...')
    # 创建一个空列表, 用于存放线程对象
    threads1 = [] # 第一组线程共10个, 用于下载豆瓣每一页都网页
    for url in urls:
        # 将生成后的线程追加到列表中
        threads1.append(
            # 每个线程均以 blog_spider 模块中的 craw() 方法为目标, 并把 URL 作为参数传入
            Thread(target=craw, args=(url, ))
        )
    # 利用for循环逐一启动所有线程
    for thread in threads1: # 这才叫编程啊, 太优雅了!
        thread.start()

    threads2 = [] # 第二组线程用于解析网页

    # 利用for循环逐一同步所有线程
    for thread in threads1:
        thread.join()
    end = time.time()
    print('多线程爬虫运行结束, 此次耗时{}秒!'.format(end - start))

if __name__ == '__main__':
    for url in urls:


    
