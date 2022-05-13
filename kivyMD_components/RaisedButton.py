#Листинг 5.9. Демонстрации работы MDRaisedButton (модуль RaisedButton.py)
# модуль RaisedButton.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDRaisedButton:
        text: 'КНОПКА'
        #md_bg_color: 1, 0, 1, 1
        #font_size: '25sp'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: print('Кнопка нажата')
        #on_release: print('Кнопка отпущена')
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()