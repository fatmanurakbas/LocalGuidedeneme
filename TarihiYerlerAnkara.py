from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class TarihiYerlerAnkaraScreen(Screen):
    pass

Builder.load_string("""
<TarihiYerlerAnkaraScreen>:
    name: "tarihi_yerler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Tarihi Yerler Ankara"  # Başlığı burada güncelledik
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            md_bg_color: 0.1, 0.1, 0.5, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                adaptive_height: True

                # 1. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/atatürk_mausoleum.jpg", "Anıtkabir", "Anıtkabir, Türkiye Cumhuriyeti'nin kurucusu Mustafa Kemal Atatürk'ün anıt mezarına ev sahipliği yapmaktadır.", "Çankaya, Ankara", "08:00–17:00")

                    FitImage:
                        source: "images/atatürk_mausoleum.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Anıtkabir"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Çankaya, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/haci_bayram_veli_mosque.jpg", "Hacı Bayram Veli Camii", "Hacı Bayram Veli Camii, Ankara'nın tarihi camilerindendir ve Hacı Bayram Veli'nin türbesine ev sahipliği yapmaktadır.", "Ulus, Ankara", "08:00–20:00")

                    FitImage:
                        source: "images/haci_bayram_veli_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Hacı Bayram Veli Camii"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Ulus, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 3. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/kocatepe_mosque.jpg", "Kocatepe Camii", "Kocatepe Camii, Türkiye'nin en büyük camilerinden biri olup, Ankara'nın önemli simgelerindendir.", "Kocatepe, Ankara", "08:00–18:00")

                    FitImage:
                        source: "images/kocatepe_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kocatepe Camii"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kocatepe, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
""")
