import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

LIMIT = 50
# global url

def create_soup(url):    
    if "linkedin" in url:
        # 1. 스크롤 다운 처리
        browser = webdriver.Chrome()
        # browser.maximize_window()
        browser.get(url)

        interval = 2
        prev_height = browser.execute_script("return document.body.scrollHeight")

        
        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(interval)
            curr_height = browser.execute_script("return document.body.scrollHeight")

            if prev_height == curr_height:
                break
            prev_height = curr_height
        
        soup = BeautifulSoup(browser.page_source, "lxml")
    else:
        headers = {
            "User-Agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language"   : "ko-KR, ko"
            }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

    return soup


def get_last_page(soup):
    # 페이징 방식
    pagination = soup.find("div", attrs={"class", "pagination"})
    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]: # [-1]: 마지막에서부터 시작하여 첫번째 item.
        # print(link.find("span").string)
        pages.append(int(link.string))
    
    # last_page = max_page
    max_page = pages[-1]
    return max_page


def extract_job(result):
    new_flag = result.find("span", attrs={"class", "new"})
    title = result.find("h2", attrs={"class", "title"})
    if new_flag:
        title = str(title.find("a").get_text()) # .string 은 None 으로 받는데 get_text() 는 값을 받아옴.. 차이 확인 
    else:
        title = str(title.get_text())
    title = title.strip()

    company = result.find("span", attrs={"class", "company"}) # .string
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    
    location = result.find("span", attrs={"class", "location"}).get_text()
    link = "https://www.indeed.com"+ result.find("a", attrs={"class", "jobtitle"})["href"] # turnstileLink
    # job_id = result["data-jk"]
    # link = f"https://www.indeed.com/viewjob?jk={job_id}"

    dict_indeed = {"title" : title
                ,"company" : company
                ,"location" : location
                ,"link" : link
                }

    return dict_indeed
    

def get_jobs(url, max_page):    
    list_indeed = []
    for page in range(max_page):
        print(f"scrapping page: {page}")
        url = f"{url}&start={page*LIMIT}"
        soup = create_soup(url)
        results = soup.find_all("div", attrs={"class", "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            list_indeed.append(job)

    return list_indeed    


def search_from_indeed(keyword):
    url = f"https://www.indeed.com/jobs?q={keyword}&limit={LIMIT}"
    soup = create_soup(url)   
    max_page = get_last_page(soup)
    list_indeed = get_jobs(url, max_page)

    return list_indeed


# def extract_job(soup):
#     results = soup.find_all("div", attrs={"class", "jobsearch-SerpJobCard"})
    
#     for result in results:
#         title = result.find("div", attrs={"class", "title"}).find("a")["title"]

#         company = result.find("span", attrs={"class", "company"}) # .string
#         company_anchor = company.find("a")
#         if company_anchor is not None:
#             company = str(company_anchor.string)
#         else:
#             company = str(company.string)
#         company = company.strip()
#         location = result.find("span", attrs={"class", "location"}).get_text()
#         link = "https://www.indeed.com"+ result.find("a", attrs={"class", "jobtitle"})["href"] # turnstileLink

#         dict_indeed = {"title" : title
#                     ,"company" : company
#                     ,"location" : location
#                     ,"link" : link
#                     }
        
#         list_indeed.append(dict_indeed)

#     return list_indeed