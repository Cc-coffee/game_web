from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
Moment(app)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/test')
def test():
    return render_template('index6.html')

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/button')
def button():
    return render_template('personal/button.html')




if __name__ == '__main__':
    app.run()
