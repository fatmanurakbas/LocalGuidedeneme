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
from EtkinlikIstanbul import SocialEventsIstanbulScreen, EventDetailScreen #Etkinlik İstanbul için
from EtkinlikAnkara import SocialEventsAnkaraScreen, EventDetailAnkara # Etkinlik Ankara için
from planlayici import PlanlayiciScreen
from kaydedilenler import KaydedilenlerScreen, KaydedilenlerDetail
from favoriler import FavorilerScreen, FavorilerDetail
from login import LoginScreen
from signup import SignUpScreen
from welcome_screen import WelcomeScreen
from forgot_password import ForgotPasswordScreen
from kivy.core.window import Window
from muze_istanbul import MuseumIstanbulScreen, MuseumIstanbulDetailScreen
from muze_ankara import MuseumAnkaraScreen, MuseumAnkaraDetailScreen
from edit_profile import EditProfileScreen
from notification_settings import NotificationSettingsScreen
from theme_settings import ThemeSettingsScreen
from account_security import AccountSecurityScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage.fitimage import FitImage
from kivy.metrics import dp
from kivy.app import App


Window.size = (360, 640)  # Telefona uygun boyut 
# 💡 TAM BU NOKTADA yaz:
Builder.load_string(EditProfileScreen.kv_string) 

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
        sm.add_widget(KaydedilenlerDetail(name="kaydedilenler_detail"))
        sm.add_widget(FavorilerScreen(name="favoriler"))
        sm.add_widget(FavorilerDetail(name="favoriler_detail"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(ForgotPasswordScreen(name="forgot_password"))
        sm.add_widget(EditProfileScreen(name="edit_profile"))
        sm.add_widget(NotificationSettingsScreen(name="notification_settings"))
        sm.add_widget(ThemeSettingsScreen(name="theme_settings"))
        sm.add_widget(AccountSecurityScreen(name="account_security"))

        # İstanbul içerik ekranları
        sm.add_widget(FoodPlacesScreen(name="food_places"))
        sm.add_widget(FoodDetailScreen(name="food_detail"))
        sm.add_widget(TarihiYerlerIstanbulScreen(name="tarihi_yerler_istanbul"))
        sm.add_widget(TarihiYerDetailScreen(name="tarihi_yer_detail"))
        sm.add_widget(UnluYerlerIstanbulScreen(name="unlu_yerler_istanbul"))
        sm.add_widget(UnluYerlerIstanbulDetailScreen(name="unlu_yer_istanbul_detail"))
        sm.add_widget(CafelerIstanbulScreen(name="cafeler_istanbul"))
        sm.add_widget(CafelerDetailIstanbul(name="cafe_detail_istanbul"))
        sm.add_widget(SocialEventsIstanbulScreen(name="social_events_ist"))
        sm.add_widget( EventDetailScreen(name="event_detail"))
        sm.add_widget(MuseumIstanbulDetailScreen(name="müze_istanbul_detail"))
        sm.add_widget(MuseumIstanbulScreen(name="müze_istanbul"))


        # Ankara içerik ekranları
        sm.add_widget(FoodPlacesAnkaraScreen(name="food_places_ankara"))
        sm.add_widget(FoodDetailAnkaraScreen(name="food_detail_ankara"))
        sm.add_widget(TarihiYerlerAnkaraScreen(name="tarihi_yerler_ankara"))
        sm.add_widget(TarihiYerDetailAnkaraScreen(name="tarihi_yer_detail_ankara"))
        sm.add_widget(UnluYerlerAnkaraScreen(name="unlu_yerler_ankara"))
        sm.add_widget(UnluYerlerAnkaraDetailScreen(name="unlu_yer_ankara_detail"))
        sm.add_widget(CafelerAnkaraScreen(name="cafeler_ankara"))
        sm.add_widget(CafelerDetailAnkara(name="cafe_detail_ankara"))
        sm.add_widget(SocialEventsAnkaraScreen(name="social_events_ankara"))
        sm.add_widget(EventDetailAnkara(name="event_detail_ankara"))
        sm.add_widget(MuseumAnkaraDetailScreen(name="müze_ankara_detail"))
        sm.add_widget(MuseumAnkaraScreen(name="müze_ankara"))

        # Auth ekranları
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(ForgotPasswordScreen(name="forgot_password"))

        return sm
    

    def go_to(self, screen_name):
        print(f"Ekran geçişi deneniyor: {screen_name}")
        try:
           self.root.current = screen_name
        except Exception as e:
           print(f"Ekran geçiş hatası: {e}")




    def go_back(self):
        self.root.current = "home"


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
        # Butonları sıfırla (her detayda bağımsız çalışsın)
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_food_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("food_detail_ankara")
        screen = self.root.get_screen("food_detail_ankara")
        screen.ids.food_image_ankara.source = image
        screen.ids.food_ankara_title.text = title
        screen.ids.food_description_ankara.text = description
        screen.ids.food_location_ankara.text = location
        screen.ids.food_hours_ankara.text = hours
        # Butonları sıfırla
        screen.ids.save_button_ankara.icon = "bookmark-outline"
        screen.ids.save_button_ankara.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button_ankara.icon = "heart-outline"
        screen.ids.favorite_button_ankara.text_color = (0, 0, 0, 1)

    def show_place_detail(self, image, title, description, location, hours, *args):
        self.go_to("tarihi_yer_detail")
        screen = self.root.get_screen("tarihi_yer_detail")
        screen.ids.tarihi_yer_image.source = image
        screen.ids.tarihi_yer_istanbul_title.text = title
        screen.ids.tarihi_yer_description.text = description
        screen.ids.tarihi_yer_location.text = location
        screen.ids.tarihi_yer_hours.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_unlu_yerler_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("unlu_yer_istanbul_detail")
        screen = self.root.get_screen("unlu_yer_istanbul_detail")
        screen.ids.unlu_image_istanbul.source = image
        screen.ids.unlu_istanbul_title.text = title
        screen.ids.unlu_description_istanbul.text = description
        screen.ids.unlu_location_istanbul.text = location
        screen.ids.unlu_hours_istanbul.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_cafe_detail_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("cafe_detail_istanbul")
        screen = self.root.get_screen("cafe_detail_istanbul")
        screen.ids.cafe_image_istanbul.source = image
        screen.ids.cafe_title_istanbul.text = title
        screen.ids.cafe_description_istanbul.text = description
        screen.ids.cafe_location_istanbul.text = location
        screen.ids.cafe_hours_istanbul.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_event_detail_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("event_detail")
        screen = self.root.get_screen("event_detail")
        screen.ids.event_image.source = image
        screen.ids.event_istanbul_title.text = title
        screen.ids.event_description.text = description
        screen.ids.event_location.text = location
        screen.ids.event_hours.text = hours


    def show_müze_detail_istanbul(self, image, title, description, location, hours, *args):
        self.go_to("müze_istanbul_detail")
        screen = self.root.get_screen("müze_istanbul_detail")
        screen.ids.müze_image.source = image
        screen.ids.müze_title.text = title
        screen.ids.müze_description.text = description
        screen.ids.müze_location.text = location
        screen.ids.müze_hours.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_place_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("tarihi_yer_detail_ankara")
        screen = self.root.get_screen("tarihi_yer_detail_ankara")
        screen.ids.tarihi_yer_image_ankara.source = image
        screen.ids.tarihi_yer_ankara_title.text = title
        screen.ids.tarihi_yer_description_ankara.text = description
        screen.ids.tarihi_yer_location_ankara.text = location
        screen.ids.tarihi_yer_hours_ankara.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_unlu_yerler_ankara(self, image, title, description, location, hours, *args):
        self.go_to("unlu_yer_ankara_detail")
        screen = self.root.get_screen("unlu_yer_ankara_detail")
        screen.ids.unlu_image_ankara.source = image
        screen.ids.unlu_ankara_title.text = title
        screen.ids.unlu_description_ankara.text = description
        screen.ids.unlu_location_ankara.text = location
        screen.ids.unlu_hours_ankara.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_cafe_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("cafe_detail_ankara")
        screen = self.root.get_screen("cafe_detail_ankara")
        screen.ids.cafe_image_ankara.source = image
        screen.ids.cafe_title_ankara.text = title
        screen.ids.cafe_description_ankara.text = description
        screen.ids.cafe_location_ankara.text = location
        screen.ids.cafe_hours_ankara.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_event_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("event_detail_ankara")
        screen = self.root.get_screen("event_detail_ankara")
        screen.ids.event_image_ankara.source = image
        screen.ids.event_ankara_title.text = title
        screen.ids.event_description_ankara.text = description
        screen.ids.event_location_ankara.text = location
        screen.ids.event_hours_ankara.text = hours


    def show_müze_detail_ankara(self, image, title, description, location, hours, *args):
        self.go_to("müze_ankara_detail")
        screen = self.root.get_screen("müze_ankara_detail")
        screen.ids.müze_image.source = image
        screen.ids.müze_title.text = title
        screen.ids.müze_description.text = description
        screen.ids.müze_location.text = location
        screen.ids.müze_hours.text = hours
        screen.ids.save_button.icon = "bookmark-outline"
        screen.ids.save_button.text_color = (0, 0, 0, 1)
        screen.ids.favorite_button.icon = "heart-outline"
        screen.ids.favorite_button.text_color = (0, 0, 0, 1)

    def show_kaydedilenler_detail(self, image, title, description, location, hours, *args):
        self.go_to("kaydedilenler_detail")
        screen = self.root.get_screen("kaydedilenler_detail")
        screen.ids.saved_image.source = image
        screen.ids.saved_title.text = title
        screen.ids.saved_description.text = description
        screen.ids.saved_location.text = location
        screen.ids.saved_hours.text = hours

    def show_favoriler_detail(self, image, title, description, location, hours, *args):
        self.go_to("favoriler_detail")
        screen = self.root.get_screen("favoriler_detail")
        screen.ids.fav_image.source = image
        screen.ids.fav_title.text = title
        screen.ids.fav_description.text = description
        screen.ids.fav_location.text = location
        screen.ids.fav_hours.text = hours



    def save_place(self, title, description, location, hours, image,*args):
        """Mekanı kaydedilenlere ekler"""
        screen = self.root.get_screen("kaydedilenler")
        container = screen.ids.place_container
        
        # Yeni kart oluştur
        card = MDCard(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10),
            elevation=4,
            radius=[12],
            size_hint_y=None,
            height=dp(260),
            on_release=lambda x: App.get_running_app().show_kaydedilenler_detail(image, title, description, location, hours)
        )
        
        # Kart içeriğini oluştur
        card_content = MDBoxLayout(orientation="vertical")
        
        # Resim
        image_widget = FitImage(
            source=image,
            size_hint_y=None,
            height=dp(180),
            radius=[12, 12, 0, 0]
        )
        
        # Başlık
        title_label = MDLabel(
            text=title,
            font_style="H6",
            theme_text_color="Primary",
            halign="left",
            size_hint_y=None,
            height=dp(40)
        )
        
        # Konum
        location_label = MDLabel(
            text=location,
            font_style="Caption",
            theme_text_color="Secondary",
            halign="left",
            size_hint_y=None,
            height=dp(20)
        )
        
        # Widget'ları karta ekle
        card_content.add_widget(image_widget)
        card_content.add_widget(title_label)
        card_content.add_widget(location_label)
        card.add_widget(card_content)
        
        # Kartı container'a ekle
        container.add_widget(card)

    def favorite_place(self, title, description, location, hours, image, *args):
        """Mekanı favorilere ekler"""
        screen = self.root.get_screen("favoriler")
        container = screen.ids.place_container
        
        # Yeni kart oluştur
        card = MDCard(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10),
            elevation=4,
            radius=[12],
            size_hint_y=None,
            height=dp(260),
            on_release=lambda x: App.get_running_app().show_favoriler_detail(image, title, description, location, hours)

        )
        
        # Kart içeriğini oluştur
        card_content = MDBoxLayout(orientation="vertical")
        
        # Resim
        image_widget = FitImage(
            source=image,
            size_hint_y=None,
            height=dp(180),
            radius=[12, 12, 0, 0]
        )
        
        # Başlık
        title_label = MDLabel(
            text=title,
            font_style="H6",
            theme_text_color="Primary",
            halign="left",
            size_hint_y=None,
            height=dp(40)
        )
        
        # Konum
        location_label = MDLabel(
            text=location,
            font_style="Caption",
            theme_text_color="Secondary",
            halign="left",
            size_hint_y=None,
            height=dp(20)
        )
        
        # Widget'ları karta ekle
        card_content.add_widget(image_widget)
        card_content.add_widget(title_label)
        card_content.add_widget(location_label)
        card.add_widget(card_content)
        
        # Kartı container'a ekle
        container.add_widget(card)

    def show_favoriler_detail(self, image, title, description, location, hours, *args):
        """Favoriler detay sayfasını gösterir"""
        self.go_to("favoriler_detail")
        screen = self.root.get_screen("favoriler_detail")
        screen.ids.fav_image.source = image
        screen.ids.fav_title.text = title
        screen.ids.fav_description.text = description
        screen.ids.fav_location.text = location
        screen.ids.fav_hours.text = hours


if __name__ == '__main__':
    LocalGuideApp().run()