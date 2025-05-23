from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast

class ThemeSettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Açık Tema", pos_hint={"center_x": 0.5, "center_y": 0.6}, on_release=lambda x: self.change_theme("Light")))
        self.add_widget(MDRaisedButton(text="Karanlık Tema", pos_hint={"center_x": 0.5, "center_y": 0.5}, on_release=lambda x: self.change_theme("Dark")))

    def change_theme(self, theme):
        toast(f"{theme} tema seçildi")
