import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=637931&page=4"
res = requests.get(url)
res.raise_for_status()

bs = BeautifulSoup(res.text, 'lxml')
titles = bs.find_all('td', attrs={'class', 'title'})

for title in titles:
    subject = title.a.get_text()
    link = 'https://comic.naver.com'+title.a['href']
    img = bs.find('img', attrs={'title': subject})
    print(subject, link)
    print(img['src'])


total_rate = 0
ranks = bs.find_all('div', attrs={'class': 'rating_type'})
for rank in ranks:
    rate = rank.strong.get_text()
    total_rate += float(rate)


print('평균 평점: ', total_rate / len(ranks))