# 面向对象

# 什么是面向对象?

# 面向对象有什么好处? (这两个问题等学完之后再仔细探索!)

'''
类
 - 类属性
 - 类方法 
 - 静态方法
 - 魔术方法: __init__, __str__, 这两种最常用.

对象
 - 对象属性: 一般在 __init__() 中进行初始化.
 - 对象方法: ⭐️重点, 要掌握如何定义对象方法(记得传 self 即可).

方法 -> 也就是函数. 在函数式编程中称为"函数", 在面向对象编程中称为"方法".
 - 种类: 对象方法, 类方法, 静态方法, 魔术方法.
'''

print('Phone'.center(50, '*'))
# 定义一个手机类
class Phone:
    # 类属性: 通过 Phone.screen 或者 my_phone.screen 均可访问, 不过后者实际上等于自己新建一个对象属性.
    screen = 'OLED'
    cpu = 'A14'

    def __init__(self) -> None:
        """初始化魔术方法: 此方法在创建对象时会自动调用.
        可以简单理解为: __init__ 方法定义了一个模板, 之后每次创建新对象时, 都会按照这个模板进行初始化!
        """
        # 统一动态添加三个对象属性
        self.brand = 'iPhone'
        self.type = '14 Pro'
        self.price = 0.0
        # 这些属性和类属性有何区别呢? 下面有介绍.
    
    def call(self):
        """对象方法: 对象方法一定要加 self, 它的意思是对象调用此方法时, 会将自身作为参数传递进来.
        比如说, obj.call() -> call(obj)
        """
        # 这里会将调用此方法的对象的地址打印出来.
        print('{}正在打电话'.format(self)) 

# 通过类来创建对象
my_phone = Phone()
your_phone = Phone()

# 创建对象时会自动调用 __init__ 方法, 所以这里的对象默认具有 brand, type 等属性.
print(my_phone.brand + my_phone.type) # iPhone14 Pro

# 通过这个例子可以看出, 方法中的 self 参数指的是调用该方法的对象本身.
print(my_phone) # <__main__.Phone object at 0x1010925d0>
my_phone.call() # <__main__.Phone object at 0x1010925d0>正在打电话
# 为什么类中的方法需要传入 self 参数呢? 
## 我的理解是: 因为一个类会创建很多对象, 它需要直到是谁调用了这个方法. 
## 并且, 把 self 传进去会让方法更加灵活, 因为每个对象各自的属性都不相同, 用 self 可以调用自己的属性.

# 类属性和在 __init__ 方法中初始化的属性有何不同?
## 首先, 它们的相同点是所有对象均可使用. 比如:
print(my_phone.type, my_phone.screen) # 14 Pro OLED
print(your_phone.brand, your_phone.cpu) # iPhone A14
## 不同之处在于类属性可以直接通过类来调用. 比如:
print(Phone.cpu, Phone.screen) # A14 OLED

# 对类属性/对象属性的进一步理解
## 在 Python 中, 对象的属性是可以动态添加的, 比如:
your_phone.color = '红色'
print('你的手机是{}的'.format(your_phone.color)) # 你的手机是红色的
## 这里动态添加的属性, 只有当前对象有, 类和其他对象均没有. 
## __init__ 方法本质上就是在创建对象时, 对当前对象动态添加了几个属性.
## 当你像上面那样调用 your_phone.color 时, 系统会先看类中有没有该属性, 若没有, 再看对象中有没有.

