'''
    要求: 
    - 使用文件读写, 对图书信息/用户信息进行持久化保存.
'''

# 用户注册函数
def register():
    """要求用户输入用户名和密码及确认密码, 当用户两次输入的密码相同:
    则将该用户的用户名和密码写在指定文件中进行持久化保存!
    """
    user_name = input('请输入您的用户名:')
    password = input('请输入您的密码:')
    re_password = input('再次输入您的密码:')

    if password == re_password:
        with open('./Library_System/users.txt', 'a') as a:
            a.write('{}, {}\n'.format(user_name, password))
        print('用户注册成功!')
    else:
        print('两次密码不一致, 请重新输入!')

# 用户登录函数
def login():
    """让用户输入用户名和密码, 并对其进行验证. 具体的验证方式是这样的:
    - 先从存放用户名/密码的文件中读取用户名(遍历), 看看有无指定用户:
        - 若有该用户, 再判断密码是否正确;
        - 若无该用户, 验证错误.
    """
    user_name = input('请输入您的用户名:')
    password = input('请输入您的密码:')
    with open('./Library_System/users.txt', 'r') as r:
        container = r.readlines()
        # print(container) # ['admin, 1234\n', 'hunan, 1234\n', 'Nathan, 1234\n']
        # 对 container 进行遍历, 每个 user 都是包含用户名和密码的字符串, 需要进行字符串处理.
        for user in container:
            # print(user.split(',')) # 对字符串进行切割, 得到这样的列表 ['admin', ' 1234\n']
            u = user.split(',') # u 是一个包含用户名和密码的列表, u[0] u[1]
            # 用户名验证成功, 再验证密码.
            if user_name == u[0]: # 验证用户名
                if password == u[1].strip(): # 验证密码
                    print('用户登录成功!')
                    break # 这里不放 break 的话, else 语句就会执行.
        else:
            print('用户名或密码错误!')

# 展示图书馆里的所有图书
def show_books():
    print('以下是图书馆里的书'.center(50, '*'))
    with open('./Library_System/books.txt', 'r') as r:
        books = r.readlines()
        for book in books: # 每个 book 是一个包含书名的字符串.
            print(book.strip().center(50))

# 用户借书

# 用户还书

# register()
# login()
# show_books()