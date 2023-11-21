
from flask import Flask, session, render_template, request, redirect
import pyrebase
import firebase_admin
from firebase_admin import firestore, credentials
from flask_wtf import FlaskForm



app = Flask(__name__)

config = {    
    'apiKey': "AIzaSyDoZdVffsnC7h6FsYO5aPvaELW2BLERW9Y",
    'authDomain': "advisor-dev-95e86.firebaseapp.com",
    'projectId': "advisor-dev-95e86",
    'storageBucket': "advisor-dev-95e86.appspot.com",
    'messagingSenderId': "162788724888",
    'appId': "1:162788724888:web:8240e343dfba0beade80ed",
    'databaseURL' : 'https://advisor-dev-95e86-default-rtdb.firebaseio.com/'
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.secret_key = 'secret-key'

@app.route('/', methods = ['POST', 'GET'])
def index():
    if('user' in session):
        return redirect('/select_role')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('Password')
        try: 
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
        except: 
            return 'Failed to log in '
    return render_template('login.html')

@app.route('/select_role', methods=['POST', 'GET'])
def select_role():
    if 'user' not in session: 
        return redirect('/')
    if request.method == 'POST':
        role = request.form.get('role')
        print(role)
        if role == 'student':
            return render_template('student_page.html') # Redirect to student page
        elif role == 'advisor':
            return render_template('advisor_page.html') # Redirect to advisor page

    return render_template('select_role.html')


@app.route('/student_page', methods = ['POST', 'GET'])
def student_page():
    if 'user' not in session: 
        return redirect('/')
    if request.method =='POST':
        option = request.form.get('action')
        if option == 'action1':
            return render_template('add_classes.html')
        elif option =='action2':
            return 'action2 selected'
    
    return render_template('student_page.html')

@app.route('/advisor_page', methods = ['POST', 'GET'])
def advisor_page():
    if 'user' not in session: 
        return redirect('/')
    if request.method =='POST':
        option = request.form.get('option')
        if option == 'option1':
            return 'option1 selected'
        elif option =='option2':
            return 'option2 selected'
    return render_template('advisor_page.html')

@app.route('/add_classes.html', methods = ['POST', 'GET'])
def add_classes():
    if 'user' not in session: 
        return redirect('/')
    if request.method =='POST':
        class_name = request.form.get('className')
        class_credits = request.form.get('creditNumber')
        class_grade = request.form.get('grade')
        db.child("names").push({'class_name': class_name,'class_credits': class_credits, 'class_grade': class_grade})
        return redirect('/student_page')
    return render_template('add_classes.html')

    


    

@app.route('/logout')
def logout():
    session.pop('user')
    return(redirect('/'))

if __name__ == '__main__':
    app.run(port = 1111)

