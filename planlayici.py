from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

class PlanlayiciScreen(Screen):
    saatlik_veri = ListProperty()

    def on_pre_enter(self):
        self.saatlik_veri = [{"text": f"{saat}:00"} for saat in range(8, 21)]

Builder.load_string("""
<PlanlayiciScreen>:
    name: "planlayici"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.95, 0.95, 1

        MDTopAppBar:
            title: "GÜNLÜK PLANLAYICI"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            right_action_items: [["information-outline", lambda x: app.show_info()]]
            md_bg_color: 0.2, 0.4, 0.6, 1
            size_hint_y: None
            height: dp(56)

        # Ekranı ortalayacak kapsayıcı ScrollView
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(20)
                spacing: dp(20)
                pos_hint: {"center_x": 0.5}

                # Tek başına ortalanmış panel (sağdaki içerik)
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(12)
                    padding: dp(20)
                    size_hint: None, None
                    size: dp(300), self.minimum_height
                    pos_hint: {"center_x": 0.5}
                    radius: [16]
                    md_bg_color: 0.96, 0.97, 0.98, 1

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(8)
                        size_hint_y: None
                        height: dp(40)

                        MDTextField:
                            hint_text: "Gün"
                            size_hint_x: 0.3

                        MDTextField:
                            hint_text: "Ay"
                            size_hint_x: 0.3

                        MDTextField:
                            hint_text: "Yıl"
                            size_hint_x: 0.4

                    MDLabel:
                        text: "NOTLAR"
                        bold: True
                        halign: "center"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: dp(24)

                    MDTextField:
                        hint_text: "Notlarınızı buraya yazın..."
                        multiline: True
                        size_hint_y: None
                        height: dp(100)

                    MDLabel:
                        text: "YAPILACAKLAR"
                        bold: True
                        halign: "center"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: dp(24)

                    MDTextField:
                        hint_text: "1."
                        size_hint_y: None
                        height: dp(40)
                    MDTextField:
                        hint_text: "2."
                        size_hint_y: None
                        height: dp(40)
                    MDTextField:
                        hint_text: "3."
                        size_hint_y: None
                        height: dp(40)

""")
