from kivy.app import App
from kivy.lang import Builder

KV = '''
Widget:
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()