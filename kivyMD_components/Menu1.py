#Листинг 5.42. Демонстрации работы класса MDDropdownMenu(модуль Menu1.py)
# модуль Menu1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd. uix. dialog import MDDialog
KV = '''
MDScreen:
    MDGridLayout:
        cols: 1
        MDRaisedButton:
            id: button
            text: 'Открыть меню'
            on_release: app.menu. open()
'''
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder. load_string(KV)
        menu_items = [{'text': 'Меню 1',
                       'viewclass': 'OneLineListItem',
                       'on_release': lambda x='Меню 1':
                       self.menu_callback(x),},
                      {'text': 'Меню 2',
                       'viewclass': 'OneLineListItem',
                       'on_release': lambda x='Меню 2':
                       self.menu_callback(x),},
                      {'text': 'Меню 3',
                       'viewclass': 'OneLineListItem',
                       'on_release': lambda x='Меню 3':
                       self.menu_callback(x),},]
        self.menu = MDDropdownMenu(caller=self.screen.ids.
                                   button,
                                   items=menu_items,
                                   width_mult=3,)
    def menu_callback(self, text_item):
        dialog = MDDialog(text='Выбрано ' + text_item)
        dialog. open()
        self.menu. dismiss()
    def build(self):
        return self.screen
MainApp().run()