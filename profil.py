from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from firebase_config import auth, db
from kivymd.toast import toast
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from os.path import expanduser



# Dialog sınıfını kaldırıyoruz çünkü artık kullanmıyoruz

class ProfileScreen(Screen):
    def on_enter(self, *args):
        self.load_user_data()

    def select_profile_image(self):
        content = FileChooserIconView(filters=["*.png", "*.jpg", "*.jpeg"])
        home = expanduser("~")
        content.path = f"{home}/Pictures"


        popup = Popup(title="Fotoğraf Seç", content=content, size_hint=(0.9, 0.9))

        def on_file_selected(instance, selection):
           if selection:
               selected_file = selection[0]
               self.ids.profile_image.source = selected_file
               popup.dismiss()

        content.bind(on_submit=lambda instance, selection, touch: on_file_selected(instance, selection))
        popup.open()


    def go_to_edit_profile(self):
        self.manager.transition.direction = "left"
        self.manager.current = "edit_profile"

    def go_to_notification_settings(self):
        self.manager.transition.direction = "left"
        self.manager.current = "notification_settings"

    def go_to_theme_settings(self):
        self.manager.transition.direction = "left"
        self.manager.current = "theme_settings"

    def go_to_account_security(self):
        self.manager.transition.direction = "left"
        self.manager.current = "account_security"
    
    def load_user_data(self):
        try:
            # Mevcut kullanıcının bilgilerini al
            user = auth.current_user
            if user:
                # Firebase'den kullanıcı verilerini çek
                user_data = db.child("users").child(user['localId']).get().val()
                if user_data:
                    # Profil bilgilerini güncelle
                    self.ids.profile_name.text = f"{user_data.get('name', '')} {user_data.get('surname', '')}"
                    self.ids.profile_username.text = f"@{user_data.get('name', '').lower()}{user_data.get('surname', '').lower()}"
                    self.ids.profile_email.text = user_data.get('email', '')
        except Exception as e:
            print("Profil yükleme hatası:", e)
            toast("Profil bilgileri yüklenirken bir hata oluştu.")
    
    def redirect_to_forgot_password(self):
        """Kullanıcıyı şifre sıfırlama sayfasına yönlendirir"""
        self.manager.transition.direction = 'left'
        self.manager.current = "forgot_password"
        toast("Şifre sıfırlama sayfasına yönlendiriliyorsunuz...")

    def logout(self):
        try:
            auth.current_user = None
            self.manager.transition.direction = 'right'
            self.manager.current = "welcome"
            toast("Başarıyla çıkış yapıldı")
        except Exception as e:
            print("Çıkış yapma hatası:", e)
            toast("Çıkış yapılırken bir hata oluştu")

Builder.load_string('''
<ProfileScreen>:
    name: "profile"

    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Profilim        "
            elevation: 5
            md_bg_color: "#5C6BC0"
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(20)
                size_hint_y: None
                adaptive_height: True
                    

                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: None, None
                    size: dp(130), dp(130)
                    pos_hint: {"center_x": 0.5}
                    on_touch_down:
                        if self.collide_point(*args[1].pos): root.select_profile_image()

                    Image:
                        id: profile_image
                        source: "default_profile.png"
                        size_hint: 1, 1
                        allow_stretch: True
                        keep_ratio: True
                        canvas.before:
                            Color:
                                rgba: 0.8, 0.8, 0.8, 1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [100]
    


                MDLabel:
                    id: profile_name
                    text: ""
                    halign: "center"
                    font_style: "H6"

                MDLabel:
                    id: profile_username
                    text: ""
                    halign: "center"
                    font_style: "Subtitle2"

                MDLabel:
                    id: profile_email
                    text: ""
                    halign: "center"
                    font_style: "Body2"

                MDLabel:
                    id: profile_bio
                    text: ""
                    halign: "center"
                    font_style: "Body2"
                    theme_text_color: "Secondary"

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                    MDLabel:
                        text: "Takipçi: 0"
                        halign: "center"

                    MDLabel:
                        text: "Takip: 0"
                        halign: "center"

                    MDLabel:
                        text: "Gönderi: 0"
                        halign: "center"

                MDCard:
                    orientation: "vertical"
                    padding: dp(16)
                    spacing: dp(16)
                    size_hint_y: None
                    height: self.minimum_height
                    md_bg_color: 0.95, 0.95, 0.95, 1
                    radius: [dp(8)]
                    
                    MDLabel:
                        text: "Hesap Ayarları"
                        font_style: "H6"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDRaisedButton:
                        text: "Profili Düzenle"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#5C6BC0"
                        elevation: 2
                        on_release: root.go_to_edit_profile()
                        
                    MDRaisedButton:
                        text: "Parola Değiştir"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#5C6BC0"
                        elevation: 2
                        on_release: root.redirect_to_forgot_password()
                
                MDCard:
                    orientation: "vertical"
                    padding: dp(16)
                    spacing: dp(16)
                    size_hint_y: None
                    height: self.minimum_height
                    md_bg_color: 0.95, 0.95, 0.95, 1
                    radius: [dp(8)]
                    
                    MDLabel:
                        text: "Uygulama Ayarları"
                        font_style: "H6"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDRaisedButton:
                        text: "Bildirim Ayarları"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#5C6BC0"
                        elevation: 2
                        on_release: root.go_to_notification_settings()

                    MDRaisedButton:
                        text: "Tema Ayarları"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#5C6BC0"
                        elevation: 2
                        on_release: root.go_to_theme_settings()
                
                MDCard:
                    orientation: "vertical"
                    padding: dp(16)
                    spacing: dp(16)
                    size_hint_y: None
                    height: self.minimum_height
                    md_bg_color: 0.95, 0.95, 0.95, 1
                    radius: [dp(8)]
                    
                    MDLabel:
                        text: "Güvenlik"
                        font_style: "H6"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDRaisedButton:
                        text: "Hesabı Dondur veya Sil"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#FF5252"
                        text_color: 1, 1, 1, 1
                        elevation: 2
                        on_release: root.go_to_account_security()

                    MDRaisedButton:
                        text: "Çıkış Yap"
                        size_hint_x: 1
                        height: dp(48)
                        md_bg_color: "#FF5252"
                        text_color: 1, 1, 1, 1
                        elevation: 2
                        on_release: root.logout()
                        
                Widget:
                    size_hint_y: None
                    height: dp(20)
''')