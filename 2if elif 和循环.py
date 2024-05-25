# str="abbbbbbbccccccdddddd"
# print("abbbbcccc".count("b"))


# if elif 的嵌套使用
# age=int(input("输入年龄"))
# if age>=12:
#     print("不能免费游玩")
#     print("vip>=3，或每月一日仍可以免费")
#     if int(input("vip_level"))>=3:
#         print("可以免费")
#     elif int(input("日期"))==1:
#         print("可以免费")
#     else:
#         print("需要买票")
# else:
#     print("欢迎你，小朋友")



# if elif 的嵌套使用
# age=int(input("输入年龄"))
# work_level=int(input("输入工作等级"))
# year=int(input("输入工作年数"))
# if age>=18:
#     print("成年，满足条件")
#     if age<=30:
#         print("年龄完全满足条件")
#         if year>=2:
#             print("可以领取礼物")
#         elif work_level>=3:
#             print("可以领取礼物")
#         else :
#             print("不满足条件")
#     else:
#         print("太老了")
# else:
#     print("太年轻了")



# 用嵌套解决猜数字问题
# import random
# num=random.randint(1,10)
# # print(num)
# a=int(input("第一次机会"))
# if a==num:
#     print("一次就猜对了")
# else:
#     print("wrong")
#     if a>num:
#         print("猜大了")
#     elif a<num:
#         print("猜小了")
#
# a = int(input("第二次机会"))
# if a==num:
#         print("第二次时猜对了")
# else:
#         print("wrong")
#         if a > num:
#             print("猜大了")
#         elif a < num:
#             print("猜小了")
#
# a = int(input("第三次机会"))
# if a==num:
#             print("ringt")
# else:
# #            print("失败，答案是%d"%num)
# #            print(f"失败，答案是{num}")
#              print("失败，答案是{}".format(num))



# 循环语句
# while 条件：
# 条件满足时要做的事1
# 条件满足时要做的事2
# 条件满足时要做的事3
# ……

# i=1
# while i<=100:# while的条件需得到bool类型，Ture表示继续，False表示终止
#     print("抄写这句话100次")
#     print(i)
#     i+=1
# 计算1到100的和
# i=1
# a=0
# while i<=100:
#     a+=i
#     print(a)
#     i+=1
# print(a)


# 用循环解决猜数字问题
# import random
# num=random.randint(1,100)
# i=1
# a=int(input("输入你猜的数字"))
# while a!=num:
#     if a>num:
#         print("猜大了")
#     else :
#         print("猜小了")
#     a=int(input("输入你猜的数字"))
#     i+=1
# print("恭喜猜对，一共猜了%d次"%(i))

# 如果通过一个bool类型的变量，做是否循环的标记
# import random
# num=random.randint(1,100)
# count=0
# flag=True
# while flag:
#     a=int(input())
#     count+=1
#     if a==num:
#         print("猜对了")
#         flag=False# 设置为false就是终止循环的条件
#     else :
#         print("猜错了")
#         if a>num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print("猜对了，一共猜了%d次"%(count))


# while 循环的嵌套运用
# i=1
# while i<=100:
#     print(f"今天是第{i}天，准备表白")
#     j=1
#     while j<=10 :
#         print(f"送给小美第{j}支玫瑰花")
#         j+=1
#     print("小美我爱你")
#     i+=1
#
#
# # 限制条件为只有前十天每天送十枝玫瑰花时
# i=1
# while i<=100:
#     print(f"今天是第{i}天，准备表白")
#     j=1
#     k=1
#     while i<=10 and k<=10:
#         print(f"送给小美第{j}支玫瑰花")
#         j+=1
#         k+=1
#     print("小美我爱你")
#     i+=1
# print(f"坚持到第{i-1}天表白成功")# 注意这里的i需要减一，因为跳出循环时i01


# i=1
# while i<=100:# while的条件需得到bool类型，Ture表示继续，False表示终止
#     print("抄写这句话100次")
#     print(i)
#     if i%2==0:
#         print("抄写到偶数次")
#         i+=1
#     else:
#         i+=1



