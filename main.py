from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
import requests  # Hava durumu API'si için
from kivy.clock import Clock  # Ekran yüklendiğinde veri çekmek için
# ... önceki importlar ...
from home import HomeScreen  # ← BUNU BURAYA EKLE

from istanbul import IstanbulScreen
from ankara import AnkaraScreen
from profil import ProfileScreen
from yemekmekanlariistanbul import FoodPlacesScreen, FoodDetailScreen
from yemekmekanlariankara import FoodPlacesAnkaraScreen, FoodDetailAnkaraScreen
from TarihiYerlerIstanbul import TarihiYerlerIstanbulScreen, TarihiYerDetailScreen
from TarihiYerlerAnkara import TarihiYerlerAnkaraScreen, TarihiYerDetailAnkaraScreen
from unluyerleristanbul import UnluYerlerIstanbulScreen, UnluYerlerIstanbulDetailScreen
from unluyerlerankara import UnluYerlerAnkaraScreen, UnluYerlerAnkaraDetailScreen
from cafeler_istanbul import CafelerIstanbulScreen, CafelerDetailIstanbul
from cafeler_ankara import CafelerAnkaraScreen, CafelerDetailAnkara
from planlayici import PlanlayiciScreen
from kaydedilenler import KaydedilenlerScreen
from favoriler import FavorilerScreen
from login import LoginScreen
from signup import SignUpScreen
from welcome_screen import WelcomeScreen
from forgot_password import ForgotPasswordScreen
from kivy.core.window import Window

Window.size = (360, 640)  # Telefona uygun boyut  

class HomeScreen(Screen):
    pass

class LocalGuideApp(MDApp):
    def build(self):
        Builder.load_file("main_panel.kv")
        sm = ScreenManager()
        

        # Ana ekranlar
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(IstanbulScreen(name="istanbul"))
        sm.add_widget(AnkaraScreen(name="ankara"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(PlanlayiciScreen(name="planlayici"))
        sm.add_widget(KaydedilenlerScreen(name="kaydedilenler"))
        sm.add_widget(FavorilerScreen(name="favoriler"))

        # İstanbul içerik ekranları
        sm.add_widget(FoodPlacesScreen(name="food_places"))
        sm.add_widget(FoodDetailScreen(name="food_detail"))
        sm.add_widget(TarihiYerlerIstanbulScreen(name="tarihi_yerler_istanbul"))
        sm.add_widget(TarihiYerDetailScreen(name="tarihi_yer_detail"))
        sm.add_widget(UnluYerlerIstanbulScreen(name="unlu_yerler_istanbul"))
        sm.add_widget(UnluYerlerIstanbulDetailScreen(name="unlu_yer_istanbul_detail"))
        sm.add_widget(CafelerIstanbulScreen(name="cafeler_istanbul"))
        sm.add_widget(CafelerDetailIstanbul(name="cafe_detail_istanbul"))

        # Ankara içerik ekranları
        sm.add_widget(FoodPlacesAnkaraScreen(name="food_places_ankara"))
        sm.add_widget(FoodDetailAnkaraScreen(name="food_detail_ankara"))
        sm.add_widget(TarihiYerlerAnkaraScreen(name="tarihi_yerler_ankara"))
        sm.add_widget(TarihiYerDetailAnkaraScreen(name="tarihi_yer_detail_ankara"))
        sm.add_widget(UnluYerlerAnkaraScreen(name="unlu_yerler_ankara"))
        sm.add_widget(UnluYerlerAnkaraDetailScreen(name="unlu_yer_ankara_detail"))
        sm.add_widget(CafelerAnkaraScreen(name="cafeler_ankara"))
        sm.add_widget(CafelerDetailAnkara(name="cafe_detail_ankara"))

        # Auth ekranları
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(ForgotPasswordScreen(name="forgot_password"))

        return sm

    def go_to(self, screen_name):
        self.root.current = screen_name


    def go_back(self, *args):
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
        self.go_to("food_detail")
        screen = self.root.get_screen("food_detail")
        screen.ids.food_image.source = image
        screen.ids.food_istanbul_title.text = title
        screen.ids.food_description.text = description
        screen.ids.food_location.text = location
        screen.ids.food_hours.text = hours

    def show_food_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("food_detail_ankara")
        screen = self.root.get_screen("food_detail_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_ankara_title.text = title
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours

    def show_place_detail(self, image, title, description, location, hours, *args):
        self.go_to("tarihi_yer_detail")
        screen = self.root.get_screen("tarihi_yer_detail")
        screen.ids.tarihi_yer_image.source = image
        screen.ids.tarihi_yer_istanbul_title.text = title
        screen.ids.tarihi_yer_description.text = description
        screen.ids.tarihi_yer_location.text = location
        screen.ids.tarihi_yer_hours.text = hours

    def show_place_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("tarihi_yer_detail_ankara")
        screen = self.root.get_screen("tarihi_yer_detail_ankara")
        screen.ids.tarihi_yer_image_ankara.source = image
        screen.ids.tarihi_yer_ankara_title.text = title
        screen.ids.tarihi_yer_description_ankara.text = description
        screen.ids.tarihi_yer_location_ankara.text = location
        screen.ids.tarihi_yer_hours_ankara.text = hours

    def show_unlu_yerler_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("unlu_yer_istanbul_detail")
        screen = self.root.get_screen("unlu_yer_istanbul_detail")
        screen.ids.unlu_image_istanbul.source = image
        screen.ids.unlu_istanbul_title.text = title
        screen.ids.unlu_description_istanbul.text = description
        screen.ids.unlu_location_istanbul.text = location
        screen.ids.unlu_hours_istanbul.text = hours

    def show_unlu_yerler_ankara(self, image, title, description, location, hours, *args):
        self.go_to("unlu_yer_ankara_detail")
        screen = self.root.get_screen("unlu_yer_ankara_detail")
        screen.ids.unlu_image_ankara.source = image
        screen.ids.unlu_ankara_title.text = title
        screen.ids.unlu_description_ankara.text = description
        screen.ids.unlu_location_ankara.text = location
        screen.ids.unlu_hours_ankara.text = hours

    def show_cafe_detail_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("cafe_detail_istanbul")
        screen = self.root.get_screen("cafe_detail_istanbul")
        screen.ids.cafe_image_istanbul.source = image
        screen.ids.cafe_istanbul_title.text = title
        screen.ids.cafe_description_istanbul.text = description
        screen.ids.cafe_location_istanbul.text = location
        screen.ids.cafe_hours_istanbul.text = hours

    def show_cafe_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("cafe_detail_ankara")
        screen = self.root.get_screen("cafe_detail_ankara")
        screen.ids.cafe_image_ankara.source = image
        screen.ids.cafe_ankara_title.text = title
        screen.ids.cafe_description_ankara.text = description
        screen.ids.cafe_location_ankara.text = location
        screen.ids.cafe_hours_ankara.text = hours

if __name__ == '__main__':
    LocalGuideApp().run()