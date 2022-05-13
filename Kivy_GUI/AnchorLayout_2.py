'''
В этом модуле заданы разные варианты параметров свойства padding
(часть строк закомментировано), и размер кнопки не задан.
'''
from kivy. app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        padding: [100, 100, 100, 100]
        #padding: [10, 100]
        #padding: [40]
    Button:
        text: 'Кнопка'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()