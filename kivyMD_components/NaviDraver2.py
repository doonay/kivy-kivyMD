#Листинг 5.47. Демонстрации работы класса MDNavigationDrawer(модуль NaviDrawer2.py)
# модуль NaviDraver2.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Навигационная панель'
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        Widget:
        MDNavigationDrawer:
            id: nav_drawer
            # Здесь будет отображаться содержимое панели
            MDScreen:
                MDFloatLayout:
                    MDLabel:
                        text: 'Заголовок'
                        pos_hint: {'center_x': .8,'center_y': .9}
                    MDLabel:
                        text: 'Контент 1'
                        pos_hint: {'center_x': .55,'center_y': .8}
                    MDLabel:
                        text: 'Контент 2'
                        pos_hint: {'center_x': .55,'center_y': .7}
                    MDLabel:
                        text: 'Контент 3'
                        pos_hint: {'center_x': .55,'center_y': .6}
'''
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()