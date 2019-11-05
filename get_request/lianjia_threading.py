import requests
from lxml import etree
import json
import threading
from queue import Queue

class Lianjia(threading.Thread):
    def __init__(self,name,q):
        super().__init__()
        self.name=name
        self.q=q

    def run(self):
        self.get_detail()

    def get_text(self,text):
        if text:
            return text[0]
        return ''

    def get_detail(self):
        while True:
            if not q.empty():
                link = q.get()
                for i in range(1,5):
                    url=link+'pg%s'%i
                    print(f"{self.name}在爬{i}页,url:{url}")
                    response=requests.get(url=url,headers=headers)
                    # print(response.text)
                    detail_element=etree.HTML(response.text)
                    div_list=detail_element.xpath('//ul[@class="sellListContent"]/li/div[@class="info clear"]')
                    # print(div_list)
                    home_list=[]
                    for div in div_list:
                        item={}
                        title=self.get_text(div.xpath('.//div[@class="title"]/a/text()'))
                        infos=self.get_text(div.xpath('.//div[@class="address"]/div/text()')).split('|')
                        size=infos[0]
                        chaoxiang = infos[2]
                        bulit_time=infos[-2]
                        price1=self.get_text(div.xpath('.//div[@class="priceInfo"]/div/span/text()'))
                        price2=self.get_text(div.xpath('.//div[@class="priceInfo"]/div/text()'))
                        price=price1+price2

                        item['title']=title
                        item['size']=size
                        item['chaoxiang']=chaoxiang
                        item['bulit_time']=bulit_time
                        item['price']=price
                        # print(item)
                        home_list.append(item)
                        # break
                    self.save_data(home_list)
            else:
                break
    def save_data(self,data):
        with open('lianjia_threading.txt','a+',encoding="utf-8") as f:
            json.dump(data,f)


if __name__ == '__main__':
    base_url="https://bj.lianjia.com/ershoufang/rs/"
    headers = {
        'Host': 'bj.lianjia.com',
        'Referer': 'https://bj.lianjia.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    response = requests.get(url=base_url, headers=headers)
    html_element = etree.HTML(response.text)
    link_list = html_element.xpath('//div[@data-role="ershoufang"]/div/a/@href')

    #定义一个消息队列
    q=Queue()
    for link in link_list:
        url="https://bj.lianjia.com"+link
        q.put(url)

    #定义一个列表
    thread_list = ['aa', 'bb', 'cc', 'dd']
    #定义一个列表，用于阻塞主线程
    wait_list=[]
    for name in thread_list:
        t=Lianjia(name,q)
        t.start()
        wait_list.append(t)
    for wait in wait_list:
        wait.join()