# i=1# 输出100以内偶数
# while i<=100:
#     if i%2==0:
#         print(i)
#         i+=1
#     else:
#         i+=1

# 用while循环打印九九乘法表
# # 补充1
# print("hello",end="")
# print("world")# 这样写print输出不换行
# # 补充2
# print("hello\tworld")
# print("itheima\tbest")# \t制表符使得输出的内容上下行对齐
#
# a=1
# while a<=9:
#     b = 1
#     while a>=b:
#         print(f"{b}*{a}={a*b}\t",end="")
#         b+=1
#     a += 1
#     print()# 换行


# for循环    无法定义循环条件，只能从被处理的数据集中，依此取出内容进行处理
# name="mike,jone"
# for x in name:    # for 临时变量 in 待处理数据集
#     print(f"{x}") # 注意空格缩进
#
# a=0
# name="abbcccddddeeeee"
# for x in name:    # for 临时变量 in 待处理数据集
#     if x=="c" :
#         a+=1
#     # else :
#     #     a+=0
# print(f"共有{a}个c")


# range 语句
# range(6)#从0开始不含6
# range(4,8)#从4到8，不包含8
# range(3,7,2)#从3到7间隔2（不填则默认为1）输出， 3，5，不包含7
# for x in range(7):
#     print(x)
#
# i=1
# while i<=10:
#     print("送一朵玫瑰花")
#     i+=1
#
# for x in range(10):# range一般配合for使用
#     print("song hua")
#
# for x in range(1,101):# 100以内输出偶数
#     if x%2==0:
#         print(x)



# # for循环的变量作用域    该变量作为临时变量按规范只能在循环内部访问
# for i in range(5):
#     print(i)
#
# print(i)# 在循环外也可以访问，但是不规范
#
# i=0# 在循环外先定义出变量，之后再使用就可以符合规范要求
# for i in range(5):
#     print(i)
#
# print(i)



# for循环的嵌套使用
# k=0
# x=0
# for x in range(1,101):
#     print(f"今天是向小美表白的第{x}天")
#     k+=1
#     if k<=10:
#         for i in range(1,11):
#             print(f"送给小美第{i}朵玫瑰")
# print(f"第{x}天表白成功")
#
# k=0# for while相互嵌套
# x=0
# for x in range(1,101):
#     print(f"今天是向小美表白的第{x}天")
#     k+=1
#     if k<=10:
#         i=1
#         while i<=10:
#             print(f"送给小美第{i}朵玫瑰")
#             i+=1
# print(f"第{x}天表白成功")



# 用for循环打印九九乘法表
# a=0
# b=0
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f"{b}*{a}={b*a}\t",end="")
#     print()


# 循环中断  用break，continue关键字控制循环
#continue直接中断本次循环进入下次循环，跳过了循环中continue之后的部分，在for和while中用法一致，
# for x in range(1,6):
#     print("操作一")
#     continue
#     print("操作二")
#
#
# for x in range(1,6):
#     print("操作一")
#     for j in range(1,6):
#         print("二")
#         continue# 在嵌套中时只作用于所属循环
#         print("操作三")
#     print("四")
#
# # break直接结束整个循环,for while中一样，嵌套中也只对所在循环生效
# for i in range(1,101):
#     print("1")
#     break
#     print("2")
# print("3")


# for x in range(1,6):
#     print("操作一")
#     for j in range(1,6):
#         print("二")
#         if j>=4:# 当满足某种条件时可以用break跳出循环
#             break# 在嵌套中时只作用于所属循环
#         print("操作三")
#     print("四")
#

# 综合运用，解决发工资问题
# sum = 10000
# for i in range(1,21):
#     import random
#     num=random.randint(1,10)
#     if num<=5:
#         print(f"第{i}名员工的绩效是{num},不满足条件，没有工资")
#         continue
#     else :
#         if sum>=1000:
#             sum-=1000
#             print(f"第{i}名员工合格，领取1000元工资")
#         else:
#             print("工资已经发完了，下次再来")
#             break

for x in range(1,10+1):
    print(x)
    if x==6:
        break
else :
    print("ok")# 这里的else不会执行，因为上面的for循环没有正常执行完，而是被break中断，对与while循环也相同



