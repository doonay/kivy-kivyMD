#Листинг 5.83. Демонстрации работы класса MDToolbar (модуль MDToolbar7.py)
# модуль MDToolbar7.py
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
            #mode: 'free-end'
            #mode: 'free-center'
            #mode: 'end'
            #mode: 'center'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def callback_m(self):
        print('Нажата левая кнопка меню')
    def callback_i(self):
        print('Нажата иконка')
MainApp().run()