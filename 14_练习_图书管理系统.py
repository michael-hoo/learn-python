'''
要求:
1. library = [{}, {}, {}], 每个字典是一本书, 每本书包含书名/作者/价格/库存, library 中至少有5本不同的书.  
2. 功能:
    1. 借书
    2. 还书
    3. 查询(根据书名/作者查询某本书)
    4. 查询所有
    5. 退出系统
'''
import time

library = [{'book_name': '西游记', 'author': '吴承恩', 'price': 22, 'num': 2}, 
           {'book_name': '红楼梦', 'author': '曹雪芹', 'price': 88, 'num': 2}, 
           {'book_name': '水浒传', 'author': '施耐庵', 'price': 33, 'num': 2}, 
           {'book_name': '三国志', 'author': '罗贯中', 'price': 66, 'num': 2}, 
           {'book_name': '金瓶梅', 'author': '笑笑生', 'price': 44, 'num': 2}]
flag = True
while flag:
    choice = input('请选择:\n\t1.借书\n\t2.还书\n\t3.查询指定书籍\n\t4.查询所有书籍\n\t5.退出系统\n')
    if  choice == '1': # 1. 借书
        # 代码逻辑:
        # - 用户输入他想要借的书.
        # - 先查询系统中有没有他想借的书:
        #     - 若有, 看库存够不够:
        #         - 库存够, 库存-1, 提示成功借出.
        #         - 库存不够, 提示用户暂时无法借书, 等其他同学还书.
        #     - 若没有, 提示用户不存在相关书籍.
        msg = input('请输入您想要借的书:')
        for book in library:
            book_name = book.get('book_name')
            if msg == book_name:
                num = book.get('num') # 获取图书库存
                if num > 0:
                    # 成功借出, 则图书库存-1
                    num -= 1
                    book['num'] = num
                    print('恭喜你成功借出《{}》, 本书当前剩余库存{}本'.format(book_name, num))
                else:
                    print('您想要借的"{}"库存不足, 请等其他同学还书后再来借吧~'.format(book_name))
                # 借书成功后需要跳出循环, 否则 for...else 中的 else 语句还是会执行.
                break
        else:
            print('您输入的书籍目前书库里还没有, 敬请期待!')
    elif choice == '2': # 2. 还书
        # 代码逻辑:
        # - 用户输入想要还的书籍.
        # - 先查询系统中有没有用户要还的书:
        #     - 若有, 则库存加1, 并提示归还成功.
        #     - 若无, 则提示"这本书不是我们店的, 不要还错了哦~"
        msg = input('请输入你要还的书名:')
        for book in library:
            book_name = book.get('book_name')
            if msg == book_name:
                num = book.get('num') # 获取本书的当前库存
                num += 1 # 库存加1
                book['num'] = num # 更新库存
                print('还书成功!{}目前库存是{}本'.format(book_name, num))
                break # 跳出循环, 防止 for...else 语句执行.
        else:
            print('这本书不是我们店的, 不要还错了哦~')
    elif choice == '3': # 根据书名或作者名查询书籍信息, 不存在提示.
        # 需要一个变量存储用户键入的查询信息
        msg = input('请根据书名或作者的姓名进行查询:')
        for book in library:
            book_name = book.get('book_name')
            author = book.get('author')
            if msg == book_name or msg == author:
                price = book.get('price')
                num = book.get('num')
                # 打印图书信息
                print('\t{0}, 作者{1}, 价格{2}元, 库存还剩{3}本'.format(book_name, author, price, num))
        # 失误:不能将 else 和 if 并列, 否则 for 循环会多次执行以下代码!
        else: # 若用户输入的信息, 书库中没有, 则执行以下操作
            print('图书馆中不存在{}相关信息, 敬请期待!'.format(msg))
    elif choice == '4': # 查询书库中存在的所有书籍
        print('图书馆中现有书籍的图书信息如下:')
        # 想法: 通过遍历将所有库存不为0的图书信息打印出来.
        for book in library: # 遍历列表 library 中的每个元素 book, book 均为字典.
            # 获得当前书籍的库存
            num = book.get('num')
            if num > 0: # 书籍有库存的时候才执行以下操作
                book_name = book.get('book_name')
                author = book.get('author')
                price = book.get('price')
                # 打印图书信息
                print('\t{0}, 作者{1}, 价格{2}元, 库存还剩{3}本'.format(book_name, author, price, num))
    elif choice == '5':
        print('正在退出图书管理系统...')
        time.sleep(1)
        print('退出成功!')
        flag = False
    else:
        print('您输入的指令有误, 请重新输入!')