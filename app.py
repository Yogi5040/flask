## Create a simple flask application	

from flask import Flask,redirect,url_for,render_template

# create the application

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello world!</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to Flask application"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the score is "+str(score)


if __name__ == '__main__':
    app.run(debug=True)

