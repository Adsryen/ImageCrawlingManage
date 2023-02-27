#!/usr/bin/env python 3.8
# -*- coding: UTF-8 -*-
# @date: 2022.01.14 下午 11:46
# @name: demo2
# @author：Ads-Ryen
# @webside：www.prlrr.com
# @software: PyCharm

import requests
import re

url_1 = "https://www.demo.net/XiuRen/485_4.html"
response = requests.get(url=url_1)
try:
    htmls = response.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(response.text)[0])
except UnicodeDecodeError:
    htmls = response.text.encode('ISO-8859-1').decode('gbk')
print(htmls)
img_name = re.findall('<h1>(.*?)</h1>', htmls)
img_content = re.findall('<div class="jianjie">&nbsp;&nbsp; &nbsp;&nbsp;(.*?)</div>', htmls)
img_url = re.findall('<img onload="size.*?" alt=".*?" src="(.*?)" /><br />',htmls)
img_url32 = re.findall('<img onload="size.*?" alt=".*?" src="(.*?)">',htmls)
# img_CoverUrls = re.findall('<li class="i_list list_n2"><a  href=".*?" alt=.*? title=.*?><img class="waitpic" src=".*?" data-original="(.*?)" style="opacity:1;display:inline;" >', htmls)
# img_times = re.findall('<i class="fa fa-clock-o"></i>(.*?)<span class="cx_like">', htmls)
# img_urls = re.findall('<li class="i_list list_n2"><a  href="(.*?)" alt=.*? title=.*?><img class="waitpic" src=".*?" data-original=".*?" style="opacity:1;display:inline;" >', htmls)
#
#
# for (img_url, img_CoverUrl, img_time, Volume_name) in zip(img_urls, img_CoverUrls, img_times, Volume_names):
#     print(Volume_name,img_url, img_CoverUrl, img_time)
#     print()
#     print()


print(img_url)
# try:
#     htmls_status = re.findall('<title>(.*?)</title>', htmls)
# except:
#     print(url_1, '判断当前套图中第',x,'页的状态时，正则表达式执行异常!!')
# htmls_status_404 = str(re.findall("\d+", str(htmls_status))[0])
# if htmls_status_404=='404':
#     print('页面404，跳出循环！')