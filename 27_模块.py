'''
在 Python 中, 模块是代码组织的一种方式, 把功能相近的函数或类放到一个文件中, 一个文件(.py)就是一个模块(module), 
模块名就是文件名. 这样做的好处是: 
 - 提高了代码的可复用性和可维护性. 一个模块编写完毕后, 可以很方便地在其他项目中导入. 
 - 解决了命名冲突问题, 不同模块中具有相同名称的函数互不影响.

常用的标准库: 
 - builtins         内建函数(默认加载)
 - math             数学库
 - random           随机数
 - time             时间
 - datetime         日期和时间
 - calendar         日历
 - hashlib          加密算法
 - copy             拷贝
 - functools        常用工具
 - os               操作系统接口
 - re               字符串正则匹配
 - sys              Python自身的运行环境
 - multiprocessing  多进程
 - threading        多线程
 - json             编码和解码JSON对象
 - logging          记录日志, 调试

 1. 自定义模块
 2. 使用系统模块
 3. 第三方模块
'''
print('1. 自定义模块'.center(50, '*'))
# 1. 自定义模块
# 1.1 导入模块并使用模块
'''
导入项目根目录下的模块:
 方法一:
    导入模块 -> import random
    使用模块 -> random.randint(), random.choice()
 方法二: 
    导入模块 -> from random import randint
    使用模块 -> randin()
 方法三: 
    导入模块 -> from random import * (相当于方法二的升级版)
总结: 使用第一种方式调用更简单, 但是用时需要加上模块名, 而用第二种方式, 调用时麻烦, 使用时却很简单.
注意: 导入模块时, 会对模块中的所有代码进行加载, 如果代码中有对函数的调用, 该调用也会执行.
'''
from random import * # 这句代码执行时, 会把 random.py 中的所有代码加载一下. 

print(choice('ABCD'))
print(randint(1, 10))

# 1.2 if __name__ == '__main__'
if __name__ == '__main__':
    print(__name__) # __main__

# 注意: 在当前模块下运行程序, __name__ 的值会变成 __main__
# 而如果将此模块导入到其他 Python 文件中, __name__ 的名称会变成所在的模块名(比如这里是 27_模块).
print(__name__) # 当把此模块导入到其他模块中时, 此代码会自动执行(上面已经说过了).

# __name__ == '__main__' 这个判断主要用于测试, 比如我编写了一个模块, 在模块中直接编写测试代码并运行会比较方便;
# 但直接在模块中编写测试代码, 其他代码中导入该模块时, 测试代码也会被执行.
# 加了此判断之后, 其他代码导入此模块也不会执行测试代码, 只有直接运行该模块才会运行测试代码. 


# 1.3 从包中导入模块
'''
什么是包? 
 包可以理解为专门存放 .py 文件的文件夹, 位于项目的根目录下. 

项目的层次机构: 
 项目 > 包 > 模块 > 类 | 变量 | 方法

从包中导入模块的几种方法: 
 - 方法一: from 包名 import 模块名
 - 方法二: from 包名.模块名 import 类/方法/变量名
 - 方法三: from 包名.模块名 import * 
 - 方法四: import 包名 -> 会直接将包下的所有模块都导入!
'''

# 1.4 __init__.py
'''
__init__.py 文件的作用: 
 - 该文件存放在包内, 当我导入整个包(import 包名)时, 系统会自动执行 __init__.py 文件.
'''

# 1.5 模块的循环导入
'''
什么叫循环导入? 
 A模块
    def test():
        f()
 B模块
    def f():
        test()
简单来说, 就是两个模块间的方法发生了互相调用. 这种情况的出现往往是因为项目架构不当, 导致的.

解决办法: 
1. 重新架构 -> 成本很高
2. 导包时用到再导(定义在函数内部)
    def test():
        from xx import f
        f()
3. 也可以把导入模块放入函数的最后.
'''


print('2. 使用系统模块'.center(50, '*'))
# 2. 使用系统模块
# 2.1 sys模块
import sys

print(sys.path) # 返回导包默认搜索路径
print(sys.version) # 返回当前 Python 解释器的版本
print(sys.argv) # 在终端中执行 Python 文件时可以传参, 这里的返回值就是当前文件的完整路径名及传入的参数(这里没传参) 

# 2.2 time & datetime 模块
import time
# 时间戳: time.time()
t1 = time.time()
print(t1) # 1698386410.8632
# 返回当前时间到1970纪元(即1970年1月1日凌晨)的时间差(小数点之前的是秒, 小数点之后是更精确的时间单位).
# 此方法常用来计算时间差, 比如程序执行时间等等.

# 休眠: time.sleep(t) - 让程序暂时休眠 t 秒.
# time.sleep(1.2345)

t2 = time.time()
print(t2 - t1) # 0.00013709068298339844

# 将时间戳转换成字符串: time.ctime(t) - 也就是以一种可以理解的方法表示当前时间.
print(time.ctime(t1)) # Fri Oct 27 14:00:10 2023

