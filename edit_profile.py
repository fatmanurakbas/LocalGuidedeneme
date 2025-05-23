from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.metrics import dp

class EditProfileScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(self.kv_string)

    def go_back_to_profile(self, *args):
        self.manager.current = "profile"

    def open_image_chooser(self):
        chooser = FileChooserIconView()
        popup = Popup(title="Fotoğraf Seç", content=chooser, size_hint=(0.9, 0.9))

        def on_select(instance, selection):
            if selection:
                selected_file = selection[0]
                self.ids.profile_image.source = selected_file
                popup.dismiss()

        chooser.bind(on_selection=on_select)
        popup.open()

    def save_profile(self, *args):
        name = self.ids.name_field.text
        surname = self.ids.surname_field.text
        bio = self.ids.bio_field.text
        photo_path = self.ids.profile_image.source
        print("Profil Bilgileri:", name, surname, bio, photo_path)
        toast("Profil kaydedildi.")

    kv_string = '''
<EditProfileScreen>:
    name: "edit_profile"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Profili Düzenle"
            md_bg_color: "#5C6BC0"
            left_action_items: [["arrow-left", lambda x: root.go_back_to_profile()]]
            elevation: 4
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(20)
                padding: dp(20)
                adaptive_height: True
                size_hint_y: None

                Image:
                    id: profile_image
                    source: "default_profile.png"
                    size_hint: None, None
                    size: dp(130), dp(130)
                    pos_hint: {"center_x": 0.5}
                    allow_stretch: True
                    keep_ratio: True
                    canvas.before:
                        Color:
                            rgba: 0.8, 0.8, 0.8, 1
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [100]

                MDRaisedButton:
                    text: "Fotoğraf Yükle"
                    size_hint_x: 0.6
                    pos_hint: {"center_x": 0.5}
                    on_release: root.open_image_chooser()

                MDTextField:
                    id: name_field
                    hint_text: "Ad"
                    mode: "fill"
                    fill_color: "#eeeeee"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    height: dp(48)

                MDTextField:
                    id: surname_field
                    hint_text: "Soyad"
                    mode: "fill"
                    fill_color: "#eeeeee"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    height: dp(48)

                MDTextField:
                    id: bio_field
                    hint_text: "Biyografi"
                    multiline: True
                    mode: "fill"
                    fill_color: "#eeeeee"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    height: dp(100)

                MDRaisedButton:
                    text: "Kaydet"
                    size_hint_x: 0.5
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: "#5C6BC0"
                    on_release: root.save_profile()
    '''
