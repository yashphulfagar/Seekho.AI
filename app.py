from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

import requests


from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *





from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re
from chatbot import chat_bot

app = Flask(__name__)
api = Api(app)



# Register Blueprints
with app.app_context():
    from backend.lecture_routes import lec
    from backend.assignments import assgn
    from backend.chat_routes import chatt
    app.register_blueprint(lec)
    app.register_blueprint(assgn)
    app.register_blueprint(chatt)



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


















if __name__ == '__main__':
    app.run(debug=True)
    
