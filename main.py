import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ['KIVY_NO_ARGS'] = '1'
os.environ["KIVY_GL_DISABLE_FBO"] = "1"

from kivy.config import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'borderless', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
import requests  # Hava durumu API'si için
from kivy.clock import Clock  # Ekran yüklendiğinde veri çekmek için

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Diğer ekranları import et
from istanbul import IstanbulScreen
from ankara import AnkaraScreen
from profil import ProfileScreen
from yemekmekanlariistanbul import FoodPlacesScreen, FoodDetailScreen
from yemekmekanlariankara import FoodPlacesAnkaraScreen, FoodDetailAnkaraScreen
from TarihiYerlerIstanbul import TarihiYerlerIstanbulScreen, TarihiYerDetailScreen  # Yeni ekledik | İstanbul tarihi yer için detay sayfası ekledim
from TarihiYerlerAnkara import TarihiYerlerAnkaraScreen, TarihiYerDetailAnkaraScreen  # Yeni ekledik | Ankara Tarihi yer için detay sayfası ekledim
from kaydedilenler import KaydedilenlerScreen  # Kaydedilenler ekranını import ettik
from unluyerleristanbul import UnluYerlerIstanbulScreen #stanbul için ünlü yerler erkanı
from EtkinlikIstanbul import SocialEventsIstanbulScreen, EventDetailScreen #Etkinlik İstanbul için
from EtkinlikAnkara import SocialEventsAnkaraScreen, EventDetailAnkara # Etkinlik Ankara için
from unluyerlerankara import UnluYerlerAnkaraScreen, UnluYerlerAnkaraDetailScreen
from planlayici import PlanlayiciScreen
from cafeler_istanbul import CafelerIstanbulScreen, CafelerDetailIstanbul
from cafeler_ankara import CafelerAnkaraScreen, CafelerDetailAnkara
from favoriler import FavorilerScreen



Window.size = (360, 640)

class HomeScreen(Screen):
    pass

