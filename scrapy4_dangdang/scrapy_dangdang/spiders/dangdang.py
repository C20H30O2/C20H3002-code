import scrapy
from scrapy4_dangdang.items import ScrapyDangdangItem# 这里报错不影响操作



class DangdangSpider(scrapy.Spider):# 案例：来爬取当当网青春文学书籍的图片 名称 价格等内容
    name = "dangdang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url='http://category.dangdang.com/pg'# 为了下载多页而设置的初始url
    page=1



    def parse(self, response):
        print('===========')# 测试
# pipeline 管道 用来下载数据
# items  用来定义数据结构   在本案例中pipeline和items中都要进行一定操作
#         src=response.xpath('//ul[@id="component_59"]/li//img/@src')
#         alt=response.xpath('//ul[@id="component_59"]/li//img/@alt')
#         price=response.xpath('//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()')
#         所有的selector对象都可以再次调用xpath方法
        li_list=response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:# 利用了路径相同的部分做成循环
            # print(li)# 测试
            src=li.xpath('.//img/@data-original').extract_first()# 千万要注意解析获取图片下载地址时 网站可能会使用懒加载 从而无法获得正常的图片地址 如果这里写.//img/@src 得到的图片地址会全部相同 就是因懒加载 所以观察后选取了别的路径解析
            # 上面修改为.//img/@data-original后第一本书的src返回为none 因为他没有@data-original
            if src:# 进行简单判断 如果src=none 则用alt路径获取
                src=src
            else:src=src=li.xpath('.//img/@alt').extract_first()

            name=li.xpath('.//img/@alt').extract_first()
            price=li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src,name,price)

            book=ScrapyDangdangItem(name=name,price=price,src=src)# 将路径传入item 注意要用这个对象需要导入import scrapyfrom scrapy4_dangdang.items import ScrapyDangdangItem

            # 获取一个book就将book交给pipeline
            yield book


# 如果要下载前十页的内容
# 每一页的业务逻辑都是一样的，所以只需要将执行的那个页的请求再次调用parse方法就可以了
# http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html第二页地址
# http://category.dangdang.com/cp01.01.02.00.00.00.html第一页
# 实际上http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html也是第一页


        if self.page<10:
            self.page+=1
            url=self.base_url+str(self.page)+'-cp01.01.02.00.00.00.html'

            # 怎么调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback就是你要执行的那个函数   注意不需要加（）  这里的.parse后就没加（）

            yield scrapy.Request(url=url,callback=self.parse)# 这里明显使用的是递归的方法