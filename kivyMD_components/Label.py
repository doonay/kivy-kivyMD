#Листинг 5.35. Демонстрации работы класса MDLabel (модуль Label.py)
# модуль Label
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Класс MDLabel'
        MDLabel:
            text: 'Текст 1'
        MDLabel:
            text: 'Текст 2'
            theme_text_color: 'Custom'
            text_color: 1, 0, 0, 1
        MDLabel:
            text: 'Текст 3'
            font_size: dp(35)
            halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()