import urllib.request
import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random
import xlrd


def spider(directory=dir, filename=filename):
    data = xlrd.open_workbook(r'dir/filename.xlsx') # 打开保存所需公司名称的xls文件
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    files = []
    for i in range(nrows): # 循环逐行打印
        if i == 0:
            continue
        f  = table.row_values(i)[1].strip().replace('*', '')
        files.append(f)

    headers = {'User-Agent': 'Chrome'}
    count = 0
    for f in files:
        print('\n.............searching for '+f+'...............\n')
        url = 'http://ipo.csrc.gov.cn/searchInSite.action' #爬取网页
        ua =  UserAgent()
        headers['User-Agent'] = ua.random
        data = {'ipoName': f}
        r = requests.post(url=url, data=data, headers=headers)
        print(r.status_code)
        s = etree.HTML(r.text)
        firm = s.xpath('//tr[@class="iponameborder"]/td[1]/text()')
        if len(firm) != 0:
            #下载相应的PDF文件
            firm[0] = firm[0].strip()
            pdf = s.xpath('//tr[@class="iponameborder"]/td[6]/a/@href')
            local = '[SOME PATH]/{}.pdf'.format(firm[0])
            pdflink = 'http://ipo.csrc.gov.cn/' + pdf[0]
            urllib.request.urlretrieve(pdflink, local)
            count = count + 1
            print(str(count) + ': ' + firm[0] + '.pdf has been stored.')


        time.sleep(random.random()*10)
    pass
