from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyAxcCB_Vt_QaFwgy21jDur9Ws6SAaN0l7U",
  "authDomain": "spacetech-b6d70.firebaseapp.com",
  "databaseURL": "https://spacetech-b6d70-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "spacetech-b6d70",
  "storageBucket": "spacetech-b6d70.appspot.com",
  "messagingSenderId": "135550954029",
  "appId": "1:135550954029:web:8e3c915fe24cd60aaae6a4",
  "measurementId": "G-SL5DDMWVY0",
  "databaseURL": "https://spacetech-b6d70-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def index():
        return render_template('index.html')

@app.route('/planet1', methods = ['GET', 'POST'])  # '/' for the default page
def planet1():
        return render_template('planet1.html')

@app.route('/planet2', methods = ['GET', 'POST'])  # '/' for the default page
def planet2():
        return render_template('planet2.html')

@app.route('/planet3', methods = ['GET', 'POST'])  # '/' for the default page
def planet3():
        return render_template('planet3.html')

@app.route('/form', methods = ['GET', 'POST'])  # '/' for the default page
def form():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        full_name = request.form['full_name']
        user = {"full_name": full_name, "username": username}
        #db.child("Users").child(login_session['user'])
        #['localId'].set(user)
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        db.child('Users').child(login_session['user']['localId']).set(user)
        try:
            return redirect(url_for('form2'))
        except:
            print("Authentication failed")
            return ('error')
    else:
        return render_template('form.html')

@app.route('/signin', methods=['GET', 'POST'])
def form2():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)

        try:
            return redirect(url_for('planetx'))
        except:
            error = "Authentication failed"
    return render_template("form2.html")

@app.route('/planetx', methods = ['GET', 'POST'])  # '/' for the default page
def planetx():
    username = db.child('Users').child(login_session['user']['localId']).get().val()
    return render_template('planetx.html', username = username)







#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)