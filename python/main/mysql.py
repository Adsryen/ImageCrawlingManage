#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.10 下午 10:12
# @name: mysql
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm

# 导入pymysql模块
import pymysql
# 连接database
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}

mysql_1 = {
    "name":"HUAWEI-MY-xiuren",
    "host":"122.9.153.176",
    "user":"xiuren",
    "password":"6sfitTyZJdFFzYYP",
    "database":"xiuren"
}
http = "https://www.demo.net"
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

def creation():
    '''
    两张示例表 ：XiuRen_VolumeMain   XiuRen_VolumeUrl
    XiuRen_VolumeMain ：VolumeID(第几期)     Volume1Name(图册第一个长名称)    CoverUrl(封面：ImgsID第一张)   VolumeTime(图册发布时间)  VolumeSource(图册在网页的源地址)     VolumeCount(图册的数量)
    XiuRen_VolumeUrl ：VolumeID(第几期)     Volume2Name(图册第二个短名称)    ImgsID(第几张)        ImgsUrl(单张图片url)    Complete(图册是否完整  0未完  1完整)
    '''
    try:
        #创建每一个图册的第一个主展示数据库
        cur.execute('DROP TABLE IF EXISTS XiuRen_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MFStar_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MiStar_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MyGirl_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS IMiss_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS YouWu_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS FeiLin_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MiiTao_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS YouMi_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS XiaoYu_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS HuaYang_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS XingYan_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS BoLoli_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS Uxing_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS WingS_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS LeYuan_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS Taste_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS HuaYan_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS DKGirl_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS Candy_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MintYe_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS MTMeng_VolumeMain')
        cur.execute('DROP TABLE IF EXISTS Micat_VolumeMain')
        #创建每一个图册的第二个详情照片数据库
        cur.execute('DROP TABLE IF EXISTS XiuRen_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MFStar_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MiStar_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MyGirl_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS IMiss_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS YouWu_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS FeiLin_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MiiTao_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS YouMi_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS XiaoYu_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS HuaYang_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS XingYan_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS BoLoli_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS Uxing_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS WingS_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS LeYuan_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS Taste_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS HuaYan_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS DKGirl_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS Candy_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MintYe_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS MTMeng_VolumeUrl')
        cur.execute('DROP TABLE IF EXISTS Micat_VolumeUrl')
        #修改每一个图册的第一个主展示数据库的字段、数据类型、主键、注释
        One_sqlQuery_1 = "CREATE TABLE XiuRen_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_2 = "CREATE TABLE MFStar_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_3 = "CREATE TABLE MiStar_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_4 = "CREATE TABLE MyGirl_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_5 = "CREATE TABLE IMiss_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_6 = "CREATE TABLE YouWu_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_7 = "CREATE TABLE FeiLin_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_8 = "CREATE TABLE MiiTao_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_9 = "CREATE TABLE YouMi_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_10 = "CREATE TABLE XiaoYu_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_11 = "CREATE TABLE HuaYang_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_12 = "CREATE TABLE XingYan_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_13 = "CREATE TABLE BoLoli_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_14 = "CREATE TABLE Uxing_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_15 = "CREATE TABLE WingS_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_16 = "CREATE TABLE LeYuan_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_17 = "CREATE TABLE Taste_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_18 = "CREATE TABLE HuaYan_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_19 = "CREATE TABLE DKGirl_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_20 = "CREATE TABLE Candy_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_21 = "CREATE TABLE MintYe_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_22 = "CREATE TABLE MTMeng_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        One_sqlQuery_23 = "CREATE TABLE Micat_VolumeMain(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        #修改每一个图册的第二个详情照片数据库的字段、数据类型、主键、注释
        Two_sqlQuery_1 = "CREATE TABLE XiuRen_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_2 = "CREATE TABLE MFStar_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_3 = "CREATE TABLE MiStar_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_4 = "CREATE TABLE MyGirl_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_5 = "CREATE TABLE IMiss_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_6 = "CREATE TABLE YouWu_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_7 = "CREATE TABLE FeiLin_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_8 = "CREATE TABLE MiiTao_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_9 = "CREATE TABLE YouMi_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_10 = "CREATE TABLE XiaoYu_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_11 = "CREATE TABLE HuaYang_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_12 = "CREATE TABLE XingYan_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_13 = "CREATE TABLE BoLoli_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_14 = "CREATE TABLE Uxing_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_15 = "CREATE TABLE WingS_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_16 = "CREATE TABLE LeYuan_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_17 = "CREATE TABLE Taste_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_18 = "CREATE TABLE HuaYan_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_19 = "CREATE TABLE DKGirl_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_20 = "CREATE TABLE Candy_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_21 = "CREATE TABLE MintYe_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_22 = "CREATE TABLE MTMeng_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        Two_sqlQuery_23 = "CREATE TABLE Micat_VolumeUrl(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        # 执行第一个主展示数据库的修改
        cur.execute(One_sqlQuery_1)
        cur.execute(One_sqlQuery_2)
        cur.execute(One_sqlQuery_3)
        cur.execute(One_sqlQuery_4)
        cur.execute(One_sqlQuery_5)
        cur.execute(One_sqlQuery_6)
        cur.execute(One_sqlQuery_7)
        cur.execute(One_sqlQuery_8)
        cur.execute(One_sqlQuery_9)
        cur.execute(One_sqlQuery_10)
        cur.execute(One_sqlQuery_11)
        cur.execute(One_sqlQuery_12)
        cur.execute(One_sqlQuery_13)
        cur.execute(One_sqlQuery_14)
        cur.execute(One_sqlQuery_15)
        cur.execute(One_sqlQuery_16)
        cur.execute(One_sqlQuery_17)
        cur.execute(One_sqlQuery_18)
        cur.execute(One_sqlQuery_19)
        cur.execute(One_sqlQuery_20)
        cur.execute(One_sqlQuery_21)
        cur.execute(One_sqlQuery_22)
        cur.execute(One_sqlQuery_23)
        # 执行第二个详情照片数据库的修改
        cur.execute(Two_sqlQuery_1)
        cur.execute(Two_sqlQuery_2)
        cur.execute(Two_sqlQuery_3)
        cur.execute(Two_sqlQuery_4)
        cur.execute(Two_sqlQuery_5)
        cur.execute(Two_sqlQuery_6)
        cur.execute(Two_sqlQuery_7)
        cur.execute(Two_sqlQuery_8)
        cur.execute(Two_sqlQuery_9)
        cur.execute(Two_sqlQuery_10)
        cur.execute(Two_sqlQuery_11)
        cur.execute(Two_sqlQuery_12)
        cur.execute(Two_sqlQuery_13)
        cur.execute(Two_sqlQuery_14)
        cur.execute(Two_sqlQuery_15)
        cur.execute(Two_sqlQuery_16)
        cur.execute(Two_sqlQuery_17)
        cur.execute(Two_sqlQuery_18)
        cur.execute(Two_sqlQuery_19)
        cur.execute(Two_sqlQuery_20)
        cur.execute(Two_sqlQuery_21)
        cur.execute(Two_sqlQuery_22)
        cur.execute(Two_sqlQuery_23)
        print("表格创建成功！")
        print()

    except pymysql.Error as e:
        print("======= 表格创建失败：=======")
        print(str(e))
        print("==========================")

