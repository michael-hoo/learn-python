print('>>1>>' * 10)
# 1. 文件的读写
'''
    open(file, mode='r')
    - file: 需要读写的文件的路径名.
    - mode: 分为以下几种:
        - r/w: 读和写 -> 纯文本文件
            - a: 写. 和 w 不同的是: w 的写是对原文件进行覆盖(如果该文件不存在则新建文件), 而 a 是在原文件末尾追加.
        - rb/wb: 二进制读和二进制写 -> 纯文本/图片/音乐/视频...
            - 尽量使用 rb/wb, 因为 r/w 能做的 rb/wb 也都能做.
'''
## 1.1 读文本
stream = open('./test.txt') # mode 是默认参数, 不写就是 'r'
container = stream.read()
print(container)
'''
    分析代码逻辑:
    - open() 会返回一个 IO 流对象, 你可以将它理解为一个管道, 具体是读是写由 mode 参数控制.
    - 这里的 stream 就是那个管道, 没有设置 mode, 默认为 r(读), 即一个指向 test.txt 的读取管道已经建好了.
    - 读取管道 stream 有相应的读文件方法:
        - read(): 一次读取文件的全部内容.
        - readline(): 一次读取一行.
        - readlines(): 按行读取文件的全部内容, 并将每行内容保存在一个列表中返回.
        - readalbe(): 判断文件是否可读.
    - 这些方法返回的都是字符串, 所以我需要使用一个容器(container)来接收它们.
'''
print(stream.readable()) # True, 当前 Stream 指向的文件是可读的.
print(stream.readline()) # None
'''
    为什么这里使用 readline() 却没有读出结果呢? 
    因为上面已经调用过 stream.read() 了! 已经读完了. 可以这么理解:
    调用 open() 之后会返回一个流(管道), 不管有没有执行具体的读方法(read/readline/readlines), 文件内容均暂存到管道中了.
    而调用 read() 方法可以想象成一次性把管道中的内容全部读进来, 后续再调用其他读方法自然返回值为空.
    可以通过下面的代码验证一下, 先用 readline(), 再用 read(), 看看结果如何.
'''
stream = open('./test.txt')
result1 = stream.readline()
print('result1:\n', result1)
result2 = stream.read()
print('result2:\n', result2)
'''
可以看到, 输出结果为: 
    result1:
    Hello, world!

    result2:
    Hello, Nathan!
说明上面的分析是正确的.
需要注意的是: 上面 Hello, world! 末尾会空一行是因为 readline() 每读取一行, 会在后面加一个换行符. 
用一下代码可以验证...
果然如此, 不过我们可以将 print() 后面的 \n 去掉来优化代码.
'''
stream = open('./test.txt')
while True:
    result = stream.readline()
    print(result, end='')
    if not result: # 当 result 非空时, not result 就是 False; 当 result 为空时, not result 就是 True.
        print()
        break

stream = open('./test.txt')
lines = stream.readlines()
print(lines) # ['Hello, world!\n', 'Hello, Nathan!\n', 'Hi, baby, nice to meet you~']

## 1.2 读图像(二进制文件)
# stream = open('./test.jpeg', 'rb')
# container = stream.read()
# print(container)

## 1.3 写文件 - w 覆盖
stream = open('./test.txt', 'w')
s = '''
你好!
    欢迎来到澳门皇家赌场, 现在送一个金币给你!
                            赌神: 高进
'''
stream.write(s) # 执行完毕, 就把原文件的内容给覆盖了.
stream.write('龙五说:\n\t赶快来玩, 否则我的子弹不长眼!') 
# 只要管道不关, 可以重复文件里写内容. 
stream.writelines(['hello', 'world']) # 和 write() 的区别在于可以写入可迭代对象.
stream.close() # 管道用完后, 要记得关闭, 不然会浪费空间!

## 1.4 写文件 - a 追加
stream = open('./test.txt', 'a')
stream.write('周杰伦')


print('>>2>>' * 10)
# 2. 文件的复制: 文件的复制本质就是先读后写.
# 练习: 将当前路径下的 test.jpeg 复制到桌面上, 要求: 不可使用相对路径.
import os

