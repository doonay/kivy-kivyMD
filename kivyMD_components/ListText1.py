#Листинг 5.37. Демонстрации работы класса MDList(модуль ListText1.py)
# модуль ListText1.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = '''
ScrollView:
    MDList:
        id: container
'''

class MainApp(MDApp):
    def build(self):
        return Builder. load_string(KV)
    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f'Однострочный элемент {i}'))
MainApp().run()