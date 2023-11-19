import pyrebase

config = {    
    'apiKey': "AIzaSyDoZdVffsnC7h6FsYO5aPvaELW2BLERW9Y",
    'authDomain': "advisor-dev-95e86.firebaseapp.com",
    'projectId': "advisor-dev-95e86",
    'storageBucket': "advisor-dev-95e86.appspot.com",
    'messagingSenderId': "162788724888",
    'appId': "1:162788724888:web:8240e343dfba0beade80ed",
    'databaseURL' : ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)

user = auth.sign_in_with_email_and_password(email,password)
# info = auth.get_account_info(user['idToken'])
# print(info)

