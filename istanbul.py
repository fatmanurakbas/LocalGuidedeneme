from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class IstanbulScreen(MDScreen):
    pass

Builder.load_string("""
<IstanbulScreen>:
    name: "istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1
                    
        MDTopAppBar:
            title: "İstanbul"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('home')]]
            md_bg_color: 0.2, 0.4, 0.8, 1
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
                            text: "12°C | Çarşamba"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Primary"

                        MDLabel:
                            text: "Parçalı Bulutlu"
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
                                text: "Hafif Rüzgar"
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

                    # 📌 Kaydedilenler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("kaydedilenler") 

                        RelativeLayout:
                            Image:
                                source: "images/kaydedilenler.jpg"
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
                                    text: "Kaydedilenler"
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
