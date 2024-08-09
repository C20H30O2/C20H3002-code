# 面向对象
# 使用对象组织数据
# 在生活中设计表格，打印表格，填写表格  分别对应程序中设计类（class），创建对象，对象属性赋值
class Student () :  # 设计类   可理解为创建一张表格中要填的项目  # 类的名称的首字母要大写是因为规范，但不强制要求
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

stu_1=Student # 创建对象      可理解为为学生1领到一张表格

stu_1.name="jack"    # 对对象的各个属性进行赋值     为学生1填表格
stu_1.gender="man"
stu_1.nationality="china"
stu_1.native_place="shangrao"
stu_1.age="18"

print(stu_1.name)# 获取到了对象的某一信息
# 类的定义和使用
class name():  # class 类的名称：
    a=None   # 类的属性  即定义在类中的变量（成员变量）

    def print_name(self,msg):  # 类的行为  即定义在类中的函数（成员方法）  形式参数self是必要的，这里msg是我  自己添加的，意在说明可以自行添加变量实现多种功能
        print(f"名字是{self.a},{msg}")

stu_3=name()# 创建对象
stu_3.a="jack"
stu_3.print_name(msg="大家好呀") #调用成员方法   还用了关键字传参

# 现实的事物有属性和行为，与类中的属性和行为相对应，使用类可以完美描述显示的事和物

# 设计一个闹钟类
# class Clock:
#     id=None
#     price=None
#
#     def ring(self):
#         import winsound   # 引入win自带的声音
#         winsound.Beep(2000,3000)  # 设置频率等参数
#
# clock_1=Clock()
# clock_1.id="10086"
# clock_1.price=20
# clock_1.ring()



# 高效赋予属性  使用构造方法：__init__()
class Student:
    # name =None  存在__init__时这里可以省略
    # age = None
    def __init__(self,name,age): # 特点：无需引用，自动执行
        self.name = name
        self.age = age
        print("Student类创建了一个对象")

stu_1=Student("a",18)
print(stu_1)# 打印出相关的地址



class Student:
    # name =None  存在__init__时这里可以省略
    # age = None
    def __init__(self,name,age): # 特点：无需引用，自动执行
        self.n = name
        self.a = age
        print("Student类创建了一个对象")
    def __str__(self):# 可以定义直接打印对象时输出的内容
        return f"Student类对象，name={self.n},age={self.a}"
    def __lt__(self, other):
        return self.a<other.a
    def __le__(self, other):
        return self.a<=other.a
    def __eq__(self, other):
        return self.a==other.a

stu_1=Student("a",18)
stu_2=Student("b",19)
print(stu_1)# 使用__str__后结果与上面不同
print(stu_1<stu_2)# 未定义__lt__时无法直接将两个对象进行>或者<比较，定义后可以比较并输出True 或者 False
print(stu_1>stu_2)
print(stu_1<=stu_2)# 同理，定义__le__可   以允许<=和>=的比较
print(stu_1>=stu_2)
print(stu_1==stu_2)# 如果没有定义__eq__那么比较的是地址，结果一定是False  定义之后可以按自己的想法判断两个对象是否相等
print(stu_1==stu_2)


# class Student:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#
# i=1
# if i<=10:
#     for x in range(1,11):
#         print(f"输入第{i}位学生的信息")
#         a=input(f"输入第{i}位学生姓名\n")
#         b=input(f"输入第{i}位学生年龄\n")
#         c=input(f"输入第{i}位学生地址\n")
#         stu=Student(a,b,c)
#         print(f"第{i}位学生{stu.name}{stu.age}{stu.address}")
#         i+=1


# 将现实世界事物在类中描述为属性和方法，即为封装
# 私有成员    类对象无法访问私有成员，类中的其他成员可以访问私有成员
# 定义私有成员变量和私有成员方法都只要在名称开头加__
class Phone:
    IMEI=10085
    producer=None
    num=1
    __current_voltage=None# 当前电压
    def call_by_5g(self):
        print("5g通话已开启")
    def __keep_single_core(self):
        if self.__current_voltage<=10:# 私有成员只能在类内部定义的函数中使用
            print("单核模式运行")


