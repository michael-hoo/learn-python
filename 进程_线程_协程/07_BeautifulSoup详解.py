'''
BeautifulSoup 是 bs4 模块中的一个类，用于解析 HTML 或 XML 文档, 使人很方便地
浏览、搜索和修改文档的内容。

可以使用 BeautifulSoup 来将 HTML 或 XML 文档解析为 Python对象 , 通过这个对象, 
我可以访问文档的各个部分, 比如标签, 属性和文本内容.

下面在代码中进行详细介绍!        
'''
from bs4 import BeautifulSoup
import requests

# 既然 BeautifulSoup 对象是用来解析 HTML 文档的, 那么, 我需要先获得一份 HTML 文档
url = 'https://www.cnblogs.com/sitehome/p/2'
response = requests.get(url)
# response.text 就是 BeautifulSoup 对象所需的 HTML 文档!
# 创建一个 BeautifulSoup 对象, 通过此对象来从 HTML 文档中提取我想要的内容
soup = BeautifulSoup(response.text, 'lxml')
'''
BeautifulSoup 解析器:
 - Python 内置解析器('html.parser'): 速度较慢, 但足以用于大多数情况.
 - lxml 解析器('lxml'): 它是一个高性能的 HTML/XML 解析器, 速度快, 具有很好的容错性.
   它是 BeautifulSoup 推荐的解析器, 但需要安装 lxml 库才可使用 -> pip3 install lxml
 - html5lib 解析器('html5lib'): 它是基于 HTML5 规范的解析器, 具有很好的容错性, 但速度较慢, 
   也需要手动安装 -> pip3 install html5lib
'''
# 既然已经成功获得一个 BeautifulSoup 对象了, 我该怎样访问文档的标签/属性/文本内容呢?
'''
1. 访问标签: find() 和 find_all()
 - find() 方法可以查找第一个匹配到标签;
 - find_all() 方法可以查找所有匹配到的标签.
'''
# 查找第一个<a>标签
tag = soup.find('a')
print(tag)
# 查找所有<a>标签
tags = soup.find_all('a')
for tag in tags: # 通过这种方式可以获得所有<a>标签中的内容
    print(tag.text)

# 搜索具有 class="example" 的<div>标签
divs = soup.find_all('div', class_='example')
# 注意: 这里的 'class_' 只是为了和 Python 中的关键字 class 发生冲突, 
#BeautifulSoup 是这样规定的, 就这样写就可以~


'''
2. 访问属性: 一旦有了标签对象, 就可以通过 tag[属性名] 的方式来获取标签的属性值.
'''
# 获取标签<a>中的 href 属性
href = tag['href']
print(href)

'''
3. 访问文本内容: 同样, 有了标签对象, 也可以通过 tag.text 的方式来获取标签的文本内容.
'''
# 获取标签<a>中的文本内容
text = tag.text
print(text)
# 或者
text = soup.find('a').text

'''
4. 访问标签名称: 和访问文本内容很相似, tag.name
'''
# 获取标签<a>的名称
name = tag.name
print(name)

'''
5. 访问父标签和子标签
'''
# 获取父标签
parent_tag = tag.parent
print(parent_tag)
# 获取所有子标签
children_tag = tag.contents # 为什么这里是 contents 而不是 children?
# children_tag = tag.children
# 获取下一个兄弟标签
next_sibling = tag.next_sibling
print(next_sibling)
# 获取上一个兄弟标签
previous_sibling = tag.previous_sibling
print(previous_sibling)

'''
6. 修改文档
'''
link = soup.find('a')
link['href'] = 'https://www.baidu.com'