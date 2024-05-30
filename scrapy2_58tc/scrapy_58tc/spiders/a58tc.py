import scrapy



class A58tcSpider(scrapy.Spider):
    name = "58tc"
    allowed_domains = ["hz.58.com"]
    start_urls = ["https://hz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]

    def parse(self, response):# 注意 可能会说访问频繁需要验证 可以在58tc网页点击验证
        print('测试看有没有反爬')# 如果没有运行成功一定要注意start_urls是否正确 保证网址不要出错
        content=response.text
        print('================')# 因为输出的想要的内容在一堆代码中间，用这一行来提示输出内容
        print(content)
        need=response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]# 括号里面直接写xpath语法定位想要的内容就行 不需要导入xpath
        # xpath返回列表 用[]选取列表内需要的内容
        print('================')
        print(need)
        print(need.extract())# 根据老师的说法二者的内容应该有不同 但是不知道为什么这里是一样的