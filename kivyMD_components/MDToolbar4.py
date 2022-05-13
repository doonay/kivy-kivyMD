#Листинг 5.80. Демонстрации работы класса MDToolbar (модуль MDToolbar4.py)
# модуль MDToolbar3.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Панель MDToolbar'
        left_action_items: [['menu', lambda x:app.callback_l()]]
        right_action_items: [['dots-vertical', lambda x: app.callback_r()],['clock', lambda x:app.callback_3()]]
    MDLabel:
        text: 'Содержимое экрана'
        halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def callback_l(self):
        print('Нажата левая кнопка меню')
    def callback_r(self):
        print('Нажата правая кнопка меню')
    def callback_3(self):
        print('Нажата кнопка – часы')
MainApp().run()