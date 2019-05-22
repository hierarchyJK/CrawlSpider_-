# -*- coding:utf-8 -*-
"""
@project: ScrapyTest01
@author: KunJ
@file: sta.py
@ide: Pycharm
@time: 2019-05-21 22:56:28
@month: 五月
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl dytt_slaver -o ddt.csv'.split())