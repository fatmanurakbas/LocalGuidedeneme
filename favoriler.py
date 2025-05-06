from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class FavorilerScreen(Screen):
    pass

Builder.load_string("""
<FavorilerScreen>:
    name: "favoriler"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Favoriler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            md_bg_color: 0.1, 0.1, 0.5, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(16)
                padding: dp(16)
                size_hint_y: None
                adaptive_height: True

                # Favori Yer 1
                MDCard:
                    orientation: "vertical"
                    radius: [12]
                    elevation: 4
                    size_hint_y: None
                    height: dp(260)
                    padding: dp(10)
                    spacing: dp(10)
                    on_release: app.show_food_detail("images/sultanahmet.jpg", "Tarihi Sultanahmet Köftecisi", "1920'den bu yana lezzet sunan tarihi mekan.", "Divan Yolu Cad. No:12, Sultanahmet/İstanbul", "11:00–23:00")

                    FitImage:
                        source: "images/sultanahmet.jpg"
                        size_hint_y: None
                        height: dp(180)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Tarihi Sultanahmet Köftecisi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sultanahmet, İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # Favori Yer 2
                MDCard:
                    orientation: "vertical"
                    radius: [12]
                    elevation: 4
                    size_hint_y: None
                    height: dp(260)
                    padding: dp(10)
                    spacing: dp(10)
                    on_release: app.show_food_detail_ankara("images/LivaPastanesi.jpg", "Liva Pastanesi", "Tatlıları ve şık atmosferiyle ünlü Ankara mekanı.", "Bestekar Sok. No:82, Çankaya/Ankara", "08:00–23:00")

                    FitImage:
                        source: "images/LivaPastanesi.jpg"
                        size_hint_y: None
                        height: dp(180)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Liva Pastanesi"
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
""")
