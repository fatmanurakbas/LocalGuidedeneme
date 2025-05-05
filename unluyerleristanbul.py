from kivy.lang import Builder
from kivy.uix.screenmanager import Screen  # Burada kivy.uix.screenmanager'dan import ediyoruz

class UnluYerlerIstanbulScreen(Screen):
    pass

Builder.load_string("""
<UnluYerlerIstanbulScreen>:
    name: "unlu_yerler_istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1
                    
        MDTopAppBar:
            title: "Ünlü Yerler"
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
                        
                # 1. ünlü yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_unlu_yerler_istanbul("images/istiklalcaddesi.jpg", "İstiklal Caddesi", "İstikal Caddesi, Türkiye'nin en önemli caddelerinden biridir.", "Üsküdar/İstanbul", "Her zaman açık")                    

                    FitImage:
                        source: "images/istiklalcaddesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "İstiklal Caddesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Beyoğlu, İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]




""")                    