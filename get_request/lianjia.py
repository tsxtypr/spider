import requests
from lxml import etree
import json

def get_text(text):
    if text:
        return text[0]
    return ''

def get_base_url(url):
    response=requests.get(url=url,headers=headers)
    # print(response.text)
    html_element=etree.HTML(response.text)
    link_list=html_element.xpath('//div[@data-role="ershoufang"]/div/a/@href')
    for link in link_list:
        url="https://bj.lianjia.com"+link
        # print(url)
        get_detail(url)
        break

def get_detail(url):
    for i in range(1,11):
        url=url+'/pg%s/'%i
        response=requests.get(url,headers=headers)
        # print(response.text)
        detail_element=etree.HTML(response.text)
        div_list=detail_element.xpath('//ul[@class="sellListContent"]/li/div[@class="info clear"]')
        # print(div_list)
        home_list=[]
        for div in div_list:
            item={}
            title=get_text(div.xpath('.//div[@class="title"]/a/text()'))
            infos=get_text(div.xpath('.//div[@class="address"]/div/text()')).split('|')
            size=infos[0]
            chaoxiang = infos[2]
            bulit_time=infos[-2]
            price1=get_text(div.xpath('.//div[@class="priceInfo"]/div/span/text()'))
            price2=get_text(div.xpath('.//div[@class="priceInfo"]/div/text()'))
            price=price1+price2

            item['title']=title
            item['size']=size
            item['chaoxiang']=chaoxiang
            item['bulit_time']=bulit_time
            item['price']=price
            # print(item)
            home_list.append(item)
            # break
        save_data(home_list)
def save_data(data):
    with open('lianjia_base.txt','a+',encoding="utf-8") as f:
        json.dump(data,f)


if __name__ == '__main__':
    base_url="https://bj.lianjia.com/ershoufang/rs/"
    headers={
'Host':'bj.lianjia.com',
'Referer':'https://bj.lianjia.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    get_base_url(base_url)

