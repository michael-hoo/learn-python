'''
    注：在 Python 中，字符串是不可变对象，所以以下各种操作，均不会改变原有字符串本身，只会产生一个新的字符串。
'''

print('1.', '*-' * 20)
# 1. 除了单引号和双引号，Python 同时也支持三引号——用于保留内容的格式。
poem_by_yuting = '''
    武夷山丛琥珀棕，阿拉比卡鲜翠浓。
    水乳交融一气成，亦是咖啡亦乌龙。
'''
print(poem_by_yuting)


print('2.', '*-' * 20)
# 2. 字符串的格式化
'''
    字符串格式化有2种方法：
    1. %d %f %s...等格式占位符
        %s - 字符串 string 🌟
        %d - 整型 digit 🌟
        %f - 浮点型 float
            %.2f - 表示保留2位小数点 🌟
        %o - 八进制整数 
        %x - 十六进制整数 (小写字母 0x)
        %e - 科学技术法 (小写的 e)
        %g - %f、%e 的简写
    2. format()
    3. join()
'''
name = '蔡徐坤'
age = 26
money = 2.5
print('我喜欢听%d岁的%s打篮球，他一首歌能挣%.2f元！' % (age, name, money))

name = '赵丽颖'
age = 18
# 这里的用法和格式占位符是一样的。
result = '美女{}今年{}岁！'.format(name, age) # 美女赵丽颖今年18岁！
print(result)
# 🌟这里是 format 比格式占位符更好用的地方，它可以对某个变量进行复用！！！
result = '美女{0}今年{1}岁，我也{1}岁了！'.format(name, age) # 美女赵丽颖今年18岁，我也18岁了！
print(result)

# join() 的作用: 用某个字符串来连接列表中的字符/字符串.
print('-'.join(['a', '2', 'c'])) # a-2-c
print('-false-'.join(('apple', 'banana', 'orange'))) # apple-false-banana-false-orange

print('3.', '*-' * 20)
# 3. 字符串保留区
s1 = 'Hello'
s2 = s1
s3 = 'Hello'
## 问：s1, s2, s3 的地址一样嘛？
# id() 函数可以返回某变量指向的地址(可以简单理解为C语言中的指针)。
print(id(s1), id(s2), id(s3)) # 结果这三个字符串的地址是一样的。
print(s1 is s3) # output: True, is 用来比较两个变量是否指向同一地址。
'''
    字符串保留池机制：
    s1, s2 的地址相同我还能理解，为何 s1, s3 的地址也相同呢？
    这是因为 Python 中有字符串保留池机制，如果保留池中有该字符串，就会将新变量指向已存在的字符串，
    而不会再新建一个字符串，这是 Python 节省内存的一种机制！

    垃圾回收机制：
    另外，每隔一段时间，“系统”会扫描每个字符串，若没有变量指向它，该字符串所在空间就会被释放。
'''
s4 = 'World'
print(s1 is s4) # output: False


print('4.', '*-' * 20)
# 4. 字符串的切片 s[start:end:step]
s = 'ABCDEFG' # Python 中的字符串和数组一样，都是有索引的，索引范围是 0 ~ lenth-1.
print(len(s)) # output: 7, len() 函数用于获取字符串的长度(即包含几个字符)。
print(s[4]) # E, 获取 s 第5个字符。
print(s[-1]) # G, 获取 s 最后一个字符。

print(s[1:4]) # BCD, 含头不含尾。
print(s[:5]) # ABCDE, s[0:5] 的 0 可以省略。
print(s[3:]) # DEFG, 取到结尾。

## 注意：切片操作中的 step 不仅可以控制切片步长，还可以控制切片的方向！
print(s[::-1]) # GFEDCBA, 直接将字符串倒序！
print(s[0:6:-2]) # 返回一个空字符，因为 step 为负值，是从右往左取的，所以必须 start > end. 
print(s[6:0:-2]) # GEC, 从 index=6 的字符(G)开始取，取到 index=0 的字符(A，不含)。
print(s[:5:-2]) # G, step 为负值时，start 若为空，则默认为 -1，从右向左的开头。


print('5.1', '*-' * 20)
# 5. 字符串的常见操作
## 5.1 获取长度 - len
print(len(s)) # 7

