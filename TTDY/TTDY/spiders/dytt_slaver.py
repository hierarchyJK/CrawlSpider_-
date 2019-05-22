# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TTDY.items import TtdyItem
import re
from selenium import webdriver
import time
class DyttSlaverSpider(CrawlSpider):
    name = 'dytt_slaver'
    allowed_domains = ['dy2018.com']
    start_urls = ['https://www.dy2018.com/2/index.html']
    for i in range(2,10):
        start_urls.append('https://www.dy2018.com/2/index_' + str(i) + '.html')
    # start_urls = ['https://www.dy2018.com/2/index_2.html']
    move_links = LinkExtractor(allow=r'/i/\d*.html', restrict_xpaths=('//div[@class="co_content8"]'))
    # page_links = LinkExtractor(allow=r'/index_\d*.html')
    rules = (
         # Rule(page_links, callback='parse_item', follow=True),
        Rule(move_links, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = TtdyItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        str_resp = response.body.decode('gb2312', errors='ignore')
        print(response.text)
        rep_chars = ['&nbsp;', '&middot;', '&ldquo;', '&rdquo;', '&hellip;']
        for rep in rep_chars:
            str_resp = str_resp.replace(rep, '')
        # print(str_resp)
        title = re.search(r'◎片　　名(.*?)</.+>', str_resp).group(1).strip()
        try:
            translation = re.search(r'◎译　　名(.*?)</.+>', str_resp).group(1).strip()
        except:
            translation = ''
        # print(title)
        # 名字
        items['name'] = title + '|' + translation

        # 年代
        items['year'] = re.search(r'◎年　　代(.*?)</.+>', str_resp).group(1).strip()
        # 评分（注意有些电影没有评分）
        try:
            items['score'] = response.xpath('//strong[@class="rank"]/text()').extract()[0].strip()
        except:
            items['score'] = "无评分"

        # 语言
        items['language'] = re.search(r'◎语　　言(.*?)</.+>', str_resp).group(1).strip()

        # 类别
        items['movie_type'] = re.search(r'◎类　　别(.*?)</.+>', str_resp).group(1).strip()

        # 上映时间
        items['release_date'] = re.search(r'◎上映日期(.*?)</.+>', str_resp).group(1).strip()

        # 文件大小
        items['file_size'] = re.search(r'◎文件大小(.*?)</.+>', str_resp).group(1).strip()

        # 片长
        items['film_time'] = re.search(r'◎片　　长(.*?)</.+>', str_resp).group(1).strip()

        # 简介
        items['introduction'] = re.search(r'◎简　　介</.+>\r\n<.+>(.*?)</.+>', str_resp).group(1).strip()

        # 海报
        items['posters'] = response.xpath('//div[@id="Zoom"]/*[1]/img/@src').extract()[0]
        # print(items['posters'])
        #下载链接
        items['download_link'] = self.get_download_link(response.url)
        # yield items
    def get_download_link(self, url):
        chrome_options =  webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        time.sleep(1)
        link = re.search(r'\"(thunder:.*?)\"', driver.page_source).group(1)
        driver.close()
        return link