from kivy. app import App
from kivy.lang import Builder
# создание текстовой строки
KV = '''
FloatLayout:
    Button:
        text: 'Кнопка'
        size_hint:.3,.2
        pos: 30, 30
'''
class MyApp(App):
    def build (self):
        return Builder.load_string(KV)

MyApp().run()