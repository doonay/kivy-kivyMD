from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDFloatLayout:
    MDRaisedButton:
        text: 'Это кнопка 1'
    MDRaisedButton:
        text: 'Это кнопка 2'
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDRaisedButton:
        text: 'Это кнопка 3'
        pos_hint: {'center_x': .8, 'center_y':.9}
'''
class MyApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MyApp().run()