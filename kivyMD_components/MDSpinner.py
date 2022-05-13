#Листинг 5.69. Демонстрации работы класса MDSpinner (модуль MDSpinner.py)
# модуль MDSpinner.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
Screen:
    MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x':.5, 'center_y':.8}
        #determinate: True
        active: True if check.active else False
    MDCheckbox:
        id: check
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x':.5, 'center_y':.4}
        active: True
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()