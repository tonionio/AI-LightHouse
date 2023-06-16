from flask import Flask
from .scraper import Scraper
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/scrape')
def scrape():
    scraper = Scraper(app.config['DB_NAME'], app.config['DB_USER'], app.config['DB_PASSWORD'],
                      app.config['DB_HOST'], app.config['DB_PORT'])
    scraper.connect_to_database()
    scraper.get_articles(app.config['API_KEY'], app.config['KEYWORDS'])
    articles = scraper.fetch_all_articles()
    scraper.disconnect_from_database()
    return {'articles': articles}, 200
