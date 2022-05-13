#Листинг 5.6. Демонстрации работы MDIconButton(модуль IconButton.py)
# модуль IconButton.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDIconButton:
        #icon: 'language-python'
        #icon: './Images/icon.png'
        #user_font_size: '64sp'
        #theme_text_color: 'Custom'
        #text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: print('Кнопка нажата')
        #on_release: print('Кнопка отпущена')
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()