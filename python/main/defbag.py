from lxml import etree
import requests
import re
import time
import os
import urllib . request
import chardet

#对保存的文本文件进行查重
def txt_check(oldfile,newfile):
    count1 = len(open(oldfile, 'r').readlines())

    with open(oldfile) as file1:
        tmp = file1.read().splitlines()
        tmp1 = set(tmp)  # 利用内置的列表去重方法工作
        tmp2 = [tmp + "\n" for tmp in tmp1]  # 给每一行的结尾加一个换行符
        count2 = len(tmp2)
    if count1 != count2:
        with open(newfile, 'w') as file2:
            file2.writelines(tmp2)
        print('success：查重完成--共计' + str(count1) + '项' + '去除' + str(count1 - count2) + '个重复项,' + '剩余有效' + str(count2) + '项')
    else:
        print('success：查重完成--共计' + str(count1) + '项,无重复项')

#查看url编码
def urlencode(url):
    a = urllib.request.urlopen(url)
    encode = chardet.detect(a.read())
    print(encode['encoding'])

#查看字符串编码
def strencode(strs):
    s = strs
    print(chardet.detect(str.encode(s)))

#保存图片
def save_imgs(img_url,htmls,HEADERS):
    #文件夹名
    dir_name = re.findall('<td.*?><div class=title>(.*)', htmls)
    dir_name_strip = str(dir_name).strip()[2:-4]
    #判定文件夹是否存在
    if not os.path.exists(dir_name_strip):
        os.mkdir(dir_name_strip)
    #图片名字
    img_name = img_url.split('/')[-1]
    #保存图片
    response = requests.get(img_url,headers=HEADERS)
    with open(dir_name_strip + '/' + img_name,'wb') as f:
        f.write(response.content)

#保存链接到目录下
def save_imgs_urls(imgs_urls):
    filepath = 'imgs_urls.txt'
    filepath_check = 'sexy.txt'
    with open(filepath, 'a') as f:
        f.write( imgs_urls + '\n')

#保存链接到api文件
def save_imgs_urls_API(imgs_urls):
    with open(r'E:\GitHub Desktop\GitHub\Pictruebed-API\php-api\sexy.txt', 'a') as f:
        f.write( imgs_urls + '\n')

