#Листинг 5.82. Демонстрации работы класса MDToolbar (модуль MDToolbar6.py)
# модуль MDToolbar6.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: 'Содержимое экрана'
        halign: 'center'
    MDBottomAppBar:
        MDToolbar:
            title: 'Панель'
            icon: 'git'
            type: 'bottom'
            left_action_items: [['menu', lambda x:app.callback_m()]]
            on_action_button: app.callback_i()
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def callback_m(self):
        print('Нажата левая кнопка меню')
    def callback_i(self):
        print('Нажата иконка')
MainApp().run()