#Листинг 5.77. Демонстрации работы класса MDToolbar (модуль MDToolbar1.py)
# модуль MDToolbar1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Панель MDToolbar'
    MDLabel:
        text: 'Содержимое экрана'
        halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()