'''
类方法
    特点:
     1. 定义需要依赖装饰器 @classmethod
     2. 类方法的参数是类本身.
     3. 类方法中只能使用类属性, 不可使用 __init__ 中的对象属性.
     4. 类方法的调用方式 cls.method(), 类方法是不依赖于对象的, 在没用对象之前也可以使用.
静态方法 -> 跟类方法很类似
    特点:
     1. 需要装饰器 @staticmethod
     2. 静态方法无需像类方法那样传入参数(不用传入 cls)
     3. 但静态方法也可以访问类属性和类方法.
        - 虽然没有传入 cls, 但我都在类里面了, 直接 类名.属性, 类名.类方法() 就可以了.
     4. 静态方法的调用方式和类方法相同: 类名.静态方法名()
注意: 类方法和静态方法都只能访问类属性和其他类方法, 是不依赖于对象的, 所以常用来完成一些对象创建之前的操作.
'''
print('Dog'.center(50, '*'))
class Dog:
    # 类属性
    type = '狗'
    # 类方法
    @classmethod
    def test1(cls):
        print('-->', cls.type)
    # 静态方法
    @staticmethod
    def test2():
        print('-->', Dog.type) # 这里虽然没有传入 cls, 但可以直接通过类名获得类属性!

    def __init__(self, nickname) -> None:
        self.nickname = nickname

    def run(self):
        print('{}在院子里跑来跑去'.format(self.nickname))
    
    def eat(self):
        print('{}在吃饭...'.format(self.nickname))
        self.run() # 对象的方法可以互相调用, 但是需要由对象 self 来调用.

d = Dog('大黄')
d.eat()
# 通过对象调用类方法和静态方法(本质是根据对象找到其类, 然后再通过类来调用的)
d.test1()
d.test2()
'''
这里的 test() 是类方法, 为什么对象 d 可以调用呢? (静态方法同理)
原理和类属性很相似, 系统会先从对象方法中寻找 test() 方法, 如果找不到就会从类里寻找.
类方法需要传入类本身 cls 作为参数, 这里会将该对象对应的类 Dog 传递进去.
'''
# 通过类调用类方法和静态方法
Dog.test1()
Dog.test2()


print('Cat'.center(50, '*'))
class Cat:
    type = '猫'

    # 魔术方法 __init__(self): 此方法常用于为对象统一创建对象属性及其初始化.
    def __init__(self, nickname, age, color) -> None:
        self.nickname = nickname
        self.age = age
        self.color = color
    # 魔术方法 __str__(self): 作用见下面的代码.
    def __str__(self) -> str:
        return '昵称: {}, 年龄: {}岁, 颜色: {}'.format(self.nickname, self.age, self.color)
    
    def eat(self, food):
        print('{}在吃{}...'.format(self.nickname, food))
        self.catch_mouse() # 对象方法是可以互相调用的, 调用方式就是 self.对象方法()

    def catch_mouse(self):
        print('{}在抓老鼠!'.format(self.nickname))

    def sleep(self, hour):
        if hour < 2: # 这里将对象方法传入的参数作为判断条件.
            print('{}有起床气, 它狠狠挠了你一下!'.format(self.nickname))
        else:
            print('{}睡得很开心, 它想继续吃东西!'.format(self.nickname))

cat1 = Cat('屎蛋', 5, '白色')
print(Cat.type) # 调用类属性
cat1.eat('猫条')
cat1.sleep(1)
cat1.sleep(2)

print(cat1) # 昵称: 屎蛋, 年龄: 5岁, 颜色: 白色
'''
__str__()的作用:
 - 触发时机: 打印对象名时, 会自动触发此方法 -> print(p), str(p), str(self)
 - 不重写 __str__() 打印对象名称, 返回的是一个地址, 地址对于开发者来说没有太大意义, 如果想在打印对象名的时候
   能够显示更多信息(我完全可以将该对象的所有属性打印出来), 就重写 __str__ !
 - 重写 __str__ 时, 一定要在此方法内添加 return, 且只能返回字符串类型.
'''

# 其他的魔术方法如 __new__, __call__, __del__ 一般都不需要重写, 不懂的情况下也别乱重写.
# 其中, __del__ 会在指向对象的指针为0时自动触发, 删除已创建的对象(节省内存空间).
# 我可以手动来删除指针, 使用 del 命令, 比如:
del cat1
del d
del your_phone

import sys
count = sys.getrefcount(my_phone) # 查看指向对象的引用
print(count) # 显示为2, 因为在调用 getrefcount(my_phone) 的时候就加1了.


''' 面向对象的三大特性: 
    1. 封装
    2. 继承
    3. 多态
'''
# 1. 封装 -> 封装需要满足两个要求: 私有化属性; 定义公有的 set/get 方法
## 1.1 私有化属性 -> __属性名: 这样可以使对象属性的访问范围仅限于类中.
print('Student'.center(50, '*'))
class Student:
    __age = 18 # 类属性也可以私有化

    def __init__(self, name, age=18, score=60) -> None:
        self.name = name
        self.age = age
        # 对对象属性进行私有化
        self.__score = score
    
    def __str__(self) -> str:
        return '姓名: {}, 年龄: {}, 分数: {}'.format(self.name, self.age, self.__score)

