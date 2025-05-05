from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class SocialEventsAnkaraScreen(Screen):
    pass

class EventDetailAnkara(Screen):
    pass

Builder.load_string("""
<SocialEventsAnkaraScreen>:
    name: "social_events_ankara"
    
                
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.6, 0.8, 0.9, 1
                    
        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            md_bg_color: 0.1, 0.1, 0.5, 1
            left_action_items: [["arrow-left", lambda x: app.go_to('ankara')]]
            size_hint_y: None
            height: dp(56)
                    
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16) 
                spacing: dp(16)
                size_hint_y: None
                adaptive_height: True

                    
                # 1. Etkinlik
                MDCard:
                    orientation : "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_ankara("images/fantafest.jpg", "Fanta Fest 2025 Ankara", "Gittiği her şehre eğlence götüren Fanta Fest, bu yılda katılımcılarına müzik, eğlence ve birbirinden keyifli aktivitelerle dolu bir festival yaşatacak.", "Atatürk Orman Çiftliği, Yenimahalle / Ankara", "3 Ağustos")

                    FitImage: 
                        source: "images/fantafest.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Fanta Fest 2025 Ankara"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Atatürk Orman Çiftliği, Yenimahalle / Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

<EventDetailAnkara>:
    name: "event_detail_ankara"
                    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.0, 0.2, 0.4, 1
                
        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('social_events_ankara')]]
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
                    id: event_image_ankara
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
                            id: event_title_ankara
                            text: "Etkinlik Adı"
                            font_style: "H5"
                            theme_text_color: "Primary"
                            bold: True
                            halign: "left"
                            size_hint_x: 0.9

                        MDIconButton:
                            icon: "bookmark-outline"
                            pos_hint: {"center_y": 0.5}

                    MDLabel:
                        id: event_description_ankara
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
                        MDLabel:
                            id: event_location_ankara
                            text: "Konum"
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
                            id: event_hours_ankara
                            text: "Çalışma Saatleri"
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
                    """)