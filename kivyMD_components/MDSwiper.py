# Листинг 5.40. Демонстрации работы класса MDSwiper (модуль MDSwiper.py)
# модуль MDSwiper.py
from kivymd.app import MDApp
from kivy.lang. builder import Builder

kv = '''
MDScreen:
    MDToolbar:
        id: toolbar
        title: 'Пример MDSwiper'
        elevation: 10
        pos_hint: {'top': 1}
    MDSwiper:
        size_hint_y: None
        height: root. height - toolbar.height - dp (20)
        y: root. height - self. height - toolbar.height - dp (10)
        MDSwiperItem:
            FitImage:
                source: './Images/Ballon.jpg'
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: './Images/Elena.jpg'
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: './Images/Flora.jpg'
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: './Images/Fortuna.jpg'
                radius: [10,]
        MDSwiperItem:
            FitImage:
                source: './Images/Gorox.jpg'
                radius: [10,]
'''

class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)
Main().run()