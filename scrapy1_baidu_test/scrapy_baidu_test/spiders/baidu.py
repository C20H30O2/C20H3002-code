import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 一般用于运行爬虫的时候使用的值
    name = "baidu"
    # 运行访问的域名  不允许其他域名的访问
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址 指第一次要访问的域名
    # start_urls 是在allowed_domains的前面添加一个http
    start_urls = ["http://www.baidu.com"]

    # 是执行了起始url之后执行的方法    方法中的response就是返回的那个对象
    def parse(self, response):
        print('jack')
# 直接在cmd运行该爬虫会被反爬 运行界面提示DEBUG: Forbidden by robots.txt: <GET http://www.baidu.com>
# 可以搜索robot.txt   这是一个反爬的君子协议
# Obey robots.txt rules  可以在settings.py里找到左侧这两行 将下面一行屏蔽就可以不遵守该协议
# ROBOTSTXT_OBEY = True