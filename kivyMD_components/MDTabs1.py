#Листинг 5.70. Демонстрации работы класса MDTabs (модуль MDTabs1.py)
# модуль MDTabs1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd. uix. tab import MDTabsBase
from kivymd. uix. floatlayout import MDFloatLayout
from kivymd. icon_definitions import md_icons
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Пример Tabs'
    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
<Tab>
    MDIconButton:
        id: icon
        icon: root.icon
        user_font_size: '48sp'
        pos_hint: {'center_x': .5, 'center_y': .5}
'''
class Tab(MDFloatLayout, MDTabsBase):
    '''Класс, реализующий содержимое для tab'''
    pass
class MainApp(MDApp):
    # формирование списка из 15 иконок
    icons = list(md_icons.keys()) [15:30]
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        # формирование заголовков вкладок из иконок
        for tab_name in self. icons:
            self.root.ids.tabs.add_widget(Tab(icon=tab_name))
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''
        Вызывается при переключении вкладок.
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label:
            <kivymd.uix.tab.MDTabsLabelobject>;
        :param tab_text: text or name icon of tab;
        '''
        # получение иконки вкладки
        count_icon = instance_tab.icon
        # печать сведений о текущей вкладке
        print(f'Загружена вкладка - {count_icon}', Tab)
MainApp().run()