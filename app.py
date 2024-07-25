from flask import Flask, render_template

app = Flask(__name__)

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
