#################################################
# MongoDB and Flask Application
#################################################


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################

# Create an instance of Flask
app = Flask(__name__)


#################################################
# PyMongo Connection Setup
#################################################

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################

# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html
# Route to render index.html template using data from Mongo to display data

@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()
    
    # Return template and data
    return render_template("index.html", mars=mars_dict)

    # Scrape Route to Import `scrape_mars.py` fileScript & Call data from `scrape` Function

@app.route("/scrape")
def scrape():
  
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

# Define Main Behavior
if __name__ == "__main__":
    app.run(debug=True)