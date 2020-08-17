import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 동적 페이지에 대한 웹 스크래핑(ex 스크롤 다운 시 목록 갱신)
# ===============================================================================
url="https://play.google.com/store/movies/top"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

interval = 2 # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이 
prev_height = browser.execute_script("return document.body.scrollHeight") 

# 반복 수행
while True:
    #스크롤을 아래로 내림 - 지정한 위치로 스크롤 내리기 (ex)  1920 * 1080 (해상도))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이 업데이트
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height

print("스크롤 완료")

# ===============================================================================
# 스크래핑 
soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class": "Vpfmgd"}) # 클래스 속성 값이 둘 이상이라면 리스트로 받아 처리한다. {"class": ["aa", "bb"]}

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    
    # 할인된 항목만 가져오기 - 1) 원래 가격
    original_price = movie.find("span", attrs={"class" : "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "할인되지 않은 영화는 제외")
        continue

    # 할인된 항목만 가져오기 - 2) 할인된 가격
    price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()
    
    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    
    print(f"제목: {title}")
    print(f"할인 전 가격: {original_price}")
    print(f"할인 후 가격: {price}")
    print("링크: ", "https://play.google.com"+ link)
    print("="*100)

browser.quit()
