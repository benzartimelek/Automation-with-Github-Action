import pytest
from hello_world import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_greeting_status_code(client):
    response = client.get("/greeting")
    assert response.status_code == 200

def test_greeting_contains_message(client):
    response = client.get("/greeting")
    assert b"Welcome to CI/CD 101 using GitHub Actions!" in response.data
