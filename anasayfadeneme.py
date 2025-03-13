from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton

# Telefon ekran boyutuna ayarlama
Window.size = (360, 640)

class HomeScreen(Screen):
    pass

class IstanbulScreen(Screen):
    pass

class AnkaraScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class NotesScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class SavedScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

KV = """
ScreenManager:
    HomeScreen:
    IstanbulScreen:
    AnkaraScreen:
    AboutScreen:
    NotesScreen:
    ChatScreen:
    SavedScreen:
    ProfileScreen:

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
                on_release: app.root.current = 'about'

        Image:
            source: 'logo.png'
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {'center_x': 0.5, 'top': 0.8}

        MDTextField:
            hint_text: 'Search'
            size_hint_x: 0.75
            pos_hint: {'center_x': 0.5, 'top': 0.7}
            mode: 'rectangle'
            icon_right: 'magnify'

        MDCard:
            size_hint: 0.85, None
            height: dp(150)
            pos_hint: {'center_x': 0.5, 'top': 0.58}
            elevation: 8
            radius: [20,]
            on_release: app.root.current = 'istanbul'

            Image:
                source: 'istanbul.jpg'
                size_hint: 1, 1
                allow_stretch: True
                keep_ratio: False

        MDLabel:
            text: 'İstanbul'
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'top': 0.55}
            font_style: 'H5'
            bold: True

        MDCard:
            size_hint: 0.85, None
            height: dp(150)
            pos_hint: {'center_x': 0.5, 'top': 0.4}
            elevation: 8
            radius: [20,]
            on_release: app.root.current = 'ankara'

            Image:
                source: 'ankara.jpg'
                size_hint: 1, 1
                allow_stretch: True
                keep_ratio: False

        MDLabel:
            text: 'Ankara'
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'top': 0.37}
            font_style: 'H5'
            bold: True

        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            md_bg_color: 1, 1, 1, 1
            pos_hint: {'bottom': 1}

            MDIconButton:
                icon: 'home'
                on_release: app.root.current = 'home'

            MDIconButton:
                icon: 'note-edit'
                on_release: app.root.current = 'notes'

            MDIconButton:
                icon: 'robot'
                on_release: app.root.current = 'chat'

            MDIconButton:
                icon: 'bookmark'
                on_release: app.root.current = 'saved'

            MDIconButton:
                icon: 'account'
                on_release: app.root.current = 'profile'

<IstanbulScreen>:
    name: 'istanbul'
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'İstanbul Sayfası'
            halign: 'center'
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'home'

<AnkaraScreen>:
    name: 'ankara'
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Ankara Sayfası'
            halign: 'center'
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x': 0.5}
            on_release: app.root.current = 'home'

<AboutScreen>:
    name: 'about'
    MDLabel:
        text: 'Bu uygulama yerel rehberlik sağlar.'
        halign: 'center'

<NotesScreen>:
    name: 'notes'
    MDLabel:
        text: 'Notlar Sayfası'
        halign: 'center'

<ChatScreen>:
    name: 'chat'
    MDLabel:
        text: 'Sohbet Sayfası'
        halign: 'center'

<SavedScreen>:
    name: 'saved'
    MDLabel:
        text: 'Kaydedilenler Sayfası'
        halign: 'center'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profil Sayfası'
        halign: 'center'
"""

class LocalGuideApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    LocalGuideApp().run()