#Листинг 5.78. Демонстрации работы класса MDToolbar (модуль MDToolbar2.py)
# модуль MDToolbar2.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Панель MDToolbar'
        left_action_items: [['menu', lambda x: app.callback()]]
    MDLabel:
        text: 'Содержимое экрана'
        halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def callback(self):
        print('Нажата кнопка меню')
MainApp().run()