from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
import yaml
import requests


from flask_restful import Resource, Api
from backend.atharva.llm_setup import *
from backend.atharva.lecture_database import *





from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re
from chatbot import chat_bot

app = Flask(__name__)
api = Api(app)

# Initialize
spec = APISpec(
    title="SE Gen AI Project",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin()],
)

"""
---
post:
  summary: Fetches video data from database
  description: Endpoint to fetch video data from database.
  responses:
    200:
      description: Success
"""        




# class lecture_url(Resource):

#     def get(self, week_id, lecture_id):
#         print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#         print(week_id, lecture_id)

#         return {"lecture_link": embed_url}
    
# api.add_resource(lecture_url, '/api/vid_database_fetch/<string:week_id>/<string:lecture_id>')





@app.route('/api/lecture_populate', methods=['POST'])
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



@app.route('/api/vid_summary', methods=['POST'])
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

@app.route('/api/vid_summary_gen', methods=['POST'])
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

@app.route('/api/vid_keyword', methods=['POST'])
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

@app.route('/api/vid_keyword_gen', methods=['POST'])
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

@app.route('/api/dashboard/lecture')
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

@app.route('/api/populate_assignments', methods=['POST'])
def populate_assignments():

    """
    ---
    post:
      summary: Populates assignment
      description: Endpoint to populate assignments into the page.
      responses:
        200:
          description: Success
    """
    return

@app.route('/api/verify_assignments', methods=['POST'])
def verify_assignments():

    """
    ---
    post:
      summary: Verifies assignment
      description: Endpoint to verify the responses that the user has given.
      responses:
        200:
          description: Success
    """
    return

@app.route('/api/chat_chain', methods=['POST'])
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

@app.route('/api/per_qn_explaination', methods=['POST'])
def per_qn_explaination():

    """
    ---
    post:
      summary: Generates explanation for individual question
      description: Endpoint to generate explanation for individual question without user query.
      responses:
        200:
          description: Success
    """        
    return

@app.route('/api/per_qn_doubt', methods=['POST'])
def per_qn_doubt():

    """
    ---
    post:
      summary: Generates explanation for individual question based on doubt
      description: Endpoint to generate explanation for individual question with user query.
      responses:
        200:
          description: Success
    """        
    return

@app.route('/api/dashboard/programmingassignment')
def programmingassignment_api():

    """
    ---
    post:
      summary: Programming Assignment Page Details
      description: Programming assignment Page populated with details
      responses:
        200:
          description: Success
    """       
    return 


@app.route('/api/dashboard/gradedassignment')
def gradedassignment_api():

    """
    ---
    post:
      summary: Graded Assignment Page Details
      description: Graded Assignment Page populated with details
      responses:
        200:
          description: Success
    """       
    return 

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

@app.route('/api/activityquestion/clear')
def activityreset():

    """
    ---
    delete:
      summary: Clear Activity
      description: Clear the answers of the current activity question
      responses:
        200:
          description: Success
    """       
    return 

@app.route('/api/programmingassignment/clear')
def programmingassignmentreset():

    """
    ---
    delete:
      summary: Clear Programming Assignment
      description: Clear the answers of the current Programming Assignment
      responses:
        200:
          description: Success
    """       
    return 

@app.route('/api/gradedassignment/clear')
def gradedassignmentreset():

    """
    ---
    delete:
      summary: Clear Graded Assignment
      description: Clear the answers of the current graded assignment
      responses:
        200:
          description: Success
    """       
    return 
@app.route('/api/dashboard')
def dashboard_api():

    """
    ---
    post:
      summary: Dashboard Page Contents
      description: Dashboard Page populated with details
      responses:
        200:
          description: Success
    """       
    return 

@app.route('/api/process_regular_questions', methods=['POST'])
def process_questions():

    """
    ---
    post:
      summary: Chatbot for regular questions
      description: Endpoint to process regular questions and generate responses from LLM.
      responses:
        200:
          description: Success
    """       
    data = request.get_json()
    question = data.get('question', '')
    options = data.get('options', [])

    # replace this with the function Aryan, for example question_answer = functioncall()
    question_answer = f"Main question: {question}\n Options: {', '.join(options)}"

    # Return the response as JSON
    return jsonify({'response': question_answer})

