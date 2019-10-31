import requests
from lxml import etree
import json

class ShanBei:
    def __init__(self,base_url):
        self.base_url=base_url
        self.headers={
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        self.shanbei_list=[]
        self.parse()

    def parse(self):
        for i in range(1,4):
            url=self.base_url%i
            response=requests.get(url=url,headers=self.headers)

            tbody_element=etree.HTML(response.text)
            tbody=tbody_element.xpath('//table[@class="table table-bordered table-striped"]/tbody')[0]
            # print(tbody)
            tr_list=tbody.xpath('./tr')
            # print(tr_list)

            for tr in tr_list:
                item = {}
                means=tr.xpath('./td[@class="span10"]/text()')[0]
                # print(word)
                word=tr.xpath('./td[@class="span2"]/strong/text()')[0]
                # print(word)
                item['word']=word
                item['means']=means
                self.shanbei_list.append(item)
            # print(self.shanbei_list)
            self.save_data(self.shanbei_list)
    def save_data(self,data):
        with open('shanbei.json','w',encoding="utf-8") as f:
            json.dump(data,f)

if __name__ == '__main__':
    base_url="https://www.shanbay.com/wordlist/110521/232414/?page=%s"
    ShanBei(base_url)
