from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class CafelerAnkaraScreen(MDScreen):
    pass

Builder.load_string("""
<CafelerAnkaraScreen>:
    name: "cafeler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Kafeler - Ankara"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            md_bg_color: 0.2, 0.4, 0.8, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                adaptive_height: True

                # 1. Kafe
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail_ankara("images/KaktüsKahvesi.jpg", "Kaktüs Kahvesi", "Sakin ortamı ve bitki temalı dekorasyonu ile sevilen bir kafe.", "Tunali Hilmi Cad. No:85, Çankaya/Ankara", "09:00–22:00")

                    FitImage:
                        source: "images/KaktüsKahvesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kaktüs Kahvesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Tunali Hilmi Cad. No:85, Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. Kafe
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail_ankara("images/LivaPastanesi.jpg", "Liva Pastanesi", "Klasikleşmiş tatlıları ve kahveleriyle Ankara’nın en bilinen kafelerinden.", "Kavaklıdere Mah. Bestekar Sok. No:82, Çankaya/Ankara", "08:00–23:00")

                    FitImage:
                        source: "images/LivaPastanesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Liva Pastanesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kavaklıdere Mah. Bestekar Sok. No:82, Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
""")



