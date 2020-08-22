from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화

url ="https://daum.net"
browser.get(url)

browser.find_element_by_id("q").send_keys("송파 헬리오시티")
browser.find_element_by_class_name("btn_search").click()


soup = BeautifulSoup(browser.page_source, "lxml")
div_realestate = soup.find("div", attrs={"id": "estateCollTabContentsResult"}).find("tbody")
realestates= div_realestate.find_all("tr")
header = "거래	공급/전용면적	매물가(만원)	동	층".split("\t")

for idx, realestate in enumerate(realestates):
    columns = realestate.find_all("td")
    
    print("="*30, "매물{}".format(idx+1), "="*30)
    print(header[0],": ", columns[0].get_text().strip())
    print(header[1],": ", columns[1].get_text().strip())
    print(header[2],": ", columns[2].get_text().strip())
    print(header[3],": ", columns[3].get_text().strip())
    print(header[4],": ", columns[4].get_text().strip())
    