def VolumeMain_insertion(SqlName,VolumeID, Volume1Name, CoverUrl, VolumeTime, VolumeSource, VolumeCount):
    '''
    当前表 ：XiuRen_VolumeMain
    XiuRen_VolumeMain ：VolumeID(第几期)     Volume1Name(图册第一个长名称)    CoverUrl(封面：ImgsID第一张)   VolumeTime(图册发布时间)  VolumeSource(图册在网页的源地址)   VolumeCount(图册的数量)
    '''
    VolumeID_list = []
    VolumeTime_str = '更新:'
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
        print("查询CoverUrl数据失败！")
        print(str(e))

    #判断封面是否存在
    print('判断第',VolumeID,'是否存在')
    if str(int(VolumeID)) in VolumeID_list:
        print("本期图册已经存在，跳过 第",VolumeID,'期')

    else:

        try:
            VolumeTime = str(VolumeTime_str) + str(VolumeTime)
            sqlQuery = " INSERT INTO " + SqlName +" (VolumeID ,Volume1Name ,CoverUrl ,VolumeTime ,VolumeSource,VolumeCount) VALUE (%s,%s,%s,%s,%s,%s) "
            value = (VolumeID, Volume1Name, CoverUrl,VolumeTime,VolumeSource,VolumeCount)
            cur.execute(sqlQuery, value)
            conn.commit()
            VolumeID_list.clear()
            print("表格 ",SqlName," 插入成功！")
            print("Volume1Name 名称:",Volume1Name)
            print("CoverUrl    封面:",CoverUrl)
            print("VolumeTime  时间:",VolumeTime)
            print("VolumeCount 数量:",VolumeCount)
            print()
        except pymysql.Error as e:
            print("===== 表格 ",SqlName," 插入失败 ： =====")
            print(str(e))
            print("=====================================")

def VolumeUrl_insertion(SqlName, VolumeID, Volume2Name, ImgsID, ImgsUrl, Complete):
    '''
    当前表 ：XiuRen_VolumeUrl
    XiuRen_VolumeUrl ：VolumeID(第几期)     Volume2Name(图册第二个短名称)    ImgsID(第几张)        ImgsUrl(单张图片url)    Complete(图册是否完整  0未完  1完整)
    '''
    try:
        sqlQuery = " INSERT INTO " + SqlName +"  (VolumeID, Volume2Name, ImgsID, ImgsUrl, Complete) VALUE (%s,%s,%s,%s,%s) "
        value = (VolumeID ,Volume2Name, ImgsID, ImgsUrl, Complete)
        cur.execute(sqlQuery, value)
        conn.commit()
        print("表格 ",SqlName," 插入成功！",ImgsID ,'  ', Volume2Name,'  ',ImgsUrl)
        print()
    except pymysql.Error as e:
        print("===== 表格 ",SqlName," 插入失败 ： ",ImgsID ,'  ', Volume2Name,'  ',ImgsUrl,"=====")
        print(str(e))
        print("====================================")

def close():
    # 关闭光标对象
    cur.close()
    # 关闭数据库连接
    conn.close()
    print("========== 数据库连接已断开 ==========")

