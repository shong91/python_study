import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url ="https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# 날짜 선택: 이번달 27, 28일
browser.find_elements_by_link_text("27")[0].click() # 이번 달 달력에서 선택
browser.find_elements_by_link_text("28")[1].click() # 다음 달 달력에서 선택

# 행선지 (제주) 선택 후 검색
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()
browser.find_element_by_link_text("항공권 검색").click()

# 로딩 페이지(browser) 에서 찾으려 하기 때문에 element = No such element 오류. 
# => 로딩이 종료되고 이후 로직 처리하도록 해야 함
try:
    # 브라우저에 대하여, 특정(xpath, id, name, ...) 에 해당하는 element 가 loacted 될 때까지 최대 10초동안 기다림
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(element.text)
finally:
    browser.quit()
