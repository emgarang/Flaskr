import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Flask App" in response.data
    # Check that links exist
    assert b'href="/add/1/2"' in response.data
    assert b'href="/reverse?q=example"' in response.data


def test_addition_page(client):
    # Test positive numbers
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert b"3 + 5 = 8" in response.data

    # Test negative numbers
    response = client.get("/add/-2/7")
    assert response.status_code == 200
    assert b"-2 + 7 = 5" in response.data

    # Test invalid input
    response = client.get("/add/a/b")
    assert response.status_code == 400
    assert b"Invalid numbers provided." in response.data


def test_reverse_page(client):
    # Normal string
    response = client.get("/reverse?q=hello")
    assert response.status_code == 200
    assert b"hello: olleh" in response.data

    # Empty string
    response = client.get("/reverse?q=")
    assert response.status_code == 200
    assert b": " in response.data

    # Missing parameter
    response = client.get("/reverse")
    assert response.status_code == 200
    assert b"<p>: </p>" in response.data
