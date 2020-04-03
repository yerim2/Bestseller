#-*- coding:utf-8 -*-
# Link : https://www.aladin.co.kr/shop/common/wbest_excel.aspx?BestType=Bestseller&BranchType=1&CID=351&Year=2020&Month=3&Week=5 
# Link : https://www.aladin.co.kr/shop/common/wbest_excel.aspx?BestType=Bestseller&BranchType=1&CID=351&Year="+now.strftime('%Y')+"&Month="+now.strftime('%m')+"&Week=5"
# 컴퓨터, 모바일 분야 베스트셀러, 스케줄러를 1주일에 한번, 매주 월요일마다

from requests import get
import datetime
import pandas as pd

now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
csv_name = today+"_Bestseller.csv"  #실행 날짜로 파일 이름 지정
url = "https://www.aladin.co.kr/shop/common/wbest_excel.aspx?BestType=Bestseller&BranchType=1&CID=351&Year=2020&Month=3&Week=5 "

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
        
if __name__ =='__main__':
    download(url,csv_name) 

data = pd.read_csv(csv_name, encoding='CP949')
data['ISBN13'] = data['ISBN13'].astype(str)
data.head()
