import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from indeed import search_from_indeed




def search_from_linkedin(keyword):
    list_linkedin = []
    url = f"https://www.linkedin.com/jobs/search?keywords={keyword}&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"
    soup = create_soup(url)
    
    results = soup.find("ul", attrs={"class", "jobs-search__results-list"}).find_all("li")
   
    # scroll down 방식 
    for result in results:
        title = result.find("h3", attrs={"class", "job-result-card__title"}).get_text()
        company = result.find("h4", attrs={"class", "job-result-card__subtitle"}).get_text()
        location = result.find("span", attrs={"class", "job-result-card__location"}).get_text()
        link = result.find("a", attrs={"class", "result-card__full-card-link"})["href"]

        dict_linkedin = {"title" : title
                        ,"company" : company
                        ,"location" : location
                        ,"link" : link
                        }
        
        list_linkedin.append(dict_linkedin)

    return list_linkedin    



def search_from_stackoverflow(keyword):
    list_stackoverflow = []
    url = f"https://stackoverflow.com/jobs?q={keyword}"
    soup = create_soup(url)
    results = soup.find_all("div", attrs={"class", "js-result"})
    
    # 페이징 방식
    for result in results:
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
    
        list_stackoverflow.append(dict_stackoverflow)

    return list_stackoverflow


if __name__ == "__main__":
    # list_linkedin = search_from_linkedin("python")
    list_indeed = search_from_indeed("python")
    # list_stackoverflow = search_from_stackoverflow("python")
    
    print(len(list_indeed)) 
    print(list(list_indeed))

    # for index, linkedin in enumerate(list_linkedin):
    #     print("==========================Search result from linkedin ({})==========================".format(index+1))
    #     print(linkedin.get("title"))
    #     print(linkedin.get("company"))
    #     print(linkedin.get("location"))
    #     print(linkedin.get("link"))

