# beautifulsoup4, lxml 설치 
# 네이버 웹툰 스크래핑 

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# res.text 의 정보로 BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, "lxml")
# print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs) # a element 의 속성 정보 반환
# print(soup.a['href']) # a element 에서 '입력한 속성' 의 값 정보를 출력

# a = soup.find('a', attrs={"class", "Nbtn_upload"}) # 해당 조건에 맞는 처음으로 발견되는 a element 반환
# b = soup.find(attrs={"class", "Nbtn_upload"}) # 클래스가 Nbtn_upload 인 element 반환
# print(b)

rank1 = soup.find('li', attrs={"class": "rank01"})
rank2 = rank1.next_sibling.next_sibling # 개행이 있을 경우 한 번 더 next_sibling 해주어야 함 
rank3 = rank2.next_sibling.next_sibling

rank2 = rank3.previous_sibling.previous_sibling

# print(rank1.parent)

rank2 = rank1.find_next_sibling('li') # 개행 여부와 상관 없이 li 태그를 바로 찾음
rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# print("rank list: ", rank1.find_next_siblings('li'))


webtoon = soup.find('a', text="독립일기-18화 엄마의 방문")
print(webtoon)