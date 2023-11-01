# Lock 用于解决线程安全问题
import threading

# 用法一: try...finally 模式
lock = threading.Lock()
lock.acquire()
try:
    # 加锁代码填写处
    pass
finally: # 锁用完一定要释放, 否则程序会进入阻塞状态, 放到 finally 中必定会执行
    lock.release()

# 用法二: with 模式
lock = threading.Lock()
with lock:
    # 加锁代码填写处
    pass
'''
推荐使用第二种方法:
 - 首先, 代码更简洁;
 - 其次, 跟 with...as 文件处理语句风格统一.
'''