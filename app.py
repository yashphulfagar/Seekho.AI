
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *
import re
from flask import Flask, render_template, request, jsonify, Blueprint, url_for

import os
from backend.Chatbot.chatbot import chat_bot


# Initialize
app = Flask(__name__)


# Register Blueprints
with app.app_context():
    from backend.lecture_routes import lec
    from backend.assignments import assgn

    from backend.chat_routes import chatt
    app.register_blueprint(lec)
    app.register_blueprint(assgn)
    app.register_blueprint(chatt)


#Logout
@app.route('/api/logout' , methods=['DELETE'])
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
    return render_template('starter-page.html'),200



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
    return render_template('chatbot.html'),200

@app.route('/dashboard/gradedassignment/<week_id>')
def gradedassignment(week_id):

    """
    ---
    get:
      summary: Graded Assignment Page
      description: Graded Assignment Page populated with details 
      responses:
        200:
          description: Success
    """     


    # print("week_id",week_id)

    weeks_asg=  all_asg[int(week_id)]
    # print(weeks_asg)
    return render_template('ga_copy.html', weeks_asg=weeks_asg, week_id=week_id)









if __name__ == '__main__':
    app.run(debug=True)
    
