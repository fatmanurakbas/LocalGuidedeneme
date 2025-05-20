# welcome_screen.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.clock import Clock
from theme import *
from kivy.core.text import LabelBase
from theme import *
#fontları tanımlıyorum

LabelBase.register(name="MyFont1", fn_regular="font/ShareTech-Regular.ttf")
LabelBase.register(name="MyFont2", fn_regular="font/Kanit-Regular.ttf")
LabelBase.register(name="MyFont3", fn_regular="font/CherryBombOne-Regular.ttf")
LabelBase.register(name="MyFont4", fn_regular="font/Underdog-Regular.ttf")

class WelcomeScreen(Screen):
    def on_enter(self):
        # Add animations when screen is shown
        Clock.schedule_once(self.animate_elements, 0.2)
    
    def animate_elements(self, dt):
        # Animate logo
        logo_anim = Animation(opacity=1, size_hint_y=0.2, duration=0.8, t='out_cubic')
        logo_anim.start(self.ids.logo_label)
        
        # Animate title
        title_anim = Animation(opacity=1, size_hint_y=0.1, duration=0.8, t='out_cubic')
        title_anim.start(self.ids.title_label)
        
        # Animate buttons with sequence
        Clock.schedule_once(lambda dt: self.animate_button(self.ids.login_button), 0.3)
        Clock.schedule_once(lambda dt: self.animate_button(self.ids.signup_button), 0.5)
        
        # Animate footer
        footer_anim = Animation(opacity=1, duration=1.2, t='out_cubic')
        footer_anim.start(self.ids.footer_label)
    
    def animate_button(self, button):
        button_anim = Animation(opacity=1, size_hint_x=0.8, duration=0.5, t='out_cubic')
        button_anim.start(button)
        
    def go_to_login(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "login"
        
    def go_to_signup(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "signup"

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import theme theme

<WelcomeScreen>:
    name: "welcome"
    
    canvas.before:
        Color:
            rgba: get_color_from_hex(theme.PRIMARY_COLOR)
        Rectangle:
            pos: self.pos
            size: self.size
        
        # Add gradient overlay
        Color:
            rgba: get_color_from_hex(theme.SECONDARY_COLOR)[0], get_color_from_hex(theme.SECONDARY_COLOR)[1], get_color_from_hex(theme.SECONDARY_COLOR)[2], 0.7
        Rectangle:
            pos: self.pos
            size: self.size
            
    BoxLayout:
        orientation: "vertical"
        padding: [dp(30), dp(50), dp(30), dp(50)]
        spacing: dp(30)
        
        Widget:
            size_hint_y: 0.1
            
        MDLabel:
            id: logo_label
            text: "LOCAL GUIDE"
            font_style: "H3"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_y: 0.15
            opacity: 0
            font_name: "MyFont1"
            font_size: "32sp"
            
        MDLabel:
            id: title_label
            text: "Gez, Gör, Keşfet!"
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.95
            size_hint_y: 0.05
            opacity: 0
            font_name: "MyFont2"
            
        Widget:
            size_hint_y: 0.1
            
        MDFillRoundFlatButton:
            id: login_button
            text: "GİRİŞ YAP"
            font_size: theme.FONT_SIZE_BUTTON
            size_hint: 0.5, None
            height: dp(56)
            pos_hint: {"center_x": 0.5}
            md_bg_color: get_color_from_hex(theme.ACCENT_COLOR)
            text_color: 1, 1, 1, 1
            opacity: 0
            ripple_scale: 0.85
            elevation: 8
            on_release: root.go_to_login()
            
        MDFillRoundFlatButton:
            id: signup_button
            text: "KAYIT OL"
            font_size: theme.FONT_SIZE_BUTTON
            size_hint: 0.5, None
            height: dp(56)
            pos_hint: {"center_x": 0.5}
            md_bg_color: [1, 1, 1, 0.2]
            text_color: 1, 1, 1, 1
            opacity: 0
            ripple_scale: 0.85
            elevation: 6
            on_release: root.go_to_signup()
            
        Widget:
            size_hint_y: 0.15
            
        MDLabel:
            id: footer_label
            text: "Türkiye'nin en iyilerini keşfedin!"
            font_style: "Subtitle1"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: 0.05
            opacity: 0
            font_name: "MyFont3"
""")
