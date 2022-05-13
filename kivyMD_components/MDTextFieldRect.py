#Листинг 5.75. Демонстрации работы класса MDTextFieldRect(модуль MDTextFieldRect.py)
# модуль MDTextFieldRect.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTextFieldRect:
        size_hint: 1, None
        hint_text: 'Высота рамки 30'
        height: '30dp'
    MDTextFieldRect:
        size_hint: 1, None
        hint_text: 'Высота рамки 60'
        height: '60dp'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()