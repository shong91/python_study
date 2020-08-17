import csv
import requests
from bs4 import BeautifulSoup

# 코스피 시가 총액 순위를 가져와 csv 파일로 저장하기

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "시가총액1-200.csv"

# 엑셀파일에서 열 때 한글깨짐 문제 encoding 설정
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline 설정하지 않을 시 엔터가 하나 더 들어가게 됨 
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows:
        columns = row.find_all("td")
        # 줄바꿈 등 의미없는 데이터는 skip
        if len(columns) <= 1:
            continue
        
        # 불필요한 공백 등은 strip() 으로 trim 함
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)


