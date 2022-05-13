#Листинг 5.81. Демонстрации работы класса MDToolbar (модуль MDToolbar5.py)
# модуль MDToolbar5.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Панель MDToolbar'
        md_bg_color: app.theme_cls.accent_color
        specific_text_color: 0,0,1,1
        elevation: 20
        left_action_items: [['menu', lambda x:app.callback_l()]]
        right_action_items: [['dots-vertical', lambda x: app.callback_r()]]
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
MainApp().run()