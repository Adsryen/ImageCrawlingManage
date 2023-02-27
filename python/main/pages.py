import time
import requests
import re
import datetime
import defbag
import mysql

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}


#图集专栏
xiuren_url = 'https://www.demo.net/XiuRen/index.html'
xiuren_all_url = 'https://www.demo.net/XiuRen/index{}.html'
#全局变量
now_time = datetime.datetime.now()
#def模块
def img_name(url_1,HEADERS):
    '''
    获取当前套图中的标题
    '''
    global VolumeID
    global Volume2Name
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
        with open('Errorlog.txt','a+') as f1:
            f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->img_name()-->htmls -->line 27')
    # 查找标题并简化
    try:
        img_name = re.findall('<td.*?><div class=title>(.*)', htmls)
    except UnboundLocalError:
        print('UnboundLocalError!')
        with open('Errorlog.txt', 'a+') as f2:
            f2.writelines(str(now_time) + 'UnboundLocalError!      -----pages.py-->img_name()-->img_name -->line 34')
    try:
        Volume2Name = str(img_name).strip()[2:-4]
        VolumeID = str(re.findall('第(.*?)期',Volume2Name)).strip()[2:-2]
    except UnboundLocalError:
        print('UnboundLocalError!')
        with open('Errorlog.txt', 'a+') as f3:
            f3.writelines(str(now_time) + 'UnboundLocalError!      -----pages.py-->img_name()-->img_name_strip -->line 40')
    try:
        # print(img_name_strip)
        # print(img_name_ID)
        return Volume2Name
        return VolumeID
    except UnboundLocalError:
        print('UnboundLocalError!')
        with open('Errorlog.txt', 'a+') as f4:
            f4.writelines(str(now_time) + 'UnboundLocalError!      -----pages.py-->img_name()-->print(img_name_strip) -->line 46')
    # 写入文件名
    '''defbag.save_imgs_urls(img_name_strip)'''

def all_pages_img_name(url_1,HEADERS):
    '''
    获取当前套图中的标题
    '''
    global VolumeID
    global Volume2Name
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
        with open('Errorlog.txt','a+') as f1:
            f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->all_pages_img_name()-->htmls -->line 60')
    # 查找标题并简化
    try:
        img_name = re.findall('<td.*?><div class=title>(.*)', htmls)
    except UnboundLocalError:
        print('UnboundLocalError!')
        with open('Errorlog.txt', 'a+') as f2:
            f2.writelines(str(now_time) + 'UnboundLocalError!      -----pages.py-->all_pages_img_name()-->img_name -->line 67')
    Volume2Name = str(img_name).strip()[2:-4]
    VolumeID = str(re.findall('第(.*?)期', Volume2Name)).strip()[2:-2]
    return Volume2Name
    return VolumeID

