from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/rand")
def rand():
  r = randint(1,5)
  if r == 3:
    return f"<h1>{r} NOT FOUND!</h1>", 404
  else:
    return f"{r} --> BINGO!!!"

if __name__ == "__main__":
  app.run(host="0.0.0.0",port="80", debug=True)