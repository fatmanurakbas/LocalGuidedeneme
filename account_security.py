from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast

class AccountSecurityScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Hesabı Dondur", pos_hint={"center_x": 0.5, "center_y": 0.6}, on_release=lambda x: toast("Hesap donduruldu")))
        self.add_widget(MDRaisedButton(text="Hesabı Sil", pos_hint={"center_x": 0.5, "center_y": 0.5}, md_bg_color="#FF5252", on_release=lambda x: toast("Hesap silindi")))
