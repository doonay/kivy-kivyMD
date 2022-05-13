#Листинг 5.59. Демонстрации работы класса MDCheckbox (модуль MDCheckbox1.py)
# модуль MDCheckbox1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDGridLayout:
        cols:2
        spacing: 2
        MDLabel:
            size_hint_x: None
            text: 'Флажок 1'
        MDCheckbox:
            size_hint_x: None
            size: '48dp', '48dp'
            on_active: app. on_checkbox_1(*args)
        MDLabel:
            size_hint_x: None
            text: 'Флажок 2'
        MDCheckbox:
            size_hint_x: None
            size: '48dp', '48dp'
            on_active: app. on_checkbox_2(*args)
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_checkbox_1(self, checkbox, value):
        if value:
            print('Флажок 1 – активный')
        else:
            print('Флажок 1 – пассивный')
    def on_checkbox_2(self, checkbox, value):
        if value:
            print('Флажок 2 – активный')
        else:
            print('Флажок 2 – пассивный')
MainApp().run()