from flask import render_template,request,redirect,url_for,Blueprint,flash,abort
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
