from kivy. app import App
from kivy.lang import Builder
# создание текстовой строки
KV = '''
BoxLayout:
    orientation: 'vertical'
    #padding: [50, 50, 50, 50]
    #spacing: 10
    Button:
        text: 'Кнопка 1'
    Button:
        text: 'Кнопка 2'
    Button:
        text: 'Кнопка 3'
    Button:
        text: 'Кнопка 4'
'''
class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()