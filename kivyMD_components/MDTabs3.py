#Листинг 5.72. Демонстрации работы класса MDTabs (модуль MDTabs3.py)
# модуль MDTabs3.py
from kivy.lang import Builder
from kivy. uix. floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd. uix. tab import MDTabsBase
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        left_action_items: [['menu', lambda x: x]]
        title: 'Модели платьев'
    MDTabs:
        id: tabs
        on_tab_switch: app. on_tab_switch(*args)
        Tab:
            icon: 'account-check'
            title: 'Флора'
            FitImage:
                source: './Images/Carbonara.jpg'
        Tab:
            icon: 'account-check'
            title: 'Елена'
            FitImage:
                source: './Images/Crudo.jpg'
        Tab:
            icon: 'account-check'
            title: 'Фортуна'
            FitImage:
                source: './Images/Marinara.jpg'
'''
class Tab(FloatLayout, MDTabsBase):
    pass
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, title):
        Snackbar(text='Вкладка-' + title).open()
MainApp().run()