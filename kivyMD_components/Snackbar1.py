#Листинг 5.67. Демонстрации работы класса Snackbar (модуль Snackbar1.py)
# модуль Snackbar.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
#:import Snackbar kivymd.uix.snackbar.Snackbar
Screen:
    MDRaisedButton:
        text: 'Открыть Snackbar'
        on_release: Snackbar(text='Это временная панель Snackbar!').open()
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()