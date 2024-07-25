from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)

@app.route('/api/process_regular_questions', methods=['POST'])
def process_questions():
    data = request.get_json()
    question = data.get('question', '')
    options = data.get('options', [])

    # replace this with the function Aryan, for example question_answer = functioncall()
    question_answer = f"Main question: {question}\n Options: {', '.join(options)}"

    # Return the response as JSON
    return jsonify({'response': question_answer})

@app.route('/api/complete_assignment_feedback', methods=['POST'])
def process_questionnaire():
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
    data = request.get_json()
    user_message = data.get('message', '')

    # sample repsonse, modify this Aryan to send the actual chatbot thing
    bot_response = f"You said: {user_message}"

    return jsonify({'response': bot_response})

@app.route('/')
def index():
    return render_template('starter-page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/lecture')
def lecture():
    return render_template('lecture.html')

@app.route('/dashboard/activityquestion')
def activityquestion():
    return render_template('activityquestion.html')

@app.route('/dashboard/gradedassignment')
def gradedassignment():
    return render_template('gradedassignment.html')

@app.route('/dashboard/programmingassignment')
def programmingassignment():
    return render_template('programmingassignment.html')

@app.route('/dashboard/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
