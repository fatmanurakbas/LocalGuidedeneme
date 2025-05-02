from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class TarihiYerlerIstanbulScreen(Screen):
    pass

Builder.load_string("""
<TarihiYerlerIstanbulScreen>:
    name: "tarihi_yerler_istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Tarihi Yerler İstanbul"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('istanbul')]]
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
                    on_release: app.show_food_detail("images/hagiasophia.jpg", "Ayasofya", "Ayasofya, Bizans İmparatoru I. Justinianus tarafından 537 yılında kilise olarak inşa edilmiştir.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/hagiasophia.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Ayasofya"
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

                # 2. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/topkapi_palace.jpg", "Topkapı Sarayı", "Topkapı Sarayı, Osmanlı İmparatorluğu'na 400 yıl boyunca başkentlik yapmış olan İstanbul'un simgelerinden biridir.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/topkapi_palace.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Topkapı Sarayı"
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

                # 3. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail("images/blue_mosque.jpg", "Sultanahmet Camii", "Sultanahmet Camii, İstanbul’un en bilinen tarihi camilerinden biridir ve mavi çinileri ile ünlüdür.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/blue_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Sultanahmet Camii"
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
""")
