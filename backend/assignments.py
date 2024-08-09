from flask import render_template,request,redirect,url_for,Blueprint,flash,abort,jsonify
import re
from youtube_transcript_api import YouTubeTranscriptApi
from backend.GA.llm_setup import *
assgn = Blueprint("assignments",__name__,static_folder = '../static',template_folder="../templates" )


@assgn.route('/api/populate_assignments', methods=['POST'])
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

@assgn.route('/api/verify_assignments', methods=['POST'])
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


@assgn.route('/api/per_qn_explaination', methods=['POST'])
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

@assgn.route('/api/per_qn_doubt', methods=['POST'])
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


'''
@assgn.route('/api/activityquestion/clear')
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
'''

@assgn.route('/api/gradedassignment/clear')
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

@assgn.route('/api/process_regular_questions', methods=['POST'])
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

@assgn.route('/api/complete_assignment_feedback', methods=['POST'])
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

@assgn.route('/api/get_transcript', methods=['POST'])
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

