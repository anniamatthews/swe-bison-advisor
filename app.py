
from flask import Flask, session, render_template, request, redirect
import pyrebase
import firebase_admin
from firebase_admin import firestore, credentials, db
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
            return render_template('student_resource_location_a.html')
        elif option == 'action3':
            return render_template('self_service_resources.html')
    
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

@app.route("/postskill",methods=["POST","GET"])
def postskill():
    if 'user' not in session: 
        return redirect('/')
    if request.method =='POST':
        # this needs to be a loop or something so that it can be stored into the db
        
        names = request.form.getlist('name[]')
        credits = request.form.getlist('credit[]')
        grades = request.form.getlist('grade[]')
        

        for i in range(len(names)):
            new_entry_ref = db.child("names").push(data={
                'class_name': names[i],
                'class_credits': credits[i],
                'class_grade': grades[i]
            })
            



    # next step: openAI integration: https://www.youtube.com/watch?v=Vo1_9-qVCM4
       
        
    return render_template('add_classes.html')





    

@app.route('/logout')
def logout():
    session.pop('user')
    return(redirect('/'))

if __name__ == '__main__':
    app.run(port = 1111)

