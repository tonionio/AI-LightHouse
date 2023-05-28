# AI-LightHouse
AI News Aggregator - a tool that uses web scraping to collect articles about artificial intelligence from various online sources.


The primary focus is on articles related to AI safety, regulations, and benefits, targeting individuals who may not be tech-savvy. The aggregator then compiles these articles into a simple, easy-to-understand email newsletter that is sent out to subscribers.

The data that drives this process, including information about the articles, sources, categories, authors, and subscribers, is stored in a Postgres database. The project's back end is built using Python, with BeautifulSoup for web scraping and smtplib for sending emails. The ER Diagram and SQL script for setting up the database have been developed. The next stages involve writing the Python script for web scraping and setting up the email newsletter functionality.
