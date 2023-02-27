#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.14 上午 1:43
# @name: Second_detail_page
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm
# 导入pymysql模块
import pymysql
import datetime
import requests
import re
import os
import time
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
http = "https://www.demo.net"
VolumeMain_SqlNames = [
    'XiuRen_VolumeMain',
    'MFStar_VolumeMain',
    'MiStar_VolumeMain',
    'MyGirl_VolumeMain',
    'IMiss_VolumeMain',
    'YouWu_VolumeMain',
    'FeiLin_VolumeMain',
    'MiiTao_VolumeMain',
    'YouMi_VolumeMain',
    'XiaoYu_VolumeMain',
    'HuaYang_VolumeMain',
    'XingYan_VolumeMain',
    'BoLoli_VolumeMain',
    'Uxing_VolumeMain',
    'WingS_VolumeMain',
    'LeYuan_VolumeMain',
    'Taste_VolumeMain',
    'HuaYan_VolumeMain',
    'DKGirl_VolumeMain',
    'Candy_VolumeMain',
    'MintYe_VolumeMain',
    'MTMeng_VolumeMain',
    'Micat_VolumeMain'
]
def download_pic(url1,url2):
    '''
    url1 : 'https://www.demo.net'
    url2 : '/UploadFile/pic/9899.jpg'
    '''
    # 将文件路径分割出来
    url3 = '.' + url2
    url4 = '.' + os.path.split(url2)[0]
    name = os.path.split(url2)[1]
    # 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
    if not os.path.isdir(url4):
        os.makedirs(url4)
        print('新文件夹，执行创建！')

    # 然后再判断文件是否存在，如果不存在，则创建
    if not os.path.exists(url3):
        try:
            response = requests.get(url=url1 + url2, headers=HEADERS)
            with open(url3, 'wb') as fd:
                for chunk in response.iter_content():
                    fd.write(chunk)
            print(name, '保存成功！')
        except:
            print(url1 + url2, '保存失败！')
    else:
        print('图片已存在！')

def connect():
    '''
    数据库连接，提供给 find_VolumeSource（）使用
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

def find_VolumeSource(VolumeMain_SqlName):
    '''
    从VolumeMain获取全部图册的源VolumeSource，写入VolumeSource_lists
    '''
    try:
        # 获取全部图册的源
        connect()
        sqlQuery_fetchall = " SELECT VolumeSource FROM " + VolumeMain_SqlName
        cur.execute(sqlQuery_fetchall)
        results = cur.fetchall()

        for url in results:
            get_url = str(url).strip()[2:-3]
            VolumeSource_lists.append(get_url)
        print(VolumeMain_SqlName,'VolumeSource写入列表成功！')
        print()
    except pymysql.Error as e:
        print(VolumeMain_SqlName,"查询VolumeSource数据失败！")
        print(str(e))
        print()
def all_pages_img_name(url_1,HEADERS):
    '''
    获取当前套图中的标题
    '''
    global VolumeID
    global Volume2Name
    try:
        response = requests.get(url=url_1, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except UnicodeDecodeError:
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except:
        print(url_1,'获取当前套图中的标题时，html源代码抓取异常!')
    # 查找标题并简化
    try:
        img_name = re.findall('<h1>(.*?)</h1>', htmls)
        img_content = re.findall('<div class="jianjie">&nbsp;&nbsp; &nbsp;&nbsp;(.*?)</div>', htmls)
    except:
        print(url_1,'获取当前套图中的标题时，正则表达式执行异常!!')
    Volume2Name = str(img_name).strip()[2:-4]
    VolumeID = str(re.findall("\d+", Volume2Name)[0])
    return Volume2Name
    return VolumeID
def detail_pages(VolumeUrl_SqlName,page1_img_urls,url,HEADERS):
    '''
    解析多页套图中的除第一页以外的套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    ImgsID = 0
    Complete = 1
    all_pages_img_name(url,HEADERS2)

    #判断VolumeID是否存在于VolumeUrl
    VolumeID_list = []
    try:

        # 查询VolumeID数据是否存在
        sqlQuery_fetchall = " SELECT VolumeID FROM " + VolumeUrl_SqlName
        cur.execute(sqlQuery_fetchall)
        results = cur.fetchall()
        for row in results:
            row = str(row).strip()[1:-2]
            VolumeID_list.append(row)
        print()
    except pymysql.Error as e:
        print("查询VolumeUrl数据失败！")
        print(str(e))

        # 判断封面是否存在
    new_VolumeID_list = list(set(VolumeID_list))
    print('正在判断第', VolumeID, '期是否存在')
    print()
    if str(int(VolumeID)) in new_VolumeID_list:
        print("本期图册已经存在，跳过 第", VolumeID, '期')
        print()
    else:
        print('第', VolumeID, '期是新数据正在爬取写入数据库')
        try:
            for page1_img_url in page1_img_urls:
                # 拼接http
                ImgsUrl1 = str(http) +str(page1_img_url)
                # 写入数据库
                ImgsID += 1
                mysql.VolumeUrl_insertion(VolumeUrl_SqlName, VolumeID, Volume2Name, ImgsID, ImgsUrl1, Complete)
        except:
            print(VolumeUrl_SqlName,'数据库插入失败！')
        #加入格式化替换符
        a = str(url)
        b = '_{}'
        str_list = list(a)
        str_list.insert(-5, b)
        a_b = ''.join(str_list)
        url_formats = a_b
        #遍历：https://www.demo.net/Uxing/316_{}.html
        time.sleep(3)
        for x in range(1, 1000):
            url_format = url_formats.format(x)
            try:
                response = requests.get(url=url_format , headers=HEADERS)
                htmls = response.text.encode('ISO-8859-1').decode('gbk')
            except:
                print(url_format,'获取当前图册详情页中的图片时，html源代码抓取异常!')
                with open('Detail_pages_Errorlog.txt', 'a+') as file3:
                    file3.write(str(url_format)+ '获取当前图册详情页中的图片时，html源代码抓取异常!\r\n')
            # html中查找图片地址
            try:
                time.sleep(1)
                img_urls = re.findall('<img onload="size.*?" alt=".*?" src="(.*?)" /><br />',htmls)
            except:
                print(url_format, '该图册详情页图片地址未找到，抓取失败!!')
                with open('Detail_pages_Errorlog.txt', 'a+') as file4:
                    file4.write(str(url_format)+'该图册详情页图片地址未找到，抓取失败!!\r\n')

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
                    ImgsUrl2 = str(http) + str(img_url)
                    # print(imgs_url)
                    # 写入数据库
                    ImgsID += 1
                    mysql.VolumeUrl_insertion(VolumeUrl_SqlName, VolumeID, Volume2Name, ImgsID, ImgsUrl2, Complete)

