# Листинг 5.48. Демонстрации работы класса MDNavigationDrawer(модуль NaviDrawer3.py)
# модуль NaviDraver3.py
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
KV = '''
# Это содержимое навигационной панели
<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineListItem:
                text: 'Экран 1'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current = 'scr 1'
            OneLineListItem:
                text: 'Экран 2'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current = 'scr 2'
            OneLineListItem:
                text: 'Экран 3'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current = 'scr 3'
#Это содержимое основного экрана приложения
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {'top': 1}
        elevation: 10
        title: 'MDNavigationDrawer'
        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
    MDNavigationLayout:
        x: toolbar. height
        ScreenManager:
            id: screen_manager
            # Это содержимое экрана 1
            Screen:
                name: 'scr 1'
                MDLabel:
                    text: 'Открыт экран 1'
                    halign: 'center'
            # Это содержимое экрана 2
            Screen:
                name: 'scr 2'
                MDLabel:
                    text: 'Открыт экран 2'
                    halign: 'center'
            # Это содержимое экрана 3
            Screen:
                name: 'scr 3'
                MDLabel:
                    text: 'Открыт экран 3'
                    halign: 'center'
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
MainApp().run()