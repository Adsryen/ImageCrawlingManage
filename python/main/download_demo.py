#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.14 上午 12:21
# @name: download_demo
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm
import requests
import os
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
                   "cookie":"UM_distinctid=17d46c535b965c-01c7a2b70e3e8c-59191353-1fa400-17d46c535baa30; __51cke__=; ASPSESSIONIDSEBBCCRT=ELFIJOMCPJGKCBGEHAEALMJP; CNZZDATA1278618868=75858223-1637567128-|1641918126; ASPSESSIONIDSABBCCRT=BKPJJOMCGCDGBBMPLMHLBOIO; __51laig__=10"}
url1 = 'https://www.demo.net'
url2 = '/UploadFile/pic/9899.jpg'
#
#将文件路径分割出来
url3 = '.'+ url2
url4 = '.'+ os.path.split(url2)[0]
name = os.path.split(url2)[1]
#判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
if not os.path.isdir(url4):
    os.makedirs(url4)
    print('新文件夹，执行创建！')

#然后再判断文件是否存在，如果不存在，则创建
if not os.path.exists(url3):
    try:
        response = requests.get(url=url1+url2, headers=HEADERS)
        with open(url3, 'wb') as fd:
            for chunk in response.iter_content():
                fd.write(chunk)
        print(name,'保存成功！')
    except:
        print(url1+url2,'保存失败！')