from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class CafelerIstanbulScreen(MDScreen):
    pass

Builder.load_string("""
<CafelerIstanbulScreen>:
    name: "cafeler_istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Kafeler - İstanbul"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('istanbul')]]
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
                    on_release: app.show_food_detail("images/mocistanbul.jpg", "MOC İstanbul", "Kahve severler için modern ve huzurlu bir ortam sunan popüler bir üçüncü nesil kahve dükkanı.", "Teşvikiye, Şakayık Sk. No:4, Şişli/İstanbul", "08:00–22:00")

                    FitImage:
                        source: "images/mocistanbul.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "MOC İstanbul"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Teşvikiye, Şakayık Sk. No:4, Şişli/İstanbul"
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
                    on_release: app.show_food_detail("images/Coffeesapiens.jpg", "Coffee Sapiens", "Karaköy’ün kalbinde taptaze çekirdekler ve özgün kahveler sunan butik bir kahveci.", "Kemankeş Karamustafa Paşa, Kılıç Ali Paşa Mescidi Sk. No:10, Beyoğlu/İstanbul", "09:00–21:00")

                    FitImage:
                        source: "images/Coffeesapiens.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Coffee Sapiens"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kemankeş Karamustafa Paşa, Kılıç Ali Paşa Mescidi Sk. No:10, Beyoğlu/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
""")
