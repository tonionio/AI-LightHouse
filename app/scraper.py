import requests
from psycopg2 import Error
import psycopg2
from .config import Config


class Scraper:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cur = None

    def connect_to_database(self):
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                                     password=self.password, host=self.host, port=self.port)
        self.cur = self.conn.cursor()
        print("Connected to database successfully")

    def disconnect_from_database(self):
        self.cur.close()
        self.conn.close()

    def get_source_id(self, source_name):
        self.cur.execute("SELECT source_id FROM source WHERE name = %s;", (source_name,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        self.cur.execute("INSERT INTO source (name) VALUES (%s) RETURNING source_id;", (source_name,))
        self.conn.commit()
        return self.cur.fetchone()[0]

    def get_author_id(self, author_name):
        self.cur.execute("SELECT author_id FROM author WHERE name = %s;", (author_name,))
        result = self.cur.fetchone()
        if result:
            return result[0]
        self.cur.execute("INSERT INTO author (name) VALUES (%s) RETURNING author_id;", (author_name,))
        self.conn.commit()
        return self.cur.fetchone()[0]

    def get_articles(self, api_key, keywords):
        url = "https://newsapi.org/v2/everything"
        for keyword in keywords:
            params = {
                'q': keyword,
                'apiKey': api_key,
            }
            response = requests.get(url, params=params)
            data = response.json()
            for article in data['articles']:
                self.insert_article(article)

    def insert_article(self, article):
        source_id = self.get_source_id(article['source']['name'])
        author_id = self.get_author_id(article['author']) if article['author'] else None
        insert_query = """
            INSERT INTO article (title, description, url, publication_date, author_id, source_id, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        values = (article['title'], article['description'], article['url'], article['publishedAt'],
                  author_id, source_id, 'General')
        self.cur.execute(insert_query, values)
        self.conn.commit()

    def fetch_all_articles(self):
        fetch_query = "SELECT * FROM article"
        self.cur.execute(fetch_query)
        articles = self.cur.fetchall()
        return articles  # Return the articles

