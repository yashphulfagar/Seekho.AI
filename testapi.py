import requests
import json

url = 'http://127.0.0.1:5000/api/process_questions'
payload = {
    'question': 'What is Flask?',
    'options': ['What is a Flask app?', 'How to use Flask?', 'Is Flask easy to learn?']
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())
