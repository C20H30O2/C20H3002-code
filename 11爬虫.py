# 通过一个程序对网站的信息进行收集
# 爬虫核心：爬取网页获取全部内容  解析得到的数据
# 难点：爬虫与反爬虫之间的博弈
# 用途：数据分析，人工数据集     社交软件冷启动    舆情监控   竞争对手监控
# 分类：通用爬虫 例子：百度 360 google  有robots协议说明本网站有哪些内容不允许抓取，但是起不到限制作用  缺点：取得的数据大多数没有用，无法精准获取所需数据
#      聚焦爬虫  根据需求精准抓取数据  设计思路1：确定爬取网站   2：模拟浏览器通过http协议访问网站，获取服务器返回的html代码   3：解析html字符串
# 反爬手段 1.user-agent（ua）  2.代理ip  3.验证码访问   4.动态加载网页   5.数据加密
import urllib.request
import urllib.parse

# # urllib库的基本使用
# # from urllib import *
# # 使用urllib获取百度首页的源码
# # 定义一个url  即所要访问的地址
# url = 'http://www.baidu.com'
# # 模拟浏览器向服务器发送请求
# response=urllib.request.urlopen(url)
# # 获取响应得到的页面源码
# content=response.read().decode('utf-8')# read方法返回的是字节形式的二进制数据  源码中的中文会以其他形式呈现，所以需要解码以将二进制的数据转化为字符串以呈现中文
# # .decode('编码的格式')  这一步为解码


# content1=response.read()# 一个字节一个字节地读
# content2=response.read(5)# 返回多少个字节
# content3=response.readline()# 只读取一行
# content4=response.readlines()# 一行一行地读直到读完


# print(content)
# print(response.getcode())# 返回状态码，如果是200就证明逻辑没问题
# print(response.geturl())# 返回url地址
# print(response.getheaders)# 获取的是一些状态信息

# 以上是一个类型：HTTPResponse  六个方法：read readline readlines getcode geturl getheaders




# 爬虫下载


# # 下载网页
# url_page = 'http://www.baidu.com'
#
# urllib.request.urlretrieve(url_page,'baidu.html')# 括号内填入两个参数 分别是url filename
# # urllib.request.urlretrieve(url=url_page,filename='baidu.html')# 关键字赋值，结果一样
#
#
# # 下载图片
# url_image = "https://tse2-mm.cn.bing.net/th/id/OIP-C.ZmadAJVppYpCj6hiuJjaxAHaFB?rs=1&pid=ImgDetMain"
# urllib.request.urlretrieve(url_image,'zjcwn.jpg')

# 下载视频    注意视频地址地获取，地址一定要准确且能通过地址直接搜索到相关视频，这里的地址有问题没有下载成功
# url_video='blob:https://yhdmoe.com/a0582cd1-ae19-4b3a-9525-313909af545d'
# urllib.request.urlretrieve(url_video,'zjcwn01.mp4')# 若下载成功，得到MP4文件也无法在pycharm直接查看因为没有内置播放器
#                                                              需要在文件中找到查看




# 请求对象的控制
url='https://www.baidu.com'

# url的组成   分为六个
#   例子（在百度搜索周杰伦）：https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1&rsv_iqid=0xb3c44d34004156cf&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=z%2526%252339%253Bj%2526%252339%253Blun&rsp=0&inputT=5679&rsv_sug4=6952
# 协议  http/https  后者有ssl协议加密，其数据更加安全
# 主机  www.baidu.com
# 端口号   http  80    https  443    mysql  3306    oracle  1521    redis  6379    mongodb  27017
# 路径 s
# 参数 wd=%E5%91%A8%E6%9D%B0%E4%BC%A6   %E5%91%A8%E6%9D%B0%E4%BC%A6为unicode编码的周杰伦
# 锚点


# response=urllib.request.urlopen()
# content=response.read().decode('utf-8')
# print(content)# 输出内容中没有网页相关信息，因为遇上了反爬  这里是ua反爬
# # user agent 用户代理




# # 应对ua反爬

# 字典里的是从网页获取到的本机的ua
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # 因为urlopen方法中不能储存字典 所以headers不能传递进去 此时就要请求对象的定制
# # 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)




