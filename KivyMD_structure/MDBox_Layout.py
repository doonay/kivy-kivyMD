from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        #adaptive_height: True
        #adaptive_width: True
        adaptive_size: True
        pos_hint: {'center_x':.5, 'center_y':.5}
        MDRaisedButton:
            text: 'Это кнопка'
'''
class MyApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MyApp().run()