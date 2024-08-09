from flask import render_template,request,redirect,url_for,Blueprint,flash,abort,jsonify, Flask
import re
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *



# TODO
chatt = Blueprint("chatbot",__name__,static_folder = '../static',template_folder="../templates" )



# TODO
@chatt.route('/api/chat/clear')
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


#  TODO
@chatt.route('/api/chat_chain', methods=['POST'])
def chat_chain():

    """
    ---
    post:
      summary: Chain LLM conversation
      description: Endpoint to chain LLM conversations and generate responses.
      responses:
        200:
          description: Success
    """    
    return