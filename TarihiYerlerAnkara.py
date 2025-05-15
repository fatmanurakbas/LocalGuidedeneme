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
            query="tarihi_yer",
            near="Ankara, Turkey",
            category="tarihi_yer",
            limit=20
        )
        
        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()
        
        for tarihi_yer in self.places:
            card = MDCard(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(10),
                elevation=4,
                radius=[12],
                size_hint_y=None,
                height=dp(250)
            )
            
            # Resim
            image = FitImage(
                source=tarihi_yer.get('photos', [{}])[0].get('prefix', '') + 
                      '300x200' + 
                      tarihi_yer.get('photos', [{}])[0].get('suffix', ''),
                size_hint_y=None,
                height=dp(200),
                radius=[12, 12, 0, 0]
            )
            
            # İsim
            name_label = MDLabel(
                text=tarihi_yer.get('name', ''),
                font_style="H6",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height=dp(30)
            )
            
            # Adres
            address_label = MDLabel(
                text=tarihi_yer.get('location', {}).get('formatted_address', ''),
                font_style="Caption",
                theme_text_color="Secondary",
                halign="left",
                size_hint_y=None,
                height=dp(30)
            )
            
            card.add_widget(image)
            card.add_widget(name_label)
            card.add_widget(address_label)
            
            # Detay sayfasına yönlendirme
            card.bind(on_release=lambda x, r=tarihi_yer: self.show_tarihi_yer_detail(r))
            
            container.add_widget(card)

    def show_tarihi_yer_detail(self, tarihi_yer):
        app = MDApp.get_running_app()
        app.show_place_detail_ankara(
            tarihi_yer.get('photos', [{}])[0].get('prefix', '') + 
            '800x600' + 
            tarihi_yer.get('photos', [{}])[0].get('suffix', ''),
            tarihi_yer.get('name', '') ,
            tarihi_yer.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            tarihi_yer.get('location', {}).get('formatted_address', '') or 'Bu mekan için adres bulunamamıştır.',
            tarihi_yer.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )


class TarihiYerDetailAnkaraScreen(Screen):
    pass

Builder.load_string("""
<TarihiYerlerAnkaraScreen>:
    name: "tarihi_yerler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Tarihi Yerler Ankara"  # Başlığı burada güncelledik
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            md_bg_color: 0.2, 0.4, 0.8, 1
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
        md_bg_color: 0.0, 0.2, 0.4, 1

        MDTopAppBar:
            title: "Tarihi Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('tarihi_yerler_ankara')]]
            md_bg_color: 0.05, 0.05, 0.3, 1
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
                            icon: "bookmark-outline"
                            pos_hint: {"center_y": 0.5}

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
