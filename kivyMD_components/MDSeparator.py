#Листинг 5.64. Демонстрации работы класса MDSeparator (модуль MDSeparator.py)
# модуль MDSeparator.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    MDSeparator:
    MDRaisedButton:
        text: 'КНОПКА 1'
    MDSeparator:
        color: 1,0,0,1
    MDRaisedButton:
        text: 'КНОПКА 2'
    MDSeparator:
        color: 0,1,0,1
    MDRaisedButton:
        text: 'КНОПКА 3'
    MDSeparator:
        color: 0,0,1,1
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()