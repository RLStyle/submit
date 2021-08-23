import flask
from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/requests')
def requests():
    return render_template('requests.json')

if(__name__ == '__main__'):
    app.run(debug=True)