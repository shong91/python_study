from indeed import search_from_indeed
from linkedin import search_from_linkedin
from stackOverflow import search_from_stackoverflow


if __name__ == "__main__":
    list_linkedin = search_from_linkedin("python")
    list_indeed = search_from_indeed("python")
    list_stackoverflow = search_from_stackoverflow("python")
    
    print(len(list_linkedin)) 
    print(list(list_linkedin))

    # for index, linkedin in enumerate(list_linkedin):
    #     print("==========================Search result from linkedin ({})==========================".format(index+1))
    #     print(linkedin.get("title"))
    #     print(linkedin.get("company"))
    #     print(linkedin.get("location"))
    #     print(linkedin.get("link"))