dir_path = os.getcwd() # /Users/hunan/Documents/Python 学习笔记, 获取当前目录的绝对路径名.
# file_path = dir_path + '/test.jpeg'
'''
    注意: 一般不推荐对路径使用字符串拼接, 因为在 Linux/macOS 中, 目录格式是 /A/B/C, 而在 Windows 中是 \A\B\C
    所以, 对于文件路径的拼接, 一般建议使用 os.path.join(dir, file) 方法.
'''
file_path = os.path.join(dir_path, 'test.jpeg')
print(file_path) # /Users/hunan/Documents/Python 学习笔记/test.jpeg

# 文件复制操作的本质是: 先读再写.
# 第一步: 先读.
# with open(file_path, 'rb') as f: # 这样就不用 f.close() 了
    # container = f.read()
    # 第二步: 再写.
    # with open('/Users/hunan/Desktop/test.jpeg', 'wb') as f: # 这里要是能通过 os 获取桌面的绝对路径就好了.
        # f.write(container)
        # print('文件复制完成!')

'''
模块: Python 中将一个 Python 文件称为"模块", 比如: xxx.py
我们常用的模块有: 
    - 内置模块: builtins.py, 内置模块无需导入即可使用.
    - os 模块: os.py
    - random 模块: random.py
所以, 我们平时 import os, 实际上是导入一个模块; 而 from random import randint, 是从模块中导入方法.
'''

## 2.1 os.path
'''
os.path
    - os.path.join(): 对路径进行连接.
    - os.path.isabs(): 判断是否是绝对路径.
    - os.path.dirname(__file__): 获取当前文件所在的目录的绝对路径.
    - os.getcwd(): 获取当前程序运行所在的目录的绝对路径.
        - 一般情况下二者是一样的, 但有些特殊情况, os.path.getcwd() 获取的不是当前文件所在的绝对路径.
    - os.path.abspath(): 通过相对路径, 得到绝对路径.
    - os.path.abspath(__file__): 获取当前文件的绝对路径
        - 所以, __file__ 就代表着当前文件本身.
    - os.path.split(p): 将路径和文件名分开, 返回一个元组.
    - os.path.splitext(file_path): 将路径和文件后缀分开, 返回一个元组.
        - splitext: 注意不是text, 是 split ext(extension)
    - os.path.size(filename): 返回文件的大小
    - os.path.expanduser(): 将 Linux 下的 ~ 转化为绝对路径.
'''
## join - 文件路径的拼接
result = os.path.join(os.getcwd(), 'file1', 'file2', 'aa.jpg')
print(result) # /Users/hunan/Documents/Python 学习笔记/file1/file2/aa.jpg
'''
os.path.join() 对路径的拼接不在乎文件本身是否存在, 它就是纯粹的字符串拼接.
但是它可以传入多个参数, 每多一个就相当于多了个层级, 并且得到的路径在 Linux/macOS/Windows 下均可用.
'''

## 绝对路径和相对路径
print(os.path.isabs(file_path)) # True
print(os.path.isabs('./test.txt')) # False
# ./ - 表示当前路径
# ../ - 表示上层目录
# 根据相对路径获取绝对路径
print(os.path.abspath('./test.txt')) # /Users/hunan/Documents/Python 学习笔记/test.txt
# 获取当前文件的绝对路径
file_path = os.path.abspath(__file__)
print(file_path) 

# 将路径和文件名分开, 返回一个元组.
result = os.path.split(file_path) 
print(result) # ('/Users/hunan/Documents/Python 学习笔记', '20_文件操作.py')
# 拿到文件名
print(os.path.split(file_path)[1])

# 将路径和文件扩展名分开, 返回一个元组
result = os.path.splitext(file_path)
print(result) # ('/Users/hunan/Documents/Python 学习笔记/20_文件操作', '.py')
# 拿到文件后缀
print(os.path.splitext(file_path)[1]) # .py

print(os.path.getsize(file_path)) # 6810, 单位是字节.

user_path = os.path.expanduser('~')
'''
在 Linux 系统中, ~ 符号代表我的用户目录的路径, 但 Python 不认识这个符号, 在 Python 中使用 '~/xxx' 是无法被识别的.
这个时候可以用 os.path.expanduser('~/xxx') 将其展开成完整的 /Users/hunan/xxx.
'''
print(user_path) # /Users/hunan
# 所以, 获得桌面的绝对路径也就简单了.
print(os.path.expanduser('~/Desktop')) # /Users/hunan/Desktop


## 2.2 os
'''
    os下常用的函数:
    - os.getcwd(): 上面已经介绍了.
    - os.listdir(dirpath): 返回 dirpath 下所有文件和目录的名字, 组成一个 list
    - os.rmdir(dir_name): 删除非空目录.
    - os.remove(file_name): 删除文件.
    - os.chdir(): 切换目录.
'''
# 得到当前目录下所有的文件和目录的名字
result = os.listdir(os.getcwd())
print(result)

