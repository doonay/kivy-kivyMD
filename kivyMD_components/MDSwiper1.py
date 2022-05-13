#Листинг 5.41. Демонстрации работы класса MDSwiper (модуль MDSwiper1.py)
# модуль MDSwiper1.py
from kivymd.app import MDApp
from kivy.lang. builder import Builder
kv = '''
<MagicButton@MagicBehavior+MDIconButton>
MDScreen:
    MDToolbar:
        id: toolbar
        title: 'Пример MDSwiper'
        elevation: 10
        pos_hint: {'top': 1}
    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(20)
        y: root.height - self. height - toolbar.height - dp(10)
        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: './Images/Crudo.jpg'
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: '12dp'
                MagicButton:
                    id: icon
                    icon: 'weather-sunny'
                    user_font_size: '56sp'
                    on_press: print('Нажата кнопка Crudo')
                MDLabel:
                    text: 'Пицца Crudo'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]
                    pos_hint: {'center_y': .5}
        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: './Images/Carbonara.jpg'
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: '12dp'
                MagicButton:
                    id: icon
                    icon: 'weather-sunny'
                    user_font_size: '56sp'
                    on_press: print('Нажата кнопка Фортуна')
                MDLabel:
                    text: 'Платье Фортуна'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self. texture_size[1]
                    pos_hint: {'center_y': .5}
        MDSwiperItem:
            RelativeLayout:
                FitImage:
                    source: './Images/Gorox.jpg'
                    radius: [10,]
                MDBoxLayout:
                    adaptive_height: True
                    spacing: '12dp'
                    MagicButton:
                        id: icon
                        icon: 'weather-sunny'
                        user_font_size: '56sp'
                        on_press: print('Нажата кнопка Горох')
                MDLabel:
                    text: 'Платье Горох'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self. texture_size[1]
                    pos_hint: {'center_y': .5}
'''
class Main(MDApp):
    def build(self):
        return Builder. load_string(kv)
Main().run()