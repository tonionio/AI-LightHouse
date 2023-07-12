import pytest
from app.scraper import Scraper

def test_scraper_initialization():
    scraper = Scraper('dbname', 'user', 'password', 'host', 'port')
    assert scraper.dbname == 'dbname'
    assert scraper.user == 'user'
    assert scraper.password == 'password'
    assert scraper.host == 'host'
    assert scraper.port == 'port'
