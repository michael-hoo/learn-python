'''
    游戏规则：
    1. 一共有2个骰子，点数为1～6.
    2. 玩游戏需要金币，否则就不能玩。
    3. 玩一次游戏会奖励1枚金币，可以通过充值获得金币。
    4. 充值金额为10的倍数，10元 = 20金币。
    5. 玩一局游戏需要消耗5个金币。
    6. 游戏方式是猜大小，猜对奖励2个金币，猜错没奖励(点数≥6为大，否则为小)。
    7. 游戏结束条件：主动退出，或者没有金币强制退出。
    8. 退出游戏时打印当前金币数，共玩了多少局。
'''
import random

coins = 0 # 金币数

if coins >= 5:
    pass
else:
    # 提示充值
    print('金币不足，请充值！')
    while True:
        money = int(input('请输入充值金额：'))
        if money % 10 == 0:
            coins += money // 10 * 20
            print('充值成功！当前金币有%d个。' % coins)
            # 开启游戏之旅
            print('*'*10, '开启游戏之旅！', '*'*10)
            answer = input('是否开始游戏？')
            n = 0 # 记录游戏次数
            while coins > 5 and answer == '是':
                n += 1 # 开始游戏时，游戏次数就要加一。
                # 开启一局游戏需要扣除5金币
                coins -= 5
                # 开启游戏奖励1金币
                coins += 1
                # 产生两枚随机的骰子数
                ran1 = random.randint(1, 6)
                ran2 = random.randint(1, 6)
                guess = input('洗牌完毕，请猜大小：')
                if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 <= 6:
                    coins += 5
                    print('恭喜您猜对了，你赢了！您当前拥有金币%d个！' % coins)
                else:
                    print('您猜错了……')
                answer = input('是否继续游戏？')
            print('*'*10, '游戏结束！', '*'*10)
            # 打印游戏次数和当前剩余金币数。
            print('本次你共玩了%d局游戏，还剩金币%d个。' % (n, coins))
            break
        else:
            print('不是10的倍数，充值失败。')