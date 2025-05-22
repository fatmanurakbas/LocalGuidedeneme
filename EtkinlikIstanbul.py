from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class SocialEventsIstanbulScreen(Screen):
    pass

class EventDetailScreen(Screen):
    pass

Builder.load_string("""
<SocialEventsIstanbulScreen>:
    name: "social_events_ist"
    

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
                    
        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            md_bg_color: "#5C6BC0"
            left_action_items: [["arrow-left", lambda x: app.go_to('istanbul')]]
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
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_istanbul("images/teafest.png", "İstanbul TeaFest 2025", "İkramlar ve dünyanındört bir yanından çay çeşitlerinin bulunacağı bir festival", "Galataport, Karaköy / İstanbul", "12 - 13 Eylül 2025")

                    FitImage:
                        source: "images/teafest.png"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "İstanbul TeaFest 2025"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Galataport, Karaköy / İstanbul"
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
                    on_release: app.show_event_detail_istanbul("images/manifestival.jpg", "MANİFESTİVAL", "Türkiye’nin Yeni Kız Grubu Manifest’ten Dev Eğlence, Bu Yazın Rüyası : MANIFESTIVAL!", "Life Park, Bahçeköy Yeni, Bahçeköy Cd. No:114, 34473 Sarıyer/İstanbul", "28-29 Haziran 2025")

                    FitImage:
                        source: "images/manifestival.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "MANİFESTİVAL"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Life Park, Bahçeköy Yeni, Bahçeköy Cd. No:114, 34473 Sarıyer/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 3. Etkinlik
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_istanbul("images/sergi.webp", "Chiharu Shiota: Dünyalar Arasında", "“Dünyalar Arasında” sergisi, İstanbul’un kozmopolit kimliğiyle sanatçının kendi göç hikâyesinden beslenirken, izleyicilerin kendi yaşamlarını, anılarını ve ilişkilerini daha evrensel bir insanlık tanımı içinde düşünebilecekleri bir tefekkür alanı kurguluyor.", "İstanbul Modern Sanat Müzesi, Kılıçali Paşa, Tophane İskele Cd. No:1/1, 34433 Beyoğlu/İstanbul", "6 Eylül 2024–25 Ocak 2026")

                    FitImage:
                        source: "images/sergi.webp"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Chiharu Shiota: Dünyalar Arasında"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "İstanbul Modern Sanat Müzesi, Kılıçali Paşa, Tophane İskele Cd. No:1/1, 34433 Beyoğlu/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]   
                    
                # 4 Etkinlik
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_istanbul("images/aurora.jpg", "Aurora Konseri", "Norveçli şarkıcı, söz yazarı, dansçı ve müzik yapımcısı AURORA, İstanbul'a geliyor!", "Küçükçiftlik Park, Harbiye, Kadırgalar Cd. No:4, 34367 Şişli/İstanbul", "12 Temmuz 2025")

                    FitImage:
                        source: "images/aurora.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Aurora Konseri"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Küçükçiftlik Park, Harbiye, Kadırgalar Cd. No:4, 34367 Şişli/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 5. Etkinlik
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_istanbul("images/tiyatro.jpg", "Cırcır Böcekleri İtler ve Biz", "İki kardeşin birbirini keşfetme, birbirine dönüşme hikayesi...", "Caddebostan Kültür Merkezi, Caddebostan, Haldun Taner Sk. No:11, 34728 Kadıköy/İstanbul", "25 Mayıs Pazar, 20:00")

                    FitImage:
                        source: "images/tiyatro.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "Cırcır Böcekleri İtler ve Biz"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Caddebostan Kültür Merkezi, Caddebostan, Haldun Taner Sk. No:11, 34728 Kadıköy/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                # 6. Etkinlik
                MDCard:
                    orientation: "vertical"
                    padding: dp(10)
                    spacing: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    radius: [12]
                    elevation: 4
                    on_release: app.show_event_detail_istanbul("images/voleybol.jpg", "FIVB Voleybol Milletler Ligi Kombine 2025", "Filenin Sultanları 2025 Voleybol Milletler Ligi 2.Haftasında İstanbul Sinan Erdem Spor Salonu'nda seyircisiyle buluşuyor!", "Sinan Erdem Spor Salonu, Zuhuratbaba, Ataköy Blv. No:14, 34147 Bakırköy/İstanbul", "18 Haziran 2025, Çarşamba, 12:29")

                    FitImage:
                        source: "images/voleybol.jpg"
                        size_hint_y: None
                        height: dp(200)
                        radius: [12, 12, 0, 0]

                    MDLabel:
                        text: "FIVB Voleybol Milletler Ligi Kombine 2025"
                        font_style: "H6"
                        theme_text_color: "Primary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Sinan Erdem Spor Salonu, Zuhuratbaba, Ataköy Blv. No:14, 34147 Bakırköy/İstanbul"
                        font_style: "Caption"
                        theme_text_color: "Secondary"
                        halign: "left"
                        size_hint_y: None
                        height: self.texture_size[1]
<EventDetailScreen>:
    name: "event_detail"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Etkinlikler"
            elevation: 5
            left_action_items: [["arrow-left", lambda x: app.go_to('social_events_ist')]]
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
                    id: event_image
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
                            id: event_istanbul_title
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
                        id: event_description
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
                            id: event_location
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
                            id: event_hours
                            text: ""
                            font_style: "Caption"
                            theme_text_color: "Secondary"
                            halign: "left"
""")  