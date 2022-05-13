#Листинг 5.55. Демонстрации работы класса MDProgressBar (модуль MDProgressBar1.py)
# модуль MDProgressBar1
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    padding: '10dp'
    MDProgressBar:
        value: 50
    MDProgressBar:
        value: 50
        orientation: 'vertical'
    MDProgressBar:
        value: 50
        color: app.theme_cls.accent_color
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()