from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
import pyrebase
from firebase_config import firebase_config
from kivy.lang import Builder

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

class LoginScreen(Screen):
    def login_user(self, email, password):
        email = email.strip()
        password = password.strip()

        if not email or not password:
            toast("Email ve şifre boş olamaz.")
            return

        try:
            auth.sign_in_with_email_and_password(email, password)
            toast("Giriş başarılı!")
            self.manager.current = "home"
        except Exception as e:
            toast("Giriş başarısız. Bilgileri kontrol edin.")
            print("Login error:", e)

import re

def is_valid_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def login_user(self, email, password):
    email = email.strip()
    password = password.strip()

    if not email or not password:
        toast("Email ve şifre boş olamaz.")
        return

    if not is_valid_email(email):
        toast("Geçerli bir email girin.")
        return

    try:
        auth.sign_in_with_email_and_password(email, password)
        toast("Giriş başarılı!")
        self.manager.current = "home"
    except Exception as e:
        toast("Giriş başarısız. Bilgileri kontrol edin.")
        print("Login error:", e)



Builder.load_string("""
<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(24)
        spacing: dp(20)

        MDTopAppBar:
            title: "Giriş Yap"
            elevation: 5
            pos_hint: {"top": 1}
            left_action_items: [["arrow-left", lambda x: app.go_to('welcome')]]
            height: dp(56)
        
        Widget:  # Üst boşluk

        MDTextField:
            id: email
            hint_text: "E-posta"
            icon_left: "email"
            mode: "rectangle"
            size_hint_x: 1
            pos_hint: {"center_x": 0.5}
        
        MDTextField:
            id: password
            hint_text: "Şifre"
            icon_left: "lock"
            password: True
            mode: "rectangle"
            size_hint_x: 1
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Giriş Yap"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.7
            on_release: root.login_user(email.text, password.text)
                    
        MDTextButton:
            text: "Hesabın yok mu? Kayıt ol"
            on_release: root.manager.current = "signup"
                    
        Widget:  # Alt boşluk
        
       


""")