def page1(url_1,HEADERS):
    '''
    解析多页套图中的第一页套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    ImgsID = 0
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        time.sleep(3)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
        with open('Errorlog.txt', 'a+') as f1:
            f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->page1()-->htmls -->line 81')
    # html中查找图片地址
    try:
        img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
    except UnicodeDecodeError:
        print('UnboundLocalError!')
        with open('Errorlog.txt', 'a+') as f1:
            f1.writelines(str(now_time) + 'UnboundLocalError!      -----pages.py-->page1()-->img_urls -->line 88')    
    http = "https://www.demo.net"

    #遍历写入文本
    try:
        for img_url in img_urls:
            # 拼接http
            ImgsUrl = str(http) + str(img_url)
            # 写入数据库
            ImgsID += 1
            mysql.XiuRen_VolumeUrl_insertion(VolumeID, Volume2Name, ImgsID, ImgsUrl)
            # 写入文件
            '''defbag.save_imgs(imgs,htmls, HEADERS3)'''
            # 写入文件链接
            defbag.save_imgs_urls(ImgsUrl)
            # 写入文件链接到api
            '''defbag.save_imgs_urls_API(imgs)'''
            # 延时
            '''time.sleep(8)'''
    except:
        print('url拼接失败！')
def all_pages_page1(url_1,HEADERS):
    '''
    解析多页套图中的第一页套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    ImgsID = 0
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except UnicodeDecodeError:
        print('UnicodeDecodeError!')
        with open('Errorlog.txt', 'a+') as f1:
            f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->all_pages_page1()-->htmls -->line 113')
    # html中查找图片地址
    img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
    http = "https://www.demo.net"
    for img_url in img_urls:
        # 拼接http
        ImgsUrl = str(http) + str(img_url)
        # print(imgs)
        #写入数据库
        ImgsID +=1
        mysql.XiuRen_VolumeUrl_insertion(VolumeID, Volume2Name, ImgsID, ImgsUrl)
        # 写入文件
        '''defbag.save_imgs(imgs,htmls, HEADERS3)'''
        #写入文件链接
        defbag.save_imgs_urls(ImgsUrl)
        #写入文件链接到api
        '''defbag.save_imgs_urls_API(imgs)'''
        # 延时
        '''time.sleep(8)'''

def pages(url_s,HEADERS):
    '''
    解析多页套图中的除第一页以外的套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    for x in range(1, 500):
        url = url_s.format(x)
        try:
            response = requests.get(url=url, headers=HEADERS)
            htmls = response.text.encode('ISO-8859-1').decode(
                requests.utils.get_encodings_from_content(response.text)[0])
        except UnicodeDecodeError:
            print('UnicodeDecodeError!')
            with open('Errorlog.txt', 'a+') as f1:
                f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->pages()-->htmls -->line 142')
        # html中查找图片地址
        img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
        http = "https://www.demo.net"
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
def all_pages_pages(url_s,HEADERS):
    '''
    解析多页套图中的除第一页以外的套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    ImgsID = 3
    for x in range(1, 500):
        url = url_s.format(x)
        try:
            response = requests.get(url=url, headers=HEADERS)
            htmls = response.text.encode('ISO-8859-1').decode('gbk')
        except UnicodeDecodeError:
            print('UnicodeDecodeError!')
            with open('Errorlog.txt', 'a+') as f1:
                f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->all_pages_pages()-->htmls -->line 171')
        # html中查找图片地址
        img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
        http = "https://www.demo.net"
        for img_url in img_urls:
            # 拼接http
            ImgsUrl = str(http) + str(img_url)
            # print(imgs_url)
            # 写入数据库
            ImgsID += 1
            mysql.XiuRen_VolumeUrl_insertion(VolumeID, Volume2Name, ImgsID, ImgsUrl)
            # 写入文件
            '''defbag.save_imgs(imgs_url,htmls, HEADERS3)'''
            # 写入文件链接
            defbag.save_imgs_urls(ImgsUrl)
            # 写入文件链接到api
            '''defbag.save_imgs_urls_API(imgs_url)'''
            # 延时
            '''time.sleep(8)'''

def all_urls(all_page_imgs):
    '''
    因页面结构是  一个html页面仅存在3个图片  用于处理后续多个未知数的页面
    '''
    a = all_page_imgs
    b = '_{}'
    str_list = list(a)
    str_list.insert(-5, b)
    a_b = ''.join(str_list)
    '''time.sleep(8)'''
    all_pages_pages(a_b,HEADERS2)

