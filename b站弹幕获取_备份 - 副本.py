import urllib.request
import urllib.parse


import pandas as pd
import requests
from lxml import etree
from bs4 import BeautifulSoup

# from pandas import *
import chardet
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面




# def count_page(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
#     # 因为urlopen方法中不能储存字典 所以headers不能传递进去 此时就要请求对象的定制
#     # 请求对象的定制
#     request = urllib.request.Request(url=url,
#                                      headers=headers)  # 将url与本机ua合在一起放入request中  这里要用位置传参 不能只填url，headers因为url与headers在传入参数中的的位置并不是第一和第二位
#
#     response = urllib.request.urlopen(request)
#     # 获取响应得到的页面源码
#     content = response.read().decode('utf-8')  # read方法返回的是字节形式的二进制数据  源码中的中文会以其他形式呈现，所以需要解码以将二进制的数据转化为字符串以呈现中文
#     # .decode('编码的格式')  这一步为解码
#     # print(content)
#
#     tree = etree.HTML(content)
#     list = tree.xpath("//body//div[@class='vui_pagenation--btns']")
#     print(list)
# 经过以上尝试 发现无法通过返回的原码取得搜索的视频的页数 所以在下面采取了循环的方式通过改变url 遍历所有页码 直到内容不足一页 直接获取所有相关视频





url_original='https://search.bilibili.com/video?keyword='

search=input("输入想要搜索的视频内容:")# 经过测试发现输入为空时取得的videurl为空
search=urllib.parse.quote(search)


tids_list=['1','13','167','3','129','4','36','188','234','223','160','211','217','119','155','202','5','181','177','23','152','']
while True:
    print("输入搜索视频的分区:\n1--动画\n13--番剧\n167--国创\n3--音乐\n129--舞蹈\n4--游戏\n36--知识\n188--科技\n234运动\n223汽车\n160--生活\n211--美食\n217--动物圈\n119--鬼畜\n155--时尚\n202--资讯\n5--娱乐\n181--影视\n177--纪录片\n23--电影\n152--电视剧\n不输入则默认全部分区")
    tids_type=input(":")
    if tids_type in tids_list:
        break
    else:
        print("输入错误")
tids='&tids'+tids_type


order_list=['click','pubdate','dm','stow','']
while True:
    print("输入搜索的方式:\nclick--最多播放\npubdate--最新上传\ndm--最多弹幕\nstow--最多收藏\n不输入则默认按综合排序")
    order_type=input(":")
    if order_type in order_list:
        break
    else:
        print("输入错误")
order='&order='+order_type


duration_list=['1','2','3','4','']
while True:
    print("输入筛选方式:\n1--十分钟以下\n2--十分钟到三十分钟\n3--三十分钟到六十分钟\n4--六十分钟以上\n不输入则默认全部时长")
    duration_type=input(":")
    if duration_type in duration_list:
        break
    else:
        print("输入错误")
duration='&duration='+duration_type




# 模拟浏览器向服务器发送请求

url_start=url_original+search+'&from_source=webtop_search&spm_id_from=333.1007&search_source=5'+tids+order+duration
# https://search.bilibili.com/video?keyword=zc&tids4&order=click&page26&o750&duration=1&tids=1&page=3&o=60//参考


print("输入允许的页数的最大值\n(将从第一页开始获取视频数据，最大页数不超过此最大值)")
max=int(input())

page_num=1
sum_videourl_list=[]
sum_title_list=[]
while page_num<=max:
    url=url_start+'&page='+str(page_num)+'&o='+str((page_num-1)*30)


    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')


    tree=etree.HTML(content)

    # 取得视频url
    list=tree.xpath("//body//div[@class='video-list row']//a")

    content_list=[]
    for x in list:
        content_list.append(x.xpath("./@href"))

    videourl_list=[]
    i=0
    while i<=len(content_list)-1:
        videourl_list.append(content_list[i])
        i+=3


    # 取得视频标题
    list2=tree.xpath("//body//div[@class='video-list row']//h3")

    title_list=[]
    for x in list2:
        title_list.append(x.xpath("./@title"))



    # upper_list=[]
    # j=2
    # while j<=len(content_list)-1:
    #     upper_list.append(content_list[j])
    #     j+=3
    # if len(upper_list)>30:
    #     upper_list=upper_list[:30]
# 可以使用字典存储video和upper的信息 但这里重点只在统计弹幕 所以不再使用upper


    if len(videourl_list)>0:
        if(len(videourl_list)>30):
            videourl_list=videourl_list[:30]
            sum_videourl_list.append(videourl_list)

            title_list=title_list[:30]
            sum_title_list.append(title_list)

            page_num+=1
        else:
            sum_videourl_list.append(videourl_list)

            sum_title_list.append(title_list)

            page_num+=1
    else :
        break


