from flask import render_template,request,redirect,url_for,Blueprint,flash,abort,jsonify, Flask
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *
from backend.GA.lecture_database import *


lec = Blueprint("lecture_routes",__name__,static_folder = '../static',template_folder="../templates" )

@lec.route('/dashboard/lecture/<week_id>/<lecture_id>', methods=['GET'])
def lecture(week_id,lecture_id):

    """
    ---
    get:
      summary: Lecture Page
      description: Route for lecture page
      responses:
        200:
          description: Success
    """       
    lecture_link = lectures_db[int(week_id)][int(lecture_id)]

    def convert_to_embed_url(youtube_url):
        # print(youtube_url)
        video_id = youtube_url[0].split(".be/")[-1].split("&")[0]
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        return embed_url  
    
    embed_url = convert_to_embed_url(lecture_link)
    lec_transcript = lecture_link[1]
    lec_summary = get_summary(lec_transcript)
    lec_key = get_key(lec_transcript)

    return render_template('lecture_copy.html', lecture_link=embed_url,lecture_id=lecture_id,week_id=week_id,lec_summary=lec_summary,lec_key=lec_key),200

# TODO
@lec.route('/api/lecture_populate', methods=['POST'])
def lecture_populate():

    """
    ---
    post:
      summary: Populates lecture pages
      description: Endpoint to populate lectures pages.
      responses:
        200:
          description: Success
    """    
    return jsonify({"message":"success"}),200