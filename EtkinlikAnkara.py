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
        md_bg_color: 1, 1, 1, 1
                    
        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            md_bg_color:"#5C6BC0"
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
                    
                # 2. Etkinlik
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_ankara("images/bale.png", "The Imperial Russian Ballet Company Swan Lake-Kuğu Gölü Balesi", "Swan Lake-Kuğu Gölü Balesi'nde aşk, ihanet ve dönüşüm temalarını işleyen bir hikaye anlatılır.", "Oran Açık Hava Sahnesi, Oran, Kudüs Cd. 26 - 1, 6550 Çankaya/Ankara", "21 Haziran 2025 Cumartesi, 21:00")

                    FitImage: 
                        source: "images/bale.png"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "The Imperial Russian Ballet Company / Swan Lake-Kuğu Gölü Balesi"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Oran Açık Hava Sahnesi, Oran, Kudüs Cd. 26 - 1, 06550 Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 3. Etkinlik
                MDCard:
                    orientation : "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_ankara("images/dans.jpg", "Aleksandrov Rus Kızılordu Korosu ve Dans Topluluğu", "Dünyanın en eski ve en büyük korolarından biri olan Aleksandrov Rus Kızılordu Korosu büyüleyici Rus, Türk müzikleri ile dansın ritmiyle buluşacak benzersiz performansıyla, izleyenlere eşsiz bir deneyim yaşatmaya hazırlanıyor.", "Oran Açık Hava Sahnesi, Oran, Kudüs Cd. 26 - 1, 06550 Çankaya/Ankara", "28 Mayıs Çarşamba, 20:30")

                    FitImage: 
                        source: "images/dans.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Aleksandrov Rus Kızılordu Korosu ve Dans Topluluğu"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Oran Açık Hava Sahnesi, Oran, Kudüs Cd. 26 - 1, 06550 Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 4. Etkinlik
                MDCard:
                    orientation : "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_ankara("images/hande.jpg", "Hande Yener Konseri", "Hande Yener, muhteşem sahne performansı ve hit şarkılarıyla Jolly Joker sahnesinde!", "Jolly Joker Ankara,  Kavaklıdere, Kızılırmak Cd. No:14, 06420 Çankaya/Ankara", "30 Mayıs Cuma, 21:00")

                    FitImage: 
                        source: "images/hande.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Hande Yener Konseri"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "Jolly Joker Ankara,  Kavaklıdere, Kızılırmak Cd. No:14, 06420 Çankaya/Ankara"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 5.Etkinlik
                MDCard:
                    orientation : "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_ankara("images/frida.jpg", "Kökler ve İzler - Frida Kahlo", "Kökler ve İzler, Frida Kahlo’nun yalnızca tablolarında değil, onu besleyen köklerde saklı izlerini takip eden sürükleyici bir deneyimdir.", "FLOW Digital Theatre", "23 Mayıs Cuma, 14:00")

                    FitImage: 
                        source: "images/frida.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Kökler ve İzler - Frida Kahlo"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                    MDLabel:
                        text: "FLOW Digital Theatre"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 6. Etkinlik
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
        md_bg_color: 1, 1, 1, 1
                
        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('social_events_ankara')]]
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
                            id: event_ankara_title
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
                        id: event_description_ankara
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
                            id: event_location_ankara
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
                            id: event_hours_ankara
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
                    """)