
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
from kaydedilenler import KaydedilenlerScreen  # Kaydedilenler ekranını import ettik
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
BoxLayout:
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
        KaydedilenlerScreen:  # Kaydedilenler ekranını ekledik


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
            on_tab_press: app.go_to('kaydedilenler')

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
                    
"""

if __name__ == "__main__":
    LocalGuideApp().run()

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.config import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'borderless', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Diğer ekranları import et
from istanbul import IstanbulScreen
from ankara import AnkaraScreen
from profil import ProfileScreen
from yemekmekanlariistanbul import FoodPlacesScreen, FoodDetailScreen
from yemekmekanlariankara import FoodPlacesAnkaraScreen, FoodDetailAnkaraScreen
from TarihiYerlerIstanbul import TarihiYerlerIstanbulScreen
from TarihiYerlerAnkara import TarihiYerlerAnkaraScreen
from kaydedilenler import KaydedilenlerScreen

Window.size = (360, 640)

class HomeScreen(Screen):
    pass

KV = '''
BoxLayout:
    orientation: "vertical"

    ScreenManager:
        id: scr_mngr

        HomeScreen:
        IstanbulScreen:
        AnkaraScreen:
        FoodPlacesScreen:
        FoodDetailScreen:
        FoodPlacesAnkaraScreen:
        FoodDetailAnkaraScreen:
        TarihiYerlerIstanbulScreen:
        TarihiYerlerAnkaraScreen:
        ProfileScreen:
        KaydedilenlerScreen:

    MDBottomNavigation:
        text_color_active: "blue"

        MDBottomNavigationItem:
            name: 'home'
            text: 'Ana Sayfa'
            icon: 'home'
            on_tab_press: app.go_to('home')

            MDLabel:
                text: "Ana Sayfa"
                halign: "center"

        MDBottomNavigationItem:
            name: 'discover'
            text: 'Planlayıcı'
            icon: 'compass-outline'

            MDLabel:
                text: "Planlayıcı"
                halign: "center"

        MDBottomNavigationItem:
            name: 'saved'
            text: 'Kaydedilenler'
            icon: 'bookmark-outline'
            on_tab_press: app.go_to('kaydedilenler')

            MDLabel:
                text: "Kaydedilenler Ekranı"
                halign: "center"

        MDBottomNavigationItem:
            name: 'favorites'
            text: 'Favoriler'
            icon: 'heart-outline'

            MDLabel:
                text: "Favoriler Ekranı"
                halign: "center"

        MDBottomNavigationItem:
            name: 'profile'
            text: 'Profil'
            icon: 'account'
            on_tab_press: app.go_to('profile')

            MDLabel:
                text: "Profil Ekranı"
                halign: "center"
'''

class LocalGuideApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def go_to(self, screen_name):
        if self.root.ids.scr_mngr.has_screen(screen_name):
            self.root.ids.scr_mngr.current = screen_name

    def go_back(self):
        self.root.ids.scr_mngr.current = "home"

    def show_info(self):
        print("Bilgi tuşuna basıldı.")

    def show_food_detail(self, image, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "food_detail"
        screen = self.root.ids.scr_mngr.get_screen("food_detail")
        screen.ids.food_image.source = image
        screen.ids.food_description.text = description
        screen.ids.food_location.text = location
        screen.ids.food_hours.text = hours

    def show_food_detail_ankara(self, image, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "food_detail_ankara"
        screen = self.root.ids.scr_mngr.get_screen("food_detail_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours

    def show_tarihi_yerler_istanbul(self, image, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "tarihi_yerler_istanbul"
        screen = self.root.ids.scr_mngr.get_screen("tarihi_yerler_istanbul")
        screen.ids.food_image_istanbul.source = image
        screen.ids.food_description_istanbul.text = description
        screen.ids.food_location_istanbul.text = location
        screen.ids.food_hours_istanbul.text = hours

    def show_tarihi_yerler_ankara(self, image, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "tarihi_yerler_ankara"
        screen = self.root.ids.scr_mngr.get_screen("tarihi_yerler_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours

if __name__ == "__main__":
    LocalGuideApp().run()
