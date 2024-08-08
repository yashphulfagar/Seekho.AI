import json
import pytest
from app import app

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def runner():
    from flask.cli import FlaskGroup
    cli = FlaskGroup(app)
    yield cli

def test_get_transcript(client):
    # Test with a valid YouTube URL
    response = client.post('/api/get_transcript', json={'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'transcript' in data
    assert 'keypoints' in data

    # Test with an invalid YouTube URL
    response = client.post('/api/get_transcript', json={'video_url': 'https://www.youtube.com/invalid'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_chatbot_page(client):
    # Test sending a message to the chatbot
    response = client.post('/api/chatbot_page', json={'message': 'Hello'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data

def test_process_questionnaire(client):
    # Test processing questionnaire
    data = [
        ["What is Flask?", ["A web framework", "A type of container"], "A web framework", "A web framework"],
        ["What is Python?", ["A programming language", "A snake"], "A programming language", "A snake"]
    ]
    response = client.post('/api/complete_assignment_feedback', json=data)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert 'response' in response_data
    assert "Question: What is Flask?" in response_data['response']

def test_dashboard(client):
    # Test the dashboard page
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_lecture_page(client):
    # Test the lecture page
    response = client.get('/dashboard/lecture')
    assert response.status_code == 200
    assert b'Lecture' in response.data

def test_logout_user(client):
    # Test clearing all user data
    response = client.delete('/api/logout')
    assert response.status_code == 200

def test_activity_reset(client):
    # Test resetting activity question
    response = client.delete('/api/activityquestion/clear')
    assert response.status_code == 200

def test_programmingassignment_reset(client):
    # Test resetting programming assignment
    response = client.delete('/api/programmingassignment/clear')
    assert response.status_code == 200

def test_gradedassignment_reset(client):
    # Test resetting graded assignment
    response = client.delete('/api/gradedassignment/clear')
    assert response.status_code == 200
