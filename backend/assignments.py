from flask import render_template,request,redirect,url_for,Blueprint,flash,abort,jsonify, Flask
import re
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *

assgn = Blueprint("assignments",__name__,static_folder = '../static',template_folder="../templates" )


# class lecture_url(Resource):

#     def get(self, week_id, lecture_id):
#         print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#         print(week_id, lecture_id)

#         return {"lecture_link": embed_url}
    
# api.add_resource(lecture_url, '/api/vid_database_fetch/<string:week_id>/<string:lecture_id>')






@assgn.route('/analyze', methods=['POST'])
def submission_analysis():
  if request.method == 'POST':
    selected_options = request.form
    print("analyze just took place")


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

        # print("_________strt____________")
        # print(act_qn)
        # print(act_opt)
        # print(act_ans)
        # print(selected_answers)
        # print("_________nxt____________")


        print(grp_counter)
        print(j)
        if selected_answers == act_ans:
          results[grp_counter][j] = "Correct"
          
        else:
          results[grp_counter][j] = "Incorrect"
        

    print("___________hib____________")
    print(results)

    somethign = feedback_gen(week_id, results)


    return jsonify(somethign)


@assgn.route('/analyze_doubt', methods=['POST'])
def analyze_doubt():
    if request.method == 'POST':
      print("doubt just took place")

      print("htis is where doubt analysis begins")
      question_index = request.form.get('question_index')
      doubt = request.form.get('doubt')
      week_id = request.form.get('week')
      print(question_index)
      print(doubt)
      print(week_id)


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
          if counter == int(question_index):
            act_qn = question_deets[0]
            act_opt = question_deets[1]
            act_ans = question_deets[2]
            act_ans.sort()


            print("_________strt____________")
            print(act_qn)
            print(act_opt)
            print(act_ans)
            
            print("_________nxt____________")

            # send the doubt top the llm
            cleared_doubt = individual_doubt(doubt= doubt, question= act_qn, options= act_opt, answer= act_ans, context= bulk_context)

            return jsonify(cleared_doubt)
        else:
          print("searcgubf")  
          continue

    return  jsonify("No question found")








@assgn.route('/submit', methods=['POST'])
def temp_submission():
  if request.method == 'POST':
    selected_options = request.form
    print("submit just took place")

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

        # print("_________strt____________")
        # print(act_qn)
        # print(act_opt)
        # print(act_ans)
        # print(selected_answers)
        # print("_________nxt____________")


        print(grp_counter)
        print(j)
        if selected_answers == act_ans:
          results[grp_counter][j] = "Correct"
          
        else:
          results[grp_counter][j] = "Incorrect"
        

    print("___________hia____________")
    print(results)


    return render_template('ga_copy_ans.html', weeks_asg=weeks_questions, week_id=week_id, results=results)






# TODO 
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



# TODO
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



@assgn.route('/api/gradedassignment/<week_id>/clear')
def gradedassignmentreset(week_id):


    """
    ---
    delete:

      summary: Clear Graded Assignment
      description: Clear the answers of the current graded assignment

      responses:
        200:
          description: Success
    """       

    weeks_asg=  all_asg[int(week_id)]
    # print(weeks_asg)
    return render_template('ga_copy.html', weeks_asg=weeks_asg, week_id=week_id)

@assgn.route('/api/dashboard/gradedassignment/<week_id>')
def gradedassignment_api(week_id):

    """
    ---
    post:
      summary: Graded Assignment Page Details
      description: Graded Assignment Page populated with details

      responses:
        200:
          description: Success
    """       

    weeks_asg=  all_asg[int(week_id)]
    # print(weeks_asg)
    return jsonify({'weeks_asg': weeks_asg, 'week_id': week_id})

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
    if request.method == 'POST':
        question = request.form.get('question')
        doubt = "Please explain this question more elaborately to me."
        response = individual_doubt(question, doubt)
        return jsonify({'response': response})

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
    if request.method == 'POST':
        question = request.form.get('question')
        doubt = request.form.get('doubt')
        response = individual_doubt(question, doubt)
        return jsonify({'response': response})
    
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
    if request.method == 'POST':
        selected_options = request.form
        print("submit just took place")

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

                # print("_________strt____________")
                # print(act_qn)
                # print(act_opt)
                # print(act_ans)
                # print(selected_answers)
                # print("_________nxt____________")


                print(grp_counter)
                print(j)
                if selected_answers == act_ans:
                    results[grp_counter][j] = "Correct"
                    
                else:
                    results[grp_counter][j] = "Incorrect"
                

        print("___________hia____________")
        print(results)


        return jsonify(results)
    







