'''
练习: 编写一个简单的工资管理程序, 系统可以管理以下四类人: 工人, 销售员, 销售经理, 经理. 所有的员工都有工号, 姓名, 
工资等属性, 有设置姓名, 获取姓名, 获取员工号, 计算工资等方法. 
 (1) 工人 Worker: 工人具有工作小时数和时薪的属性, 工资计算方法为 "工作小时数 * 时薪"
 (2) 销售员 Salesman: 具有销售额和提成比例的属性, 工资计算方法为 "销售额 * 提成比例"
 (3) 销售经理 Salesmanager: 具有固定月薪的属性, 工资计算方法为 "销售额 * 提成比例 + 固定月薪"
 (4) 经理 Manager: 具有固定月薪的属性, 工资计算方法为固定月薪.
根据以上要求设计合理的类, 并完成以下功能: 
 (1) 添加所有类型的人员
 (2) 计算月薪
 (3) 显示所有人的工资情况
'''

# 定义雇员类, 将工人/销售员/销售经理/经理的共性提取出来
class Employee(object):
    count = 0 # 对象计数器: 每创建一个对象, 使用 __init__ 自增1

    def __init__(self, name) -> None:
        Employee.count += 1
        # 将员工属性全部私有化
        self.__name = name
        self.__salary = self.get_salary() # 通过 get_salary 为员工的工资动态赋值
        self.__work_no = Employee.generate_wkno() # 工号

    def __str__(self) -> str:
        return '姓名: {}\t工号: {}\t薪水: {}元'.format(self.__name, self.__work_no, self.__salary)
    
    # 编写一个产生工号的静态方法
    @staticmethod
    def generate_wkno():
        wkno  = str(Employee.count).rjust(6, '0')
        return wkno

    # 工资计算方法: 因为每类员工的工资计算方法不同, 所以需要重写
    def get_salary(self):
        return 0

    # 定义 get/set 方法
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def work_no(self): # 要求工号只读
        return self.__work_no

# 定义工人类
class Worker(Employee):
    def __init__(self, name, hour_salary, work_time) -> None:
        # 定义工人特有的属性
        self.hour_salary = hour_salary # 时薪, 单位: 元
        self.work_time = work_time # 工作时长, 单位: 小时
        super().__init__(name)
    
    def get_salary(self): # 工人的工资 = 时薪 * 工作时长
        return round(float(self.hour_salary) * self.work_time, 2)

# 定义销售员类
class Salesman(Employee):
    def __init__(self, name, saleroom=0) -> None:
        # 定义销售员的特有属性: 销售额
        self.saleroom = saleroom
        super().__init__(name)

    def get_salary(self): # 销售员的工资 = 销售额 * 提成比例
        percent = 0.025 # 销售员的提成比例 写死
        return self.saleroom * percent # 此方法会将计算结果直接付给 __salary 属性

# 定义销售经理类
class SalesManager(Employee):
    def __init__(self, name, saleroom=0) -> None:
        # 定义销售经理的特有属性
        self.saleroom = saleroom
        self.fixed_salary = 3000 # 固定月薪 写死
        super().__init__(name)

    def get_salary(self): # 销售经理的工资 = 销售额 * 提成比例 + 固定月薪
        percent = 0.050 # 销售经理的提成比例 写死
        return self.saleroom * percent + self.fixed_salary

class Manager(Employee):
    def __init__(self, name) -> None:
        self.fixed_salary = 50000 # 固定月薪 写死
        super().__init__(name)

    def get_salary(self):
        """终于明白这里为什么会报错了!
        当我创建一个 Manager 对象时, 会先执行 Manager 中的 __init__ 方法, 而在 __init__ 中, 第一句是: 
        super().__init__(name) 这会调用父类的 __init__ 方法, 然后再看父类的 __init__ 方法, 而这个方法中的 
        self.__salary = self.get_salary() 又会调用当前对象的 get_salary() 方法, 这又会回到 Manager 类的
        get_salary() 方法中, 这个方法的返回值是 self.fixed_salary, 然而此时, 我的 Manager 对象属性
        self.fixed_salary 还没有声明!!!!

        所以, 解决方法是: 把 self.fixed_salary 放到 super() 之前, 或者直接将其定义为类属性!
        改了一下, 果然成功了! 所以, 遇到问题不要害怕, 要一步一步去 Debug!

        Returns:
            float: 工资
        """
        return self.fixed_salary

# 下面对类进行实例化, 传入相关参数
# Nathan 是总经理, 拿固定工资
manager = Manager('Nathan')
print(manager)
# Tom 是销售经理, 本月销售额300000元
tom = SalesManager('Tom', 300000)
print(tom)
# Emma 是销售员, 她本月销售额300000元
emma = Salesman('Emma', 300000)
print(emma)
# Tim 是工人, 他的时薪20元, 工作了160小时
tim = Worker('Tim', 20, 160)
print(tim)

print(Worker.__mro__) # (<class '__main__.Worker'>, <class '__main__.Employee'>, <class 'object'>)
# 这个参数打印了调用顺序: 比如这里 Worker -> Empoyee -> object