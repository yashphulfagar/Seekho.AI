###############Importing Libraries################
from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
#from apispec import APISpec
#from apispec_webframeworks.flask import FlaskPlugin
#import yaml
#import requests
from lecture_database import lectures_db as lectures_db
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re
from backend.Chatbot.chatbot import chat_bot
from backend.lecture_routes import lec
from backend.assignments import assgn
###############Importing Libraries################


# Initialize
app = Flask(__name__)
api = Api(app)
app.register_blueprint(lec)
app.register_blueprint(assgn)
'''
spec = APISpec(
    title="SE Gen AI Project",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin()],
)
'''

@app.route('/api/chat/clear')
def clearchat():

    """
    ---
    delete:
      summary: Clear Chat History
      description: Clears all chat history involving the chatbot and current user
      responses:
        200:
          description: Success
    """       
    return 

@app.route('/api/logout')
def logout_user():

    """
    ---
    delete:
      summary: Clear All User Data
      description: Clears all of the current users history and data
      responses:
        200:
          description: Success
    """       
    return 


@app.route('/api/chatbot_page', methods=['POST'])
def chatbot_page():

    """
    ---
    post:
      summary: Chatbot for general questions
      description: Route for chatbot page
      responses:
        200:
          description: Success
    """       
    data = request.get_json()
    user_message = data.get('message', '')
    print(user_message)
    chatbot_response = chat_bot(str(user_message))
    # sample repsonse, modify this Aryan to send the actual chatbot thing
    return jsonify({'response': chatbot_response})
      

@app.route('/')
def index():

    """
    ---
    get:
      summary: Home Page
      description: Route for home page
      responses:
        200:
          description: Success
    """       
    return render_template('starter-page.html')

@app.route('/dashboard')
def dashboard():

    """
    ---
    get:
      summary: Dashboard
      description: Route for dashboard
      responses:
        200:
          description: Success
    """       
    return render_template('dashboard_copy.html')




@app.route('/dashboard/chatbot')
def chatbot():
       
    """
    ---
    get:
      summary: Central Chatbot 
      description: Route for chatbot interface
      responses:
        200:
          description: Success
    """           
    return render_template('chatbot.html')

@app.route('/dashboard/activityquestion')
def activityquestion():

    """
    ---
    get:
      summary: Activity Question Page
      description: Route for activity question page
      responses:
        200:
          description: Success
    """       
    return render_template('activityquestion.html')

@app.route('/api/dashboard/activityquestion')
def activityquestion_api():

    """
    ---
    post:
      summary: Activity Question Page Details
      description: Activity Question Page populated with details
      responses:
        200:
          description: Success
    """       
    return 


@app.route('/dashboard/programmingassignment')
def programmingassignment():

    """
    ---
    get:
      summary: Programming Assignment Page
      description: Route for programming assignment page
      responses:
        200:
          description: Success
    """       
    return render_template('programmingassignment.html')

"""
# Register paths with the spec
with app.test_request_context():
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            spec.path(view=app.view_functions[rule.endpoint])

# Output the spec to a YAML file
with open('se_api.yaml', 'w') as file:
    yaml.dump(spec.to_dict(), file)
"""

if __name__ == '__main__':
    app.run(debug=True)
    
