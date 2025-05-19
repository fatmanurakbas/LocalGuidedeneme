from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
import pyrebase
from firebase_config import firebase_config

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


from kivymd.toast import toast
from firebase_config import auth

class SignUpScreen(Screen):
    def register_user(self, email, password):
        try:
            auth.create_user_with_email_and_password(email, password)
            toast("Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
            self.manager.current = "login"  # Giriş ekranına yönlendir
        except Exception as e:
            toast("Kayıt başarısız: " + str(e))




Builder.load_string("""
<SignUpScreen>:
    name: "signup"
    BoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        MDTopAppBar:
            title: "Kayıt Ol"
            elevation: 4
            pos_hint: {"top": 1}
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
            text: "Kayıt Ol"
            pos_hint: {"center_x": 0.5}
            on_release: root.register_user(email.text, password.text)
        MDTextButton:
            text: "Zaten hesabın var mı? Giriş yap"
            on_release: root.manager.current = "login"
        Widget:  # Alt boşluk
""")
