import re
import pymysql
import datetime
import requests
import re
import os
import time
import Second_detail_page
import mysql

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}

# 连接database
mysql_1 = {
    "name":"HUAWEI-MY-xiuren",
    "host":"122.9.153.176",
    "user":"xiuren",
    "password":"6sfitTyZJdFFzYYP",
    "database":"xiuren"
}
#全局变量
now_time = datetime.datetime.now()
VolumeSource_lists = []

ImgsID = 0
def connect():
    '''
    数据库连接
    '''
    global conn
    global cur
    try:
        conn = pymysql.connect(host=mysql_1["host"],user=mysql_1["user"],password=mysql_1["password"],database=mysql_1["database"],charset="utf8")
        cur = conn.cursor()
        print("数据库 %s 连接成功！" %mysql_1["name"])
        print()
    except pymysql.Error as e:
        print("数据库 %s 连接失败 ："+str(e) %mysql_1["name"])
        print()

def find_VolumeSource(SqlName):
    try:

        # 获取全部图册的源
        sqlQuery_fetchall = " SELECT VolumeSource FROM " + SqlName
        cur.execute(sqlQuery_fetchall)
        results = cur.fetchall()

        for url in results:
            get_url = str(url).strip()[2:-3]
            print(get_url)
            VolumeSource_lists.append(get_url)

    except pymysql.Error as e:
        print("查询CoverUrl数据失败！")
        print(str(e))

def all_pages_img_name(url_1,HEADERS):
    '''
    获取当前套图中的标题
    '''
    global VolumeID
    global Volume2Name
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except:
        print(url_1,'获取当前套图中的标题时，html源代码抓取异常!')
    # 查找标题并简化
    try:
        img_name = re.findall('<td.*?><div class=title>(.*)', htmls)
    except:
        print(url_1,'获取当前套图中的标题时，正则表达式执行异常!!')
    Volume2Name = str(img_name).strip()[2:-4]
    VolumeID = str(re.findall("\d+", Volume2Name)[0])
    return Volume2Name
    return VolumeID
def detail_pages(page1_img_urls,url,HEADERS):
    '''
    解析多页套图中的除第一页以外的套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    http = "https://www.demo.net"
    ImgsID = 0
    Complete = 1
    all_pages_img_name(url,HEADERS2)
    try:
        for page1_img_url in page1_img_urls:
            # 拼接http
            ImgsUrl = str(page1_img_url)
            # 写入数据库
            ImgsID += 1
            mysql.VolumeUrl_insertion(SqlName, VolumeID, Volume2Name, ImgsID, ImgsUrl, Complete)
    except:
        print(SqlName,'数据库插入失败！')
    #加入格式化替换符
    a = str(url)
    b = '_{}'
    str_list = list(a)
    str_list.insert(-5, b)
    a_b = ''.join(str_list)
    url_formats = a_b
    #遍历：https://www.demo.net/Uxing/316_{}.html
    time.sleep(2)
    for x in range(1, 1000):
        url_format = url_formats.format(x)
        try:
            response = requests.get(url=url_format , headers=HEADERS)
            htmls = response.text.encode('ISO-8859-1').decode('gbk')
        except:
            print(url_format,'获取当前图册详情页中的图片时，html源代码抓取异常!')
        # html中查找图片地址
        try:
            img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
        except:
            print(url_format, '该图册详情页图片地址未找到，抓取失败!!')

        try:
            htmls_status = re.findall('<title>(.*?)</title>', htmls)
            htmls_status_404 = str(re.findall("\d+", str(htmls_status))[0])
        except:
            print(url_format, '判断当前套图中第', x , '页的状态时，正则表达式执行异常!!')
        if htmls_status_404 == '404':
            print('页面404，跳出循环！')
            break
        else:
            for img_url in img_urls:
                # 拼接http
                ImgsUrl = str(http) + str(img_url)
                # print(imgs_url)
                # 写入数据库
                ImgsID += 1
                mysql.VolumeUrl_insertion(SqlName, VolumeID, Volume2Name, ImgsID, ImgsUrl, Complete)

def detail_page1(url,HEADERS):
    '''
    解析多页套图中的第一页套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    try:
        response = requests.get(url=url, headers=HEADERS)
        time.sleep(1.5)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except :
        print(url,'获取当前图册详情页中的图片时，html源代码抓取异常!')
    # html中查找图片地址
    try:
        img_urls = re.findall('alt=".*?" src="(.*?)" /><br />', htmls)
    except:
        print(url,'该图册详情页图片地址未找到，抓取失败!!')
    detail_pages(img_urls,url,HEADERS)

if __name__ == '__main__':
    SqlName = 'XiuRen_VolumeUrl'
    ss = 'https://www.demo.net/XiuRen/9900.html'
    mysql.connect()
    # find_VolumeSource(SqlName)
    # for VolumeSource_list in VolumeSource_lists:
    #     detail_page1(VolumeSource_list,HEADERS)


    detail_page1(ss,HEADERS)

