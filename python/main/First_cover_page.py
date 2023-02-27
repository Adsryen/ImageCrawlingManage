#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.13 下午 8:51
# @name: First_cover_page
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm

import os
import requests
import re
import datetime
import defbag
import mysql
import pymysql
import Second_detail_page
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}
#全局变量
now_time = datetime.datetime.now()
http = "https://www.demo.net"

mysql_1 = {
    "name":"HUAWEI-MY-xiuren",
    "host":"122.9.153.176",
    "user":"xiuren",
    "password":"6sfitTyZJdFFzYYP",
    "database":"xiuren"
}

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

def all_page1_mysql(url,SqlName,HEADERS):
    '''
    解析 https://www.demo.net/XiuRen/index.html 这个多个套图页面，中的的多个套图：名称、封面、日期、地址，最后执行保存并写入的程序
    '''
    everyday_pamphlets_VolumeSource = []
    try:
        response = requests.get(url=url, headers=HEADERS)
        htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
    except UnicodeDecodeError:
        htmls = response.text.encode('ISO-8859-1').decode('gbk')
    except:
        print(url, '页面抓取无效或加载异常')
    # html中查找图片地址
    Volume_names = re.findall('<li class="i_list list_n2"><a  href=".*?" alt=(.*?) title=.*?><img class="waitpic" src=".*?" data-original=".*?" style="opacity:1;display:inline;" >',htmls)
    img_CoverUrls = re.findall('<li class="i_list list_n2"><a  href=".*?" alt=.*? title=.*?><img class="waitpic" src=".*?" data-original="(.*?)" style="opacity:1;display:inline;" >',htmls)
    img_times = re.findall('<i class="fa fa-clock-o"></i>(.*?)<span class="cx_like">',htmls)
    img_urls = re.findall('<li class="i_list list_n2"><a  href="(.*?)" alt=.*? title=.*?><img class="waitpic" src=".*?" data-original=".*?" style="opacity:1;display:inline;" >',htmls)
    http = "https://www.demo.net"
    for (img_url, img_CoverUrl, img_time, Volume_name) in zip(img_urls, img_CoverUrls, img_times, Volume_names):
        # 拼接http
        VolumeSource = http + str(img_url)
        # 数据库变量
        # CoverUrl = 'https://sexy.prlrr.com'+ str(img_CoverUrl)
        CoverUrl = str(http) + str(img_CoverUrl)
        Volume1Name = str(Volume_name).strip()
        VolumeID = str(re.findall("\d+", Volume1Name)[0])
        VolumeCount = str(re.findall("\d+", Volume1Name)[-1])
        # 保存文件
        # download_pic(http, img_CoverUrl)
        # 日常更新判断VolumeID是否存在
        VolumeID_list = []
        try:
            # 查询VolumeID数据是否存在
            sqlQuery_fetchall = " SELECT VolumeID FROM " + SqlName
            cur.execute(sqlQuery_fetchall)
            results = cur.fetchall()

            for row in results:
                row = str(row).strip()[1:-2]
                VolumeID_list.append(row)
            print()
        except pymysql.Error as e:
            print("查询VolumeID数据失败！")
            print(str(e))

        # 判断封面是否存在
        print('判断第', VolumeID, '是否存在')
        if str(int(VolumeID)) in VolumeID_list:
            print("本期图册已经存在，跳过 第", VolumeID, '期')
            for everyday_pamphlets_VolumeSource1 in everyday_pamphlets_VolumeSource:
                Second_detail_page.Judge_VolumeSource(everyday_pamphlets_VolumeSource1)
            break
        else:
            # 保存每日更新的图册源地址
            everyday_pamphlets_VolumeSource.append(VolumeSource)
        # 写入数据库
        mysql.VolumeMain_insertion(SqlName, VolumeID, Volume1Name, CoverUrl, img_time, VolumeSource, VolumeCount)

