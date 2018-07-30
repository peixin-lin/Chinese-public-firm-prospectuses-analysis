#Extract birthday information from text files
import urllib
import re
import os
import pandas as pd
import xlrd
import xlutils.copy


def info_extracter(dir=dir, result_path=res_path):
	dir = dir #保存招股说明书txt文件的文件夹
	filename_list=os.listdir(dir) #将该文件夹中所有文件名存入一个list
	birth = []
	firm = []
	for j in filename_list: #遍历所有文件
	    txt = os.path.join(dir, j)
	    with open(txt, 'r', encoding='utf8') as f: #打开一个txt文件
	        #匹配文本中的出生日期
	        text = f.read().replace('\n', '').replace(' ','')
	        year = re.findall(r"\d{4}年\d{2}月\d{2}日出生", text)
	        if len(year) == 0:
	            year = re.findall(r"\d{4}年\d{2}月出生", text)
	            if len(year) == 0:
	                year = re.findall(r"\d{4}年出生", text)
	                if len(year) == 0:
	                    year = re.findall(r"\d{4}年\d{2}月\d{2}日生", text)
	                    if len(year) == 0:
	                        year = re.findall(r"\d{4}年\d{2}月生", text)
	                        if len(year) == 0:
	                            year = re.findall(r"\d{4}年生", text)
	                            if len(year) == 0:
	                                year = re.findall(r"出生于\d{4}年", text)
	                                if len(year) == 0:
	                                    year = re.findall(r"出生于\d{4}年\d{2}月", text)
	                                    if len(year) == 0:
	                                        year = re.findall(r"出生于\d{4}年\d{2}月\d{2}日", text)
	                                        if len(year) == 0:
	                                            year = ['lost'] #若以上规则均匹配不到，则定义为"lost"

	        birth.append(year[0])
	        firm.append(j.replace('.txt', ''))
	        print(j+': '+year[0])
	age = []
	#统一格式成为两个数字表示年代，如：“1964年”改为“60”。
	for x in birth:
	    if x != 'lost':
	        temp = re.findall("19(.+?)年", x)
	        if len(temp) == 0:
	            age.append('lost')
	        else:
	            cvt = temp[0]
	            cvt = cvt[0]+'0'
	            age.append(cvt)
	    else:
	        age.append('lost')

	result = {'firm': firm, 'age': age} #将结果存入一个字典
	df = pd.DataFrame(result)
	df.to_excel(r'res_path/result.xlsx') #保存为Excel文件
	pass