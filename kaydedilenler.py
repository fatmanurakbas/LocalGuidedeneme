from kivy.lang import Builder
from kivy.uix.screenmanager import Screen  # Burada kivy.uix.screenmanager'dan import ediyoruz

class KaydedilenlerScreen(Screen):
    pass

Builder.load_string("""
<KaydedilenlerScreen>:
    name: "kaydedilenler"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1
                    
        MDTopAppBar:
            title: "Kaydedilenler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
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

                # 1. Kaydedilen Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/atakule.jpg", "Atakule", "Atakule, Ankara'nın simgesel yapılarından biri olup, 125 metre yüksekliğiyle dikkat çeker.", "Dikmen, Ankara", "09:00–22:00")

                    FitImage:
                        source: "images/atakule.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Atakule"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Dikmen, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. Kaydedilen Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/tCDD_building.jpg", "TCDD Genel Müdürlüğü Binası", "TCDD Genel Müdürlüğü Binası, Ankara'daki en eski ve önemli yapılar arasında yer alır.", "Ulus, Ankara", "08:00–17:00")

                    FitImage:
                        source: "images/tCDD_building.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "TCDD Genel Müdürlüğü"
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

                # 3. Kaydedilen Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/ciya.jpg", "Kuzey Güneşi", "Kuzey Güneşi, modern yapısıyla Ankara'nın dikkat çeken binalarından biridir.", "Çankaya, Ankara", "10:00–19:00")

                    FitImage:
                        source: "images/ciya.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kuzey Güneşi"
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