@app.route('/api/complete_assignment_feedback', methods=['POST'])
def process_questionnaire():

    """
    ---
    post:
      summary: Generate student custom feedback
      description: Endppoint to generate student custom feedback based on the questionnaire and student responses.
      responses:
        200:
          description: Success
    """       
    # input format: [[question, options, marked_answer, correct_answer]]
    # [
    # ["What is Flask?", ["A web framework", "A type of container"], "A web framework", "A web framework"],
    # ["What is Python?", ["A programming language", "A snake"], "A programming language", "A snake"]
    # ] 

    data = request.get_json()
    
    question_options_markedanswer_correctanswer = []
    
    # Process each question
    for item in data:
        question = item[0]
        options = item[1]
        marked_option = item[2]
        correct_option = item[3]
        
        # Create a formatted string for each question
        question_str = f"Question: {question}, Options: {', '.join(options)}, Marked Option: {marked_option}, Correct Option: {correct_option}"
        question_options_markedanswer_correctanswer.append(question_str)
    
    # Combine all questions into a single line response
    single_line_response = ' | '.join(question_options_markedanswer_correctanswer)
    
    # Return the response as JSON
    return jsonify({'response': single_line_response})

@app.route('/api/get_transcript', methods=['POST'])
def get_transcript():

    """
    ---
    post:
      summary: Fetches video transcript
      description: Get the transcript of a given video lecture.
      responses:
        200:
          description: Success
    """       
    #input format: {'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}

    data = request.get_json()
    video_url = data.get('video_url', '')

    # Extract video ID from URL
    video_id = re.search(r'v=([^&]+)', video_url)
    if video_id:
        video_id = video_id.group(1)
    else:
        return jsonify({'error': 'Invalid YouTube URL'}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript])
        keypoints="keypoint 1, keypoint 2, keypoint 3"
        return jsonify({'transcript': transcript_text,'keypoints': keypoints})
    except Exception as e:
        return jsonify({'error': str(e)}), 500












































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



@app.route('/dashboard/lecture/<week_id>/<lecture_id>')
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




@app.route('/submit', methods=['POST'])
def temp_submission():
  if request.method == 'POST':
    selected_options = request.form

    # Print the submitted form data to the console
    week_id = selected_options.get('week')
    print(week_id)
    print(selected_options)
    print("hiiiiiiiiiiiiiiiii")
    # print(all_asg)

    results={}
    counter = 0
    grp_counter = 0
    weeks_questions=all_asg[int(week_id)]
    print("new")
    # print(weeks_questions)
    for i, bulk_question in weeks_questions.items():
      # print(bulk_question)
      # print("yo")
      grp_counter += 1
      results[grp_counter] = {}
      


      bulk_context = bulk_question[0]
      for j, question_deets in bulk_question[1].items():
        counter += 1
        print(question_deets)

        act_qn = question_deets[0]
        act_opt = question_deets[1]
        act_ans = question_deets[2]
        act_ans.sort()
        this_name = "question-"+str(counter)

        

        selected_answers = selected_options.getlist(this_name)
        selected_answers.sort()

        print("_________strt____________")
        print(act_qn)
        print(act_opt)
        print(act_ans)
        print(selected_answers)
        print("_________nxt____________")


        print(grp_counter)
        print(j)
        if selected_answers == act_ans:
          results[grp_counter][j] = "yes"
          
        else:
          results[grp_counter][j] = "no"
        

    print("___________hi____________")
    print(results)










    # Return the submitted form data as a simple text response
    return f"Received: {dict(selected_options)}"
   

















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


# Register paths with the spec
with app.test_request_context():
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            spec.path(view=app.view_functions[rule.endpoint])

# Output the spec to a YAML file
with open('se_api.yaml', 'w') as file:
    yaml.dump(spec.to_dict(), file)
    




if __name__ == '__main__':
    app.run(debug=True)
    
