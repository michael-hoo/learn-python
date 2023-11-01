'''
    二进制：0, 1
    八进制：0, 1, 2, 3, 4, 5, 6, 7
    十进制：0~9
    十六进制：0~9, a~f
'''
# 进制转换
num = 149 # num 是一个十进制数字。
# 1. 十进制 → 其他进制
## 十进制 → 二进制 binary
result_1 = bin(num) # bin()函数的作用是将十进制的数字转化为二进制的数字！
print(result_1) # output: 0b10010101, 以 0b 开头就是一个二进制数。 

## 十进制 → 八进制 octal
result_2 = oct(num)
print(result_2) # output: 0o225, 以 0o 开头就是一个八进制数字。

## 十进制 → 十六进制 hexadecimal
result_3 = hex(num)
print(result_3) # output: 0x95, 以 0x 开头就是一个十六进制数字。

# 2. 其他进制 → 十进制 (直接用 int 函数即可)
# 十六进制 → 十进制
num_hex = 0x95
result_4 = int(num_hex) 
print(result_4) # output: 149

## 二进制 → 十进制
num_bin = 0b10010101
print(int(num_bin)) # output: 149

## 八进制 → 十进制
num_oct = 0o225
print(int(num_oct)) # output: 149

# 3. 其他进制 → 其他进制 (直接使用对应的函数即可)
## 十六进制 → 二进制
num_hex = 0x95
print(bin(num_hex)) # output: 0b10010101

## 二进制 → 八进制
num_bin = 0b10010101
print(oct(num_bin)) # output: 0o225

## 八进制 → 十六进制
num_oct = 0o225
print(hex(num_oct)) # output: 0x95

# 注意：二进制和八进制、十六进制的特殊关系！
'''
    0b1111 = 8+4+2+1 = 15, 所以，一个十六进制最大的数就是二进制的 1111
    二进制 → 十六进制，0b10010101 → 1001 0101 = 0x95
    十六进制 → 二进制，0x95 → 1001 0101(4位一组，不足补0) → 0b10010101
    0b111 = 4+2+1 = 7, 所以，一个八进制最大的数就是二进制的 111
    二进制 → 八进制，0b10010101 → 010 010 101(3位一组，不足补0) → 0o225
    八进制 → 二进制，0o225 → 010 010 101 → 0b010010101(删除前面的0) → 0b10010101
'''