import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Headless(Chrome without Chrome) - 브라우저를 띄우지 않고 작업하기
# ===============================================================================
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# 동적 페이지에 대한 웹 스크래핑(ex 스크롤 다운 시 목록 갱신)
# ===============================================================================
url="https://play.google.com/store/movies/top"

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

interval = 2 # 2초에 한 번씩 스크롤 내림
prev_height = browser.execute_script("return document.body.scrollHeight") 

# 반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

# ===============================================================================
# 스크래핑 
soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class": "Vpfmgd"}) # 클래스 속성 값이 둘 이상이라면 리스트로 받아 처리한다. {"class": ["aa", "bb"]}

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    
    original_price = movie.find("span", attrs={"class" : "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    
    price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()
    
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    
    print(f"제목: {title}")
    print(f"할인 전 가격: {original_price}")
    print(f"할인 후 가격: {price}")
    print("링크: ", "https://play.google.com"+ link)
    print("="*100)

browser.quit()
