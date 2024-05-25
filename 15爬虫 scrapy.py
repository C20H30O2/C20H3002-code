# scrapy是在计算机领域的专业单词
# 用于爬取网站数据 提取结构性数据而编写的应用框架
# 数据挖掘 信息处理 存储历史数据
# 安装scrapy  最好用国内源 国外源太慢
# 使用cmd创建项目  先进入指定路径  输入scrapy startproject 项目名称（不能以数字开头，不能包含中文）
# 有了项目后创建爬虫文件 先跳转到项目内的spiders文件夹 再输入scrapy genspider 爬虫名字 网页的域名  例如scrapy genspider baidu www.baidu.com
# 详细内容转到左侧新建的scrapy_baidu_test项目中




# scrapy shell 调试爬虫代码
# 加入scrapy shell的终端 直接在cmd中输入scrapy shell就可以  不需要进入什么环境中
# 例如直接输入scrapy shell www.baidu.com
# 如果像看到一些高亮或者自动补全 可以安装ipython  pip install ipython
# response.body response.text response.url response.status这些是可以在调试过程中直接使用的方法
# response.xpath('//input[@id="su"]/@value')可以直接用xpath定位取得想要的数据

# a=response.xpath('//input[@id="su"]/@value')# 再输入这两句代码可以从返回的列表中获得  百度一下
# a.extract_first()

# 也可以用css语法来达成相同效果 bs4
# a=response.css('#su::attr("value")')
# a.extract_first()


# crawlspider 继承自 scrapy.spider
# crawlspider 可以定义规则 在解析html内容的时候 可以根据链接规则提取出指定的链接 然后再向这些；连接发送请求
# 所以如果有需要跟进连接的需求 也就是在爬取了网页之后 需要提取连接再次爬取 此时使用crawlspider是非常合适的

# 链接提取器 scrapy.linkextractors.LinkExtractor()
# allow=() # 填写正则表达式 提取符合规则的链接
# deny=()      # 括号内填写正则表达式  不提取符合规则的链接
# allow_domains=()   # 允许的域名
# deny_domains=()   # 不允许的域名
# restrict_xpath=()   # 提取符合xpath规则的链接
# restrict_css=()   # 提取符合选择器规则的链接


# 提取链接 link.extract_links(response)

# 例子 读书网获取链接示范
# 在cmd按顺序输入五行代码
# 1.scrapy shell https://www.dushu.com/book/1188.html
# 2.from scrapy.linkextractors import LinkExtractor
# 3.link=LinkExtractor(allow=r'/book/1188_\d+\.html')
# 4.link
# 5.link.extract_links(response)


# 后续的内容转到 左侧的新建的scrapy_crawlspider_dushu目录中
# 新建crawlspider项目与新建上面的scrapy项目有一点不同
# 使用cmd创建项目  先进入指定路径  输入scrapy startproject 项目名称（不能以数字开头，不能包含中文）
# 转到项目中的spiders文件夹中 再创建爬虫类  scrapy genspider -t crawl 爬虫名称 网页的域名