from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDRaisedButton:
        text: 'Светлый оттенок'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        md_bg_color: app.theme_cls.primary_light
    MDRaisedButton:
        text: 'Базовый цвет'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDRaisedButton:
        text: 'Темный оттенок'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        md_bg_color: app.theme_cls.primary_dark
'''
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Green'
        return Builder. load_string(KV)
MainApp().run()