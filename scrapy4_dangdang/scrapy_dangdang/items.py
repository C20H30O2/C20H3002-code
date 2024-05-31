# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdangItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通俗地说就是你要下载地数据都有什么



    # 需要下载的内容
    # 图片
    src=scrapy.Field()
    # 名字
    name=scrapy.Field()
    # 价格
    price=scrapy.Field()
    pass
