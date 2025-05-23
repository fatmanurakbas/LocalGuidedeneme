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

class HistoricCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

class TarihiYerlerAnkaraScreen(Screen):
    tarihi_yerler = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_tarihi_yerler)

    def load_tarihi_yerler(self, dt):
        results = self.api.search_places(
            query="tarihi yer",
            near="Ankara, Turkey",
            category="tarihi_yer",
            limit=10
        )

        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()

        for tarihi_yer in self.places[1:]:
            fsq_id = tarihi_yer.get('fsq_id')
            name = tarihi_yer.get('name', '')
            address = tarihi_yer.get('location', {}).get('formatted_address', '')

            # Fotoğraf çek (önce cache kontrol edilir)
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
                font_style="Body1",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height=dp(30),
                padding=(0, dp(5)),
                shorten=True,
                shorten_from='right'
            )

            address_label = MDLabel(
                text=address,
                font_style="Caption",
                theme_text_color="Secondary",
                halign="left",
                size_hint_y=None,
                height=dp(24),
                padding=(dp(12), 0),
                shorten=True,
                shorten_from='right'

            )

            card.add_widget(image)
            card.add_widget(name_label)
            card.add_widget(address_label)

            # Detay ekranına yönlendirme
            card.bind(on_release=lambda x, r=tarihi_yer: self.show_tarihi_yer_detail(r))

            container.add_widget(card)

    def show_tarihi_yer_detail(self, tarihi_yer):
        app = MDApp.get_running_app()
        fsq_id = tarihi_yer.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        app.show_place_detail_ankara(
            photo_url,
            tarihi_yer.get('name', ''),
            tarihi_yer.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            tarihi_yer.get('location', {}).get('formatted_address', '') or 'Adres bilgisi bulunamadı.',
            tarihi_yer.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class TarihiYerDetailAnkaraScreen(Screen):
    pass


Builder.load_string("""
<TarihiYerlerAnkaraScreen>:
    name: "tarihi_yerler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Tarihi Yerler Ankara"  # Başlığı burada güncelledik
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

                # 1. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_place_detail_ankara("images/atatürk_mausoleum.jpg", "Anıtkabir", "Anıtkabir, Türkiye Cumhuriyeti'nin kurucusu Mustafa Kemal Atatürk'ün anıt mezarına ev sahipliği yapmaktadır.", "Çankaya, Ankara", "08:00–17:00")

                    FitImage:
                        source: "images/atatürk_mausoleum.jpg"
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

                # 2. Tarihi Yer
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_place_detail_ankara("images/haci_bayram_veli_mosque.jpg", "Hacı Bayram Veli Camii", "Hacı Bayram Veli Camii, Ankara'nın tarihi camilerindendir ve Hacı Bayram Veli'nin türbesine ev sahipliği yapmaktadır.", "Ulus, Ankara", "08:00–20:00")

                    FitImage:
                        source: "images/haci_bayram_veli_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Hacı Bayram Veli Camii"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Ulus, Ankara"
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
                    on_release: app.show_place_detail_ankara("images/kocatepe_mosque.jpg", "Kocatepe Camii", "Kocatepe Camii, Türkiye'nin en büyük camilerinden biri olup, Ankara'nın önemli simgelerindendir.", "Kocatepe, Ankara", "08:00–18:00")

                    FitImage:
                        source: "images/kocatepe_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kocatepe Camii"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kocatepe, Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
<TarihiYerDetailAnkaraScreen>:
    name: "tarihi_yer_detail_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Tarihi Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('tarihi_yerler_ankara')]]
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
                    id: tarihi_yer_image_ankara
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
                            id: tarihi_yer_ankara_title
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
                            on_release:
                                app.save_place(tarihi_yer_ankara_title.text, tarihi_yer_description_ankara.text, tarihi_yer_location_ankara.text, tarihi_yer_hours_ankara.text, tarihi_yer_image_ankara.source)
                                self.icon = "bookmark"
                                self.text_color = (0.1, 0.2, 0.7, 1)

                        MDIconButton:
                            id: favorite_button
                            icon: "heart-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            on_release:
                                app.favorite_place(tarihi_yer_ankara_title.text, tarihi_yer_description_ankara.text, tarihi_yer_location_ankara.text, tarihi_yer_hours_ankara.text, tarihi_yer_image_ankara.source)
                                self.icon = "heart"
                                self.text_color = (1, 0, 0, 1)

                    MDLabel:
                        id: tarihi_yer_description_ankara
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
                            id: tarihi_yer_location_ankara
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
                            id: tarihi_yer_hours_ankara
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
