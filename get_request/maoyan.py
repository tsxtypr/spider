import re
import requests
import json

class Maoyan:
    def __init__(self,url):
        self.url=url
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        self.parse()
    def parse(self):
        movie_list = []
        for i in range(10):
            url=self.url+"?offset={}".format(i*10)
            response=requests.get(url=url,headers=self.headers)

            #匹配dd
            dl_pattern=re.compile(r'<dl class="board-wrapper">(.*?)</dl>',re.S)
            dl_content=dl_pattern.search(response.text).group()

            #找到一页当中的所有dl
            dd_pattern=re.compile(r'<dd>(.*?)</dd>',re.S)
            dd_list=dd_pattern.findall(dl_content)


            for dd in dd_list:
                item={}
                # 电影名称
                movie_name_pattern=re.compile(r'title="(.*?)" class=',re.S)
                movie_name=movie_name_pattern.findall(dd)[0]
                # print(movie_name)
                item["电影名称"]=movie_name

                # 主演
                actors_pattern=re.compile(r'<p class="star">(.*?)</p>',re.S)
                actors=actors_pattern.findall(dd)[0].strip()[3:]
                # print(actors)
                item["主演"]=actors

                # #上映时间
                time_pattern=re.compile(r'<p class="releasetime">(.*?)</p>',re.S)
                time=time_pattern.findall(dd)[0][5:15]
                # print(time)
                item["上映时间"]=time

                # 评分
                score_pattern=re.compile(r'<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>',re.S)
                score=score_pattern.findall(dd)[0][0]+score_pattern.findall(dd)[0][1]
                # print(score)
                item["评分"]=score

                #将字典放入总的列表中
                movie_list.append(item)
        # print(movie_list)
        self.save_file(movie_list)
    def save_file(self,data):
        #将数据存储为二进制的json数据
        with open('maoyan.json','w',encoding="utf-8") as f:
            json.dump(data,f)
if __name__ == '__main__':
    base_url="https://maoyan.com/board/4"
    Maoyan(base_url)

    #读取json数据
    with open("maoyan.json",'r') as f:
        res=json.load(f)
        for each in res:
            print(each)

headers={}