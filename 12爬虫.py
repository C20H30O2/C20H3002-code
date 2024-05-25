import json
import urllib.request
import urllib.parse

import requests
# handler处理器
# urllib.request.urlopen(url) # 不能定制请求头
# urllib.request.Request(url,headers,data) # 可以定制请求头
# handler # 可以定制更高级的请求头（简单的请求对象的定制已经不能满足需求，动态cookie和代理不能使用请求对象的定制


# # handler处理器的基本使用
# # 需求：使用handler处理器访问百度，获取网页源码
# url='http://www.baidu.com'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# request=urllib.request.Request(url=url,headers=headers)
#
# # handler bulid_opener  open
# # 获取handler对象
# handler=urllib.request.HTTPHandler()
# # 获取opener对象
# opener=urllib.request.build_opener(handler)
# # 调用open方法
# response=opener.open(request)
#
# content=response.read().decode('utf-8')
# print(content)



# 代理服务器
# 作用举例：突破ip访问限制，访问外国站点   隐藏自己的ip免受攻击    提高访问速度等


# url='http://www.baidu.com/s?wd=ip'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)
# # 模拟浏览器访问服务器
# response=urllib.request.urlopen(request)
# # 获取响应信息
# content=response.read().decode('utf-8')
# # 保存
# with open('ip_自己的.html','w',encoding='utf-8') as fp:
#     fp.write(content)


# # 使用代理
# url='http://www.baidu.com/s?wd=ip'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)
# proxy={
#     'http':'114.231.108.102:8089'
# } # 得到一个代理ip   例如使用网站快代理 得到一个免费的代理IP   这里获取的免费ip效果不好，总是报错
#
# headler=urllib.request.ProxyHandler(proxies=proxy)# 在这里输入代理ip
# opener=urllib.request.build_opener(headler)
#
# # 模拟浏览器访问服务器
# response=opener.open(request)
# # 获取响应信息
# content=response.read().decode('utf-8')
# # 保存
# with open('ip_代理的.html','w',encoding='utf-8') as fp:
#     fp.write(content)
#


# # 简易代理池
# proxies_pool=[
#     {'http':'114.231.108.102:8089'},
#     {'http':'114.231.108.102:8090'}
# ]# 这里的ip是随便编的
# import random
#
# proxies=random.choice(proxies_pool)
# print(proxies)# 验证使用随机函数随机选择ip
#
# url='http://www.baidu.com/s?wd=ip'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
#
# # 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)
#
# headler=urllib.request.ProxyHandler(proxies=proxy)# 在这里输入随机出来的代理ip
# opener=urllib.request.build_opener(headler)
# # 模拟浏览器访问服务器
# response=opener.open(request)
# # 获取响应信息
# content=response.read().decode('utf-8')
#
# with open('ip_代理的.html','w',encoding='utf-8') as fp:
#     fp.write(content)
#




# 解析  从得到的网页源码中获取真正想要的数据


# xpath的使用
# xpath  使用前要先在浏览器的拓展中导入xpath.crx扩展程序  用于辅助检验路径是否正确
# 安装lxml库
from lxml import etree# 验证是否成功

# xpath解析  xpath的返回值是一个列表数据
# （1）解析本地文件   etree.parse
# （2）解析服务器响应的数据   即response.read().decode('utf-8')   etree.HTML()


