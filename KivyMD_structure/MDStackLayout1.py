from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDStackLayout:
    padding: '10dp'
    spacing: '10dp'
    #adaptive_height: True
    #adaptive_width: True
    #adaptive_size: True
    MDRaisedButton:
        text: 'КНОПКА 1'
    MDRaisedButton:
        text: 'КНОПКА 2'
    MDRaisedButton:
        text: 'КНОПКА 3'
    MDRaisedButton:
        text: 'КНОПКА 4'
'''

class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)

MainApp().run()