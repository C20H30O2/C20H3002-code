from typing import Iterable, Any

import scrapy
from scrapy import Request
from scrapy.http import Response
import json

class BaidupostSpider(scrapy.Spider):
    name = "baidupost"
    allowed_domains = ["fanyi.baidu.com"]
    # post请求如果没有参数 那么这个请求将没有任何意义
    # 所以这个start_url就没有用了
    # parse方法也没用了
    # 因为与post请求无关 所以屏蔽掉了这两个

    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):# post请求就使用scrapy提供的start_requests
        url='https://fanyi.baidu.com/sug'

        data={
            'kw':'final' # 检查 network 在sug的payload项目中发现要传入的参数是kw
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)# 用callback进入下一个函数
        # .FormRequest是用于post请求的

    def parse_second(self,response):# response是上面的返回值

        content=response.text
        obj=json.loads(content)# 老师在这里还加了encoding='utf-8' 经过测试发现这里如果加了反而会报错
        print(obj)# 不进行转化 直接输出content 输出的内容就是一堆编码 不是文字