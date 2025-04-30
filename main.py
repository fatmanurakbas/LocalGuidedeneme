import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Ekranları import et
from istanbul import IstanbulScreen
from ankara import AnkaraScreen
from profil import ProfileScreen
from yemekmekanlariistanbul import FoodPlacesScreen, FoodDetailScreen
from yemekmekanlariankara import FoodPlacesAnkaraScreen, FoodDetailAnkaraScreen

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
        ProfileScreen:
        FoodPlacesScreen:
        FoodDetailScreen:
        FoodPlacesAnkaraScreen:
        FoodDetailAnkaraScreen:

    MDBottomNavigation:
        size_hint_y: None
        height: dp(60)
        text_color_active: "blue"


        MDBottomNavigationItem:
            name: 'home'
            text: 'Ana Sayfa'
            icon: 'home'
            on_tab_press: app.go_to('home')

        MDBottomNavigationItem:
            name: 'discover'
            text: 'Planlayıcı'
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

    BoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Local Guide"
            elevation: 5
            md_bg_color: 0.2, 0.4, 0.8, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(8)  # spacing azaltıldı
                size_hint_y: None
                height: self.minimum_height

                MDTextField:
                    hint_text: "Ara..."
                    icon_left: "magnify"
                    size_hint_x: 1
                    size_hint_y: None
                    height: dp(40)
                    mode: "rectangle"
                    pos_hint: {"center_x": 0.5}

                # Arama kutusuyla İstanbul kartı arasında özel boşluk
                Widget:
                    size_hint_y: None
                    height: dp(4)
                

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
                            source: "images/istanbul.jpg"
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
                                text: "Asya ve Avrupa'yı birleştiren, zengin tarihi, kültürel çeşitliliği ve hareketli yaşamıyla büyüleyici bir şehir."
                                font_style: "Caption"
                                halign: "left"

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
                            source: "images/ankara.jpg"
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
                                text: "Türkiye’nin başkenti olarak sakin, düzenli yapısı, resmi kurumları ve kültürel etkinlikleriyle kendine özgü bir atmosfere sahip."
                                font_style: "Caption"
                                halign: "left"

'''

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

if __name__ == "__main__":
    LocalGuideApp().run()