def detail_page1(url,VolumeUrl_SqlName,HEADERS):
    '''
    解析多页套图中的第一页套图中的图片（由于第一页与之后的每一页都毫无规律）
    '''
    try:
        print('===当前执行页面：',url,'===')
        print()
        response = requests.get(url=url, headers=HEADERS)
        time.sleep(1.5)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except UnicodeDecodeError:
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except :
        print(url,'获取当前图册详情页中的图片时，源代码出现了新的HTML解析异常!')
        with open('Detail_pages_Errorlog.txt','a+') as file1:
            file1.write(str(url)+'获取当前图册详情页中的图片时，html源代码抓取异常!\r\n')
    # html中查找图片地址
    try:
        time.sleep(1)
        img_urls = re.findall('<img onload="size.*?" alt=".*?" src="(.*?)" /><br />',htmls)
        detail_pages(VolumeUrl_SqlName, img_urls, url, HEADERS)
    except:
        print(url,'该图册详情页图片地址未找到，抓取失败!!')
        with open('Detail_pages_Errorlog.txt','a+') as file2:
            file2.write(str(url)+'该图册详情页图片地址未找到，抓取失败!!\r\n')


def Judge_VolumeSource(url):
    '''
    解析 https://www.demo.net/XiuRen/index.html 这个多个套图页面，中的的多个套图：名称、封面、日期、地址，在通过pages解析1个套图地址中的所有图片地址、数量（由于第一页与之后的每一页都毫无规律）
    '''
    print("===== 当前执行VolumeUrl的数据插入  =====")

    if 'XiuRen' in url:
        print("当前机构： XiuRen ")
        print()
        SqlName = 'XiuRen_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MFStar' in url:
        print(" 当前机构： MFStar")
        print()
        SqlName = 'MFStar_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MiStar' in url:
        print(" 当前机构： MiStar ")
        print()
        SqlName = 'MiStar_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MyGirl' in url:
        print(" 当前机构： MyGirl   ")
        print()
        SqlName = 'MyGirl_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'IMiss' in url:
        print(" 当前机构： IMiss   ")
        print()
        SqlName = 'IMiss_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'YouWu' in url:
        print(" 当前机构： YouWu   ")
        print()
        SqlName = 'YouWu_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'FeiLin' in url:
        print(" 当前机构： FeiLin   ")
        print()
        SqlName = 'FeiLin_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MiiTao' in url:
        print(" 当前机构： MiiTao   ")
        print()
        SqlName = 'MiiTao_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'YouMi' in url:
        print(" 当前机构： YouMi   ")
        print()
        SqlName = 'YouMi_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'XiaoYu' in url:
        print(" 当前机构： XiaoYu   ")
        print()
        SqlName = 'XiaoYu_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'HuaYang' in url:
        print(" 当前机构： HuaYang   ")
        print()
        SqlName = 'HuaYang_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'XingYan' in url:
        print(" 当前机构： XingYan ")
        print()
        SqlName = 'XingYan_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'BoLoli' in url:
        print(" 当前机构： BoLoli   ")
        print()
        SqlName = 'BoLoli_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'Uxing' in url:
        print(" 当前机构： Uxing   ")
        print()
        SqlName = 'Uxing_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'WingS' in url:
        print(" 当前机构： WingS   ")
        print()
        SqlName = 'WingS_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'LeYuan' in url:
        print(" 当前机构： LeYuan   ")
        print()
        SqlName = 'LeYuan_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'Taste' in url:
        print(" 当前机构： Taste   ")
        print()
        SqlName = 'Taste_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'HuaYan' in url:
        print(" 当前机构： HuaYan   ")
        print()
        SqlName = 'HuaYan_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'DKGirl' in url:
        print(" 当前机构： DKGirl   ")
        print()
        SqlName = 'DKGirl_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'Candy' in url:
        print(" 当前机构： Candy   ")
        print()
        SqlName = 'Candy_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MintYe' in url:
        print(" 当前机构： MintYe   ")
        print()
        SqlName = 'MintYe_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'MTMeng' in url:
        print(" 当前机构： MTMeng   ")
        print()
        SqlName = 'MTMeng_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

    elif 'Micat' in url:
        print(" 当前机构： Micat   ")
        print()
        SqlName = 'Micat_VolumeUrl'
        detail_page1(url, SqlName,HEADERS)

def main():
    for VolumeMain_SqlName in VolumeMain_SqlNames:
        find_VolumeSource(VolumeMain_SqlName)
    for VolumeSource_list in VolumeSource_lists:
        Judge_VolumeSource(VolumeSource_list)
