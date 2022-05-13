#Листинг 5.46. Демонстрации работы класса MDNavigationDrawer(модуль NaviDrawer1.py)
# модуль NaviDraver1.py
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
# корневой контейнер
Screen:
    # контейнер для размещения элементов навигации
    MDNavigationLayout:
        # менеджер экранов
        ScreenManager:
            # экран приложения
            Screen:
                # контейнер для размещения виджетов
                BoxLayout:
                    orientation: 'vertical'
                    # верхняя панель
                    MDToolbar:
                        title: 'Навигационная панель'
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                    Widget:
                        # выдвижная навигационная панель
                        MDNavigationDrawer:
                            id: nav_drawer
                            # контейнер для виджетов
                            MDFloatLayout:
                                #…элемент 1…#
                                #…элемент 2…#
                                #элемент N…#
'''
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()