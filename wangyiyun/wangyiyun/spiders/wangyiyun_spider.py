# -*- coding: utf-8 -*-
import scrapy

from wangyiyun.items import WangyiyunItem


class WangyiyunSpiderSpider(scrapy.Spider):
    name = 'wangyiyun_spider'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/discover/artist']

    def parse(self, response):
        # print(response.text)
        li_list=response.xpath('//div[@id="singer-cat-nav"]/div[@class="blk"]/ul/li')
        # print(li_list)
        for li in li_list:
            url="https://music.163.com"+li.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url,callback=self.parse_zm)
            break

    def parse_zm(self,response):
        li_list=response.xpath('//ul[@id="initial-selector"]/li')
        # print(li_list)
        for li in li_list:
            url="https://music.163.com"+li.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url,callback=self.parse_detail)
            break

    def parse_detail(self,response):
        li_list=response.xpath('//ul[@id="m-artist-box"]/li')
        # print(li_list)
        item=WangyiyunItem()
        for li in li_list:
            name = li.xpath('./p/a[1]/text()|./a/text()').extract_first()
            # print(name)
            singer_url = "https://music.163.com"+li.xpath('./div[@class="u-cover u-cover-5"]/a/@href|./a/@href').extract_first()
            # print(singer_url)
            item['name']=name
            item['singer_url']=singer_url
            detail_url=singer_url.replace('?',"/desc?")
            yield scrapy.Request(url=detail_url,callback=self.parse_detail_infos,meta={'item':item})

    def parse_detail_infos(self,response):
        item=response.meta['item']
        #
        # 'https://music.163.com/#/artist?id=1875'
        # 'https://music.163.com/#/artist/desc?id=1875'
        desc=response.xpath('//div[@class="n-artdesc"]/p/text()').extract_first()
        # print(desc)
        item['desc']=desc