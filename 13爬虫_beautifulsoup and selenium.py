# 简称bs4  和lxml一样是一个html解析器 主要功能也是解析和提取数据
# 缺点：效率没有lxml高   优点：接口人性化，使用方便
# 需要安装bs4  pip install bs4
import urllib.request

from bs4 import BeautifulSoup

#通过解析本地文件来讲解

# 默认打开文件的编码格式是gbk 所以在打开文件时需要指定编码encoding='utf-8'
soup=BeautifulSoup(open('爬虫——bs4——test.html',encoding='utf-8'),'lxml')
print(soup)# 测试

# 根据标签名字来查找结点  注意找到的是第一个符合条件的数据
print(soup.a)
print(soup.a.attrs)  # attrs获取标签的属性和属性值

# bs4的一些函数
# （1）find  （2）fing_all  (3)select
print(soup.find('a'))# 返回第一个符号条件的数据
print(soup.find('a',title="a2"))# 取title为a2的标签
# print(soup.find('a',class='a1'))# 会报错  不能用直接用class定位 因为class是保留字
print(soup.find('a',class_='a1'))# 这样才能用


print(soup.find_all('a'))# 返回一个列表 里面有所有的a标签
print(soup.find_all(['a','span']))# 获取列表内的所有标签的数据
print(soup.find_all('li',limit=2))# limit获取前几个数据


print(soup.select('a'))# select返回一个列表 包含满足条件的所有数据
print(soup.select('.a1'))# 利用select查找对应class的数据的格式'.class名'  这种操作叫做类选择器
print(soup.select('#l1'))# 查找对应id


# 属性选择器--通过属性来寻找对应的标签
# 查找到li中有id的标签
print(soup.select('li[id]'))

# 查找li标签中id为l2的标签
print(soup.select('li[id="l2"]'))


# 层级选择器
# (1)后代选择器
# 找到div下的li
print(soup.select('div li'))

# (2)子代(某标签的第一级子标签)选择器
print(soup.select('div > ul > li'))# 如果>两边不加空格 在很多计算机编程语言中会没有输出内容  但是在bs4中内容正常输出

# 找到a标签和li标签的所有对象
print(soup.select('a,li'))


# 节点信息
# 获取节点内容
obj=soup.select('#d1')[0]# 注意select返回的是一个列表
print(obj)
print(obj.string)# 通过打印obj发现obj是以个满足条件的完整标签  标签对象中除了内容还有标签，string可能就获取不到内容
print(obj.get_text())# 所有一般使用这个更好


# 节点的属性
obj=soup.select('#p1')[0]
# name是标签的名字
print(obj.name)
# 将属性值作为一个字典返回
print(obj.attrs)



# 获取节点的属性  三种方式
obj=soup.select('#p1')[0]
print(obj.attrs.get('class'))# 因为obj.attrs是一个字典，所以可以用.get获取指定key对应的value
print(obj.get('class'))
print(obj['class'])


# # 获取星巴克信息https://www.starbucks.com.cn/menu/
# url='https://www.starbucks.com.cn/menu/'
# response=urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# # print(content)#检验
# soup=BeautifulSoup(content,'lxml')
# 由于xbk网页更改已经无法按照网课内容爬取数据 所以跳过



# selenium  是一个用于web应用程序测试的工具
# 测试直接运行在浏览器中就像真正的用户在操作一样，能更大概率获取数据
# 支持通过各种driver驱动真实浏览器完成测试    也支持无界面浏览器操作
# 速度较慢
# 安装

# url='https://jd.com/'
# response=urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# print(content)# ctrl+f查询发现没有返回关于秒杀商品的内容  因为被检测到这里是模拟浏览器访问  selenium可以避开这一点


# # 基本使用
# # 导入
from selenium import webdriver
# # 创建浏览器操作对象
#
# browser=webdriver.Chrome()
# # 访问网站
# url='https://jd.com'
# browser.get(url)
# content=browser.page_source
# print(content)# 获取到了秒杀相关的内容


# selenium的元素定位  元素定位：自动化要做的就是模拟鼠标和键盘来操作这些元素，点击，输入等，操作这些元素首先要找到它们，webdriver提供了很多定位元素的方法
# browser=webdriver.Chrome()
# url='https://www.baidu.com'
# browser.get(url)
# 元素定位

# # 根据id找到对象
# button=browser.find_element_by_id('su')# 低版本的语法
# # 高版本selenium语法 button=browser.find_element(by=By.ID,value="su")   在高版本中，这里展示的各种语法都被整合到了这种写法中
# print(button)
#
# # 根据标签属性的属性值获取对象
# button=browser.find_element_by_name('wd')
# print(button)
#
# # 根据xpath来获取对象
# button=browser.find_elements_by_xpath('//input[@id="kw"]')
# button1=browser.find_element_by_xpath('//input[@id="kw"]')
# print(button)# 带s的结果会被放入列表中
# print(button1)
#
# # 根据标签的名字来获取对象
# button=browser.find_elements_by_tag_name('input')
# print(button)# 页面中有多个input标签
#
# button=browser.find_elements_by_css_selector('#su')# 用bs4中的语法来获取对象
# print(button)
#
# button=browser.find_elements_by_link_text('新闻')# 获取页面中的链接信息
# print(button)



# 元素信息以及交互
# browser=webdriver.Chrome()
# url='https://www.baidu.com'
# browser.get(url)
#
# input=browser.find_element_by_id('su')# 获取id为su的标签
# print(input)
# print(input.get_attribute('class'))# 输出获取到的标签的class值
# print(input.tag_name)# 打印标签名
# print(input.text)# 获取元素文本 打印出指定标签的><中间的内容  例如<a>zhangsan</a>  输出zhangsan



# # 交互   可以模拟实现人浏览网页 获取信息的功能
# browser=webdriver.Chrome()
# url='https://www.baidu.com'
# browser.get(url)
#
# import time# 睡眠两秒
# time.sleep(2)
#
# # 获取文本框的对象
# # <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off"> 在检查界面点击百度搜索的文本框会跳到这一行
# input=browser.find_element_by_id('kw')# 获取kw对象再输入值 以实现输入搜索内容的步骤
# # 在文本框中输入周杰伦
# input.send_keys('周杰伦')
# time.sleep(2)
#
# # 获取百度一下的按钮  在检查界面点击百度一下的按钮会跳到这一行
# button=browser.find_element_by_id('su')
# # 点击按钮
# button.click()
#
# time.sleep(2)# 为了让演示效果更清楚 多次进行了两秒钟的休眠
#
#
# # 在跳出的界面滑到底部 再点击下一页
# js_bottom='document.documentElement.scrollTop=100000'# 设置划到距离顶部100000距离的脚本
# browser.execute_script(js_bottom)# 引用脚本，执行脚本的任务  在一些情况下写browser.execute_script(
# # browser.execute_script("window.scrollBy(0,100000)")# 直接这样写也行
# time.sleep(2)
#
# # 定位下一页的按钮
# next=browser.find_element_by_xpath('//a[@class="n"]')
# # 点击
# next.click()
# time.sleep(2)# 记得要休眠一会 测试时发现如果没有这一行就不会执行返回和回去的指令
#
#
# # 控制返回上一页
# browser.back()
# time.sleep(2)
#
# # 回去
# browser.forward()
# time.sleep(3)
#
# browser.quit()# 退出



# phantomjs 是一个无界面浏览器
# 不进行css和gui渲染，速度比正常浏览器快很多 但这个几乎已经被淘汰


# chrome handless 谷歌浏览器的一种模式 可以在不打开ui的情况下使用浏览器



