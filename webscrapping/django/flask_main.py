from flask import Flask, render_template, request
 
app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("potato.html")


@app.route("/<username>")
def contact(username):
  return f"Hello {username}, how are you doing "


@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", searchingBy=word, potato="whatever")


app.run()