def all_page1(all_url_1,HEADERS):
    '''
    解析 https://www.demo.net/XiuRen/index.html 这个多个套图页面，中的的多个套图：名称、封面、日期、地址，在通过pages解析1个套图地址中的所有图片地址、数量（由于第一页与之后的每一页都毫无规律）
    '''


    try:
        response = requests.get(url=all_url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except UnicodeDecodeError:
        print(all_url_1,'页面抓取无效或加载异常')
        with open('Errorlog.txt', 'a+') as f1:
            f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->all_page1()-->htmls -->line 198')
    # html中查找图片地址
    Volume_names = re.findall('<div class="dan"><a href=.*? target=.*? title=(.*?) alt=.*?>', htmls)
    img_CoverUrls = re.findall('<img src="(.*?)"border=0>', htmls)
    img_times = re.findall('<font style="font-size:12px;">(更新:.*?)&nbsp;&nbsp;浏览:.*?</font></b></a></div>', htmls)
    img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)
    http = "https://www.demo.net"
    for (img_url,img_CoverUrl,img_time,Volume_name) in zip(img_urls,img_CoverUrls,img_times,Volume_names):
        # 拼接http
        all_page1_imgs = http + str(img_url)
        # 数据库变量
        CoverUrl = str(http) + str(img_CoverUrl)
        Volume1Name = str(Volume_name).strip()
        VolumeID = str(re.findall('No.(.*?)_', Volume1Name)).strip()[2:-2]
        VolumeCount = str(re.findall("\d+", Volume1Name)[-1])
        # 写入数据库
        mysql.XiuRen_VolumeMain_insertion(VolumeID, Volume1Name, CoverUrl, img_time, all_page1_imgs, VolumeCount)
        # #调用img_name
        # img_name(all_page1_imgs,HEADERS2)
        # #调用page1
        # page1(all_page1_imgs,HEADERS3)
        # #调用pages2.all_urls
        # all_urls(all_page1_imgs)


def all_pages(all_url_s,HEADERS):
    '''
    解析多个单页套图中，除去第一页单页套图外，剩余的多个套图地址，在通过pages解析单个套图地址中的图片地址（由于第一页与之后的每一页都毫无规律）
    '''
    for x in range(2, 300):
        url = all_url_s.format(x)
        try:
            response = requests.get(url=url, headers=HEADERS)
            htmls = response.text.encode('ISO-8859-1').decode('gbk')
        except UnicodeDecodeError:
            print('UnicodeDecodeError!')
            with open('Errorlog.txt', 'a+') as f1:
                f1.writelines(str(now_time) + 'UnicodeDecodeError!      -----pages.py-->all_pages()-->htmls -->line 224')
        # html中查找图片地址
        img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)
        Volume_names = re.findall('<div class="dan"><a href=.*? target=.*? title=(.*?) alt=.*?>', htmls)
        img_CoverUrls = re.findall('<img src="(.*?)"border=0>', htmls)
        img_times = re.findall('<font style="font-size:12px;">(更新:.*?)&nbsp;&nbsp;浏览:.*?</font></b></a></div>', htmls)
        http = "https://www.demo.net"
        for (img_url,img_CoverUrl,Volume_name,img_time) in zip(img_urls,img_CoverUrls,Volume_names,img_times):
            # 拼接http
            all_page1_imgs = str(http) + str(img_url)
            # 数据库变量
            CoverUrl = str(http) + str(img_CoverUrl)
            Volume1Name = str(Volume_name).strip()
            VolumeID = str(re.findall('No.(.*?)_', Volume1Name)).strip()[2:-2]
            VolumeCount = str(re.findall("\d+", Volume1Name)[-1]).strip()
            # 写入数据库
            mysql.XiuRen_VolumeMain_insertion(VolumeID, Volume1Name, CoverUrl, img_time, all_page1_imgs, VolumeCount)
            # # 调用img_name
            # all_pages_img_name(all_page1_imgs, HEADERS2)
            # # 调用page1
            # all_pages_page1(all_page1_imgs, HEADERS3)
            # # 调用pages2.all_urls
            # all_urls(all_page1_imgs)

def justone_imgs(page_url,HEADERS,all_page):
    '''
    爬取单独一个页面，适用查漏数据库后进行
    仅仅合并三个类，方便主程序调用
    '''
    img_name(page_url, HEADERS)
    page1(page_url,HEADERS)
    all_urls(all_page)
