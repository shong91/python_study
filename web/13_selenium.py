# 선작업: webdriver - chromedriver 설치 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# * request : [웹 페이지 읽어오기] 빠르다 / 동적 웹 페이지 불가
#     => 주어진 url 을 통해 받아온 html 에 원하는 정보가 있을 때 유용
# * selenium: [웹 페이지 자동화]   느리다 / 동적 웹 페이지 가능 
#     => 로그인, 어떤 결과에 대한 필터링 등 어떤 동작을 해야하는 경우 유용. (chromedriver.exe - version 확인 필)
#     => 페이지에 로딩을 기다려야 하는 경우 WebDriverWait().until()
# * beautifulSoup
# selenium 참조 링크: https://selenium-python.readthedocs.io/
# beautifulSoup 참조 링크: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# 1. 네이버로 이동
browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
element = browser.find_element_by_class_name("link_login")
element.click()

# 3. 아이디/패스워드 입력 후 로그인 
browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("pw").send_keys("password")
browser.find_element_by_id("log.login").click()

# 4. 아이디 재입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_rev_id")

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 탭 종료

# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()

# element = browser.find_element_by_id("query")
# element.send_keys("나도코딩")
# element.send_keys(Keys.ENTER)
