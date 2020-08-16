import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list.nhn?titleId=637931"
res = requests.get(url)
res.raise_for_status()

# res.text 의 정보로 BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all('td', attrs={'class': 'title'})

# 타이틀, 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com'+cartoon.a['href']
    # print(title, link)


# 평점 구하기
total_rates = 0
ranks = soup.find_all('div', attrs={'class': 'rating_type'})
for rank in ranks:
    rate = rank.find('strong').get_text()
    total_rates += float(rate)

print("평점: ", total_rates / len(ranks))