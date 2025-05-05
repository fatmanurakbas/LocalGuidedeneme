from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class AnkaraScreen(MDScreen):
    pass

Builder.load_string("""
<AnkaraScreen>:
    name: "ankara"

    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Ankara"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            md_bg_color: 0.2, 0.4, 0.8, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(12)
                spacing: dp(20)
                size_hint_y: None
                adaptive_height: True

                # 🟦 HAVA DURUMU
                MDCard:
                    orientation: "horizontal"
                    padding: dp(10)
                    radius: [16]
                    elevation: 6
                    size_hint_y: None
                    height: dp(140)
                    md_bg_color: 0.97, 0.97, 1, 1

                    Image:
                        source: "images/ankara.jpg"
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
                            text: "10°C | Perşembe"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Primary"

                        MDLabel:
                            text: "Bulutlu"
                            font_style: "Body2"
                            theme_text_color: "Secondary"
                            halign: "left"

                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: dp(6)
                            size_hint_y: None
                            height: dp(24)

                            MDIcon:
                                icon: "weather-cloudy"
                                theme_text_color: "Secondary"
                                size_hint: None, None
                                size: dp(20), dp(20)

                            MDLabel:
                                text: "Rüzgarlı"
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

                    # Yemek Mekanları
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("food_places_ankara")

                        RelativeLayout:
                            Image:
                                source: "images/ankaralokanta.jpg"
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

                    # Ünlü Yerler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("unlu_yerler_ankara")


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

                    # Müzeler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.show_info()

                        RelativeLayout:
                            Image:
                                source: "images/muzeler.jpg"
                                allow_stretch: True
                                keep_ratio: False

                            MDBoxLayout:
                                orientation: "vertical"
                                padding: dp(8)
                                spacing: dp(6)
                                md_bg_color: 0, 0, 0, 0.4

                                MDIcon:
                                    icon: "bank"
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
                    # 📌 Kaydedilenler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)

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


                    # Tarihi Yerler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)          
                        on_release: app.go_to("tarihi_yerler_ankara")  # Updated to link to the new screen

                        RelativeLayout:
                            Image:
                                source: "images/tarihimekanlarankara.jpg"
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
                                    text: "Tarihi Yerler"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1

                    # Etkinlikler
                    MDCard:
                        radius: [16]
                        elevation: 4
                        size_hint_y: None
                        height: dp(110)
                        on_release: app.go_to("social_events_ankara")

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