hunan = Student('hunan')
print(hunan) # 姓名: hunan, 年龄: 18, 分数: 60
# 可以看到, 这里私有化属性也可以访问.

# 这里对对象属性进行更改, 但是私有化属性数值没有发生变化!
hunan.name = '胡楠'
hunan.age = 31
hunan.__score = 100
print(hunan) # 姓名: 胡楠, 年龄: 31, 分数: 60
print(hunan.__score) # 100
# 这里却是100? 这说明我其实是为 hunan 动态创建了一个新属性 __score, 这和 __init__ 中定义的私有属性没有关联.
# 可以验证一下: 当我把第208行代码注掉, 第210行代码就会报错.

## 1.2 定义公有的 set/get 方法 -> 用 set() 进行赋值, 用 get() 进行取值
print('Student_new'.center(50, '*'))
class Student_new:

    def __init__(self, name, age=18, score=60) -> None:
        # 对对象属性进行私有化
        self.__name = name
        self.__age = age
        self.__score = score
    
    # 定义公有的 set/get 方法:
    # set 方法用来赋值.
    def set_name(self, name):
        if len(name) <= 6: # 限制名字的长度
            self.__name = name
        else:
            print('名字长度过长!')

    def set_age(self, age):
        # 定义 set 方法的好处: 当外界对对象属性修改时, 可以加入判断, 这样可以对外界对修改进行一定限制(增强数据安全性 ).
        if isinstance(age, int): # 这里将修改的年龄限制为整型.
            self.__age = age
        else:
            print('年龄必须为整数!')
        
    def set_score(self, score):
        if 100 >= score >= 0: # 这里将修改的分数限制在 0~100 范围内
            self.__score = score
        else:
            print('分数必须在0~100之间!')
    
    # get 方法用来取值.
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_score(self):
        return self.__score
    
    def __str__(self) -> str:
        return '姓名: {}, 年龄: {}, 分数: {}'.format(self.__name, self.__age, self.__score)
    
hunan = Student_new('hunan')
# 这里可以看到我目前的基本信息
print(hunan) # 姓名: hunan, 年龄: 18, 分数: 60
# 对姓名进行修改
hunan.set_name('胡楠')
# 查询姓名的修改
print(hunan.get_name()) # 胡楠
# 对年龄进行错误的修改
hunan.set_age(5.5) # 这里提示了"年龄必须为整数!"
# 查询年龄是否修改成功
print(hunan.get_age()) # 18, 说明年龄没有修改成功
# 对年龄进行符合要求的修改
hunan.set_age(31)
print(hunan.get_age()) # 31, 年龄修改成功!
# 对分数进行错误的修改
hunan.set_score(150) # 提示: 分数必须在0~100之间!
# 对分数进行符合要求的修改
hunan.set_score(99)
print(hunan.get_score()) # 99

# 通过 dir() 能看到对象所具备的属性和方法
print(dir(hunan)) # 这里需要注意的有: _Student_new__age, _Student_new__name, _Student_new__score
# 我对这几个变量进行赋值试试:
hunan._Student_new__score = 200 # 这说明这里的私有只是伪装的私有.
print(hunan.get_score()) # 200
# 结果分数还是被改掉了!!!


## 1.3 开发中常用的私有化处理: 装饰器 @property
print('People'.center(50, '*'))
class People:

    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age
    
    def set_age(self, age):
        if 120 >= age >=0:
            self.__age = age
        else:
            print('请输入正确的年龄!')
    
    def get_age(self):
        return self.__age

    def __str__(self) -> str:
        return '姓名: {}, 年龄: {}'.format(self.name, self.__age)

