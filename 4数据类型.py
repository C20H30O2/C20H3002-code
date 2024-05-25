# # 数据容器根据特点不同   是否支持重复元素，是否可以修改，是否有序等  分为列表list 元组tuple 字符串str 集合set 字典dict
#
#
# # 列表的定义
#
# # 字面量   [元素1，元素2，元素3，……]
# # 定义变量  变量名=[1,2,3……]
# # 定义空列表 变量名=[]     变量名=list()
# list1=["a","b",6,"d",["你","好"]]# 支持不同类型的数据，可以嵌套，元素有序排列都有相应下标，允许元素重复存在，可以修改
# print(list1)
# print(type(list1))
# # 下标索引
# print(list1[0]) # 从前往后从0开始
# print(list1[2])
# print(list1[4])
# print(type(list1[4]))
# print(list1[-1])# 3从后往前从-1开始
#
# print(list1[4][1])# 嵌套列表中的数据的调用方式
#
# # 对列表的常用操作 插入，删除，修改，统计元素，清空列表等称之为：列表的方法
# index=list1.index(6) # 查找元素对于的下标，若该元素不存在则会报错
# print(index)
#
# list1[0]="g"# 替换对于下标的元素
# print(list1[0])
#
# list1.insert(1,"k")# 在指定位置插入元素
# print(list1)
# print(list1[1])
# list1.append(10)# 直接在列表末尾加入元素
#
#
# list2=[6,7,8,9]# 在指定列表的后面接上另一个指定列表的元素
# list1.extend(list2) # 方法一
# list1.extend([11,12,13])# 方法二
# print(list1)
#
#
# del list1[0]# 直接删除对应下标的元素
# print(list1)
#
# delete=list1.pop(0)# 同样删除对应元素，但有返回值可以被接收
# print(list1)
# print(delete)
#
#
# list3=[1,2,3,3,4,5,6]
# print(list3.count(3))# 统计元素出现次数
#
# list3.remove(3)# 移除列表中第一个匹配项
# print(list3)
#
# list3.clear()# 清空元素
# print(list3)
#
# list3=[1,2,3,3,4,5,6]
# num=len(list3)# 统计列表中全部的元素数量
# print(num)
#
#
# # 列表的遍历（迭代）  将元素逐个取出再进行处理
#
# list1=[1,2,3,4,5,"abc"]
# count=0
# while count<len(list1):
#     print(list1[count])
#     count+=1
#
#
#
# for x in list1:
#     print(x)
#
#
# list=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# count=0
# while count<len(list):# 用while循环找出偶数并存入利另一个list中
#     a=list[count]
#     if a%2==0:
#         list2.append(a)
#         count+=1
#     else :
#         count+=1
# print(list2)
#
#
# list0=[]
# for x in list:# 用for循环
#     if x % 2 == 0:
#         list0.append(x)
#     else :
#         continue
# print(list0)


# 元组    一旦定义完成，不可以修改,尝试修改会报错
# 定义元组字面量 (元素1，元素2……)
# 定义元组变量  变量名称=(元素1，元素2……)
# 定义空元组 变量名称=（）  变量名称=tuple（）
# tuple1=(1,2,3,4,"abc",True)#
# t2=()
# t3=tuple()
# t4=("hello",)# 若只有一个元素，则必须加上逗号，否则不是元组类型
# t5=("hello")
# print(type(t5))
# print(type(t2))
#
# t6=(1,12,2,3,4,(6,7,8,9,),1,1,1)# 元组嵌套和调用
# print(t6[-4][0])

# 由于元素不可修改，可用操作比列表少
# index=t6[5].index(7)# 查找元素下标
# print(index)
#
# num=t6.count(1)# 统计个数
# print(num)
#
# num=0
# while num<9:
#     print(t6[num])
#     num+=1
#
#
# for x in t6:
#     print(x)
#
#
# # 若在元组内定义列表,可以改变列表内的元素
# t7=(1,2,3,4,[1])
# t7[-1][0]="b"
# print(t7)
# print(t7[-1][0])


# 字符串 无法修改
# a="abcd"
# print(a[0])# 字符串的下标索引
# print(a[-1])
# # a[0]="e"# 修改无法完成
# b=a.index("a")# 查找元素的下标
# print(b)
#
# new=a.replace("d","e")# 替换元素
# print(new)
#
# str="a b c d e f"
# list=str.split()# 将字符串以指定字符（默认空格）为界分隔开存入一个列表中，字符串本身没有变化
# print(list)
#
# str2=" 12a|b|c|d|e|fg21 "
# list3=str2.split("|")
# print(list3)
#
# new_str=str2.strip() # 括号不填则默认为去除字符串首尾的空格
# print(new_str)
#
# str2="12a|b|c|d|e|fg21"
# newstr=str2.strip("12")# 去除括号内元素及其子集  此处为12，1，2
# print(newstr)
#
#
# num=str2.count("|") # 统计元素出现次数
# print(num)
#
# num=len(str2)# 计算长度
# print(num)
#
#
# str="hello" # 两种方式遍历str指定中的元素
# for x in str:
#     print(x)
#
# count=0
# while count<5:
#     print(str[count])
#     count+=1
#
#
# # 序列：指内容连续，有序，可以使用下标索引的一类数据容器 如列表 元组 字符串
# # 切片是序列的常用操作   [起始:终止:步长]
# tuple=(0,1,2,3,4,5,6)
# a=tuple[:] # 默认从最前方开始至末尾结束，步长为1,
# b=tuple[::-1]# 倒序从末尾开始
# print(a,b)
#
# str="0123456"
# c=str[3:1:-1]# 从下标为3的开始取到下表为1    倒序取出则步长一定为负数，相应的始末下标也要反过来
# print(c)
#
# str=("dcba,jihgfe,nmlk")
# a=str[::-1][5:10]# 此处为10则不包含j    终止若填入数字则不包含该下标所对应的元素
# b=str[5:11][::-1]
# c=str.split(",")[1][::-1]
# print(a)
# print(b)
# print(c)

