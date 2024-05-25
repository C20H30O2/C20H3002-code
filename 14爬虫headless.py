# phantomjs 是一个无界面浏览器
# 不进行css和gui渲染，速度比正常浏览器快很多 但这个几乎已经被淘汰


# chrome handless 谷歌浏览器的一种模式 可以在不打开ui的情况下使用浏览器


# 一直到第二十行都是基本的配置  使用时唯一要注意修改的是path 一定要指向chrome。exe
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options=Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')# 在新版本中这一行可以不要
#
# # path是自己的chrome。exe的位置
# path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location=path
#
# browser=webdriver.Chrome(chrome_options=chrome_options)
#
# url='https://www.baidu.com'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.jpg')# 截图 因为不显示浏览器界面 所以靠截图来验证 将界面截图并保存为baidu。jpg


# 封装的headless  之后要使用可以直接复制
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# def share_browser():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     # path是自己的chrome。exe的位置
#     path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
#     chrome_options.binary_location = path
#     browser = webdriver.Chrome(chrome_options=chrome_options)
#     return browser
#
# browser=share_browser()# 测试封装
# url='https://www.baidu.com'
# browser.get(url)
# browser.save_screenshot('baidu2.jpg')


# request
# 基本使用：官方文档：http://cn.python-request.org/zh_CN/latest/
# 快速上手：http://cn.python-request.org/zh_CN/latest/user/quickstart.html
# 安装 pip install requests

import requests
# url='http://www.baidu.com'
# response=requests.get(url=url)
#
# # 一个类型，六个属性
# print(type(response))# <class 'requests.models.Response'>
#
# # 设置响应的编码格式
# response.encoding='utf-8'# 如果不设置获取的text可能会有乱码
# # 以字符串的形式返回了网页的源码
# print(response.text)
#
# # 返回一个url地址
# print(response.url)
#
# # 返回的是二进制的数据
# print(response.content)# 返回的内容以b开头 代表这是一个二进制字符串
#
# print(response.status_code)# 返回响应的状态码 200代表正常
#
# # 获取响应头的信息
# print(response.headers)


# 对比

# urllib
#1.一个类型 六个方法
#2.get请求
#3，post请求   百度翻译
#4.ajax的get请求
#5.ajax的post请求
#6.cookie登录 微博
#7.代理


#requests
#1.一个类型 六个属性
#2.get请求
#3.post请求
#4.代理
#5.cookie   破解验证码


# requests的get请求
# url='https://www.baidu.com/s?'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# data={'wd':'北京'}
#
# # url 请求资源路径
# # params 参数
# # kwargs 字典
# response =requests.get(url=url,params=data,headers=headers)# 参数使用params接收
# content=response.text
# print(content)
# # 输出内容无乱码  说明不需要urlencode编码
# # 不需要请求对象的定制
# # 请求资源路径中的？可以不加   即直接写https://www.baidu.com/s
#
#
#
# # request的post请求
# # 爬取百度翻译
# url="https://fanyi.baidu.com/sug"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
# data={'kw':'eye'}
#
# # url请求地址
# # data请求参数
# # kwargs字典
# response = requests.post(url=url,data=data,headers=headers)# requests
# content=response.text
# print(content)# 返回的内容是一串编码
#
# import json
# obj=json.loads(content)# 将编码转换
# print(obj)
# #post不需要编解码
# #post请求的参数是data
# #不需要请求对象的定制





