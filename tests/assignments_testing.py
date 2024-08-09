import pytest
from flask import Flask
from backend.assignments import assgn  # Import the Blueprint

# Configure pytest fixture for the Flask application
@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(assgn)
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

# Test for /analyze endpoint
def test_submission_analysis(client):
    data = {
        "week": "1",
        "question-1": "A",
        "question-2": "B"
    }
    response = client.post('/analyze', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "feedback" in json_data
    assert "results" in json_data
    assert json_data["results"]["1"]["1"] == "Correct" or "Incorrect"

# Test for /analyze_doubt endpoint
def test_analyze_doubt(client):
    data = {
        "week": "1",
        "question_index": "1",
        "doubt": "What is this?"
    }
    response = client.post('/analyze_doubt', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "cleared_doubt" in json_data

# Test for /dashboard/gradedassignment/<week_id> endpoint
def test_gradedassignment(client):
    response = client.get('/dashboard/gradedassignment/1')
    assert response.status_code == 200
    assert b"ga_copy.html" in response.data

# Test for /submit endpoint
def test_temp_submission(client):
    data = {
        "week": "1",
        "question-1": "A",
        "question-2": "B"
    }
    response = client.post('/submit', data=data)
    assert response.status_code == 200
    assert b"ga_copy_ans.html" in response.data

# Test for /api/complete_assignment_feedback endpoint
def test_complete_assignment_feedback(client):
    data = [
        ["What is Flask?", ["A web framework", "A type of container"], "A web framework", "A web framework"]
    ]
    response = client.post('/api/complete_assignment_feedback', json=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "response" in json_data

# Test for /api/process_regular_questions endpoint
def test_process_regular_questions(client):
    data = {
        "question": "What is Flask?",
        "options": ["A web framework", "A type of container"]
    }
    response = client.post('/api/process_regular_questions', json=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "response" in json_data

# Test for /api/populate_assignments endpoint
def test_populate_assignments(client):
    response = client.post('/api/populate_assignments')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data.get("message") == "Success"

# Test for /api/gradedassignment/<week_id>/clear endpoint
def test_gradedassignmentreset(client):
    response = client.get('/api/gradedassignment/1/clear')
    assert response.status_code == 200
    assert b"ga_copy.html" in response.data

# Test for /api/dashboard/gradedassignment/<week_id> endpoint
def test_gradedassignment_api(client):
    response = client.post('/api/dashboard/gradedassignment/1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "weeks_asg" in json_data
    assert json_data.get("week_id") == "1"

# Test for /api/per_qn_explaination endpoint
def test_per_qn_explaination(client):
    data = {
        "question": "What is Flask?"
    }
    response = client.post('/api/per_qn_explaination', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "response" in json_data

# Test for /api/per_qn_doubt endpoint
def test_per_qn_doubt(client):
    data = {
        "question": "What is Flask?",
        "doubt": "Is Flask a micro framework?"
    }
    response = client.post('/api/per_qn_doubt', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "response" in json_data

# Test for /api/verify_assignments endpoint
def test_verify_assignments(client):
    data = {
        "week": "1",
        "question-1": "A",
        "question-2": "B"
    }
    response = client.post('/api/verify_assignments', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "results" in json_data
    assert json_data["results"]["1"]["1"] == "Correct" or "Incorrect"
