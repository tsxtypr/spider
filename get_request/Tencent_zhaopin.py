import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import json

class Tencent(object):
    def __init__(self,url):
        self.url=url
        self.driver=webdriver.PhantomJS()
        self.wait=WebDriverWait(self.driver,10)
        self.parse()


    def get_text(self,text):
        if text:
            return text[0]
        return ''


    #用于设置等待时长，以及返回页面
    def get_element(self,url,xpath):
        self.driver.get(url)
        #设置等待事件
        self.wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
        return self.driver.page_source

    def get_link(self):
        timestamp = time.time()
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + str(
            timestamp * 1000) + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex='+str(i)+'&pageSize=10&language=zh-cn&area=cn'
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        }
        page = requests.get(url=url, headers=headers)
        page_data = json.loads(page.text)
        datas = page_data['Data']['Posts']
        links = []
        for each in datas:
            link = each['PostURL']
            links.append(link)
        return links

    def parse(self):
        html=self.get_element(self.url,'//div[@class="recruit-wrap recruit-margin"]')
        html_element=etree.HTML(html)
        div_list=html_element.xpath('//div[@class="recruit-wrap recruit-margin"]/div')
        links=self.get_link()
        for div in div_list:
            i=0
            item={}
            name=self.get_text(div.xpath('.//a/h4/text()'))
            # print(name)
            location=self.get_text(div.xpath('.//p[@class="recruit-tips"]/span[2]/text()'))
            type=self.get_text(div.xpath('.//p[@class="recruit-tips"]/span[3]/text()'))
            time=self.get_text(div.xpath('.//p[@class="recruit-tips"]/span[4]/text()'))
            desc=self.get_text(div.xpath('.//p[@class="recruit-text"]/text()'))
            item['name']=name
            item['location']=location
            item['type']=type
            item['time']=time
            item['desc']=desc
            item['url']=links[i]
            i+=1
            print(item)
if __name__ == '__main__':
    base_url="https://careers.tencent.com/search.html?index=%s"
    for i in range(1,3):
        url=base_url%i
        Tencent(url)
