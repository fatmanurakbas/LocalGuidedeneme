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

class CafeCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

class CafelerAnkaraScreen(Screen):
    cafes = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_cafes)

    def load_cafes(self, dt):
        results = self.api.search_places(
            query="kafe",
            near="Ankara, Turkey",
            category="kafe",
            limit=10
        )

        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()

        for kafe in self.places:
            fsq_id = kafe.get('fsq_id')
            name = kafe.get('name', '')
            address = kafe.get('location', {}).get('formatted_address', '')

            # Fotoğraf (API'den veya cache'ten)
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

            card.bind(on_release=lambda x, r=kafe: self.show_kafe_detail(r))
            container.add_widget(card)

    def show_kafe_detail(self, kafe):
        app = MDApp.get_running_app()
        fsq_id = kafe.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        if hasattr(app, 'show_cafe_detail_ankara'):
            app.show_cafe_detail_ankara(
                photo_url,
                kafe.get('name', ''),
                kafe.get('description', '') or 'Sıcak bir atmosferde kahvenizi yudumlamak için sizleri bekliyoruz.',
                kafe.get('location', {}).get('formatted_address', ''),
                kafe.get('hours', {}).get('display', '') or 'Her gün sabah 08:00\'den akşam 22:00\'ye kadar hizmet vermektedir.'
            )
        else:
            print("Hata: app.show_cafe_detail_ankara fonksiyonu bulunamadı. Uygulama ana dosyasında bu fonksiyon tanımlanmalı.")

class CafelerDetailAnkara(Screen):
    pass


Builder.load_string("""
<CafelerAnkaraScreen>:
    name: "cafeler_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Kafeler          "
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

                # 1. Kafe
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_cafe_detail_ankara("images/KaktüsKahvesi.jpg", "Kaktüs Kahvesi", "Sakin ortamı ve bitki temalı dekorasyonu ile sevilen bir kafe.", "Tunali Hilmi Cad. No:85, Çankaya/Ankara", "09:00–22:00")

                    FitImage:
                        source: "images/KaktüsKahvesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kaktüs Kahvesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Tunali Hilmi Cad. No:85, Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. Kafe
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_cafe_detail_ankara("images/LivaPastanesi.jpg", "Liva Pastanesi", "Klasikleşmiş tatlıları ve kahveleriyle Ankara'nın en bilinen kafelerinden.", "Kavaklıdere Mah. Bestekar Sok. No:82, Çankaya/Ankara", "08:00–23:00")

                    FitImage:
                        source: "images/LivaPastanesi.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Liva Pastanesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kavaklıdere Mah. Bestekar Sok. No:82, Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
<CafelerDetailAnkara>:
    name: "cafe_detail_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Kafeler         "
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('cafeler_ankara')]]
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
                    id: cafe_image_ankara
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
                            id: cafe_title_ankara
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
                            on_release:
                                app.save_place(cafe_title_ankara.text, cafe_description_ankara.text, cafe_location_ankara.text, cafe_hours_ankara.text, cafe_image_ankara.source)
                                self.icon = "bookmark"
                                self.text_color = (0.1, 0.2, 0.7, 1)

                        MDIconButton:
                            id: favorite_button
                            icon: "heart-outline"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            on_release:
                                app.favorite_place(cafe_title_ankara.text, cafe_description_ankara.text, cafe_location_ankara.text, cafe_hours_ankara.text, cafe_image_ankara.source)
                                self.icon = "heart"
                                self.text_color = (1, 0, 0, 1)
                    
                    MDLabel:
                        id: cafe_description_ankara
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
                        padding: [dp(11.5), 0, 0, 0]

                        MDIcon:
                            icon: "map-marker"
                            theme_text_color: "Secondary"
                        MDTextButton:
                            id: cafe_location_ankara
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
                            id: cafe_hours_ankara
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")



