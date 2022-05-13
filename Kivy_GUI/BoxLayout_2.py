from kivy.app import App
from kivy.lang import Builder

# создание текстовой строки
KV = '''
BoxLayout:
    orientation: 'vertical'
    orientation: 'horizontal'
    Button:
        text: 'Кнопка 1'
        #size_hint: (.5,.3)
        #size_hint: (None,.3)
        #size_hint: (.5, None)
    Button:
        text: 'Кнопка 2'
        #size_hint: (.5,.3)
        #size_hint: (None,.3)
        #size_hint: (.5, None)
'''
class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()
