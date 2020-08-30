import requests
from bs4 import BeautifulSoup
from indeed import create_soup

def get_last_page(soup):
    # 페이징 (advanced than indeed.py)
    pagination = soup.find("div", attrs={"class", "s-pagination"})
    pages = pagination.find_all("a")   
    max_page = int(pages[-2].get_text(strip=True))
 
    return max_page

def extract_job(result):
    title = result.find("h2", attrs={"class", "fs-body3"}).get_text().strip()
    h3 = result.find("h3", attrs={"class", "fs-body1"}).find_all("span")
    company = h3[0].get_text().strip()
    location = h3[1].get_text().strip()
    link = "https://stackoverflow.com" + result.find("a", attrs={"class", "s-link stretched-link"})["href"]
    
    dict_stackoverflow = {"title" : title
                            ,"company" : company
                            ,"location" : location
                            ,"link" : link
                        }
    
    return dict_stackoverflow


def get_jobs(url, max_page):
    list_stackoverflow = []
    for page in range(max_page):
        print(f"scrapping page: {page}")
        url = f"{url}&pg={page}"
        soup = create_soup(url)
        results = soup.find_all("div", attrs={"class", "js-result"})

        for result in results:
            job = extract_job(result)
            list_stackoverflow.append(job)

    return list_stackoverflow


def search_from_stackoverflow(keyword):
    url = f"https://stackoverflow.com/jobs?q={keyword}&sort=i"
    soup = create_soup(url)
    max_page = get_last_page(soup)
    list_stackoverflow = get_jobs(url, max_page)
    
    return list_stackoverflow
    