#requests代理  https://www.baidu.com/s?ie=UTF-8&wd=ip查看ip
# url="https://www.baidu.com/s?ie=UTF-8&"
# headers={
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 'Accept-Encoding':'gzip, deflate, br, zstd',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Cache-Control':'max-age=0',
# 'cookie':'BDUSS=Hc4b2Nlc3MzczNYaWFhUVI2R3QyUTVZMy1jdFFsMWVmUkgyb05YRGxUVmctVUZtSVFBQUFBJCQAAAAAAAAAAAEAAAAe1H6NzcPJvdPwwfdfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBsGmZgbBpmW; BDUSS_BFESS=Hc4b2Nlc3MzczNYaWFhUVI2R3QyUTVZMy1jdFFsMWVmUkgyb05YRGxUVmctVUZtSVFBQUFBJCQAAAAAAAAAAAEAAAAe1H6NzcPJvdPwwfdfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBsGmZgbBpmW; BIDUPSID=37C9091F9D73C6BACC9DE96BF38D190F; PSTM=1713008006; BD_UPN=12314753; BAIDUID=5361CFB30DC3BECF60FFDA6960510225:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=5361CFB30DC3BECF60FFDA6960510225:FG=1; BA_HECTOR=840104a08l2ga42lal2121a141672d1j21dmk1s; ZFY=iSbVAakHUqaQ22Mw3SAH4NdCSyO:ACy4N9bVSQDTZwsk:C; B64_BOT=1; channel=baidusearch; H_PS_PSSID=40298_40369_40374_40481_40511_60024_60030_60048_60120_40080; delPer=1; BD_CK_SAM=1; PSINO=3; sugstore=1; H_PS_645EC=41229EifVLjqMONXjL41WeDR91LJz1gHxszqj7tFDiBZt5197a%2BW2nWAowc; baikeVisitId=7c8b19a3-d58d-4554-8230-8a7d89478071; COOKIE_SESSION=243749_0_4_2_10_17_1_3_3_3_3_1_3107_0_0_0_1713176120_0_1713419867%7C7%230_0_1713420645%7C1%7C1; BDSVRTM=0; ab_sr=1.0.1_N2JkY2IwM2RkNzUyNzlhNDlhZWQ3YzY3YTU4YTk4YTY4MDFjNjU1NGE2Y2ZkZjBlNTBjNmE5OTU5MTkzMzg1ZjY4Y2RkNzAyYTFhZDUxYWVmYjJkZmNjNDAxNWZjMDFiYjc3NTdkY2NmYzFkYWYxZTZkY2MxMmE2MjBmZDBkMjBjNDc2N2ExNzA3YWQ3MDliNzQzZjRiZWFmZWY2MjBhYjc0MjE4M2Y3Mzc4YjYyNjRmOTZlMTJiNmZiNjczYmQ4YmUxMDI1MDBmZjUzNjgzMjBjZjFiNTE5NGVmOTkzNjY1NGFjZTE4NTBkZWE2Nzc1ODkwODFmNDQ1OTEyMGI3NQ==; RT="z=1&dm=baidu.com&si=da2b575c-86b8-48af-8dc6-628975ee51f6&ss=lv4ufq1q&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=i25&hd=i2l"',
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
#          }
# data={'wd':'ip'}
# response=requests.get(url=url,data=data,headers=headers)
# content=response.text
# with open('daili.html','w',encoding='utf-8')as fp:
#     fp.write(content)
# 不知道怎么回事得访问不到ip的页面，只停留在了搜索框 除了原有的ua还添加量其他的header还是没用


# 使用代理ip
# url="https://www.baidu.com/s?ie=UTF-8&"
# headers={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
#          }
# data={'wd':'ip'}
# proxy={'http':'111,111,111,11:1111'}# 随意编写的ip  可以到代理网站获取代理ip
# response=requests.get(url=url,data=data,headers=headers,proxies=proxy)
# content=response.text
# with open('daili.html','w',encoding='utf-8')as fp:
#     fp.write(content)




# requests cookie 登录古诗文网   登录界面https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx
# 目标：要通过验证登录进入到主页面

# 通过检查登录界面发现登录需要的参数有很多   下面的内容在network的login.aspx的payload处
# __VIEWSTATE: gRPRfaO7NJ4KkysYlCiYFn/d6O5V8t1Ns4OXIKWU8+Dm39BJuc0+cw3g3RP4XYnIMEcNdqID0Yiae1Iwz9UT6tfV3EK4R6H94Zqs+XQraVniVKozW1OuT3+8rZKqszmHvKVasB6tLIOGox7HHqzINaKD0ZE=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 19884192844
# pwd: 123456789
# code: OB6M
# denglu: 登录

# __VIEWSTATEGENERATOR  __VIEWSTATE这两项不认识
# 观察到以上内容的__VIEWSTATEGENERATOR  __VIEWSTATE  code是变化的

