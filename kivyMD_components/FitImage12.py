#Листинг 5.30. Демонстрации работы класса FitImage (модуль FitImage12.py)
# модуль FitImage12.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: 15
    FitImage:
        source: './Images/forest.jpg'
        size_hint_x: None
        size_hint_y: None
        height: '540dp'
        width: '250dp'
        radius: [20, 30, 0, 0,]
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()