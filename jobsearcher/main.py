import requests
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {
                "User-Agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
                "Accept-Language"   : "ko-KR, ko"
             }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    return soup


def search_from_linkedin(keyword):
    list_linkedin = []
    url = "https://www.linkedin.com/jobs/search?keywords={}&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0".format(keyword)
    soup = create_soup(url)
    
    results = soup.find("ul", attrs={"class", "jobs-search__results-list"}).find_all("li")

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


def search_from_indeed(keyword):
    list_indeed = []
    url = "https://www.indeed.com/jobs?q={}".format(keyword)
    soup = create_soup(url)
    results = soup.find_all("div", attrs={"class", "jobsearch-SerpJobCard"})
  
    for result in results:
        new_flag = result.find("span", attrs={"class", "new"})
        title = result.find("h2", attrs={"class", "title"})
        if new_flag:
            title = title.find("a").get_text().strip()
        else:
            title = title.get_text().strip()

        # title = result.find("h2", attrs={"class", "title"}).get_text().strip()
        company = result.find("span", attrs={"class", "company"}).get_text().strip()
        location = result.find("span", attrs={"class", "location"}).get_text()
        link = "https://www.indeed.com"+ result.find("a", attrs={"class", "jobtitle"})["href"] # turnstileLink

        dict_indeed = {"title" : title
                      ,"company" : company
                      ,"location" : location
                      ,"link" : link
                      }
        
        list_indeed.append(dict_indeed)

    return list_indeed


def search_from_stackoverflow(keyword):
    list_stackoverflow = []
    url = "https://stackoverflow.com/jobs?q={}".format(keyword)
    soup = create_soup(url)
    results = soup.find_all("div", attrs={"class", "js-result"})
    
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
    list_linkedin = search_from_linkedin("python")
    list_indeed = search_from_indeed("python")
    list_stackoverflow = search_from_stackoverflow("python")

    for index, linkedin in enumerate(list_linkedin):
        print("==========================Search result from linkedin ({})==========================".format(index+1))
        print(linkedin.get("title"))
        print(linkedin.get("company"))
        print(linkedin.get("location"))
        print(linkedin.get("link"))

