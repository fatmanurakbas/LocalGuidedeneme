from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def go_to_login(self):
        self.manager.current = "login"
        
    def go_to_signup(self):
        self.manager.current = "signup"

Builder.load_string("""
<WelcomeScreen>:
    name: "welcome"
    
    canvas.before:
        Color:
            rgba: 0.36, 0.8, 0.94, 1  # #5CCBF0 in RGBA
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"
        padding: dp(30)
        spacing: dp(20)
        
        Widget:
            size_hint_y: 0.2
            
        MDLabel:
            text: "LOCAL GUIDE"
            font_style: "H3"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_y: 0.2
            
        MDLabel:
            text: "WELCOME TO LOCALGUIDE!"
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: 0.1
            
        Widget:
            size_hint_y: 0.2
            
        MDFillRoundFlatButton:
            text: "GİRİŞ YAP"
            font_size: "18sp"
            size_hint: 0.8, None
            height: dp(56)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.11, 0.17, 0.29, 1  # #1B2C49 in RGBA
            on_release: root.go_to_login()
            
        MDFillRoundFlatButton:
            text: "KAYIT OL"
            font_size: "18sp"
            size_hint: 0.8, None
            height: dp(56)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.11, 0.17, 0.29, 1  # #1B2C49 in RGBA
            on_release: root.go_to_signup()
            
        Widget:
            size_hint_y: 0.1
            
        MDLabel:
            text: "Türkiye'nin en iyilerini keşfedin"
            font_style: "Body1"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: 0.1
""")