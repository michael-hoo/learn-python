import random
numbers = []
def score_random():
    numbers.clear() # 每次调用此函数之前, 先将 numbers 列表清空.
    for i in range(8):
        numbers.append(random.randint(0, 100))
    else:
        print('排序之前:', numbers)

# 升序冒泡: 把最大的数字移到列表右侧.
score_random()
# 外层循环控制比较轮数, 每次比较会将最大的数字移到列表右侧, 8个数字只需要比较7轮.
for i in range(len(numbers) - 1): 
    # 内层循环控制每轮比较的次数, 第1轮比较7次(i=0), 第2轮比较6次(i=1), 第i轮比较 len-1-i 次.
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j+1]: # 若左侧的数字比右侧大, 则交换两者的位置.
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print('第{}轮交换,结果为{}'.format(i+1, numbers))

print('这是分割线' * 8)

# 降序冒泡: 把最小的数字移到列表右侧.
score_random()
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] < numbers[j+1]:# 若左侧的数字比右侧小, 则交换两者的位置.
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print('第{}轮交换,结果为{}'.format(i+1, numbers))

'''
总结: 对于冒泡排序, 无论升序还是降序, 我只需找到最大/最小的数字, 通过不断比较, 将其移到列表最右侧.
'''