# 将时间戳转换成元组: time.localtime(t)
t = time.localtime(t1)
print(t)
'''返回结果:
time.struct_time(tm_year=2023, tm_mon=10, tm_mday=27, tm_hour=13, tm_min=47, 
tm_sec=9, tm_wday=4, tm_yday=300, tm_isdst=0)
 - tm_wday=4, 指今天在本周
 - tm_yday=300, 指今天是今年的第300天.

以元组的形式返回时间戳的具体时间细节, 直接用元组的取值方式, 取出的都是整型!
'''
print('今天是{}年{}月{}日, 星期{}, {}点{}分{}秒'.format(t[0], t[1], t[2], t[6]+1, t[3], t[4], t[5]))
# 返回结果: 今天是2023年10月27日, 星期5, 13点59分13秒
# 元组中的时间信息还可以用这种方式获得(感觉更方便)
print(t.tm_yday, t.tm_hour) 

# 将元组转换成时间戳: time.mktime()
tt = time.mktime(t)
print(tt) # 1698386410.0, 转回来会删除其秒之内精度值.

# 将元组转换成字符串: time.strftime(format, t) ⭐️
st = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(st) # 2023-10-27 14:10:58
'''格式化符号: 
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

# 将时间字符串转化为元组: time.strptime('str', format)
tst = time.strptime('1992/12/17 01:00', '%Y/%m/%d %H:%M')
print(tst)
'''输出结果:
time.struct_time(tm_year=1992, tm_mon=12, tm_mday=17, tm_hour=1, tm_min=0, tm_sec=0, 
tm_wday=3, tm_yday=352, tm_isdst=-1)
'''

import datetime

# 返回今天的日期: datetime.date.today()
print(datetime.date.today()) # 2023-10-27

# 获取当前的系统时间: datetime.date.now()
print(datetime.datetime.now()) # 2023-10-27 14:29:57.450652

# datetime.timedelta(): 计算时间差, 往往需要与其他时间结合.
now = datetime.datetime.now()
timedel = datetime.timedelta(days=10)
print(now + timedel) # 2023-11-06 14:33:29.946143
# 这里就得出了10天之后的现在的时间信息!
# 计算过去的时间用减法, 计算未来的时间用加法!!!

# 2.3 random 模块
import random
# random.random(): 返回 0~1 之间的随机浮点数
print(random.random())
# random.randrange(start, stop, step): 从 range(1, 3) 中产生一个随机数
print(random.randrange(1, 3))
# 设置一下步长
print(random.randrange(1, 10, 2)) # 返回 1~9 之间的奇数, 因为 range(1, 10, 2) -> [1, 3, 5, 7, 9]
# random.randint(a, b): 注意, randint 不同于 randrange, 它是含头又含尾的! 
print(random.randint(1, 10)) # 返回 1~10 之间的随机数

# random.choice(s): 从一个非空序列中选取一个值.
s = ['胡楠', '李雨婷', 'Nathan', 'Jack']
print(random.choice(s))

# random.shuffle(l): 将列表 l 打乱顺序, 是对列表本身进行操作, 没有返回值, 可以简单理解为字面意思"洗牌".
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.shuffle(l)) # None
print(l) # [8, 0, 3, 6, 9, 4, 7, 5, 1, 2]
# 和排序方法是相反的操作!

'''练习: 生成四位验证码
要求: 
 - 验证码中必须要包含2位数字和2位字母
 - 字母和数字的位置不固定
'''
def valid_code():
    code = ''
    # 产生一个2位的数字字符串
    ran_12 = random.randrange(0, 100)
    if ran_12 < 10:
        ran_12 = '0' + str(ran_12) # 形成 01, 02, ..., 10, 11, ..., 99 的样式
    else:
        ran_12 = str(ran_12)
    # chr(): 将 ASCII 码转化为字符
    ran_3 = chr(random.randint(97, 122)) # 小写字母的 ASCII 码值为 97~122
    ran_4 = chr(random.randint(97, 122))
    # 使用 list() 方法直接将一个字符串拆分成以字母数字为单位的列表!
    code = list((ran_12 + ran_3 + ran_4))
    # 把验证码的顺序打乱(此方法只能用在列表上)
    random.shuffle(code)
    return ''.join(code) # 将单个字符组成的列表再组成一个字符串!
    
print(valid_code()) # e25r

# 2.4 hashlib 模块: 加密算法
import hashlib

msg = '雨婷, 咱们待会一起吃饭去!'
# 注: md5 方法不能直接加密中文, 需要先对中文进行编码!
md5_msg = hashlib.md5(msg.encode('utf-8'))
print(md5_msg) # <md5 _hashlib.HASH object @ 0x10b6e3390>
print(md5_msg.hexdigest()) # 84dbc7f01f1b28f3a8259b100ccd4d0e
# 输出结果为一个十六进制加密数据
# 这种不可解的加密一般用于储存用户的用户名和密码.



print('3. 使用第三方模块'.center(50, '*'))
# 3. 使用第三方模块
'''
Python 中没有内置第三方模块(内置了就不能叫第三方模块了), 所以需要额外下载! 
如何下载呢? 
    在终端中使用: pip3 install pillow 
    如果终端中没有 pip, 那就先: brew install pip3
'''
# 3.1 pillow
# import pillow
import requests
# 一直没安装成功


