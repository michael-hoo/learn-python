'''
    已经有一个帖子“昨天晚上遇到一个漂亮的小姐姐，要不要表白？”
    输入用户名：小白
    支持反复回复，要求：
    1. 回复内容不能为空。
    2. 回复中不能存在敏感词。
    3. 最多评论20个字，剩余多少个字。
    4. 回复的内容前后不能有空格。

    例如：
    小白：抓紧表白。
    小黑：就你这b样？算了吧！
    小花：你长得帅吗？
'''
msg = input('发表一句话:')
print('-' * 50)
print('以下内容为回复内容:')
while True:
    # 输入用户名
    user_name = input('请输入您的用户名:')
    # 输入回复内容
    comment = input('请输入您的评论:').strip() # 用户输入完毕, 直接将评论前后的空格清除掉.
    # 验证内容
    if len(comment) == 0 or len(comment) > 20:
        print('评论输入不能为空, 且长度不能超过20个字!')
        continue
    # 成功发出评论, 否则重新输入
    else:
        comment = comment.replace('b', '*')
        print('{0}说: {1}'.format(user_name, comment))
        break
