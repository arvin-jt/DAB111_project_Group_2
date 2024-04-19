from flask import Flask, render_template
from functions import queries

# Set up Flask application
app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # Render index page
    return render_template("index.html") 

# Route for the about page
@app.route("/about")
def about():
    # Return about page
    return render_template("about.html")

# Route for the data page
@app.route("/data")
def data():
    # Call path function
    db_path = queries.directory()
    
    # Call select all function
    results = queries.db_selectAll(db_path)
    
    # Render the data page with the title tables data
    return render_template("data.html", titles=results)

# Run Flask application 
if __name__=="__main__":
    app.run(debug=True)
