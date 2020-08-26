from flask import Flask, render_template, request, redirect
import project_method as method

app = Flask(__name__)

# fake DB
# db = {}
str_db = ""

@app.route("/")
def home():
  return render_template("potato.html")


# @app.route("/<username>")
# def contact(username):
#   return f"Hello {username}, how are you doing "


@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    # fromdb = db.get('weather')
    # if fromdb:
    # #  word = fromdb
    # else:
    print(method.scrape_weather())
    str_db = method.scrape_weather()
    # db['weather'] = method.scrape_weather()
  else:
    return redirect("/")

  return render_template("report.html", 
                          searchingBy=word, 
                          resultNumber=len(word),
                          result=str_db)

if __name__ == "__main__":
  app.run(host="172.30.1.3", port="5000", debug=True)
