from kivy.app import App
from kivy.lang import Builder

KV = '''
GridLayout:
    cols: 2
    rows: 2
    row_force_default: True
    row_default_height: 40
    Button:
        text: 'Это кнопка 1'
        size_hint_x: None
    Button:
        text: 'Это кнопка 2'
        size_hint:.5,.3
    Button:
        text: 'Это кнопка 3'
        size_hint_x: None
    Button:
        text: 'Это кнопка 4'
        size_hint:.5,.3
'''

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()
