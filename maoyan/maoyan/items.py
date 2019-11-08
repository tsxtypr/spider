# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    actors = scrapy.Field()
    play_time = scrapy.Field()
    score = scrapy.Field()
    detail_url = scrapy.Field()
    pass
