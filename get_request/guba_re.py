import requests
import re
import json

# base_url="http://guba.eastmoney.com/default,99_%s.html"
#
# headers={
#   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }
#
#
# guba_list=[]
# for i in range(1,13):
#
#     response=requests.get(base_url %i,headers=headers)
#     # print(response.text)
#
#     ul_pattern=re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>',re.S)
#     ul_content=ul_pattern.search(response.text).group()
#     # print(ul_content)
#
#     #分析每一页的每条数据
#     li_pattern=re.compile(r'<li>(.*?)</li>',re.S)
#     li_list=li_pattern.findall(ul_content)
#     # print(li_list)
#
#     for li in li_list:
#         item={}
#         num_pattern=re.compile(r'<cite>(.*?)</cite>',re.S)
#         num_list=num_pattern.findall(li)
#         #阅读数
#         read_num=num_list[0].strip()
#         #评论数
#         commend_num=num_list[1].strip()
#         # print(read_num,commend_num)
#
#         #标题
#         title_pattern=re.compile(r'class="balink">(.*?)</a>].*?class="note">(.*?)</a>',re.S)
#         title_list=title_pattern.findall(li)
#         title=''
#         if title_list:
#             title=title_list[0][0]+title_list[0][1]
#             # print(title)
#
#         #作者
#         author_pattern=re.compile(r'<cite class="aut">.*?<font>(.*?)</font>',re.S)
#         author=author_pattern.search(li).group(1)
#         # print(author)
#
#         #更新时间
#         last_pattern=re.compile(r'<cite class="last">(.*?)</cite>',re.S)
#         last=last_pattern.search(li).group(1)
#         # print(last)
#
#         item["read_num"]=read_num
#         item["commend_num"]=commend_num
#         item["title"]=title
#         item["author"]=author
#         item["last"]=last
#
#         guba_list.append(item)
# # print(guba_list)
#
# with open('guba.json','w',encoding="utf-8") as f:
#     json.dump(guba_list,f)

class Guba:
    def __init__(self,base_url):
        self.base_url=base_url
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        self.guba_list=[]
        self.parse()
    def parse(self):
        for i in range(1,13):
            print("正在爬取第%s页"%i)
            if i==12:
                print("爬取完成")
            url=self.base_url %i
            response=requests.get(url=url,headers=self.headers)

            ul_pattern = re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>', re.S)
            ul_content=ul_pattern.search(response.text).group()
            # print(ul_content)

            #分析每一页的每条数据
            li_pattern=re.compile(r'<li>(.*?)</li>',re.S)
            li_list=li_pattern.findall(ul_content)
            # print(li_list)

            for li in li_list:
                item={}
                num_pattern=re.compile(r'<cite>(.*?)</cite>',re.S)
                num_list=num_pattern.findall(li)
                #阅读数
                read_num=num_list[0].strip()
                #评论数
                commend_num=num_list[1].strip()
                # print(read_num,commend_num)

                #标题
                title_pattern=re.compile(r'class="balink">(.*?)</a>].*?class="note">(.*?)</a>',re.S)
                title_list=title_pattern.findall(li)
                title=''
                if title_list:
                    title=title_list[0][0]+':'+title_list[0][1]
                    # print(title)

                #作者
                author_pattern=re.compile(r'<cite class="aut">.*?<font>(.*?)</font>',re.S)
                author=author_pattern.search(li).group(1)
                # print(author)

                #更新时间
                last_pattern=re.compile(r'<cite class="last">(.*?)</cite>',re.S)
                last=last_pattern.search(li).group(1)
                # print(last)

                item["read_num"]=read_num
                item["commend_num"]=commend_num
                item["title"]=title
                item["author"]=author
                item["last"]=last

                self.guba_list.append(item)
        self.save_file(self.guba_list)
    def save_file(self,data):
        with open('guba.json','w',encoding="utf-8") as f:
            json.dump(data,f)

if __name__ == '__main__':
    base_url="http://guba.eastmoney.com/default,99_%s.html"
    Guba(base_url)

    # with open('guba.json','r') as f:
    #     res=json.load(f)
    #     for each in res:
    #         print(each)