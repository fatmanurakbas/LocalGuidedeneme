from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel

class NotificationSettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text="Uygulama İçi Bildirimler", pos_hint={"center_x": 0.5, "center_y": 0.7}))
        self.add_widget(MDSwitch(pos_hint={"center_x": 0.5, "center_y": 0.6}))