def all_pages_mysql(url, SqlName,HEADERS):
    for x in range(2, 300):
        get_url = url.format(x)
        try:
            response = requests.get(url=get_url, headers=HEADERS)
            htmls = response.text.encode('ISO-8859-1').decode(
                requests.utils.get_encodings_from_content(response.text)[0])
        except UnicodeDecodeError:
            htmls = response.text.encode('ISO-8859-1').decode('gbk')
        except:
            print(url, '页面抓取无效或加载异常')
        # html中查找图片地址
        img_urls = re.findall('<div class="dan"><a href=(.*?) target=.*? title=.*? alt=.*?>', htmls)
        Volume_names = re.findall('<div class="dan"><a href=.*? target=.*? title=(.*?) alt=.*?>', htmls)
        img_CoverUrls = re.findall('<img src="(.*?)"border=0>', htmls)
        img_times = re.findall('<font style="font-size:12px;">(更新:.*?)&nbsp;&nbsp;浏览:.*?</font></b></a></div>', htmls)
        http = "https://www.demo.net"
        for (img_url, img_CoverUrl, Volume_name, img_time) in zip(img_urls, img_CoverUrls, Volume_names, img_times):
            # 拼接http
            all_page1_imgs = str(http) + str(img_url)
            # 数据库变量
            # CoverUrl = 'https://sexy.prlrr.com'+ str(img_CoverUrl)
            CoverUrl = str(http) + str(img_CoverUrl)
            Volume1Name = str(Volume_name).strip()
            VolumeID = str(re.findall("\d+", Volume1Name)[0])
            VolumeCount = str(re.findall("\d+", Volume1Name)[-1]).strip()
            # 保存文件
            # download_pic(http, img_CoverUrl)
            # 写入数据库
            mysql.VolumeMain_insertion(SqlName, VolumeID, Volume1Name, CoverUrl, img_time, all_page1_imgs, VolumeCount)

def all_page1(url, HEADERS):
    '''
    解析 https://www.demo.net/XiuRen/index.html 这个多个套图页面，中的的多个套图：名称、封面、日期、地址，在通过pages解析1个套图地址中的所有图片地址、数量（由于第一页与之后的每一页都毫无规律）
    '''
    print("===== 当前执行第一页封面页面 =====")
    if 'XiuRen' in url:
        print("当前机构： XiuRen ")
        print()
        SqlName = 'XiuRen_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MFStar' in url:
        print(" 当前机构： MFStar")
        print()
        SqlName = 'MFStar_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MiStar' in url:
        print(" 当前机构： MiStar ")
        print()
        SqlName = 'MiStar_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MyGirl' in url:
        print(" 当前机构： MyGirl   ")
        print()
        SqlName = 'MyGirl_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'IMiss' in url:
        print(" 当前机构： IMiss   ")
        print()
        SqlName = 'IMiss_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'YouWu' in url:
        print(" 当前机构： YouWu   ")
        print()
        SqlName = 'YouWu_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'FeiLin' in url:
        print(" 当前机构： FeiLin   ")
        print()
        SqlName = 'FeiLin_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MiiTao' in url:
        print(" 当前机构： MiiTao   ")
        print()
        SqlName = 'MiiTao_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'YouMi' in url:
        print(" 当前机构： YouMi   ")
        print()
        SqlName = 'YouMi_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'XiaoYu' in url:
        print(" 当前机构： XiaoYu   ")
        print()
        SqlName = 'XiaoYu_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'HuaYang' in url:
        print(" 当前机构： HuaYang   ")
        print()
        SqlName = 'HuaYang_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'XingYan' in url:
        print(" 当前机构： XingYan ")
        print()
        SqlName = 'XingYan_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'BoLoli' in url:
        print(" 当前机构： BoLoli   ")
        print()
        SqlName = 'BoLoli_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'Uxing' in url:
        print(" 当前机构： Uxing   ")
        print()
        SqlName = 'Uxing_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'WingS' in url:
        print(" 当前机构： WingS   ")
        print()
        SqlName = 'WingS_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'LeYuan' in url:
        print(" 当前机构： LeYuan   ")
        print()
        SqlName = 'LeYuan_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'Taste' in url:
        print(" 当前机构： Taste   ")
        print()
        SqlName = 'Taste_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'HuaYan' in url:
        print(" 当前机构： HuaYan   ")
        print()
        SqlName = 'HuaYan_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'DKGirl' in url:
        print(" 当前机构： DKGirl   ")
        print()
        SqlName = 'DKGirl_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'Candy' in url:
        print(" 当前机构： Candy   ")
        print()
        SqlName = 'Candy_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MintYe' in url:
        print(" 当前机构： MintYe   ")
        print()
        SqlName = 'MintYe_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'MTMeng' in url:
        print(" 当前机构： MTMeng   ")
        print()
        SqlName = 'MTMeng_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

    elif 'Micat' in url:
        print(" 当前机构： Micat   ")
        print()
        SqlName = 'Micat_VolumeMain'
        all_page1_mysql(url, SqlName,HEADERS)

