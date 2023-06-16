# Description: This file contains the code for the AI Safety News Scraper

# replace with your actual NewsAPI


# ------------------------------- version TWO of the code - used beautifulsoup-------------------------------------------------------
""" import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import Error
import time


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
        # Print after successful connection
        print("Connected to database successfully")

    def disconnect_from_database(self):
        self.cur.close()
        self.conn.close()

    def create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS articles (
                ID SERIAL PRIMARY KEY,
                URL TEXT NOT NULL,
                article_url TEXT NOT NULL
            );
        '''
        try:
            self.cur.execute(create_table_query)
            self.conn.commit()
            print("Table created successfully in PostgreSQL")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)
            self.conn.commit()

    def scrape_websites(self, urls, keywords):
        for url in urls:
            print(f"Processing: {url}")  # Print the url being processed
            response = requests.get(url)
            if response.status_code == 200:
                webpage = response.content
                soup = BeautifulSoup(webpage, 'html.parser')
                articles = self.find_articles(url, soup)

                for article in articles:
                    title = self.extract_title(url, article)
                    author = self.extract_author(url, article)
                    article_url = self.extract_article_url(url, article)

                    print(f"Found article: {title} by {author} at {article_url}")  # Print all articles found

                    if any(keyword.lower() in title.lower() for keyword in keywords):
                        print(f"Keyword found in article: {title} by {author} at {article_url}")  # Print when keyword is found
                        self.insert_article(url, article_url)
                        break  # Stop after inserting one article per website

            # Sleep for 1 second between requests to respect the server
            time.sleep(1)

    def find_articles(self, url, soup):
        if url == 'https://towardsai.net/':
            return soup.find_all('div', class_='post-categories')
        elif url == 'https://medium.com/':
            return soup.find_all('div', class_='fdbc')
        elif url == 'https://variety.com/':
            return soup.find_all('header', class_='article-header')
        elif url == 'https://www.huffpost.com/':
            return soup.find_all('h3', class_='headline')
        elif url == 'https://openai.com/blog':
            return soup.find_all('h2', class_='f-display-2')
        elif url == 'https://www.theverge.com/':
            return soup.find_all('h2', class_='group-hover:shadow-underline-franklin')
        elif url == 'https://www.nytimes.com/':
            return soup.find_all('h2', class_='css-1ay0v87 e1h9rw200')
        elif url == 'https://www.wsj.com/':
            return soup.find_all('h3', class_='css-1lvqw7f-StyledHeadline e1ipbpvp0')
        else:
            return []

    def extract_title(self, url, article):
        if url == 'https://towardsai.net/':
            return article.find('h3', class_='post-title').get_text(strip=True)
        elif url == 'https://medium.com/':
            return article.find('h1', class_='f-subhead-2').get_text(strip=True)
        elif url == 'https://variety.com/':
            return article.find('h1').get_text(strip=True)
        elif url == 'https://www.huffpost.com/':
            return article.find('h3', class_='headline').get_text(strip=True)
        elif url == 'https://openai.com/blog':
            return article.find('h2', class_='f-display-2').get_text(strip=True)
        elif url == 'https://www.theverge.com/':
            return article.find('h2', class_='group-hover:shadow-underline-franklin').get_text(strip=True)
        elif url == 'https://www.nytimes.com/':
            return article.find('h2', class_='css-1ay0v87 e1h9rw200').get_text(strip=True)
        elif url == 'https://www.wsj.com/':
            return article.find('h3', class_='css-1lvqw7f-StyledHeadline e1ipbpvp0').get_text(strip=True)
        else:
            return ''

    def extract_author(self, url, article):
        if url == 'https://towardsai.net/':
            return article.find('span', class_='medium-author').get_text(strip=True)
        elif url == 'https://medium.com/':
            return article.find('span', class_='af ag ah ai aj ak al am an ao ap aq ar tm').get_text(strip=True)
        elif url == 'https://variety.com/':
            return article.find('div', class_='author-social').get_text(strip=True)
        elif url == 'https://www.huffpost.com/':
            return article.find('span', class_='entry__byline__author').get_text(strip=True)
        elif url == 'https://openai.com/blog':
            return ''
        elif url == 'https://www.theverge.com/':
            return article.find('span', class_='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8').get_text(strip=True)
        elif url == 'https://www.nytimes.com/':
            return article.find('span', class_='css-1baulvz last-byline').get_text(strip=True)
        elif url == 'https://www.wsj.com/':
            return article.find('a', class_='css-mbn33i-AuthorLink e10pnb9y0').get_text(strip=True)
        else:
            return ''

    def extract_article_url(self, url, article):
        if url == 'https://towardsai.net/':
            return article.find('a')['href']
        elif url == 'https://medium.com/':
            return article.find('a')['href']
        elif url == 'https://variety.com/':
            return article.find('a')['href']
        elif url == 'https://www.huffpost.com/':
            return article.find('a')['href']
        elif url == 'https://openai.com/blog':
            return article.find('a')['href']
        elif url == 'https://www.theverge.com/':
            return article.find('a')['href']
        elif url == 'https://www.nytimes.com/':
            return article.find('a')['href']
        elif url == 'https://www.wsj.com/':
            return article.find('a')['href']
        else:
            return ''

    def insert_article(self, url, article_url):
        insert_query = "INSERT INTO articles (url, article_url) VALUES (%s, %s)"
        values = (url, article_url)
        self.cur.execute(insert_query, values)
        self.conn.commit()

    def fetch_all_articles(self):
        fetch_query = "SELECT * FROM articles"
        self.cur.execute(fetch_query)
        articles = self.cur.fetchall()
        for article in articles:
            print(article)


# Database connection details
dbname = 'enter database name here'
user = 'enter username here'
password = 'enter password here'
host = 'enter host here'
port = 'enter port number here'

# List of URLs of the websites
urls = [
    'https://towardsai.net/',
    'https://medium.com/',
    'https://variety.com/',
    'https://www.huffpost.com/',
    'https://openai.com/blog',
    'https://www.theverge.com/',
    'https://www.nytimes.com/',
    'https://www.wsj.com/'
]

# Keywords related to AI safety, regulations, and benefits
keywords = ['artificial intelligence', 'AI', 'machine learning',
            'AI safety', 'AI regulations', 'AI benefits']

scraper = Scraper(dbname, user, password, host, port)
scraper.connect_to_database()
scraper.create_table()
scraper.scrape_websites(urls, keywords)
scraper.fetch_all_articles()
scraper.disconnect_from_database()
"""


