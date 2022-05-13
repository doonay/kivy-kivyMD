#Листинг 5.68. Демонстрации работы класса Snackbar (модуль Snackbar2.py)
# модуль Snackbar2.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
KV = '''
Screen:
    MDFloatingActionButton:
        x: root. width - self. width - dp(10)
        y: dp(10)
        on_release: app.snackbar_show()
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def snackbar_show(self):
        Snackbar(text='Это временная панель Snackbar!').open()

MainApp().run()