real_page_num = page_num - 1



# 切片取得视频的BV号
sum_video_BVlist=[]
for page_video_list in sum_videourl_list:
    page_video_BVlist=[]
    for videourl in page_video_list:
        sum_video_BVlist.append(videourl[0][25:-1])



# 输出取得的视频页数 视频数量 方便使用者对弹幕提取进行进一步的条件限制
print(f"一共有{real_page_num}页视频\n完整的一页有30个视频")
if len(sum_video_BVlist) % 30!=0:
    print(f'其中最后一页有{len(sum_video_BVlist)}个视频')
else:
    print('这里所取的每一页都有30个视频')



# 通过BV号获取cid

while True:
    print("输入想要起始的页码")
    start_page=int(input(":"))
    print("输入要取弹幕的视频个数")
    number=int(input(":"))

    page_number=len(sum_video_BVlist[(start_page-1)*30:])
    if 0<=start_page<=real_page_num and 0<number<=page_number:
        break
    else:
        print("请正确输入")



base_get_cid_url="https://api.bilibili.com/x/player/pagelist?bvid="
# 参考 https://api.bilibili.com/x/player/pagelist?bvid=BV1e84y1T7jp  取cid的网站


real_cid_list = []
counts=1

aftercut_BVlist=sum_video_BVlist[(start_page-1)*30:]

for BVid in aftercut_BVlist:
    while number >= counts:
        get_cid_url=base_get_cid_url+BVid
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        request = urllib.request.Request(url=get_cid_url,headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')


        dict_content=eval(content)
        print(dict_content)
        cid_list=dict_content["data"]


        set_video_cid_list=[]
        if len(cid_list)>=1:# 说明由该BV号取到的视频是一个视频合集 里面有不同的视频 包含不同的弹幕
            for things in cid_list:
                set_video_cid_list.append(things["cid"])
            real_cid_list.append(set_video_cid_list)

        else:
            real_cid_list.append(cid_list["cid"])

        counts+=1

    if counts>number:
        break



for cids in real_cid_list:
    clist=[]
    if len(cids)!=1:
        for cid in cids:
            base_url='https://comment.bilibili.com/'
            get_comment_url=base_url+str(cid)+'.xml'

            # print(get_comment_url)

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}

            # request = urllib.request.Request(url=get_comment_url, headers=headers)
            # response = urllib.request.urlopen(request)

            # print(type((response)))
            # print(response)

            # content = response.read()

            response = requests.get(get_comment_url, headers=headers)

            # f = open("E:/comment_bili.py.csv", "w", encoding="UTF-8")
            # f.write(content)

            # result=chardet.detect(content)
            # encoding=result['encoding']
            # print(f"{encoding}")

            # 默认打开文件的编码格式是gbk 所以在打开文件时需要指定编码encoding='utf-8'
            soup = BeautifulSoup(response.content,'xml',from_encoding='utf-8')
            comment_s=soup.findAll('d')

            for comments in comment_s:
                comment=comments.get_text()
                clist.append([str(cid),comment])


            datas = pd.DataFrame(clist, columns=['视频cid', '弹幕内容'])
            datas.to_csv('bili_comments.csv', index=False)

            # print('abc',soup)  # 测试
            # print('def',comments)
            # print(content)

            # print(content)

    else:
        base_url = 'https://comment.bilibili.com/'
        get_comment_url = base_url + str(cids[0]) + '.xml'


        # print(get_comment_url)
        #
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}

        # request = urllib.request.Request(url=get_comment_url, headers=headers)
        #
        # response = urllib.request.urlopen(request)
        # content = response.read()

        response=requests.get(get_comment_url,headers=headers)


        # print(type(response))
        # print(response)



        # f = open("E:/comment_bili.py.csv", "w", encoding="UTF-8")
        # f.write(content)


        soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
        comment_s = soup.findAll('d')

        for comments in comment_s:
            comment = comments.get_text()
            clist.append([str(cids[0]), comment])


        datas=pd.DataFrame(clist,columns=['视频cid','弹幕内容'])
        datas.to_csv('bili_comments.csv',index=False)

        # print('456',comments)



        # result = chardet.detect(content)
        # encoding = result['encoding']
        # print(f"{encoding}")

        # print(content)


# b'\x94\xbdYs\\Iv&\xf8W`\xf9\xd4=\xcd\xbe\xf2s\x8e\x1f?\xeee\xd9\xd9&U\xcf\xc8z\xcc4\xf3\xd2z\x18\x8dM\x8f\xc5\x9aJIY)xff'