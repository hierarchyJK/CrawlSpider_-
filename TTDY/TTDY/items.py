# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TtdyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 片名
    name = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 上映时间
    release_date = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 类别
    movie_type = scrapy.Field()
    # 文件大小
    file_size = scrapy.Field()
    # 片长
    film_time = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 下载链接
    download_link = scrapy.Field()
    # 海报
    posters = scrapy.Field()
