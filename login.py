# login.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
import pyrebase
from firebase_config import firebase, auth
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
import re
from theme import *

class LoginScreen(Screen):
    def on_enter(self, *args):
        # Reset fields
        self.ids.email.text = ""
        self.ids.password.text = ""
        
        # Add animations when screen is shown
        Clock.schedule_once(self.animate_elements, 0.2)
    
    def animate_elements(self, dt):
        # Animate the card
        card_anim = Animation(opacity=1, pos_hint={"center_y": 0.5}, duration=0.5, t='out_cubic')
        card_anim.start(self.ids.login_card)
    
    def login_user(self, email, password):
        email = email.strip()
        password = password.strip()

        if not email or not password:
            toast("Email ve şifre boş olamaz.")
            return
        
        if not self.is_valid_email(email):
            toast("Geçerli bir email girin.")
            return

        self.ids.login_button.disabled = True
        self.show_loading_indicator(True)
        
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.show_loading_indicator(False)
            toast("Giriş başarılı!")
            self.manager.transition.direction = 'left'
            self.manager.current = "home"
        except Exception as e:
            self.show_loading_indicator(False)
            toast("Giriş başarısız. Bilgileri kontrol edin.")
            print("Login error:", e)
        finally:
            self.ids.login_button.disabled = False
    
    def show_loading_indicator(self, show):
        self.ids.login_spinner.opacity = 1 if show else 0
        self.ids.login_spinner.active = show
    
    def is_valid_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None

    def forgot_password(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password"

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import theme theme

<LoginScreen>:
    name: "login"
    
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1  # Açık gri arka plan
        Rectangle:
            pos: self.pos
            size: self.size
    
    MDBoxLayout:
        orientation: "vertical"
        padding: 0
        
        MDTopAppBar:
            title: "Giriş Yap            "
            elevation: 1
            md_bg_color: get_color_from_hex("#474ED7")  # Koyu mavi
            specific_text_color: "white"
            left_action_items: [["arrow-left", lambda x: app.go_to('welcome')]]
            height: dp(56)
        
        MDFloatLayout:
            
            MDCard:
                id: login_card
                orientation: "vertical"
                padding: dp(24)
                spacing: dp(15)
                size_hint: None, None
                size: min(dp(400), root.width - dp(16)), dp(500)
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (0, 1)
                md_bg_color: 1, 1, 1, 1  # Beyaz
                opacity: 0
                radius: [dp(4)]
                
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(4)
                    padding: [0, 0, 0, dp(20)]
                    
                    MDLabel:
                        text: "Local Guide'a Hoş Geldiniz"
                        font_style: "H6"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Primary"
                        bold: True
                    
                    MDLabel:
                        text: "Hesabınıza giriş yapın"
                        font_style: "Body1"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Secondary"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(15)
                    adaptive_height: True
                    size_hint_y: None
                    height: dp(140)
                
                    MDRelativeLayout:
                        size_hint_y: None
                        height: email.height
                        
                        MDTextField:
                            id: email
                            hint_text: "E-posta"
                            icon_left: "email"
                            mode: "fill"
                            size_hint_x: 1
                            line_color_normal: [0.7, 0.7, 0.7, 1]
                            line_color_focus: get_color_from_hex("#474ED7")
                            
                    
                    MDRelativeLayout:
                        size_hint_y: None
                        height: password.height
                        
                        MDTextField:
                            id: password
                            hint_text: "Şifre"
                            icon_left: "lock"
                            password: True
                            mode: "fill"
                            size_hint_x: 1
                            line_color_normal: [0.7, 0.7, 0.7, 1]
                            line_color_focus: get_color_from_hex("#474ED7")
                            
                
                Widget:
                    size_hint_y: None
                    height: dp(20)
                    
                MDFillRoundFlatButton:
                    id: login_button
                    text: "GİRİŞ YAP"
                    font_size: theme.FONT_SIZE_BUTTON
                    pos_hint: {"center_x": 0.5}
                    size_hint_x: 1
                    md_bg_color: get_color_from_hex(theme.PRIMARY_COLOR)
                    on_release: root.login_user(email.text, password.text)
                    
                Widget:
                    size_hint_y: None
                    height: dp(15)
                    
                MDTextButton:
                    text: "Şifremi Unuttum"
                    pos_hint: {"center_x": 0.5}
                    theme_text_color: "Custom"
                    text_color: get_color_from_hex("#474ED7")
                    font_style: "Caption"
                    font_name: "Roboto"
                    on_release: root.forgot_password()
                    
                Widget:
                    size_hint_y: None
                    height: dp(25)
                    
                MDBoxLayout:
                    orientation: "horizontal"
                    adaptive_height: True
                    spacing: dp(8)
                    pos_hint: {"center_x": 0.5}
                    
                    MDLabel:
                        text: "Hesabın yok mu?"
                        font_style: "Body2"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Secondary"
                        halign: "right"
                    
                    MDTextButton:
                        text: "Kayıt ol"
                        font_style: "Body2"
                        theme_text_color: "Primary"
                        bold: True
                        on_release: root.manager.current = "signup"
                    
                    MDSpinner:
                        id: login_spinner
                        size_hint: None, None
                        size: dp(36), dp(36)
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        active: False
                        opacity: 0
""")
