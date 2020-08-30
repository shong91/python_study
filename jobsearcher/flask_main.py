from flask import Flask, render_template, request, redirect
from linkedin import search_from_linkedin
from indeed import search_from_indeed
from stackOverflow import search_from_stackoverflow
from exporter import save_to_file

app = Flask(__name__)

# fake DB
db = {} 
# {"python": [{title, company, location, link}, {title, company, location, link}]
# ,"react": [{title, company, location, link}, ... ]
# } 의 형태로 fake db 에 저장된다. 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    keyword = request.args.get("word")
    print(keyword)
    if keyword:
        keyword = keyword.lower()
        fromdb = db.get(keyword)
        if fromdb:
            jobs = fromdb
        else:
            jobs = search_from_linkedin(keyword)
            jobs.extend(search_from_indeed(keyword))
            jobs.extend(search_from_stackoverflow(keyword))
            db[keyword] = jobs

       
        print("len: ", len(jobs))
    else:
        return redirect("/")
    return render_template("report.html",
                            searchingBy=keyword,
                            resultNumber=len(jobs),
                            jobs=jobs)

@app.route("/export")
def export():
    print("execute method export()")
    try:
        keyword = request.args.get("word")
        if not keyword:
            raise Exception
        
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception
        
        save_to_file(jobs)
        
        return f"Generate CSV for {keyword}"
    except:
        return redirect("/")


if __name__ == "__main__":
    app.run(host="172.30.1.3", port="5000", debug=True)