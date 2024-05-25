# 初认python  第一个python程序
# print("hello world" )
# print("hello world" )
# print("hello world" )
# ctrl+f为寻找的快捷键，查找关键词   ctrl+d快速复制选中行  ctrl+shift+上下键移动选中行

# python字面量
# python中常用的6种数据类型
# 数字number  包括整数int  浮点数float 复数complex如3+4j       布尔bool表示生活中的逻辑ture表示真1 false表示假0
# 字符串string    程序中要加上双引号表示字符串如"hello" "34"
# 列表lists
# 集合set
# 字典dictionary
print(666)# 完成各种字面量的输出
print(13.14)
print("heima")



# 添加注释增强可读性  以#号注释一行(#后最好加一个空格以符合规范）  以"""   """中间为注释，可以包括多行



# 定义一个变量记录钱包余额
money=50
print("qianbaoyue=",money)
money=money-20
print("qianbaoyue=",money,"yuan")


# 通过type语句查看数据类型
print(type(11)) # 方法一
print(type(11.1))
print(type("jk"))


type_int=type(11)# 方法2
print(type_int)


name="jk" # 方法三
type_name=type(name)
print(type_name)



# 转换变量类别
int_str=str(11)# 整数小数转字符串
print(type(int_str))
float_str=str(11.1)
print(type(float_str))

str_int=int("11")# 字符串转整数小数  字符串中必须是数字才能转  浮点数也可以转整数，但是会丢失精度
print(type(str_int),str_int)
str_float=float("11.1")
print(type(str_float),str_float)


# 命名规则：标识符命名中只能出现英文，中文，数字，下划线_
# 不推荐使用中文，不能用数字开头，不可以和关键字一样，对字母大小写敏感
# 一般对  变量，类，方法  用标识符命名，后两者还没学
# 对变量的命名规范 简洁明了，多个单词组合变量名要用下划线分隔，如first_number=1,英文字母全部小写


# 运算符+ — * /除 //取整除 %取余 **乘方
print(5/3)
print(5%3)
print(5**3)
print(5//3)




# python中定义字符串可用''  " "   """ """
name='jk'
name1="hso"
name2="""nk"""
name3="""n
j
k
"""
print(name)
print(name1)
print(name2)
print(name3)
# 字符串中包含双引号可以用单引号表示字符串，包含单引号可以用双引号表示字符串，也可以用转义字符\解除所包含的引号的效用
name=("\"jk")
print(name)



# 字符串字面量之间的拼接
print("hello"+"jk")
tel=135
print("my phone",tel,"ok")
print("wo shi"+'tel'+"ok")
print("wo shi"+str(tel)+"ok")
# 无法运行print("wo shi"+tel+"ok")


# 字符串格式化，更方便的拼接字符串   %表示占位，s表示将变量变成字符串放入展位的地方
a=1
b=2
c="jk%s,%s"% (a,b) # 按顺序填入
print(c)
c="jk%s"% a
print(c)
# python中常用三种占位类型 %s将内容转换为字符串，放入占位位置
# python中常用三种占位类型 %d将内容转换为整数，放入占位位置
# python中常用三种占位类型 %f将内容转换为浮点型，放入占位位置
c="jk%d"% a
print(c)
c="jk%f" % a
print(c)

#c="jk%s,%s"%(input(),b)
print(c)



# 格式化的精度设置    用m.n控制数据的宽度和精度   m控制宽度，设置的宽度小于数字本身时不生效
# n控制小数点精度，会进行小数的四舍五入
num1=11
num2=11.345
print("将11限制宽度5，结果是：%5d"%num1)# 大于数字本身的宽度部分会用空格代替
print("数字11限制宽度1，结果是：%1d"%num1)
print("数字11.345限制宽度7，小数精度2，结果是：%7.2f"%num2)
print("数字11.345小数精度2，结果是：%.2f"%num2)


# 字符串格式化的方式2   f"{}"   # f:format
a="jk"
b=136
c=11.345
print(f"我叫{a}，电话{b}，。。{c}")
print(f"我叫{a}，电话{5}，。。{c}")
print("{:.2f}".format(c))


# 对表达式进行格式化   表达式:一条具有明确执行结果的代码语句  比如1+1  5*5，
# 不储存变量直接格式化表达式，以简化代码
print("1*1的结果是:%d"%(1*1))
print(f"1*2的结果是:{1*2}")
print("字符串在python中的类型名是:%s"%type("字符串"))

# 练习 计算股价
name="传智播客"
stock_code="003032"
stock_price=19.99
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
stock_daily_growth_factor=1.2
grow_days=7
print("每日增长系数是：%.2f,进过%d天的增长，股价达到了：%.2f"%(stock_daily_growth_factor,grow_days,19.99*1.2**7))



# print("请告诉我你是谁,你几岁了")
# name=input()
# age=int(input())
# print(f"{name}，你{age}岁")



# 用bool，比较运算符 表示真假
# 比较运算符 ==判断是否相等，  ！=是否不相等，<,>,<=,>=,六种
# 用定义的方式
bool1=True# 注意要大写
bool2=False
print(f"bool1变量的内容是：{bool1},类型是:{type(bool1)}")
print(f"bool1变量的内容是：{bool2},类型是:{type(bool2)}")

# 比较
num1=10
num2=10
print(f"10=10的结果是{num1==num2}")



# if语句
# age=int(input())
# vip_level=int(input("一到五级"))
# day=input("输入星期")
# if age<=10:
#     print("不需要门票")
# elif vip_level>=3:
#     print("buxuyaomenpiao")
# elif day=="一":
#     print("不需要门票")
# elif int(input("输入身高cm")) <= 120:# 可以不用变量接收，直接输入进行判断
#     print("不需要门票")
# else:
#     print("不符合要求，需购买门票")
# print("游玩愉快")


# 练习作业 学习str.split的使用，求两点距离


# import math
# n,m= map(int, input().split())
# p,q= map(int, input().split())
# print("{:.2f}".format(math.sqrt((n-p)**2+(m-q)**2)))
import math


# import math
# A=input()
# B=input()
# A=A.split(",")
# B=B.split(",")
# x1=int(A[0])
# y1=int(A[1])
# x2=int(B[0])
# y2=int(B[1])
# print("{:.2f}".format(math.sqrt((x1-x2)**2+(y1-y2)**2)))import math


# A=input()
# B=input()
# A=A.split(",")
# B=B.split(",")
# x1=float(A[0])
# y1=float(A[1])
# x2=float(B[0])
# y2=float(B[1])
# print("{:.2f}".format(math.sqrt((x1-x2)**2+(y1-y2)**2)))

# y1=A.split(",")[1]
# x2=B.split(",")[0]
# y2=B.split(",")[1]
# print("{:.2f}".format(math.sqrt((x1-x2)**2+(y1-y2)**2)))



# 学习统计字符出现个数
# str1 = input()
# str2 = input()
# ncount = str1.count(str2)
# print(ncount)




