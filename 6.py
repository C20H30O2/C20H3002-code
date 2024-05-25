# 异常 bug
# 捕获异常
# 基本捕获语法
try:    # 运行可能出错的代码
    f = open("E:/test4.py.txt", "a", encoding="UTF-8")
except:  # 上述代码运行异常时执行的代码
    print("出现异常")

# 捕获指定的异常
try:
    print(name)# 未定义的变量
except NameError as e:
    print("出现了未定义的变量")
    print(e)# 这里将出现的异常存入了e中，可以print e看看出现的错误

# try:
#     1/0
# except NameError as e:
#     print("出现了未定义的变量")  # 这里的错误是除0错误，上面的类型指定错误，无法捕获，导致报错

try:
    1/0
except (NameError,ZeroDivisionError) as e:# 将多种错误类型放入元组中，可以捕获其中类型的错误
    print("出现了未定义的变量")  #

try:
    1/0
except Exception as e:  # 以这种形式也可以捕获所有的错误
    print("出现了未定义的变量")

try:
    f = open("E:/test.py.txt", "a", encoding="UTF-8")
except Exception as e:
    print(e)
else:# else和finally都是可写可不写的
    print("我是else，是没有发生错误时执行的代码")# 若try中没有错误就会执行完try和else，若有错误就只会执行except
finally:
    print("我是finally，是不管有没有错误都会执行的代码")
    f.close()



# 异常的传递  异常是具有传递性的

# def func01():
#     print("01stsrt")
#     num=1/0
#     print("01end")
# def func02():
#     print("02start")  # 01中没有捕获异常，因为02引用了01，错误就传递到了02
#     func01()
#     print("02end")
# def main():
#     try:
#         func02()# 错误传递到了main中被捕获，所以不会报错，如果所有函数都没有捕获错误，就会报错
#     except Exception as e:
#         print(e)
# main() # 函数定义出错，如果不引用也不会报错

# def func01():  # 如果所有函数都没有捕获错误，就会报错
#     print("01stsrt")
#     num=1/0
#     print("01end")
# def func02():
#     print("02start")
#     func01()
#     print("02end")
# def main():
#         func02()
# main()



# 模块 python模块（Module），是一个python文件，以.py结尾，模块能定义函数，类，变量  也能包含可执行的代码
# 像一个工具包，每一个工具包都有不同的工具可供我们使用以实现不同的功能


# 模块在使用前要先导入，语法：[from 模块名] import [模块|类|变量|函数|*] [as别名]
# 常用的组合形式： import 模块名
# from 模块名 import 类，变量，方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名
import time# 调用模块全部功能
print("start")
time.sleep(1)
print("end")


from time import sleep# 直接调用具体功能
sleep(1)


from time import*# 调用一个模块的全部功能，  与import不同不用加time.
sleep(1)
# 模块别名
import time as t# 将time起一个别名为t输入更加方便
t.sleep(1)
# 功能别名
from time import sleep as sl# 给sleep取别名
sl(1)

# import my_module1# 调用了自己建的my_module1模块
# my_module1.test(1,2)# 使用了其中的test功能
#
# from my_module1 import test
# test(3,4)


from my_module1 import test
from my_module2 import test# 调用了不同模块下的同名功能，后面调用的会覆盖掉前面的
test(4,6)# 执行的是2中的功能


# python包  逻辑上看包是一个模块
 # 物理上看包的本质是一个文件夹，里面包含多个模块文件以及一个__init__.py文件（存在这个文件就是一个包，不存在就仅仅是一个文件夹）
# 自定义一个python包
# 左侧右键可以创建包，会自动在包中生成一个__init__.py文件，包中可以放入多个模块
# import my_package.my_module3
# import my_package.my_module4
# my_package.my_module3.print1()
# my_package.my_module4.print2()


# from my_package import my_module3
# from my_package import my_module4
# my_module3.print1()# 不用写包名了
# my_module4.print2()


# from my_package.my_module4 import print2
# from my_package.my_module3 import print1
# print2()# 更简便
# print1()

from my_package import*# 导入全部模块




# 如何安装第三方包
# python环境中有很多第三方包（非官方），丰富python的生态，提高了开发效率
# 如：科学计算常用numpy包  数据分析常用pandas包 大数据计算pyspark包，apache-flink包  图形可视化matplitlib包，pyecharts包  人工智能tensorflow包
# python没有内置，要安装才能使用
# 用python内置的pip程序安装第三方包   打开命令提示符程序，输入pip install 包名称      以通过网络安装第三方包
# 上面的方法安装时下载速度可能会很慢，因为连接的是国外的网站
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称  以清华提供的国内网站下载
# pycharm点击右下角python3.12处 再点击interpret settings 可以看到已安装的包，点击加号可以搜索其他的包并下载


# 在练习1中练习了python包的构建
