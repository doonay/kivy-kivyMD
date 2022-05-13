#Листинг 5.44. Демонстрации работы класса MDDropdownMenu(модуль Menu3.py)
# модуль Menu3.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Меню в MDToolbar'
        left_action_items: [['menu', lambda x: app.callback(x)]]
        right_action_items: [['dots-vertical', lambda x:app.callback_r(x)]]
    MDLabel:
        text: 'Основное окно приложения'
        halign: 'center'
'''
class MainApp(MDApp):
    def build(self):
        # опции меню левой кнопки
        menu_items = [
            {'text': 'Меню левое 1', 'viewclass': 'OneLineListItem', 'on_release': lambda x='Меню левое 1': self.menu_callback(x),},
            {'text': 'Меню левое 2', 'viewclass': 'OneLineListItem', 'on_release': lambda x='Меню левое 2': self.menu_callback(x),},
            {'text': 'Меню левое 3', 'viewclass': 'OneLineListItem', 'on_release': lambda x='Меню левое 3': self.menu_callback(x),},
        ]
        self.menu = MDDropdownMenu(items=menu_items, width_mult=2.5,)
        # опции меню правой кнопки
        menu_items_r = [{'text': 'Меню правое 1',
                         'viewclass': 'OneLineListItem',
                         'on_release': lambda x='Меню правое 1': self.menu_callback_r(x),},
                        {'text': 'Меню правое 2',
                         'viewclass': 'OneLineListItem',
                         'on_release': lambda x='Меню правое 2': self.menu_callback_r(x),},
                        {'text': 'Меню правое 3',
                         'viewclass': 'OneLineListItem',
                         'on_release': lambda x='Меню правое 3': self.menu_callback_r(x),},]
        self.menu_r = MDDropdownMenu(items=menu_items_r, width_mult=2.5,)
        return Builder. load_string(KV)
    # Открыть левое меню ##################
    def callback(self, button):
        self.menu.caller = button
        self.menu. open()
    # Обработка событий левого меню #######
    def menu_callback(self, text_item):
        self.menu. dismiss()
        Snackbar(text=text_item).open()
    # Открыть правое меню #################
    def callback_r(self, button):
        self.menu_r.caller = button
        self.menu_r. open()
    # Обработка событий правого меню #######
    def menu_callback_r(self, text_item):
        self.menu_r. dismiss()
        Snackbar(text=text_item).open()
MainApp().run()