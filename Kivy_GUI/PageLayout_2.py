from kivy.lang import Builder
from kivy.app import App

KV = '''
PageLayout:
    BoxLayout:
        Button:
            text: 'Страница 1'
    BoxLayout:
        Button:
            text: 'Страница 2'
    BoxLayout:
        Button:
            text: 'Страница 3'
'''

class MainApp(App):
        def build(self):
            return Builder.load_string(KV)

MainApp().run()