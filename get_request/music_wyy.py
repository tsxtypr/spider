import requests
from lxml import etree

#获取首页的xpath对象
def get_xpath(url):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }

    response=requests.get(url=url,headers=headers)
    # print(response.text)
    return etree.HTML(response.text)

#获取首页的链接
def parse_index():
    html=get_xpath(base_url)
    res=html.xpath('//div[@class="blk"]/ul/li/a/@href')
    # print(res)
    return res

#获得详情页的element对象
def get_detail():
    url_link=parse_index()
    for each_url in url_link:
        new_url="https://music.163.com"+each_url
        return get_xpath(new_url)

#获得A、B、C的链接
def get_content():
    data_element=get_detail()
    res=data_element.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')
    return res

#获得歌手的信息
def get_singer():
    zm_list=get_content()
    for each_zm in zm_list:
        item={}
        newer_url="https://music.163.com/"+each_zm
        singer_element=get_xpath(newer_url)
        name=singer_element.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/text()')
        link=singer_element.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/@href')
        for index,name in enumerate(name):
            item['name']=name
            item['link']=link[index]
            singer_list.append(item)
        print(singer_list)

if __name__ == '__main__':
    singer_list=[]
    base_url = "https://music.163.com/discover/artist"
    parse_index()