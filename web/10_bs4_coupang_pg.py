import requests
import re
from bs4 import BeautifulSoup

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

    for item in items:
        ad_badge = item.find('span', attrs={'class': 'ad-badge-text'})
        name = item.find('div', attrs={'class': 'name'}).get_text()
        price = item.find('strong', attrs={'class': 'price-value'}).get_text()
        rate = item.find('em', attrs={'class': 'rating'})
        rate_cnt = item.find('span', attrs={'class': 'rating-total-count'})
        link = item.find('a', attrs={'class': 'search-product-link'})['href']
        
        # 광고 제품은 제외
        if ad_badge:
            continue
        
        # Apple 사의 제품은 제외
        if "Apple" in name:
            continue
        
        # 리뷰 100건 이상, 평점 4.5 이상만 조회
        if rate or rate_cnt:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()[1: -1] # 슬라이싱
        else:
            continue

        if float(rate) >= 4.5 and int(rate_cnt) >= 100 :
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate} 점 ({rate_cnt})개 리뷰")
            print("링크 바로가기: {}".format('https://www.coupang.com'+link))
            print("-"*100)

            
        