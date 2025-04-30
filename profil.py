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
        md_bg_color: 0.95, 0.95, 1, 1

        MDTopAppBar:
            title: "Profilim"
            elevation: 5
            md_bg_color: 0.1, 0.1, 0.5, 1
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
                    theme_text_color: "Primary"

                MDLabel:
                    text: "@haticeaydin"
                    halign: "center"
                    font_style: "Subtitle2"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Gezi sever, kitap kurdu."
                    halign: "center"
                    font_style: "Body2"
                    theme_text_color: "Primary"

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
                    font_style: "Body2"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "İlgi Alanları: Seyahat, Yemek, Sanat"
                    halign: "center"
                    font_style: "Body2"
                    theme_text_color: "Secondary"

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
            name: "home"
        IstanbulScreen:
            name: "istanbul"
        AnkaraScreen:
            name: "ankara"
        ProfileScreen:
            name: "profile"
        FoodPlacesScreen:
            name: "food_places"
        FoodDetailScreen:
            name: "food_detail"
        FoodPlacesAnkaraScreen:
            name: "food_places_ankara"
        FoodDetailAnkaraScreen:
            name: "food_detail_ankara"

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
                spacing: dp(20)
                size_hint_y: None
                height: self.minimum_height

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






