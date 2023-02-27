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

def creation():
    '''
    两张示例表 ：XiuRen_VolumeMain   XiuRen_VolumeUrl
    XiuRen_VolumeMain ：VolumeID(第几期)     Volume1Name(图册第一个长名称)    CoverUrl(封面：ImgsID第一张)   VolumeTime(图册发布时间)  VolumeSource(图册在网页的源地址)     VolumeCount(图册的数量)
    XiuRen_VolumeUrl ：VolumeID(第几期)     Volume2Name(图册第二个短名称)    ImgsID(第几张)        ImgsUrl(单张图片url)    Complete(图册是否完整  0未完  1完整)
    '''
    try:
        cur.execute('DROP TABLE IF EXISTS XiuRen_VolumeMain1')
        cur.execute('DROP TABLE IF EXISTS MFStar_VolumeMain1')
        cur.execute('DROP TABLE IF EXISTS XiuRen_VolumeUrl1')
        cur.execute('DROP TABLE IF EXISTS MFStar_VolumeUrl1')
        sqlQuery = "CREATE TABLE XiuRen_VolumeMain1(VolumeID int COMMENT \'第几期\',Volume1Name VARCHAR(200) NOT NULL COMMENT \'第一个长名称\',CoverUrl VARCHAR(200) COMMENT \'封面地址\',VolumeTime VARCHAR(100) COMMENT \'图册更新的时间\',VolumeSource VARCHAR(200) NOT NULL COMMENT \'爬取当前这一期的图册源地址\',VolumeCount int COMMENT \'图册的照片数量\',PRIMARY KEY(VolumeID , CoverUrl))"
        sqlQuery2 = "CREATE TABLE XiuRen_VolumeUrl1(VolumeID int COMMENT \'第几期\',Volume2Name VARCHAR(200) NOT NULL COMMENT \'第二个短名称\',ImgsID int COMMENT \'当前图册的第几张图片\',ImgsUrl VARCHAR(200) PRIMARY KEY COMMENT \'该照片的地址\',Complete int COMMENT \'是否完成\') "
        cur.execute(sqlQuery)
        cur.execute(sqlQuery2)
        print("表格创建成功！")
        print()

    except pymysql.Error as e:
        print("===== 表格创建失败 ：" + str(e)+' =====')
        print()
def VolumeUrl_insertion(SqlName, VolumeID):
    '''
    当前表 ：XiuRen_VolumeUrl
    XiuRen_VolumeUrl ：VolumeID(第几期)     Volume2Name(图册第二个短名称)    ImgsID(第几张)        ImgsUrl(单张图片url)    Complete(图册是否完整  0未完  1完整)
    '''
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
        print("查询VolumeUrl数据失败！")
        print(str(e))

    # 判断封面是否存在
    new_VolumeID_list = list(set(VolumeID_list))
    print(new_VolumeID_list)

    print('判断第', VolumeID, '期是否存在')
    if str(int(VolumeID)) in new_VolumeID_list:
        print("本期图册已经存在，跳过 第", VolumeID, '期')
    else:
        print("不存在")
if __name__ == '__main__':
    SqlName = 'XiuRen_VolumeUrl'
    VolumeID = '0010'
    # print (type(VolumeID))
    connect()
    VolumeUrl_insertion(SqlName, VolumeID)