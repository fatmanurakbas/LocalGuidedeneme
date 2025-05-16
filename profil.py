from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

class ProfileScreen(Screen):
    pass


Builder.load_string('''
<ProfileScreen>:
    name: "profile"

    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.2, 0.4, 0.8, 1

        MDTopAppBar:
            title: "Profilim"
            elevation: 5
            md_bg_color: 0.2, 0.4, 0.8, 1
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

                MDCard:
                    size_hint: None, None
                    size: dp(120), dp(120)
                    pos_hint: {'center_x': 0.5}
                    radius: [60]
                    md_bg_color: 0.8, 0.8, 0.8, 1
                    elevation: 5

                MDLabel:
                    text: "Hatice Aydın"
                    halign: "center"
                    font_style: "H6"

                MDLabel:
                    text: "@haticeaydin"
                    halign: "center"
                    font_style: "Subtitle2"

                MDLabel:
                    text: "Gezi sever, kitap kurdu."
                    halign: "center"
                    font_style: "Body2"

                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                    MDLabel:
                        text: "Takipçi: 500"
                        halign: "center"

                    MDLabel:
                        text: "Takip: 300"
                        halign: "center"

                    MDLabel:
                        text: "Gönderi: 80"
                        halign: "center"

                MDRaisedButton:
                    text: "Profili Düzenle"
                    size_hint: (0.7, None)
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                MDLabel:
                    text: "İstanbul, Türkiye 🌍"
                    halign: "center"

                MDLabel:
                    text: "İlgi Alanları: Seyahat, Yemek, Sanat"
                    halign: "center"

                MDRaisedButton:
                    text: "Parola Değiştir"
                    size_hint: (0.8, None)
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                MDRaisedButton:
                    text: "Bildirim Ayarları"
                    size_hint: (0.8, None)
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                MDRaisedButton:
                    text: "Tema Ayarları"
                    size_hint: (0.8, None)
                    height: dp(40)
                    pos_hint: {'center_x': 0.5}

                MDRaisedButton:
                    text: "Hesabı Dondur veya Sil"
                    size_hint: (0.8, None)
                    height: dp(40)
                    md_bg_color: 1, 0.5, 0.5, 1
                    text_color: 1, 1, 1, 1
                    pos_hint: {'center_x': 0.5}

                MDRaisedButton:
                    text: "Çıkış Yap"
                    size_hint: (0.8, None)
                    height: dp(40)
                    md_bg_color: 1, 0.2, 0.2, 1
                    text_color: 1, 1, 1, 1
                    pos_hint: {'center_x': 0.5}
''')
