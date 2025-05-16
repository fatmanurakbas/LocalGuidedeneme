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

class FoodPlacesScreen(Screen):
    restaurants = ListProperty([])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api = FoursquareAPI()
        Clock.schedule_once(self.load_restaurants)

    def load_restaurants(self, dt):
        results = self.api.search_places(
            query="restaurant",
            near="Istanbul, Turkey",
            category="restaurant",
            limit=20
        )
        
        if results and 'results' in results:
            self.places = results['results']
            self.update_ui()

    def update_ui(self):
        container = self.ids.place_container
        container.clear_widgets()
        
        for restaurant in self.places:
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
                source=restaurant.get('photos', [{}])[0].get('prefix', '') + 
                      '300x200' + 
                      restaurant.get('photos', [{}])[0].get('suffix', ''),
                size_hint_y=None,
                height=dp(200),
                radius=[12, 12, 0, 0]
            )
            
            # İsim
            name_label = MDLabel(
                text=restaurant.get('name', ''),
                font_style="H6",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height=dp(30)
            )
            
            # Adres
            address_label = MDLabel(
                text=restaurant.get('location', {}).get('formatted_address', ''),
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
            card.bind(on_release=lambda x, r=restaurant: self.show_restaurant_detail(r))
            
            container.add_widget(card)

    def show_restaurant_detail(self, restaurant):
        app = MDApp.get_running_app()
        app.show_food_detail(
            restaurant.get('photos', [{}])[0].get('prefix', '') + 
            '800x600' + 
            restaurant.get('photos', [{}])[0].get('suffix', ''),
            restaurant.get('name', ''),
            restaurant.get('description', '') or 'Detaylı bilgi için mekanı ziyaret edin.',
            restaurant.get('location', {}).get('formatted_address', ''),
            restaurant.get('hours', {}).get('display', 'Çalışma saatleri bilgisi mevcut değil.')
        )

class FoodDetailScreen(Screen):
    pass

Builder.load_string("""
<FoodPlacesScreen>:
    name: "food_places"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.2, 0.4, 0.8, 1
        MDTopAppBar:
            title: "Yemek Mekanları"
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

<FoodDetailScreen>:
    name: "food_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1

        MDTopAppBar:
            title: "Yemek Mekanları"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('food_places')]]
            md_bg_color: 0.2, 0.4, 0.8, 1
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
                    id: food_image
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
                            id: food_istanbul_title
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
                        id: food_description
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
                            id: food_location
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
                            on_release: app.konuma_git(self.text)  # Tıklanınca adresi yolla

                    MDBoxLayout:
                        spacing: dp(6)
                        size_hint_y: None
                        height: dp(24)

                        MDIcon:
                            icon: "clock-outline"
                            theme_text_color: "Secondary"
                        MDLabel:
                            id: food_hours
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")
