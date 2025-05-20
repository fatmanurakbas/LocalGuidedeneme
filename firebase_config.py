import pyrebase
import os

firebase_config = {
  "apiKey": "AIzaSyABgJnv0DNfzBvevwk6_odkPwPsCbvqDv0",
  "authDomain": "localguide-76436.firebaseapp.com",
  "projectId": "localguide-76436",
  "storageBucket": "localguide-76436.firebasestorage.app",
  "messagingSenderId": "867602781343",
  "appId": "1:867602781343:web:b34a5726e56bdef7ae7eaa",
  "measurementId": "G-35SKKGPP04",
  "databaseURL": "https://localguide-76436.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()