#Листинг 5.34. Демонстрации работы подкласса SmartTileWithLabel(модуль ImageList2.py)
# модуль ImageList2.py
from kivymd.app import MDApp
from kivy.lang import Builder
KV = '''
<MyTile@SmartTileWithLabel>
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
            source: './Images/Carbonara.jpg'
            text:' [size=26] Платье - "Баллон" [/size][size=14]Carbonara.jpg [/size]'
        MyTile:
            source: './Images/Crudo.jpg'
            text:' [size=26] Платье - "Crudo" [/size][size=14]Crudo.jpg [/size]'
            tile_text_color: app.theme_cls.accent_color
        MyTile:
            source: './Images/Margaritta.jpg'
            text:' [size=26] Платье - "Флора" [/size][size=14]Margaritta.jpg [/size]'
        MyTile:
            source: './Images/Marinara.jpg'
            text:' [size=26] Платье - "Фортуна" [/size][size=14]Marinara.jpg [/size]'
        MyTile:
            source: './Images/Ganna.jpg'
            text:' [size=26] Платье - "Жанна" [/size][size=14]Ganna.jpg [/size]'
        MyTile:
            source: './Images/Gorox.jpg'
            text:' [size=26] Платье - "Горох" [/size][size=14]Gorox.jpg [/size]'
'''
class MyApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MyApp().run()