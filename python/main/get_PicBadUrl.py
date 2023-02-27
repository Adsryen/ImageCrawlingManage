#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2021.10.14 下午 11:56
# @name: get_PicBadUrl
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm
import requests
import re
url = 'https://www.demo.cc/'
ResponseHtml = requests.get(url).text.encode('ISO-8859-1').decode('gbk')
thrift = requests.get()
print()
Pic1 = re.findall('',ResponseHtml)