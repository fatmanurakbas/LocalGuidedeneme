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

class UnluYerlerIstanbulScreen(Screen):
    meydanlar = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_plazas)

    def load_plazas(self, dt):
        results = self.api.search_places(
            query="meydan",
            near="İstanbul, Turkey",
            category="meydan",
            limit=10
        )

        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()

        for meydan in self.places:
            fsq_id = meydan.get('fsq_id')
            name = meydan.get('name', '')
            address = meydan.get('location', {}).get('formatted_address', '')

            # Fotoğrafı API'den veya cache'ten al
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
                padding=(dp(12), dp(5)),
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

            card.bind(on_release=lambda x, r=meydan: self.show_unlu_yer_detail(r))
            container.add_widget(card)

    def show_unlu_yer_detail(self, meydan):
        app = MDApp.get_running_app()
        fsq_id = meydan.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        app.show_unlu_yerler_istanbul(
            photo_url,
            meydan.get('name', ''),
            meydan.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            meydan.get('location', {}).get('formatted_address', '') or 'Bu mekan için adres bulunamadı.',
            meydan.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class UnluYerlerIstanbulDetailScreen(Screen):
    pass


Builder.load_string("""
<UnluYerlerIstanbulScreen>:
    name: "unlu_yerler_istanbul"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
                    
        MDTopAppBar:
            title: "Ünlü Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('istanbul')]]
            md_bg_color: "#5C6BC0"
            size_hint_y: None
            height: dp(56)
                    
        ScrollView:
            MDBoxLayout:
                id:place_container
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
                    on_release: app.show_unlu_yerler_istanbul("images/istiklalcaddesi.jpg", "İstiklal Caddesi", "İstikal Caddesi, Türkiye'nin en önemli caddelerinden biridir.", "Beyoğlu/İstanbul", "Her zaman açık")                    

                    FitImage:
                        source: "images/istiklalcaddesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "İstiklal Caddesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Beyoğlu, İstanbul"
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
                    on_release: app.show_unlu_yerler_istanbul("images/kuzguncuk.jpg", "Kuzguncuk", "Mahalle kültürü, ahşap evleri ve Arnavut kaldırımlı sokaklarıyla İstanbul'un nostaljik noktalarından biridir. ", "Üsküdar/İstanbul", "Her zaman açık")                    

                    FitImage:
                        source: "images/kuzguncuk.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kuzguncuk"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Üsküdar, İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
<UnluYerlerIstanbulDetailScreen>:
    name: "unlu_yer_istanbul_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        MDTopAppBar:
            title: "Ünlü Yerler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('unlu_yerler_istanbul')]]
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
                    id: unlu_image_istanbul
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
                            id: unlu_istanbul_title
                            text: ""
                            font_style: "Subtitle1"
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
                                app.save_place(unlu_istanbul_title.text, unlu_description_istanbul.text, unlu_location_istanbul.text, unlu_hours_istanbul.text, unlu_image_istanbul.source)
                                self.icon = "bookmark"
                                self.text_color = (0.1, 0.2, 0.7, 1)

                        MDIconButton:
                            id: favorite_button
                            icon: "heart-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            pos_hint: {"center_y": 0.5}
                            on_release:
                                app.favorite_place(unlu_istanbul_title.text, unlu_description_istanbul.text, unlu_location_istanbul.text, unlu_hours_istanbul.text, unlu_image_istanbul.source)
                                self.icon = "heart"
                                self.text_color = (1, 0, 0, 1)

                    MDLabel:
                        id: unlu_description_istanbul
                        text: ""
                        font_style: "Body1"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        text_size: self.width, None
                        height: self.texture_size[1]

                    MDSeparator:

                    MDBoxLayout:
                        spacing: dp(19)
                        size_hint_y: None
                        height: dp(24)
                        padding: [dp(11.5), 0, 0, 0]  # Sola 16dp boşluk ekledik, bu sayede içerik sağa kayar
                    
                        MDIcon:
                            icon: "map-marker"
                            theme_text_color: "Secondary"
                        MDTextButton:
                            id: unlu_location_istanbul
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
                            id: unlu_hours_istanbul
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")                    