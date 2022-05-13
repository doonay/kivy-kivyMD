#Листинг 5.36. Демонстрации работы класса MDIcon (модуль Icon.py)
# модуль Icon
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Класс MDIcon'
        MDIcon:
            #halign: 'center'
            icon: 'language-python'
        MDIcon:
            icon: 'language-python'
            theme_text_color: 'Custom'
            text_color: 1, 0, 0, 1
        MDIcon:
            icon: 'language-python'
            halign: 'center'
            font_size: dp(45)
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()