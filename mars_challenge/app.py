from unicodedata import name
import pymongo
from flask import Flask, render_template, request

from scraping import scrape_all

app = Flask(__name__)


myclient = pymongo.MongoClient(
    "mongodb+srv://hiren:hiren123@cluster0.csb7i2z.mongodb.net/?retryWrites=true&w=majority")

# databasename and collection name
mydb = myclient["scraper"]
mycol = mydb["moonscraper"]

# routers for website


@app.route("/")
def scraper():
    return render_template('index.html')


@app.route('/scrape', methods=['GET', 'POST'])
def mars_facts():
    alldata = {}
    data = scrape_all()
    alldata['data'] = data
    print(data)
    mycol.insert_one(alldata)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
