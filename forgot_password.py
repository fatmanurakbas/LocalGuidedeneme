# forgot_password.py
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from firebase_config import auth
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
import re
from theme import *

class ForgotPasswordScreen(Screen):
    def on_enter(self, *args):
        # Reset field
        self.ids.email.text = ""
        
        # Add animation when screen is shown
        Clock.schedule_once(self.animate_elements, 0.2)
    
    def animate_elements(self, dt):
        # Animate the card
        card_anim = Animation(opacity=1, pos_hint={"center_y": 0.5}, duration=0.5, t='out_cubic')
        card_anim.start(self.ids.forgot_card)
    
    def is_valid_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None
    
    def send_verification(self, email):
        email = email.strip()
        if not email:
            toast("Lütfen email adresinizi girin.")
            return
        
        if not self.is_valid_email(email):
            toast("Geçerli bir email adresi girin.")
            return
        
        # Show loading indicator and disable button
        self.ids.reset_button.disabled = True
        self.show_loading_indicator(True)
        
        try:
            auth.send_password_reset_email(email)
            self.show_loading_indicator(False)
            toast("Şifre sıfırlama bağlantısı email adresinize gönderildi.")
            self.manager.transition.direction = 'right'
            self.manager.current = "login"
        except Exception as e:
            self.show_loading_indicator(False)
            toast("Email gönderilirken bir hata oluştu. Lütfen email adresinizi kontrol edin.")
            print("Error:", e)
        finally:
            self.ids.reset_button.disabled = False
    
    def show_loading_indicator(self, show):
        self.ids.reset_spinner.opacity = 1 if show else 0
        self.ids.reset_spinner.active = show

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import theme theme

<ForgotPasswordScreen>:
    name: "forgot_password"
    
    canvas.before:
        Color:
            rgba: get_color_from_hex(theme.BACKGROUND_COLOR)
        Rectangle:
            pos: self.pos
            size: self.size
            
    MDBoxLayout:
        orientation: "vertical"
        padding: 0
        
        MDTopAppBar:
            title: "Şifremi Unuttum"
            elevation: 1
            md_bg_color: get_color_from_hex(theme.PRIMARY_COLOR)
            specific_text_color: "white"
            left_action_items: [["arrow-left", lambda x: app.go_to('login')]]
            shadow_softness: 8
            shadow_offset: (0, 2)
        
        MDFloatLayout:
            
            MDCard:
                id: forgot_card
                orientation: "vertical"
                padding: dp(24)
                spacing: dp(20)
                size_hint: None, None
                size: min(dp(400), root.width - dp(48)), dp(350)
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                elevation: 8
                shadow_softness: 10
                shadow_offset: (0, 4)
                md_bg_color: get_color_from_hex(theme.CARD_COLOR)
                opacity: 0
                radius: [10, 10, 10, 10]
                
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(8)
                    padding: [0, 0, 0, dp(20)]
                    
                    MDLabel:
                        text: "Şifremi Unuttum"
                        font_style: "H5"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Primary"
                        bold: True
                    
                    MDLabel:
                        text: "Şifre sıfırlama bağlantısı için email adresinizi girin"
                        font_style: "Subtitle1"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Secondary"
                        
                
                MDTextField:
                    id: email
                    hint_text: "E-posta"
                    icon_left: "email"
                    mode: "fill"
                    size_hint_x: 1
                    line_color_normal: get_color_from_hex(theme.PRIMARY_COLOR)
                    line_color_focus: get_color_from_hex(theme.PRIMARY_COLOR)
                    helper_text_mode: "on_error"
                    helper_text: "Geçerli bir email adresi girin"
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    padding: [0, dp(20), 0, dp(10)]
                    
                    Widget:
                        size_hint_y: None
                        height: dp(20)

                    MDFillRoundFlatButton:
                        id: reset_button
                        text: "BAĞLANTI GÖNDER"
                        font_size: theme.FONT_SIZE_BUTTON
                        pos_hint: {"center_x": 0.5}
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex(theme.PRIMARY_COLOR)
                        on_release: root.send_verification(email.text)
                    
                    MDTextButton:
                        text: "Giriş sayfasına dön"
                        theme_text_color: "Primary"
                        font_style: "Body2"
                        pos_hint: {"center_x": 0.5}
                        on_release: root.manager.current = "login"
                
                MDSpinner:
                    id: reset_spinner
                    size_hint: None, None
                    size: dp(36), dp(36)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False
                    opacity: 0
""")
