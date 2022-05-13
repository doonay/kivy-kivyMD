#Листинг 5.33. Демонстрации работы подкласса SmartTileWithStar(модуль ImageList1.py)
# модуль ImageList1
from kivymd.app import MDApp
from kivy.lang import Builder
KV = '''
<MyTile@SmartTileWithStar>
    size_hint_y: None
    size_hint_x: None
    height: '340dp'
    width: '240dp'
ScrollView:
    MDGridLayout:
        cols: 3
        adaptive_height: True
        adaptive_width: True
        padding: dp(5), dp(5)
        spacing: dp(5)
        MyTile:
            stars: 2
            source: './Images/Carbonara.jpg'
        MyTile:
            stars: 3
            source: './Images/Crudo.jpg'
        MyTile:
            stars: 4
            source: './Images/Margaritta.jpg'
        MyTile:
            stars: 5
            source: './Images/Marinara.jpg'
        MyTile:
            stars: 5
            source: './Images/Carbonara.jpg'
        MyTile:
            stars: 3
            source: './Images/Crudo.jpg'
'''
class MyApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MyApp().run()