# 编解码

# 需求：获取 https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6 的网页源码
# url='https://www.baidu.com/s?wd=周杰伦'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# content=response.read().decode("utf-8")
# print(content)# 结果：url中填写的周杰伦是汉字导致报错



# get请求的quote方法
# 解决方法：将周杰伦变成unicode形式
# 需引入新的方法import urllib.parse写在了开头
# url='https://www.baidu.com/s?wd='
#
# name=urllib.parse.quote('周杰伦')
# print('name')# 验证转换结果
# url=url+name
# print(url)# 验证
#
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)


# get请求的urlencode方法 需要导入urllib.parse 应用场景：有多个参数的时候
# url='https://www.baidu.com/s?'
# data={
#     'wd':'周杰伦','sex':'男'
# }
# a=urllib.parse.urlencode(data)# data的类型需要为字典
# print(a)
# url=url+a
# print(url)
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)



# post请求
url='https://fanyi.baidu.com/mtpe-individual/multimodal?aldtype=16047&ext_channel=Aldtype'

data={
    'kw':'spider'
}

#post请求的参数一定要进行编码
# data=urllib.parse.urlencode(data)
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # post请求的参数是不会放在url的后面的，而是在request中将内容用位置传参传入data中
# request=urllib.request.Request(url=url,headers=headers,data=data)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)
# 报错TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
# post内容应为字节型数据而这里的data是字符串类型



# 修改后   这里因为url错误仍然没有得到想要的结果
# url='https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&rsv_spt=1&rsv_iqid=0xb6b2ffd600a22e49&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ih_0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsv_btype=i&rsp=0&rsv_sug9=es_2_1&rsv_sug4=960&rsv_sug=2'
# data={
#     'kw':'spider'
# }
# #post请求的参数一定要进行编码
# data=urllib.parse.urlencode(data).encode('utf-8')# 将data从字符串进行转化
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # post请求的参数是不会放在url的后面的，而是在request中将内容用位置传参传入data中
# request=urllib.request.Request(url=url,headers=headers,data=data)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)




# ajax的get请求
# 获取豆瓣电影第一页的数据并保存
# url="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)   # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
# response=urllib.request.urlopen(request)     # 将request放入urlopen中
# content=response.read().decode('utf-8')
# print(content)
# fp=open('douban.json','w',encoding='utf-8')# open方法默认情况下使用的是gbk的编码，如果需要保存汉字，需要在open方法中指定编码格式为utf-8
# fp.write(content)# 将内容保存到fp中   执行完成后会生成douban。json   这里的douban。json是用ctrl+alt+l处理过的，更加直观
#
# with open('douban.json','w',encoding='utf-8') as fp:
#     fp.write(content)# 与上面的方法作用一样，但是会自动关闭文件不会一直占用，上面最好手动关闭文件




# 爬取豆瓣电影前十页
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# start=0&limit=20表示从第一条开始限制一页20条
# start=20&limit=20表示从第二十一条开始显示20条
# def creat_request(page):
#     base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
#     data ={'start':(page-1)*20,'limit':20}
#     data=urllib.parse.urlencode(data)
#     url=base_url+data
#     headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
#     request = urllib.request.Request(url=url,headers=headers)  # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
#     return request
#
#
#
# def get_content(request):
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     return content
#
#
# def down_load(page,content):
#     with open('douban_'+str(page)+'.json','w',encoding='utf-8')as fp:
#         fp.write(content)
#
#
#
# if __name__=='__main__':
#     start_page=int(input('输入起始页码：'))
#     end_page=int(input('输入结束页码：'))
#     for page in range(start_page,end_page+1):
# # 定义一个方法使得每一页都有自己的请求对象的定制
#         request=creat_request(page)
# # 获取响应的数据
#         content=get_content(request)
# # 下载
#         down_load(page,content)






# ajax的post请求   在检查页面中的 request headers中看到 X-Requested-With:XMLHttpRequest 说明是ajax请求
# 案例：爬肯德基官网
url="https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
# 第一页的负载内容
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页的负载内容
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10



