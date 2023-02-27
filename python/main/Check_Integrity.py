#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.16 上午 12:09
# @name: Check_Integrity
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm
#检查VolumeUrl数据库单个VolumeID的imgsid数量是否符合 VolumeMain表中的VolumeCount数量
import pymysql

mysql_1 = {
    "name":"HUAWEI-MY-xiuren",
    "host":"122.9.153.176",
    "user":"xiuren",
    "password":"6sfitTyZJdFFzYYP",
    "database":"xiuren"
}
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
VolumeUrl_SqlNames = [
    'XiuRen_VolumeUrl',
    'MFStar_VolumeUrl',
    'MiStar_VolumeUrl',
    'MyGirl_VolumeUrl',
    'IMiss_VolumeUrl',
    'YouWu_VolumeUrl',
    'FeiLin_VolumeUrl',
    'MiiTao_VolumeUrl',
    'YouMi_VolumeUrl',
    'XiaoYu_VolumeUrl',
    'HuaYang_VolumeUrl',
    'XingYan_VolumeUrl',
    'BoLoli_VolumeUrl',
    'Uxing_VolumeUrl',
    'WingS_VolumeUrl',
    'LeYuan_VolumeUrl',
    'Taste_VolumeUrl',
    'HuaYan_VolumeUrl',
    'DKGirl_VolumeUrl',
    'Candy_VolumeUrl',
    'MintYe_VolumeUrl',
    'MTMeng_VolumeUrl',
    'Micat_VolumeUrl'
]



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

def Get_VolumeCount(SqlName):
    VolumeID_list = []
    try:
        # 查询VolumeID数据是否存在
        sqlQuery_fetchall = " SELECT VolumeID VolumeCount FROM " + SqlName
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
        pass

if __name__ == '__main__':
    for VolumeMain_SqlName in VolumeMain_SqlNames:
        Get_VolumeCount(VolumeMain_SqlName)