# # 函数的多返回值
# def add_x(a,b):
#     x=a+b
#     y=a*b
#     return x,y,True,"abc"# return后的代码不会执行，使用同时返回多个
# c,d,e,f=add_x(2,3)


# 函数的多个种类
# 位置函数，关键字函数，缺省函数，不定长函数，对应的传入参数也有四个种类

# 位置参数  调用函数时根据函数定义的参数位置来传递参数
def user_info(name,age,gender):
    print(f"name:{name},age:{age},gender:{gender}")
user_info("jack",18,"man")# 位置要对应

# 关键字参数  通过  键=值   形式传递参数
user_info(age=18,name="jack",gender="man")# 可以乱序
user_info("jack",age=18,gender="man")# 位置参数可以和关键字参数混用，但位置参数必须在关键字参数前面

# 缺省参数
def user_info(name,age,gender="man"):# 提供默认值，此处为gender提供了默认值man
    print(f"name:{name},age:{age},gender:{gender}")
user_info(age=18,name="jack")# 有缺省参数引用函数时可以不填写直接用默认值
user_info(age=18,name="jack",gender="woman")# 可以修改

# 不定长参数
# 类型1  位置传递   位置不定长
def user_info(*args):# 由*标记为位置传递类型的不定长参数 规范命名为args，不是也行
    print(f"args的类型为{type(args)},内容为：{args}")
user_info("tom")         # 不定长定义的形式参数会以元组形式存在，接收不定长数量的参数传入
user_info("tom",18)# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组，args为元组类型，这就是位置传递
print()

# 类型2   关键字传递
def user_info(**kwargs):# 规范命名为kwargs    key_word args
    print(f"kwargs的类型为{type(kwargs)},内容为：{kwargs}")# 打印出来为字典类型

user_info(name="tom",age=18)# 参数是  键=值  的情况下，所有的 键=值 都会被kwargs接收，同时会根据 键=值 组成字典


# 函数作为参数传递   这是一种计算逻辑的传递而不是数据的传递，不只是数字计算，任何逻辑都可以自行定义并作为函数传入
def test_func(func):# 提供数据，将其他函数作为参数对数据进行处理
    result=func(1,2)
    print(result)
def a(x,y):
    return x+y

def b(x,y):
    return x*y

test_func(a)# 用a的方法处理
test_func(b)# 用b的方法处理


# lambda匿名函数
# def定义带有名称的函数，可以重复使用
# lambda定义匿名函数，只可以临时使用一次
# 定义 lambda 传入参数：函数体（一行代码）    传入参数表示匿名函数的形式参数  # 函数体中只能写一行代码
def test_func(func):
    result=func(1,2)
    print(result)
test_func(lambda x,y:x+y)   # 如果只用一次lambda会更简洁



fun=lambda x:print(x/3)
fun(12)# 结果为4.0因为这里的除为浮点除
print(12/3)# 事实上单纯的12/3的结果也是带一位小数


# 文件的编码
# 计算机只认识0和1   要使用编码技术（密码本）将文件翻译成0和1存入     编码技术记录了如何将文件内容翻译成0和1，以及如何翻译回来
# 计算机有多种可用编码，目前使用广泛的是utf——8
# 文件操作主要包含 打开，关闭，读写
# 在python中可以使用open函数打开或新建一个文件
# open(name,mode,encoding)  name:要打开的目标文件名的字符串（可以包含文件所在的路径）
# mode：设置打开文件的模式：只读，写入，追加等   encoding：编码格式 推荐使用UTF-8
# 例子：f=open('python','r',encoding="UTF-8)  模式有r w a 等

f=open("E:/test.py.txt","r",encoding="UTF-8")# encoding实际上不是第三位，所以要用关键词指定
# print(f)
#
# print(f"读取十个字节的结果是{f.read(10)}")  # 读取相关操作方法
# print(f"读取全部内容的结果是{f.read()}")# 连续读时下一个read的开始是上一个的结尾  # a=f.read()将f的内容全部读取并以字符串的形式存入a中
# line=f.readlines()
# print(type(line))
# print(line)# 如果不注释掉上面两行read代码，会导致readlines的内容为空，因为readlines接着上面的结尾  结果的/n表示换行
# line1=f.readline() # 单行读取
# line2=f.readline()
# line3=f.readline()
# print(line1)
#
# #for循环读取文件行   # 防止读取的操作互相影响，在这里要注释掉上面的代码
for line in f:
    print(line)
#
# #有打开就要有关闭否则python会一直占用文件
# f.close()# 停止占用文件，关闭文件   在文件停留50000秒前停止占用
# import time
# time.sleep(50000)# 让程序在此处停留50000秒，程序停留50000秒后再往下走  在此过程中无法对文件进行任何操作，因为一直被占用着




with open("E:/test.py.txt","r",encoding="UTF-8") as f:# with open会在：后的语句执行完后自动结束占用，关闭文件
    for line in f:
        print(f"每一行为{line}")

count=0
with open("E:/test.py.txt","r",encoding="UTF-8") as f:
    for line in f:
        # line=line.strip()  # 如果line取得的每一行最后带有\n 则要去除\n,否则结果可能有误 这里strip（）会自动删除开头和结尾的空格和换行符（\n）,但最新版本的pycharm好像结尾没有\n,所以注释掉了这一行
        list=line.split()
        for code in list:
            if code=="a":
                count+=1
print(f"a出现的次数{count}")


count=0
with open("E:/test.py.txt","r",encoding="UTF-8") as f:
    all=f.read()
    list=all.split()
    print(list)
    for x in list:
        if x=="a":
            count+=1
print(count)

with open("E:/test.py.txt","r",encoding="UTF-8") as f:
    all=f.read()
    num=all.count("a")
    print(num)


# 文件的写入 f.write("指定的内容")  其实写入的地方是在内存的某个缓冲区，不是真正在硬盘中
# 内容刷新 f.flush()  需要刷新文件才能真正把写入的内容转到硬盘中

f=open("E:/test3.py.txt","w",encoding="UTF-8")# 写这串代码时如果实际上不存在test3.py.txt的文件，w模式会自动添加该文件，涉及到文件的追加
f.write("hello world")# 将内容写入到内存中
f.flush()# 在程序停留之前刷新，可以直接在硬盘中找到更新后的文件
import time
# time.sleep(50000)
f=open("E:/test3.py.txt","w",encoding="UTF-8")# 以w模式打开会把文件原有内容清空，再写入下面的write内容内容
for line in f:
    print(line)# 无内容
f.write("NI HAO")
f.flush()

f=open("E:/test3.py.txt","a",encoding="UTF-8")# 以a模式打开不用担心会清空内容，若该文件不存在也会新建文件
f.write("hello world")
f.write("\nhello world")# 在另一行加入内容


f.seek(8,2)#相对于文件结束的位置
f.seek(8,0)#0表示从开头  8表示往后移动八个字节
f.seek(8,1)#1表示从当前位置开始

f.close()# close自带flush的功能


#f.writelines(list)表示将列表的每一个元素占一行写入文件



#f.tell() 返回当前读取案件的指针所在的位置