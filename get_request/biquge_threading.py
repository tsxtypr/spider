import requests
from lxml import etree
from selenium import webdriver
import json
from queue import Queue
import threading

class Biquge(threading.Thread):
    def __init__(self,q=None):
        super().__init__()
        self.headers={
            'Host':'www.xbiquge.la',
            'Referer':'http://www.xbiquge.la/xuanhuanxiaoshuo/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36           ',
        }
        self.base_path='./books_spider/'
        self.q=q


    def get_text(self,text):
        if text:
            return text[0]
        return ''

    def get_content(self,url,headers):
        response=requests.get(url=url,headers=headers)
        return response.content.decode("utf-8")

    def run(self):
        self.get_base_link()

    def get_base_link(self):
        while True:
            if self.q.empty():
                break
            base_url = self.q.get()
            html=self.get_content(url=base_url,headers=self.headers)
            # print(html)
            # print(self.base_url % i)
            self.parse_base_url(html=html,referer_url=base_url)


    def parse_base_url(self,html,referer_url):
        html_element=etree.HTML(html)
        li_list=html_element.xpath('//div[@class="l"]/ul/li')
        for li in li_list:
            book_link=self.get_text(li.xpath('.//span[@class="s2"]/a/@href'))
            # print(book_link)
                # print(referer_url)
            self.get_chapters_url(book_link,referer_url)
            break



    def get_chapters_url(self,url,referer_url):
        headers={
            'Host':'www.xbiquge.la',
            'Referer':referer_url,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        }
        response=requests.get(url=url,headers=headers)
        self.parse_chapters_url(response.content.decode("utf-8"))

    def parse_chapters_url(self,html):
        html_element=etree.HTML(html)
        dd_list=html_element.xpath('//div[@id="list"]/dl/dd')
        # print(dd_list)
        for dd in dd_list:
            chapters_url=self.get_text(dd.xpath('.//a/@href'))
            chapters_url='http://www.xbiquge.la'+chapters_url
            # print(chapters_url)
            self.get_detail(chapters_url)
            # break

    def get_detail(self,chapters_url):
        browser=webdriver.PhantomJS()
        browser.get(chapters_url)
        html=browser.page_source
        self.parse_detail(html)

    def parse_detail(self,html):
        html_element=etree.HTML(html)
        title=self.get_text(html_element.xpath('//div[@class="bookname"]/h1/text()'))
        name=self.get_text(html_element.xpath('//div[@class="con_top"]/a[last()]/text()'))
        contents=html_element.xpath('//div[@id="content"]/text()')
        contents_list=[]
        for each in contents:
            item={}
            each=each.strip().replace('\xa0','')
            if each:
                contents_list.append(each)
        contents_strings=''.join(contents_list)
        item[title]=contents_strings
        item['name']=name
        # print(name)
        self.save_data(item)
        # print(contents_strings)
        # print(title)


    def save_data(self,data):
        dirname=self.base_path+data['name']+'.txt'
        with open(dirname,'a+',encoding='utf-8') as f:
            json.dump(data,f)



if __name__ == '__main__':
    base_url = "http://www.xbiquge.la/fenlei/1_%s.html"
    url_list=[]
    for i in range(1,402):
        url=base_url%i
        url_list.append(url)


    #定义一个队列
    q=Queue()
    #将数据写入队列
    for url in url_list:
        q.put(url)
    #开线程
    crawl_list=['a','b','c','d','e']
    for crawl in crawl_list:
        b=Biquge(q=q)
        b.start()
