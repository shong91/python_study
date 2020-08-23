import requests 
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    return soup 

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("   (링크: {})".format(link))
    print()



# 1. 오늘의 날씨 
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    
    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class": "min"}).get_text()
    max_temp = soup.find("span", attrs={"class": "max"}).get_text() 
    morning_rain_rate = soup.find("span", attrs={"class": "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()
    dust = soup.find("dl", attrs={"class": "indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    # attrs={"class": "aa", "id": "bb", text=["미세먼지", "초미세먼지"]}
    # attrs={"class": ["aa", "bb", "cc"]}
    
    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("미세먼지 {}".format(pm25))
    print()

# 2. 헤드라인 뉴스
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3) # limit 옵션으로 갯수 제한
    
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)

# 3. IT 뉴스 정보 가져오기
def scrape_IT_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class" : "type06_headline"}).find_all("li", limit=3)
    
    for index, news in enumerate(news_list):
        img = news.find("img")
        a_index = 0
        if img:
            a_index = 1 # img 태그가 있으번면 1번째 a 태그의 정보 사용 
        
        a_tag = news.find_all("a")[a_index]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)


if __name__ == "__main__":
    # scrape_weather()
    # scrape_headline_news()
    scrape_IT_news()
