import requests
from bs4 import BeautifulSoup

'''爬取的网页内容重复问题
最后经过B站弹幕提醒, 发现竟然是链接有问题...改成这样就莫名其妙的好了!
之前用的是 https://www.cnblogs.com/#p{page}, 一直不行
'''
urls = [f'https://www.cnblogs.com/sitehome/p/{page}' for page in range(1, 50+1)]

# 对 craw() 函数进行生产者-消费者模式的改造!
# 生产者craw(): 仅用于发送请求/获得响应, 并将网页内容返回到另一个函数parse()中进行处理.
def craw(url):
    # 把请求伪装成真实的浏览器
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # 程序这里出现问题: 虽然url是不同的, 但获得的网页是相同的, 应该是触发了反爬虫机制.
    r = requests.post(url, headers=headers) # get 换成 post 还是不行...
    # print('def craw():', url) # 这里的url也没问题, 但为何下面打印出的数值每次都一样呢?
    # print(len(r.text)) # 这里打印出的数值每次都是70410, 说明每次传的都是同一个url!
    return r.text # 直接返回网页内容

# 消费者parse(): 从生产者那里获取网页内容并进行处理, 并将处理结果返回给用户.
def parse(html):
    """代码逻辑分析: 创建 bs 对象以及查找指定属性的<a>标签这里就不赘述了.
    着重讲讲 link.get_text() 的作用以及它和 link.text 的区别:
     - get_text() 是获得标签对象 link (实际是 <a>)的文本内容的方法.
        - 只要是标签对象都有此方法!
        - 所有 soup.find() 或 soup.find_all() 返回的都是标签对象!
     - link.get_text() 和 link.text 从作用上来说是差不多的, 都是获得标签内的文本内容
        - 但 get_text() 刚好的地方是, 它可以传递参数来控制文本提取的方式!
        - 比如, 我可以使用 link.get_text(strip=True) 来删除文本前后的空白字符!
        - 所以, 能用 get_text() 就别用 text...

    Args:
        html (string): 这个参数传入 craw() 方法中返回的网页文本内容(response.text)
    Returns:
        list: 实际形式是这样的 [(), (), (), ...], 通过列表推导式将 links 中的每个 link 的
              链接和文本内容存放到一个元组中.
    """
    # 创建一个 BeautifulSoup 对象来解析网页内容
    soup = BeautifulSoup(html, 'lxml')
    # 查找所有 class 属性为 'post-item-title' 的 <a> 标签
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text(strip=True)) for link in links]
    # 这里返回的是博客园一页的链接和标题组成的列表 [(url, name), (url, name), ...]

if __name__ == '__main__':
    url = urls[3] # 这里我修改数字, 结果都一样, 为什么? 估计是触发了反爬虫机制...
    i = 0
    for result in parse(craw(url)): 
        i += 1
        print(f'{i}: {result}')
    print(url)