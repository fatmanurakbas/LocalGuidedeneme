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

class RestaurantCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

class FoodPlacesAnkaraScreen(Screen):
    restaurants = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_restaurants)

    def load_restaurants(self, dt):
        results = self.api.search_places(
            query="restaurant",
            near="Ankara, Turkey",
            limit=10
        )
        if results and 'results' in results:
            self.restaurants = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.restaurant_container
        container.clear_widgets()

        for restaurant in self.restaurants:
            fsq_id = restaurant.get('fsq_id')
            name = restaurant.get('name', '')
            address = restaurant.get('location', {}).get('formatted_address', '')

            # Fotoğraf URL'si (önce cache kontrol edilir)
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

            # Detay ekranına yönlendirme
            card.bind(on_release=lambda x, r=restaurant: self.show_restaurant_detail_ankara(r))

            container.add_widget(card)

    def show_restaurant_detail_ankara(self, restaurant):
        app = MDApp.get_running_app()
        fsq_id = restaurant.get('fsq_id')
        photo_urls = self.api.get_place_photos(fsq_id)
        photo_url = photo_urls[0] if photo_urls else "https://via.placeholder.com/800"

        app.show_food_detail_ankara(
            photo_url,
            restaurant.get('name', ''),
            restaurant.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            restaurant.get('location', {}).get('formatted_address', ''),
            restaurant.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class FoodDetailAnkaraScreen(Screen):
    pass

Builder.load_string("""
<FoodPlacesAnkaraScreen>:
    name: "food_places_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Yemek Mekanları"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            md_bg_color: "#5C6BC0"  # Soft mavi
            size_hint_y: None
            height: dp(56)

        ScrollView:
            MDBoxLayout:
                id: restaurant_container
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(16)
                size_hint_y: None
                adaptive_height: True

                # 1. Mekan
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail_ankara("images/trilye.jpg", "Trilye Restaurant", "Ankara'nın deniz ürünleriyle ünlü lüks restoranıdır.", "Kazım Özalp Mah. Kuleli Sok. No:32 Gaziosmanpaşa/Ankara", "12:00–23:00")

                    FitImage:
                        source: "images/trilye.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Trilye Restaurant"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Kazım Özalp Mah. Kuleli Sok. No:32 Gaziosmanpaşa/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 2. Mekan
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail_ankara("images/beyzade.jpg", "Beyzade Konağı", "Ankara'nın geleneksel Türk mutfağını sunan otantik restoranı.", "Atpazarı Sk. No:20 Altındağ/Hamamönü", "11:00–22:00")

                    FitImage:
                        source: "images/beyzade.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Beyzade Konağı"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Atpazarı Sk. No:20 Altındağ/Hamamönü"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                # 3. Mekan
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    elevation: 4
                    radius: [12]
                    size_hint_y: None
                    height: self.minimum_height
                    on_release: app.show_food_detail_ankara("images/gozlemeci.jpg", "Hamamönü Gözlemecisi", "Samimi atmosferiyle el yapımı gözlemeleriyle ünlü.", "Sakarya Sk. No:12 Hamamönü/Altındağ", "09:00–20:00")

                    FitImage:
                        source: "images/gozlemeci.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Hamamönü Gözlemecisi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sakarya Sk. No:12 Hamamönü/Altındağ"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

<FoodDetailAnkaraScreen>:
    name: "food_detail_ankara"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1,1,1,1

        MDTopAppBar:
            title: "Yemek Mekanları"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('food_places_ankara')]]
            md_bg_color: "#5C6BC0"  # Soft mavi
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
                    id: food_image_ankara
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
                            id: food_ankara_title
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
                        id: food_description_ankara
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
                            id: food_location_ankara
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
                            id: food_hours_ankara
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
