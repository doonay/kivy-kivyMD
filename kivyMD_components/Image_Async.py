#Листинг 5.32. Демонстрации работы класса AsyncImage(модуль Image_Async.py)
# модуль Image_Async.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: 15
    AsyncImage:
        source: 'https://kivy.org/logos/kivy-logo-black-64.png'
        size: self. texture_size
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()