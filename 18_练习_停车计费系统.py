'''
停车计费系统: 
- 进入停车场记录进入时间, 如果出去则记录出去时间, 停车时间 = 出去时间 - 进入时间.
- 停车场的数据结构是: [{'车牌1': [进入时间, 0]}, {'车牌2': [进入时间, 出去时间]}, ...]
    - 原则上记录时间应该用 time.time(), 但为了方便演示, 直接用随机数来记录时间.
- 收费标准: 15分钟1块, 1小时4块(未满15分钟按15分钟计费).
- 停车位共50个, 入库一辆车, 车位-1; 出库一辆车, 车位+1; 入库时需要判断有没有空余车位.
'''
import random
import time

# 停车场的数据结构, 初始化是一个空列表
car_park = []
# 停车位数量, 初始值为5
park_num = 5

# 车辆入库方法
def enter_in():
    global park_num # 全局变量
    if park_num > 0: # 有停车位才允许停车
        car_number = input('请输入您的车牌号: ')
        # 时间怎么计算? 一天只有1440分钟, 创建一个 0~1440 的随机数, 作为进入时间.
        enter_time = random.randint(0, 1440)
        # 按照题目要求构建一个记录停车信息的字典
        car = {car_number: [enter_time, 0]}
        # 把字典存入列表 car_park 中.
        car_park.append(car)
        park_num -= 1 # 每次有一辆车入库, 停车位减1
        print('车辆[{}]入库成功, 剩余车位{}个!\n'.format(car_number, park_num))
    else:
        print('不好意思, 没有停车位了, 去其他地方看看吧!\n')

# 车辆出库方法
def go_out():
    car_number = input('请输入您的车牌号: ')
    # 先判断车牌号是否存在于库中
    for car in car_park: # 从列表中遍历字典
        if car_number in car: # 判断字符串是否在字典的 key 中
            # 获取当前车辆的进入时间
            enter_time = car.get(car_number)[0] # 通过 key 车牌获取 value - 一个包含进入时间和出库时间的列表
            # 出库时间: 产生一个比进入时间大, 且小于1440的随机数.
            out_time = random.randint(enter_time, 1440)
            # 把出库时间存入字典中的列表中
            car.get(car_number)[1] = out_time
            # 计算时间差(单位: 分钟)
            time_diff = out_time - enter_time
            # 收费标准: 直接整除15吧, 虽然这样不严谨, 16分钟也只会收一块
            cost = time_diff // 15
            # 成功出库, 车位加1
            global park_num
            park_num += 1
            print('车辆[{}]已成功出库, 需缴费{}元! 剩余车位{}个'.format(car_number, cost, park_num))
            break
    else:
        print('车辆[{}]不在库中, 请重新输入车牌号!\n'.format(car_number))

flag = True
while flag:
    cmd = input('请输入您的指令: \n1 车辆入库\n2 车辆出库\n3 查询所有停车信息\n4 退出系统\n>> ')
    if cmd == '1': # 车辆入库
        enter_in()
    elif cmd == '2': # 车辆出库
        go_out()
    elif cmd == '3': # 查询所有停车信息
        # 直接对 car_park 进行遍历并打印
        for car in car_park: # {'车牌1': [进入时间, 0]}
            # 获得车牌号
            car_number = list(car)[0]
            # 获得入库时间
            ## values() 是把所有值放在一个列表里, 而这个字典的值本身就是一个列表, 像这样 [[time1, time2]]
            enter_time = list(car.values())[0][0]
            # 获得出库时间
            out_time = list(car.values())[0][1]
            print('车牌号:{}\t入库时间:{}\t出库时间:{}'.format(car_number, enter_time, out_time))
    elif cmd == '4': # 退出系统
        print('正在退出系统, 请稍候...')
        time.sleep(1)
        flag = False
        print('系统退出成功!')
    else:
        print('您输入的指令有误, 请重新输入!\n')