# # 本地
tree=etree.parse('test_xpath_本地文件.html')
print(tree)
# tree.xpath('xpath路径')
# 查找ul下的li
# //为查找所有子孙节点，不考虑层级关系   /为查找直接子节点
li_list=tree.xpath('//body//ul/li')
li_list1=tree.xpath('//body//ul/li/text()')# text()可以显示内容
print(len(li_list1))# 结果为所有ul下的li个数之和
print(li_list)
print(li_list1)
#
#
# # 查找所有有id的属性的标签
# li_list=tree.xpath('//ul/li[@id]/text()')
# print(len(li_list))
# print(li_list)
#
# # 找到指定id的li标签
# li_list=tree.xpath('//ul/li[@id="l1"]/text()')# 注意单引号中引用字符串要用双引号
# print(li_list)
#
# # 查找到id为l1的li标签的clss属性值
# li_list=tree.xpath('//ul/li[@id="l1"]/@class')
# print(li_list)
#
#
# # 模糊查询
# li_list=tree.xpath('//ul/li[contains(@id,"c")]/text()')# 这里查询了id中包含c的内容
# print(li_list)
#
# li_list=tree.xpath('//ul/li[starts-with(@id,"c")]/text()')# 查询了以指定字符为开头的id对应的内容
# print(li_list)
#
# # 逻辑运算   实际使用较少
# # 查询id为l1和class为c1的内容
# li_list=tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# print(li_list)
#
#
# li_list=tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')# 查询id为l1或l2的内容的两种表示方法
# li_list1=tree.xpath('//ul/li[@id="l1" or @id="l2"]/text()')
# print(li_list)
# print(li_list1)


# # 解析百度网页源码获取’百度一下‘
# url='https://www.baidu.com/'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# # 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)
# # 模拟浏览器访问服务器
# response=urllib.request.urlopen(request)
# # 获取响应信息
# content=response.read().decode('utf-8')
# print(content)
# tree=etree.HTML(content)# 解析服务器响应的文件
# # 获取想要的数据
# # result=tree.xpath('//a [@id="aging-total-page"]/@aria-label') # 这个路径是正确的但是没有结果输出，可能是在源代码界面被隐藏
# result=tree.xpath('//link [@rel="search"]/@title')
# print(result)



# 运用解析在站长素材上获取图片  这里获取的是樱花图片
# https://sc.chinaz.com/tu/yinghua.html 第一页  https://sc.chinaz.com/tu/yinghua-1-0-0.html经过检验发现这个不是第一页的网址
# https://sc.chinaz.com/tu/yinghua-2-0-0.html 第二页
# def creat_request(page):
#     if page==1:
#         url='https://sc.chinaz.com/tu/yinghua.html'
#     else:
#         url='https://sc.chinaz.com/tu/yinghua-'+str(page)+"-0-0.html"
#     # print(url) 用于测试
#     headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
#     # 请求对象的定制
#     request=urllib.request.Request(url=url,headers=headers)
#     return request
#
# def get_content(request):
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     return content
#
# # 解析网页原码获取图片路径 找到图片并下载图片
# def down_load(content):
#     tree=etree.HTML(content)
#
#     src_list=tree.xpath('//div[@class="imgload"]//a/img/@data-src')
#     name_list=tree.xpath('//div[@class="imgload"]//a/img/@alt')
#     print(len(src_list),len(name_list))
#     for x in range(len(name_list)):
#         name=name_list[x]
#         src=src_list[x]
#         # print(name,src)# 测试 发现只有src不完整
#         url='https:'+src# 注意要通过这一步获得完整的url
#         url1=url.replace('\\','/')
#         print(name,url1)# 测试
#         urllib.request.urlretrieve(url=url,filename=name+'.jpg')# 以jpg格式保存到指定目录中
#
# if __name__=='__main__':
#     start_page=int(input('输入起始页码：'))
#     end_page=int(input('输入结束页码：'))
#     for page in range(start_page, end_page + 1):
#         # 请求对象的定制
#         request=creat_request(page)
#         # 获取网页源码
#         content = get_content(request)
#         # 下载
#         down_load(content)



# # 下载图片
# url_image = "https://scpic1.chinaz.net/Files/picpic9/201901/bpic10263_s_w285.jpg"
# urllib.request.urlretrieve(url_image,'zjcwn.jpg')