yuting = People('yuting', 28)
print(yuting) # 姓名: yuting, 年龄: 28
yuting.name = '李雨婷' # 对于非私有化属性, 是以直接赋值的方式进行修改的.
print(yuting.name) # 李雨婷
yuting.set_age(18)
print(yuting.get_age()) # 18
'''
那么问题来了, 我们能否像访问普通属性一样访问私有化属性呢? 因为那样赋值取值都更方便.
这时, 我们就要用到装饰器!
'''
print('People_new'.center(50, '*'))
class People_new:

    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age
    
    @property # 相当于之前的 get 方法(注意它的定义方式)
    def age(self):
        """这里需要着重强调一下装饰器的设置方法:
        1. 必须先定义"get方法", 在get方法上加上装饰器 @property, 方法名就定义成你想用的"属性名".
        2. 定义完"get方法"后, 再定义"set方法", set方法的装饰器是 @age.setter (容易错, 要注意!)
        3. 这俩定义好之后就可以像正常属性一样调用了!

        Returns:
            int: 年龄
        """
        return self.__age

    @age.setter # 相当于之前的 set 方法
    def age(self, age):
        """定义和使用方法看上面, 需要先有 get, 再有 set

        Args:
            age (int): 传入年龄
        """
        if 120 >= age >=0:
            self.__age = age
        else:
            print('请输入正确的年龄!')

    def __str__(self) -> str:
        return '姓名: {}, 年龄: {}'.format(self.name, self.__age)

hunan = People_new('hunan', 18)
'''
这样一来, 我们就可以像普通属性一样修改/调用私有化属性了!
这样做的好处是:
 - 既能像普通属性那样方便使用(修改/调用) -> 对象.属性 = 18, print(对象.属性)
 - 又能像 get/set 那样对数据的修改进行限制.
'''
hunan.age = 150 # 这里会提示年龄输入错误
print(hunan.age) # 18

hunan.age = 31
print(hunan.age) # 31, 成功!

print(dir(hunan))

'''
练习: 定义一个公路类和一个车类
 公路(Road)
    属性: 公路名称, 公路长度
 车(Car)
    属性: 车名, 时速
    方法: 
        1. 求车名在那条公路上以多少时速行驶了多长距离, get_time(self, road)
        2. 初始化车属性信息 __init__
        3. 打印对象显示车的属性信息
'''
print('Road & Car'.center(50, '*'))

class Road:
    def __init__(self, name, len) -> None:
        self.name = name
        self.len = len # 单位: 千米

class Car:
    def __init__(self, brand='Tesla', speed=180) -> None:
        self.brand = brand
        self.speed = speed

    def run(self, road):
        time = round(road.len / self.speed, 2) # 保留2位小数
        msg = '{}品牌的车在{}上, 以{}km/h的速度行驶了{}小时'.format(self.brand, road.name, self.speed, time)
        print(msg)

    def __str__(self) -> str:
        return '车辆品牌: {}, 时速: {}km/h'.format(self.brand, self.speed)

road = Road('长江西路', 100)
my_car = Car()
my_car.run(road)
print(my_car) # 车辆品牌: Tesla, 时速: 180
my_car.speed = 40
my_car.run(road)
print(my_car) # 车辆品牌: Tesla, 时速: 40


# 2. 继承: is a, has a
## 2.1 has a 关系 -> 它并非是继承
# 下面通过 Student, Computer, Book 这三个类来说明 has a 关系:
print('Student & Computer & Book'.center(50, '*'))
class Student:
    def __init__(self, name, age, book, computer) -> None:
        self.name = name
        self.age = age
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        print('{}从图书馆借了一本{}, 作者是{}'.format(self.name, book.book_name, book.author))

class Computer:
    def __init__(self, brand, cpu, price) -> None:
        self.brand = brand
        self.cpu = cpu
        self.price = price

    def __str__(self) -> str:
        return '品牌: {}, CPU型号: {}, 价格: {}'.format(self.brand, self.cpu, self.price)

    def online(self, student):
        print('{}正在使用{}电脑上网...'.format(student.name, self.brand))

class Book:
    def __init__(self, book_name, author, book_num) -> None:
        self.book_name = book_name
        self.author = author
        # 图书编号, 图书管理系统需要用到
        self.book_num = book_num
    
    def __str__(self) -> str:
        return '书名: {}, 作者: {}, 图书编号: {}'.format(self.book_name, self.author, self.book_num)

