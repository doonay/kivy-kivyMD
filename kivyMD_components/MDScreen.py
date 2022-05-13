#Листинг 5.58. Демонстрации работы класса MDScreen (модуль MDScreen.py)
# модуль MDScreen.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    radius: [25, 25, 25, 25]
    md_bg_color: app.theme_cls.primary_color
    MDRelativeLayout:
        orientation: 'vertical'
        MDRaisedButton:
            text: 'КНОПКА'
            pos_hint: {'center_x':.5, 'center_y':.5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()