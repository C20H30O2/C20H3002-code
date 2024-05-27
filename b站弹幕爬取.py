import urllib.request
import urllib.parse
import requests
from lxml import etree
from bs4 import BeautifulSoup
import csv

#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面
#记住最好将部分功能封装到函数里面





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

while True:
    try:
        print("输入允许的页数的最大值\n(将从第一页开始获取视频数据，最大页数不超过此最大值)")
        max=int(input())
        if max>0:
            break
        else:
            print("请正确输入")

    except:
        print("请正确输入")

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




# # test1
# print(sum_videourl_list)
# print(sum_title_list)





# 切片取得视频的BV号
sum_video_BVlist=[]
for page_video_list in sum_videourl_list:
    for videourl in page_video_list:
        sum_video_BVlist.append(videourl[0][25:-1])

sum_video_titlelist=[]
for page_title_list in sum_title_list:
    for single_title in page_title_list:
        sum_video_titlelist.append(single_title)




# # test2
# print(sum_video_BVlist)
# print(len(sum_video_BVlist))
# print(sum_video_titlelist)
# print(len(sum_video_titlelist))




# 输出取得的视频页数 视频数量 方便使用者对弹幕提取进行进一步的条件限制
print(f"一共有{real_page_num}页视频\n完整的一页有30个视频")
if len(sum_video_BVlist) % 30!=0:
    print(f'其中最后一页有{len(sum_video_BVlist)%30}个视频')
else:
    print('这里所取的每一页都有30个视频')



# 通过BV号获取cid

while True:
    try:
        print("输入想要起始的页码")
        start_page=int(input(":"))
        print("输入要取弹幕的视频个数")
        number=int(input(":"))

        page_number=len(sum_video_BVlist[(start_page-1)*30:])
        if 0<=start_page<=real_page_num and 0<number<=page_number:
            break
        else:
            print("请正确输入")
    except:
        print("请正确输入")



base_get_cid_url="https://api.bilibili.com/x/player/pagelist?bvid="
# 参考 https://api.bilibili.com/x/player/pagelist?bvid=BV1e84y1T7jp  取cid的网站


real_cid_list = []
counts=1
print(sum_video_BVlist)
aftercut_BVlist=sum_video_BVlist[(start_page-1)*30:]
aftercut_titlelist=sum_video_titlelist[(start_page-1)*30:]



# # test3
# print(aftercut_BVlist)
# print(aftercut_titlelist)




for BVid in aftercut_BVlist:
    while number >= counts:
        get_cid_url=base_get_cid_url+BVid
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        request = urllib.request.Request(url=get_cid_url,headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')


        dict_content=eval(content)
        cid_list=dict_content["data"]




        set_video_cid_list=[]
        if len(cid_list)>=1:# 说明由该BV号取到的视频是一个视频合集 里面有不同的视频 包含不同的弹幕
            for things in cid_list:
                set_video_cid_list.append(things["cid"])
            real_cid_list.append(set_video_cid_list)
            counts+=1
            break

        else:
            real_cid_list.append(cid_list["cid"])
            counts+=1
            break

    if counts>number:
        break



# test3
print(real_cid_list )
print(len(real_cid_list))



num_for_title=0
for cids in real_cid_list:
    clist=[]
    if len(cids)!=1:
        for cid in cids:
            base_url='https://comment.bilibili.com/'
            get_comment_url=base_url+str(cid)+'.xml'
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
            response = requests.get(get_comment_url, headers=headers)


            soup = BeautifulSoup(response.content,'xml',from_encoding='utf-8')
            comment_s=soup.findAll('d')

            for comments in comment_s:
                comment=comments.get_text()
                clist.append([str(cid),comment])

        title = 'bili_comments_{}'.format(aftercut_titlelist[num_for_title][0])

        # print(csv_title) # 测试
        print(f"合集视频：{aftercut_titlelist[num_for_title][0]} 的弹幕总数为{len(clist)}")
        num_for_title += 1


        title2=title.replace('\\','').replace('/','').replace('|','')
        f = open(file=title2, mode="a", encoding="UTF-8")
        # print(csv_title) # 测试

        writer=csv.writer(f)
        writer.writerows(clist)
        f.close()
        clist.clear()

    else:
        base_url = 'https://comment.bilibili.com/'
        get_comment_url = base_url + str(cids[0]) + '.xml'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        response=requests.get(get_comment_url,headers=headers)


        soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
        comment_s = soup.findAll('d')

        for comments in comment_s:
            comment = comments.get_text()
            clist.append([str(cids[0]), comment])

        title='bili_comments_'+aftercut_titlelist[num_for_title][0]

        print(f"视频：{aftercut_titlelist[num_for_title][0]} 的弹幕数量为{len(clist)}")
        num_for_title+=1

        title2=title.replace('\\','').replace('/','').replace('|','')
        f = open(file=title2, mode="a", encoding="UTF-8")
        # print(csv_title) # 测试

        writer=csv.writer(f)
        writer.writerows(clist)
        f.close()
        clist.clear()



