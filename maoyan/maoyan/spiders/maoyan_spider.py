# -*- coding: utf-8 -*-
import scrapy

from maoyan.items import MaoyanItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    # allowed_domains = ['www']
    start_urls = []
    for i in range(1):
        url="https://maoyan.com/board/4?offset=%s"%i
        start_urls.append(url)

    def parse(self, response):
        # print(response.text)
        item=MaoyanItem()
        dd_list=response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            name = dd.xpath('.//p[@class="name"]/a/text()').extract_first()
            # print(name)
            actors = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()[3:]
            play_time = dd.xpath('.//p[@class="releasetime"]/text()').extract_first()[5:]
            score_list = dd.xpath('.//p[@class="score"]/i/text()').extract()
            score="".join(score_list)
            detail_url="https://maoyan.com"+dd.xpath('.//p[@class="name"]/a/@href').extract_first()
            # print(actors)
            # print(play_time)
            # print(score)
            # print(detail_url)
            item['name']=name
            item['actors']=actors
            item['score']=score
            item['detail_url']=detail_url
