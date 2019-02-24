from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars
import os

app = Flask(__name__)

#use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marmission")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_results = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars_results=mars_results)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    #mars = mongo.db.mars
    mars_results = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_results, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
