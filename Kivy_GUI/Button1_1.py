from kivy. app import App
from kivy.lang import Builder

KV = '''
Button:
    text: 'Это кнопка'
    size_hint:.5,.5
    pos_hint: {'x':.5, 'y':.5}
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()