# ------------------------------------------------------ version ONE of the code - no OOP or Optimization ------------------------------------------------------
""" import requests
from bs4 import BeautifulSoup
import psycopg2

# Database connection details
dbname = 'enter database name here'
user = 'enter username here'
password = 'enter password here'
host = 'enter host here'
port = 'enter port number here'

# List of URLs of the websites
urls = [
    'https://towardsai.net/',
    'https://medium.com/',
    'https://variety.com/',
    'https://www.huffpost.com/',
    'https://openai.com/blog',
    'https://www.theverge.com/',
    'https://www.nytimes.com/',
    'https://www.wsj.com/',
    'https://www.researchgate.net/',
    'https://www.gatesnotes.com/'
]

# Keywords related to AI safety, regulations, and benefits
keywords = ['artificial intelligence', 'AI', 'machine learning',
            'AI safety', 'AI regulations', 'AI benefits']

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host, port=port)
cur = conn.cursor()

# Iterate over the URLs
for url in urls:
    # Send HTTP request and get the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the response
        webpage = response.content

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(webpage, 'html.parser')

        # Find elements by their tag and class
        if url == 'https://towardsai.net/':
            articles = soup.find_all('div', class_='page-content')
        elif url == 'https://medium.com/':
            articles = soup.find_all('h3', class_='post-title')
        elif url == 'https://variety.com/':
            articles = soup.find_all('h2', class_='article-title')
        elif url == 'https://www.huffpost.com/':
            articles = soup.find_all('h2', class_='entry-title')
        elif url == 'https://openai.com/blog':
            articles = soup.find_all('h3', class_='blog-post-title')
        elif url == 'https://www.theverge.com/':
            articles = soup.find_all('h2', class_='c-entry-title')
        elif url == 'https://www.nytimes.com/':
            articles = soup.find_all('h2', class_='story-heading')
        elif url == 'https://www.wsj.com/':
            articles = soup.find_all('h3', class_='hed')
        elif url == 'https://www.researchgate.net/':
            articles = soup.find_all('div', class_='article-title')
        elif url == 'https://www.gatesnotes.com/':
            articles = soup.find_all('h3', class_='post-title')
        else:
            articles = []

        # Iterate over the articles
        for article in articles:
            # Extract the desired information
            title = article.get_text()
            author = ''  # Set author to empty for now, as it is not available in the provided HTML structure
            date = ''  # Set date to empty for now, as it is not available in the provided HTML structure
            url = article.find('a')['href']

            # Check if any of the keywords are in the title
            if any(keyword.lower() in title.lower() for keyword in keywords):
                # Insert the data into the database
                insert_query = "INSERT INTO article (title, author, publication_date, url) VALUES (%s, %s, %s, %s)"
                values = (title, author, date, url)
                cur.execute(insert_query, values)
                conn.commit()

                # Break the loop after finding the first relevant article on each website
                break

# Close the cursor and connection
cur.close()
conn.close()
"""