print('5.2', '*-' * 20)
## 5.2 查找内容 - find, rfind, index, rindex
'''
    find() - 从左向右查询第一个查询目标首字符的索引(所以尽可能确保查询目标的独特性)，查不到则返回-1.
    rfind() - 从右向左查询，其他和 find() 一样。
    index() - 和 find() 差不多，但查不到会报错。
    rindex() - 从右向左查询，其他和 index() 一样。
'''
path = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
## 想要获取图片的名字
i = path.find('googlelogo_')
image_name = path[i:]
print(image_name)
## 获取图片后缀名
i = path.rfind('.')
suffix_name = path[i+1:]
print(suffix_name)

print('5.3', '*-' * 20)
## 5.3 计算出现次数 - count
## 统计 path 中斜杠出现的次数
print(path.count('/')) # 7
print(path.count('_')) # 2

print('5.4', '*-' * 20)
## 5.4 字符串判断 - startswith, endswith, isalpha, isdigit, isalnum, isspace (返回值均为布尔型)
'''
    - startswith(s): 判断字符串是否以 s 开头。
    - endswith(s): 判断字符串是否以 s 结尾。
    - isalpha(): 判断字符串是否完全以字母组成。
    - isdigit(): 判断字符串是否完全以数字组成。
    - isalnum(): 判断字符串是否由字母或数字组成。
    - isspace(): 判断字符串是否由空格、换行符、制表符等“空白字符”组成。
    - isupper(): 判断字符串是否全部是大写。
    - islower(): 判断字符串是否全部是小写。
'''
print(path.startswith('https:')) # True
print(path.endswith('png')) # True
print(path.isalpha()) # False
print(path.isdigit()) # False
print(path.isalnum()) # False

print('abc'.isalpha()) # True
print('123'.isdigit()) # True
print('123'.isalnum()) # True
print('  \n \t '.isspace()) # True
print(''.isspace()) # False, 注意空白字符和“空”的区别！

print('5.4 练习1:', '*-' * 20)
'''
    练习1：模拟文件上传。
    - 需要手动输入上传文件的名称。
    - 判断文件名是否大于6个字符，若不满足条件则自动生成一个6位的随机数组成新的文件名。
    - 判断扩展名是否为 jpg, png, gif, 若不是则提示“上传失败”。
    - 成功上传要打印文件名。
'''
import random
# file = input('请输入待上传的文件名(只支持上传 jpg/png/jpeg 文件):')
file = 'hello.jpg'
# 判断扩展名
if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
    # 先获取文件名
    i = file.rfind('.') # 为什么用 rfind()？因为有些文件名带'.'，从右侧查找可以确保万无一失。
    file_name = file[:i] # 这里的 file[:i] 切片刚好就是文件名。
    # 再判断文件名的长度
    if len(file_name) < 6:
        # 重新构建文件名
        file_name = str(random.randint(100000, 999999))
        # 组成完整的文件名称
        file = file_name + file[i:] # 这里的 file[i:] 带点的后缀，如 .jpg
    print('文件\'%s\'已成功上传！' % file)
else:
    print('文件格式不正确，文件上传失败！')

## 上面的练习中产生的随机文件名只包含数字，如何定义随机产生字母+数字的组合呢？

print('5.4 练习2: ', '*-' * 20)
## 练习2: 随机生成6位字母+数字验证码
valid_code = ''
key = 'abcdefghijklmnopqrstuvwxyz0123456789' # 这里就不加大写字母了
lenth = 6 # 这里可以控制验证码的长度
for i in range(lenth): # 设计一个执行6次的循环，每次产生一个随机数字或字母。
    index = random.randint(0, len(key)-1) # 为 key 随机产生一个索引
    valid_code += key[index] # 每循环一次就会追加一个随机的字母或数字，直到形成6位的验证码。
print('新的验证码为:', valid_code)

print('5.4 练习3: ', '*-' * 20)
'''
    练习3: 用户名或者手机号加密码登录
    1. 用户名必须全部小写，首字母不能是数字，长度必须是6位以上。
    2. 手机号码必须是纯数字，长度是11位。
    3. 密码必须是6位数字。
    以上条件均符合，则判断用户名和密码是否正确。
'''
for i in range(3):
    # name = input('请输入用户名或手机号：')
    name = '123123'
    # 对用户名或手机号进行判断
    if (name.islower() and name[0].isalpha() and len(name) >= 6) or (name.isdigit() and len(name) == 11):
        password = input('请输入您的密码：')
        if password.isdigit() and len(password) == 6:
            if (name == 'liyuting' or name == '13135551070') and password == '123456':
                print('登录成功！')
                break
            else:
                print('用户名或密码错误！')
        else:
            print('密码格式错误，请重新输入！')
    else:
        print('无效的用户名或手机号！')
