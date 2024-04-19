from flask import Flask, render_template
from functions import queries

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    db_path = queries.directory()
    results = queries.db_selectAll(db_path)
    return render_template("data.html", titles=results)

if __name__=="__main__":
    app.run(debug=True)