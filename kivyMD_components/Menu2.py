#Листинг 5.43. Демонстрации работы классаMDDropdownMenu(модуль Menu2.py)
# модуль Menu2.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd. uix. dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
KV = '''
<IconListItem>
    IconLeftWidget:
        icon: root.icon
MDScreen:
    MDGridLayout:
        cols: 1
        MDRaisedButton:
            id: button
            text: 'Открыть меню'
            on_release: app.menu.open()
'''
class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder. load_string(KV)
        menu_items = [{'text': 'Кондиционер',
                       'icon': 'air-conditioner',
                       'viewclass': 'IconListItem',
                       'on_release': lambda x='Меню 1': self.menu_callback(x),},
                      {'text': 'Фильтр',
                       'icon': 'air-filter',
                       'viewclass': 'IconListItem',
                       'on_release': lambda x='Меню 2': self.menu_callback(x),},
                      {'text': 'Насос',
                       'icon': 'air-purifier',
                       'viewclass': 'IconListItem',
                       'on_release': lambda x='Меню 3': self.menu_callback(x),},]
        self.menu = MDDropdownMenu(caller=self.screen.ids.button, items=menu_items, width_mult=3.1,)

    def menu_callback(self, text_item):
        print(text_item)
        dialog = MDDialog(text='Выбрано ' + text_item)
        dialog.open()
        self.menu.dismiss()

    def build(self):
        return self.screen

MainApp().run()