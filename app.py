###############Importing Libraries################
from flask import Flask, render_template, request, jsonify, Blueprint, url_for
#from apispec import APISpec
#from apispec_webframeworks.flask import FlaskPlugin
#import yaml
#import requests
from backend.Chatbot.chatbot import chat_bot
###############Importing Libraries################


# Initialize
app = Flask(__name__)

# Register Blueprints
with app.app_context():
    from backend.lecture_routes import lec
    from backend.assignments import assgn
    app.register_blueprint(lec)
    app.register_blueprint(assgn)

'''
spec = APISpec(
    title="SE Gen AI Project",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin()],
)
'''
#Home Page
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
    return render_template('starter-page.html'),200

#Dashboard
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
    return render_template('dashboard_copy.html'),200

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
    return jsonify({'response': chatbot_response}),200
      

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



'''
@app.route('/dashboard/activityquestion')
def activityquestion():

    """
    ---
    get:
      summary: Activity Question Page
      description: Route for activity question page
      responses:
        200:
          description: Success
    """       
    return render_template('activityquestion.html'),200

@app.route('/api/dashboard/activityquestion')
def activityquestion_api():

    """
    ---
    post:
      summary: Activity Question Page Details
      description: Activity Question Page populated with details
      responses:
        200:
          description: Success
    """       
    return 


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


'''


@app.route('/dashboard/gradedassignment')
def gradedassignment():

    """
    ---
    get:
      summary: Graded Assignment Page
      description: Graded Assignment Page populated with details 
      responses:
        200:
          description: Success
    """       
    return render_template('ga_copy.html')

"""
# Register paths with the spec
with app.test_request_context():
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            spec.path(view=app.view_functions[rule.endpoint])

# Output the spec to a YAML file
with open('se_api.yaml', 'w') as file:
    yaml.dump(spec.to_dict(), file)
"""

if __name__ == '__main__':
    app.run(debug=True)
    
