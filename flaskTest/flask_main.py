from flask import Flask, render_template, request, redirect
import project_method as method
from csv_exporter import save_to_file

app = Flask(__name__)

# fake DB

# db = {}
global str_db
str_db = None

@app.route("/")
def home():
  return render_template("potato.html")


# @app.route("/<username>")
# def contact(username):
#   return f"Hello {username}, how are you doing "


@app.route("/report")
def report():
  word = request.args.get('target')
  if word:
    word = word.lower()
    # fromdb = db.get('weather')
    # if fromdb:
    # #  target = fromdb
    # else:
    str_db = method.scrape_weather()
    # db['weather'] = method.scrape_weather()
    print("str_db in report(): ", str_db)
  else:
    return redirect("/")

  return render_template("report.html", 
                          searchingBy=word, 
                          resultNumber=len(word),
                          result=str_db)


@app.route("/export")
def export():
  print("execute method export()")
  try:
    word = request.args.get('target')
    if not word:
      raise Exception

    word = word.lower()
    jobs = str_db
    print("target in export(): ", word)
    print("str_db in export(): ", str_db)

    # if not jobs:
    #   raise Exception
    save_to_file(word)
    return "lalaalall"
  except:
    return redirect("/")





if __name__ == "__main__":
  app.run(host="172.30.1.3", port="5000", debug=True)
