import pytest
from app import app

def test_scrape_route():
    with app.test_client() as client:
        response = client.get('/scrape')
        assert response.status_code == 200
