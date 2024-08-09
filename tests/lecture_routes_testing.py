import pytest
from flask import Flask
from backend.lecture_routes import lec  # Import the Blueprint

# Configure pytest fixture for the Flask application
@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(lec)
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

# Test for /dashboard/lecture/<week_id>/<lecture_id> endpoint
def test_lecture(client):
    response = client.get('/dashboard/lecture/1/1')
    assert response.status_code == 200
    assert b"lecture_copy.html" in response.data
    assert b"https://www.youtube.com/embed/" in response.data
    assert b"Summary" in response.data  # Assuming the summary is rendered in the template
    assert b"Key Points" in response.data  # Assuming the key points are rendered in the template

# Test for /api/lecture_populate endpoint
def test_lecture_populate(client):
    response = client.post('/api/lecture_populate')
    assert response.status_code == 200
    assert response.get_json() == {}
