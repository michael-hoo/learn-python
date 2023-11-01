'''
王者荣耀角色管理

角色: 姓名, 性别, 职业
功能要求:
    添加角色
    删除角色
    修改角色
    查询角色
        - 查询单个角色
        - 遍历所有角色
    退出系统
'''
import time

all_role = []  # 存放所有角色的容器
print('*' * 20, '欢迎进入王者荣耀角色管理系统', '*' * 20)
while True:
    choice = input(
        '请选择功能:\n1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.显示所有角色\n6.退出系统\n')
    # 判断
    if choice == '1':
        print('添加角色模块:')
        name = input('\t角色名:')
        gender = input('\t性别:')
        job = input('\t职业:')
        role = [name, gender, job]
        all_role.append(role)  # 将新角色添加到 all_role
        print('成功添加{}到王者荣耀系统!\n'.format(name))
    elif choice == '2':
        print('删除角色模块:')
        role_name = input('请输出你想要删除的角色名称:')
        # 查找是否存在此角色名称
        for role in all_role:
            if role_name in role:  # 判断我输入的角色名是否能和当前角色相匹配.
                # 若匹配, 直接从 all_role 中删除 role(不要只删除 role_name 了)
                all_role.remove(role)
                print('角色{}已从系统中删除'.format(role_name))
                print('-' * 40)
                break
        else:
            print('你所输入的角色不存在与系统中.')
            print('-' * 40)
    elif choice == '3':
        print('修改角色模块:')
        role_name = input('请输出你想要修改的角色名称:')
        # 查找是否存在此角色名称
        for role in all_role:
            if role_name in role:  # 判断我输入的角色名是否能和当前角色相匹配.
                # 若存在, 则继续询问需要修改哪些信息?
                modify_choice = input('您需要修改该角色的哪项信息?\n1.姓名\n2.性别\n3.职业\n4.返回主菜单')
                if modify_choice == '1':
                    new_name = input('请输入角色的新姓名:')
                    role[0] = new_name
                elif modify_choice == '2':
                    new_gender = input('请输入角色的新性别:')
                    role[1] = new_gender
                elif modify_choice == '3':
                    new_job = input('请输入角色的新职业:')
                    role[2] = new_job
                else:
                    print('当前角色{}的最近信息是:'.format(role_name))
                    print(role[0].center(10), role[1].center(10), role[2].center(10))
                    print('-' * 40)
                    print('正在返回主菜单, 请稍候...')
                    time.sleep(1)
                    break
                print(role[0].center(10), role[1].center(10), role[2].center(10))
                print('-' * 40)
                break
        else:
            print('你所输入的角色不存在与系统中.')
            print('-' * 40)
    elif choice == '4':
        print('查询角色模块:')
        role_name = input('请输出你想要查询的角色名称:')
        # 查找是否存在此角色名称
        for role in all_role:
            if role_name in role:  # 判断我输入的角色名是否能和当前角色相匹配.
                print('您所查询的角色信息如下:')
                print(role[0].center(10), role[1].center(10), role[2].center(10))
                print('-' * 40)
                break
        else:
            print('你所输入的角色不存在与系统中.')
            print('-' * 40)
    elif choice == '5':
        print('显示所有角色:')
        for role in all_role:
            print(role[0].center(10), end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print()
            print('*-' * 20)
    elif choice == '6':
        print('正在退出王者荣耀角色管理系统...')
        time.sleep(1)
        print('成功退出!')
        break
    else:
        print('输入错误, 请重新选择!')
