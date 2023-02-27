import requests
import re
import time
import os
import pages
import defbag
from lxml import html
from lxml import etree
from html.parser import HTMLParser
from bs4 import BeautifulSoup

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
#获取页面源代码
url_1 = 'https://www.demo.com/7635.html'
all_urls = 'https://www.demo.com/7635_{}.html'

# 图集专栏
xiuren_url = 'https://www.demo.com/index.html'
xiuren_all_urls = 'https://wdemo.com/index{}.html'

response = requests.get(xiuren_url, headers=HEADERS)
htmls = response.text.encode('iso-8859-1').decode('gbk')
# html中查找图片地址
img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)

http = "https://www.demo.com"
for img_url in img_urls:
    # 拼接http
    all_page1_imgs = str(http) + str(img_url)
    a = all_page1_imgs
    b = '_{}'
    str_list = list(a)
    str_list.insert(-5, b)
    a_b = ''.join(str_list)
    time.sleep(1)
    print(a_b)

'''for x in range(2, 25):
    all_url = xiuren_all_urls.format(x)
    print(all_url)'''
