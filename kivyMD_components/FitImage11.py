#Листинг 5.29. Демонстрации работы класса FitImage (модуль FitImage11.py)
# модуль FitImage11.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: 15
    FitImage:
        source: './Images/forest.jpg'
        size_hint_x: 1
        size_hint_y: 1
        radius: [20, 30, 0, 0,]
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()