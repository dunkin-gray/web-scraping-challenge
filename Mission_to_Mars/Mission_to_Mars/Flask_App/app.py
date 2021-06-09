####################################################
#Import Dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#####################################################
#Set up Flask

app = Flask(__name__)

#####################################################
#Set up PyMongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#####################################################
#Set up Flask routes

#Root route to query MongoDB and pass Mars data into HTML template
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#####################################################
#Scrape route to import scrape_mars.py

@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

#####################################################
#Define main behavior

if __name__ == "__main__":
    app.run() 