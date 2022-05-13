#Листинг 5.61. Демонстрации работы класса MDSwitch (модуль MDSwitch.py)
# модуль MDSwitch.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text: 'Переключатель 1'
        pos_hint: {'center_x':.5, 'center_y':.5}
    MDSwitch:
        pos_hint: {'center_x':.8, 'center_y':.5}
        on_active: app. switch_active1(self)
    MDLabel:
        text: 'Переключатель 2'
        pos_hint: {'center_x':.5, 'center_y':.4}
    MDSwitch:
        pos_hint: {'center_x':.8, 'center_y':.4}
        width: dp(64)
        on_active: app. switch_active2(self)
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def switch_active1(self, instance):
        print('Переключатель 1, статус -', instance.active)
    def switch_active2(self, instance):
        print('Переключатель 2, статус -', instance.active)
MainApp().run()