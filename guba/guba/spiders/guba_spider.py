# -*- coding: utf-8 -*-
import scrapy

from guba.items import GubaItem


class GubaSpiderSpider(scrapy.Spider):
    name = 'guba_spider'
    # allowed_domains = ['www']
    start_urls = []
    for i in range(1,2):
        url="http://guba.eastmoney.com/default,99_%s.html"%i
        start_urls.append(url)

    def parse(self, response):
        # print(response.text)
        li_list=response.xpath('//div[@class="cont bg gbbb1"]/div[@class="balist"]/ul/li')
        # print(li_list)
        item=GubaItem()
        for li in li_list:
            read_num=li.xpath('./cite[1]/text()').extract_first().strip()
            # print(read_num)
            comment = li.xpath('./cite[2]/text()').extract_first().strip()
            # print(comment)
            title = li.xpath('.//span[@class="sub"]/a[@class="note"]/text()').extract_first().strip()
            # print(title)
            author = li.xpath('.//cite[@class="aut"]/a/font/text()').extract_first().strip()
            update_time = li.xpath('.//cite[@class="last"]/text()').extract_first().strip()
            # print(author)
            # print(update_time)
            item['read_num']=read_num
            item['comment']=comment
            item['title']=title
            item['author']=author
            item['update_time']=update_time