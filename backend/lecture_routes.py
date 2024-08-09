from flask import render_template,request,redirect,url_for,Blueprint,flash,abort,jsonify, Flask
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *
from backend.GA.lecture_database import *


lec = Blueprint("lecture_routes",__name__,static_folder = '../static',template_folder="../templates" )

@lec.route('/dashboard/lecture/<week_id>/<lecture_id>')
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
    # print(week_id+"_"+lecture_id+"_"+"lectureeeeeeeeeeeeeeeeee")

    # print("before passing")
    # print(week_id, lecture_id)


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

    return render_template('lecture_copy.html', lecture_link=embed_url,lecture_id=lecture_id,week_id=week_id,lec_summary=lec_summary,lec_key=lec_key)


'''
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
    return

'''

'''
@lec.route('/api/vid_summary/<string:week_id>/<string:lecture_id>', methods=['POST'])
def vid_summary(week_id, lecture_id):


    """
    ---
    post:
      summary: Fetches video summary
      description: Endpoint to fetch video summary.
      responses:
        200:
          description: Success
          
    """    

    lecture_link = lectures_db[int(week_id)][int(lecture_id)]


    lec_transcript = lecture_link[1]


    lec_summary = get_summary(lec_transcript)
    
    return  jsonify({'summary': lec_summary})


@lec.route('/api/vid_summary_gen/<string:week_id>/<string:lecture_id>', methods=['POST'])
def vid_summary_gen(week_id, lecture_id):


    """
    ---
    post:
      summary: Generates video summary
      description: Endpoint to generate video summary.
      responses:
        200:
          description: Success
    """    

    lecture_link = lectures_db[int(week_id)][int(lecture_id)]


    lec_transcript = lecture_link[1]


    lec_summary = get_summary(lec_transcript)
    
    return  jsonify({'summary': lec_summary})
    '''
'''
@lec.route('/api/vid_keyword_gen/<string:week_id>/<string:lecture_id>', methods=['POST'])
def vid_keyword_gen(week_id, lecture_id):


    """
    ---
    post:
      summary: Generates video keywords
      description: Endpoint to generate keywords mentioned in video.
      responses:
        200:
          description: Success
    """        

    lecture_link = lectures_db[int(week_id)][int(lecture_id)]


    lec_transcript = lecture_link[1]
    lec_key = get_key(lec_transcript)
    return jsonify({'keypoints': lec_key})
'''
'''
@lec.route('/api/dashboard/lecture/<week_id>/<lecture_id>')
def lecture_api(week_id,lecture_id):


    """
    ---
    post:
      summary: Lecture Page Contents
      description: Lecture Page populated with details
      responses:
        200:
          description: Success
    """       
    lecture_link = lectures_db[int(week_id)][int(lecture_id)]

    video_url = lecture_link[0]
    lec_transcript = lecture_link[1]
    lec_summary = get_summary(lec_transcript)
    lec_key = get_key(lec_transcript)
    return jsonify({'video_url': video_url, 'summary': lec_summary, 'keypoints': lec_key, 'transcript': lec_transcript})
'''

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
    return