computer = Computer('苹果', 'M2', 12000)
book1 = Book('道德经', '老子', 1123456)
hunan = Student('hunan', 31, book1, computer)

hunan.borrow_book(book1)
computer.online(hunan)
print(hunan.computer) # 品牌: 苹果, CPU型号: M2, 价格: 12000, 这里的 computer 属性是对象.
print(hunan.books) # [<__main__.Book object at 0x101008d90>], 列表中的对象
# 如何将 hunan.books 中的信息打印出来呢?
for book in hunan.books:
    print(book) # 书名: 道德经, 作者: 老子, 图书编号: 1123456

'''
知识点总结:
 1. has a: 简单来说, 就是在一个对象属性中包含了其他对象. 比如: 一个学生有一台电脑, hunan.computer
 2. 类型:
    - 系统类型: str, int, float, list, dict...
    - 自定义类型: Student, Computer, Book
      hunan = Student(), 可以理解为 hunan 是变量名, Student 是其类型, 就像 num = int(1) 一样, 
      不过在 Python 中, 系统类型不需要声明, 能够自动识别出来, 比如 s = 'abc' 系统知道它是字符串.
'''

## 2.2 is a -> 继承关系: 将每个类中的共性提取出来, 放到父类中.
print('继承'.center(50, '*'))
class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return '姓名: {}, 年龄: {}'.format(self.name, self.age)

    def eat(self):
        print('{}正在吃饭...'.format(self.name))

    def run(self):
        print('{}正在跑步...'.format(self.name))

# class Student(Person):
#     pass

class Employee(Person):
    pass

class Doctor(Person):
    pass

# s = Student('hunan', 31)
e = Employee('Jack', 18)
d = Doctor('Tom', 46)
# s.eat() # hunan正在吃饭...
d.run() # Tom正在跑步...
'''
继承需要我们将若干子类的共性提取出来, 放到父类中, 从而增强代码的复用性. 譬如: 
这里的 Student/Employee/Doctor 都是人, 都会有姓名和年龄, 都会吃饭和跑步, 
所以需要定义一个 Person 类, 将它们公共的部分抽出来.

而所有继承父类的子类, 就同时继承了它的属性和方法! 譬如这里的 Student 就继承了 
Person 的 __init__ 方法, run(), eat()...
'''
# 但如果我们想对子类的 __init__ 方法进行重写, 该怎么办? 这里把上面的 Student 类代码优化一下:
class Student(Person):
    def __init__(self, name, age, score) -> None: # 编辑器会自动生成这些代码
        """自定义 __init__ 方法不要忘了调用父类中的 __init__ 方法!
        super().__init__(name, age) 是什么意思?
         - super 指的就是当前类的父类, 也就是 Person; super() 指的也就是一个 Person 类的对象 -> Person()
         - 这里通过使用 Person 对象调用 __init__ 方法在子类中初始化在父类中定义的属性.
        Args:
            name (str): 姓名 <- 父类
            age (int): 年龄 <- 父类
            score (float): 分数 <- 子类独有
        """
        super().__init__(name, age)
        # 在子类中定义自己独有的属性: 分数
        self.score = score
    
    # 重写(覆盖): 当我在子类中定义了和父类同名的方法, 子类对象默认调用的是在子类中重写后的方法.
    ## 这遵循了"就近原则", 无论属性还是方法, 默认先找对象有没有, 找不到再去类中找, 类中找不到去父类中找...
    def eat(self):
        print('{}考了{}分, 奖励他吃一个狮子头!'.format(self.name, self.score))
    
    # 当然, 重写也可以在父类的基础上优化.
    def run(self):
        # 先执行此代码, 然后再调用父类的 run 方法.
        print('{}正在热身...'.format(self.name))
        return super().run()

# 重新创建一个学生对象
yuting = Student('yuting', 18, 98)
print(yuting) # 返回结果是: 姓名: yuting, 年龄: 18, 说明 Student 对象也继承了父类的 __str__ 方法
yuting.eat()
yuting.run()

'''
注意: Python 支持多继承! 比如, 
    clss Salesman(Employee, SalesManager):
        pass
'''


