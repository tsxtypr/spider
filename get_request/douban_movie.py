import requests,re
import json
from lxml import etree

def get_content(url,headers):
    response=requests.get(url,headers=headers)
    return response.text

def save_data(data):
    with open('douban_movie.txt','a+',encoding='utf-8') as f:
        json.dump(data,f)

def parse_detail(type):
    url="https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=1"
   # print(type)
    headers={
        'Host':'movie.douban.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    i=0
    while True:
        html=get_content(url.format(type,str(i)),headers=headers)
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
            # print(item)
            save_data(item)
        i=i+20


def main():
    base_url="https://movie.douban.com/chart"
    headers={
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36       ',
    }
    html=get_content(base_url,headers)
    # print(html)
    html_element=etree.HTML(html)
    href_list=html_element.xpath('//div[@class="types"]/span/a/@href')
    # print(href_list)
    for href in href_list:
        type_pattern=re.compile(r'&type=(.*?)&interval')
        type=type_pattern.search(href).group(1)
        # print(type)
        parse_detail(type)


        #https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
if __name__ == '__main__':
    main()