import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Headless(Chrome without Chrome) - 브라우저를 띄우지 않고 작업하기
# ===============================================================================
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# headless 로 작업 시 argument 설정하지 않으면 user-agent 값이 HeadlessChrome 으로 설정됨 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()


