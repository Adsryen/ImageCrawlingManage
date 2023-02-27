import os

one_file_path = r'E:\OneDrive\python\demo-py\main\imgs_urls.txt'
two_file_path = r'E:\OneDrive\python\demo-py\plugin\imgs_urls.txt'

lines = open(two_file_path, 'r').readlines()
for line in lines:
    # print(line)
    with open(one_file_path,'a+') as f:
        f.writelines(line)

f.close()

count1 = len(open(r'E:\OneDrive\python\demo-py\main\imgs_urls.txt', 'r').readlines())

with open(r'E:\OneDrive\python\demo-py\main\imgs_urls.txt') as file1:
    tmp = file1.read().splitlines()
    tmp1 = set(tmp)#利用内置的列表去重方法工作
    tmp2 = [tmp + "\n" for tmp in tmp1]#给每一行的结尾加一个换行符
    count2 = len(tmp2)
if count1!=count2:
    with open(r'E:\OneDrive\python\demo-py\main\sexy.txt', 'w') as file2:
        file2.writelines(tmp2)
    print('success：查重完成--共计' + str(count1) + '项'+ '去除' + str(count1 - count2) + '个重复项,'+'剩余有效'+ str(count2) + '项')
else:
    print('success：查重完成--共计' + str(count1) + '项,无重复项')

if os.path.exists(two_file_path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(two_file_path)