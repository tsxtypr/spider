import requests,re
import json
from lxml import etree


class Douban:
    def __init__(self,url):
        self.url=url

    #根据url,headers去抓取网页的text
    def get_content(self,url,headers):
        response=requests.get(url,headers=headers)
        return response.text

    #将数据保存下来
    def save_data(self,data):
        with open('douban_movie.txt','a+',encoding='utf-8') as f:
            json.dump(data,f)

    def parse_detail(self,type):
        url="https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=1"
       # print(type)
        headers={
            'Host':'movie.douban.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        i=0
        while True:
            html=self.get_content(url.format(type,str(i)),headers=headers)
            # print(html)
            content=json.loads(html)
            for data in content:
                item={}
                score=data['rating'][0]
                types=data['types']
                link=data['url']
                title=data['title']
                release_date=data['release_date']
                actors=data['actors']
                item['title']=title
                item['score']=score
                item['types']=types
                item['url']=link
                item['release_date']=release_date
                item['actors']=actors
                print(item)
                self.save_data(item)
            i=i+20


    def main(self):
        headers={
        'Host':'movie.douban.com',
        'Referer':'https://movie.douban.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36       ',
        }
        html=self.get_content(self.url,headers)
        # print(html)
        html_element=etree.HTML(html)
        href_list=html_element.xpath('//div[@class="types"]/span/a/@href')
        # print(href_list)
        for href in href_list:
            type_pattern=re.compile(r'&type=(.*?)&interval')
            type=type_pattern.search(href).group(1)
            # print(type)
            self.parse_detail(type)


if __name__ == '__main__':
    base_url = "https://movie.douban.com/chart"
    d=Douban(base_url)
    d.main()