#Листинг 5.84. Демонстрации работы класса MDToolbar (модуль MDToolbar8.py)
# модуль MDToolbar8
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: 'Содержимое экрана'
        halign: 'center'
    MDBottomAppBar:
        md_bg_color: 0, 1, 0, 1
        MDToolbar:
            title: 'Панель'
            icon: 'git'
            type: 'bottom'
            icon_color: 1, 0, 0, 1
            specific_text_color: 0,0,1,1
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