from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    pass

Builder.load_string("""
<HomeScreen>:
    name: "home"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Local Guide"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            right_action_items: [["information-outline", lambda x: app.show_info()]]
            md_bg_color: 0.2, 0.4, 0.8, 1

        MDLabel:
            text: "ANA SAYFA"
            font_style: "Subtitle1"
            halign: "center"
            size_hint_y: None
            height: "40dp"

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "10dp"
                spacing: "20dp"
                size_hint_y: None
                adaptive_height: True

                MDCard:
                    size_hint_y: None
                    height: "180dp"
                    radius: [20]
                    elevation: 8
                    orientation: "horizontal"
                    padding: "10dp"
                    spacing: "10dp"
                    on_release: app.go_to("istanbul")

                    Image:
                        source: "istanbul.jpg"
                        size_hint_x: 0.4
                        allow_stretch: True
                        keep_ratio: False

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "8dp"

                        MDLabel:
                            text: "İstanbul"
                            font_style: "H6"
                            halign: "left"
                            size_hint_y: None
                            height: "30dp"

                        MDLabel:
                            text: "Asya ve Avrupa'yı birleştiren,\\nzengin tarihi ve kültürüyle büyüleyici."
                            font_style: "Caption"
                            halign: "left"
                            theme_text_color: "Secondary"

                        MDIconButton:
                            icon: "bookmark-outline"
                            pos_hint: {"right": 1}
                            theme_text_color: "Secondary"

                MDCard:
                    size_hint_y: None
                    height: "180dp"
                    radius: [20]
                    elevation: 8
                    orientation: "horizontal"
                    padding: "10dp"
                    spacing: "10dp"
                    on_release: app.go_to("ankara")

                    Image:
                        source: "ankara.jpg"
                        size_hint_x: 0.4
                        allow_stretch: True
                        keep_ratio: False

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "8dp"

                        MDLabel:
                            text: "Ankara"
                            font_style: "H6"
                            halign: "left"
                            size_hint_y: None
                            height: "30dp"

                        MDLabel:
                            text: "Türkiye'nin başkenti, kültürel etkinlikler ve tarih dolu."
                            font_style: "Caption"
                            halign: "left"
                            theme_text_color: "Secondary"

                        MDIconButton:
                            icon: "bookmark-outline"
                            pos_hint: {"right": 1}
                            theme_text_color: "Secondary"

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(60)

            MDBottomNavigationItem:
                name: 'home'
                text: 'Anasayfa'
                icon: 'home'

            MDBottomNavigationItem:
                name: 'discover'
                text: 'Keşfet'
                icon: 'compass-outline'

            MDBottomNavigationItem:
                name: 'saved'
                text: 'Kaydedilenler'
                icon: 'bookmark-outline'

            MDBottomNavigationItem:
                name: 'favorites'
                text: 'Favoriler'
                icon: 'heart-outline'

            MDBottomNavigationItem:
                name: 'profile'
                text: 'Profil'
                icon: 'account'
                on_tab_press: app.go_to('profile')
""")
# --- main.py ---

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # Windows FBO hatası çözümü

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# Ekranları import et
from istanbul import IstanbulScreen
from ankara import AnkaraScreen
from profil import ProfileScreen
from yemekmekanlariistanbul import FoodPlacesScreen, FoodDetailScreen
from yemekmekanlariankara import FoodPlacesAnkaraScreen, FoodDetailAnkaraScreen

Window.size = (360, 640)

# Ana Sayfa Ekranı
class HomeScreen(Screen):
    pass

class LocalGuideApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def go_to(self, screen_name):
        self.root.ids.scr_mngr.current = screen_name

    def go_back(self):
        self.root.ids.scr_mngr.current = "home"

    def show_info(self):
        print("Bilgi tuşuna basıldı.")

    def show_food_detail(self, image, description, location, hours):
        self.root.ids.scr_mngr.current = "food_detail"
        screen = self.root.ids.scr_mngr.get_screen("food_detail")
        screen.ids.food_image.source = image
        screen.ids.food_description.text = description
        screen.ids.food_location.text = location
        screen.ids.food_hours.text = hours

    def show_food_detail_ankara(self, image, description, location, hours):
        self.root.ids.scr_mngr.current = "food_detail_ankara"
        screen = self.root.ids.scr_mngr.get_screen("food_detail_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours

# KV dosyası
KV = """
MDBoxLayout:
    orientation: "vertical"

    ScreenManager:
        id: scr_mngr

        HomeScreen:
        IstanbulScreen:
        FoodPlacesScreen:
        FoodDetailScreen:
        AnkaraScreen:
        FoodPlacesAnkaraScreen:
        FoodDetailAnkaraScreen:
        ProfileScreen:

    MDBottomNavigation:
        panel_color: 1, 1, 1, 1
        height: dp(60)
        text_color_active: "blue"

        MDBottomNavigationItem:
            name: 'home'
            text: 'Ana Sayfa'
            icon: 'home'
            on_tab_press: app.go_to('home')

        MDBottomNavigationItem:
            name: 'discover'
            text: 'Keşfet'
            icon: 'compass-outline'

        MDBottomNavigationItem:
            name: 'saved'
            text: 'Kaydedilenler'
            icon: 'bookmark-outline'

        MDBottomNavigationItem:
            name: 'favorites'
            text: 'Favoriler'
            icon: 'heart-outline'

        MDBottomNavigationItem:
            name: 'profile'
            text: 'Profil'
            icon: 'account'
            on_tab_press: app.go_to('profile')

<HomeScreen>:
    name: "home"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Local Guide"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            right_action_items: [["information-outline", lambda x: app.show_info()]]
            md_bg_color: 0.2, 0.4, 0.8, 1

        MDLabel:
            text: "ANA SAYFA"
            font_style: "Subtitle1"
            halign: "center"
            size_hint_y: None
            height: "40dp"

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(20)
                size_hint_y: None
                height: self.minimum_height


                # İstanbul Kartı
                MDCard:
                    size_hint_y: None
                    height: dp(180)
                    radius: [20]
                    elevation: 8
                    on_release: app.go_to("istanbul")

                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: dp(10)
                        spacing: dp(10)

                        Image:
                            source: "istanbul.jpg"
                            size_hint_x: 0.4
                            allow_stretch: True
                            keep_ratio: False

                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: dp(5)

                            MDLabel:
                                text: "İstanbul"
                                font_style: "H6"
                                halign: "left"

                            MDLabel:
                                text: "Tarihi ve kültürüyle büyüleyici."
                                font_style: "Caption"
                                halign: "left"

                # Ankara Kartı
                MDCard:
                    size_hint_y: None
                    height: dp(180)
                    radius: [20]
                    elevation: 8
                    on_release: app.go_to("ankara")

                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: dp(10)
                        spacing: dp(10)

                        Image:
                            source: "ankara.jpg"
                            size_hint_x: 0.4
                            allow_stretch: True
                            keep_ratio: False

                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: dp(5)

                            MDLabel:
                                text: "Ankara"
                                font_style: "H6"
                                halign: "left"

                            MDLabel:
                                text: "Başkent kültürü ve düzeni."
                                font_style: "Caption"
                                halign: "left"

                Widget:  # >>> ALTTA BOŞLUK İÇİN
                    size_hint_y: None
                    height: dp(50)
"""

if __name__ == "__main__":
    LocalGuideApp().run()
