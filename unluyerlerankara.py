from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.app import MDApp
from foursquare_api import FoursquareAPI
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

class PlazaCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

class UnluYerlerAnkaraScreen(Screen):
    meydanlar = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_plazas)

    def load_plazas(self, dt):
        results = self.api.search_places(
            query="meydan",
            near="Ankara, Turkey",
            category="meydan",
            limit=10
        )

        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()

        for meydan in self.places[2:]:
            fsq_id = meydan.get('fsq_id')
            name = meydan.get('name', '')
            address = meydan.get('location', {}).get('formatted_address', '')

            # Fotoğraf API'den veya cache'ten
            photo_urls = self.api.get_place_photos(fsq_id)
            photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/300"



            # Kart oluştur


            card = MDCard(
                orientation="vertical",
                padding=0,  # padding kaldırıldı
                spacing=dp(0),
                elevation=4,
                radius=[12],
                size_hint_y=None,
                height=dp(290),  # daha büyük kart yüksekliği
                md_bg_color=(1, 1, 1, 1)
            ) 

            # Görsel
            image = FitImage(
               source=photo_url,
               size_hint_y=None,
               height=dp(240),
               radius=[12, 12, 0, 0],
               allow_stretch=True,
               keep_ratio=True,
               pos_hint={"center_x": 0.5}
            )

            # İsim ve adres
            name_label = MDLabel(
                text=name,
                font_style="H6",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height=dp(30),
                padding=(0, dp(5))
            )

            address_label = MDLabel(
                text=address,
                font_style="Caption",
                theme_text_color="Secondary",
                halign="left",
                size_hint_y=None,
                height=dp(24),
                padding=(dp(12), 0)
            )

            card.add_widget(image)
            card.add_widget(name_label)
            card.add_widget(address_label)

            card.bind(on_release=lambda x, r=meydan: self.show_unlu_yer_detail(r))
            container.add_widget(card)

    def show_unlu_yer_detail(self, meydan):
        app = MDApp.get_running_app()
        fsq_id = meydan.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        app.show_unlu_yerler_ankara(
            photo_url,
            meydan.get('name', ''),
            meydan.get('description', '') or 'Ankara’nın tarihi ve kültürel dokusunu keşfetmeniz için bu noktayı ziyaret edebilirsiniz.',
            meydan.get('location', {}).get('formatted_address', '') or 'Bu mekan için adres bilgisi mevcut değildir.',
            meydan.get('hours', {}).get('display', '') or 'Ziyaret saatleriyle ilgili detaylı bilgiye ilgili kaynaklardan ulaşabilirsiniz.'
        )
class UnluYerlerAnkaraDetailScreen(Screen):
    pass


Builder.load_string("""
<UnluYerlerAnkaraScreen>:
    name: "unlu_yerler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        MDTopAppBar:
            title: "Ünlü Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            md_bg_color: "#5C6BC0"
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                id: place_container
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
                    on_release: app.show_unlu_yerler_ankara("images/anitkabir.jpg", "Anıtkabir", "Mustafa Kemal Atatürk'ün anıt mezarıdır ve Ankara'nın en önemli simgelerindendir.", "Çankaya/Ankara", "08:00 - 17:00")

                    FitImage:
                        source: "images/anitkabir.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Anıtkabir"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Çankaya, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. ünlü yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_unlu_yerler_ankara("images/genclikparki.jpg", "Gençlik Parkı", "Büyük göleti, lunaparkı ve yürüyüş alanlarıyla Ankara'nın merkezi parklarından biridir.", "Altındağ/Ankara", "07:00 - 22:00")

                    FitImage:
                        source: "images/genclikparki.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Gençlik Parkı"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Altındağ, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

<UnluYerlerAnkaraDetailScreen>:
    name: "unlu_yer_ankara_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Ünlü Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('unlu_yerler_ankara')]]
            md_bg_color: "#5C6BC0"
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(12)
                size_hint_y: None
                adaptive_height: True

                FitImage:
                    id: unlu_image_ankara
                    size_hint_y: None
                    height: dp(220)
                    radius: [16]
                    allow_stretch: True
                    keep_ratio: False

                MDCard:
                    orientation: "vertical"
                    padding: dp(20)
                    radius: [16]
                    elevation: 6
                    md_bg_color: 0.98, 0.98, 0.98, 1
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(16)

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(8)
                        size_hint_y: None
                        height: self.minimum_height

                        MDLabel:
                            id: unlu_ankara_title
                            text: ""
                            font_style: "H5"
                            theme_text_color: "Primary"
                            bold: True
                            halign: "left"
                            size_hint_x: 0.9
                    
                        MDIconButton:
                            id: save_button
                            icon: "bookmark-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            pos_hint: {"center_y": 0.5}
                            on_release:
                                app.save_place(unlu_ankara_title.text, unlu_description_ankara.text, unlu_location_ankara.text, unlu_hours_ankara.text, unlu_image_ankara.source)
                                self.icon = "bookmark"
                                self.text_color = (0.1, 0.2, 0.7, 1)

                        MDIconButton:
                            id: favorite_button
                            icon: "heart-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            pos_hint: {"center_y": 0.5}
                            on_release:
                                app.favorite_place(unlu_ankara_title.text, unlu_description_ankara.text, unlu_location_ankara.text, unlu_hours_ankara.text, unlu_image_ankara.source)
                                self.icon = "heart"
                                self.text_color = (1, 0, 0, 1)


                    MDLabel:
                        id: unlu_description_ankara
                        text: ""
                        font_style: "Body1"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        text_size: self.width, None
                        height: self.texture_size[1]

                    MDSeparator:

                    MDBoxLayout:
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(24)

                        MDIcon:
                            icon: "map-marker"
                            theme_text_color: "Secondary"
                        MDTextButton:
                            id: unlu_location_ankara
                            text: ""
                            on_release: app.konuma_git(self.text)  # Tıklanınca adresi yolla
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"

                    MDBoxLayout:
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(24)

                        MDIcon:
                            icon: "clock-outline"
                            theme_text_color: "Secondary"
                        MDLabel:
                            id: unlu_hours_ankara
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
