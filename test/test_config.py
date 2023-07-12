import pytest
from app.config import Config

def test_config():
    config = Config()
    assert config.DB_NAME == 'Enter your database name here'
    assert config.DB_USER == 'Enter your username here'
    assert config.DB_PASSWORD == 'Enter your password here'
    assert config.DB_HOST == 'Enter your host here'
    assert config.DB_PORT == 'Enter your port here'
    assert config.KEYWORDS == ['artificial intelligence', 'AI', 'machine learning', 'AI safety', 'AI regulations', 'AI benefits']
    assert config.API_KEY == 'Enter your API key here'
