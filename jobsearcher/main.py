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
    url = "https://www.linkedin.com/jobs/search?keywords={}&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0".format(keyword)
    soup = create_soup(url)
    results = soup.find("ul", attrs={"class", "jobs-search__results-list"}).find_all("li")

    for result in results:
        title = result.find("h3", attrs={"class", "job-result-card__title"}).get_text()
        company = result.find("h4", attrs={"class", "job-result-card__subtitle"}).get_text()
        location = result.find("span", attrs={"class", "job-result-card__location"}).get_text()
        link = result.find("a", attrs={"class", "result-card__full-card-link"})["href"]

        print("======= JOB SEARCH Keyword: {} ===============".format(keyword))
        print(title)
        print(company)
        print(location)
        print(link)


def search_from_indeed(keyword):
    url = "https://www.indeed.com/jobs?q={}".format(keyword)
    soup = create_soup(url)
    results = soup.find_all("div", attrs={"class", "jobsearch-SerpJobCard"})
    # soup.find("td", attrs={"id", "resultsCol"}) is None
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
   
        print("======= JOB SEARCH Keyword: {} ===============".format(keyword))
        print(title)
        print(company)
        print(location)
        print(link)





def search_from_stackoverflow(keyword):
    url = "https://www.indeed.com/jobs?q={}".format(keyword)
    soup = create_soup(url)



if __name__ == "__main__":
    # search_from_linkedin("python")
    search_from_indeed("python")