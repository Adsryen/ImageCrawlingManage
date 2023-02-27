#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.14 上午 1:58
# @name: Everyday_Update
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm
import First_cover_page
import Second_detail_page
import datetime
import defbag
import time
import mysql

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
                   "cookie":"UM_distinctid=17d46c535b965c-01c7a2b70e3e8c-59191353-1fa400-17d46c535baa30; __51cke__=; ASPSESSIONIDSEBBCCRT=ELFIJOMCPJGKCBGEHAEALMJP; CNZZDATA1278618868=75858223-1637567128-|1641918126; ASPSESSIONIDSABBCCRT=BKPJJOMCGCDGBBMPLMHLBOIO; __51laig__=10"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"ASPSESSIONIDACQTASAT=KHIILAHBBNLDEIBDCLAHDOCM; UM_distinctid=17b521e05531-0bcd55c5c01b1b-7868786b-1fa400-17b521e055451; CNZZDATA1278618868=619290373-1629169207-%7C1629169207; __51cke__=; CFWztgFirstShowTime_724_Cookie=2021-8-17%2011%3A18%3A26; CFWztgVisitTotal_724_Cookie=4; pageviews=4; __tins__20641871=%7B%22sid%22%3A%201629170304411%2C%20%22vd%22%3A%2010%2C%20%22expires%22%3A%201629172246232%7D; __51laig__=10"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}

# 当前时间
now_time = datetime.datetime.now()
#图集专栏
urls = ['https://www.demo.net/XiuRen/',
    'https://www.demo.net/MFStar/',
    'https://www.demo.net/MiStar/',
    'https://www.demo.net/MyGirl/',
    'https://www.demo.net/IMiss/',
    'https://www.demo.net/YouWu/',
    'https://www.demo.net/FeiLin/',
    'https://www.demo.net/MiiTao/',
    'https://www.demo.net/YouMi/',
    'https://www.demo.net/XiaoYu/',
    'https://www.demo.net/HuaYang/',
    'https://www.demo.net/XingYan/',
    'https://www.demo.net/BoLoli/',
    'https://www.demo.net/Uxing/',
    'https://www.demo.net/WingS/',
    'https://www.demo.net/LeYuan/',
    'https://www.demo.net/Taste/',
    'https://www.demo.net/HuaYan/',
    'https://www.demo.net/DKGirl/',
    'https://www.demo.net/Candy/',
    'https://www.demo.net/MintYe/',
    'https://www.demo.net/MTMeng/',
    'https://www.demo.net/Micat/']

if __name__ == '__main__':
    #主程序-专栏-自动跳转识别详情页（）
    mysql.connect()
    First_cover_page.connect()
    for i in range(0,len(urls)):
        First_cover_page.all_page1(urls[i],HEADERS)