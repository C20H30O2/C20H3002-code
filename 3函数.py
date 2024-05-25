# 函数
a="abbcccdddd eeeee"
l=len(a)# len为自带的函数
print(l)


def my_len(str):# 用自己定义的len函数计算长度
    count=0
    for i in str:
        count+=1
    print(f"长度为{count}")
#
# str1="666666"
# str2="7777777"
# str3="88888888"
# my_len(str1)  # 调用函数的格式 函数名（参数）
# my_len(str2)
# my_len(str3)

# 函数的定义
# def 函数名(传入的参数):     函数的基础定义   参数用于在函数使用时能够接受外部的数据
#     函数体
#     return 返回值  #这一行暂时不学

#
# def say_hello():# 传入的参数如果不需要可以省略
#     print("hello")
# say_hello()
#
# def add(x,y):# x,y为两个形式参数   可以没有参数也可以有n个参数
#     print(f"{x}+{y}={x+y}")
#
# add(3,7)# 3，7为实际参数

# 应用，自动查核酸
# def check(a):
#     if a<=37.5:
#         print("体温正常，请进")
#     else :
#         print("体温过高，隔离")
# check(int(input("请出示健康码,输入体温:")))


# 函数的返回值
# def add(x,y):
#     result=x+y
#     return result# 可以使函数产生一个返回值（此处返回了result），这个返回值可以被变量接收
  # print("hello")# 函数遇到return后不会执行之后的内容，
# a=add(3,4)# 接收函数的返回值
# print(a)
#
#
# # 如果函数没有return语句，仍然会有返回值
# def add(x,y):
#     print(f"{x}+{y}={x+y}")
#
# a=add(3,4)
# print(a)# 结果为输出None
# print(type(a))# 类型 <class 'NoneType'>
#
# def add(x,y):
#     print(f"{x}+{y}={x+y}")
#     return None  # 如果不写也会默认返回None

# 在if判断中 None等同于False
# def check_age(a):
#     if a>=18:
#         return "满足要求"
#     else:
#         return None
# result=check_age(int(input("年龄：")))
# if not result:
#     print("未成年请不要进入网吧")
#
#
# # None用于声明无初始值的变量
# name=None# 表示暂时不给name赋值





# 函数的说明文档  给函数添加说明文档，辅助理解函数
# def add(x,y):
#     """
#     add函数可以接收两个参数，并进行相加
#     :param x: 形参x表示参与相加的一个数字
#     :param y: 形y表示参与相加的一个数字
#     :return: 返回值是两数相加的结果
#     """
#     result=x+y
#     print(f"{result}")
#     return result
# add(5,6)# 将鼠标悬停在引用的函数上可以查看说明文档



# 函数的嵌套调用  在一个函数里面又调用另一个函数
# def func1():
#     print("a")
# def func2():
#     print("b")
#     func1()
#     print("c")
#
# func2()


# money=50000
# name="tom"
# a=input("输入姓名:")
# while a==name:
#     g=input("欢迎，查询余额a\n存款b\n取款c\n:")
#     if g=="a":
#         print(f"您的余额是{money}")
#         continue
#     elif g=="b":
#         m=int(input("输入您要存的数目:"))
#         money = money +m
#         print(f"当前余额为{money}")
#         continue
#     elif g=="c":
#         m = int(input("输入您要取的数目:"))
#         money=money-m
#         print(f"当前余额为{money}")
#         continue
#     else :
#         print("输入错误，请重新输入")
#         continue
#


# 标准示范
money=500000
#name=None
name=input("输入姓名:")
def query(biaoti):# 借判断biaoti是否为真来控制是否输出”查询余额“的标题
    if biaoti:
                 print("查询余额")
    print(f"{name}你好，剩余{money}元")

def save(num):
    global money
    money+=num
    print("存款")
    print(f"{name}你好,成功存款{num}元")
    query(False)

def get(num):
    global money
    money-=num
    print("取款")
    print(f"{name}好，成功取款{num}元")
    query(False)


def main():
    print("主菜单")
    print("请选择操作")
    print("查询余额\t[1]")
    print("存款\t\t[2]")
    print("取款\t\t[3]")
    print("退出\t\t[4]")
    return   input("您的选择：")# 将输入的值返回，以进行下一步判断


while True:# 制造死循环使得程序一直运行
    keyboard_input=main()# 接收main函数的返回值
    if    keyboard_input=="1":
        query(True)
        continue
    elif   keyboard_input=="2":
        num=int(input("输入要存的钱数："))
        save(num)
        continue
    elif   keyboard_input=="3":
        num = int(input("输入要取的钱数："))
        get(num)
        continue
    else :
        print("要退出了")
        break



x=1
y=2
def func():
    x=3
print(x)# 这里形式参数的变化没有影响到xy的变化

# 但是对与字典，列表，集合来说则会有所改变

