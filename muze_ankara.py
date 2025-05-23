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

class MuseumCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

class MuseumAnkaraScreen(Screen):
    museums = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_museum)

    def load_museum(self, dt):
        results = self.api.search_places(
            query="müze",
            near="Ankara, Turkey",
            category="müze",
            limit=10
        )

        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()

        for müze in self.places[1:]:
            fsq_id = müze.get("fsq_id")
            name = müze.get("name", "")
            address = müze.get("location", {}).get("formatted_address", "")

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

            card.bind(on_release=lambda x, r=müze: self.show_museum_detail_ankara(r))
            container.add_widget(card)

    def show_museum_detail_ankara(self, müze):
        app = MDApp.get_running_app()
        fsq_id = müze.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        app.show_müze_detail_ankara(
            photo_url,
            müze.get('name', ''),
            müze.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            müze.get('location', {}).get('formatted_address', '') or 'Bu mekan için adres bulunamadı.',
            müze.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class MuseumAnkaraDetailScreen(Screen):
    pass


Builder.load_string("""
<MuseumAnkaraScreen>:
    name: "müze_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Müzeler          "
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
                    on_release: app.show_place_detail("images/blue_mosque.jpg", "Sultanahmet Camii", "Sultanahmet Camii, İstanbul'un en bilinen tarihi camilerinden biridir ve mavi çinileri ile ünlüdür.", "Sultanahmet, İstanbul", "09:00–18:00")

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
                    
<MuseumAnkaraDetailScreen>:
    name: "müze_ankara_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Müzeler          "
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('müze_ankara')]]
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
                    id: müze_image
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

                    Widget:
                        size_hint_y: None
                        height: dp(4)
                    

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(8)
                        size_hint_y: None
                        height: self.minimum_height

                        MDLabel:
                            id: müze_title
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
                                app.save_place(müze_title.text, müze_description.text, müze_location.text, müze_hours.text, müze_image.source)
                                self.icon = "bookmark"
                                self.text_color = (0.1, 0.2, 0.7, 1)

                        MDIconButton:
                            id: favorite_button
                            icon: "heart-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            pos_hint: {"center_y": 0.5}
                            on_release:
                                app.favorite_place(müze_title.text, müze_description.text, müze_location.text, müze_hours.text, müze_image.source)
                                self.icon = "heart"
                                self.text_color = (1, 0, 0, 1)


                    
                    Widget:
                        size_hint_y: None
                        height: dp(10)
                    

                    MDLabel:
                        id: müze_description
                        text: "Açıklama"
                        font_style: "Body1"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        text_size: self.width, None
                        height: self.texture_size[1]


                    MDBoxLayout:
                        spacing: dp(19)
                        size_hint_y: None
                        height: dp(24)
                        padding: [dp(11.5), 0, 0, 0]
                    
                        MDIcon:
                            icon: "map-marker"
                            theme_text_color: "Secondary"
                        MDTextButton:
                            id: müze_location
                            text: "Konum"
                            on_release: app.konuma_git(self.text)  # Tıklanınca adresi yolla
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
                            shorten: True
                            shorten_from: 'right'

                    MDBoxLayout:
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(24)

                        MDIcon:
                            icon: "clock-outline"
                            theme_text_color: "Secondary"
                        MDLabel:
                            id: müze_hours
                            text: "Çalışma Saatleri"
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
