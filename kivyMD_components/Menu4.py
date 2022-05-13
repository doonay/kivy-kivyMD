#Листинг 5.45. Демонстрации работы класса MDDropdownMenu(модуль Menu4.py)
# модуль Menu4.py
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
KV = '''
<IconListItem>
    IconLeftWidget:
        icon: root. icon
MDScreen
    MDTextField:
        id: field
        pos_hint: {'center_x':.35, 'center_y':.7}
        size_hint_x: None
        width: '200dp'
        hint_text: 'Выбор адреса'
        on_focus: if self.focus: app.menu.open()
'''
class IconListItem(OneLineIconListItem):
    icon = StringProperty()
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder. load_string(KV)
        menu_items = [{'viewclass': 'IconListItem',
                       'icon': 'email',
                       'height': dp(36),
                       'text': 'soft_1@mail.ru',
                       'on_release': lambda x='soft_1@mail.ru':
                       self.set_item(x),},
                      {'viewclass': 'IconListItem',
                       'icon': 'email',
                       'height': dp(36),
                       'text': 'soft_2@mail.ru',
                       'on_release': lambda x='soft_2@mail.ru':
                       self.set_item(x),},
                      {'viewclass': 'IconListItem',
                       'icon': 'email',
                       'height': dp(36),
                       'text': 'soft_3@mail.ru',
                       'on_release': lambda x='soft_3@mail.ru':
                       self.set_item(x),}]
        self.menu = MDDropdownMenu(caller=self.screen.ids.field,
               items=menu_items,
               position='bottom',
               # position='center',
               width_mult=3.5,)
    def set_item(self, text__item):
        self.screen.ids.field. text = text__item
        self.menu. dismiss()
    def build(self):
        return self.screen
MainApp().run()