else:
    print('当前账户被锁定，请5分钟后再试！')

print('5.5', '*-' * 20)
## 5.5 替换内容 - replace(old_string, new_string, count)，count 用来指定替换几次，默认全部替换。
s = '我们今天去超市买可乐，晚上做糖醋里脊吧'
result = s.replace('脊吧', '**')
print(result)
## 如何同时替换多个字符串？脊吧，买可乐
result = s.replace('脊吧', '**').replace('买可乐', '***')
print(result)
## 当然，更好的方法是通过正则表达式搞定，这个后面会介绍。

print('5.6', '*-' * 20)
## 5.6 切割字符串 - split, rsplit, splitlines, partition, rpartition
'''
    - 🌟split('sep', n): 用分隔符 sep 来切割字符串，最多切割 n 刀(一般不写)，将切割后的字符串们返回一个列表。
        - 直接用 s.split() 意思是通过换行符 \n 进行切割。
    - 🌟rsplit('sep', n): 和 split() 函数类似，一个从左往右切，一个从右往左切，下面详细介绍。
    - splitline(): 按行分割
    - partition(): 按照分隔符将字符串分为三部分，“分隔符前面的部分”、“分隔符”、“分隔符后面的部分”。
        - 与 split() 不同的是，partition() 返回的是一个元组。
'''
s = 'Nathan Liyuting hunan Mike'
result = s.split(' ') # 用空格来切割字符串，split() 会返回一个列表。
print(result)

# 在 split('sep', n) 的 n 值缺省时，split 和 rsplit 没有区别，设置为1就能看出区别了。
print(s.split(' ', 1)) # ['Nathan', 'Liyuting hunan Mike']
print(s.rsplit(' ', 1)) # ['Nathan Liyuting hunan', 'Mike']

poem = '''武夷山丛琥珀棕
阿拉比卡鲜翠浓
水乳交融一气成
亦是咖啡亦乌龙
'''
print(poem.splitlines()) # ['武夷山丛琥珀棕', '阿拉比卡鲜翠浓', '水乳交融一气成', '亦是咖啡亦乌龙']
print(poem.split()) # splitlines() 和 split() 效果完全一样？

print(s.partition(' ')) # ('Nathan', ' ', 'Liyuting hunan Mike')
print(s.rpartition(' ')) # ('Nathan Liyuting hunan', ' ', 'Mike')

print('5.7', '*-' * 20)
## 5.7 修改大小写
'''
    - title(): 所有单词的首字母大写，其余小写。
    - capitalize(): 一句话的第一个字母大写，其余小写。
    - upper(): 全部转为大写。
    - lower(): 全部转为小写。
'''
s = 'hEllO wORld!'
print(s.title()) # Hello World!
print(s.capitalize()) # Hello world!
print(s.upper()) # HELLO WORLD!
print(s.lower()) # hello world!

print('5.8', '*-' * 20)
## 5.8 空格处理: ljust, rjust, center, lstrip, rstrip, strip
'''
    - strip(): 将字符串首尾的空白字符全部清除。🌟
        - lstrip(): 只去除左侧空格。
        - rstrip(): 只去除右侧空格。
    - center(width, fillchar=' '): 用于对其，使用空格调整对其方式。
        - width 表示调整后的字符串的长度。
        - fillchar 表示使用什么字符来填充，默认是空格。
    - ljust(): 左对齐。同理。
    - rjust(): 右对齐。
'''
s = '  hello world \n \t  '
print( s, len(s)) # 原长度为19
s = s.strip()
print(s, len(s)) # strip 之后的长度为11
# 指定处理后的字符串长度为30，且 s 中的内容放在处理后字符串的正中央
print(s.center(30), len(s.center(30))) #          hello world          30
print(s.center(30, '~')) # ~~~~~~~~~hello world~~~~~~~~~~
print(s.ljust(30, '+')) # hello world+++++++++++++++++++
print(s.rjust(30, '-')) # -------------------hello world

print('5.9', '*-' * 20)
## 5.9 字符串拼接: join
'''
    join 属于列表中的内容，它会将一个列表中的字符串连接成一个完整的字符串。
    ['a', 'b', 'c', 'd'].join()
'''