#Листинг 5.54. Демонстрации работы класса MDThemePicker(модуль MDThemePicker.py)
# модуль MDThemePicker1
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. picker import MDThemePicker
KV = '''
MDFloatLayout:
    MDToolbar:
        title: 'Компонента Theme Picker'
        pos_hint: {'top': 1}
        elevation: 10
    MDRaisedButton:
        text: 'Открыть Theme Picker'
        pos_hint: {'center_x':.5, 'center_y':.6}
        on_release: app.show_theme_picker()
    MDLabel:
        id: date_label
        text: 'Итоги смены темы!'
        halign: 'center'
'''
class Main(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog. open()
Main().run()