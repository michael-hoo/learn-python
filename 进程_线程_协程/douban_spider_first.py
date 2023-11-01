import requests
from bs4 import BeautifulSoup

urls = [f'https://movie.douban.com/top250?start={id}&filter=' for id in range(0, 225+1, 25)]

# 对 craw() 函数进行生产者-消费者模式的改造!
def craw(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
    return response.text # 返回的就是网页内容(共10页)

def parse(html):
    # 对HTML中的"class=post-item-title"
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all('span', {'class': 'title'})
    return [name.get_text() for name in names]

'''对上面的代码要仔细梳理一遍!'''


if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        print(result)


