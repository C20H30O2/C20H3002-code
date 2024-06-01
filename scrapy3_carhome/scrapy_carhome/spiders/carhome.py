import scrapy


class CarhomeSpider(scrapy.Spider):
    name = "carhome"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_15"]

    def parse(self, response):
        print('==============')# 测试
        name_list=response.xpath('//div[@class="tw-mt-1 tw-px-4"]/a/text()')
        price_list=response.xpath('//div[@class="tw-mt-1 tw-px-4"]/p/text()')
        print(name_list)# 返回一个selector列表
        for i in range(len(name_list)):
            name=name_list[i].extract()
            price=price_list[i].extract()
            print(name,price)
