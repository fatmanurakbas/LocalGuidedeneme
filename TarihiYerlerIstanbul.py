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


class TarihiYerlerIstanbulScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_tarihi_yerler)

    def load_tarihi_yerler(self, dt):
        results = self.api.search_places(
            query="tarihi_yer",
            near="İstanbul, Turkey",
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
        app.show_place_detail(
            tarihi_yer.get('photos', [{}])[0].get('prefix', '') + 
            '800x600' + 
            tarihi_yer.get('photos', [{}])[0].get('suffix', ''),
            tarihi_yer.get('name', '') ,
            tarihi_yer.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            tarihi_yer.get('location', {}).get('formatted_address', '') or 'Bu mekan için adres bulunamamıştır.',
            tarihi_yer.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class TarihiYerDetailScreen(Screen):
    pass

Builder.load_string("""
<TarihiYerlerIstanbulScreen>:
    name: "tarihi_yerler_istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Tarihi Yerler İstanbul"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('istanbul')]]
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
                    on_release: app.show_place_detail("images/hagiasophia.jpg", "Ayasofya", "Ayasofya, Bizans İmparatoru I. Justinianus tarafından 537 yılında kilise olarak inşa edilmiştir.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/hagiasophia.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Ayasofya"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sultanahmet, İstanbul"
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
                    on_release: app.show_place_detail("images/topkapi_palace.jpg", "Topkapı Sarayı", "Topkapı Sarayı, Osmanlı İmparatorluğu'na 400 yıl boyunca başkentlik yapmış olan İstanbul'un simgelerinden biridir.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/topkapi_palace.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Topkapı Sarayı"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sultanahmet, İstanbul"
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
                    on_release: app.show_place_detail("images/blue_mosque.jpg", "Sultanahmet Camii", "Sultanahmet Camii, İstanbul’un en bilinen tarihi camilerinden biridir ve mavi çinileri ile ünlüdür.", "Sultanahmet, İstanbul", "09:00–18:00")

                    FitImage:
                        source: "images/blue_mosque.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Sultanahmet Camii"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sultanahmet, İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
<TarihiYerDetailScreen>:
    name: "tarihi_yer_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.0, 0.2, 0.4, 1

        MDTopAppBar:
            title: "Tarihi Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('tarihi_yerler_istanbul')]]
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
                    id: tarihi_yer_image
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
                            id: tarihi_yer_istanbul_title
                            text: "Yer Adı"
                            font_style: "H5"
                            theme_text_color: "Primary"
                            bold: True
                            halign: "left"
                            size_hint_x: 0.9

                        MDIconButton:
                            icon: "bookmark-outline"
                            pos_hint: {"center_y": 0.5}

                    MDLabel:
                        id: tarihi_yer_description
                        text: "Açıklama"
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
                            id: tarihi_yer_location
                            text: "Konum"
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
                            id: tarihi_yer_hours
                            text: "Çalışma Saatleri"
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