def all_pages(url, HEADERS):
    '''
    解析多个单页套图中，除去第一页单页套图外，剩余的多个套图地址，在通过pages解析单个套图地址中的图片地址（由于第一页与之后的每一页都毫无规律）
    '''
    print("===== 当前执行除第一页外的封面页面 =====")

    if 'XiuRen' in url:
        print(" 当前机构： XiuRen")
        print()
        SqlName = 'XiuRen_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MFStar' in url:
        print(" 当前机构： MFStar")
        print()
        SqlName = 'MFStar_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MiStar' in url:
        print(" 当前机构： MiStar ")
        print()
        SqlName = 'MiStar_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MyGirl' in url:
        print(" 当前机构： MyGirl   ")
        print()
        SqlName = 'MyGirl_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'IMiss' in url:
        print(" 当前机构： IMiss   ")
        print()
        SqlName = 'IMiss_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'YouWu' in url:
        print(" 当前机构： YouWu   ")
        print()
        SqlName = 'YouWu_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'FeiLin' in url:
        print(" 当前机构： FeiLin   ")
        print()
        SqlName = 'FeiLin_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MiiTao' in url:
        print(" 当前机构： MiiTao   ")
        print()
        SqlName = 'MiiTao_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'YouMi' in url:
        print(" 当前机构： YouMi   ")
        print()
        SqlName = 'YouMi_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'XiaoYu' in url:
        print(" 当前机构： XiaoYu   ")
        print()
        SqlName = 'XiaoYu_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'HuaYang' in url:
        print(" 当前机构： HuaYang   ")
        print()
        SqlName = 'HuaYang_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'XingYan' in url:
        print(" 当前机构： XingYan ")
        print()
        SqlName = 'XingYan_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'BoLoli' in url:
        print(" 当前机构： BoLoli   ")
        print()
        SqlName = 'BoLoli_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'Uxing' in url:
        print(" 当前机构： Uxing   ")
        print()
        SqlName = 'Uxing_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'WingS' in url:
        print(" 当前机构： WingS   ")
        print()
        SqlName = 'WingS_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'LeYuan' in url:
        print(" 当前机构： LeYuan   ")
        print()
        SqlName = 'LeYuan_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'Taste' in url:
        print(" 当前机构： Taste   ")
        print()
        SqlName = 'Taste_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'HuaYan' in url:
        print(" 当前机构： HuaYan   ")
        print()
        SqlName = 'HuaYan_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'DKGirl' in url:
        print(" 当前机构： DKGirl   ")
        print()
        SqlName = 'DKGirl_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'Candy' in url:
        print(" 当前机构： Candy   ")
        print()
        SqlName = 'Candy_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MintYe' in url:
        print(" 当前机构： MintYe   ")
        print()
        SqlName = 'MintYe_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'MTMeng' in url:
        print(" 当前机构： MTMeng   ")
        print()
        SqlName = 'MTMeng_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)

    elif 'Micat' in url:
        print(" 当前机构： Micat   ")
        print()
        SqlName = 'Micat_VolumeMain'
        all_pages_mysql(url, SqlName, HEADERS)
