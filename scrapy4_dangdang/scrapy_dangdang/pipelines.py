# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道需要现在setting中开启管道


# # 开发中不推荐使用这种方法 因为每传过来一个对象就打开一次文件 对文件的操作过于频繁
# class ScrapyDangdangPipeline:
#
#     # item就是yield后面的book对象
#     def process_item(self, item, spider):
#
#         # write方法写入的必须是字符串
#         with open('book.json','a',encoding='utf-8')as fp:# 注意w模式每次打开文件会先清空 再写入所以这里要用a模式
#             fp.write(str(item))# item是一个对象 无法直接写入
#         return item



# 推荐的方法
class ScrapyDangdangPipeline:

    def open_spider(self, spider):# 在爬虫文件开始前运行的内容
        self.fp = open('book.json', "w", encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
        self.fp.close()# 在爬虫文件运行后的内容


# 什么的管道用于获取要下载的内容有关的json文件
# 可以开启多管道


import urllib.request

# 1.定义管道类
# 2.在settings中开启管道 "scrapy4_dangdang.pipelines.dangdang_dowmloadpipeline":301

class dangdang_dowmloadpipeline:
    def process_item(self, item, spider):

        url='http:'+item.get('src')# 发现item中的src没有http前缀 所以自行加上
        filename='./books/'+item.get('name')+'.jpg'

        urllib.request.urlretrieve(url=url,filename=filename)

        return item