#Листинг 5.60. Демонстрации работы класса MDCheckbox (модуль MDCheckbox2.py)
# модуль MDCheckbox2.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
FloatLayout:
    Check:
        active: True
        pos_hint: {'center_x':.4, 'center_y':.5}
    Check:
        pos_hint: {'center_x':.6, 'center_y':.5}
    Check:
        pos_hint: {'center_x':.8, 'center_y':.5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()