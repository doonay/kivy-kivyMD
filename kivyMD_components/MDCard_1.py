#Листинг 5.17. Демонстрации работы MDCard(модуль MDCard_1.py)
# модуль MDCard_1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDCard:
        size_hint: None, None
        size: '280dp', '180dp'
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()