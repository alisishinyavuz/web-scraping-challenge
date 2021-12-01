#import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create instance of Flask app
app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#Create route that renders index.html template
@app.route("/")
def index():
    mars_news= mongo.db.mars_news.find_one()

    return render_template("index.html", mars_news = mars_news)

@app.route("/scrape")
def scrape():
    mars_news= mongo.db.mars_news
    mars_data = scrape_mars.scrape()
    mars_news.update({}, mars_data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)






