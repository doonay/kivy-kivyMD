#Листинг 5.8. Демонстрации работы MDFlatButton(модуль FloatButton.py)
# модуль FlatButton.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDFlatButton:
        text: 'КНОПКА'
        #font_size: '20sp'
        #font_name: 'gothic.ttf'
        #theme_text_color: 'Custom'
        #text_color: 0, 0, 1, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: print('Кнопка нажата')
        #on_release: print('Кнопка отпущена')
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()