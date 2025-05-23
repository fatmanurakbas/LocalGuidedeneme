from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
import json
import os
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp


class PlanlayiciScreen(Screen):
    saatlik_veri = ListProperty()
    plan_dialog = None

    def on_pre_enter(self):
        self.saatlik_veri = [{"text": f"{saat}:00"} for saat in range(8, 21)]

    def save_plan(self):
        gun = self.ids.gun.text
        ay = self.ids.ay.text
        yil = self.ids.yil.text
        notlar = self.ids.notlar.text
        todo1 = self.ids.todo1.text
        todo2 = self.ids.todo2.text
        todo3 = self.ids.todo3.text

        plan = {
            "tarih": f"{gun}/{ay}/{yil}",
            "notlar": notlar,
            "yapilacaklar": [todo1, todo2, todo3]
        }

        os.makedirs("app_data", exist_ok=True)
        path = "app_data/saved_plans.json"
        data = []

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        data.append(plan)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        # 🔄 Giriş alanlarını temizle
        self.ids.gun.text = ""
        self.ids.ay.text = ""
        self.ids.yil.text = ""
        self.ids.notlar.text = ""
        self.ids.todo1.text = ""
        self.ids.todo2.text = ""
        self.ids.todo3.text = ""





    def show_info(self):
        path = "app_data/saved_plans.json"

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    plans = json.load(f)
                except json.JSONDecodeError:
                    plans = []
        else:
            plans = []

        if not plans:
            content = MDLabel(
                text="Henüz kaydedilmiş plan yok.",
                halign="center",
                padding=(10, 10),
                theme_text_color="Secondary"
            )
        else:
            layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10, size_hint_y=None)
            layout.bind(minimum_height=layout.setter("height"))

            for p in plans:
                metin = f"[b]{p['tarih']}[/b]\n{p['notlar']}\n- " + "\n- ".join(p["yapilacaklar"])
                label = MDLabel(
                    text=metin,
                    markup=True,
                    halign="left",
                    theme_text_color="Primary",
                    size_hint_y=None,
                    height=dp(120),
                )
                layout.add_widget(label)

            content = MDScrollView(size_hint=(1, None), height=dp(400))
            content.add_widget(layout)

        self.plan_dialog = MDDialog(
            title="Kaydedilen Planlar",
            type="custom",
            content_cls=content,
            buttons=[MDFlatButton(text="Kapat", on_release=lambda x: self.plan_dialog.dismiss())]
        )
        self.plan_dialog.open()



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
            right_action_items: [["information-outline", lambda x: root.show_info()]]
            md_bg_color: "#5C6BC0"
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(20)
                spacing: dp(20)
                pos_hint: {"center_x": 0.5}

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
                            id: gun
                            hint_text: "Gün"
                            size_hint_x: 0.3

                        MDTextField:
                            id: ay
                            hint_text: "Ay"
                            size_hint_x: 0.3

                        MDTextField:
                            id: yil
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
                        id: notlar
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
                        id: todo1
                        hint_text: "1."
                        size_hint_y: None
                        height: dp(40)

                    MDTextField:
                        id: todo2
                        hint_text: "2."
                        size_hint_y: None
                        height: dp(40)

                    MDTextField:
                        id: todo3
                        hint_text: "3."
                        size_hint_y: None
                        height: dp(40)

                    MDRaisedButton:
                        text: "Kaydet"
                        pos_hint: {"center_x": 0.5}
                        on_release: root.save_plan()


""")