print('多态'.center(50, '*'))
# 3. 多态
'''
什么是多态? 多态就是指一类事物有多种形态, 比如, 对于动物来说, 它可以是猫, 可以是狗, 也可以是老虎...
多态的概念依赖于继承.
'''
# 以一段代码为例
class Animal(object): # 定义一个动物类, 并定义一个 run 方法
    def run(self):
        print('Animal is running...')

class Dog(Animal): # 定义一个狗类, 继承 Animal 并对 run 方法进行重写
    def run(self):
        print('Dog is running...')

class Cat(Animal): # 定义一个猫类
    def run(self):
        print('Cat is running...')

# 而当我们有一个函数, 需要 Animal 类的对象作为参数传入时
def run_twice(animal):
    animal.run()
    animal.run()

# 我们可以传入一个 Animal 对象, 比如:
run_twice(Animal()) # Animal is running... * 2
# 我们也可以传入一个 Dog 类或者 Cat 类的对象, 比如:                                                                                  
run_twice(Dog()) # Dog is running... * 2
run_twice(Cat()) # Cat is running... * 2

# 这有什么好处呢? 不妨再定义一个 Animal 的子类看看
class Puma(Animal):
    def run(self):
        print('Puma is running very fastly!')

run_twice(Puma()) # Puma is running very fastly! * 2
'''
我们可以看出, 新增一个 Animal 的子类, 不必对 run_twice() 函数进行任何修改, 只要我们传入的参数是 Animal 及其子类, 
他们都会调用自己各自的 run() 方法, 具体执行细节由各自子类而定. 这也符合了著名的"开放封闭"原则: 
 - 对扩展开放: 允许新增 Animal 子类;
 - 对修改封闭: 不需要修改 run_twice() 的具体源码.
而在这里又涉及到静态语言和动态语言之间的区别, 静态语言比如 Java, 由于其在函数参数设置时就将类型写死了, 比如:
    public static void runTwice(Animal animal):
        pass
你只能传入 Animal 及其子类型的对象, 传入其他类型会报错.
而在 Python 这种动态语言中, 只需保证传入的对象有个 run() 方法即可, 比如:
'''
class Car(object):
    def run(self):
        print('The car is running on the road...')

run_twice(Car()) # The car is running on the road... * 2
'''
这就是动态语言的"鸭子类型", 它并不要求严格的继承体系, 一个对象只要"看起来像鸭子, 走路像鸭子", 它就可以被看作鸭子!
当然, 我们也可以通过 isinstance 来实现类似于 Java 中那种严格的多态.
'''
def run_thrice(animal):
    if isinstance(animal, Animal):
        animal.run()
        animal.run()
        animal.run()
    else:
        print('您传入的不是 Animal 对象!')
# 分别传入 Dog, Cat, Puma, Car 试试
run_thrice(Dog())
run_thrice(Cat())
run_thrice(Puma())
run_thrice(Car()) # 您传入的不是 Animal 对象!


'''
单例模式 <- 开发模式的一种
 单例, 就是单个实例/对象.
 当我们使用普通类创建对象时, 每创建一个对象, 就会给它分配一块内存地址.
 在实际开发中, 有可能会遇到只需使用类中部分功能的情况, 不需要太多对象, 
 这时, 就可以用到单例模式, 确保每次创建对象指向的都是同一块内存空间!
'''
# 用以下代码为例:
class Singleton(object):
    # 创建一个私有化类属性, 用于存放单例的地址
    __instance = None
    # 重写 __new__, 因为 __new__ 是负责分配内存地址的.
    def __new__(cls):
        if cls.__instance is None: # 判断类属性是否为空, 第一次创建对象时一定为空
            # 如果为空, 则调用 object 类的 __new__ 方法来分配一块内存空间, 并把地址给 __instance
            cls.__instance = object.__new__(cls)
        # 再将内存地址返回. 并且, 当下一次创建对象时, 由于 __instance 非空, 则不会执行上面的代码,
        # 而是直接将 cls.__instance 中的地址返回.
        return cls.__instance

s1 = Singleton()
s2 = Singleton()
print(s1) # <__main__.Singleton object at 0x103422910>
print(s2) # <__main__.Singleton object at 0x103422910>
# 两次创建对象的地址是相同的, 单例模式实现成功.