# print(chr(65))#查询数字对应的阿斯克码表字符
# print(ord("A"))# 查询字符的阿斯克码值

#
#
# # 集合的定义   集合无序，没有重复元素，会自动去重
# # 定义集合字面量  {yuansu1,yuansu2,……}
# # 定义集合变量  a={1,2,3,……}
# # 定义空集合  a=set()
#
# a={1,2,3,3}
# a.add(4) # 添加元素
# print(a)
# a.remove(4)# 删除元素
# print(a)
# b=a.pop()# 因为集合元素没有顺序即没有下标所以只能随机取出一个元素
# print(b)
# print(a)# 取出的元素就不在里面了
# c=a.clear()# 清空集合里的元素
# print(c)
#
# a={1,2,3,4}
# b={3,4,5,6}
# c=a.difference(b)# 取出a和b的差集（a有但b没有的元素组成的集合）,不改变a,b集合
# print(c)
#
# a.difference_update(b)# 去除a内和b相同的元素，会改变集合a
# print(a)
#
# c=a.union(b) # 将ab组成一个新集合
# print(c)
#
# for x in c:# 集合的遍历
#     print(x)

# 字典的定义    字典字面量  {key:vulue,key:vulue,key:vulue,……}   字典的元素由键值对构成
# 字典变量 a={key:vulue,key:vulue,key:vulue,……}
# 定义空字典 a={}   a=dict()
a={"tom":99,"jack":88}# 字典的key和vulue可以是任何类型的数据但key不可为字典
b={"staffA":{
    "age":22,
    "level":3}
   ,"staffB":{
        "age":23,
        "level":3
    }}# 字典的嵌套
levelB=b["staffB"]["level"]=4# 字典数据的调用和改变
print(levelB)
levelC=b["staffC"]=4# 若调用的元素不存在则视为将对应的键值对加入字典
print(b)


dict={"1":2,"1":1,"2":3}# 数据重复时会有警告
print(dict)# 由输出结果可知重复key的vulue由最后一个key决定

delete=dict.pop("2")# 删除元素
print(delete)

dict.clear()# 清空字典
print(dict)


dict={"a":1,"b":2,"c":3}
keys=dict.keys()# 获取一个字典中全部的key并放入一个列表中
print(keys)


# 两种遍历方法
for key in keys:
    print(f"key{key}对应的vulue是{dict[key]}")


for key in dict:
    print(f"key{key}对应的vulue是{dict[key]}")

num=len(dict)# 计算长度
print(num)

list1=[1,2,3,4,6]
tuple1=(1,2,3,4,6)
str1="abcd5fg"
set1={1,2,3,4,6}
dict1={"a":1,"b":2,"c":3}
# 都可以用len求长度
a=max(list1)# 都可以用max求最大值，比较的是字符对应ASCII表值的大小# list tuple set中的比大小不能字符串和数字混搭
print(a)
# key
# kea
# 上面两个字符串的比较：第一位k相同，第二位相同，第三位y大于a则key大于kea，若两个不一样长则长的更大
print(f"是否key>kea,{"key">"kea"}")

# 容器转换类型 list()  tuple()  str()  set()
a=list(tuple1)
print(a)
b=list(dict1)# 注意：b中只会保留字典的key
print(b)
c=str(dict1)# 字典转字符串会保留全部
print(c)

# d=dict(c)# 其他类型转dict可能出错,这个没报错
# print(d)

# e=dict(a) 会报错
# print(e)

a=[6,5,4,3,1,2]
b=sorted(a)
print(b) #将容器中的数据按大小排序

c=sorted(a,reverse=True)# 倒序
print(c)




b=1
c=2
a=(a,b)
(b,c)=(c,b)#交换
print(b,c)
#first *others last=()


d="abc"
e="-".join(("a","b","c"))
print(type(e))
print("-".join(("a","b","c")))
print("-".join("abc"))
print("-".join(['a','b','c']))

stra="abc"
strb="def"
strc=stra+strb#连接
strd="abc"'def'
stre="abc"*2
print(strc,strd,stre)

print(len("abc def"))

print(stra.find("a"))#返回第一次出现时的下标
print(stre.count("a"))


k=("a","b","c")
strf="cba"
j=sorted(strf)
print(j)# 是列表类型
list0=list(enumerate(strf))# 查看序列的元素和对应下标
list1=list(enumerate(strf,start=1))# 查看序列的元素和对应下标 定义开始下标
print(list0,list1)

dict2={i:i*2 for i in range(1,10)}# 利用推导式创建
print(dict2)

dict3=(zip(["a","b","c"],[1,2,3]))
print(dict3)

dict4={}.fromkeys((1,2,3),'student')
print(dict4)

list2=[["a",10],["b",30],["c",20]]
dict5={k:v for k,v in list2}
print(dict5)

p=sorted(dict5.items(),key= lambda x:x[1],reverse=True)
print(p)
# dict6={['a','b','c']:"student"}# 错误的创建方法 必须确保键是不可变的 但是列表是可以修改的 就是可变的

o=dict4

q=dict5.get("a" ,__default="none")
print(q)



H=dict3.pop("a":10)