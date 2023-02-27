from lxml import etree
import requests
import re
import time
import os
import urllib . request
import chardet
import pages2
import defbag

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}


#图集专栏
xiuren_url = 'https://demo.com/index.html'
xiuren_all_url = 'https://demo.com/index{}.html'
#def模块
def img_name(url_1,HEADERS):
    '''
    获取当前套图中的标题
    '''
    response = requests.get(url=url_1, headers=HEADERS)
    htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    # 查找标题并简化
    img_name = re.findall('<td.*?><div class=title>(.*)', htmls)
    img_name_strip = str(img_name).strip()[2:-4]
    print(img_name_strip)
    # 写入文件名
    '''defbag.save_imgs_urls(img_name_strip)'''

def page1(url_1,HEADERS):
    '''
    解析多页套图中的第一页套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    response = requests.get(url=url_1, headers=HEADERS)
    htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    # html中查找图片地址
    img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
    http = "https://demo.com"
    for img_url in img_urls:
        # 拼接http
        imgs = str(http) + str(img_url)
        print(imgs)
        # 写入文件
        '''defbag.save_imgs(imgs,htmls, HEADERS3)'''
        #写入文件链接
        defbag.save_imgs_urls(imgs)
        #写入文件链接到api
        '''defbag.save_imgs_urls_API(imgs)'''
        # 延时
        '''time.sleep(8)'''

def pages(url_s,HEADERS):
    '''
    解析多页套图中的除第一页以外的套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    for x in range(1, 50):
        url = url_s.format(x)
        response = requests.get(url=url, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode(
            requests.utils.get_encodings_from_content(response.text)[0])
        # html中查找图片地址
        img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
        http = "https://demo.com"
        for img_url in img_urls:
            # 拼接http
            imgs_url = str(http) + str(img_url)
            print(imgs_url)
            # 写入文件
            '''defbag.save_imgs(imgs_url,htmls, HEADERS3)'''
            # 写入文件链接
            defbag.save_imgs_urls(imgs_url)
            # 写入文件链接到api
            '''defbag.save_imgs_urls_API(imgs_url)'''
            # 延时
            '''time.sleep(8)'''

def all_page1(all_url_1,HEADERS):
    '''
    解析多个单页套图中，第一个套图地址中的的多个套图地址，在通过pages解析单个套图地址中的图片地址（由于第一页与之后的每一页都毫无规律）
    '''
    response = requests.get(url=all_url_1, headers=HEADERS)
    htmls = response.text.encode('iso-8859-1').decode('gbk')
    # html中查找图片地址
    img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)
    http = "https://demo.com"
    for img_url in img_urls:
        # 拼接http
        all_page1_imgs = str(http) + str(img_url)
        #调用img_name
        img_name(all_page1_imgs,HEADERS2)
        #调用page1
        page1(all_page1_imgs,HEADERS3)
        #调用pages2.all_urls
        pages2.all_urls(all_page1_imgs)

def all_pages(all_url_s,HEADERS):
    '''
    解析多个单页套图中，除去第一页单页套图外，剩余的多个套图地址，在通过pages解析单个套图地址中的图片地址（由于第一页与之后的每一页都毫无规律）
    '''
    for x in range(2, 300):
        url = all_url_s.format(x)
        response = requests.get(url=url, headers=HEADERS)
        htmls = response.text.encode('iso-8859-1').decode('gbk')
        # html中查找图片地址
        img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)
        http = "https://demo.com"
        for img_url in img_urls:
            # 拼接http
            all_page1_imgs = str(http) + str(img_url)
            # 调用img_name
            img_name(all_page1_imgs, HEADERS2)
            # 调用page1
            page1(all_page1_imgs, HEADERS3)
            # 调用pages2.all_urls
            pages2.all_urls(all_page1_imgs)
