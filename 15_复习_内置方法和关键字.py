# 1. Python 的常用内置方法: print, input, len, id, type, bin, oct, hex
'''
    - chr(): 根据 ASCII 码, 返回对应字符.
    - ord(): 根据字符, 返回对应 ASCII 码.
    - max(): 找出最大值.
    - min(): 找出最小值.
    - sum(): 求和.
    - abs(): 求绝对值.
    - sorted(): 排序.
'''
# 1.1 chr() 和 ord(): ASCII码共128个, 范围是0~127.
print(ord('A'), ord('a'), ord('1')) # 65 97 49
print(chr(65), chr(97), chr(49)) # A a 1

# 1.2 max() 和 min(): 列表, 元组, 集合均适用.
l = [1, 1, 7, 4, 9, 6]
print(max(l)) # 9
print(min(l)) # 1
t = (1, 1, 7, 4, 9, 6)
s = {1, 1, 7, 4, 9, 6}
print(max(t), max(s)) # 9 9

# 1.3 sum(): 同样是列表/元组/集合都适用.
l = [1, 2, 3, 4, 5]
print(sum(l)) # 15
t = tuple(l)
s = set(l)
print(sum(t), sum(s)) # 15 15

# 1.4 sorted()
# 已知 list 有排序方法 sort(), 那元组怎么排序? 可以使用 Python 内置的排序方法 sorted()!
t = (45, 12, 78, 90, 10, 55)
# sorted() 方法返回的是排好序的列表.
print(sorted(t)) # [10, 12, 45, 55, 78, 90]
# sorted() 方法支持倒序排序.
print(sorted(t, reverse=True)) # [90, 78, 55, 45, 12, 10]
# 同理, list 和 set 同样可以使用该方法进行排序(排序之后产生新列表, set 是无序的)
l = list(t)
s = set(t)
print(l, s) # [45, 12, 78, 90, 10, 55] {10, 12, 45, 78, 55, 90}
print(sorted(l), sorted(s)) # [10, 12, 45, 55, 78, 90] [10, 12, 45, 55, 78, 90]


# 2. 符号和关键字: +, -, *, &, |, del, in, not in, is
'''
    + -> 支持字符串/列表/元组.
    * -> 支持字符串/列表/元组.
    - & | -> 只能在集合中使用.
    in, not in -> 支持字符串/列表/元组/字典(注意: 在字典中只判断 key 是否存在).
'''