# 创建文件夹
dir_path = os.path.join(os.path.expanduser('~/Desktop'), 'test')
if os.path.exists(dir_path): # 判断文件或目录是否存在, 已存在就跳过, 不存在就创建一个目录
    pass
else:
    os.mkdir(dir_path)

# 删除目录
os.rmdir(dir_path) # 这个方法只能删除空目录
# 删除非空目录如何操作呢? 可以使用 shutil 库, 这个库是 Python 的内置库, 可以和 os 完成一些互补操作.
import shutil
# shutil.rmtree(dir_path) # 此方法可以递归删除非空目录!

# 删除文件
# os.remove(dir_path)

# 切换目录: 这个就是 Linux 中的 cd 命令.
os.chdir(os.path.expanduser('~/Desktop')) # 切换目录到桌面
## 此时再对比一下 os.getcwd() 和 os.path.dirname(__file__) 的区别:
print(os.getcwd()) # /Users/hunan/Desktop
print(os.path.dirname(__file__)) # /Users/hunan/Documents/Python 学习笔记
# 所以说, 这两者还是有区别的, 如果需要严格的当前文件所在路径, 还是要用第二种方法!


# 如何批量复制文件? 
def copy(src, tar):
    if os.path.isdir(src): # 先判断 src 是否是文件夹
        filelist = os.listdir(src) # 把目录 src 下的所有文件/目录名存入一个列表中.
        for file in filelist: # file 是文件/目录名.
            # 获取每个 file 的完整路径名, src/file 就对了.
            path_r = os.path.join(src, file)
            with open(path_r, 'r') as f: # 如果目录下有图片或者doc文件, 记得 mode='rb', 相应的, 下面写要用 'wb'
                container = f.read()
                # 获得需要写入的完整路径名.
                if os.path.isdir(tar):
                    path_w = os.path.join(tar, file)
                    with open(path_w, 'w') as f:
                        f.write(container)
                else:
                    print('写入路径有误!')
    else:
        print('读取路径有误!')

src_path = os.path.dirname(__file__)
tar_path = os.path.expanduser('~/Desktop')
# copy(src_path, tar_path)
'''
上面的代码只能批量复制一个目录的若干文件, 如果目录下有文件夹就会报错.
'''
# 如何批量复制文件? (升级版)
# 上面的函数既然只针对于文件, 那么一遇到目录, 我就运用递归, 对他重新执行此操作!
def copy_pro(src, tar):
    filelist = os.listdir(src) # 获取 src 下的所有文件名和目录名
    for file_name in filelist:
        # 思考代码逻辑:
        # path_r 它其实就是 src 下面的文件或目录的路径, 它是文件时, 只需直接复制(读)就好, 但如果它是目录, 则需要
        # 对其递归! 而对于 path_w 也是如此啊, 如果是文件, 直接粘贴(写); 如果是目录, 需要创建一个新目录!
        # 所以, path_r 和 path_w 都要写在这个位置!
        path_r = os.path.join(src, file_name)
        path_w = os.path.join(tar, file_name) # path_r 是目录, path_w 肯定也是目录, 主要是 file_name 就是目录
        # 如果是目录, 则进行递归操作.
        if os.path.isdir(path_r):
            # 进行递归操作之前, 现在需要粘贴的位置建立新文件夹.
            os.mkdir(path_w)
            # 为什么路径这样改? 因为我进入一个目录后, 需要把里面的文件复制到目标目录相应的目录蹭几下!
            copy_pro(path_r, path_w)
            # return copy_pro(path_r, path_w) # 思路总体是没问题的, 这里不用 return 就对了!
            # 递归的代码一层结束了之后怎样返回? 我还是不懂, 说明我对递归的理解深度依旧不够.
        else: # 如果不是目录, 则像上面那样正常复制即可. 复制, 就是先读后写.
            with open(path_r, 'rb') as f: # 1. 先读
                container = f.read()
                with open(path_w, 'wb') as f: #再写
                    f.write(container)

# src_path = os.path.dirname(__file__)
# tar_path = os.path.expanduser('~/Desktop')
src_path = '/Users/hunan/Documents/goodbook'
tar_path = '/Users/hunan/Desktop/target'

# copy_pro(src_path, tar_path)