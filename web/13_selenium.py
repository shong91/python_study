# 선작업: webdriver - chromedriver 설치 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# opts = Options()
# opts.add_experimental_option("detach", True)

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

time.sleep(3)
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_rev_id")

# html 정보 출력
print(broser.page_source)

# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()

# element = browser.find_element_by_id("query")
# element.send_keys("나도코딩")
# element.send_keys(Keys.ENTER)