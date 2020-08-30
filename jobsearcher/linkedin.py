import requests
from bs4 import BeautifulSoup
from indeed import create_soup

def extract_job(result):
    title = result.find("h3", attrs={"class", "job-result-card__title"}).get_text()
    company = result.find("h4", attrs={"class", "job-result-card__subtitle"}).get_text()
    location = result.find("span", attrs={"class", "job-result-card__location"}).get_text()
    link = result.find("a", attrs={"class", "result-card__full-card-link"})["href"]

    dict_linkedin = {"title" : title
                    ,"company" : company
                    ,"location" : location
                    ,"link" : link
                    }

    return dict_linkedin


def get_jobs(soup):
    list_linkedin = []
    results = soup.find("ul", attrs={"class", "jobs-search__results-list"}).find_all("li")
   
    for result in results:
        job = extract_job(result)
        list_linkedin.append(job)
    
    return list_linkedin 


def search_from_linkedin(keyword):
    url = f"https://www.linkedin.com/jobs/search?keywords={keyword}&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"
    soup = create_soup(url)
    list_linkedin = get_jobs(soup)

    return list_linkedin