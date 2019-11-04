import requests
from selenium import webdriver
import time
from lxml import etree

def handle_text(text):
    if text:
        return text[0]
    return ''

def parse_html(text):
    html_element=etree.HTML(text)
    div_list=html_element.xpath('//div[@id="root"]/div/div/div/div/div')
    # print(div_list)
    for div in div_list:
        item={}
        #书名
        title=handle_text(div.xpath('.//div[@class="title"]/a/text()'))
        #评分
        score=handle_text(div.xpath('.//span[@class="rating_nums"]/text()'))
        #评论数量
        comment_num=handle_text(div.xpath('.//span[@class="pl"]/text()'))
        #链接
        link=handle_text(div.xpath('.//div[@class="title"]/a/@href'))

        info_list=handle_text(div.xpath('.//div[@class="meta abstract"]/text()')).split('/')
        # print(info_list)
        if info_list and len(info_list)>=4:
            item['price']=info_list[-1]
            item['time']=info_list[-2]
            item['publish']=info_list[-3]
            item['authors']=info_list[:-3]

        if all([title,link]):
            item['title']=title
            item['score']=score
            item['comment_num']=comment_num[1:-1]
            item['link']=link


            print(item)

if __name__ == '__main__':
    base_url="https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=%s"
    # 声明浏览器对象
    browser = webdriver.PhantomJS()
    for i in range(2):
        url=base_url% str(i*15)
        # time.sleep(1)
        # print(url)
        browser.get(url)
        html=browser.page_source
        # print(html)
        #进行解析
        parse_html(html)