# # jsonpath
# import json
# import jsonpath
# obj=json.load(open('爬虫-jsonpath-test.json','r',encoding='utf-8'))
# #  获取所有书的作者
# author_list=jsonpath.jsonpath(obj,"$.store.book[*].author")# 获取所有作者
# author1=jsonpath.jsonpath(obj,"$.store.book[0].author")# 获取第一本书的作者
# print(author_list)
# print(author1)
#
# # 获取所有物品的作者
# author=jsonpath.jsonpath(obj,'$..author')
# # author2=jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author)
#
# # store下的所有元素
# tag_list=jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)
#
# # store下的所有价格
# price_list=jsonpath.jsonpath(obj,"$.store..price")
# print(price_list)
#
# # 第二本书的信息
# book2=jsonpath.jsonpath(obj,"$..book[1]")
# print(book2)
#
# # 最后一本书的信息
# book_last=jsonpath.jsonpath(obj,"$..book[(@.length-1)]")
# print(book_last)
#
# # 前两本书的信息
# book12=jsonpath.jsonpath(obj,"$..book[0,1]")# 方法一
# book12_2=jsonpath.jsonpath(obj,"$..book[:2]")# 方法二
# print(book12)
# print(book12_2)
#
#
# # 条件过滤需要在（）前加上？ 而不是像取最后一本书的信息一样
# # 过滤出包含isbn信息的书
# book_isdn=jsonpath.jsonpath(obj,"$..book[?(@.isbn)]")
# print(book_isdn)
#
#
# # 找出价格超过15的书
# book_list=jsonpath.jsonpath(obj,"$..book[?(@price>15)]")
# print(book_list)



# # 用jsonpath解析淘票票https://dianying.taobao.com/
# url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1713096796345_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
# # 直接搜索url发现没有数据，说明可能需要定制请求对象  因为不知道是那个起作用所以先复制了全部
# # 然后先屏蔽了所有以冒号开头的请求头因为以冒号开头一般是没有用的
# headers={# ':authority':'dianying.taobao.com',
# # ':method':'GET',
# # ':path':'/cityAction.json?activityId&_ksTS=1713096796345_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
# # ':scheme':'https',
# 'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# # 'Accept-Encoding':'gzip, deflate, br, zstd',# 这一行说明对编码类型的支持  可能会导致报错 所以要屏蔽掉
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Bx-V':'2.5.11',
# 'Cookie':'t=fe8ef13ff8fd6558bc51d7ed50fe29b6; cookie2=193d27e580957297f9ab799d03d24100; v=0; _tb_token_=e17b3b38ee7e1; cna=bLWiHipvMkkBASQJiiioWkbR; xlly_s=1; isg=BDQ0Z1137nyCfXqwue6mxx0ZBfKmDVj3YvkE_M6VUr9COdSD9h3kh6f_uXHhwZBP',
# 'Referer':'https://dianying.taobao.com/',
# 'Sec-Ch-Ua':'"Google Chrome";v="123", "Not A;Brand";v="8", "Chromium";v="123"',
# 'Sec-Ch-Ua-Mobile':'?0',
# 'Sec-Ch-Ua-Platform':'"Windows"',
# 'Sec-Fetch-Dest':'empty',
# 'Sec-Fetch-Mode':'cors',
# 'Sec-Fetch-Site':'same-origin',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
# 'X-Requested-With':'XMLHttpRequest'}
#
# request=urllib.request.Request(url=url,headers=headers)
#
# response=urllib.request.urlopen(request)
#
# content=response.read().decode('utf-8')
#
# # print(content)# 可以将得到的一大串json字符复制到json.cn 方便看清结构
# content=content.split("(")# 要去除原content内容开头和结尾的部分内容才真正得到一个json
# content=content[1].split(")")# 切除结尾的部分内容
# content=content[0]# 得到想要的json数据
# # 因为jsonpath只能解析本地文件，所以要存入本地文件
# with open('jsonpath解析——淘票票.json','w',encoding='utf-8')as fp:
#     fp.write(content)# 得到的原本地json文件只有很长的一行，要按ctrl+alt+l进行排版才能看得清楚结构
# # 本案例中要求获取reignName中的全部内容
# obj=json.load(open('jsonpath解析——淘票票.json','r',encoding='utf-8'))
#
# city_list=jsonpath.jsonpath(obj,"$..regionName")
# print(city_list)