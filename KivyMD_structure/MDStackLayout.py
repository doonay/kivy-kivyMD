from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDStackLayout:
    adaptive_height: True
    #adaptive_width: True
    #adaptive_size: True
    md_bg_color: app.theme_cls.primary_color
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()