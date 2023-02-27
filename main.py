import pages
import pages2
import datetime
import defbag
import time

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; CNZZDATA1278618868=1401620223-1614819280-%7C1614819280; ASPSESSIONIDQGRRBTRT=GJMFCFMDKHDCIBPDCNMHCCCF; __tins__20641871=%7B%22sid%22%3A%201614822574632%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201614824374632%7D; __51cke__=; __51laig__=1"}
HEADERS2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
                   "cookie":"UM_distinctid=177f889959e1a-05ecc8e5c3d2b2-7a667166-1fa400-177f889959f1c3; ASPSESSIONIDSGTRASQS=DLJPPMFBCLEOGJGELLNIGHJM; __51cke__=; CNZZDATA1278618868=1333432856-1614780575-%7C1615044272; __tins__20641871=%7B%22sid%22%3A%201615044111332%2C%20%22vd%22%3A%207%2C%20%22expires%22%3A%201615047215384%7D; __51laig__=7"}
HEADERS3 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
                   "cookie":"UM_distinctid=177fae3c73189-08aa09437f5cf4-6a53702b-1fa400-177fae3c732139; ASPSESSIONIDSGTRASQS=JELPPMFBBKBIGLFGGEOALNJP; CNZZDATA1278618868=1401620223-1614819280-%7C1615044272; __51cke__=; __tins__20641871=%7B%22sid%22%3A%201615046036960%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201615047843536%7D; __51laig__=2"}

# 当前时间
now_time = datetime.datetime.now()
#图集专栏
xiuren_url = 'https://www.demo.com/index.html'
xiuren_all_url = 'https://www.demo.com/index{}.html'
#单页面
justone_imgs_url = 'https://www.demo.com/7901.html'
#查重目录
filepath = 'imgs_urls.txt'
filepath_check = 'imgs_urls_check.txt'
#入口
if __name__ == '__main__':
    #开始统计爬取时间
    py_start_time = time.time()
    '''
    #时间戳
    with open(r'imgs_urls.txt', 'a') as f:
        f.write(str(now_time) + '\n')'''
    #主程序-专栏
    # pages.all_page1(xiuren_url,HEADERS)
    #pages.all_pages(xiuren_all_url,HEADERS)

    #主程序-单页面
    # pages2.justone_imgs(justone_imgs_url,HEADERS2,justone_imgs_url)
    # 结束爬取时间统计
    py_end_time = time.time()
    #开始统计查重时间
    check_start_time = time.time()
    #文件去重
    defbag.txt_check(filepath,filepath_check)
    # 结束爬取时间统计
    check_end_time = time.time()
    print()
    print(f"-> The running PY-time is :{py_end_time - py_start_time} s <-")
    print(f"-> The running Check-time is :{check_end_time - check_start_time} s <-")
    print(f"-> The running ALL-time is :{(py_end_time - py_start_time)+(check_end_time - check_start_time)} s <-")
