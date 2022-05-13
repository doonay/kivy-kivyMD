from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDRelativeLayout:
        MDRaisedButton:
            text: 'КНОПКА 1'
        MDRaisedButton:
            text: 'КНОПКА 2'
            pos_hint: {'center_x':.5, 'center_y':.5}
        MDRaisedButton:
            text: 'КНОПКА 3'
            pos_hint: {'x': 0.1, 'y': 0.8}
'''

class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)

MainApp().run()