# def creat_request(page):
#     base_url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
#     data ={'cname': '北京',
#     'pid':'',
#     'pageIndex':page,
#     'pageSize':10}
#     data=urllib.parse.urlencode(data).encode('utf-8')
#     headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
#     request = urllib.request.Request(url=url,headers=headers,data=data)  # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
#     return request
#
#
# def get_content(request):
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     return content
#
#
# def down_load(page,content):
#     with open('kfc_'+str(page)+'.json','w',encoding='utf-8')as fp:
#         fp.write(content)
#
# base_url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# if __name__=='__main__':
#     start_page=int(input('输入起始页码：'))
#     end_page=int(input('输入结束页码：'))
#     for page in range(start_page, end_page + 1):
#         # 请求对象的定制
#         request=creat_request(page)
#         # 获取网页源码
#         content = get_content(request)
#         # 下载
#         down_load(page,content)




# 异常
# 两类异常urlerror    httperror
# httperror是urlerror的子类
# 导入的包：urllib.error
import urllib.error

#https://blog.csdn.net/D_31415926/article/details/137425619# 这个是正确url
# url = 'https://blog.csdn.net/D_31415926/article/details/1374256190'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# try:
#     request=urllib.request.Request(url=url,headers=headers)
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     print(content)
# except urllib.error.HTTPError as e:# 捕获httperror
#     print(e)


#https://blog.csdn.net/D_31415926/article/details/137425619# 这个是正确url
# url = 'https://blog.dsdn.com'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# try:
#     request=urllib.request.Request(url=url,headers=headers)
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     print(content)
# except urllib.error.URLError as e:# 捕获urlerror
#     print(e)





# urllib里的cookie登录   有些网站的信息要登陆后才能获取   适用场景：数据采集的时候需要绕过登录然后进入到某个页面
# 案例：微博cookie登录


# 个人信息界面是utf-8，但有可能报编码错误，因为并没有进入该界面，而是进入登陆界面，登陆界面经检查源代码后发现可能不是utf-8
# 无法访问成功一般是因为请求头的信息不够充分 这里为了成功登录获取信息，先在网页端登录后，查看登录成功后的检查页面的info项的请求头的信息，并排查到底是其中的哪一项起到关键作用，从而将其运用到代码的headers中以成功登录
#


# url='https://weibo.cn/7914637402/info'# 我的微博账号的个人详细资料页面
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# content=response.read().decode('utf-8')# 经检查微博的登陆界面仍然为utf-8，所以没有修改
# with open('weibo.html','w',encoding='utf-8') as fp:
#     fp.write(content)
# 这一段代码只停留在了登陆界面，所以获取和编写入文件的都是登录界面的代码



# 查看登录成功后的检查页面的info项的请求头的信息，将其处理为字典格式后复制到headers中，去除多余的项后发现cookie起主要作用
# url='https://weibo.cn/7914637402/info'# 我的微博账号的个人详细资料页面
# headers = {# cookie中携带着你的登录信息，如果有登录后的cookie 那么我们就可以带着cookie进入到任何页面
#     'Cookie':'_T_WM=3b0279cd300ccc86f368755279436f80; SCF=AlsqvW51TXgElnaulxtqZfkVquws8yU7XA2zLtjlboLz80_sb1ouUoUWw728xelZHyaJQyBGlIpVuTsJW6QWO2M.; SUB=_2A25LEg64DeRhGeFH6lYX8ynIyz6IHXVobg5wrDV6PUJbktANLUbdkW1Ne_0SF2eVUdBSAWxsIH50vTWSrDGrPqya; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYba.sdAny7EDEJsEVT2KM5NHD95QN1K2XSoeNSh5EWs4Dqcj6i--Xi-iWiKyhi--fiKy2iKnpi--Xi-zRiKn7i--Ni-2Ei-z0i--Xi-iWiK.Xi--NiKn0i-8si--4iKnfi-zR; SSOLoginState=1712750312; ALF=1715342312',
#     # referer去除后仍然可以成功登录，  这个referer起到防盗链的作用，会判断当前路径是不是由是一个路径进来的，如果不是就会报错 一般情况下会作为图片防盗链，是一种反爬手段
#     'Referer':'https://weibo.cn/',
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# content=response.read().decode('utf-8')
# with open('weibo_data.html','w',encoding='utf-8') as fp:
#     fp.write(content)




