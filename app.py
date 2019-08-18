from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/marsdata_app'
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo

@app.route('/')
def index():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collections.find_one()
    # Return template and data
    return render_template('index.html', mars1=mars_data)

# Route that will trigger the scrape function
@app.route('/scrape')
def scraper():

    # Run the scrape function
    mars = scrape_mars.scrape_info()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars, upsert=True)
    mongo.db.collection.update({}, mars_title_and_images, upsert=True)
    # Redirect back to home page
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)


