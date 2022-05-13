#Листинг 5.31. Демонстрации работы класса Image(модуль Image.py)
# модуль Image.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: 15
    Image:
        source: './Images/forest.jpg'
        size: self. texture_size
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()