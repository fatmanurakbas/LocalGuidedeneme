from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

Window.size = (360, 640)

class FoodPlacesAnkaraScreen(Screen):
    pass

class FoodDetailAnkaraScreen(Screen):
    pass

Builder.load_string('''
<FoodPlacesAnkaraScreen>:
    name: "food_places_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Ankara Yemek Mekanları"
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

                MDRaisedButton:
                    text: "Trilye Restaurant"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    on_release: app.show_food_detail_ankara("trilye.jpg", "Deniz ürünlerinde uzmanlaşmış, Ankara'nın gözde restoranlarından.", "Kazım Özalp Mahallesi, Kuleli Sk. No:32, Çankaya/Ankara", "12:00–23:00")

                MDRaisedButton:
                    text: "Fige Restaurant"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    on_release: app.show_food_detail_ankara("fige.jpg", "Romantik atmosferi ve dünya mutfağından seçkiler sunan popüler bir mekan.", "Hilal Mahallesi, Hollanda Cad. No:3, Çankaya/Ankara", "11:30–00:00")

                MDRaisedButton:
                    text: "Göksu Lokantasi"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    on_release: app.show_food_detail_ankara("goksu.jpg", "Klasik Türk yemeklerinin en iyi örneklerini sunan bir aile lokantası.", "Siyasal Bilgiler Fakültesi Karşısı, Cebeci/Ankara", "10:00–22:00")

<FoodDetailAnkaraScreen>:
    name: "food_detail_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.95, 0.95, 1, 1

        MDTopAppBar:
            title: "Mekan Detayı"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            md_bg_color: 0.1, 0.1, 0.5, 1
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(10)
                size_hint_y: None
                adaptive_height: True

                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_x: 0.95
                    pos_hint: {"center_x": 0.5}
                    elevation: 8
                    radius: [20]

                    Image:
                        id: food_image_ankara
                        size_hint_y: None
                        height: dp(220)
                        allow_stretch: True
                        keep_ratio: True

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(10)
                        padding: dp(10)

                        MDLabel:
                            id: food_description_ankara
                            text: "Açıklama"
                            font_style: "Body1"
                            halign: "center"

                        MDLabel:
                            id: food_location_ankara
                            text: "Konum"
                            font_style: "Caption"
                            halign: "center"

                        MDLabel:
                            id: food_hours_ankara
                            text: "Çalışma Saatleri"
                            font_style: "Caption"
                            halign: "center"
''')
