from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

# Telefon ekran boyutuna ayarlama
Window.size = (360, 640)

class IstanbulScreen(Screen):
    pass

KV = """
ScreenManager:
    IstanbulScreen:

<IstanbulScreen>:
    name: 'istanbul'

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
                on_release: app.root.current = 'home'

            MDLabel:
                text: 'İSTANBUL'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                font_style: 'H6'

        # Butonlar
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.85, None
            height: dp(400)
            spacing: dp(10)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRaisedButton:
                text: 'Ünlü Yerler'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'famous_places'
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Yemek Mekanları'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'food_places'
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Müzeler'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'museums'
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Kaydedilenler'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'saved'
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Tarihi Mekanlar'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'historical_places'
                pos_hint: {'center_x': 0.5}

            MDRaisedButton:
                text: 'Etkinlikler'
                size_hint_y: None
                height: dp(50)
                on_release: app.root.current = 'events'
                pos_hint: {'center_x': 0.5}

        # Alt Navigasyon
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(60)
            md_bg_color: 1, 1, 1, 1
            pos_hint: {'bottom': 1}
            spacing: dp(20)  # Butonlar arasındaki mesafe
            padding: dp(20), 0  # Sol ve sağ kenarlara eşit mesafe

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
"""

class IstanbulApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    IstanbulApp().run()
