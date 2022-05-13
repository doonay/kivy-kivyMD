#Листинг 5.7. Демонстрации работы MDFloatingActionButton (модуль FloatActButton.py)
# модуль FloatActButton.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDFloatingActionButton:
        icon: 'microphone'
        elevation: 20
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: print('Кнопка нажата')
        #on_release: print('Кнопка отпущена')
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()