# 难点1.对__VIEWSTATEGENERATOR  __VIEWSTATE着两项的处理  一般情况下看不到 不认识的项都在页面源码中 可以试着到源码中查找
# 2.code验证码

# 在登录界面选择查看页面源代码 ctrl+f输入可以进行查找
# <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="C93BE1AE" />
# 此为查找__VIEWSTATEGENERATOR的结果  里面有hidden 被称为隐藏域 在页面中存在 但是不显示
# 由于我们现在知道__VIEWSTATEGENERATOR  __VIEWSTATE存在与源码中
# 我们就可以通过获取页面源码来解析出这两个数据的值 再把值赋给这两项
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
          }
response=requests.get(url=url,headers=headers)
content=response.text
# print(content)# 测试 在返回的内容中搜索__VIEWSTATEGENERATOR 和 __VIEWSTATE有对应项说明没有问题

# 解析源码 获取对应的值  这里为了熟练bs4 所以用的bs4
from bs4 import BeautifulSoup
soup=BeautifulSoup(content,'lxml')
# 获取__VIEWSTATE的value
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
#获取__VIEWSTATEGENERATOR
viewstategenerator=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate,viewstategenerator)# 测试

# 通过检查定位到验证码图片
# <img id="imgCode" style="cursor: pointer; float:left; margin-left:5px; margin-top:1px;" width="60" height="27" src="/RandCode.ashx" onclick="GetCodeImg()" alt="看不清，换一张">
# 需要获取到验证码图片
code=soup.select('#imgCode')[0].attrs.get('src')
print(code)# 测试
# 得到的验证码的地址是不完全的 发现真正定位到图片的完整地址https://so.gushiwen.cn/RandCode.ashx
code_url='https://so.gushiwen.cn'+code

# # 获取了验证码的图片后下载到本地 然后自己输入  还可以用更高级的方法自动识别验证码
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# code_name=input('输入验证码：')
#
#
# # 通过输入错误密码防止页面跳转 获取登录接口
# url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
# data_post={'__VIEWSTATE':viewstate,
# '__VIEWSTATEGENERATOR':viewstategenerator,
# 'from: http':'//so.gushiwen.cn/user/collect.aspx',
# 'email':' 19884192844',
# 'pwd':' 123456789abc',
# 'code':'',
# 'denglu':' 登录'}
# response_post=requests.post(url=url,headers=headers,data=data_post)
# content_post=response_post.text
# with open('gushiwen.html','w',encoding='utf-8')as fp:
#     fp.write(content_post)



# 点入gushiwen.html后提示验证码错误
# 因为用urllib发送请求获取验证码图片和用requests登录 二者不是同一个请求 验证码是不一样的
# 我们需要让其保持一致
# 以下是从下载图片开始修改的正确代码



# requests里有一个方法session（）  通过session的返回值 就能使请求变成一个对象
session = requests.session()
response_code=session.get(code_url)# 验证码的url的内容
content_code=response_code.content# 注意这里不能用text，因为图片的下载要用二进制 所以用content 使其保持二进制
with open('code.jpg','wb',)as fp:# 这里wb的模式就是将二进制数据写入到文件
    fp.write(content_code)# 下载的图片可能没有那么快在pycharm上显示 可以直接在本地pycharm文件夹中查看
code_name=input('输入验证码：')

url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post={'__VIEWSTATE':viewstate,
'__VIEWSTATEGENERATOR':viewstategenerator,
'from: http':'//so.gushiwen.cn/user/collect.aspx',
'email':' 19884192844',
'pwd':' 123456789abc',
'code':code_name,
'denglu':' 登录'}
response_post=session.post(url=url,headers=headers,data=data_post)# 这里要将requests.post 换成session.post 用session发送请求 统一用session保持同一对象
content_post=response_post.text                                                                                    # 这样就是同一个请求了
with open('gushiwen.html','w',encoding='utf-8')as fp:
    fp.write(content_post)

# 总结：难点1.隐藏域wt
# 2.验证码

# 可以使用超级鹰之类的打码平台来自动识别验证码 省去手动输入

