from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def index():
        return render_template('index.html')

@app.route('/planet1', methods = ['GET', 'POST'])  # '/' for the default page
def planet1():
        return render_template('planet1.html')



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)