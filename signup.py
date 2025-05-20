# signup.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
import pyrebase
from firebase_config import firebase, auth, db
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
import json
import re
from theme import *

class SignUpScreen(Screen):
    def on_enter(self, *args):
        # Reset fields
        self.ids.name.text = ""
        self.ids.surname.text = ""
        self.ids.email.text = ""
        self.ids.password.text = ""
        
        # Add animations when screen is shown
        Clock.schedule_once(self.animate_elements, 0.2)
    
    def animate_elements(self, dt):
        # Animate the card
        card_anim = Animation(opacity=1, pos_hint={"center_y": 0.5}, duration=0.5, t='out_cubic')
        card_anim.start(self.ids.signup_card)
    
    def is_valid_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None
    
    def validate_password(self, password):
        if len(password) < 6:
            return False
        return True
    
    def register_user(self, name, surname, email, password):
        # Validate inputs
        name = name.strip()
        surname = surname.strip()
        email = email.strip()
        password = password.strip()
        
        if not name or not surname or not email or not password:
            toast("Lütfen tüm alanları doldurun.")
            return
        
        if not self.is_valid_email(email):
            toast("Geçerli bir email adresi girin.")
            return
        
        if not self.validate_password(password):
            toast("Şifre en az 6 karakter uzunluğunda olmalıdır.")
            return
        
        # Show loading indicator and disable button
        self.ids.signup_button.disabled = True
        self.show_loading_indicator(True)

        try:
            # Create user
            user = auth.create_user_with_email_and_password(email, password)
            print("Kullanıcı oluşturuldu:", user)  # Debug için
            
            # Save user data to database
            user_data = {
                "name": name,
                "surname": surname,
                "email": email
            }
            
            try:
                db.child("users").child(user['localId']).set(user_data)
                print("Veritabanına kayıt başarılı")  # Debug için
                self.show_loading_indicator(False)
                toast("Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
                self.manager.transition.direction = 'right'
                self.manager.current = "login"
            except Exception as db_error:
                print("Veritabanı hatası:", str(db_error))  # Debug için
                # Even with database error, user was created so continue
                self.show_loading_indicator(False)
                toast("Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
                self.manager.transition.direction = 'right'
                self.manager.current = "login"
                
        except Exception as e:
            self.show_loading_indicator(False)
            error_message = str(e)
            print("Hata detayı:", error_message)  # Debug için
            
            try:
                error_dict = json.loads(error_message)
                error_code = error_dict.get('error', {}).get('code', '')
                error_message = error_dict.get('error', {}).get('message', '')
                print("Hata kodu:", error_code)  # Debug için
                print("Hata mesajı:", error_message)  # Debug için
            except:
                pass

            if "EMAIL_EXISTS" in error_message:
                toast("Bu email adresi zaten kullanımda. Lütfen başka bir email adresi deneyin veya giriş yapın.")
            elif "INVALID_EMAIL" in error_message:
                toast("Geçersiz email adresi. Lütfen geçerli bir email adresi girin.")
            elif "WEAK_PASSWORD" in error_message:
                toast("Şifre çok zayıf. Lütfen daha güçlü bir şifre seçin.")
            elif "400" in error_message:
                toast("Kayıt işlemi başarısız oldu. Lütfen bilgilerinizi kontrol edip tekrar deneyin.")
            elif "401" in error_message:
                toast("Yetkilendirme hatası. Lütfen daha sonra tekrar deneyin.")
            elif "403" in error_message:
                toast("Erişim engellendi. Lütfen daha sonra tekrar deneyin.")
            elif "404" in error_message:
                toast("Sunucu hatası. Lütfen daha sonra tekrar deneyin.")
            else:
                toast("Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        finally:
            self.ids.signup_button.disabled = False
    
    def show_loading_indicator(self, show):
        self.ids.signup_spinner.opacity = 1 if show else 0
        self.ids.signup_spinner.active = show

Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import theme theme

<SignUpScreen>:
    name: "signup"
    
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
            title: "Kayıt Ol            "
            elevation: 1
            md_bg_color: get_color_from_hex("#474ED7")  # Koyu mavi
            specific_text_color: "white"
            left_action_items: [["arrow-left", lambda x: app.go_to('welcome')]]
            height: dp(56)
        
        MDFloatLayout:
            
            MDCard:
                id: signup_card
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(20)
                size_hint: None, None
                size: min(dp(400), root.width - dp(48)), dp(550)
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                elevation: 8
                shadow_softness: 10
                shadow_offset: (0, 4)
                md_bg_color: get_color_from_hex(theme.CARD_COLOR)
                opacity: 0
                radius: [dp(4)]
                
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: dp(4)
                    padding: [0, 0, 0, dp(20)]
                    
                    Widget:
                        size_hint_y: None
                        height: dp(20)

                    MDLabel:
                        text: "Yeni Hesap Oluştur"
                        font_style: "H6"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Primary"
                        bold: True
                    
                    MDLabel:
                        text: "Local Guide'a hoş geldiniz!"
                        font_style: "Body1"
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        theme_text_color: "Secondary"
                        
                
                MDTextField:
                    id: name
                    hint_text: "Ad"
                    icon_left: "account"
                    mode: "fill"
                    size_hint_x: 1
                    line_color_normal: get_color_from_hex(theme.PRIMARY_COLOR)
                    line_color_focus: get_color_from_hex(theme.PRIMARY_COLOR)
                
                MDTextField:
                    id: surname
                    hint_text: "Soyad"
                    icon_left: "account"
                    mode: "fill"
                    size_hint_x: 1
                    line_color_normal: get_color_from_hex(theme.PRIMARY_COLOR)
                    line_color_focus: get_color_from_hex(theme.PRIMARY_COLOR)
                
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
                
                MDTextField:
                    id: password
                    hint_text: "Şifre"
                    icon_left: "lock"
                    password: True
                    mode: "fill"
                    size_hint_x: 1
                    line_color_normal: get_color_from_hex(theme.PRIMARY_COLOR)
                    line_color_focus: get_color_from_hex(theme.PRIMARY_COLOR)
                    helper_text_mode: "on_focus"
                    helper_text: "Şifreniz en az 6 karakter uzunluğunda olmalıdır"
                                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    padding: [0, dp(10), 0, dp(10)]
                    
                    Widget:
                        size_hint_y: None
                        height: dp(95)

                    MDFillRoundFlatButton:
                        id: signup_button
                        text: "KAYIT OL"
                        font_size: theme.FONT_SIZE_BUTTON
                        pos_hint: {"center_x": 0.5}
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex(theme.PRIMARY_COLOR)
                        on_release: root.register_user(name.text, surname.text, email.text, password.text)
                        
                    MDBoxLayout:
                        orientation: "horizontal"
                        adaptive_height: True
                        spacing: dp(8)
                        pos_hint: {"center_x": 0.5}
                        
                        MDLabel:
                            text: "Zaten hesabın var mı?"
                            font_style: "Body2"
                            size_hint_y: None
                            height: self.texture_size[1]
                            theme_text_color: "Secondary"
                            halign: "right"
                        
                        MDTextButton:
                            text: "Giriş yap"
                            font_style: "Body2"
                            theme_text_color: "Primary"
                            bold: True
                            on_release: root.manager.current = "login"
                    
                    MDSpinner:
                        id: signup_spinner
                        size_hint: None, None
                        size: dp(36), dp(36)
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        active: False
                        opacity: 0
""")
