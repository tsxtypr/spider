import requests
from lxml import etree
import json

class Sougou:
    def __init__(self,url):
        self.headers={
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        self.base_url=url
        self.singer_detail_list=[]
        self.parse_base()

    def get_element(self,url):
        response=requests.get(url=url,headers=self.headers)
        res_element=etree.HTML(response.text)
        # print(response.text)
        return res_element

    #爬取基础页的链接
    def parse_base(self):
        data=self.get_element(self.base_url)
        base_link=data.xpath('//div[@class="l"]/ul/li/a/@href')[1:]
        # print(base_link)
        self.get_zm(base_link)

    #爬取明星分组
    def get_zm(self,base_link):
        #遍历明星分组
        for each_url in base_link:
            #得到页面的element对象
            index_element=self.get_element(each_url)
            #接下来解析每个分组明星下面的A、B、C
            self.parse_zm(index_element)
            return #返回第一条数据

    #得到A、B、C的超链接
    def parse_zm(self,index_element):
        zm_list=index_element.xpath('//div[@class="num"]/a/@href')[1:]
        self.get_singer(zm_list)

    #获得每个歌单页面的element对象
    def get_singer(self,zm_list):
        #获得到每个歌单页面
        for each_url in zm_list:
            singer_element=self.get_element(each_url)
            self.parse_sings(singer_element)
            return  #返回第一条数据

    #获取A页面的名字及超链接
    def parse_sings(self,singer_element):
        #第一页的表头数据
        form_link=singer_element.xpath('//ul[@id="list_head"]/li/strong/a/@href')
        # print(form_link)
        #第一页的表内数据
        content_link=singer_element.xpath('//div[@id="list1"]/ul/li/a/@href')
        # print(content_link)
        singer_list=form_link+content_link
        # print(singer_list)
        self.get_detail(singer_list)

    #进入到歌手详情页面，并得到页面的element对象
    def get_detail(self,singer_list):
        #遍历每一个歌手
        for singer_url in singer_list:
            singer_element=self.get_element(singer_url)
            self.parse_detail(singer_element)
            print(singer_element)
            return  #返回第一条数据

    #解析歌手的详情页面
    def parse_detail(self,singer_element):
        item={}
        name=singer_element.xpath('//div[@class="intro"]/div/strong/text()')
        desc=singer_element.xpath('//div[@class="intro"]/p/text()')
        sings=singer_element.xpath('//ul[@id="song_container"]/li/a/span[@class="text"]/i/text()')
        item["name"]=name
        item["desc"]=desc
        item["sings"]=sings
        self.singer_detail_list.append(item)
        # print(self.singer_detail_list)
        return self.singer_detail_list

if __name__ == '__main__':
    base_url="https://www.kugou.com/yy/singer/index"
    res=Sougou(base_url)
    with open('sougou.json','w',encoding="utf-8") as f:
        json.dump(res,f)