# 单继承  class 子类名（父类名）：
class Phone2024(Phone):
    face_id=True
    IMEI = 10086  # 复写  直接在子类中修该父类中的同名属性或方法即可
                     # 复写之后，如果想调用父类中的原来的成员
    def father(self):# 方法一    要使用父类成员变量时：父类名.成员变量    要使用父类成员变量时：父类名.成员方法(self)
        print(f"父类的产品代码是{Phone.IMEI}")
        Phone.call_by_5g(self)
    def father2(self):
        print(f'父类的产品代码是{super().IMEI}')# 方法二   super().成员变量   super().成员方法
        super().call_by_5g()




iphone=Phone2024()
print(iphone.num)# 继承了父类中的num
iphone.father()
iphone.father2()



class Phone2025():
    IMEI=10087


# 多继承
class Phone2026(Phone2024,Phone,Phone2025):
    pass  # 不想写入或没有东西要写入可以pass

my_phone=Phone2026()
print(my_phone.IMEI)# 这里打出的是Phone2024的imei  说明不同父类中的同名成员取继承排序中最左的那个




# import random
# a=random.randint() # 在括号内停留时会自动提示括号内要填入的内容为两个类型为int的参数
# list.    输入.后也会自动提示可选的方法，方便直接填入
# def func(data):
#     data.  # 但对于自己定义的内容，比如这里data.之后却不会有提示，因为系统不知道data的类型
# 所以引入了类型注解  主要功能：帮助第三方ide工具（如pycharm）对代码进行类型推断，协助做代码提示
#                          帮助开发者自身对变量进行类型注释
# 类型注解支持对变量的类型注解，对函数（方法）形参列表和返回值的类型注解

# 基础数据类型注解  这些数据一般能直接看出类型，无需注解，因为没有什么意义
a:int =10
b:float =10.00
c:bool =True
d:str ="jack"

# 对容器注解
my_list:list =[1,2,3]
my_list1:list[int]=[3,4,5]  # 详细注解
my_tuple:tuple[str,int,bool]=("jack",22,True)# 对元组的详细注解要一一对应
my_tuple1:tuple=(1,2,3)
my_set:set={1,2,3}
my_set1:set[int]={1,2,3}
my_dict:dict={"a":1}
my_dict1:dict[str,int]={"a":1}


# 对类的对象进行注解
class Student():
    pass
stu:Student=Student()


# 在注释中进行类型注解
import random
import json
class Student1():
    pass
e=random.randint(1,10) # type:int
f="abc"  # type:str
g=json.loads('{"name":"jack"}')  # type:dict[str,str]
# h=func() # type:int   # 这里表示对某个函数的返回值进行类型注解的情况，因为上面没有定义相关函数，所以屏蔽掉防止报错


# 对于一些显示出内容的数据一般无需注解，因为一眼就能看出类型，
# 一般，无法直接看出变量类型之时会添加变量的注解
# h=func() # type:int   # 比如对函数的返回值注解

j:int="abc"  # 不会报错，注解只是为了方便，不会影响程序运行，在任何地方进行的注解的类型错误都不会报错


# 函数（方法）的类型注解——形参注解
def func(data1:int,data2:int):
    return data1+data2
l=func(1,2)   # 有了上面的注解后，在打出l=func()后在括号内停留会提示要输入的参数类型

def func1(data:list):
    m=data.clear()# 有了注释之后 打出.之后会自动提示list类型的可以方法


def func2(data:list)->list:# 对返回值注解
    return data


# union类型联合注解
from typing import Union
my_list2:list[Union[str,int]]=[1,2,"a"]
my_dict2:dict[str,Union[str,int]]={"a":1,"b":"c"}# value中既有字符串又有数字
def func(data:Union[str,int])->Union[str,int]:
    return data




# 多态：指完成某个行为时使用不同的对象会得到不同的状态
class Animal:  # 抽象类， 父类来决定有哪些方法，具体的方法实现由子类决定  这种写法称为抽象类也叫接口
    def speak(self):# 抽象方法
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal):# 使用同样的函数，对象不同结果不同
    animal.speak()

dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)


# isinstance()如何使用   测试某个对象是否是某个类型
print(isinstance(dog,Dog))