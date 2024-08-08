from flask import render_template,request,redirect,url_for,Blueprint,flash,abort
from lecture_database import lectures_db as lectures_db
from backend.GA.llm_setup import get_summary,get_key
lec = Blueprint("lecture_routes",__name__,static_folder = '../static',template_folder="../templates" )


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



@lec.route('/api/vid_summary', methods=['POST'])
def vid_summary():

    """
    ---
    post:
      summary: Fetches video summary
      description: Endpoint to fetch video summary.
      responses:
        200:
          description: Success
    """    
    return


@lec.route('/api/vid_summary_gen', methods=['POST'])
def vid_summary_gen():

    """
    ---
    post:
      summary: Generates video summary
      description: Endpoint to generate video summary.
      responses:
        200:
          description: Success
    """    
    return

@lec.route('/api/vid_keyword', methods=['POST'])
def vid_keyword():

    """
    ---
    post:
      summary: Fetches video keywords
      description: Endpoint to fetch keywords mentioned in video.
      responses:
        200:
          description: Success
    """        
    return

@lec.route('/api/vid_keyword_gen', methods=['POST'])
def vid_keyword_gen():

    """
    ---
    post:
      summary: Generates video keywords
      description: Endpoint to generate keywords mentioned in video.
      responses:
        200:
          description: Success
    """        
    return

@lec.route('/api/dashboard/lecture')
def lecture_api():

    """
    ---
    post:
      summary: Lecture Page Contents
      description: Lecture Page populated with details
      responses:
        200:
          description: Success
    """       
    return 

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
    # print(week_id+"_"+lecture_id+"_"+"lectureeeeeeeeeeeeeeeeeeeeeeeeeee")

    print("before passing")
    print(week_id, lecture_id)


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
