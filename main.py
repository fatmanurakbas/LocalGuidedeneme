from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import subprocess  # .py dosyalarını açmak için

# Telefon ekran boyutuna ayarlama
Window.size = (360, 640)

class HomeScreen(Screen):
    pass

class LocalGuideApp(MDApp):

    # İstanbul sayfasını subprocess ile açmak
    def open_istanbul(self):
        subprocess.run(["python", r"C:\Python\LOCALGUIDE\istanbul.py"])# İstanbul sayfasını açmak için

    # Ankara sayfasını subprocess ile açmak
    def open_ankara(self):
        subprocess.run(["python", r"C:\Python\LOCALGUIDE\ankara.py"])  # Ankara sayfasını açmak için

    # Notlar sayfasını subprocess ile açmak
    def open_notes(self):
        subprocess.run(["python", "LOCAL GUIDE/PYTHON/notes.py"])

    # Sohbet sayfasını subprocess ile açmak
    def open_chat(self):
        subprocess.run(["python", "LOCAL GUIDE/PYTHON/chat.py"])

    # Kaydedilenler sayfasını subprocess ile açmak
    def open_saved(self):
        subprocess.run(["python", "LOCAL GUIDE/PYTHON/saved.py"])

    # Profil sayfasını subprocess ile açmak
    def open_profile(self):
        subprocess.run(["python", "LOCAL GUIDE/PYTHON/profile.py"])

    def build(self):
        return Builder.load_string(KV)

KV = """
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    MDFloatLayout:
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            md_bg_color: 0, 0, 0.5, 1
            pos_hint: {'top': 1}

            MDIconButton:
                icon: 'arrow-left'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                pos_hint: {'center_y': 0.5}

            MDLabel:
                text: 'LOCAL GUIDE'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_style: 'H6'

            MDIconButton:
                icon: 'information'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                pos_hint: {'center_y': 0.5}

        Image:
            source: 'logo.png'
            size_hint: None, None
            size: dp(120), dp(120)
            pos_hint: {'center_x': 0.5, 'top': 0.84}

        MDTextField:
            hint_text: 'Search'
            size_hint_x: 0.75
            pos_hint: {'center_x': 0.5, 'top': 0.7}
            mode: 'rectangle'
            icon_right: 'magnify'

        # İstanbul için bir buton (MDCard)
        MDCard:
            size_hint: (None, None)
            size: dp(300), dp(150)
            pos_hint: {'center_x': 0.5, 'top': 0.58}
            elevation: 8
            radius: [20,]
            on_release: app.open_istanbul()

            BoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                Image:
                    source: 'istanbul.jpg'
                    size_hint: 1, 1
                    allow_stretch: True
                    keep_ratio: True
                MDLabel:
                    text: 'İstanbul'
                    halign: 'center'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    font_style: 'H5'
                    bold: True
                    size_hint: 1, None
                    height: dp(30)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        # Ankara için bir buton (MDCard)
        MDCard:
            size_hint: (None, None)
            size: dp(300), dp(150)
            pos_hint: {'center_x': 0.5, 'top': 0.34}
            elevation: 8
            radius: [20,]
            on_release: app.open_ankara()

            BoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                Image:
                    source: 'ankara.jpg'
                    size_hint: 1, 1
                    allow_stretch: True
                    keep_ratio: True
                MDLabel:
                    text: 'Ankara'
                    halign: 'center'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1
                    font_style: 'H5'
                    bold: True
                    size_hint: 1, None
                    height: dp(30)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        # Alt navigasyon butonları
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(60)
            pos_hint: {'bottom': 0}
            md_bg_color: 1, 1, 1, 1
            spacing: dp(20)
            padding: dp(20), 0

            MDIconButton:
                icon: 'home'
                theme_text_color: 'Custom'
                on_release: app.root.current = 'home'

            MDIconButton:
                icon: 'note'
                theme_text_color: 'Custom'
                on_release: app.open_notes()

            MDIconButton:
                icon: 'robot'
                theme_text_color: 'Custom'
                on_release: app.open_chat()

            MDIconButton:
                icon: 'bookmark'
                theme_text_color: 'Custom'
                on_release: app.open_saved()

            MDIconButton:
                icon: 'account'
                theme_text_color: 'Custom'
                on_release: app.open_profile()
"""

if __name__ == '__main__':
    LocalGuideApp().run()
