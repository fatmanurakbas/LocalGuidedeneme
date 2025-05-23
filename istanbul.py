from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from datetime import datetime
from kivy.clock import Clock
from kivy.metrics import dp
import requests

from kivy.uix.screenmanager import Screen

class IstanbulScreen(MDScreen):
    def on_enter(self):
        # Ekran açılır açılmaz hava durumunu çek
        Clock.schedule_once(lambda dt: self.fetch_weather_data(), 0)

    def fetch_weather_data(self):
        api_key = "9cfff90aa46036e986416a727bdb45be"
        url = f"https://api.openweathermap.org/data/2.5/weather?q=Istanbul&appid={api_key}&units=metric&lang=tr"
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            if response.status_code == 200:
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"].capitalize()
                wind_speed = data["wind"]["speed"]

                days_tr = {
                    "Monday": "Pazartesi",
                    "Tuesday": "Salı",
                    "Wednesday": "Çarşamba",
                    "Thursday": "Perşembe",
                    "Friday": "Cuma",
                    "Saturday": "Cumartesi",
                    "Sunday": "Pazar"
                }
                day_en = datetime.now().strftime("%A")
                day_tr = days_tr.get(day_en, day_en)

                self.ids.weather_temp_label.text = f"{temp:.1f}°C | {day_tr}"
                self.ids.weather_desc_label.text = description
                self.ids.weather_wind_label.text = f"Rüzgar: {wind_speed} m/s"
            else:
                self.ids.weather_temp_label.text = "Hava durumu alınamadı"
                self.ids.weather_desc_label.text = ""
                self.ids.weather_wind_label.text = ""
        except Exception as e:
            self.ids.weather_temp_label.text = "Hava durumu hatası"
            self.ids.weather_desc_label.text = ""
            self.ids.weather_wind_label.text = ""
            print(f"Weather API error: {e}")

    
Builder.load_string("""
<IstanbulScreen>:
    name: "istanbul"
    halign: "center"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1
                    
        MDTopAppBar:
            title: "İSTANBUL        "
            anchor_title: "center"
            title_font_style: "H2"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('home')]]
            md_bg_color: "#5C6BC0"  # Soft mavi
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(12)
                spacing: dp(20)
                size_hint_y: None
                adaptive_height: True

                # 🟦 HAVA DURUMU KARTI
                MDCard:
                    orientation: "horizontal"
                    padding: dp(10)
                    radius: [16]
                    elevation: 6
                    size_hint_y: None
                    height: dp(140)
                    md_bg_color: 0.97, 0.97, 1, 1

                    Image:
                        source: "images/istanbul1.jpg"
                        size_hint_x: None
                        width: dp(130)
                        allow_stretch: True
                        keep_ratio: False
                        radius: [12]

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: dp(10)
                        spacing: dp(4)

                        MDLabel:
                            id: weather_temp_label
                            text: " "
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Primary"

                        MDLabel:
                            id: weather_desc_label
                            text: " "
                            font_style: "Body2"
                            theme_text_color: "Secondary"
                            halign: "left"

                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: dp(6)
                            size_hint_y: None
                            height: dp(24)

                            MDIcon:
                                icon: "weather-partly-cloudy"
                                theme_text_color: "Secondary"
                                size_hint: None, None
                                size: dp(20), dp(20)

                            MDLabel:
                                id: weather_wind_label
                                text: " "
                                font_style: "Caption"
                                theme_text_color: "Secondary"
                                halign: "left"

                # 🟩 KATEGORİ KARTLARI
                MDGridLayout:
                    cols: 2
                    spacing: dp(12)
                    padding: dp(4)
                    size_hint_y: None
                    adaptive_height: True

                    # 📍 Yemek Mekanları
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to('food_places')

                        RelativeLayout:
                            Image:
                                source: "images/yemek.png"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "silverware-fork-knife"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Yemek Mekanları"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                    # 🌟 Ünlü Yerler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to('unlu_yerler_istanbul')
                    
                        RelativeLayout:
                            Image:
                                source: "images/unluyerler.jpg"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "star"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Ünlü Yerler"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    

                    # ☕ Cafeler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("cafeler_istanbul") 
                    

                        RelativeLayout:
                            Image:
                                source: "images/cafe.jpg"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "coffee"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Cafeler"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                    # 📌 Müzeler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("müze_istanbul") 

                        RelativeLayout:
                            Image:
                                source: "images/müzee.jpg"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "bookmark"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Müzeler"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                    # 🏰 Tarihi Mekanlar
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("tarihi_yerler_istanbul")  # Updated to link to the new screen

                        RelativeLayout:
                            Image:
                                source: "images/tarihimekanlar.jpg"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "castle"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Tarihi Mekanlar"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                    # 📆 Etkinlikler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("social_events_ist")
                    

                        RelativeLayout:
                            Image:
                                source: "images/etkinlik.png"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "calendar"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    size_hint_y: None
                                    height: dp(24)

                                MDLabel:
                                    text: "Etkinlikler"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                
""")