KV = '''
FloatLayout:

    ScreenManager:
        id: scr_mngr
        size_hint: 1, 1

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
        KaydedilenlerScreen:  # Kaydedilenler ekranını ekledik
        UnluYerlerIstanbulDetailScreen: # ünlü yerler istanbul detay ekranı
        UnluYerlerIstanbulScreen: # ünlü yerler ekranı ekledim
        TarihiYerDetailScreen: # İstanbul için detay ekranı
        TarihiYerDetailAnkaraScreen: # Ankara için detay ekranı
        SocialEventsIstanbulScreen:
        EventDetailScreen:
        SocialEventsAnkaraScreen:
        EventDetailAnkara:
        UnluYerlerAnkaraScreen:
        UnluYerlerAnkaraDetailScreen:
        PlanlayiciScreen:
        CafelerIstanbulScreen:
        CafelerAnkaraScreen:
        FavorilerScreen:

    MDBottomNavigation:
        size_hint: 1, None
        height: dp(60)
        pos_hint: {"x": 0, "y": 0}  # Alt köşeye sabitle
        text_color_active: "blue"

        MDBottomNavigationItem:
            name: 'home'
            text: 'Ana Sayfa'
            icon: 'home'
            on_tab_press: app.go_to('home')

        MDBottomNavigationItem:
            name: 'planner'
            text: 'Planlayıcı'
            icon: 'calendar-text'
            on_tab_press: app.go_to('planlayici')

        MDBottomNavigationItem:
            name: 'saved'
            text: 'Kaydedilenler'
            icon: 'bookmark-outline'
            on_tab_press: app.go_to('kaydedilenler')

        MDBottomNavigationItem:
            name: 'favorites'
            text: 'Favoriler'
            icon: 'heart-outline'
            on_tab_press: app.go_to('favoriler')

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
            md_bg_color: "#5C6BC0"  # Soft mavi
            size_hint_y: None
            height: dp(56)
            title_align: "center"

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(12)
                spacing: dp(14)
                size_hint_y: None
                height: self.minimum_height

                MDTextField:
                    hint_text: "Şehir, etkinlik veya mekan ara..."
                    icon_left: "magnify"
                    mode: "fill"
                    fill_color: "#F2F2F2"
                    size_hint_x: 0.95
                    size_hint_y: None
                    height: dp(48)
                    pos_hint: {"center_x": 0.5}
                    radius: [16, 16, 16, 16]

                Widget:
                    size_hint_y: None
                    height: dp(6)

                MDCard:
                    size_hint_y: None
                    height: dp(180)
                    radius: [24]
                    elevation: 10
                    shadow_softness: 3
                    ripple_behavior: True
                    on_release: app.go_to("istanbul")

                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: dp(10)
                        spacing: dp(12)

                        FitImage:
                            source: "images/istanbul.jpg"
                            size_hint_x: 0.4
                            radius: [16]
                            allow_stretch: True

                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: dp(6)

                            MDLabel:
                                text: "İstanbul"
                                font_style: "H5"
                                theme_text_color: "Primary"
                                bold: True

                            MDLabel:
                                text: "Kültür, tarih ve enerjik yaşam: Asya ile Avrupa'nın keskin karışımı."
                                font_style: "Body2"
                                theme_text_color: "Secondary"
                                shorten: True
                                max_lines: 3

                MDCard:
                    size_hint_y: None
                    height: dp(180)
                    radius: [24]
                    elevation: 10
                    shadow_softness: 3
                    ripple_behavior: True
                    on_release: app.go_to("ankara")

                    MDBoxLayout:
                        orientation: "horizontal"
                        padding: dp(10)
                        spacing: dp(12)

                        FitImage:
                            source: "images/ankara.jpg"
                            size_hint_x: 0.4
                            radius: [16]
                            allow_stretch: True

                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: dp(6)

                            MDLabel:
                                text: "Ankara"
                                font_style: "H5"
                                theme_text_color: "Primary"
                                bold: True

                            MDLabel:
                                text: "Başkentin huzurlu dokusu ve resmi atmosferiyle sürükleyici deneyim."
                                font_style: "Body2"
                                theme_text_color: "Secondary"
                                shorten: True
                                max_lines: 3
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

    def konuma_git(self, adres):
        url = f"https://www.google.com/maps/dir/?api=1&destination={adres.replace(' ', '+')}"
        try:
        # google mapsi varsayılan tarayıcıda açar. 
            webbrowser.open(url)
        except Exception as e:
            print("Harita açılamadı:", e)

    def show_food_detail(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "food_detail"
        screen = self.root.ids.scr_mngr.get_screen("food_detail")
        screen.ids.food_image.source = image
        screen.ids.food_istanbul_title.text = title
        screen.ids.food_description.text = description
        screen.ids.food_location.text = location
        screen.ids.food_hours.text = hours

    def show_food_detail_ankara(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "food_detail_ankara"
        screen = self.root.ids.scr_mngr.get_screen("food_detail_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_ankara_title.text = title
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours

    def show_place_detail(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "tarihi_yer_detail"
        screen = self.root.ids.scr_mngr.get_screen("tarihi_yer_detail")
        screen.ids.tarihi_yer_image.source = image
        screen.ids.tarihi_yer_istanbul_title.text = title
        screen.ids.tarihi_yer_description.text = description
        screen.ids.tarihi_yer_location.text = location
        screen.ids.tarihi_yer_hours.text = hours

    def show_place_detail_ankara(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "tarihi_yer_detail_ankara"
        screen = self.root.ids.scr_mngr.get_screen("tarihi_yer_detail_ankara")
        screen.ids.tarihi_yer_image_ankara.source = image
        screen.ids.tarihi_yer_ankara_title.text = title
        screen.ids.tarihi_yer_description_ankara.text = description
        screen.ids.tarihi_yer_location_ankara.text = location
        screen.ids.tarihi_yer_hours_ankara.text = hours
    
    def show_event_detail_istanbul(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "event_detail"
        screen = self.root.ids.scr_mngr.get_screen("event_detail")
        screen.ids.event_image.source = image
        screen.ids.event_istanbul_title.text = title
        screen.ids.event_description.text = description
        screen.ids.event_location.text = location
        screen.ids.event_hours.text = hours

    def show_event_detail_ankara(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "event_detail_ankara"
        screen = self.root.ids.scr_mngr.get_screen("event_detail_ankara")
        screen.ids.event_image_ankara.source = image
        screen.ids.event_ankara_title.text = title
        screen.ids.event_description_ankara.text = description
        screen.ids.event_location_ankara.text = location
        screen.ids.event_hours_ankara.text = hours

    def show_unlu_yerler_istanbul(self, image, title, description, location, hours, *args):
        self.root.ids.scr_mngr.current = "unlu_yer_istanbul_detail"
        screen = self.root.ids.scr_mngr.get_screen("unlu_yer_istanbul_detail")
        screen.ids.unlu_image_istanbul.source = image
        screen.ids.unlu_istanbul_title.text = title
        screen.ids.unlu_description_istanbul.text = description
        screen.ids.unlu_location_istanbul.text = location
        screen.ids.unlu_hours_istanbul.text = hours
    
    def show_unlu_yerler_ankara(self, image, title, description, location, hours, *args):
       self.root.ids.scr_mngr.current = "unlu_yer_ankara_detail"
       screen = self.root.ids.scr_mngr.get_screen("unlu_yer_ankara_detail")
       screen.ids.unlu_image_ankara.source = image
       screen.ids.unlu_ankara_title.text = title
       screen.ids.unlu_description_ankara.text = description
       screen.ids.unlu_location_ankara.text = location
       screen.ids.unlu_hours_ankara.text = hours
    
    def show_cafe_detail_istanbul(self, image, title, description, location, hours, *args):
      self.root.ids.scr_mngr.current = "cafe_detail_istanbul"
      screen = self.root.ids.scr_mngr.get_screen("cafe_detail_istanbul")
      screen.ids.cafe_image_istanbul.source = image
      screen.ids.cafe_istanbul_title.text = title
      screen.ids.cafe_description_istanbul.text = description
      screen.ids.cafe_location_istanbul.text = location
      screen.ids.cafe_hours_istanbul.text = hours

    def show_cafe_detail_ankara(self, image, title, description, location, hours, *args):
      self.root.ids.scr_mngr.current = "cafe_detail_ankara"
      screen = self.root.ids.scr_mngr.get_screen("cafe_detail_ankara")
      screen.ids.cafe_image_ankara.source = image
      screen.ids.cafe_ankara_title.text = title
      screen.ids.cafe_description_ankara.text = description
      screen.ids.cafe_location_ankara.text = location
      screen.ids.cafe_hours_ankara.text = hours
 





if __name__ == "__main__":
    LocalGuideApp().run()
